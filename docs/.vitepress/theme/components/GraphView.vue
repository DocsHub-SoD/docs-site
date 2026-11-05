<script setup>
import { onMounted, onBeforeUnmount, ref } from 'vue'

const container = ref(null)
const loading = ref(true)
const selectedNode = ref(null)
const filterCategory = ref('All')
const hideIsolated = ref(true)
const searchQuery = ref('')

const CATEGORY_COLORS = {
  'Combat & Abilities': '#ef4444',
  'Actors & Entities': '#22c55e',
  'Buffs & Statuses': '#a855f7',
  'Managers & Systems': '#3b82f6',
  'Items & Economy': '#eab308',
  'User Interface': '#ec4899',
  'Networking': '#06b6d4',
  'Data & Core Math': '#f97316',
  'Miscellaneous & Utility': '#64748b'
}

let graphInstance = null
let rawData = null
let isDraggingCanvas = false
let pointerDownPos = { x: 0, y: 0 }

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

  initGraph()
})

onBeforeUnmount(() => {
  if (graphInstance) {
    graphInstance._destructor?.()
  }
})

function getFilteredData() {
  if (!rawData) return { nodes: [], links: [] }

  // Set of IDs that have at least one link
  const connectedIds = new Set()
  rawData.links.forEach(l => {
    connectedIds.add(typeof l.source === 'object' ? l.source.id : l.source)
    connectedIds.add(typeof l.target === 'object' ? l.target.id : l.target)
  })

  let filteredNodes = rawData.nodes.filter(n => {
    if (hideIsolated.value && !connectedIds.has(n.id)) return false
    if (filterCategory.value !== 'All' && n.category !== filterCategory.value) return false
    if (searchQuery.value && !n.name.toLowerCase().includes(searchQuery.value.toLowerCase())) return false
    return true
  })

  const visibleNodeIds = new Set(filteredNodes.map(n => n.id))
  let filteredLinks = rawData.links.filter(l => {
    const s = typeof l.source === 'object' ? l.source.id : l.source
    const t = typeof l.target === 'object' ? l.target.id : l.target
    return visibleNodeIds.has(s) && visibleNodeIds.has(t)
  })

  return { nodes: filteredNodes, links: filteredLinks }
}

function initGraph() {
  if (!container.value) return

  const elem = container.value
  elem.innerHTML = ''

  const currentData = getFilteredData()

  graphInstance = ForceGraph()(elem)
    .graphData(currentData)
    .nodeId('id')
    .nodeLabel(node => `${node.name}\n[${node.category}]`)
    .nodeColor(node => node.color)
    .nodeVal(node => Math.max(node.val, 2))
    .linkColor(() => 'rgba(140, 140, 160, 0.22)')
    .linkWidth(1.2)
    .linkDirectionalParticles(1)
    .linkDirectionalParticleSpeed(0.004)
    .linkDirectionalParticleWidth(2)
    .backgroundColor('#0a0d13')
    .d3AlphaDecay(0.02)
    .d3VelocityDecay(0.3)
    // Obsidian-like physics: strong repulsion, longer springs
    .d3Force('charge', window.d3?.forceManyBody().strength(-140))
    .d3Force('link', window.d3?.forceLink().distance(40).strength(0.4))
    .enableNodeDrag(true)
    .onNodeHover(node => {
      elem.style.cursor = node ? 'pointer' : 'default'
    })
    .onNodeClick((node, event) => {
      // Ignore click if user was actually dragging canvas
      if (isDraggingCanvas) return
      selectedNode.value = node
    })
    .nodeCanvasObject((node, ctx, globalScale) => {
      if (!Number.isFinite(node.x) || !Number.isFinite(node.y)) return

      const r = Math.max(Math.sqrt(node.val || 2) * 2, 2.5)
      ctx.beginPath()
      ctx.arc(node.x, node.y, r, 0, 2 * Math.PI, false)
      ctx.fillStyle = node.color
      ctx.fill()

      // High zoom label display
      if (globalScale > 1.3 || (node.val && node.val > 7)) {
        const label = node.name
        const fontSize = Math.max(9 / globalScale, 3.5)
        ctx.font = `${fontSize}px -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif`
        ctx.textAlign = 'center'
        ctx.textBaseline = 'top'
        ctx.fillStyle = 'rgba(240, 240, 250, 0.85)'
        ctx.fillText(label, node.x, node.y + r + 2)
      }
    })

  // Prevent false-clicks during canvas drag
  elem.addEventListener('pointerdown', (e) => {
    isDraggingCanvas = false
    pointerDownPos = { x: e.clientX, y: e.clientY }
  })

  elem.addEventListener('pointermove', (e) => {
    const dist = Math.hypot(e.clientX - pointerDownPos.x, e.clientY - pointerDownPos.y)
    if (dist > 5) {
      isDraggingCanvas = true
    }
  })

  // Auto zoom-to-fit once simulation settles
  setTimeout(() => {
    graphInstance?.zoomToFit(400, 40)
  }, 1200)
}

function updateGraph() {
  if (!graphInstance) return
  graphInstance.graphData(getFilteredData())
  setTimeout(() => {
    graphInstance?.zoomToFit(400, 30)
  }, 300)
}

function toggleIsolated() {
  hideIsolated.value = !hideIsolated.value
  updateGraph()
}

function setFilter(cat) {
  filterCategory.value = cat
  updateGraph()
}

function onSearchInput() {
  updateGraph()
}
</script>

<template>
  <div class="graph-viewport">
    <div class="graph-top-bar">
      <div class="title-row">
        <div>
          <h1 class="main-title">Interactive Dependency Graph</h1>
          <p class="desc">
            Visualizing class inheritance and interface implementations.
            <span v-if="hideIsolated" class="stat-badge">Showing 350 connected nodes</span>
            <span v-else class="stat-badge">Showing all 897 types</span>
          </p>
        </div>

        <div class="controls-row">
          <input 
            v-model="searchQuery" 
            type="text" 
            placeholder="Search class in graph..." 
            class="graph-search"
            @input="onSearchInput"
          />

          <button 
            :class="['toggle-btn', { active: hideIsolated }]" 
            @click="toggleIsolated"
          >
            {{ hideIsolated ? '✓ Only Connected Nodes' : 'Show All (incl. Isolated)' }}
          </button>
        </div>
      </div>

      <!-- Categories Filter -->
      <div class="category-filters">
        <button 
          :class="['cat-pill', { active: filterCategory === 'All' }]" 
          @click="setFilter('All')"
        >
          All Domains
        </button>
        <button 
          v-for="(color, cat) in CATEGORY_COLORS" 
          :key="cat"
          :class="['cat-pill', { active: filterCategory === cat }]"
          @click="setFilter(cat)"
        >
          <span class="color-dot" :style="{ background: color }"></span>
          {{ cat }}
        </button>
      </div>
    </div>

    <!-- Main Canvas Box -->
    <div class="canvas-container">
      <div v-if="loading" class="spinner">
        Loading Graph Universe...
      </div>
      <div ref="container" class="canvas-mount"></div>

      <!-- Detail Card on Node Click -->
      <div v-if="selectedNode" class="node-inspector">
        <div class="inspector-header">
          <span class="category-tag" :style="{ background: selectedNode.color }">
            {{ selectedNode.category }}
          </span>
          <button class="close-card" @click="selectedNode = null">✕</button>
        </div>
        <h3 class="inspector-name">{{ selectedNode.name }}</h3>
        <p class="inspector-methods">Methods / Members: <strong>{{ selectedNode.methods }}</strong></p>
        <a :href="`/api/${selectedNode.id}`" class="jump-link">
          Open Documentation Page →
        </a>
      </div>
    </div>
  </div>
</template>

<style scoped>
.graph-viewport {
  display: flex;
  flex-direction: column;
  height: calc(100vh - 90px);
  padding: 1rem 1.5rem;
  box-sizing: border-box;
}

.graph-top-bar {
  margin-bottom: 0.85rem;
}

.title-row {
  display: flex;
  justify-content: space-between;
  align-items: flex-end;
  gap: 1rem;
  margin-bottom: 0.6rem;
  flex-wrap: wrap;
}

.main-title {
  margin: 0;
  font-size: 1.4rem;
  font-weight: 700;
  letter-spacing: -0.02em;
}

.desc {
  margin: 0.2rem 0 0;
  font-size: 0.85rem;
  color: var(--vp-c-text-2);
}

.stat-badge {
  display: inline-block;
  margin-left: 0.5rem;
  padding: 0.15rem 0.5rem;
  border-radius: 4px;
  background: var(--vp-c-bg-mute);
  border: 1px solid var(--vp-c-divider);
  font-size: 0.75rem;
  font-weight: 500;
  color: var(--vp-c-brand-1);
}

.controls-row {
  display: flex;
  gap: 0.5rem;
  align-items: center;
}

.graph-search {
  padding: 0.35rem 0.75rem;
  border-radius: 6px;
  border: 1px solid var(--vp-c-divider);
  background: var(--vp-c-bg-soft);
  color: var(--vp-c-text-1);
  font-size: 0.8rem;
  width: 180px;
}

.graph-search:focus {
  outline: none;
  border-color: var(--vp-c-brand-1);
}

.toggle-btn {
  padding: 0.35rem 0.75rem;
  border-radius: 6px;
  border: 1px solid var(--vp-c-divider);
  background: var(--vp-c-bg-soft);
  color: var(--vp-c-text-1);
  font-size: 0.8rem;
  cursor: pointer;
  transition: all 0.15s ease;
}

.toggle-btn.active {
  border-color: var(--vp-c-brand-1);
  color: var(--vp-c-brand-1);
  background: var(--vp-c-bg-mute);
}

.category-filters {
  display: flex;
  flex-wrap: wrap;
  gap: 0.35rem;
}

.cat-pill {
  display: inline-flex;
  align-items: center;
  gap: 0.35rem;
  padding: 0.2rem 0.55rem;
  font-size: 0.75rem;
  border-radius: 9999px;
  background: var(--vp-c-bg-soft);
  border: 1px solid var(--vp-c-divider);
  color: var(--vp-c-text-1);
  cursor: pointer;
  transition: all 0.15s ease;
}

.cat-pill:hover, .cat-pill.active {
  border-color: var(--vp-c-brand-1);
  background: var(--vp-c-bg-mute);
}

.color-dot {
  width: 7px;
  height: 7px;
  border-radius: 50%;
}

.canvas-container {
  position: relative;
  flex: 1;
  min-height: 500px;
  border-radius: 10px;
  border: 1px solid var(--vp-c-divider);
  background: #0a0d13;
  overflow: hidden;
}

.canvas-mount {
  width: 100%;
  height: 100%;
}

.spinner {
  position: absolute;
  inset: 0;
  display: flex;
  align-items: center;
  justify-content: center;
  color: var(--vp-c-text-2);
  font-size: 0.9rem;
}

.node-inspector {
  position: absolute;
  bottom: 1.25rem;
  right: 1.25rem;
  width: 270px;
  padding: 1.15rem;
  border-radius: 8px;
  background: rgba(18, 22, 30, 0.94);
  border: 1px solid var(--vp-c-divider);
  backdrop-filter: blur(8px);
  box-shadow: 0 10px 30px rgba(0, 0, 0, 0.5);
  z-index: 10;
}

.inspector-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 0.4rem;
}

.category-tag {
  font-size: 0.68rem;
  padding: 0.15rem 0.45rem;
  border-radius: 4px;
  color: #fff;
  font-weight: 600;
}

.close-card {
  background: none;
  border: none;
  color: var(--vp-c-text-2);
  cursor: pointer;
  font-size: 0.85rem;
}

.inspector-name {
  margin: 0.2rem 0;
  font-size: 1.05rem;
  font-weight: 600;
  color: #fff;
}

.inspector-methods {
  margin: 0.2rem 0 0.8rem;
  font-size: 0.8rem;
  color: var(--vp-c-text-2);
}

.jump-link {
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
</style>
