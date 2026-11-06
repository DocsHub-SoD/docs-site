# Class: PlayLobby_Character

- **Category:** <span class="cat-dot" style="--cat-color: #06b6d4" data-cat="Networking"></span> Networking
- **Namespace:** `Global`
- **Assembly:** `Dew.Core.dll`
- **Attributes:** `[LogicUpdatePriority]`
- **Inheritance / Derived:** [LogicBehaviour](/api/Global.LogicBehaviour)

```csharp
[LogicUpdatePriority(2000)]
public class PlayLobby_Character : LogicBehaviour, ILogicUpdate
```

## Fields (5)

::: details Click to expand Fields (5)

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`characterRotation`** | `public float? characterRotation` |  |
| **`forceSetup`** | `public string forceSetup` |  |
| **`fxClick`** | `public GameObject fxClick` |  |
| **`model`** | `public CharacterModelDisplay model` |  |
| **`playerIndex`** | `public int playerIndex` |  |

:::

## Methods (4)

::: details `Click()`

```csharp
public void Click()
```

:::

::: details `FrameUpdate()`

```csharp
public override void FrameUpdate()
```

:::

::: details `IsLocalPlayer()`

```csharp
public bool IsLocalPlayer()
```

**Returns:** `bool`

:::

::: details `LogicUpdate(float)`

```csharp
public override void LogicUpdate(float dt)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `dt` | `float` |  |

:::


## Architecture & Relationships

::: details Click to expand Architecture & Relationships

### Used By (3)

*Classes and systems that invoke, reference, or depend on `PlayLobby_Character`:*

[PlayLobby_CharacterCamera](/api/Global.PlayLobby_CharacterCamera) · `UI_Lobby_ChangeCharacterGamepadButton` · `UI_Lobby_PlayerNametag`

### Dependencies (10)

*Types and components that `PlayLobby_Character` references or depends upon:*

[CharacterModelDisplay](/api/Global.CharacterModelDisplay) · [DewEffect](/api/Global.DewEffect) · [DewPlayer](/api/Global.DewPlayer) · [ListReturnHandle`1](/api/Global.ListReturnHandle`1) · [LobbyUIManager](/api/Global.LobbyUIManager) · [LogicBehaviour](/api/Global.LogicBehaviour) · [SafeAction`2](/api/Global.SafeAction`2) · [Skin](/api/Global.Skin) · `ToListNonAllocExtensions` · [UIManager](/api/Global.UIManager)

:::
