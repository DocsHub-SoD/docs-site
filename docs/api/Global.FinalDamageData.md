# Struct: FinalDamageData

- **Category:** <span class="cat-dot" style="--cat-color: #ef4444" data-cat="Combat & Abilities"></span> Combat & Abilities
- **Namespace:** `Global`
- **Assembly:** `Dew.Core.dll`

```csharp
public struct FinalDamageData
```

## Fields (10)

::: details Click to expand Fields (10)

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`amount`** | `public float amount` |  |
| **`attackEffectStrength`** | `public float attackEffectStrength` |  |
| **`attackEffectType`** | `public AttackEffectType attackEffectType` |  |
| **`attributes`** | `public DamageAttribute attributes` |  |
| **`direction`** | `public Vector3? direction` |  |
| **`discardedAmount`** | `public float discardedAmount` |  |
| **`elemental`** | `public ElementalType? elemental` |  |
| **`overrideElementalStacks`** | `public int? overrideElementalStacks` |  |
| **`procCoefficient`** | `public float procCoefficient` |  |
| **`type`** | `public DamageData.SourceType type` |  |

:::

## Properties (1)

::: details Click to expand Properties (1)

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`canMerge`** | `public bool canMerge { get; }` |  |

:::

## Methods (1)

::: details `HasAttr(DamageAttribute)`

Does this damage has specific attribute?

```csharp
public bool HasAttr(DamageAttribute attr)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `attr` | <a href="/enums#damageattribute" class="enum-link" data-tooltip="None=0 · IsCrit=1 · IgnoreArmor=2 · IgnoreShield=4 · IgnoreDamageImmunity=8 (+5 more)">DamageAttribute</a> |  |

**Returns:** `bool`

:::


## Architecture & Relationships

::: details Click to expand Architecture & Relationships

### Used By (21)

*Classes and systems that invoke, reference, or depend on `FinalDamageData`:*

[Actor](/api/Global.Actor) · `Ai_D_SharedPain_Instance` · `Ai_Gem_L_PureWhite_Projectile` · `Ai_Gem_R_Accuracy_Projectile` · `Ai_Gem_R_Ricochet` · `Ai_Star_Mist_F_LG_ChainAttack_Phantom` · [CameraManager](/api/Global.CameraManager) · [DamageData](/api/Global.DamageData) · `DewDamageNumberRenderer` · [EventInfoDamage](/api/Global.EventInfoDamage) · [EventInfoDamageNegatedByImmunity](/api/Global.EventInfoDamageNegatedByImmunity) · [EventInfoDamageNegatedByShield](/api/Global.EventInfoDamageNegatedByShield) · [HealData](/api/Global.HealData) · `Se_HeroOneShotProtection` · `Se_MirageSkin_Sanctification_Protected` · `Se_Star_Husk_D_DamageOverTimeCritWithPenalty_DoT` · `Se_Star_Mist_F_LG_ChainAttack` · `UI_DamageNumberGroup` · `UI_DamageNumberText` · `UI_EntityFollow` · `Mirror.GeneratedNetworkCode`

### Dependencies (5)

*Types and components that `FinalDamageData` references or depends upon:*

[Actor](/api/Global.Actor) · `ActorFlags` · [DamageData](/api/Global.DamageData) · [Entity](/api/Global.Entity) · [EntityStatus](/api/Global.EntityStatus)

### Related Enums (3)

*Enumerations referenced in fields, properties, or method signatures:*

<a href="/enums#attackeffecttype" class="enum-link" data-tooltip="BasicAttackMain=0 · BasicAttackSub=1 · Others=2">AttackEffectType</a> · <a href="/enums#damageattribute" class="enum-link" data-tooltip="None=0 · IsCrit=1 · IgnoreArmor=2 · IgnoreShield=4 · IgnoreDamageImmunity=8 (+5 more)">DamageAttribute</a> · <a href="/enums#elementaltype" class="enum-link" data-tooltip="Fire=0 · Cold=1 · Light=2 · Dark=3">ElementalType</a>

:::
