# Class: Room_Trap_Toggleable

- **Namespace:** `Global`
- **Assembly:** `Dew.Core.dll`
- **Inheritance / Derived:** [DewNetworkBehaviour](/api/Global.DewNetworkBehaviour) → [Actor](/api/Global.Actor)

```csharp
[DewResourceLink(ResourceLinkBy.None)]
public abstract class Room_Trap_Toggleable : Actor, ILogicUpdate, ICleanup, ICustomDestroyRoutine, IToggleableTrap, IBanRoomNodesNearby, IBanCampsNearby
```

## Fields

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`fxOff`** | `public GameObject fxOff` |  |
| **`fxOn`** | `public GameObject fxOn` |  |

## Properties

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`isOn`** | `public bool isOn { get; }` |  |
| **`startTime`** | `public float startTime { get; }` | Available on server. Based onTime.time. By default it is negative infinity. |

## Methods

### `OnStartTrapServer()`

Called on server when this trap is started.

```csharp
protected virtual void OnStartTrapServer()
```

### `OnStopTrapServer()`

Called on server when this trap is stopped.

```csharp
protected virtual void OnStopTrapServer()
```

### `StartTrap()`

```csharp
public void StartTrap()
```

### `StopTrap()`

```csharp
public void StopTrap()
```
