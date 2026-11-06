# Class: UI_GamepadNavigationHint

- **Category:** <span class="cat-dot" style="--cat-color: #ec4899" data-cat="User Interface"></span> User Interface
- **Namespace:** `Global`
- **Assembly:** `Dew.Core.dll`

```csharp
public class UI_GamepadNavigationHint : MonoBehaviour, IGamepadNavigationHint
```

## Fields (6)

::: details Click to expand Fields (6)

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`down`** | `[Header] [Header("Down")] [ShowIf("useDifferentNavigationsPerDirection", true)] [HideLabel] public UI_GamepadNavigationHint.NavigationSettings down` |  |
| **`left`** | `[Header] [Header("Left")] [ShowIf("useDifferentNavigationsPerDirection", true)] [HideLabel] public UI_GamepadNavigationHint.NavigationSettings left` |  |
| **`navigation`** | `[HideIf("useDifferentNavigationsPerDirection", true)] [HideLabel] public UI_GamepadNavigationHint.NavigationSettings navigation` |  |
| **`right`** | `[Header] [Header("Right")] [ShowIf("useDifferentNavigationsPerDirection", true)] [HideLabel] public UI_GamepadNavigationHint.NavigationSettings right` |  |
| **`up`** | `[Header] [Header("Up")] [ShowIf("useDifferentNavigationsPerDirection", true)] [HideLabel] public UI_GamepadNavigationHint.NavigationSettings up` |  |
| **`useDifferentNavigationsPerDirection`** | `[ToggleLeft] public bool useDifferentNavigationsPerDirection` |  |

:::

## Methods (4)

::: details `TryGetDown(out IGamepadFocusable)`

```csharp
public bool TryGetDown(out IGamepadFocusable next)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `next` | [`IGamepadFocusable`](/api/Global.IGamepadFocusable) |  |

**Returns:** `bool`

:::

::: details `TryGetLeft(out IGamepadFocusable)`

```csharp
public bool TryGetLeft(out IGamepadFocusable next)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `next` | [`IGamepadFocusable`](/api/Global.IGamepadFocusable) |  |

**Returns:** `bool`

:::

::: details `TryGetRight(out IGamepadFocusable)`

```csharp
public bool TryGetRight(out IGamepadFocusable next)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `next` | [`IGamepadFocusable`](/api/Global.IGamepadFocusable) |  |

**Returns:** `bool`

:::

::: details `TryGetUp(out IGamepadFocusable)`

```csharp
public bool TryGetUp(out IGamepadFocusable next)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `next` | [`IGamepadFocusable`](/api/Global.IGamepadFocusable) |  |

**Returns:** `bool`

:::


## Architecture & Relationships

::: details Click to expand Architecture & Relationships

### Used By (0)

*No incoming dependencies recorded.*

### Dependencies (5)

*Types and components that `UI_GamepadNavigationHint` references or depends upon:*

[GlobalUIManager](/api/Global.GlobalUIManager) · [IGamepadFocusable](/api/Global.IGamepadFocusable) · [IGamepadNavigationHint](/api/Global.IGamepadNavigationHint) · [ManagerBase`1](/api/Global.ManagerBase`1) · [UI_GamepadFocusableGroup](/api/Global.UI_GamepadFocusableGroup)

### Related Enums (1)

*Enumerations referenced in fields, properties, or method signatures:*

<a href="/enums#gamepadnavigation" class="enum-link" data-tooltip="Generic=0 · Grid=10 · GridWrapAround=11 · GridLong=12 · Wide=20 (+2 more)">GamepadNavigation</a>

:::
