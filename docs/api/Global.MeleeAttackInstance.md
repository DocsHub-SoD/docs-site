# Class: MeleeAttackInstance

- **Category:** <span class="cat-dot" style="--cat-color: #ef4444" data-cat="Combat & Abilities"></span> Combat & Abilities
- **Namespace:** `Global`
- **Assembly:** `Dew.Core.dll`
- **Inheritance / Derived:** [DewNetworkBehaviour](/api/Global.DewNetworkBehaviour) → [Actor](/api/Global.Actor) → [AbilityInstance](/api/Global.AbilityInstance)

```csharp
public class MeleeAttackInstance : AbilityInstance, ILogicUpdate, ICleanup, ICustomDestroyRoutine
```

## Fields (10)

::: details Click to expand Fields (10)

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`fxHitMain`** | `public GameObject fxHitMain` |  |
| **`fxHitSub`** | `public GameObject fxHitSub` |  |
| **`hitCount`** | `[NonSerialized] public int hitCount` | Available on server. |
| **`isCrit`** | `public bool isCrit` |  |
| **`mainTargetAttackEffect`** | `public float mainTargetAttackEffect` |  |
| **`mainTargetDamage`** | `public float mainTargetDamage` |  |
| **`range`** | `public DewCollider range` |  |
| **`scaleRangeWithTriggerRange`** | `public bool scaleRangeWithTriggerRange` |  |
| **`subTargetAttackEffect`** | `public float subTargetAttackEffect` |  |
| **`subTargetDamage`** | `public float subTargetDamage` |  |

:::

## Properties (1)

::: details Click to expand Properties (1)

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`didHit`** | `public bool didHit { get; }` | Available on server. |

:::

## Methods (1)

::: details `OnCreate()`

```csharp
protected override void OnCreate()
```

:::


## Architecture & Relationships

::: details Click to expand Architecture & Relationships

### Used By (12)

*Classes and systems that invoke, reference, or depend on `MeleeAttackInstance`:*

`Ai_Atk_AurenaSwipe` · `Ai_Atk_AurenaSwipe_Crit` · `Ai_Atk_HuskSword` · `Ai_Atk_HuskSword_Crit` · `Ai_Atk_MistSabre` · `Ai_Atk_MistSabre_Crit` · `Ai_Atk_VesperMace` · `Ai_Atk_VesperMace_Crit` · `Ai_D_BurningFist_Attack` · `Ai_D_Resolve_Push` · `Ai_D_ScarOfTheWind_DashAtk` · `Ai_R_FrozenFists_Attack`

### Dependencies (9)

*Types and components that `MeleeAttackInstance` references or depends upon:*

[AbilityInstance](/api/Global.AbilityInstance) · [AbilityTrigger](/api/Global.AbilityTrigger) · [Actor](/api/Global.Actor) · [CastInfo](/api/Global.CastInfo) · [DewCollider](/api/Global.DewCollider) · [DewNetworkBehaviour](/api/Global.DewNetworkBehaviour) · [Entity](/api/Global.Entity) · [ListReturnHandle`1](/api/Global.ListReturnHandle`1) · [TriggerConfig](/api/Global.TriggerConfig)

:::
