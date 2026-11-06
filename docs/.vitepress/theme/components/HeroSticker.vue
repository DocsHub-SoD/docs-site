<script setup>
import { ref } from 'vue'

const isRevealed = ref(false)

function toggleReveal() {
  isRevealed.value = !isRevealed.value
}
</script>

<template>
  <div class="hero-sticker-container">
    <div 
      class="sticker-card" 
      :class="{ 'is-revealed': isRevealed }"
      @click="toggleReveal"
    >
      <!-- Layer 1: Work in Progress Text -->
      <div class="sticker-layer sticker-text-view">
        <div class="sticker-tape"></div>
        <div class="sticker-badge">🚧 WIP</div>
        <div class="sticker-quote">
          <span class="line-1">work in progress,</span>
          <span class="line-2">someday it'll look better</span>
        </div>
      </div>

      <!-- Layer 2: Preloaded Ramsay Image (always mounted, zero-FOUC instant reveal) -->
      <div class="sticker-layer sticker-image-view">
        <img 
          src="/ramsey.webp" 
          alt="IT'S FUCKING RAW!!!" 
          class="ramsay-img"
          loading="eager"
          decoding="async"
        />
      </div>
    </div>
  </div>
</template>

<style scoped>
.hero-sticker-container {
  display: flex;
  justify-content: center;
  align-items: center;
  width: 100%;
  height: 100%;
  min-height: 280px;
  user-select: none;
}

.sticker-card {
  position: relative;
  width: 320px;
  height: 256px;
  border-radius: 14px;
  background: var(--vp-c-bg-soft);
  border: 2px dashed rgba(245, 158, 11, 0.45);
  box-shadow: 0 14px 34px rgba(0, 0, 0, 0.35);
  transform: rotate(-2deg);
  cursor: pointer;
  overflow: hidden;
  transition: transform 0.25s cubic-bezier(0.16, 1, 0.3, 1), 
              border-color 0.25s ease, 
              box-shadow 0.25s ease;
}

.sticker-card:hover {
  transform: rotate(0deg) scale(1.025);
  border-color: rgba(245, 158, 11, 0.85);
  box-shadow: 0 18px 40px rgba(0, 0, 0, 0.45);
}

.sticker-card.is-revealed {
  border-style: solid;
  border-color: rgba(239, 68, 68, 0.65);
  transform: rotate(1deg);
}

.sticker-card.is-revealed:hover {
  transform: rotate(0deg) scale(1.025);
  border-color: rgba(239, 68, 68, 0.95);
}

/* --- Stacked Layers for Zero-FOUC Crossfade --- */
.sticker-layer {
  position: absolute;
  inset: 0;
  width: 100%;
  height: 100%;
  transition: opacity 0.25s ease, transform 0.25s cubic-bezier(0.16, 1, 0.3, 1);
}

.sticker-text-view {
  opacity: 1;
  transform: scale(1);
  pointer-events: auto;
  padding: 1.6rem 1.25rem 1.4rem;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: space-between;
  text-align: center;
}

.sticker-image-view {
  opacity: 0;
  transform: scale(0.97);
  pointer-events: none;
}

.sticker-card.is-revealed .sticker-text-view {
  opacity: 0;
  transform: scale(1.03);
  pointer-events: none;
}

.sticker-card.is-revealed .sticker-image-view {
  opacity: 1;
  transform: scale(1);
  pointer-events: auto;
}

.sticker-tape {
  position: absolute;
  top: -8px;
  left: 50%;
  transform: translateX(-50%);
  width: 70px;
  height: 18px;
  background: rgba(245, 158, 11, 0.22);
  border: 1px dashed rgba(245, 158, 11, 0.4);
  backdrop-filter: blur(4px);
  border-radius: 2px;
}

.sticker-badge {
  font-size: 0.72rem;
  font-weight: 700;
  text-transform: uppercase;
  letter-spacing: 0.08em;
  color: #f59e0b;
  background: rgba(245, 158, 11, 0.12);
  padding: 0.18rem 0.65rem;
  border-radius: 999px;
  margin-top: 0.35rem;
}

.sticker-quote {
  display: flex;
  flex-direction: column;
  gap: 0.4rem;
  margin: auto 0;
}

.line-1 {
  font-size: 1.08rem;
  font-weight: 600;
  color: var(--vp-c-text-1);
  font-style: italic;
  font-family: var(--vp-font-family-base);
}

.line-2 {
  font-size: 0.9rem;
  font-weight: 500;
  color: var(--vp-c-text-2);
}

.ramsay-img {
  width: 100%;
  height: 100%;
  object-fit: cover;
  display: block;
}
</style>
