# Class: UI_GamepadNavigationHint

- **Namespace:** `Global`
- **Assembly:** `Dew.Core.dll`

```csharp
public class UI_GamepadNavigationHint : MonoBehaviour, IGamepadNavigationHint
```

## Fields

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`down`** | `[Header("Down")]
[ShowIf("useDifferentNavigationsPerDirection", true)]
[HideLabel]
public UI_GamepadNavigationHint.NavigationSettings down` |  |
| **`left`** | `[Header("Left")]
[ShowIf("useDifferentNavigationsPerDirection", true)]
[HideLabel]
public UI_GamepadNavigationHint.NavigationSettings left` |  |
| **`navigation`** | `[HideIf("useDifferentNavigationsPerDirection", true)]
[HideLabel]
public UI_GamepadNavigationHint.NavigationSettings navigation` |  |
| **`right`** | `[Header("Right")]
[ShowIf("useDifferentNavigationsPerDirection", true)]
[HideLabel]
public UI_GamepadNavigationHint.NavigationSettings right` |  |
| **`up`** | `[Header("Up")]
[ShowIf("useDifferentNavigationsPerDirection", true)]
[HideLabel]
public UI_GamepadNavigationHint.NavigationSettings up` |  |
| **`useDifferentNavigationsPerDirection`** | `[ToggleLeft]
public bool useDifferentNavigationsPerDirection` |  |

## Methods

### `TryGetDown(out IGamepadFocusable)`

```csharp
public bool TryGetDown(out IGamepadFocusable next)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `next` | [IGamepadFocusable](/api/Global.IGamepadFocusable) |  |

**Returns:** `bool`

### `TryGetLeft(out IGamepadFocusable)`

```csharp
public bool TryGetLeft(out IGamepadFocusable next)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `next` | [IGamepadFocusable](/api/Global.IGamepadFocusable) |  |

**Returns:** `bool`

### `TryGetRight(out IGamepadFocusable)`

```csharp
public bool TryGetRight(out IGamepadFocusable next)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `next` | [IGamepadFocusable](/api/Global.IGamepadFocusable) |  |

**Returns:** `bool`

### `TryGetUp(out IGamepadFocusable)`

```csharp
public bool TryGetUp(out IGamepadFocusable next)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `next` | [IGamepadFocusable](/api/Global.IGamepadFocusable) |  |

**Returns:** `bool`
