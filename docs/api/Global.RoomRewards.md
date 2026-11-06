# Class: RoomRewards

- **Category:** <span class="cat-dot" style="--cat-color: #eab308" data-cat="Items & Economy"></span> Items & Economy
- **Namespace:** `Global`
- **Assembly:** `Dew.Core.dll`
- **Inheritance / Derived:** [DewNetworkBehaviour](/api/Global.DewNetworkBehaviour) → [RoomComponent](/api/Global.RoomComponent)

```csharp
[RoomComponentStartDependency(typeof(RoomModifiers))]
[RoomComponentStartDependency(typeof(RoomMonsters))]
public class RoomRewards : RoomComponent, ILogicUpdate
```

## Fields

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`disableRewards`** | `public bool disableRewards` |  |
| **`gemBonusQuality`** | `[NonSerialized] public int gemBonusQuality` | Available on server. |
| **`giveHighRarityReward`** | `[NonSerialized] public bool giveHighRarityReward` | Available on server. |
| **`skillBonusLevel`** | `[NonSerialized] public int skillBonusLevel` | Available on server. |

## Properties

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`isRegularRewardDisabled`** | `public bool isRegularRewardDisabled { get; }` |  |

## Methods

### `DisableRegularRewards()`

Disable all shrines and props that would normally spawn as a reward, except the ones from room modifiers.(O) Default skill and essence shrines(O) Natural spawning golds and dream dusts(X) RoomMod_GoldEverywhere golds(X) Shrines from RoomModifierBase.PlaceShrine()

```csharp
public void DisableRegularRewards()
```

### `DropChaosReward(Vector3, bool)`

```csharp
public void DropChaosReward(Vector3 pos, bool isHighQuality)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `pos` | `UnityEngine.Vector3` |  |
| `isHighQuality` | `bool` |  |

### `OnRoomStartServer()`

```csharp
public override void OnRoomStartServer()
```

### `SpawnCombatCoreShrines()`

```csharp
public void SpawnCombatCoreShrines()
```
