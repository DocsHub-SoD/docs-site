# Struct: EventInfoAttackEffect

- **Category:** <span class="cat-dot" style="--cat-color: #ef4444" data-cat="Combat & Abilities"></span> Combat & Abilities
- **Namespace:** `Global`
- **Assembly:** `Dew.Core.dll`

```csharp
public struct EventInfoAttackEffect
```

## Fields (6)

::: details Click to expand Fields (6)

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`actor`** | `public Actor actor` |  |
| **`attacker`** | `public Entity attacker` |  |
| **`chain`** | `public ReactionChain chain` |  |
| **`strength`** | `public float strength` |  |
| **`type`** | `public AttackEffectType type` |  |
| **`victim`** | `public Entity victim` |  |

:::


## Architecture & Relationships

::: details Click to expand Architecture & Relationships

### Used By (24)

*Classes and systems that invoke, reference, or depend on `EventInfoAttackEffect`:*

[Actor](/api/Global.Actor) · `Gem_L_Embertail` · `Gem_R_Momentum` · `Gem_R_NightSky` · `Se_D_AstridsMasterpieceEnGarde` · `Se_D_AstridsMasterpiecePriorite` · `Se_D_BeautifulThreat` · `Se_D_IcyVeins` · `Se_D_MasterOfAssassination_Exposed` · `Se_D_MercyOfEl` · `Se_Gem_R_Wound_Wounded` · `Se_L_Multishot_Buff` · `Se_Nor_WindowToTheSoul_SpiritualDominance` · `Se_R_ShadowWalk_EmpowerAttacks` · `Se_R_UnbreakableDetermination` · `Se_Star_Husk_F_DE_MarkHitDodgeCDR` · `Se_Treasure_CrimsonElixir_AdBoost` · `St_D_CircleOfLife` · `St_D_DanceOfValor` · `St_D_DisintegratingClaw` · `St_E_Harvest` · `St_Q_Discipline` · `St_R_LightningDance` · `St_R_Somersault`

### Dependencies (3)

*Types and components that `EventInfoAttackEffect` references or depends upon:*

[Actor](/api/Global.Actor) · [Entity](/api/Global.Entity) · [ReactionChain](/api/Global.ReactionChain)

### Related Enums (1)

*Enumerations referenced in fields, properties, or method signatures:*

[`AttackEffectType`](/enums#attackeffecttype)

:::
