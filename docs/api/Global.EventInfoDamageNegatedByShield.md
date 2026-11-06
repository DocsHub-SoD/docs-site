# Struct: EventInfoDamageNegatedByShield

- **Category:** <span class="cat-dot" style="--cat-color: #ef4444" data-cat="Combat & Abilities"></span> Combat & Abilities
- **Namespace:** `Global`
- **Assembly:** `Dew.Core.dll`

```csharp
public struct EventInfoDamageNegatedByShield
```

## Fields (5)

::: details Click to expand Fields (5)

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`actor`** | `public Actor actor` | The actor who started the damage. |
| **`damage`** | `public FinalDamageData damage` |  |
| **`negatedAmount`** | `public float negatedAmount` |  |
| **`shield`** | `[NonSerialized] public ShieldEffect shield` | The shield effect responsible for this event. Only available on server. |
| **`victim`** | `public Entity victim` |  |

:::


## Architecture & Relationships

::: details Click to expand Architecture & Relationships

### Used By (6)

*Classes and systems that invoke, reference, or depend on `EventInfoDamageNegatedByShield`:*

`ACH_SHIELD_BATTERY` · `Ai_Mon_Special_BossObliviax_ChargeSequence_Ready` · [ClientEventManager](/api/Global.ClientEventManager) · `Gem_L_Supersymmetry` · `Se_GenericShield_OneShot` · `Mirror.GeneratedNetworkCode`

### Dependencies (4)

*Types and components that `EventInfoDamageNegatedByShield` references or depends upon:*

[Actor](/api/Global.Actor) · [Entity](/api/Global.Entity) · [FinalDamageData](/api/Global.FinalDamageData) · [ShieldEffect](/api/Global.ShieldEffect)

:::
