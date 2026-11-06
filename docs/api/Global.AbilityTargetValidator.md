# Class: AbilityTargetValidator

- **Category:** <span class="cat-dot" style="--cat-color: #ef4444" data-cat="Combat & Abilities"></span> Combat & Abilities
- **Namespace:** `Global`
- **Assembly:** `Dew.Core.dll`

```csharp
[Serializable]
[InlineProperty]
public class AbilityTargetValidator : IBinaryEntityValidator
```

## Fields (1)

::: details Click to expand Fields (1)

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`targets`** | `[HideLabel] [EnumToggleButtons] public EntityRelation targets` |  |

:::

## Methods (1)

::: details `Evaluate(Entity, Entity)`

```csharp
public bool Evaluate(Entity self, Entity target)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `self` | [`Entity`](/api/Global.Entity) |  |
| `target` | [`Entity`](/api/Global.Entity) |  |

**Returns:** `bool`

:::


## Architecture & Relationships

::: details Click to expand Architecture & Relationships

### Used By (40)

*Classes and systems that invoke, reference, or depend on `AbilityTargetValidator`:*

[AbilityTargetValidatorWrapper](/api/Global.AbilityTargetValidatorWrapper) · [ActionCast](/api/Global.ActionCast) · `Ai_C_BeamOfLight` · `Ai_Gem_E_Thunder` · `Ai_GlacialBarrier_Spawn` · `Ai_L_SoulKiller_Soul` · `Ai_Mon_Forest_Hound_Charge` · `Ai_Mon_Ink_DivineAnimal_Bite` · `Ai_Mon_Ink_DivineAnimal_Missile_Sub` · `Ai_Mon_Ink_DivineAnimal_Stomp` · `Ai_Mon_Ink_EgoSword_Atk` · `Ai_Mon_Ink_GhostBlade_DemolitionMan` · `Ai_Mon_Ink_GhostBlade_MeleeAtk` · `Ai_Mon_Ink_Tiger_DashAtk` · `Ai_Mon_Sky_Baam_Teleport` · `Ai_Mon_Sky_StellaMatter_ThrowSub` · `Ai_Nor_CosmicBlast` · `Ai_Q_Fleche_Dash` · `Ai_R_Fireball` · `At_Atk_YubarStardust` · [ChargingChannelData](/api/Global.ChargingChannelData) · [ControlManager](/api/Global.ControlManager) · [DamageInstance](/api/Global.DamageInstance) · [EntityAI](/api/Global.EntityAI) · `Gem_E_Pain` · `Gem_L_Embertail` · `Gem_L_Paranoia` · `Gem_R_Snow` · `Gem_R_Spiral` · `Hero_Bismuth` · [Projectile](/api/Global.Projectile) · [SampleCastInfoContext](/api/Global.SampleCastInfoContext) · `Se_GenericStealth` · `Se_Nor_MyOwnLittleNebula` · `Se_Nor_WindowToTheSoul_SpiritualDominance` · `SpawnGemStarProp` · `St_C_Starfall` · `St_D_SalamanderPowder` · [TriggerConfig](/api/Global.TriggerConfig) · `Mirror.GeneratedNetworkCode`

### Dependencies (3)

*Types and components that `AbilityTargetValidator` references or depends upon:*

[Actor](/api/Global.Actor) · [Entity](/api/Global.Entity) · [IBinaryEntityValidator](/api/Global.IBinaryEntityValidator)

### Related Enums (1)

*Enumerations referenced in fields, properties, or method signatures:*

<a href="/enums#entityrelation" class="enum-link" data-tooltip="Self=1 · Neutral=2 · Enemy=4 · Ally=8">EntityRelation</a>

:::
