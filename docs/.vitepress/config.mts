import { defineConfig } from 'vitepress'

export default defineConfig({
  title: "Shape of Dreams ModDocs",
  description: "Community API Documentation and Knowledge Base for Shape of Dreams modders",
  base: "/",
  cleanUrls: true,
  head: [
    ['link', { rel: 'preload', as: 'image', href: '/ramsey.webp', type: 'image/webp' }]
  ],
  themeConfig: {
    nav: [
      { text: "Getting Started", link: "/getting-started" },
      { text: "Graph View", link: "/graph" }
    ],
    search: {
      provider: 'local'
    },
    sidebar: [
      {
        text: 'Modding Guides',
        items: [
          { text: 'Getting Started', link: '/getting-started' },
          { text: 'Using Docs with AI', link: '/ai-workflows' }
        ]
      },
      {
        text: 'Visual Exploration & Reference',
        items: [
          { text: 'Interactive Graph View', link: '/graph' },
          { text: 'Full Type Catalog (897)', link: '/catalog' },
          { text: 'Enums & Constants (118)', link: '/enums' }
        ]
      },
      {
        text: 'Core Gameplay Systems',
        collapsed: false,
        items: [
          { text: 'Abilities & Spells', link: '/api/Global.AbilityInstance' },
          { text: 'Actors & Entities', link: '/api/Global.Actor' },
          { text: 'Effects & Buffs', link: '/api/Global.StatusEffect' }
        ]
      },
      {
        text: 'Architecture & Engine',
        collapsed: true,
        items: [
          { text: 'Managers & Services', link: '/api/Global.ActorManager' },
          { text: 'Console & Audio', link: '/api/Global.ConsoleManager' }
        ]
      },
      {
        text: 'Data & Calculations',
        collapsed: true,
        items: [
          { text: 'Damage Calculations', link: '/api/Global.DamageData' }
        ]
      }
    ],
    socialLinks: [
      { icon: 'github', link: 'https://github.com/DocsHub-SoD' }
    ],
    footer: {
      message: 'Independent community documentation project. Not affiliated with, endorsed, or sponsored by Lizard Smoothie or Shape of Dreams developers.',
      copyright: 'Shape of Dreams is a trademark of Lizard Smoothie. All game assets, class names, and code references belong to their respective copyright holders.'
    }
  }
})
