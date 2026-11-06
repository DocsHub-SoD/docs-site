# Class: AttackProjectile

- **Category:** <span class="cat-dot" style="--cat-color: #ef4444" data-cat="Combat & Abilities"></span> Combat & Abilities
- **Namespace:** `Global`
- **Assembly:** `Dew.Core.dll`
- **Inheritance / Derived:** [DewNetworkBehaviour](/api/Global.DewNetworkBehaviour) → [Actor](/api/Global.Actor) → [AbilityInstance](/api/Global.AbilityInstance) → [Projectile](/api/Global.Projectile) → [StandardProjectile](/api/Global.StandardProjectile)

```csharp
public class AttackProjectile : StandardProjectile, ILogicUpdate, ICleanup, ICustomDestroyRoutine
```

## Fields (3)

::: details Click to expand Fields (3)

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`isCrit`** | `public bool isCrit` |  |
| **`isMain`** | `[NonSerialized] public bool isMain` |  |
| **`strength`** | `public float strength` |  |

:::

## Methods (3)

::: details `OnCreate()`

```csharp
protected override void OnCreate()
```

:::

::: details `OnEntity(EntityHit)`

```csharp
protected override void OnEntity(Projectile.EntityHit hit)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `hit` | [`Projectile.EntityHit`](/api/Global.Projectile) |  |

:::

::: details `OnPrepare()`

```csharp
protected override void OnPrepare()
```

:::


## Architecture & Relationships

::: details Click to expand Architecture & Relationships

### Used By (13)

*Classes and systems that invoke, reference, or depend on `AttackProjectile`:*

`Ai_Atk_AurenaFeather` · `Ai_Atk_AurenaFeather_Crit` · `Ai_Atk_BismuthRock` · `Ai_Atk_BismuthRock_Crit` · `Ai_Atk_CetusStaff` · `Ai_Atk_CetusStaff_Crit` · `Ai_Atk_LacertaRifle` · `Ai_Atk_LacertaRifle_Crit` · `Ai_Atk_NachiaStaff` · `Ai_Atk_NachiaStaff_Crit` · `Ai_Atk_YubarStardust` · `Ai_D_PrismaticEyes_Attack` · `Ai_Mon_Despair_ParalyticFly_Atk`

### Dependencies (6)

*Types and components that `AttackProjectile` references or depends upon:*

[AbilityInstance](/api/Global.AbilityInstance) · [AbilityTrigger](/api/Global.AbilityTrigger) · [Actor](/api/Global.Actor) · [Projectile](/api/Global.Projectile) · [StandardProjectile](/api/Global.StandardProjectile) · [TriggerConfig](/api/Global.TriggerConfig)

:::
