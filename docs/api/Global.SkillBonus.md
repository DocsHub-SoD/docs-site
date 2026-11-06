# Class: SkillBonus

- **Category:** <span class="cat-dot" style="--cat-color: #ef4444" data-cat="Combat & Abilities"></span> Combat & Abilities
- **Namespace:** `Global`
- **Assembly:** `Dew.Core.dll`

```csharp
[Serializable]
public class SkillBonus
```

## Fields (1)

::: details Click to expand Fields (1)

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`ignoreReceiveCooldownReductionFlag`** | `public bool ignoreReceiveCooldownReductionFlag` |  |

:::

## Properties (4)

::: details Click to expand Properties (4)

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`addedCharge`** | `public int addedCharge { get; set; }` |  |
| **`cooldownMultiplier`** | `public float cooldownMultiplier { get; set; }` |  |
| **`cooldownOffset`** | `public float cooldownOffset { get; set; }` |  |
| **`parent`** | `public SkillTrigger parent { get; }` |  |

:::

## Methods (2)

::: details `Clone()`

```csharp
public SkillBonus Clone()
```

**Returns:** `SkillBonus`

:::

::: details `Stop()`

```csharp
public void Stop()
```

:::


## Architecture & Relationships

::: details Click to expand Architecture & Relationships

### Used By (56)

*Classes and systems that invoke, reference, or depend on `SkillBonus`:*

`Gem_C_Efficiency` · `Gem_E_Direness` · `Gem_E_Inversion` · `Gem_E_Virtuousness` · `Gem_L_ChaosApple` · `Gem_L_Embertail` · `Gem_L_Paranoia` · `Gem_R_Lightweight` · `Se_Gem_L_Infinity` · `Se_Gem_R_Panic` · `Se_RoomMod_UnstableVeilOfTime_ModifyCooldowns` · `Se_Star_Aurena_F_DT_TwiceWithPenalty` · `Se_Star_Aurena_F_RE_CooldownButNoHeal` · `Se_Star_Bismuth_F_DM_BonusOnFullCharge` · `Se_Star_Bismuth_F_IN_LessCooldownLessMissiles` · `Se_Star_Bismuth_F_IN_MoreProjByAtkSpd` · `Se_Star_Bismuth_F_IT_AddedDurationOnHit` · `Se_Star_Bismuth_F_VH_Shield` · `Se_Star_Bismuth_L_DodgeNoDashMoreCharges` · `Se_Star_Cetus_F_BA_LightningEcho` · `Se_Star_Husk_D_MovementSkillHaste` · `Se_Star_Husk_F_LA_DodgeResetOnRed` · `Se_Star_Husk_F_LA_QuickBlueForm` · `Se_Star_Husk_L_DodgeChargesAndRangeWithPenalty` · `Se_Star_Husk_L_DodgeCooldownOnKillWithEmptyCharges` · `Se_Star_L_DodgeCooldown` · `Se_Star_L_DodgeCooldownOnLowHealth` · `Se_Star_Lacerta_F_HC_NoDelayDoubleCast` · `Se_Star_Lacerta_F_HC_ResetOnDodge` · `Se_Star_Lacerta_F_IR_MoreShots` · `Se_Star_Lacerta_F_QT_AddedCharges` · `Se_Star_Lacerta_F_QT_RapidFire` · `Se_Star_Lacerta_L_DodgeCharges` · `Se_Star_Mist_F_FL_DecreasedCooldownAndCharge` · `Se_Star_Mist_F_LG_ChainAttack` · `Se_Star_Mist_F_LG_SingleTarget` · `Se_Star_Mist_F_PR_AllDirections` · `Se_Star_Mist_F_PR_PerfectParry` · `Se_Star_Mist_L_AddedDodgeWithPenalty` · `Se_Star_Mist_L_DodgeCooldownWithPenalty` · `Se_Star_Nachia_F_MP_NoJump` · `Se_Star_Nachia_F_MP_StrongerFenrirNoCast` · `Se_Star_Nachia_F_NW_LessCooldownLessAtkSpd` · `Se_Star_Nachia_F_SC_MoreSummons` · `Se_Star_Nachia_L_WaltzArmor` · `Se_Star_Nachia_L_WaltzDurationWithPenalty` · `Se_Star_Vesper_F_DP_SwitchToMelee` · `Se_Star_Yubar_F_TQ_EssenceCooldown` · `Se_Star_Yubar_F_TQ_LowerCooldownNoInvul` · `Se_Star_Yubar_F_TQ_ReducedCooldownAndDuration` · `Se_Star_Yubar_L_DodgeChargeWithLongerCooldown` · `Se_Star_Yubar_L_DodgeCooldownWithShorterRange` · [SkillTrigger](/api/Global.SkillTrigger) · `St_D_ParryMaster` · `St_Q_Fleche` · [StarEffect](/api/Global.StarEffect)

### Dependencies (1)

*Types and components that `SkillBonus` references or depends upon:*

[SkillTrigger](/api/Global.SkillTrigger)

:::
