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
| **`skipBossSoulFlow`** | `[SyncVar] [NonSerialized] public bool skipBossSoulFlow` |  |

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


## Architecture & Relationships

::: details Click to expand Architecture & Relationships

### Used By (15)

*Classes and systems that invoke, reference, or depend on `BossMonster`:*

`Mon_DarkCave_BossSeeker` · `Mon_Despair_BossAzurak` · `Mon_Despair_BossCrawler` · `Mon_Forest_BossDemon` · `Mon_Ink_BossDarkMoon` · `Mon_Ink_BossWhiteNight` · `Mon_LavaLand_BossInfernus` · `Mon_Primus_BossPrimusAeron` · `Mon_Sky_BossNyx` · `Mon_SnowMountain_BossSkoll` · `Mon_Special_BossErebos` · `Mon_Special_BossLightElemental` · `Mon_Special_BossMaw` · `Mon_Special_BossObliviax` · `Mon_Special_BossPolaris`

### Dependencies (9)

*Types and components that `BossMonster` references or depends upon:*

[Actor](/api/Global.Actor) · [Entity](/api/Global.Entity) · [EntityCheck](/api/Global.EntityCheck) · [EntityStatus](/api/Global.EntityStatus) · [EventInfoKill](/api/Global.EventInfoKill) · [GameManager](/api/Global.GameManager) · [GameSettingsManager](/api/Global.GameSettingsManager) · [Monster](/api/Global.Monster) · [NetworkedManagerBase`1](/api/Global.NetworkedManagerBase`1)

:::
