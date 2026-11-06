# Struct: EventInfoAttackFired

- **Category:** <span class="cat-dot" style="--cat-color: #ef4444" data-cat="Combat & Abilities"></span> Combat & Abilities
- **Namespace:** `Global`
- **Assembly:** `Dew.Core.dll`

```csharp
public struct EventInfoAttackFired
```

## Fields (7)

::: details Click to expand Fields (7)

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`actor`** | `public Actor actor` | The actor who invoked this event in an actor chain. |
| **`everyFourAttackNormalizedProgress`** | `public float everyFourAttackNormalizedProgress` | Charge amount of every four attack effect, after firing this basic attack. |
| **`info`** | `public CastInfo info` | Cast info of this attack. Note the attack might be directional cast thus have no target. |
| **`instance`** | `public AbilityInstance instance` | The attack ability instance. |
| **`isCrit`** | `public bool isCrit` | Is fired attack critical hit? |
| **`isNextAttackFourthAttack`** | `public bool isNextAttackFourthAttack` | Is next attack going to be fourth attack? |
| **`isThisAttackFourthAttack`** | `public bool isThisAttackFourthAttack` | Is this attack fourth attack? |

:::


## Architecture & Relationships

::: details Click to expand Architecture & Relationships

### Used By (22)

*Classes and systems that invoke, reference, or depend on `EventInfoAttackFired`:*

`Gem_E_Crimson` · `Gem_E_Fangs` · `Gem_E_Twilight` · `Gem_R_Shock` · `Mon_Ink_EgoSword` · `Se_D_ConvergencePoint` · `Se_D_DoubleTap` · `Se_D_ExoticMatter` · `Se_Nor_MyOwnLittleNebula` · `Se_Nor_ReptilianThirdEye` · `Se_Q_IncendiaryRounds_EmpowerAttacks` · `Se_R_AnnihilationStance` · `Se_R_DangerousTheory` · `St_C_LuckyHammer` · `St_C_SpearThrow` · `St_D_MercyOfEl` · `St_D_MomentumOfCombat` · `St_D_QuartetOfDeath` · `St_D_Resolve` · `St_D_RoaringFist` · `St_D_SalamanderPowder` · `St_D_ThirstOfVengence`

### Dependencies (3)

*Types and components that `EventInfoAttackFired` references or depends upon:*

[AbilityInstance](/api/Global.AbilityInstance) · [Actor](/api/Global.Actor) · [CastInfo](/api/Global.CastInfo)

:::
