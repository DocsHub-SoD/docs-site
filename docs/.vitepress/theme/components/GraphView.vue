<script setup>
import { onMounted, onBeforeUnmount, ref } from 'vue'

const container = ref(null)
const loading = ref(true)
const selectedNode = ref(null)
const activeCategory = ref('All')
const hideOrphans = ref(false)
const searchQuery = ref('')
const searchMatchCount = ref(0)

const CATEGORY_COLORS = {
  'Combat & Abilities': '#ef4444',
  'Actors & Entities': '#22c55e',
  'Managers & Systems': '#3b82f6',
  'Buffs & Statuses': '#a855f7',
  'Items & Economy': '#eab308',
  'User Interface': '#ec4899',
  'Networking': '#06b6d4',
  'Data & Core Math': '#f97316',
  'Miscellaneous & Utility': '#64748b'
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
let isWheeling = false
let wheelTimer = null
let panStart = { x: 0, y: 0 }
let dragDistance = 0
let mouseDownPos = { x: 0, y: 0 }

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
    .filter(n => (activeCategory.value === 'All' || n.category === activeCategory.value))
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
    .nodeLabel(n => `${n.name}\n[${n.category}]`)
    .nodeColor(n => n.color)
    .nodeVal(n => Math.max(n.val || 2.5, 2.5))
    .backgroundColor('#090c10')
    .cooldownTicks(0) // Zero CPU cost on load
    .enableNodeDrag(true) // User can freely reposition nodes manually if desired
    .linkWidth(l => highlightLinks.has(l) ? 2.5 : 1)
    .linkColor(l => highlightLinks.has(l) ? 'rgba(255, 255, 255, 0.9)' : 'rgba(120, 130, 160, 0.18)')
    .linkDirectionalParticles(l => highlightLinks.has(l) ? 3 : 0)
    .linkDirectionalParticleSpeed(0.007)
    .onNodeHover(node => {
      hoveredNode = node
      if (!selectedNode.value) {
        updateHighlights(node)
      }
    })
    .onNodeClick(node => {
      // Strict click filter: ignore when zooming or panning
      if (isWheeling || isPanning || isCtrlPressed || dragDistance > 5) return
      setSelectedNode(node)
    })
    .nodeCanvasObject((node, ctx, globalScale) => {
      if (!Number.isFinite(node.x) || !Number.isFinite(node.y)) return

      const isSearched = matchedQueryIds.size > 0
      const isMatch = matchedQueryIds.has(node.id)
      const isSelected = selectedNode.value === node
      const isHighlighted = highlightNodes.has(node)
      const isDimmed = (highlightNodes.size > 0 && !isHighlighted) || (isSearched && !isMatch)

      const r = Math.max(Math.sqrt(node.val || 2.5) * 2.2, 3.5)

      ctx.beginPath()
      ctx.arc(node.x, node.y, r, 0, 2 * Math.PI, false)
      ctx.fillStyle = isDimmed ? 'rgba(45, 50, 60, 0.18)' : node.color
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

      // Type Label
      if ((globalScale > 1.2 || node.val > 7 || isMatch || isSelected) && !isDimmed) {
        const fontSize = Math.max(9 / globalScale, 3.8)
        ctx.font = `${isMatch || isSelected ? 'bold ' : ''}${fontSize}px sans-serif`
        ctx.textAlign = 'center'
        ctx.textBaseline = 'top'
        ctx.fillStyle = isSelected ? '#fbbf24' : (isMatch ? '#38bdf8' : 'rgba(240, 240, 250, 0.9)')
        ctx.fillText(node.name, node.x, node.y + r + 2.5)
      }
    })

  setupNavigationControls(elem)
  applyDataToGraph()
}

function applyDataToGraph() {
  if (!graphInstance) return
  const data = getFilteredData()
  graphInstance.graphData(data)
  setTimeout(() => {
    graphInstance?.zoomToFit(500, 40)
  }, 100)
}

function updateHighlights(targetNode) {
  highlightNodes.clear()
  highlightLinks.clear()

  if (targetNode) {
    highlightNodes.add(targetNode)
    const data = graphInstance.graphData()
    data.links.forEach(l => {
      const s = typeof l.source === 'object' ? l.source.id : l.source
      const t = typeof l.target === 'object' ? l.target.id : l.target
      if (s === targetNode.id || t === targetNode.id) {
        highlightLinks.add(l)
        highlightNodes.add(typeof l.source === 'object' ? l.source : data.nodes.find(n => n.id === s))
        highlightNodes.add(typeof l.target === 'object' ? l.target : data.nodes.find(n => n.id === t))
      }
    })
  }
}

function setSelectedNode(node) {
  selectedNode.value = node
  updateHighlights(node)
}

function clearSelection() {
  selectedNode.value = null
  updateHighlights(hoveredNode)
}

function setupNavigationControls(elem) {
  // Prevent wheel scroll from triggering clicks
  elem.addEventListener('wheel', () => {
    isWheeling = true
    clearTimeout(wheelTimer)
    wheelTimer = setTimeout(() => { isWheeling = false }, 300)
  }, { passive: true })

  elem.addEventListener('mousedown', e => {
    dragDistance = 0
    mouseDownPos = { x: e.clientX, y: e.clientY }

    // Middle Click or Ctrl + Left Click
    if (e.button === 1 || (e.button === 0 && e.ctrlKey)) {
      isPanning = true
      panStart = { x: e.clientX, y: e.clientY }
      elem.classList.add('canvas-panning')
      e.preventDefault()
    }
  })

  window.addEventListener('mousemove', e => {
    dragDistance = Math.hypot(e.clientX - mouseDownPos.x, e.clientY - mouseDownPos.y)

    if (!isPanning || !graphInstance) return
    const dx = e.clientX - panStart.x
    const dy = e.clientY - panStart.y
    panStart = { x: e.clientX, y: e.clientY }

    const currentPos = graphInstance.centerAt()
    const zoom = graphInstance.zoom()
    graphInstance.centerAt(currentPos.x - dx / zoom, currentPos.y - dy / zoom)
  })

  window.addEventListener('mouseup', () => {
    if (isPanning) {
      isPanning = false
      if (!isCtrlPressed) elem.classList.remove('canvas-panning')
    }
  })

  window.addEventListener('keydown', e => {
    if (e.key === 'Control') {
      isCtrlPressed = true
      elem.classList.add('canvas-panning')
    }
    if (e.key === 'Escape') {
      searchQuery.value = ''
      matchedQueryIds.clear()
      searchMatchCount.value = 0
      clearSelection()
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
      if (!isPanning) elem.classList.remove('canvas-panning')
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
}

function selectCategory(cat) {
  activeCategory.value = cat
  applyDataToGraph()
}

function toggleOrphans() {
  hideOrphans.value = !hideOrphans.value
  applyDataToGraph()
}

function recenterCamera() {
  graphInstance?.zoomToFit(500, 40)
}
</script>

<template>
  <div class="graph-page-wrapper">
    <!-- Top Bar -->
    <div class="graph-top-row">
      <div class="title-meta">
        <h1 class="graph-heading">Interactive Topology Map</h1>
        <p class="graph-subheading">
          Hierarchical Constrained Radial Domain Layout (HCRDL). Precomputed coordinates, zero physics lag.
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
          <span class="esc-tag">Esc</span>
        </div>

        <button 
          :class="['orphan-toggle', { active: hideOrphans }]" 
          @click="toggleOrphans"
        >
          {{ hideOrphans ? 'Show All (incl. Orphans)' : 'Hide Outer Orphans' }}
        </button>

        <button class="reset-camera-btn" @click="recenterCamera">Recenter</button>
      </div>
    </div>

    <!-- Category Pills -->
    <div class="domain-pills-bar">
      <button 
        :class="['domain-pill', { active: activeCategory === 'All' }]" 
        @click="selectCategory('All')"
      >
        All Domains (897)
      </button>
      <button 
        v-for="(color, cat) in CATEGORY_COLORS" 
        :key="cat"
        :class="['domain-pill', { active: activeCategory === cat }]"
        @click="selectCategory(cat)"
      >
        <span class="color-badge" :style="{ background: color }"></span>
        {{ cat }}
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

      <!-- Selected Node Card -->
      <div v-if="selectedNode" class="node-flyout-card">
        <div class="flyout-header">
          <span class="flyout-badge" :style="{ background: selectedNode.color }">
            {{ selectedNode.category }}
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
  padding: 0.35rem 1.8rem 0.35rem 0.75rem;
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

.esc-tag {
  position: absolute;
  right: 6px;
  top: 50%;
  transform: translateY(-50%);
  font-size: 0.62rem;
  padding: 0.1rem 0.3rem;
  border-radius: 3px;
  background: var(--vp-c-bg-mute);
  color: var(--vp-c-text-2);
  pointer-events: none;
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
  padding: 0.2rem 0.55rem;
  font-size: 0.72rem;
  border-radius: 9999px;
  background: var(--vp-c-bg-soft);
  border: 1px solid var(--vp-c-divider);
  color: var(--vp-c-text-1);
  cursor: pointer;
  transition: all 0.15s ease;
}

.domain-pill:hover, .domain-pill.active {
  border-color: var(--vp-c-brand-1);
  background: var(--vp-c-bg-mute);
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
  right: 1.25rem;
  width: 270px;
  padding: 1.15rem;
  border-radius: 8px;
  background: rgba(18, 22, 30, 0.95);
  border: 1px solid var(--vp-c-divider);
  backdrop-filter: blur(8px);
  box-shadow: 0 10px 30px rgba(0, 0, 0, 0.5);
  z-index: 10;
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

:deep(.canvas-panning) {
  cursor: grab !important;
}

:deep(.canvas-panning:active) {
  cursor: grabbing !important;
}
</style>
