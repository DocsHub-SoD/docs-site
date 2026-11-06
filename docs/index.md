---
layout: home

hero:
  name: "Shape of Dreams"
  text: "Modding Documentation"
  tagline: "API reference, method signatures, and guides for modding Shape of Dreams"
  image:
    src: /ramsey.webp
    alt: "Work in progress"
  actions:
    - theme: brand
      text: Getting Started
      link: /getting-started
    - theme: alt
      text: All types in graph
      link: /graph

features:
  - icon: 🛠️
    title: Modding Setup
    details: How to install BepInEx 5, write Harmony patches, and configure your mod for DewMod.
  - icon: 🔍
    title: Fast Search
    details: Search across all 897 classes, structs, enums, fields, and method declarations.
  - icon: 🔗
    title: Cross-References
    details: Parameters, interfaces, base classes, and related enums link directly to their definitions.
  - icon: 💾
    title: Offline SQLite
    details: Grab api.db from the docs-data repository to query offline or use with local LLM tools.
---

<div style="margin-top: 3.5rem; padding: 1.5rem; border-radius: 10px; background: var(--vp-c-bg-soft); border: 1px solid var(--vp-c-divider);">
  <h2 style="margin-top: 0; font-size: 1.25rem; font-weight: 600; color: var(--vp-c-text-1);">Explore the Documentation</h2>
  <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 1.25rem; margin-top: 1rem;">
    <a href="/getting-started" style="padding: 1.25rem; border-radius: 8px; background: var(--vp-c-bg); border: 1px solid var(--vp-c-divider); text-decoration: none; color: inherit; display: flex; flex-direction: column; justify-content: space-between; transition: border-color 0.15s ease, transform 0.15s ease;">
      <div>
        <h3 style="margin: 0 0 0.5rem; font-size: 1.05rem; font-weight: 600; color: var(--vp-c-brand-1);">Just starting? →</h3>
        <p style="margin: 0; font-size: 0.88rem; line-height: 1.5; color: var(--vp-c-text-2);">
          Step-by-step setup for BepInEx 5 and Harmony. Covers mod structure, registering with DewMod, and checking game logs when something doesn't load.
        </p>
      </div>
      <span style="margin-top: 0.85rem; font-size: 0.8rem; font-weight: 600; color: var(--vp-c-brand-1);">Getting Started Guide →</span>
    </a>
    <a href="/catalog" style="padding: 1.25rem; border-radius: 8px; background: var(--vp-c-bg); border: 1px solid var(--vp-c-divider); text-decoration: none; color: inherit; display: flex; flex-direction: column; justify-content: space-between; transition: border-color 0.15s ease, transform 0.15s ease;">
      <div>
        <h3 style="margin: 0 0 0.5rem; font-size: 1.05rem; font-weight: 600; color: var(--vp-c-brand-1);">Looking for a specific type? →</h3>
        <p style="margin: 0; font-size: 0.88rem; line-height: 1.5; color: var(--vp-c-text-2);">
          Browse all 897 classes, structs, and enums. Includes exact method signatures, network attributes ([Server], [ClientRpc]), parameter types, and caller references.
        </p>
      </div>
      <span style="margin-top: 0.85rem; font-size: 0.8rem; font-weight: 600; color: var(--vp-c-brand-1);">Full Type Catalog (897) →</span>
    </a>
  </div>
</div>
