# Class: GameResultManager

- **Category:** <span class="cat-dot" style="--cat-color: #3b82f6" data-cat="Managers & Systems"></span> Managers & Systems
- **Namespace:** `Global`
- **Assembly:** `Dew.Core.dll`
- **Inheritance / Derived:** [DewNetworkBehaviour](/api/Global.DewNetworkBehaviour) → `NetworkedManagerBase` → [GameResultManager](/api/Global.GameResultManager)

```csharp
public class GameResultManager : NetworkedManagerBase<GameResultManager>, ILogicUpdate
```

## Fields

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`ClientEvent_OnGameConcluded`** | `public SafeAction<DewGameResult> ClientEvent_OnGameConcluded` | Called everywhere when server wraps up the game and results are sent to clients.This is not used for conceded (exited out) games. |
| **`current`** | `public DewGameResult current` | Currently registered game result. The server gives this out to clients periodically, and when the game concludes.Available everywhere. |
| **`onUpdateGameResult`** | `public SafeAction<DewGameResult> onUpdateGameResult` | Called on server when updating game result mid-game or when the game has concluded.You can use this to modify stats or add custom ones to the result, before it gets sent to clients. |

## Properties

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`tracked`** | `[SaveVar(SaveVarFlags.Default)] public DewGameResult tracked { get; }` | Only available on server. |

## Methods

### `OnStartClient()`

```csharp
public override void OnStartClient()
```

### `OnStartServer()`

```csharp
public override void OnStartServer()
```

### `StartTrackingPlayer(DewPlayer)`

```csharp
public void StartTrackingPlayer(DewPlayer p)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `p` | [`DewPlayer`](/api/Global.DewPlayer) |  |

### `UpdateAndSendMidGameResultToClients()`

```csharp
public void UpdateAndSendMidGameResultToClients()
```

### `WrapUp(ResultType)`

Ends tracking and shows statistics to everyone.

```csharp
public void WrapUp(DewGameResult.ResultType type)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `type` | [`DewGameResult.ResultType`](/api/Global.DewGameResult) |  |
