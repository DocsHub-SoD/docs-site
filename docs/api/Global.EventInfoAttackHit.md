# Struct: EventInfoAttackHit

- **Category:** <span class="cat-dot" style="--cat-color: #ef4444" data-cat="Combat & Abilities"></span> Combat & Abilities
- **Namespace:** `Global`
- **Assembly:** `Dew.Core.dll`

```csharp
public struct EventInfoAttackHit
```

## Fields (5)

::: details Click to expand Fields (5)

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`actor`** | `public Actor actor` | The actor who invoked this event in an actor chain. |
| **`attacker`** | `public Entity attacker` | Attacker of this hit. |
| **`isCrit`** | `public bool isCrit` | Is hit attack critical hit? |
| **`strength`** | `public float strength` | Strength of this attack. Set to 1 by default. |
| **`victim`** | `public Entity victim` | Victim of this hit. |

:::


## Architecture & Relationships

::: details Click to expand Architecture & Relationships

### Used By (18)

*Classes and systems that invoke, reference, or depend on `EventInfoAttackHit`:*

`ACH_THOUSAND_THUNDERS` · [Actor](/api/Global.Actor) · `Ai_Q_IncendiaryRounds_Attack` · [ClientEventManager](/api/Global.ClientEventManager) · `Gem_E_Domination` · `Gem_E_Fangs` · `Gem_R_Crucible` · `Se_R_AnnihilationStance` · `Se_Shrine_SmallSoul` · `Se_Star_Bismuth_D_BonusAttackEffect` · `Se_Star_Bismuth_D_Conquerer_Stacks` · `Se_Star_Husk_L_DodgeCooldownOnKillOrAttack` · `Se_Star_I_GoldPerCrit` · `Se_Star_L_HealOnAttack` · [SkillTrigger](/api/Global.SkillTrigger) · `St_D_QuartetOfDeath` · [Summon](/api/Global.Summon) · `Mirror.GeneratedNetworkCode`

### Dependencies (2)

*Types and components that `EventInfoAttackHit` references or depends upon:*

[Actor](/api/Global.Actor) · [Entity](/api/Global.Entity)

:::
