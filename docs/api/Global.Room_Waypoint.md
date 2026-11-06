# Class: Room_Waypoint

- **Category:** <span class="cat-dot" style="--cat-color: #3b82f6" data-cat="Managers & Systems"></span> Managers & Systems
- **Namespace:** `Global`
- **Assembly:** `Dew.Core.dll`
- **Inheritance / Derived:** [DewNetworkBehaviour](/api/Global.DewNetworkBehaviour)

```csharp
public class Room_Waypoint : DewNetworkBehaviour, ILogicUpdate, IPlayerPathablePoint
```

## Fields (3)

::: details Click to expand Fields (3)

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`dewCollider`** | `public DewCollider dewCollider` |  |
| **`lockedEffect`** | `public GameObject lockedEffect` |  |
| **`unlockedEffect`** | `public GameObject unlockedEffect` |  |

:::

## Properties (1)

::: details Click to expand Properties (1)

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`isUnlocked`** | `public bool isUnlocked { get; }` |  |

:::

## Methods (4)

::: details `Lock()`

```csharp
public void Lock()
```

:::

::: details `OnLateStartServer()`

```csharp
public override void OnLateStartServer()
```

:::

::: details `OnStart()`

```csharp
public override void OnStart()
```

:::

::: details `Unlock()`

```csharp
public void Unlock()
```

:::


## Architecture & Relationships

::: details Click to expand Architecture & Relationships

### Used By (2)

*Classes and systems that invoke, reference, or depend on `Room_Waypoint`:*

[Hero](/api/Global.Hero) · [Room](/api/Global.Room)

### Dependencies (6)

*Types and components that `Room_Waypoint` references or depends upon:*

[DewCollider](/api/Global.DewCollider) · [DewNetworkBehaviour](/api/Global.DewNetworkBehaviour) · [IPlayerPathablePoint](/api/Global.IPlayerPathablePoint) · [Room](/api/Global.Room) · [RoomSection](/api/Global.RoomSection) · [SingletonDewNetworkBehaviour`1](/api/Global.SingletonDewNetworkBehaviour`1)

:::
