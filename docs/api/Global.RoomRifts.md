# Class: RoomRifts

- **Category:** <span class="cat-dot" style="--cat-color: #3b82f6" data-cat="Managers & Systems"></span> Managers & Systems
- **Namespace:** `Global`
- **Assembly:** `Dew.Core.dll`
- **Inheritance / Derived:** [DewNetworkBehaviour](/api/Global.DewNetworkBehaviour) → [RoomComponent](/api/Global.RoomComponent)

```csharp
public class RoomRifts : RoomComponent, ILogicUpdate
```

## Fields (1)

::: details Click to expand Fields (1)

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`openedSidetrackRifts`** | `public List<string> openedSidetrackRifts` |  |

:::

## Methods (3)

::: details `CreateSidetrackRift(Rift_Sidetrack)`

Create a sidetrack rift on adequate position. This can fail if there's no position to spawn the new rift.

```csharp
public void CreateSidetrackRift(Rift_Sidetrack prefab)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `prefab` | [`Rift_Sidetrack`](/api/Global.Rift_Sidetrack) |  |

:::

::: details `OnRoomStartServer()`

```csharp
public override void OnRoomStartServer()
```

:::

::: details `OpenRifts()`

Open room exit rift.Can also spawn sidetrack rifts if combat node.

```csharp
public void OpenRifts()
```

:::


## Architecture & Relationships

::: details Click to expand Architecture & Relationships

### Used By (1)

*Classes and systems that invoke, reference, or depend on `RoomRifts`:*

[Room](/api/Global.Room)

### Dependencies (13)

*Types and components that `RoomRifts` references or depends upon:*

[ActorCheck](/api/Global.ActorCheck) · [Dew](/api/Global.Dew) · [DewBuildProfile](/api/Global.DewBuildProfile) · [DewRandom](/api/Global.DewRandom) · [DewResources](/api/Global.DewResources) · [NetworkedManagerBase`1](/api/Global.NetworkedManagerBase`1) · [Rift](/api/Global.Rift) · [Rift_RoomExit](/api/Global.Rift_RoomExit) · [Rift_Sidetrack](/api/Global.Rift_Sidetrack) · [Room](/api/Global.Room) · [RoomComponent](/api/Global.RoomComponent) · [SingletonDewNetworkBehaviour`1](/api/Global.SingletonDewNetworkBehaviour`1) · [ZoneManager](/api/Global.ZoneManager)

:::
