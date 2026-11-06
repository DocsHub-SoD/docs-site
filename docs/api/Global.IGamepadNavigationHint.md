# Interface: IGamepadNavigationHint

- **Category:** <span class="cat-dot" style="--cat-color: #ec4899" data-cat="User Interface"></span> User Interface
- **Namespace:** `Global`
- **Assembly:** `Dew.Core.dll`

```csharp
public interface IGamepadNavigationHint
```

## Methods

### `TryGetDown(out IGamepadFocusable)`

Return false to fallback to default generic navigation

```csharp
bool TryGetDown(out IGamepadFocusable next)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `next` | [`IGamepadFocusable`](/api/Global.IGamepadFocusable) |  |

**Returns:** `bool`

### `TryGetLeft(out IGamepadFocusable)`

Return false to fallback to default generic navigation

```csharp
bool TryGetLeft(out IGamepadFocusable next)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `next` | [`IGamepadFocusable`](/api/Global.IGamepadFocusable) |  |

**Returns:** `bool`

### `TryGetRight(out IGamepadFocusable)`

Return false to fallback to default generic navigation

```csharp
bool TryGetRight(out IGamepadFocusable next)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `next` | [`IGamepadFocusable`](/api/Global.IGamepadFocusable) |  |

**Returns:** `bool`

### `TryGetUp(out IGamepadFocusable)`

Return false to fallback to default generic navigation

```csharp
bool TryGetUp(out IGamepadFocusable next)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `next` | [`IGamepadFocusable`](/api/Global.IGamepadFocusable) |  |

**Returns:** `bool`
