import { defineConfig } from 'vitepress'

export default defineConfig({
  title: "Shape of Dreams ModDocs",
  description: "Community API Documentation and Knowledge Base for Shape of Dreams modders",
  base: "/",
  cleanUrls: true,
  themeConfig: {
    nav: [
      { text: "Getting Started", link: "/getting-started" },
      { text: "Graph View", link: "/graph" },
      { text: "API Catalog", link: "/catalog" },
      { text: "AI Workflows", link: "/ai-workflows" },
      {
        text: "v1.0 (Latest)",
        items: [
          { text: "v1.0 (Current)", link: "/" },
          { text: "Version History", link: "/catalog" }
        ]
      }
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
        text: 'Visual Exploration',
        items: [
          { text: 'Interactive Graph View', link: '/graph' },
          { text: 'Full Type Catalog (897)', link: '/catalog' }
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
      message: 'Maintained by the Shape of Dreams Modding Community',
      copyright: 'Shape of Dreams API Documentation'
    }
  }
})
