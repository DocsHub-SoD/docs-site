# Interface: IGamepadNavigationHint

- **Category:** <span class="cat-dot" style="--cat-color: #ec4899" data-cat="User Interface"></span> User Interface
- **Namespace:** `Global`
- **Assembly:** `Dew.Core.dll`

```csharp
public interface IGamepadNavigationHint
```

## Methods (4)

::: details `TryGetDown(out IGamepadFocusable)`

Return false to fallback to default generic navigation

```csharp
bool TryGetDown(out IGamepadFocusable next)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `next` | [`IGamepadFocusable`](/api/Global.IGamepadFocusable) |  |

**Returns:** `bool`

:::

::: details `TryGetLeft(out IGamepadFocusable)`

Return false to fallback to default generic navigation

```csharp
bool TryGetLeft(out IGamepadFocusable next)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `next` | [`IGamepadFocusable`](/api/Global.IGamepadFocusable) |  |

**Returns:** `bool`

:::

::: details `TryGetRight(out IGamepadFocusable)`

Return false to fallback to default generic navigation

```csharp
bool TryGetRight(out IGamepadFocusable next)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `next` | [`IGamepadFocusable`](/api/Global.IGamepadFocusable) |  |

**Returns:** `bool`

:::

::: details `TryGetUp(out IGamepadFocusable)`

Return false to fallback to default generic navigation

```csharp
bool TryGetUp(out IGamepadFocusable next)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `next` | [`IGamepadFocusable`](/api/Global.IGamepadFocusable) |  |

**Returns:** `bool`

:::


## Architecture & Relationships

::: details Click to expand Architecture & Relationships

### Used By (5)

*Classes and systems that invoke, reference, or depend on `IGamepadNavigationHint`:*

[GlobalUIManager](/api/Global.GlobalUIManager) · [UI_GamepadNavigationHint](/api/Global.UI_GamepadNavigationHint) · `UI_Lobby_Constellations_HeroConstellation` · `UI_Lobby_DejavuWindow` · `UI_TravelerStory_HeroConstellation`

### Dependencies (0)

*No outgoing class dependencies recorded.*

:::
