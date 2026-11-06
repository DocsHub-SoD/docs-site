# Class: RoomModifiers

- **Category:** <span class="cat-dot" style="--cat-color: #3b82f6" data-cat="Managers & Systems"></span> Managers & Systems
- **Namespace:** `Global`
- **Assembly:** `Dew.Core.dll`
- **Inheritance / Derived:** [DewNetworkBehaviour](/api/Global.DewNetworkBehaviour) → [RoomComponent](/api/Global.RoomComponent)

```csharp
public class RoomModifiers : RoomComponent, ILogicUpdate
```

## Fields (1)

::: details Click to expand Fields (1)

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`modifierInstances`** | `[NonSerialized] public List<RoomModifierBase> modifierInstances` | Available on server. |

:::

## Methods (1)

::: details `OnRoomStartServer()`

```csharp
public override void OnRoomStartServer()
```

:::


## Architecture & Relationships

::: details Click to expand Architecture & Relationships

### Used By (2)

*Classes and systems that invoke, reference, or depend on `RoomModifiers`:*

[Room](/api/Global.Room) · [ZoneManager](/api/Global.ZoneManager)

### Dependencies (8)

*Types and components that `RoomModifiers` references or depends upon:*

[Actor](/api/Global.Actor) · [ActorCheck](/api/Global.ActorCheck) · [Dew](/api/Global.Dew) · [DewPersistence](/api/Global.DewPersistence) · [DewResources](/api/Global.DewResources) · [NetworkedManagerBase`1](/api/Global.NetworkedManagerBase`1) · [RoomComponent](/api/Global.RoomComponent) · [ZoneManager](/api/Global.ZoneManager)

:::
