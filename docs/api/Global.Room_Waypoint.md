# Class: Room_Waypoint

- **Namespace:** `Global`
- **Assembly:** `Dew.Core.dll`
- **Inheritance / Derived:** [DewNetworkBehaviour](/api/Global.DewNetworkBehaviour)

```csharp
public class Room_Waypoint : DewNetworkBehaviour, ILogicUpdate, IPlayerPathablePoint
```

## Fields

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`dewCollider`** | `public DewCollider dewCollider` |  |
| **`lockedEffect`** | `public GameObject lockedEffect` |  |
| **`unlockedEffect`** | `public GameObject unlockedEffect` |  |

## Properties

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`isUnlocked`** | `public bool isUnlocked { get; }` |  |

## Methods

### `Lock()`

```csharp
public void Lock()
```

### `OnLateStartServer()`

```csharp
public override void OnLateStartServer()
```

### `OnStart()`

```csharp
public override void OnStart()
```

### `Unlock()`

```csharp
public void Unlock()
```
