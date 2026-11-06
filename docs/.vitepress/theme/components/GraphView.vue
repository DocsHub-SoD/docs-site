<script setup>
import { onMounted, onBeforeUnmount, ref, computed } from 'vue'

const container = ref(null)
const loading = ref(true)
const selectedNode = ref(null)
const hideOrphans = ref(false)
const searchQuery = ref('')
const searchMatchCount = ref(0)
const currentZoom = ref(1.0)

const CATEGORIES = [
  { id: 'Combat & Abilities', label: 'Combat & Abilities', color: '#ef4444' },
  { id: 'Actors & Entities', label: 'Actors & Entities', color: '#22c55e' },
  { id: 'Managers & Systems', label: 'Managers & Systems', color: '#3b82f6' },
  { id: 'Buffs & Statuses', label: 'Buffs & Statuses', color: '#a855f7' },
  { id: 'Items & Economy', label: 'Items & Economy', color: '#eab308' },
  { id: 'User Interface', label: 'User Interface', color: '#ec4899' },
  { id: 'Networking', label: 'Networking', color: '#06b6d4' },
  { id: 'Data & Core Math', label: 'Data & Core Math', color: '#f97316' },
  { id: 'Miscellaneous & Utility', label: 'Misc & Utility', color: '#64748b' }
]

const CATEGORY_COLORS = Object.fromEntries(CATEGORIES.map(c => [c.id, c.color]))
const selectedCategories = ref(new Set(CATEGORIES.map(c => c.id)))

const isFilterModified = computed(() => {
  return selectedCategories.value.size < CATEGORIES.length
})

function formatCategory(cat) {
  if (cat === 'Miscellaneous & Utility') return 'Misc & Utility'
  return cat || 'Unknown'
}

let graphInstance = null
let rawData = null
let hoveredNode = null
let highlightNodes = new Set()
let highlightLinks = new Set()
let matchedQueryIds = new Set()

// Input & gesture tracking
let isCtrlPressed = false
let isPanning = false
let isNodeDragging = false
let suppressClickUntil = 0
let panStart = { x: 0, y: 0 }

function hexToRgba(hex, alpha) {
  if (!hex || hex[0] !== '#') return `rgba(140, 150, 170, ${alpha})`
  const r = parseInt(hex.slice(1, 3), 16)
  const g = parseInt(hex.slice(3, 5), 16)
  const b = parseInt(hex.slice(5, 7), 16)
  return `rgba(${r}, ${g}, ${b}, ${alpha})`
}

onMounted(async () => {
  if (typeof window === 'undefined') return

  if (!window.ForceGraph) {
    await new Promise((resolve, reject) => {
      const script = document.createElement('script')
      script.src = 'https://unpkg.com/force-graph@1.43.5/dist/force-graph.min.js'
      script.onload = resolve
      script.onerror = reject
      document.head.appendChild(script)
    })
  }

  const res = await fetch('/graph-data.json')
  rawData = await res.json()
  loading.value = false

  initPrecomputedGraph()
})

onBeforeUnmount(() => {
  if (graphInstance) graphInstance._destructor?.()
})

function getFilteredData() {
  if (!rawData) return { nodes: [], links: [] }

  let nodes = rawData.nodes
    .filter(n => (!hideOrphans.value || !n.isOrphan))
    .filter(n => selectedCategories.value.has(n.category))
    .map(n => ({
      ...n,
      // Fully precomputed frozen positions: ZERO physics compute on client!
      fx: n.x,
      fy: n.y
    }))

  const nodeMap = new Set(nodes.map(n => n.id))
  const links = rawData.links
    .filter(l => {
      const s = typeof l.source === 'object' ? l.source.id : l.source
      const t = typeof l.target === 'object' ? l.target.id : l.target
      return nodeMap.has(s) && nodeMap.has(t)
    })
    .map(l => ({
      source: typeof l.source === 'object' ? l.source.id : l.source,
      target: typeof l.target === 'object' ? l.target.id : l.target,
      type: l.type
    }))

  return { nodes, links }
}

function initPrecomputedGraph() {
  if (!container.value) return

  const elem = container.value
  elem.innerHTML = ''

  window.addEventListener('resize', () => {
    if (graphInstance) {
      graphInstance.width(elem.clientWidth)
      graphInstance.height(elem.clientHeight)
    }
  })

  // 100% Deterministic Render: physics simulation is turned off completely!
  graphInstance = ForceGraph()(elem)
    .width(elem.clientWidth)
    .height(elem.clientHeight)
    .nodeId('id')
    .nodeLabel(n => `${n.name}\n[${formatCategory(n.category)}]`)
    .nodeColor(n => n.color)
    .nodeVal(n => Math.max(n.val || 2.5, 2.5))
    .backgroundColor('#090c10')
    .d3AlphaDecay(1)
    .d3VelocityDecay(1)
    .cooldownTicks(0)
    .autoPauseRedraw(false) // Continuous rendering loop: instant reactivity on click/esc without canvas move!
    .enableNodeDrag(true) // User can reposition nodes if desired
    .enablePanInteraction(false) // Disable left-click canvas pan
    .enableZoomInteraction(true) // Keep mouse wheel zoom
    .minZoom(0.3)
    .maxZoom(3.0)
    .onZoom(({ k }) => {
      currentZoom.value = Math.max(0.3, Math.min(3.0, Math.round(k * 100) / 100))
    })
    .onNodeDrag(node => {
      isNodeDragging = true
      suppressClickUntil = Date.now() + 400
    })
    .onNodeDragEnd(node => {
      node.fx = node.x
      node.fy = node.y
      setTimeout(() => { isNodeDragging = false }, 150)
      triggerRedraw()
    })
    .linkWidth(l => {
      if (highlightLinks.has(l)) return 2.5
      if (selectedNode.value || hoveredNode) return 0.5
      return 0.85
    })
    .linkColor(l => {
      if (highlightLinks.has(l)) return 'rgba(255, 255, 255, 0.95)'
      if (selectedNode.value || (hoveredNode && !isPanning)) return 'rgba(70, 80, 100, 0.025)' // Super subtle when a node is selected or hovered
      return 'rgba(120, 130, 160, 0.15)'
    })
    .linkDirectionalParticles(l => highlightLinks.has(l) ? 3 : 0)
    .linkDirectionalParticleSpeed(0.007)
    .onNodeHover(node => {
      if (isPanning || isNodeDragging) return
      hoveredNode = node
      if (!selectedNode.value) {
        updateHighlights(node)
        triggerRedraw()
      }
    })
    .onNodeClick((node, event) => {
      // ONLY Left Mouse Button (button 0) without modifier keys
      if (event) {
        if (event.button !== 0) return
        if (event.ctrlKey || event.metaKey || event.shiftKey || event.altKey) return
      }
      if (isNodeDragging || isPanning || isCtrlPressed || Date.now() < suppressClickUntil) return
      setSelectedNode(node)
    })
    .onBackgroundClick(event => {
      if (event) {
        if (event.button !== 0) return
        if (event.ctrlKey || event.metaKey || event.shiftKey || event.altKey) return
      }
      if (isNodeDragging || isPanning || isCtrlPressed || Date.now() < suppressClickUntil) return
      clearSelection()
    })
    .nodeCanvasObject((node, ctx, globalScale) => {
      if (!Number.isFinite(node.x) || !Number.isFinite(node.y)) return

      // Viewport Frustum Culling: skip drawing off-screen nodes for 60fps performance
      const center = graphInstance?.centerAt?.()
      const w = container.value ? container.value.clientWidth : 1000
      const h = container.value ? container.value.clientHeight : 700
      const halfW = w / (2 * globalScale) + 60
      const halfH = h / (2 * globalScale) + 60
      if (center) {
        if (Math.abs(node.x - center.x) > halfW || Math.abs(node.y - center.y) > halfH) {
          return
        }
      }

      const isSearched = matchedQueryIds.size > 0
      const isMatch = matchedQueryIds.has(node.id)
      const isSelected = selectedNode.value && selectedNode.value.id === node.id
      const isHighlighted = highlightNodes.has(node.id)
      const isDimmed = (highlightNodes.size > 0 && !isHighlighted) || (isSearched && !isMatch)

      const r = Math.max(Math.sqrt(node.val || 2.5) * 2.2, 3.5)

      ctx.beginPath()
      ctx.arc(node.x, node.y, r, 0, 2 * Math.PI, false)
      ctx.fillStyle = isDimmed ? hexToRgba(node.color, 0.25) : node.color
      ctx.fill()

      // Wildcard Search Match: Neon Beacon
      if (isMatch) {
        ctx.lineWidth = 2.5
        ctx.strokeStyle = '#38bdf8'
        ctx.stroke()

        ctx.beginPath()
        ctx.arc(node.x, node.y, r + 4, 0, 2 * Math.PI, false)
        ctx.strokeStyle = 'rgba(56, 189, 248, 0.6)'
        ctx.lineWidth = 1.2
        ctx.stroke()
      }

      // Active Selection: Gold Halo
      if (isSelected) {
        ctx.lineWidth = 2.8
        ctx.strokeStyle = '#fbbf24'
        ctx.stroke()

        ctx.beginPath()
        ctx.arc(node.x, node.y, r + 5, 0, 2 * Math.PI, false)
        ctx.strokeStyle = 'rgba(251, 191, 36, 0.7)'
        ctx.lineWidth = 1.5
        ctx.stroke()
      } else if (isHighlighted) {
        ctx.lineWidth = 1.8
        ctx.strokeStyle = '#fff'
        ctx.stroke()
      }

      // Hierarchical LOD Labeling:
      // High-importance nodes (val=16) appear earlier (zoom >= 0.75)
      // Lower-importance nodes gradually appear as user zooms in
      // All nodes visible once zoom reaches ~2.0x
      // Hover, selection, or search matches ALWAYS show label
      const minScaleRequired = Math.max(0.75, 2.35 - (node.val || 2.5) * 0.11)
      const isLodVisible = globalScale >= minScaleRequired
      const shouldShowLabel = isHighlighted || isSelected || isMatch || isLodVisible

      if (shouldShowLabel && !isDimmed) {
        const fontSize = Math.max(10 / globalScale, 4.5)
        ctx.font = `${isMatch || isSelected ? '600 ' : ''}${fontSize}px -apple-system, sans-serif`
        ctx.textAlign = 'center'
        ctx.textBaseline = 'top'
        ctx.fillStyle = isSelected ? '#fbbf24' : (isMatch ? '#38bdf8' : (isHighlighted ? '#ffffff' : 'rgba(235, 240, 255, 0.9)'))
        ctx.fillText(node.name, node.x, node.y + r + 2.5)
      }
    })

  setupNavigationControls(elem)
  applyDataToGraph(true)
}

function applyDataToGraph(shouldRecenter = false) {
  if (!graphInstance) return
  const data = getFilteredData()
  graphInstance.graphData(data)
  if (shouldRecenter) {
    setTimeout(() => {
      graphInstance?.zoomToFit(500, 40)
    }, 100)
  }
}

function triggerRedraw() {
  if (graphInstance) {
    graphInstance.nodeColor(graphInstance.nodeColor())
    graphInstance.linkColor(graphInstance.linkColor())
    graphInstance.linkWidth(graphInstance.linkWidth())
  }
}

function updateHighlights(targetNode) {
  highlightNodes.clear()
  highlightLinks.clear()

  if (targetNode) {
    highlightNodes.add(targetNode.id)
    const data = graphInstance.graphData()
    data.links.forEach(l => {
      const s = typeof l.source === 'object' ? l.source.id : l.source
      const t = typeof l.target === 'object' ? l.target.id : l.target
      if (s === targetNode.id || t === targetNode.id) {
        highlightLinks.add(l)
        highlightNodes.add(s)
        highlightNodes.add(t)
      }
    })
  }
}

function setSelectedNode(node) {
  if (selectedNode.value && selectedNode.value.id === node.id) {
    clearSelection()
    return
  }
  selectedNode.value = node
  updateHighlights(node)
  triggerRedraw()
}

function clearSelection() {
  selectedNode.value = null
  highlightNodes.clear()
  highlightLinks.clear()
  triggerRedraw()
}

function setupNavigationControls(elem) {
  // Prevent browser autoscroll when middle-clicking
  elem.addEventListener('auxclick', e => {
    if (e.button === 1) {
      e.preventDefault()
    }
  })

  const startPan = e => {
    // Middle click (button 1) OR Ctrl + Left click (button 0 + ctrlKey / isCtrlPressed)
    if (e.button === 1 || (e.button === 0 && (e.ctrlKey || isCtrlPressed))) {
      isPanning = true
      suppressClickUntil = Date.now() + 600
      panStart = { x: e.clientX, y: e.clientY }
      elem.classList.add('canvas-panning', 'is-dragging')
      if (!selectedNode.value) {
        hoveredNode = null
        highlightNodes.clear()
        highlightLinks.clear()
        triggerRedraw()
      }
      e.preventDefault()
    }
  }

  elem.addEventListener('pointerdown', startPan)
  elem.addEventListener('mousedown', startPan)

  const onPanMove = e => {
    if (!isPanning || !graphInstance) return

    const dx = e.clientX - panStart.x
    const dy = e.clientY - panStart.y

    panStart = { x: e.clientX, y: e.clientY }
    suppressClickUntil = Date.now() + 600

    const currentPos = graphInstance.centerAt()
    const zoom = graphInstance.zoom()
    if (currentPos && Number.isFinite(zoom) && zoom > 0) {
      graphInstance.centerAt(currentPos.x - dx / zoom, currentPos.y - dy / zoom)
    }
  }

  window.addEventListener('pointermove', onPanMove, { passive: true })
  window.addEventListener('mousemove', onPanMove, { passive: true })

  const endPan = e => {
    if (isPanning) {
      isPanning = false
      suppressClickUntil = Date.now() + 400
      elem.classList.remove('is-dragging')
      if (!isCtrlPressed) elem.classList.remove('canvas-panning')
      if (!selectedNode.value) {
        hoveredNode = null
        highlightNodes.clear()
        highlightLinks.clear()
        triggerRedraw()
      }
      if (e.button === 1) {
        e.preventDefault()
      }
    }
  }

  window.addEventListener('pointerup', endPan)
  window.addEventListener('mouseup', endPan)

  window.addEventListener('keydown', e => {
    if (e.key === 'Control') {
      isCtrlPressed = true
      elem.classList.add('canvas-panning')
    }
    if (e.key === 'Escape') {
      clearSelection()
      if (searchQuery.value) {
        searchQuery.value = ''
        matchedQueryIds.clear()
        searchMatchCount.value = 0
      }
      document.getElementById('graph-quick-search')?.blur()
      triggerRedraw()
      return
    }

    // Direct search typing on keyboard without clicking input
    const searchEl = document.getElementById('graph-quick-search')
    if (document.activeElement !== searchEl && e.key.length === 1 && !e.ctrlKey && !e.altKey && !e.metaKey) {
      searchEl?.focus()
    }
  })

  window.addEventListener('keyup', e => {
    if (e.key === 'Control') {
      isCtrlPressed = false
      if (!isPanning) {
        elem.classList.remove('canvas-panning', 'is-dragging')
      }
    }
  })
}

function onSearchInput() {
  const q = searchQuery.value.toLowerCase().trim()
  matchedQueryIds.clear()

  if (!q) {
    searchMatchCount.value = 0
  } else {
    rawData.nodes.forEach(n => {
      if (n.name.toLowerCase().includes(q)) {
        matchedQueryIds.add(n.id)
      }
    })
    searchMatchCount.value = matchedQueryIds.size
  }
  triggerRedraw()
}

function toggleCategory(catId) {
  const next = new Set(selectedCategories.value)
  if (next.has(catId)) {
    next.delete(catId)
  } else {
    next.add(catId)
  }
  selectedCategories.value = next
  applyDataToGraph(false)
}

function resetFilters() {
  selectedCategories.value = new Set(CATEGORIES.map(c => c.id))
  applyDataToGraph(false)
}

function toggleOrphans() {
  hideOrphans.value = !hideOrphans.value
  applyDataToGraph(false)
}

function recenterCamera() {
  graphInstance?.zoomToFit(500, 40)
}

function zoomIn() {
  if (!graphInstance) return
  const next = Math.min(3.0, currentZoom.value * 1.25)
  graphInstance.zoom(next, 250)
  currentZoom.value = Math.round(next * 100) / 100
}

function zoomOut() {
  if (!graphInstance) return
  const next = Math.max(0.3, currentZoom.value / 1.25)
  graphInstance.zoom(next, 250)
  currentZoom.value = Math.round(next * 100) / 100
}

function zoomReset() {
  if (!graphInstance) return
  graphInstance.zoom(1.0, 300)
  currentZoom.value = 1.0
}

function onZoomSlider(e) {
  if (!graphInstance) return
  const val = parseFloat(e.target.value)
  currentZoom.value = val
  graphInstance.zoom(val)
}
</script>

<template>
  <div class="graph-page-wrapper">
    <!-- Top Bar -->
    <div class="graph-top-row">
      <div class="title-meta">
        <h1 class="graph-heading">Interactive Topology Map</h1>
        <p class="graph-subheading">
          Visual map of game systems, cross-class dependencies, and modding architecture (HCRDL topology).
        </p>
      </div>

      <!-- Quick Search & Actions -->
      <div class="tools-bar">
        <div class="search-box-wrap">
          <input 
            id="graph-quick-search"
            v-model="searchQuery" 
            type="text" 
            placeholder="Type anywhere to search..." 
            class="search-bar"
            @input="onSearchInput"
          />
        </div>

        <button 
          :class="['orphan-toggle', { active: hideOrphans }]" 
          @click="toggleOrphans"
        >
          {{ hideOrphans ? 'Show Orphans' : 'Hide Orphans' }}
        </button>

        <button class="reset-camera-btn" @click="recenterCamera">Recenter</button>
      </div>
    </div>

    <!-- Category Pills -->
    <div class="domain-pills-bar">
      <button 
        :class="['domain-pill', 'reset-pill', { modified: isFilterModified }]" 
        title="Reset all category filters"
        @click="resetFilters"
      >
        Reset Filters
      </button>
      <button 
        v-for="cat in CATEGORIES" 
        :key="cat.id"
        :class="['domain-pill', selectedCategories.has(cat.id) ? 'active' : 'inactive']"
        :title="selectedCategories.has(cat.id) ? `Click to hide ${cat.label}` : `Click to show ${cat.label}`"
        @click="toggleCategory(cat.id)"
      >
        <span class="color-badge" :style="{ background: cat.color }"></span>
        {{ cat.label }}
      </button>
      <span v-if="searchMatchCount > 0" class="search-match-badge">
        Matches: {{ searchMatchCount }}
      </span>
    </div>

    <!-- Canvas Frame -->
    <div class="canvas-viewport">
      <div v-if="loading" class="preloader">
        Rendering Precomputed Map...
      </div>
      <div ref="container" class="canvas-mount" tabindex="0"></div>

      <!-- Help / Controls Info Button (Top-Right) -->
      <div class="canvas-info-control">
        <button class="info-btn" title="Navigation Controls" @click.prevent.stop>
          <svg viewBox="0 0 24 24" width="16" height="16" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round">
            <circle cx="12" cy="12" r="10"></circle>
            <line x1="12" y1="16" x2="12" y2="12"></line>
            <line x1="12" y1="8" x2="12.01" y2="8"></line>
          </svg>
        </button>
        <div class="info-tooltip-card">
          <div class="info-header">Controls & Navigation</div>
          
          <div class="control-row">
            <div class="icon-wrap">
              <svg viewBox="0 0 24 32" width="16" height="22" fill="none" stroke="currentColor" stroke-width="1.8">
                <rect x="2" y="2" width="20" height="28" rx="10"></rect>
                <path d="M12 2 L12 13"></path>
                <path d="M2 13 L22 13"></path>
                <path d="M2 12 Q2 2 12 2 L12 13 L2 13 Z" fill="currentColor"></path>
              </svg>
            </div>
            <div class="control-desc">
              Select node <span class="control-sub">(drag to move)</span>
            </div>
          </div>

          <div class="control-row">
            <div class="icon-wrap">
              <svg viewBox="0 0 24 32" width="16" height="22" fill="none" stroke="currentColor" stroke-width="1.8">
                <rect x="2" y="2" width="20" height="28" rx="10"></rect>
                <path d="M12 2 L12 6"></path>
                <path d="M12 14 L12 13"></path>
                <rect x="10" y="6" width="4" height="8" rx="2" fill="currentColor"></rect>
              </svg>
            </div>
            <div class="control-desc">
              Pan canvas <span class="control-sub">(or <kbd class="kbd-badge">Ctrl</kbd> + LMB)</span>
            </div>
          </div>

          <div class="control-row">
            <div class="icon-wrap">
              <svg viewBox="0 0 24 32" width="16" height="22" fill="none" stroke="currentColor" stroke-width="1.8">
                <rect x="2" y="2" width="20" height="28" rx="10"></rect>
                <rect x="10" y="6" width="4" height="8" rx="2" stroke="currentColor"></rect>
                <path d="M12 8 L12 12" stroke-width="2"></path>
              </svg>
            </div>
            <div class="control-desc">
              Zoom in / out
            </div>
          </div>

          <div class="control-row">
            <div class="icon-wrap">
              <kbd class="kbd-badge">Esc</kbd>
            </div>
            <div class="control-desc">
              Deselect / Clear search
            </div>
          </div>
        </div>
      </div>

      <!-- Vertical Zoom Control (Bottom-Right) -->
      <div class="canvas-zoom-control">
        <button class="zoom-btn" title="Zoom In" @click="zoomIn">+</button>
        <div class="zoom-slider-wrap">
          <input 
            type="range" 
            orient="vertical" 
            class="zoom-slider" 
            min="0.3" 
            max="3.0" 
            step="0.05" 
            :value="currentZoom" 
            @input="onZoomSlider" 
          />
        </div>
        <button class="zoom-btn" title="Zoom Out" @click="zoomOut">−</button>
        <button class="zoom-reset-btn" title="Reset Zoom (1:1)" @click="zoomReset">1:1</button>
      </div>

      <!-- Selected Node Card -->
      <div v-if="selectedNode" class="node-flyout-card">
        <div class="flyout-header">
          <span class="flyout-badge" :style="{ background: selectedNode.color }">
            {{ formatCategory(selectedNode.category) }}
          </span>
          <button class="flyout-close" @click="clearSelection">✕</button>
        </div>
        <h3 class="flyout-title">{{ selectedNode.name }}</h3>
        <p class="flyout-detail">Documented members: <strong>{{ selectedNode.val || 'N/A' }}</strong></p>
        <a :href="`/api/${selectedNode.id}`" class="flyout-link">
          Open Documentation Page →
        </a>
      </div>
    </div>
  </div>
</template>

<style scoped>
.graph-page-wrapper {
  display: flex;
  flex-direction: column;
  height: calc(100vh - 90px);
  padding: 1rem 1.5rem;
  box-sizing: border-box;
}

.graph-top-row {
  display: flex;
  justify-content: space-between;
  align-items: flex-end;
  gap: 1rem;
  margin-bottom: 0.6rem;
  flex-wrap: wrap;
}

.graph-heading {
  margin: 0;
  font-size: 1.35rem;
  font-weight: 700;
  letter-spacing: -0.02em;
}

.graph-subheading {
  margin: 0.2rem 0 0;
  font-size: 0.8rem;
  color: var(--vp-c-text-2);
}

.tools-bar {
  display: flex;
  gap: 0.4rem;
  align-items: center;
}

.search-box-wrap {
  position: relative;
}

.search-bar {
  padding: 0.35rem 0.75rem;
  border-radius: 6px;
  border: 1px solid var(--vp-c-divider);
  background: var(--vp-c-bg-soft);
  color: var(--vp-c-text-1);
  font-size: 0.8rem;
  width: 190px;
}

.search-bar:focus {
  outline: none;
  border-color: var(--vp-c-brand-1);
}

.orphan-toggle, .reset-camera-btn {
  padding: 0.35rem 0.75rem;
  border-radius: 6px;
  border: 1px solid var(--vp-c-divider);
  background: var(--vp-c-bg-soft);
  color: var(--vp-c-text-1);
  font-size: 0.8rem;
  cursor: pointer;
  transition: all 0.15s ease;
}

.orphan-toggle.active {
  border-color: var(--vp-c-brand-1);
  color: var(--vp-c-brand-1);
}

.domain-pills-bar {
  display: flex;
  flex-wrap: wrap;
  gap: 0.35rem;
  margin-bottom: 0.75rem;
  align-items: center;
}

.domain-pill {
  display: inline-flex;
  align-items: center;
  gap: 0.35rem;
  padding: 0.2rem 0.6rem;
  font-size: 0.72rem;
  font-weight: 500;
  border-radius: 9999px;
  background: var(--vp-c-bg-soft);
  border: 1px solid var(--vp-c-divider);
  color: var(--vp-c-text-1);
  cursor: pointer;
  user-select: none;
  transition: all 0.15s ease;
}

.domain-pill.active {
  border-color: var(--vp-c-brand-1);
  background: var(--vp-c-bg-mute);
  color: var(--vp-c-text-1);
}

.domain-pill.active:hover {
  border-color: var(--vp-c-brand-2);
  background: var(--vp-c-bg-alt);
}

html.dark .domain-pill.active {
  border-color: rgba(56, 189, 248, 0.45);
  background: rgba(56, 189, 248, 0.12);
  color: #f8fafc;
}

html:not(.dark) .domain-pill.active {
  border-color: #0284c7;
  background: #f0f9ff;
  color: #0369a1;
}

.domain-pill.inactive {
  opacity: 0.45;
  border-color: var(--vp-c-divider);
  background: transparent;
  color: var(--vp-c-text-3);
}

.domain-pill.inactive:hover {
  opacity: 0.8;
  border-color: var(--vp-c-text-2);
}

.domain-pill.inactive .color-badge {
  filter: grayscale(1);
  opacity: 0.4;
}

.domain-pill.reset-pill {
  font-weight: 600;
  border-style: dashed;
  color: var(--vp-c-text-2);
}

.domain-pill.reset-pill:hover {
  color: var(--vp-c-brand-1);
  border-color: var(--vp-c-brand-1);
}

.domain-pill.reset-pill.modified {
  border-style: solid;
  border-color: #d97706;
  color: #b45309;
  background: rgba(217, 119, 6, 0.08);
}

html.dark .domain-pill.reset-pill.modified {
  border-color: #f59e0b;
  color: #fbbf24;
  background: rgba(245, 158, 11, 0.12);
}

.color-badge {
  width: 7px;
  height: 7px;
  border-radius: 50%;
}

.search-match-badge {
  font-size: 0.75rem;
  color: #38bdf8;
  font-weight: 600;
  margin-left: 0.5rem;
}

.canvas-viewport {
  position: relative;
  flex: 1;
  min-height: 520px;
  border-radius: 10px;
  border: 1px solid var(--vp-c-divider);
  background: #090c10;
  overflow: hidden;
}

.canvas-mount {
  width: 100%;
  height: 100%;
  outline: none;
}

.preloader {
  position: absolute;
  inset: 0;
  display: flex;
  align-items: center;
  justify-content: center;
  color: var(--vp-c-text-2);
  font-size: 0.9rem;
}

.node-flyout-card {
  position: absolute;
  bottom: 1.25rem;
  left: 1.25rem;
  width: 270px;
  padding: 1.15rem;
  border-radius: 8px;
  background: rgba(18, 22, 30, 0.95);
  border: 1px solid var(--vp-c-divider);
  backdrop-filter: blur(8px);
  box-shadow: 0 10px 30px rgba(0, 0, 0, 0.5);
  z-index: 15;
}

.flyout-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 0.4rem;
}

.flyout-badge {
  font-size: 0.68rem;
  padding: 0.15rem 0.45rem;
  border-radius: 4px;
  color: #fff;
  font-weight: 600;
}

.flyout-close {
  background: none;
  border: none;
  color: var(--vp-c-text-2);
  cursor: pointer;
  font-size: 0.85rem;
}

.flyout-title {
  margin: 0.2rem 0;
  font-size: 1.05rem;
  font-weight: 600;
  color: #fff;
}

.flyout-detail {
  margin: 0.2rem 0 0.8rem;
  font-size: 0.8rem;
  color: var(--vp-c-text-2);
}

.flyout-link {
  display: block;
  text-align: center;
  padding: 0.45rem 0.75rem;
  border-radius: 6px;
  background: var(--vp-c-brand-1);
  color: #fff;
  text-decoration: none;
  font-size: 0.8rem;
  font-weight: 500;
}

/* --- Controls Help Tooltip (Top Right) --- */
.canvas-info-control {
  position: absolute;
  top: 14px;
  right: 14px;
  z-index: 25;
}

.info-btn {
  width: 32px;
  height: 32px;
  border-radius: 7px;
  background: rgba(22, 27, 34, 0.85);
  border: 1px solid var(--vp-c-divider);
  color: var(--vp-c-text-2);
  display: flex;
  align-items: center;
  justify-content: center;
  cursor: default;
  backdrop-filter: blur(8px);
  transition: all 0.15s ease;
}

.canvas-info-control:hover .info-btn {
  color: var(--vp-c-brand-1);
  border-color: var(--vp-c-brand-1);
  background: rgba(30, 38, 50, 0.95);
}

.info-tooltip-card {
  position: absolute;
  top: 0;
  right: 42px;
  width: 250px;
  padding: 0.9rem 1rem;
  border-radius: 8px;
  background: rgba(18, 22, 30, 0.96);
  border: 1px solid var(--vp-c-divider);
  backdrop-filter: blur(12px);
  box-shadow: 0 12px 32px rgba(0, 0, 0, 0.55);
  opacity: 0;
  pointer-events: none;
  transform: translateX(6px);
  transition: all 0.2s cubic-bezier(0.16, 1, 0.3, 1);
  display: flex;
  flex-direction: column;
  gap: 0.65rem;
}

.canvas-info-control:hover .info-tooltip-card {
  opacity: 1;
  pointer-events: auto;
  transform: translateX(0);
}

.info-header {
  font-size: 0.75rem;
  font-weight: 700;
  color: var(--vp-c-text-2);
  text-transform: uppercase;
  letter-spacing: 0.06em;
  padding-bottom: 0.3rem;
  border-bottom: 1px solid var(--vp-c-divider);
}

.control-row {
  display: flex;
  align-items: center;
  gap: 0.75rem;
}

.icon-wrap {
  width: 24px;
  display: flex;
  justify-content: center;
  align-items: center;
  color: #c9d1d9;
}

.control-desc {
  font-size: 0.78rem;
  color: var(--vp-c-text-1);
  line-height: 1.35;
}

.control-key {
  font-weight: 600;
  color: #fff;
}

.control-sep {
  color: var(--vp-c-text-2);
  font-size: 0.72rem;
  margin: 0 0.25rem;
}

.control-sub {
  font-size: 0.7rem;
  color: var(--vp-c-text-2);
}

.control-text {
  color: var(--vp-c-text-2);
}

.kbd-badge {
  display: inline-block;
  padding: 0.1rem 0.35rem;
  font-size: 0.68rem;
  font-family: var(--vp-font-family-mono, monospace);
  font-weight: 600;
  background: #21262d;
  border: 1px solid #30363d;
  border-radius: 4px;
  color: #e6edf3;
  box-shadow: 0 1px 0 rgba(255, 255, 255, 0.1);
}

/* --- Vertical Zoom Dragbar (Bottom Right) --- */
.canvas-zoom-control {
  position: absolute;
  bottom: 16px;
  right: 14px;
  z-index: 20;
  width: 32px;
  padding: 4px 0;
  border-radius: 8px;
  background: rgba(22, 27, 34, 0.85);
  border: 1px solid var(--vp-c-divider);
  backdrop-filter: blur(8px);
  box-shadow: 0 4px 16px rgba(0, 0, 0, 0.4);
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 4px;
}

.zoom-btn {
  width: 26px;
  height: 26px;
  border: none;
  background: transparent;
  color: var(--vp-c-text-1);
  font-size: 1.05rem;
  font-weight: 600;
  cursor: pointer;
  border-radius: 5px;
  display: flex;
  align-items: center;
  justify-content: center;
  transition: background 0.12s ease;
}

.zoom-btn:hover {
  background: rgba(255, 255, 255, 0.08);
  color: var(--vp-c-brand-1);
}

.zoom-slider-wrap {
  height: 80px;
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 2px 0;
}

.zoom-slider {
  writing-mode: vertical-lr;
  direction: rtl;
  -webkit-appearance: slider-vertical;
  appearance: slider-vertical;
  width: 8px;
  height: 76px;
  accent-color: var(--vp-c-brand-1);
  cursor: pointer;
  opacity: 0.85;
}

.zoom-slider:hover {
  opacity: 1;
}

.zoom-reset-btn {
  width: 26px;
  height: 18px;
  border: none;
  background: transparent;
  color: var(--vp-c-text-2);
  font-size: 0.62rem;
  font-family: monospace;
  font-weight: 700;
  cursor: pointer;
  border-radius: 3px;
  display: flex;
  align-items: center;
  justify-content: center;
  transition: all 0.12s ease;
}

.zoom-reset-btn:hover {
  background: rgba(255, 255, 255, 0.08);
  color: var(--vp-c-brand-1);
}

:deep(.canvas-panning),
:deep(.canvas-panning canvas) {
  cursor: grab !important;
}

:deep(.canvas-panning.is-dragging),
:deep(.canvas-panning.is-dragging canvas),
:deep(.canvas-panning:active),
:deep(.canvas-panning canvas:active) {
  cursor: grabbing !important;
}
</style>
