# Class: ModItem

- **Category:** <span class="cat-dot" style="--cat-color: #eab308" data-cat="Items & Economy"></span> Items & Economy
- **Namespace:** `Global`
- **Assembly:** `Dew.Core.dll`

```csharp
public class ModItem
```

## Fields (11)

::: details Click to expand Fields (11)

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`assemblyPaths`** | `public string[] assemblyPaths` |  |
| **`description`** | `public string description` |  |
| **`descriptionRichText`** | `public string descriptionRichText` |  |
| **`icon`** | `public Texture2D icon` |  |
| **`iconPath`** | `public string iconPath` |  |
| **`metadata`** | `public ModMetadata metadata` |  |
| **`path`** | `public string path` |  |
| **`previewPath`** | `public string previewPath` |  |
| **`publishedFileId`** | `public ulong publishedFileId` |  |
| **`source`** | `public ModSourceType source` |  |
| **`state`** | `public ModItemState state` |  |

:::


## Architecture & Relationships

::: details Click to expand Architecture & Relationships

### Used By (4)

*Classes and systems that invoke, reference, or depend on `ModItem`:*

[DewMod](/api/Global.DewMod) · [LoadedModInstance](/api/Global.LoadedModInstance) · [ModBehaviour](/api/Global.ModBehaviour) · `UI_ModManager_Item`

### Dependencies (1)

*Types and components that `ModItem` references or depends upon:*

[ModMetadata](/api/Global.ModMetadata)

### Related Enums (2)

*Enumerations referenced in fields, properties, or method signatures:*

<a href="/enums#moditemstate" class="enum-link" data-tooltip="Ok=0 · InvalidMetadata=1 · IdConflict=2">ModItemState</a> · <a href="/enums#modsourcetype" class="enum-link" data-tooltip="Local=0 · Steam=1">ModSourceType</a>

:::
