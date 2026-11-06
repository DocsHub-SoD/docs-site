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
| **`down`** | `[Header("Down")] [ShowIf("useDifferentNavigationsPerDirection", true)] [HideLabel] public UI_GamepadNavigationHint.NavigationSettings down` |  |
| **`left`** | `[Header("Left")] [ShowIf("useDifferentNavigationsPerDirection", true)] [HideLabel] public UI_GamepadNavigationHint.NavigationSettings left` |  |
| **`navigation`** | `[HideIf("useDifferentNavigationsPerDirection", true)] [HideLabel] public UI_GamepadNavigationHint.NavigationSettings navigation` |  |
| **`right`** | `[Header("Right")] [ShowIf("useDifferentNavigationsPerDirection", true)] [HideLabel] public UI_GamepadNavigationHint.NavigationSettings right` |  |
| **`up`** | `[Header("Up")] [ShowIf("useDifferentNavigationsPerDirection", true)] [HideLabel] public UI_GamepadNavigationHint.NavigationSettings up` |  |
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
