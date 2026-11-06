# Class: SpecialEntityRoomModifier

- **Category:** <span class="cat-dot" style="--cat-color: #22c55e" data-cat="Actors & Entities"></span> Actors & Entities
- **Namespace:** `Global`
- **Assembly:** `Dew.Core.dll`
- **Inheritance / Derived:** [DewNetworkBehaviour](/api/Global.DewNetworkBehaviour) → [Actor](/api/Global.Actor) → [RoomModifierBase](/api/Global.RoomModifierBase)

```csharp
public abstract class SpecialEntityRoomModifier : RoomModifierBase, ILogicUpdate, ICleanup, ICustomDestroyRoutine, IExcludeFromPool
```

## Fields (4)

::: details Click to expand Fields (4)

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`dontSpawnIfHunted`** | `public bool dontSpawnIfHunted` |  |
| **`spawnedDreamDust`** | `public Vector2Int spawnedDreamDust` |  |
| **`spawnedGold`** | `public Vector2Int spawnedGold` |  |
| **`spawnedStardust`** | `public Vector2Int spawnedStardust` |  |

:::

## Methods (4)

::: details `GetEntityType()`

```csharp
protected abstract Type GetEntityType()
```

**Returns:** `System.Type`

:::

::: details `OnCreate()`

```csharp
protected override void OnCreate()
```

:::

::: details `OnDestroyActor()`

```csharp
protected override void OnDestroyActor()
```

:::

::: details `SpawnNpc(Vector3)`

```csharp
protected virtual Entity SpawnNpc(Vector3 pos)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `pos` | `UnityEngine.Vector3` |  |

**Returns:** `Entity`

:::


## Architecture & Relationships

::: details Click to expand Architecture & Relationships

### Used By (2)

*Classes and systems that invoke, reference, or depend on `SpecialEntityRoomModifier`:*

`RoomMod_DreamTeller` · `RoomMod_GiftMerchant`

### Dependencies (14)

*Types and components that `SpecialEntityRoomModifier` references or depends upon:*

[Actor](/api/Global.Actor) · `ActorRef`1` · [Dew](/api/Global.Dew) · [DewPlayer](/api/Global.DewPlayer) · [DewResources](/api/Global.DewResources) · [Entity](/api/Global.Entity) · [EntityCheck](/api/Global.EntityCheck) · [NetworkedManagerBase`1](/api/Global.NetworkedManagerBase`1) · [Room](/api/Global.Room) · [RoomModifierBase](/api/Global.RoomModifierBase) · [RoomProps](/api/Global.RoomProps) · [RoomSection](/api/Global.RoomSection) · [SingletonDewNetworkBehaviour`1](/api/Global.SingletonDewNetworkBehaviour`1) · [ZoneManager](/api/Global.ZoneManager)

:::
