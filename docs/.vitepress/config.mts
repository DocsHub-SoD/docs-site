import { defineConfig } from 'vitepress'

export default defineConfig({
  title: "Shape of Dreams ModDocs",
  description: "Community API Documentation and Knowledge Base for Shape of Dreams modders",
  base: "/",
  cleanUrls: true,
  themeConfig: {
    nav: [
      { text: "Getting Started", link: "/getting-started" },
      { text: "API Catalog", link: "/catalog" },
      { text: "Core Classes", link: "/api/Global.AbilityInstance" },
      {
        text: "v1.0 (Latest)",
        items: [
          { text: "v1.0 (Current)", link: "/" },
          { text: "Version History", link: "/catalog" }
        ]
      },
      { text: "GitHub", link: "https://github.com/DocsHub-SoD" }
    ],
    search: {
      provider: 'local'
    },
    sidebar: [
      {
        text: 'Modding Guides',
        items: [
          { text: 'Getting Started', link: '/getting-started' }
        ]
      },
      {
        text: 'API Reference',
        items: [
          { text: 'Overview', link: '/' },
          { text: 'Full Type Catalog (897)', link: '/catalog' }
        ]
      },
      {
        text: 'Key Gameplay Classes',
        collapsed: false,
        items: [
          { text: 'AbilityInstance (Spells & Skills)', link: '/api/Global.AbilityInstance' },
          { text: 'AbilityTrigger (Ability Triggers)', link: '/api/Global.AbilityTrigger' },
          { text: 'Actor (Entities, Players, Enemies)', link: '/api/Global.Actor' },
          { text: 'ActorManager (Actor Management)', link: '/api/Global.ActorManager' },
          { text: 'StatusEffect (Statuses & Buffs)', link: '/api/Global.StatusEffect' },
          { text: 'DamageData (Damage Calculation)', link: '/api/Global.DamageData' },
          { text: 'ConsoleManager (In-Game Console)', link: '/api/Global.ConsoleManager' },
          { text: 'AudioManager (Audio System)', link: '/api/Global.AudioManager' }
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
