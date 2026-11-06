# Class: DevGameManager

- **Category:** <span class="cat-dot" style="--cat-color: #3b82f6" data-cat="Managers & Systems"></span> Managers & Systems
- **Namespace:** `Global`
- **Assembly:** `Dew.Core.dll`
- **Inheritance / Derived:** [DewNetworkBehaviour](/api/Global.DewNetworkBehaviour) → `NetworkedManagerBase` → [GameManager](/api/Global.GameManager) → [GameManager](/api/Global.GameManager)

```csharp
public class DevGameManager : GameManager, ILogicUpdate
```

## Fields

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`startZonePrefab`** | `public Zone startZonePrefab` |  |

## Methods

### `HostGame()`

```csharp
public void HostGame()
```

### `OnLateStart()`

```csharp
public override void OnLateStart()
```

### `OnLateStartServer()`

```csharp
public override void OnLateStartServer()
```

### `OnStartClient()`

```csharp
public override void OnStartClient()
```

### `OnStopClient()`

```csharp
public override void OnStopClient()
```

### `SpawnHero(Type, int, HeroLoadoutData, NetworkConnectionToClient)`

```csharp
public void SpawnHero(Type heroType, int level, HeroLoadoutData loadout, NetworkConnectionToClient sender = null)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `heroType` | `System.Type` |  |
| `level` | `int` |  |
| `loadout` | [`HeroLoadoutData`](/api/Global.HeroLoadoutData) |  |
| `sender` | `Mirror.NetworkConnectionToClient` |  |

### `StartLocalGame()`

```csharp
public void StartLocalGame()
```
