# Class: Room_Trap_Toggleable

- **Category:** <span class="cat-dot" style="--cat-color: #22c55e" data-cat="Actors & Entities"></span> Actors & Entities
- **Namespace:** `Global`
- **Assembly:** `Dew.Core.dll`
- **Attributes:** `[DewResourceLink]`
- **Inheritance / Derived:** [DewNetworkBehaviour](/api/Global.DewNetworkBehaviour) → [Actor](/api/Global.Actor)

```csharp
[DewResourceLink(ResourceLinkBy.None)]
public abstract class Room_Trap_Toggleable : Actor, ILogicUpdate, ICleanup, ICustomDestroyRoutine, IToggleableTrap, IBanRoomNodesNearby, IBanCampsNearby
```

## Fields (2)

::: details Click to expand Fields (2)

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`fxOff`** | `public GameObject fxOff` |  |
| **`fxOn`** | `public GameObject fxOn` |  |

:::

## Properties (2)

::: details Click to expand Properties (2)

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`isOn`** | `public bool isOn { get; }` |  |
| **`startTime`** | `public float startTime { get; }` | Available on server. Based onTime.time. By default it is negative infinity. |

:::

## Methods (4)

::: details `OnStartTrapServer()`

Called on server when this trap is started.

```csharp
protected virtual void OnStartTrapServer()
```

:::

::: details `OnStopTrapServer()`

Called on server when this trap is stopped.

```csharp
protected virtual void OnStopTrapServer()
```

:::

::: details `StartTrap()`

```csharp
public void StartTrap()
```

:::

::: details `StopTrap()`

```csharp
public void StopTrap()
```

:::


## Architecture & Relationships

::: details Click to expand Architecture & Relationships

### Used By (1)

*Classes and systems that invoke, reference, or depend on `Room_Trap_Toggleable`:*

`Trap_FlameJet`

### Dependencies (5)

*Types and components that `Room_Trap_Toggleable` references or depends upon:*

[Actor](/api/Global.Actor) · [DewNetworkBehaviour](/api/Global.DewNetworkBehaviour) · [IBanCampsNearby](/api/Global.IBanCampsNearby) · [IBanRoomNodesNearby](/api/Global.IBanRoomNodesNearby) · [IToggleableTrap](/api/Global.IToggleableTrap)

:::
