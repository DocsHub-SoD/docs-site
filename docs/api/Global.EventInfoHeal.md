# Struct: EventInfoHeal

- **Category:** <span class="cat-dot" style="--cat-color: #f97316" data-cat="Data & Core Math"></span> Data & Core Math
- **Namespace:** `Global`
- **Assembly:** `Dew.Core.dll`

```csharp
public struct EventInfoHeal
```

## Fields (8)

::: details Click to expand Fields (8)

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`actor`** | `public Actor actor` | The actor who invoked this event in an actor chain. |
| **`amount`** | `public float amount` | Actual amount. |
| **`canMerge`** | `public bool canMerge` |  |
| **`chain`** | `public ReactionChain chain` |  |
| **`discardedAmount`** | `public float discardedAmount` | Discarded amount due to going over the maximum. |
| **`heal`** | `public FinalHealData heal` |  |
| **`isCrit`** | `public bool isCrit` |  |
| **`target`** | `public Entity target` |  |

:::


## Architecture & Relationships

::: details Click to expand Architecture & Relationships

### Used By (18)

*Classes and systems that invoke, reference, or depend on `EventInfoHeal`:*

`ACH_OVERFLOWING_HEALS` · [Actor](/api/Global.Actor) · [ClientEventManager](/api/Global.ClientEventManager) · [Gem](/api/Global.Gem) · `Gem_C_Guidance` · `Gem_C_Love` · `Gem_R_Ricochet` · `Gem_U_GlacialCore` · `Se_D_BeautifulThreat` · `Se_Star_Aurena_I_PotionGold` · `Se_Star_Aurena_L_ShareHeal` · `Se_Star_Mist_L_PotionShield` · `Se_Star_Nachia_L_AllyUnstoppable` · `St_D_HeartOfThePack` · `Treasure_SparklingElixir` · `UI_DamageNumberGroup` · `UI_DamageNumberText` · `Mirror.GeneratedNetworkCode`

### Dependencies (4)

*Types and components that `EventInfoHeal` references or depends upon:*

[Actor](/api/Global.Actor) · [Entity](/api/Global.Entity) · [FinalHealData](/api/Global.FinalHealData) · [ReactionChain](/api/Global.ReactionChain)

:::
