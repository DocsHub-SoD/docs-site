import DefaultTheme from 'vitepress/theme'
import { h } from 'vue'
import GraphView from './components/GraphView.vue'
import HeroSticker from './components/HeroSticker.vue'
import './custom.css'

export default {
  extends: DefaultTheme,
  Layout() {
    return h(DefaultTheme.Layout, null, {
      'home-hero-image': () => h(HeroSticker)
    })
  },
  enhanceApp({ app }) {
    app.component('GraphView', GraphView)
    app.component('HeroSticker', HeroSticker)
  }
}
