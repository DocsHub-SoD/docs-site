# Getting Started with Shape of Dreams Modding

::: info Work in Progress / Note on Modding Methods
**Please note**: The guide below currently serves as an initial placeholder focused on BepInEx. *Shape of Dreams* supports multiple simpler, native modding approaches (such as the engine's built-in **DewMod** loader, which requires no external injectors). Comprehensive documentation for each of these native modding methods will be published here shortly.
:::

Welcome to the **Shape of Dreams** modding community! This guide provides a rapid-onboarding overview of the game's modding stack, runtime architecture, and how to create your first mod.

---

## 1. Modding Architecture & Tech Stack

Shape of Dreams is built on **Unity (C#)** with standard .NET assemblies. Community modding relies on the battle-tested Unity modding stack:

```
┌──────────────────────────────────────────┐
│             Your Custom Mod              │
├──────────────────────────────────────────┤
│        HarmonyX (Runtime Patching)       │
├──────────────────────────────────────────┤
│     BepInEx 5.x (Mod Loader & Injection) │
├──────────────────────────────────────────┤
│      Shape of Dreams (Game Engine)       │
└──────────────────────────────────────────┘
```

### Key Components:
- **[BepInEx 5](https://github.com/BepInEx/BepInEx)**: The mod loader that hooks into the game process on launch, loads custom DLLs from the `BepInEx/plugins/` folder, and sets up logging.
- **[HarmonyX](https://github.com/BepInEx/HarmonyX)**: The runtime method-patching library. It allows you to intercept, modify, prefix, postfix, or replace internal game methods without decompiling or permanently rewriting game binaries.
- **`Dew.Core.dll` / `Assembly-CSharp.dll`**: The core game assemblies containing all gameplay logic (actors, abilities, cooldowns, stats, UI).

---

## 2. Environment Setup

To begin developing mods:

1. **Install .NET SDK**:
   - Install [.NET 6.0 SDK](https://dotnet.microsoft.com/download) or higher (the game uses modern C# standards).
2. **Install an IDE**:
   - Visual Studio, JetBrains Rider, or VS Code with C# Dev Kit.
3. **Decompiler (Essential for Exploring Logic)**:
   - Download **[dnSpy](https://github.com/dnSpy/dnSpy)** or **[ILSpy](https://github.com/icsharpcode/ILSpy)** to view disassembled game methods while referencing this documentation.

---

## 3. Anatomy of a Minimal Mod

Every BepInEx plugin starts with a class deriving from `BaseUnityPlugin`:

```csharp
using BepInEx;
using HarmonyLib;

namespace MyFirstSoDMod
{
    [BepInPlugin("com.username.sod.myfirstmod", "My First Mod", "1.0.0")]
    public class MyFirstModPlugin : BaseUnityPlugin
    {
        private void Awake()
        {
            // Initialize Harmony instance and apply all patches in this assembly
            Harmony harmony = new Harmony("com.username.sod.myfirstmod");
            harmony.PatchAll();

            Logger.LogInfo("My First SoD Mod loaded successfully!");
        }
    }
}
```

---

## 4. Hooking Game Logic with Harmony

Harmony uses annotations (`[HarmonyPatch]`) to target game classes and methods documented in this API portal.

### Example: Intercepting Spell Casts
Suppose you want to detect when an entity casts a spell or ability. Looking at the [`AbilityTrigger`](/api/Global.AbilityTrigger) or [`AbilityInstance`](/api/Global.AbilityInstance) documentation, we can write a Prefix patch:

```csharp
using HarmonyLib;
using UnityEngine;

namespace MyFirstSoDMod
{
    // Target the AbilityTrigger class and its Cast method
    [HarmonyPatch(typeof(AbilityTrigger), nameof(AbilityTrigger.Cast))]
    public static class AbilityTriggerCastPatch
    {
        // Prefix runs BEFORE the original game method executes
        // Return true to allow original method to run, return false to block it!
        [HarmonyPrefix]
        public static bool Prefix(AbilityTrigger __instance)
        {
            Debug.Log($"[SoD Mod] Cast triggered on ability: {__instance.name}");
            
            // Allow cast to proceed
            return true;
        }
    }
}
```

---

## 5. Next Steps & Where to Go

- **[Explore Core Classes](/api/Global.AbilityInstance)**: Dive into abilities, actor lifecycle, and combat calculation.
- **[Full API Catalog](/catalog)**: Browse all 897 classes, structs, and interfaces.
- **Offline & AI Agent Usage**: Read how to query our offline SQLite database `api.db` directly using your AI coding assistant in the [docs-data repository](https://github.com/DocsHub-SoD/docs-data).
