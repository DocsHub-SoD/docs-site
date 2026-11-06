# Class: PersistentStatBonusEffect

- **Category:** <span class="cat-dot" style="--cat-color: #ef4444" data-cat="Combat & Abilities"></span> Combat & Abilities
- **Namespace:** `Global`
- **Assembly:** `Dew.Core.dll`
- **Attributes:** `[SaveActor]`
- **Inheritance / Derived:** [DewNetworkBehaviour](/api/Global.DewNetworkBehaviour) → [Actor](/api/Global.Actor) → [AbilityInstance](/api/Global.AbilityInstance) → [StatusEffect](/api/Global.StatusEffect)

```csharp
[SaveActor(true)]
public class PersistentStatBonusEffect : StatusEffect, ILogicUpdate, ICleanup, ICustomDestroyRoutine
```

## Fields (1)

::: details Click to expand Fields (1)

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`bonus`** | `[SaveVar] [SaveVar(SaveVarFlags.Default)] public StatBonus bonus` |  |

:::

## Methods (1)

::: details `OnCreate()`

```csharp
protected override void OnCreate()
```

:::


## Architecture & Relationships

::: details Click to expand Architecture & Relationships

### Used By (8)

*Classes and systems that invoke, reference, or depend on `PersistentStatBonusEffect`:*

`Se_Culinary_StatReward` · `Se_D_IceColdPresence_PersistentBuff` · `Se_Gem_E_Domination_Buff` · `Se_Gem_E_Predation_StatBonus` · `Se_Gem_R_Frost_Stat` · `Se_L_HerosReturn_Buff` · `Se_Shrine_Chaos_StatBonus` · `Se_Star_Husk_L_FatalHitProtectionWithPenalty_Repaired`

### Dependencies (2)

*Types and components that `PersistentStatBonusEffect` references or depends upon:*

[StatBonus](/api/Global.StatBonus) · [StatusEffect](/api/Global.StatusEffect)

### Related Enums (1)

*Enumerations referenced in fields, properties, or method signatures:*

[`SaveVarFlags`](/enums#savevarflags)

:::
