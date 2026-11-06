# Struct: EventInfoAbilityInstance

- **Category:** <span class="cat-dot" style="--cat-color: #ef4444" data-cat="Combat & Abilities"></span> Combat & Abilities
- **Namespace:** `Global`
- **Assembly:** `Dew.Core.dll`

```csharp
public struct EventInfoAbilityInstance
```

## Fields (2)

::: details Click to expand Fields (2)

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`actor`** | `public Actor actor` | The actor who invoked this event in an actor chain. |
| **`instance`** | `public AbilityInstance instance` |  |

:::


## Architecture & Relationships

::: details Click to expand Architecture & Relationships

### Used By (118)

*Classes and systems that invoke, reference, or depend on `EventInfoAbilityInstance`:*

[Actor](/api/Global.Actor) · `Ai_Q_EtherealInfluence` · `Ai_Q_SuperNova` · `Gem_E_OurStory_Completed` · `Hero_Husk` · `Mon_Sky_BossNyx` · `Mon_SnowMountain_LivingShards` · `Se_Nor_WindowToTheSoul_SpiritualDominance` · `Se_R_Cataclysm` · `Se_Star_Aurena_F_CR_GlobalHeal` · `Se_Star_Aurena_F_CR_NoHealCooldownReduction` · `Se_Star_Aurena_F_DT_LowerThresholdBiggerHeals` · `Se_Star_Aurena_F_DT_TwiceWithPenalty` · `Se_Star_Aurena_F_DT_UnstoppableAndRemoveDelusion` · `Se_Star_Aurena_F_GB_LessDamageLessSacrifice` · `Se_Star_Aurena_F_RE_AtkEffect` · `Se_Star_Aurena_F_RE_CooldownButNoHeal` · `Se_Star_Aurena_F_RE_MoreProjMoreSacrifice` · `Se_Star_Bismuth_F_DM_BonusOnFullCharge` · `Se_Star_Bismuth_F_DM_MoreShootNoMove` · `Se_Star_Bismuth_F_DM_NonFullChargeCooldown` · `Se_Star_Bismuth_F_IN_Elementals` · `Se_Star_Bismuth_F_IN_LessCooldownLessMissiles` · `Se_Star_Bismuth_F_IN_MoreProjByAtkSpd` · `Se_Star_Bismuth_F_IT_AddedDurationOnHit` · `Se_Star_Bismuth_F_IT_InnerDamage` · `Se_Star_Bismuth_F_IT_SmallerRingAddDisplacement` · `Se_Star_Bismuth_F_IT_SmallerRingMoreDamage` · `Se_Star_Bismuth_F_VH_ResetOnDodge` · `Se_Star_Bismuth_L_DodgeNoDashMoreCharges` · `Se_Star_Cetus_F_BA_CdReductionOnKill` · `Se_Star_Cetus_F_BA_ChargeMsNoShield` · `Se_Star_Cetus_F_BA_LightningEcho` · `Se_Star_Cetus_F_BI_FastChargeTakeDamageUp` · `Se_Star_Cetus_F_BI_MaxChargeTimePerLevel` · `Se_Star_Cetus_F_BI_SelfDamageAoeCold` · `Se_Star_Cetus_F_EM_ChaseTarget` · `Se_Star_Cetus_F_EM_DamageUpSelfDamage` · `Se_Star_Cetus_F_EM_InfiniteDuration` · `Se_Star_Cetus_F_FR_RecastCdrNoKnockback` · `Se_Star_Husk_F_AS_NoShockwaveFasterAttack` · `Se_Star_Husk_F_AS_NonUltimate` · `Se_Star_Husk_F_DE_MarkHitDodgeCDR` · `Se_Star_Husk_F_LA_BlueFormOnly` · `Se_Star_Husk_F_LA_DodgeResetOnRed` · `Se_Star_Husk_F_LA_QuickBlueForm` · `Se_Star_Husk_F_LA_SingleTargetCooldown` · `Se_Star_Husk_L_DodgeChargesAndRangeWithPenalty` · `Se_Star_Lacerta_F_HC_KnockbackAndSlow` · `Se_Star_Lacerta_F_HC_NearDamage` · `Se_Star_Lacerta_F_HC_NoDelayDoubleCast` · `Se_Star_Lacerta_F_IR_AoEDamage` · `Se_Star_Lacerta_F_IR_MoreShots` · `Se_Star_Lacerta_F_IR_RechargeAmmoAmpBurnDamage` · `Se_Star_Lacerta_F_PS_ChargeSpeed` · `Se_Star_Lacerta_F_PS_CooldownReset` · `Se_Star_Lacerta_F_PS_SlowerStronger` · `Se_Star_Lacerta_F_QT_AttackEffect` · `Se_Star_Lacerta_F_QT_RapidFire` · `Se_Star_Mist_F_FL_Lightning` · `Se_Star_Mist_F_FL_MaxRangeExplosion` · `Se_Star_Mist_F_LG_ChainAttack` · `Se_Star_Mist_F_LG_IncreasedCooldownReduction` · `Se_Star_Mist_F_LG_SingleTarget` · `Se_Star_Mist_F_PR_ShieldAndCrit` · `Se_Star_Mist_F_UD_HealLostHealth` · `Se_Star_Mist_F_UD_NonUltimate` · `Se_Star_Nachia_F_MP_NachiaHeal` · `Se_Star_Nachia_F_MP_NoJump` · `Se_Star_Nachia_F_MP_StrongerFenrirNoCast` · `Se_Star_Nachia_F_NW_LessCooldownLessAtkSpd` · `Se_Star_Nachia_F_NW_MovSpeed` · `Se_Star_Nachia_F_NW_Teleport` · `Se_Star_Nachia_F_SB_DurationBonus` · `Se_Star_Nachia_F_SB_SecondWind` · `Se_Star_Nachia_F_SB_StrongerBuffNoSelf` · `Se_Star_Nachia_F_SC_AtkEffect` · `Se_Star_Nachia_F_SC_MoreSummons` · `Se_Star_Nachia_L_SelfWaltz` · `Se_Star_Nachia_L_WaltzArmor` · `Se_Star_Nachia_L_WaltzDurationWithPenalty` · `Se_Star_Vesper_F_BS_ADWithArmor` · `Se_Star_Vesper_F_BS_AddedDurationPerAtk` · `Se_Star_Vesper_F_BS_ExplosionOnEnd` · `Se_Star_Vesper_F_BS_MovSpd` · `Se_Star_Vesper_F_CS_ColdDamage` · `Se_Star_Vesper_F_CS_LingeringBenefits` · `Se_Star_Vesper_F_CS_UnlockMoveWithPenalty` · `Se_Star_Vesper_F_DP_FarTargetBonus` · `Se_Star_Vesper_F_DP_PointCast` · `Se_Star_Vesper_F_DP_SwitchToMelee` · `Se_Star_Vesper_F_SE_FullOffense` · `Se_Star_Vesper_F_SE_Invulnerability` · `Se_Star_Vesper_F_SE_PointCast` · `Se_Star_Vesper_L_EmpowerDodgeShield` · `Se_Star_Yubar_F_CC_DamageOverTime` · `Se_Star_Yubar_F_CC_IncreaseAD` · `Se_Star_Yubar_F_CC_LongerDuration` · `Se_Star_Yubar_F_CC_MeteorPerLightSkill` · `Se_Star_Yubar_F_EI_BiggerExplosion` · `Se_Star_Yubar_F_EI_DashNoProjectile` · `Se_Star_Yubar_F_EI_NoRootMoreDamage` · `Se_Star_Yubar_F_SN_Artillery` · `Se_Star_Yubar_F_SN_AutoExplosion` · `Se_Star_Yubar_F_SN_PullEnemy` · `Se_Star_Yubar_F_TQ_EssenceCooldown` · `Se_Star_Yubar_F_TQ_LowerCooldownNoInvul` · `Se_Star_Yubar_F_TQ_ReducedCooldownAndDuration` · `Star_Lacerta_IncendiaryRounds` · `Star_Lacerta_PrecisionShot` · `Star_Mist_LightningFleche` · `Star_Mist_ParryAllDirections` · `Star_Mist_UnbreakableDeterminationHeal` · `Star_Vesper_SanctuaryOfElHeal` · `Star_Vesper_StrongerSuppression` · `Star_Yubar_StrongerCataclysm` · `Star_Yubar_StrongerSuperNova` · `Star_Yubar_TranquilityDamage`

### Dependencies (2)

*Types and components that `EventInfoAbilityInstance` references or depends upon:*

[AbilityInstance](/api/Global.AbilityInstance) · [Actor](/api/Global.Actor)

:::
