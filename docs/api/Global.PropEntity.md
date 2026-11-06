# Class: PropEntity

- **Category:** <span class="cat-dot" style="--cat-color: #ef4444" data-cat="Combat & Abilities"></span> Combat & Abilities
- **Namespace:** `Global`
- **Assembly:** `Dew.Core.dll`
- **Inheritance / Derived:** [DewNetworkBehaviour](/api/Global.DewNetworkBehaviour) → [Actor](/api/Global.Actor) → [Entity](/api/Global.Entity) → [PropEnt_Merchant_Backpack](/api/Global.PropEnt_Merchant_Backpack) → [PropEnt_Merchant_Base](/api/Global.PropEnt_Merchant_Base) → [PropEnt_Stone_DreamDust](/api/Global.PropEnt_Stone_DreamDust) → [PropEnt_Stone_Gold](/api/Global.PropEnt_Stone_Gold) → [PropEnt_Stone_Nightmare](/api/Global.PropEnt_Stone_Nightmare)

```csharp
public class PropEntity : Entity, ILogicUpdate, ICleanup, ICustomDestroyRoutine, IProp
```

## Fields (3)

::: details Click to expand Fields (3)

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`hitInvulnerableTime`** | `[ShowIf("takeOneDamageOnHit", true)] public float hitInvulnerableTime` |  |
| **`isUnstoppable`** | `public bool isUnstoppable` |  |
| **`takeOneDamageOnHit`** | `public bool takeOneDamageOnHit` |  |

:::

## Properties (2)

::: details Click to expand Properties (2)

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`isRegularReward`** | `public virtual bool isRegularReward { get; }` |  |
| **`scaleSpawnRateWithPlayers`** | `public bool scaleSpawnRateWithPlayers { get; }` |  |

:::

## Methods (2)

::: details `GetStaggerSettings()`

```csharp
protected override Entity.StaggerSettings GetStaggerSettings()
```

**Returns:** `Entity.StaggerSettings`

:::

::: details `OnCreate()`

```csharp
protected override void OnCreate()
```

:::


## Architecture & Relationships

::: details Click to expand Architecture & Relationships

### Used By (11)

*Classes and systems that invoke, reference, or depend on `PropEntity`:*

`PropEnt_GlacialBarrier` · [PropEnt_Merchant_Backpack](/api/Global.PropEnt_Merchant_Backpack) · [PropEnt_Merchant_Base](/api/Global.PropEnt_Merchant_Base) · `PropEnt_MisticIceVein` · `PropEnt_Sky_Orca` · [PropEnt_Stone_DreamDust](/api/Global.PropEnt_Stone_DreamDust) · [PropEnt_Stone_Gold](/api/Global.PropEnt_Stone_Gold) · [PropEnt_Stone_Nightmare](/api/Global.PropEnt_Stone_Nightmare) · `PropEnt_Stone_PitchBlackOre` · `PropEnt_Tutorial_Obstacle` · `PropEnt_VigilanteHaven_Obstacle`

### Dependencies (5)

*Types and components that `PropEntity` references or depends upon:*

[Actor](/api/Global.Actor) · [Entity](/api/Global.Entity) · [EventInfoDamage](/api/Global.EventInfoDamage) · [IProp](/api/Global.IProp) · [SafeAction`1](/api/Global.SafeAction`1)

:::
