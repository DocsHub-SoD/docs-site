# Class: BossMonster

- **Namespace:** `Global`
- **Assembly:** `Dew.Core.dll`
- **Inheritance / Derived:** [DewNetworkBehaviour](/api/Global.DewNetworkBehaviour) → [Actor](/api/Global.Actor) → [Entity](/api/Global.Entity) → [Monster](/api/Global.Monster)

```csharp
public class BossMonster : Monster, ILogicUpdate, ICleanup, ICustomDestroyRoutine
```

## Fields

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`isHiddenBoss`** | `public bool isHiddenBoss` |  |
| **`playBossKillFeedback`** | `public bool playBossKillFeedback` |  |
| **`skipBossSoulFlow`** | `[NonSerialized]
public bool skipBossSoulFlow` |  |

## Methods

### `GetUniqueReward()`

```csharp
public virtual Type GetUniqueReward()
```

**Returns:** `System.Type`

### `GetUniqueRewardChance()`

```csharp
public virtual float GetUniqueRewardChance()
```

**Returns:** `float`

### `OnCreate()`

```csharp
protected override void OnCreate()
```

### `OnDeath(EventInfoKill)`

```csharp
protected override void OnDeath(EventInfoKill info)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `info` | [EventInfoKill](/api/Global.EventInfoKill) |  |

### `OnDestroyActor()`

```csharp
protected override void OnDestroyActor()
```
