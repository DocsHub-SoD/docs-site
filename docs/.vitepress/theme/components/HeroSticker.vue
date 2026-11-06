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
      title="Click to toggle"
    >
      <!-- State 1: Work in Progress Text -->
      <transition name="fade-switch" mode="out-in">
        <div v-if="!isRevealed" key="text" class="sticker-text-view">
          <div class="sticker-tape"></div>
          <div class="sticker-badge">🚧 WIP</div>
          <div class="sticker-quote">
            <span class="line-1">work in progress,</span>
            <span class="line-2">someday it'll look better</span>
          </div>
          <div class="sticker-hint">(click me)</div>
        </div>

        <!-- State 2: Ramsay Easter Egg -->
        <div v-else key="image" class="sticker-image-view">
          <img 
            src="/ramsey.webp" 
            alt="IT'S FUCKING RAW!!!" 
            class="ramsay-img"
          />
        </div>
      </transition>
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
  border-color: rgba(239, 68, 68, 0.6);
  transform: rotate(1deg);
}

.sticker-card.is-revealed:hover {
  transform: rotate(0deg) scale(1.025);
  border-color: rgba(239, 68, 68, 0.9);
}

/* --- Text View --- */
.sticker-text-view {
  width: 100%;
  height: 100%;
  padding: 1.5rem 1.25rem 1rem;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: space-between;
  text-align: center;
  position: relative;
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
  padding: 0.15rem 0.6rem;
  border-radius: 999px;
  margin-top: 0.25rem;
}

.sticker-quote {
  display: flex;
  flex-direction: column;
  gap: 0.35rem;
  margin: auto 0;
}

.line-1 {
  font-size: 1.05rem;
  font-weight: 600;
  color: var(--vp-c-text-1);
  font-style: italic;
  font-family: var(--vp-font-family-base);
}

.line-2 {
  font-size: 0.88rem;
  font-weight: 500;
  color: var(--vp-c-text-2);
}

.sticker-hint {
  font-size: 0.72rem;
  color: var(--vp-c-text-3);
  font-family: var(--vp-font-family-mono);
  transition: color 0.15s ease;
}

.sticker-card:hover .sticker-hint {
  color: #f59e0b;
}

/* --- Image View --- */
.sticker-image-view {
  width: 100%;
  height: 100%;
  position: relative;
}

.ramsay-img {
  width: 100%;
  height: 100%;
  object-fit: cover;
  display: block;
}

/* --- Crossfade transition --- */
.fade-switch-enter-active,
.fade-switch-leave-active {
  transition: opacity 0.25s ease, transform 0.25s ease;
}

.fade-switch-enter-from {
  opacity: 0;
  transform: scale(0.96);
}

.fade-switch-leave-to {
  opacity: 0;
  transform: scale(1.04);
}
</style>
