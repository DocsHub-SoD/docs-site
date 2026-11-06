# Class: BossMonster

- **Category:** <span class="cat-dot" style="--cat-color: #22c55e" data-cat="Actors & Entities"></span> Actors & Entities
- **Namespace:** `Global`
- **Assembly:** `Dew.Core.dll`
- **Inheritance / Derived:** [DewNetworkBehaviour](/api/Global.DewNetworkBehaviour) → [Actor](/api/Global.Actor) → [Entity](/api/Global.Entity) → [Monster](/api/Global.Monster)

```csharp
public class BossMonster : Monster, ILogicUpdate, ICleanup, ICustomDestroyRoutine
```

## Fields (3)

::: details Click to expand Fields (3)

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`isHiddenBoss`** | `public bool isHiddenBoss` |  |
| **`playBossKillFeedback`** | `public bool playBossKillFeedback` |  |
| **`skipBossSoulFlow`** | `[NonSerialized] public bool skipBossSoulFlow` |  |

:::

## Methods (5)

::: details `GetUniqueReward()`

```csharp
public virtual Type GetUniqueReward()
```

**Returns:** `System.Type`

:::

::: details `GetUniqueRewardChance()`

```csharp
public virtual float GetUniqueRewardChance()
```

**Returns:** `float`

:::

::: details `OnCreate()`

```csharp
protected override void OnCreate()
```

:::

::: details `OnDeath(EventInfoKill)`

```csharp
protected override void OnDeath(EventInfoKill info)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `info` | [`EventInfoKill`](/api/Global.EventInfoKill) |  |

:::

::: details `OnDestroyActor()`

```csharp
protected override void OnDestroyActor()
```

:::
