# Class: PlayLobbyManager

- **Namespace:** `Global`
- **Assembly:** `Dew.Core.dll`
- **Inheritance / Derived:** [LogicBehaviour](/api/Global.LogicBehaviour) → `ManagerBase` → [PlayLobbyManager](/api/Global.PlayLobbyManager)

```csharp
public class PlayLobbyManager : ManagerBase<PlayLobbyManager>, ILogicUpdate
```

## Fields

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`fxRiftActivate`** | `public GameObject fxRiftActivate` |  |
| **`fxRiftCharge`** | `public GameObject fxRiftCharge` |  |
| **`fxRiftLoop`** | `public GameObject fxRiftLoop` |  |
| **`fxRiftOpen`** | `public GameObject fxRiftOpen` |  |

## Properties

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`isEveryoneReady`** | `public bool isEveryoneReady { get; }` |  |
| **`numOfReadyPlayers`** | `public int numOfReadyPlayers { get; }` |  |
| **`numOfReadyPlayersMax`** | `public int numOfReadyPlayersMax { get; }` |  |

## Methods

### `AddStartGameCondition(Func&lt;string&gt;)`

Given function must return a reason for start button unavailability. Return null for approval.

```csharp
public void AddStartGameCondition(Func<string> func)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `func` | `System.Func&lt;TResult&gt;&lt;string&gt;` |  |

### `CheckStartGameCondition(out string, bool)`

```csharp
public bool CheckStartGameCondition(out string reason, bool showMessage)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `reason` | `string` |  |
| `showMessage` | `bool` |  |

**Returns:** `bool`

### `GoBack()`

```csharp
public void GoBack()
```

### `JoinMidGame()`

```csharp
public void JoinMidGame()
```

### `LogicUpdate(float)`

```csharp
public override void LogicUpdate(float dt)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `dt` | `float` |  |

### `RemoveStartGameCondition(Func&lt;string&gt;)`

```csharp
public void RemoveStartGameCondition(Func<string> func)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `func` | `System.Func&lt;TResult&gt;&lt;string&gt;` |  |

### `SetReady(bool)`

```csharp
public void SetReady(bool ready)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `ready` | `bool` |  |

### `StartGame()`

```csharp
public void StartGame()
```

### `ToggleReady()`

```csharp
public void ToggleReady()
```
