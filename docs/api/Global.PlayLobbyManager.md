# Class: PlayLobbyManager

- **Category:** <span class="cat-dot" style="--cat-color: #3b82f6" data-cat="Managers & Systems"></span> Managers & Systems
- **Namespace:** `Global`
- **Assembly:** `Dew.Core.dll`
- **Inheritance / Derived:** [LogicBehaviour](/api/Global.LogicBehaviour) → `ManagerBase` → [PlayLobbyManager](/api/Global.PlayLobbyManager)

```csharp
public class PlayLobbyManager : ManagerBase<PlayLobbyManager>, ILogicUpdate
```

## Fields (4)

::: details Click to expand Fields (4)

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`fxRiftActivate`** | `public GameObject fxRiftActivate` |  |
| **`fxRiftCharge`** | `public GameObject fxRiftCharge` |  |
| **`fxRiftLoop`** | `public GameObject fxRiftLoop` |  |
| **`fxRiftOpen`** | `public GameObject fxRiftOpen` |  |

:::

## Properties (3)

::: details Click to expand Properties (3)

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`isEveryoneReady`** | `public bool isEveryoneReady { get; }` |  |
| **`numOfReadyPlayers`** | `public int numOfReadyPlayers { get; }` |  |
| **`numOfReadyPlayersMax`** | `public int numOfReadyPlayersMax { get; }` |  |

:::

## Methods (9)

::: details `AddStartGameCondition(Func&lt;string&gt;)`

Given function must return a reason for start button unavailability. Return null for approval.

```csharp
public void AddStartGameCondition(Func<string> func)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `func` | `System.Func<TResult><string>` |  |

:::

::: details `CheckStartGameCondition(out string, bool)`

```csharp
public bool CheckStartGameCondition(out string reason, bool showMessage)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `reason` | `string` |  |
| `showMessage` | `bool` |  |

**Returns:** `bool`

:::

::: details `GoBack()`

```csharp
public void GoBack()
```

:::

::: details `JoinMidGame()`

```csharp
public void JoinMidGame()
```

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

::: details `RemoveStartGameCondition(Func&lt;string&gt;)`

```csharp
public void RemoveStartGameCondition(Func<string> func)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `func` | `System.Func<TResult><string>` |  |

:::

::: details `SetReady(bool)`

```csharp
public void SetReady(bool ready)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `ready` | `bool` |  |

:::

::: details `StartGame()`

```csharp
public void StartGame()
```

:::

::: details `ToggleReady()`

```csharp
public void ToggleReady()
```

:::


## Architecture & Relationships

::: details Click to expand Architecture & Relationships

### Used By (3)

*Classes and systems that invoke, reference, or depend on `PlayLobbyManager`:*

[GameMod_Limbo](/api/Global.GameMod_Limbo) · `UI_Lobby_ReadyStatusText` · `UI_Lobby_StartButtonController`

### Dependencies (14)

*Types and components that `PlayLobbyManager` references or depends upon:*

[DewBuildProfile](/api/Global.DewBuildProfile) · [DewEffect](/api/Global.DewEffect) · [DewLocalization](/api/Global.DewLocalization) · [DewNetworkManager](/api/Global.DewNetworkManager) · [DewPlayer](/api/Global.DewPlayer) · [DewResources](/api/Global.DewResources) · [GameSettingsManager](/api/Global.GameSettingsManager) · [LobbyUIManager](/api/Global.LobbyUIManager) · [LogicBehaviour](/api/Global.LogicBehaviour) · [ManagerBase`1](/api/Global.ManagerBase`1) · [MessageManager](/api/Global.MessageManager) · [NetworkedManagerBase`1](/api/Global.NetworkedManagerBase`1) · [SafeAction](/api/Global.SafeAction) · [UIManager](/api/Global.UIManager)

:::
