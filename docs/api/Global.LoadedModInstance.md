# Class: LoadedModInstance

- **Category:** <span class="cat-dot" style="--cat-color: #64748b" data-cat="Misc & Utility"></span> Misc & Utility
- **Namespace:** `Global`
- **Assembly:** `Dew.Core.dll`

```csharp
public class LoadedModInstance
```

## Fields (4)

::: details Click to expand Fields (4)

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`container`** | `public GameObject container` |  |
| **`isAlteringGameplay`** | `public bool isAlteringGameplay` | This must be set to true, if this mod is altering gameplay in any way. This will show mod icon in the lobby list to let the clients know prior to joining your game.This is automatically set to true if the mod contains any JSON overrides. |
| **`mod`** | `public ModItem mod` |  |
| **`registeredCommands`** | `public List<string> registeredCommands` |  |

:::


## Architecture & Relationships

::: details Click to expand Architecture & Relationships

### Used By (3)

*Classes and systems that invoke, reference, or depend on `LoadedModInstance`:*

[DewMod](/api/Global.DewMod) · [ModBehaviour](/api/Global.ModBehaviour) · `UI_Settings_ModsSection_Item`

### Dependencies (1)

*Types and components that `LoadedModInstance` references or depends upon:*

[ModItem](/api/Global.ModItem)

:::
