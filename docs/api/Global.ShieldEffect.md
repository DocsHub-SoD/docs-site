# Class: ShieldEffect

- **Category:** <span class="cat-dot" style="--cat-color: #ef4444" data-cat="Combat & Abilities"></span> Combat & Abilities
- **Namespace:** `Global`
- **Assembly:** `Dew.Core.dll`
- **Inheritance / Derived:** [BasicEffect](/api/Global.BasicEffect)

```csharp
public class ShieldEffect : BasicEffect
```

## Fields (2)

::: details Click to expand Fields (2)

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`onAmountModified`** | `public Action<float, float> onAmountModified` | Called when the amount of this shield is modified by any means. In code, by damage, etc. |
| **`onDamageNegated`** | `public SafeAction<EventInfoDamageNegatedByShield> onDamageNegated` | Called when this shield negates a damage. Partially or completely. |

:::

## Properties (2)

::: details Click to expand Properties (2)

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`amount`** | `public float amount { get; set; }` |  |
| **`mask`** | `public override BasicEffectMask mask { get; }` |  |

:::

## Methods (1)

::: details `AddAmount(float, float, bool)`

This will process, add the amount to the effect, and invoke relevant effects.

```csharp
public void AddAmount(float originalAmount, float totalMax = Infinity, bool processTotalMax = true)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `originalAmount` | `float` |  |
| `totalMax` | `float` |  |
| `processTotalMax` | `bool` |  |

:::


## Architecture & Relationships

::: details Click to expand Architecture & Relationships

### Used By (15)

*Classes and systems that invoke, reference, or depend on `ShieldEffect`:*

[Actor](/api/Global.Actor) · `Ai_Mon_Special_BossObliviax_ChargeSequence_Ready` · [EntityStatus](/api/Global.EntityStatus) · [EventInfoDamageNegatedByShield](/api/Global.EventInfoDamageNegatedByShield) · `Gem_L_Supersymmetry` · `Gem_R_Snow` · `Se_E_Permafrost_Shield` · `Se_GenericShield_OneShot` · `Se_GenericShield_Stacking` · `Se_Mon_Primus_BossPrimusAeron_Rage_DecayingShield` · `Se_Mon_Special_BossMaw_ShieldConversion` · `Se_RoomMod_MisticIceVein_Shield` · `Se_Star_Mist_F_PR_ShieldAndCrit` · `Se_Star_Mist_L_PotionShield_PersistentShield` · [StatusEffect](/api/Global.StatusEffect)

### Dependencies (7)

*Types and components that `ShieldEffect` references or depends upon:*

[Actor](/api/Global.Actor) · [BasicEffect](/api/Global.BasicEffect) · [Entity](/api/Global.Entity) · [EntityStatus](/api/Global.EntityStatus) · [ReactionChain](/api/Global.ReactionChain) · [SafeAction`1](/api/Global.SafeAction`1) · [StatusEffect](/api/Global.StatusEffect)

### Related Enums (1)

*Enumerations referenced in fields, properties, or method signatures:*

<a href="/enums#basiceffectmask" class="enum-link" data-tooltip="Slow=1 · Speed=2 · Haste=4 · Cripple=8 · Root=16 (+19 more)">BasicEffectMask</a>

:::
