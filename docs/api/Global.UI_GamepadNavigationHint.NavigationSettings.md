# Struct: UI_GamepadNavigationHint.NavigationSettings

- **Category:** <span class="cat-dot" style="--cat-color: #ec4899" data-cat="User Interface"></span> User Interface
- **Namespace:** `Global`
- **Assembly:** `Dew.Core.dll`

```csharp
[Serializable]
[InlineProperty]
public struct UI_GamepadNavigationHint.NavigationSettings
```

## Fields (4)

::: details Click to expand Fields (4)

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`canFallbackToGeneric`** | `[ShowIf("@navigation != GamepadNavigation.Generic \|\| limitToChildren", true)] [ToggleLeft] public bool canFallbackToGeneric` |  |
| **`customTarget`** | `[ShowIf("@navigation == GamepadNavigation.Custom", true)] public GameObject customTarget` |  |
| **`limitToChildren`** | `[ShowIf("@navigation != GamepadNavigation.Custom", true)] [ToggleLeft] public bool limitToChildren` |  |
| **`navigation`** | `[EnumToggleButtons] [HideLabel] public GamepadNavigation navigation` |  |

:::


## Architecture & Relationships

::: details Click to expand Architecture & Relationships

### Used By (0)

*No incoming dependencies recorded.*

### Dependencies (0)

*No outgoing class dependencies recorded.*

### Related Enums (1)

*Enumerations referenced in fields, properties, or method signatures:*

<a href="/enums#gamepadnavigation" class="enum-link" data-tooltip="Generic=0 · Grid=10 · GridWrapAround=11 · GridLong=12 · Wide=20 (+2 more)">GamepadNavigation</a>

:::
