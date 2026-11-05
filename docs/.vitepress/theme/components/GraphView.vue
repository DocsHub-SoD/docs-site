<script setup>
import { onMounted, ref } from 'vue'

const container = ref(null)
const loading = ref(true)
const selectedNode = ref(null)
const filterCategory = ref('All')

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
let fullData = null

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
  fullData = await res.json()
  loading.value = false

  renderGraph(fullData)
})

function renderGraph(data) {
  if (!container.value) return

  const elem = container.value
  elem.innerHTML = ''

  graphInstance = ForceGraph()(elem)
    .graphData(data)
    .nodeId('id')
    .nodeLabel(node => `${node.name} (${node.category})`)
    .nodeColor(node => node.color)
    .nodeVal(node => node.val)
    .linkColor(() => 'rgba(150, 150, 150, 0.25)')
    .linkWidth(1)
    .linkDirectionalParticles(1)
    .linkDirectionalParticleSpeed(0.005)
    .linkDirectionalParticleWidth(2)
    .backgroundColor('transparent')
    .onNodeClick(node => {
      selectedNode.value = node
    })
    .onNodeHover(node => {
      elem.style.cursor = node ? 'pointer' : 'default'
    })
    .nodeCanvasObject((node, ctx, globalScale) => {
      const r = Math.sqrt(node.val) * 2
      ctx.beginPath()
      ctx.arc(node.x, node.y, r, 0, 2 * Math.PI, false)
      ctx.fillStyle = node.color
      ctx.fill()

      if (globalScale > 1.2 || node.val > 8) {
        const label = node.name
        const fontSize = Math.max(10 / globalScale, 4)
        ctx.font = `${fontSize}px Sans-Serif`
        ctx.textAlign = 'center'
        ctx.textBaseline = 'top'
        ctx.fillStyle = 'rgba(255, 255, 255, 0.85)'
        ctx.fillText(label, node.x, node.y + r + 2)
      }
    })
}

function setFilter(cat) {
  filterCategory.value = cat
  if (!fullData || !graphInstance) return

  if (cat === 'All') {
    graphInstance.graphData(fullData)
  } else {
    const filteredNodes = fullData.nodes.filter(n => n.category === cat)
    const nodeIds = new Set(filteredNodes.map(n => n.id))
    const filteredLinks = fullData.links.filter(l => nodeIds.has(l.source.id || l.source) && nodeIds.has(l.target.id || l.target))
    graphInstance.graphData({ nodes: filteredNodes, links: filteredLinks })
  }
}
</script>

<template>
  <div class="graph-page">
    <div class="graph-header">
      <div>
        <h1 class="title">Interactive Dependency Graph</h1>
        <p class="subtitle">Explore 897 classes and 1,354 inheritance links. Drag to pan, scroll to zoom, click any node to inspect.</p>
      </div>

      <div class="filters">
        <button 
          :class="['pill', { active: filterCategory === 'All' }]" 
          @click="setFilter('All')"
        >
          All (897)
        </button>
        <button 
          v-for="(color, cat) in CATEGORY_COLORS" 
          :key="cat"
          :class="['pill', { active: filterCategory === cat }]"
          :style="{ '--cat-color': color }"
          @click="setFilter(cat)"
        >
          <span class="dot" :style="{ background: color }"></span>
          {{ cat }}
        </button>
      </div>
    </div>

    <div class="canvas-wrapper">
      <div v-if="loading" class="loading-overlay">
        <p>Loading Graph Universe (897 nodes)...</p>
      </div>
      <div ref="container" class="graph-canvas"></div>

      <div v-if="selectedNode" class="node-card">
        <div class="card-header">
          <span class="badge" :style="{ background: selectedNode.color }">{{ selectedNode.category }}</span>
          <button class="close-btn" @click="selectedNode = null">✕</button>
        </div>
        <h3 class="node-title">{{ selectedNode.name }}</h3>
        <p class="node-meta">Methods documented: <strong>{{ selectedNode.methods }}</strong></p>
        <a :href="`/api/${selectedNode.id}`" class="view-btn">Open Documentation Page →</a>
      </div>
    </div>
  </div>
</template>

<style scoped>
.graph-page {
  display: flex;
  flex-direction: column;
  height: calc(100vh - 100px);
  padding: 1rem 0;
  box-sizing: border-box;
}

.graph-header {
  margin-bottom: 0.75rem;
}

.title {
  margin: 0;
  font-size: 1.5rem;
  font-weight: 700;
}

.subtitle {
  margin: 0.25rem 0 0.5rem;
  font-size: 0.85rem;
  color: var(--vp-c-text-2);
}

.filters {
  display: flex;
  flex-wrap: wrap;
  gap: 0.4rem;
  margin-top: 0.5rem;
}

.pill {
  display: flex;
  align-items: center;
  gap: 0.35rem;
  padding: 0.25rem 0.6rem;
  font-size: 0.75rem;
  border-radius: 9999px;
  background: var(--vp-c-bg-soft);
  border: 1px solid var(--vp-c-divider);
  color: var(--vp-c-text-1);
  cursor: pointer;
  transition: all 0.15s ease;
}

.pill:hover, .pill.active {
  border-color: var(--vp-c-brand-1);
  background: var(--vp-c-bg-mute);
}

.dot {
  width: 8px;
  height: 8px;
  border-radius: 50%;
}

.canvas-wrapper {
  position: relative;
  flex: 1;
  border-radius: 12px;
  border: 1px solid var(--vp-c-divider);
  background: #0d1117;
  overflow: hidden;
  min-height: 550px;
}

.graph-canvas {
  width: 100%;
  height: 100%;
}

.loading-overlay {
  position: absolute;
  inset: 0;
  display: flex;
  align-items: center;
  justify-content: center;
  color: var(--vp-c-text-2);
  font-size: 0.9rem;
}

.node-card {
  position: absolute;
  bottom: 1.5rem;
  right: 1.5rem;
  width: 280px;
  padding: 1.25rem;
  border-radius: 10px;
  background: rgba(22, 27, 34, 0.95);
  border: 1px solid var(--vp-c-divider);
  backdrop-filter: blur(8px);
  box-shadow: 0 8px 24px rgba(0, 0, 0, 0.4);
  z-index: 10;
}

.card-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 0.5rem;
}

.badge {
  font-size: 0.7rem;
  padding: 0.15rem 0.45rem;
  border-radius: 4px;
  color: #fff;
  font-weight: 600;
}

.close-btn {
  background: none;
  border: none;
  color: var(--vp-c-text-2);
  cursor: pointer;
  font-size: 0.9rem;
}

.node-title {
  margin: 0.25rem 0;
  font-size: 1.1rem;
  font-weight: 600;
  color: #fff;
}

.node-meta {
  margin: 0.25rem 0 0.85rem;
  font-size: 0.8rem;
  color: var(--vp-c-text-2);
}

.view-btn {
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
