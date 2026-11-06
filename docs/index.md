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
      text: All types in graph
      link: /graph

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

<div style="margin-top: 3.5rem; padding: 1.5rem; border-radius: 10px; background: var(--vp-c-bg-soft); border: 1px solid var(--vp-c-divider);">
  <h2 style="margin-top: 0; font-size: 1.25rem; font-weight: 600; color: var(--vp-c-text-1);">Explore the Documentation</h2>
  <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 1.25rem; margin-top: 1rem;">
    <a href="/getting-started" style="padding: 1.25rem; border-radius: 8px; background: var(--vp-c-bg); border: 1px solid var(--vp-c-divider); text-decoration: none; color: inherit; display: flex; flex-direction: column; justify-content: space-between; transition: border-color 0.15s ease, transform 0.15s ease;">
      <div>
        <h3 style="margin: 0 0 0.5rem; font-size: 1.05rem; font-weight: 600; color: var(--vp-c-brand-1);">Just starting? →</h3>
        <p style="margin: 0; font-size: 0.88rem; line-height: 1.5; color: var(--vp-c-text-2);">
          First time modding Shape of Dreams? Follow our beginner setup guide to configure BepInEx 5, hook into game methods with Harmony, understand the DewMod lifecycle, and build your very first working mod.
        </p>
      </div>
      <span style="margin-top: 0.85rem; font-size: 0.8rem; font-weight: 600; color: var(--vp-c-brand-1);">Read Getting Started Guide →</span>
    </a>
    <a href="/catalog" style="padding: 1.25rem; border-radius: 8px; background: var(--vp-c-bg); border: 1px solid var(--vp-c-divider); text-decoration: none; color: inherit; display: flex; flex-direction: column; justify-content: space-between; transition: border-color 0.15s ease, transform 0.15s ease;">
      <div>
        <h3 style="margin: 0 0 0.5rem; font-size: 1.05rem; font-weight: 600; color: var(--vp-c-brand-1);">Know what you're doing? →</h3>
        <p style="margin: 0; font-size: 0.88rem; line-height: 1.5; color: var(--vp-c-text-2);">
          Ready to dive straight into the code? Browse the Full Type Catalog of all 897 classes, structs, and enums, complete with C# signatures, parameters, [Server] attributes, and cross-class dependencies.
        </p>
      </div>
      <span style="margin-top: 0.85rem; font-size: 0.8rem; font-weight: 600; color: var(--vp-c-brand-1);">Open Full Type Catalog (897) →</span>
    </a>
  </div>
</div>
