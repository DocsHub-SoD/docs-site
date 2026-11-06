# Class: RoomProps

- **Category:** <span class="cat-dot" style="--cat-color: #3b82f6" data-cat="Managers & Systems"></span> Managers & Systems
- **Namespace:** `Global`
- **Assembly:** `Dew.Core.dll`
- **Attributes:** `[RoomComponentStartDependency]`
- **Inheritance / Derived:** [DewNetworkBehaviour](/api/Global.DewNetworkBehaviour) → [RoomComponent](/api/Global.RoomComponent)

```csharp
[RoomComponentStartDependency(typeof(RoomModifiers))]
public class RoomProps : RoomComponent, ILogicUpdate
```

## Fields (2)

::: details Click to expand Fields (2)

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`defaultPerSectionRule`** | `public PropSpawnRule defaultPerSectionRule` |  |
| **`globalRule`** | `public PropSpawnRule globalRule` |  |

:::

## Methods (2)

::: details `OnRoomStartServer()`

```csharp
public override void OnRoomStartServer()
```

:::

::: details `TryGetGoodNodePosition(out Vector3, DewRandom)`

Returns false if suboptimal position is returned.

```csharp
public bool TryGetGoodNodePosition(out Vector3 position, DewRandom random = null)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `position` | `UnityEngine.Vector3` |  |
| `random` | [`DewRandom`](/api/Global.DewRandom) |  |

**Returns:** `bool`

:::


## Architecture & Relationships

::: details Click to expand Architecture & Relationships

### Used By (8)

*Classes and systems that invoke, reference, or depend on `RoomProps`:*

`DewConsoleCommands` · `LucidDream_MarshOfDestiny` · [Room](/api/Global.Room) · `RoomMod_HeroSoul` · `RoomMod_SpawnPileOfSnow` · `RoomMod_StardustEverywhere` · [RoomModifierBase](/api/Global.RoomModifierBase) · [SpecialEntityRoomModifier](/api/Global.SpecialEntityRoomModifier)

### Dependencies (15)

*Types and components that `RoomProps` references or depends upon:*

[Actor](/api/Global.Actor) · [AssetRef`1](/api/Global.AssetRef`1) · [Dew](/api/Global.Dew) · [DewPlayer](/api/Global.DewPlayer) · [DewRandom](/api/Global.DewRandom) · [GameManager](/api/Global.GameManager) · [IProp](/api/Global.IProp) · [ManagerBase`1](/api/Global.ManagerBase`1) · [NetworkedManagerBase`1](/api/Global.NetworkedManagerBase`1) · [PropSpawnRule](/api/Global.PropSpawnRule) · [Room](/api/Global.Room) · [RoomComponent](/api/Global.RoomComponent) · [RoomRewards](/api/Global.RoomRewards) · [RoomSection](/api/Global.RoomSection) · [ZoneManager](/api/Global.ZoneManager)

:::
