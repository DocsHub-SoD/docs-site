# Struct: EventInfoShield

- **Category:** <span class="cat-dot" style="--cat-color: #a855f7" data-cat="Buffs & Statuses"></span> Buffs & Statuses
- **Namespace:** `Global`
- **Assembly:** `Dew.Core.dll`

```csharp
public struct EventInfoShield
```

## Fields (6)

::: details Click to expand Fields (6)

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`chain`** | `public ReactionChain chain` |  |
| **`discardedAmount`** | `public float discardedAmount` | The amount of discarded shield due to total max restrictions. |
| **`finalAmount`** | `public float finalAmount` | The amount of shield after being processed by processors. |
| **`originalAmount`** | `public float originalAmount` | The amount of shield before being processed by processors. |
| **`statusEffect`** | `public StatusEffect statusEffect` | The status effect that is giving the entity shield. |
| **`target`** | `public Entity target` | The entity receiving the shield. |

:::


## Architecture & Relationships

::: details Click to expand Architecture & Relationships

### Used By (9)

*Classes and systems that invoke, reference, or depend on `EventInfoShield`:*

`ACH_BARE_SKIN_SUPREMACY` · [Actor](/api/Global.Actor) · [ClientEventManager](/api/Global.ClientEventManager) · `Gem_C_Love` · `Gem_R_Glass` · `Se_Star_Cetus_L_ArmorBuffOnShield` · `Se_Star_Nachia_L_AllyUnstoppable` · `St_D_HeartOfThePack` · `Mirror.GeneratedNetworkCode`

### Dependencies (3)

*Types and components that `EventInfoShield` references or depends upon:*

[Entity](/api/Global.Entity) · [ReactionChain](/api/Global.ReactionChain) · [StatusEffect](/api/Global.StatusEffect)

:::
