<script setup>
import { onMounted, onBeforeUnmount, ref } from 'vue'

const container = ref(null)
const loading = ref(true)
const selectedNode = ref(null)
const activeCategory = ref('All')
const searchQuery = ref('')

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

// Angular positions for domain star layout (radians)
const CATEGORY_ANGLES = {
  'Combat & Abilities': 0,                     // East (0 deg)
  'Actors & Entities': Math.PI * 0.25,        // SE (45 deg)
  'Managers & Systems': Math.PI * 0.5,        // South (90 deg)
  'Buffs & Statuses': Math.PI * 0.75,         // SW (135 deg)
  'Items & Economy': Math.PI,                 // West (180 deg)
  'User Interface': Math.PI * 1.25,           // NW (225 deg)
  'Networking': Math.PI * 1.5,                // North (270 deg)
  'Data & Core Math': Math.PI * 1.75,         // NE (315 deg)
  'Miscellaneous & Utility': null             // Center
}

let graphInstance = null
let fullNodes = []
let fullLinks = []
let isDragging = false
let downPos = { x: 0, y: 0 }

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
  const json = await res.json()

  // Save clean clones
  fullNodes = json.nodes.map(n => ({ ...n }))
  fullLinks = json.links.map(l => ({
    source: typeof l.source === 'object' ? l.source.id : l.source,
    target: typeof l.target === 'object' ? l.target.id : l.target,
    type: l.type
  }))

  loading.value = false
  initRadialGraph()
})

onBeforeUnmount(() => {
  if (graphInstance) graphInstance._destructor?.()
})

function getFilteredData() {
  let nodes = fullNodes.map(n => ({ ...n }))

  if (activeCategory.value !== 'All') {
    nodes = nodes.filter(n => n.category === activeCategory.value)
  }

  if (searchQuery.value.trim()) {
    const q = searchQuery.value.toLowerCase().trim()
    nodes = nodes.filter(n => n.name.toLowerCase().includes(q))
  }

  const validIds = new Set(nodes.map(n => n.id))
  const links = fullLinks
    .filter(l => validIds.has(l.source) && validIds.has(l.target))
    .map(l => ({ ...l }))

  return { nodes, links }
}

function initRadialGraph() {
  if (!container.value) return

  const elem = container.value
  elem.innerHTML = ''

  const initialData = getFilteredData()
  const CLUSTER_RADIUS = 280

  graphInstance = ForceGraph()(elem)
    .graphData(initialData)
    .nodeId('id')
    .nodeLabel(node => `${node.name}\n[${node.category}]`)
    .nodeColor(node => node.color)
    .nodeVal(node => Math.max(node.val, 3))
    .linkColor(() => 'rgba(120, 130, 160, 0.25)')
    .linkWidth(1.2)
    .backgroundColor('#090c10')
    .d3AlphaDecay(0.02)
    .d3VelocityDecay(0.28)
    .enableNodeDrag(true)

  // Configure Radial Star Physics with D3 forces
  if (window.d3) {
    const d3 = window.d3

    // 1. Force Collide: Hard repulsion preventing nodes from overlapping
    graphInstance.d3Force('collide', d3.forceCollide().radius(node => {
      const r = Math.max(Math.sqrt(node.val || 3) * 2.2, 4)
      return r + 5 // 5px padding between nodes
    }))

    // 2. Link Force: Spring tension
    graphInstance.d3Force('link', d3.forceLink().id(d => d.id).distance(35).strength(0.3))

    // 3. ManyBody: Moderate charge so clusters don't blow up
    graphInstance.d3Force('charge', d3.forceManyBody().strength(-35))

    // 4. Radial Star Attraction (X and Y sectoral anchors)
    graphInstance.d3Force('radialX', d3.forceX(node => {
      const angle = CATEGORY_ANGLES[node.category]
      if (angle === null || angle === undefined) return 0
      return Math.cos(angle) * CLUSTER_RADIUS
    }).strength(0.25))

    graphInstance.d3Force('radialY', d3.forceY(node => {
      const angle = CATEGORY_ANGLES[node.category]
      if (angle === null || angle === undefined) return 0
      return Math.sin(angle) * CLUSTER_RADIUS
    }).strength(0.25))
  }

  // Canvas drawing
  graphInstance.nodeCanvasObject((node, ctx, globalScale) => {
    if (!Number.isFinite(node.x) || !Number.isFinite(node.y)) return

    const r = Math.max(Math.sqrt(node.val || 3) * 2.2, 3.5)
    ctx.beginPath()
    ctx.arc(node.x, node.y, r, 0, 2 * Math.PI, false)
    ctx.fillStyle = node.color
    ctx.fill()

    // Outer ring for major hubs
    if (node.val > 8) {
      ctx.lineWidth = 1.2
      ctx.strokeStyle = 'rgba(255, 255, 255, 0.6)'
      ctx.stroke()
    }

    // Zoomed-in label
    if (globalScale > 1.2 || node.val > 7) {
      const fontSize = Math.max(9 / globalScale, 3.8)
      ctx.font = `${fontSize}px -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif`
      ctx.textAlign = 'center'
      ctx.textBaseline = 'top'
      ctx.fillStyle = 'rgba(245, 245, 250, 0.9)'
      ctx.fillText(node.name, node.x, node.y + r + 2.5)
    }
  })

  // Safe Drag vs Click Detection
  elem.addEventListener('pointerdown', e => {
    isDragging = false
    downPos = { x: e.clientX, y: e.clientY }
  })

  elem.addEventListener('pointermove', e => {
    if (Math.hypot(e.clientX - downPos.x, e.clientY - downPos.y) > 4) {
      isDragging = true
    }
  })

  graphInstance.onNodeClick(node => {
    if (isDragging) return
    selectedNode.value = node
  })

  // Fit camera after initial layout
  setTimeout(() => {
    graphInstance?.zoomToFit(500, 30)
  }, 1000)
}

function applyFilter(cat) {
  activeCategory.value = cat
  if (!graphInstance) return

  const data = getFilteredData()
  graphInstance.graphData(data)
  setTimeout(() => {
    graphInstance?.zoomToFit(400, 30)
  }, 250)
}

function handleSearch() {
  if (!graphInstance) return
  const data = getFilteredData()
  graphInstance.graphData(data)
  setTimeout(() => {
    graphInstance?.zoomToFit(400, 30)
  }, 250)
}

function resetView() {
  activeCategory.value = 'All'
  searchQuery.value = ''
  applyFilter('All')
}
</script>

<template>
  <div class="graph-layout">
    <!-- Header -->
    <div class="header-box">
      <div class="header-top">
        <div>
          <h1 class="header-title">Radial Domain Dependency Graph</h1>
          <p class="header-subtitle">
            Visualizing 897 classes clustered radially by domain. Drag nodes, scroll to zoom, click to inspect.
          </p>
        </div>

        <div class="action-tools">
          <input 
            v-model="searchQuery" 
            type="text" 
            placeholder="Search class..." 
            class="search-input"
            @input="handleSearch"
          />
          <button class="reset-btn" @click="resetView">Reset View</button>
        </div>
      </div>

      <!-- Domain Sector Pills -->
      <div class="domain-pills">
        <button 
          :class="['domain-pill', { active: activeCategory === 'All' }]" 
          @click="applyFilter('All')"
        >
          All Domains (897)
        </button>
        <button 
          v-for="(color, cat) in CATEGORY_COLORS" 
          :key="cat"
          :class="['domain-pill', { active: activeCategory === cat }]"
          :style="{ '--c': color }"
          @click="applyFilter(cat)"
        >
          <span class="pill-dot" :style="{ background: color }"></span>
          {{ cat }}
        </button>
      </div>
    </div>

    <!-- Canvas Frame -->
    <div class="viewport-box">
      <div v-if="loading" class="loading-state">
        Compiling Radial Star Layout...
      </div>
      <div ref="container" class="mount-target"></div>

      <!-- Selected Node Popover -->
      <div v-if="selectedNode" class="node-popover">
        <div class="popover-top">
          <span class="domain-badge" :style="{ background: selectedNode.color }">
            {{ selectedNode.category }}
          </span>
          <button class="close-popover" @click="selectedNode = null">✕</button>
        </div>
        <h3 class="popover-name">{{ selectedNode.name }}</h3>
        <p class="popover-info">Documented members: <strong>{{ selectedNode.methods }}</strong></p>
        <a :href="`/api/${selectedNode.id}`" class="popover-btn">
          View Class API →
        </a>
      </div>
    </div>
  </div>
</template>

<style scoped>
.graph-layout {
  display: flex;
  flex-direction: column;
  height: calc(100vh - 90px);
  padding: 1rem 1.5rem;
  box-sizing: border-box;
}

.header-box {
  margin-bottom: 0.75rem;
}

.header-top {
  display: flex;
  justify-content: space-between;
  align-items: flex-end;
  gap: 1rem;
  margin-bottom: 0.6rem;
  flex-wrap: wrap;
}

.header-title {
  margin: 0;
  font-size: 1.35rem;
  font-weight: 700;
  letter-spacing: -0.02em;
}

.header-subtitle {
  margin: 0.2rem 0 0;
  font-size: 0.82rem;
  color: var(--vp-c-text-2);
}

.action-tools {
  display: flex;
  gap: 0.4rem;
}

.search-input {
  padding: 0.35rem 0.7rem;
  border-radius: 6px;
  border: 1px solid var(--vp-c-divider);
  background: var(--vp-c-bg-soft);
  color: var(--vp-c-text-1);
  font-size: 0.8rem;
  width: 170px;
}

.search-input:focus {
  outline: none;
  border-color: var(--vp-c-brand-1);
}

.reset-btn {
  padding: 0.35rem 0.7rem;
  border-radius: 6px;
  border: 1px solid var(--vp-c-divider);
  background: var(--vp-c-bg-soft);
  color: var(--vp-c-text-1);
  font-size: 0.8rem;
  cursor: pointer;
  transition: all 0.15s ease;
}

.reset-btn:hover {
  background: var(--vp-c-bg-mute);
  border-color: var(--vp-c-brand-1);
}

.domain-pills {
  display: flex;
  flex-wrap: wrap;
  gap: 0.35rem;
}

.domain-pill {
  display: inline-flex;
  align-items: center;
  gap: 0.35rem;
  padding: 0.2rem 0.55rem;
  font-size: 0.74rem;
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

.pill-dot {
  width: 7px;
  height: 7px;
  border-radius: 50%;
}

.viewport-box {
  position: relative;
  flex: 1;
  min-height: 520px;
  border-radius: 10px;
  border: 1px solid var(--vp-c-divider);
  background: #090c10;
  overflow: hidden;
}

.mount-target {
  width: 100%;
  height: 100%;
}

.loading-state {
  position: absolute;
  inset: 0;
  display: flex;
  align-items: center;
  justify-content: center;
  color: var(--vp-c-text-2);
  font-size: 0.9rem;
}

.node-popover {
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

.popover-top {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 0.4rem;
}

.domain-badge {
  font-size: 0.68rem;
  padding: 0.15rem 0.45rem;
  border-radius: 4px;
  color: #fff;
  font-weight: 600;
}

.close-popover {
  background: none;
  border: none;
  color: var(--vp-c-text-2);
  cursor: pointer;
  font-size: 0.85rem;
}

.popover-name {
  margin: 0.2rem 0;
  font-size: 1.05rem;
  font-weight: 600;
  color: #fff;
}

.popover-info {
  margin: 0.2rem 0 0.8rem;
  font-size: 0.8rem;
  color: var(--vp-c-text-2);
}

.popover-btn {
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
