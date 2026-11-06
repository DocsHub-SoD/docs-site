# Class: RoomRewards

- **Category:** <span class="cat-dot" style="--cat-color: #eab308" data-cat="Items & Economy"></span> Items & Economy
- **Namespace:** `Global`
- **Assembly:** `Dew.Core.dll`
- **Attributes:** `[RoomComponentStartDependency] [RoomComponentStartDependency]`
- **Inheritance / Derived:** [DewNetworkBehaviour](/api/Global.DewNetworkBehaviour) → [RoomComponent](/api/Global.RoomComponent)

```csharp
[RoomComponentStartDependency(typeof(RoomModifiers))]
[RoomComponentStartDependency(typeof(RoomMonsters))]
public class RoomRewards : RoomComponent, ILogicUpdate
```

## Fields (4)

::: details Click to expand Fields (4)

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`disableRewards`** | `public bool disableRewards` |  |
| **`gemBonusQuality`** | `[NonSerialized] public int gemBonusQuality` | Available on server. |
| **`giveHighRarityReward`** | `[NonSerialized] public bool giveHighRarityReward` | Available on server. |
| **`skillBonusLevel`** | `[NonSerialized] public int skillBonusLevel` | Available on server. |

:::

## Properties (1)

::: details Click to expand Properties (1)

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`isRegularRewardDisabled`** | `public bool isRegularRewardDisabled { get; }` |  |

:::

## Methods (4)

::: details `DisableRegularRewards()`

Disable all shrines and props that would normally spawn as a reward, except the ones from room modifiers.(O) Default skill and essence shrines(O) Natural spawning golds and dream dusts(X) RoomMod_GoldEverywhere golds(X) Shrines from RoomModifierBase.PlaceShrine()

```csharp
public void DisableRegularRewards()
```

:::

::: details `DropChaosReward(Vector3, bool)`

```csharp
public void DropChaosReward(Vector3 pos, bool isHighQuality)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `pos` | `UnityEngine.Vector3` |  |
| `isHighQuality` | `bool` |  |

:::

::: details `OnRoomStartServer()`

```csharp
public override void OnRoomStartServer()
```

:::

::: details `SpawnCombatCoreShrines()`

```csharp
public void SpawnCombatCoreShrines()
```

:::


## Architecture & Relationships

::: details Click to expand Architecture & Relationships

### Used By (9)

*Classes and systems that invoke, reference, or depend on `RoomRewards`:*

[Room](/api/Global.Room) · `RoomMod_Ambush` · `RoomMod_DistantMemories` · `RoomMod_GoldEverywhere` · `RoomMod_PureDream` · `RoomMod_SpawnHatred` · `RoomMod_SpawnMawOfDoom` · `RoomMod_SpawnParadox` · [RoomProps](/api/Global.RoomProps)

### Dependencies (17)

*Types and components that `RoomRewards` references or depends upon:*

[Actor](/api/Global.Actor) · [Dew](/api/Global.Dew) · [DewBuildProfile](/api/Global.DewBuildProfile) · [DewPlayer](/api/Global.DewPlayer) · [DewRandom](/api/Global.DewRandom) · [EntityCheck](/api/Global.EntityCheck) · [Formula](/api/Global.Formula) · `GetStableHashCodeExtensions` · [IProp](/api/Global.IProp) · [NetworkedManagerBase`1](/api/Global.NetworkedManagerBase`1) · [Room](/api/Global.Room) · [RoomComponent](/api/Global.RoomComponent) · [RoomSection](/api/Global.RoomSection) · [Shrine](/api/Global.Shrine) · `ShuffleListExtension` · [SingletonDewNetworkBehaviour`1](/api/Global.SingletonDewNetworkBehaviour`1) · [ZoneManager](/api/Global.ZoneManager)

### Related Enums (1)

*Enumerations referenced in fields, properties, or method signatures:*

[`Rarity`](/enums#rarity)

:::
