# Class: GameResultManager

- **Category:** <span class="cat-dot" style="--cat-color: #3b82f6" data-cat="Managers & Systems"></span> Managers & Systems
- **Namespace:** `Global`
- **Assembly:** `Dew.Core.dll`
- **Inheritance / Derived:** [DewNetworkBehaviour](/api/Global.DewNetworkBehaviour) → `NetworkedManagerBase` → [GameResultManager](/api/Global.GameResultManager)

```csharp
public class GameResultManager : NetworkedManagerBase<GameResultManager>, ILogicUpdate
```

## Fields (3)

::: details Click to expand Fields (3)

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`ClientEvent_OnGameConcluded`** | `public SafeAction<DewGameResult> ClientEvent_OnGameConcluded` | Called everywhere when server wraps up the game and results are sent to clients.This is not used for conceded (exited out) games. |
| **`current`** | `public DewGameResult current` | Currently registered game result. The server gives this out to clients periodically, and when the game concludes.Available everywhere. |
| **`onUpdateGameResult`** | `public SafeAction<DewGameResult> onUpdateGameResult` | Called on server when updating game result mid-game or when the game has concluded.You can use this to modify stats or add custom ones to the result, before it gets sent to clients. |

:::

## Properties (1)

::: details Click to expand Properties (1)

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`tracked`** | `[SaveVar(SaveVarFlags.Default)] public DewGameResult tracked { get; }` | Only available on server. |

:::

## Methods (5)

::: details `OnStartClient()`

```csharp
public override void OnStartClient()
```

:::

::: details `OnStartServer()`

```csharp
public override void OnStartServer()
```

:::

::: details `StartTrackingPlayer(DewPlayer)`

```csharp
public void StartTrackingPlayer(DewPlayer p)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `p` | [`DewPlayer`](/api/Global.DewPlayer) |  |

:::

::: details `UpdateAndSendMidGameResultToClients()`

```csharp
public void UpdateAndSendMidGameResultToClients()
```

:::

::: details `WrapUp(ResultType)`

Ends tracking and shows statistics to everyone.

```csharp
public void WrapUp(DewGameResult.ResultType type)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `type` | [`DewGameResult.ResultType`](/api/Global.DewGameResult) |  |

:::
