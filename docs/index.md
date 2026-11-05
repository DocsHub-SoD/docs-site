---
layout: home

hero:
  name: "Shape of Dreams"
  text: "Modding Documentation"
  tagline: "Community-maintained API reference, method signatures, and guides for modders"
  actions:
    - theme: brand
      text: Getting Started
      link: /getting-started
    - theme: alt
      text: API Reference
      link: /api/Global.AbilityInstance
    - theme: alt
      text: All Types (897)
      link: /catalog

features:
  - icon: 🛠️
    title: Getting Started
    details: Basic setup guide for BepInEx 5 and Harmony runtime patching.
  - icon: 🔍
    title: Searchable API
    details: Client-side search across all 897 classes, structs, enums, and methods.
  - icon: 🔗
    title: Cross-Linked Types
    details: Parameter types, interfaces, and base classes link directly to their definitions.
  - icon: 💾
    title: SQLite Database
    details: The raw data is available as an indexed SQLite database in the docs-data repository for local querying or AI tools.
---

<div style="margin-top: 3rem; padding: 1.5rem; border-radius: 8px; background: var(--vp-c-bg-soft); border: 1px solid var(--vp-c-divider);">
  <h2 style="margin-top: 0; font-size: 1.25rem; font-weight: 600;">Navigation</h2>
  <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(220px, 1fr)); gap: 1rem; margin-top: 1rem;">
    <a href="/getting-started" style="padding: 1rem; border-radius: 6px; background: var(--vp-c-bg); border: 1px solid var(--vp-c-divider); text-decoration: none; color: inherit; display: block;">
      <h3 style="margin: 0; font-size: 1rem; color: var(--vp-c-brand-1);">Getting Started →</h3>
      <p style="margin: 0.35rem 0 0; font-size: 0.85rem; color: var(--vp-c-text-2);">BepInEx setup and a basic Harmony patch example.</p>
    </a>
    <a href="/api/Global.AbilityInstance" style="padding: 1rem; border-radius: 6px; background: var(--vp-c-bg); border: 1px solid var(--vp-c-divider); text-decoration: none; color: inherit; display: block;">
      <h3 style="margin: 0; font-size: 1rem; color: var(--vp-c-brand-1);">Core Classes →</h3>
      <p style="margin: 0.35rem 0 0; font-size: 0.85rem; color: var(--vp-c-text-2);">AbilityInstance, Actor, StatusEffect, and related types.</p>
    </a>
    <a href="/catalog" style="padding: 1rem; border-radius: 6px; background: var(--vp-c-bg); border: 1px solid var(--vp-c-divider); text-decoration: none; color: inherit; display: block;">
      <h3 style="margin: 0; font-size: 1rem; color: var(--vp-c-brand-1);">Type Catalog →</h3>
      <p style="margin: 0.35rem 0 0; font-size: 0.85rem; color: var(--vp-c-text-2);">Index of all 897 types in the game assembly.</p>
    </a>
  </div>
</div>
