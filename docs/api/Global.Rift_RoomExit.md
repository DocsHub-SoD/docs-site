# Class: Rift_RoomExit

- **Category:** <span class="cat-dot" style="--cat-color: #22c55e" data-cat="Actors & Entities"></span> Actors & Entities
- **Namespace:** `Global`
- **Assembly:** `Dew.Core.dll`
- **Inheritance / Derived:** [DewNetworkBehaviour](/api/Global.DewNetworkBehaviour) → [Actor](/api/Global.Actor) → [Rift](/api/Global.Rift) → [Rift_MockExit](/api/Global.Rift_MockExit)

```csharp
public class Rift_RoomExit : Rift, ILogicUpdate, ICleanup, ICustomDestroyRoutine, IInteractable, IBanRoomNodesNearby, IBanRoomNodesNearbyMultiple
```

## Fields (3)

::: details Click to expand Fields (3)

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`forceTravelToNextZone`** | `[SyncVar] public bool forceTravelToNextZone` |  |
| **`nextNodeIndex`** | `[SyncVar] public int nextNodeIndex` |  |
| **`softInstance`** | `public static Rift_RoomExit softInstance` |  |

:::

## Properties (1)

::: details Click to expand Properties (1)

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`instance`** | `public static Rift_RoomExit instance { get; }` | If you expect the instance to be null, you MUST USE softInstance in Update loops.This will call FindObjectOfType if current instance is null, which can be very expensive. |

:::

## Methods (6)

::: details `Awake()`

```csharp
protected override void Awake()
```

:::

::: details `GetBanSpots()`

```csharp
public Vector3[] GetBanSpots()
```

**Returns:** `UnityEngine.Vector3[]`

:::

::: details `GetSidetrackPortalPositions(List&lt;(Vector3, Quaternion)&gt;)`

```csharp
public void GetSidetrackPortalPositions(List<(Vector3, Quaternion)> list)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `list` | `System.Collections.Generic.List<T><(UnityEngine.Vector3,UnityEngine.Quaternion)>` |  |

:::

::: details `OnCreate()`

```csharp
protected override void OnCreate()
```

:::

::: details `OnInteractRift(Hero)`

```csharp
protected override bool OnInteractRift(Hero hero)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `hero` | [`Hero`](/api/Global.Hero) |  |

**Returns:** `bool`

:::

::: details `TpcInteract(NetworkConnectionToClient)`

```csharp
public void TpcInteract(NetworkConnectionToClient target)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `target` | `Mirror.NetworkConnectionToClient` |  |

:::


## Architecture & Relationships

::: details Click to expand Architecture & Relationships

### Used By (13)

*Classes and systems that invoke, reference, or depend on `Rift_RoomExit`:*

[ControlManager](/api/Global.ControlManager) · `Forest_LoopCat_Spawner` · [Rift_MockExit](/api/Global.Rift_MockExit) · [Room](/api/Global.Room) · `RoomMod_Ambush` · `RoomMod_ChallengingFight` · `RoomMod_CorruptedChaos_AuraOfPain` · `RoomMod_DistantMemories` · `RoomMod_SpawnMiniBoss` · [RoomRifts](/api/Global.RoomRifts) · `Shrine_MarshOfDestiny_SeedOfTorment` · `UI_InGame_WorldMap` · [ZoneManager](/api/Global.ZoneManager)

### Dependencies (17)

*Types and components that `Rift_RoomExit` references or depends upon:*

[Actor](/api/Global.Actor) · [Dew](/api/Global.Dew) · [DewBuildProfile](/api/Global.DewBuildProfile) · [DewLocalization](/api/Global.DewLocalization) · [DewPlayer](/api/Global.DewPlayer) · [Entity](/api/Global.Entity) · [GameManager](/api/Global.GameManager) · [Hero](/api/Global.Hero) · [IBanRoomNodesNearbyMultiple](/api/Global.IBanRoomNodesNearbyMultiple) · [InGameUIManager](/api/Global.InGameUIManager) · [ManagerBase`1](/api/Global.ManagerBase`1) · [MessageManager](/api/Global.MessageManager) · [NetworkedManagerBase`1](/api/Global.NetworkedManagerBase`1) · [Rift](/api/Global.Rift) · [Room](/api/Global.Room) · [SingletonDewNetworkBehaviour`1](/api/Global.SingletonDewNetworkBehaviour`1) · [ZoneManager](/api/Global.ZoneManager)

:::
