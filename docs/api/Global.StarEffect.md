# Class: StarEffect

- **Category:** <span class="cat-dot" style="--cat-color: #ef4444" data-cat="Combat & Abilities"></span> Combat & Abilities
- **Namespace:** `Global`
- **Assembly:** `Dew.Core.dll`
- **Attributes:** `[SaveActor]`
- **Inheritance / Derived:** [DewNetworkBehaviour](/api/Global.DewNetworkBehaviour) → [Actor](/api/Global.Actor) → [AbilityInstance](/api/Global.AbilityInstance) → [StatusEffect](/api/Global.StatusEffect)

```csharp
[SaveActor(true)]
public class StarEffect : StatusEffect, ILogicUpdate, ICleanup, ICustomDestroyRoutine
```

## Fields (5)

::: details Click to expand Fields (5)

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`maxStarLevel`** | `[BoxGroup("Star Settings", true, false, 0)] public int maxStarLevel` |  |
| **`price`** | `[BoxGroup("Star Settings", true, false, 0)] public int[] price` |  |
| **`requiredLevel`** | `[BoxGroup("Star Settings", true, false, 0)] [LabelText("Req. Mastery Level")] public int requiredLevel` |  |
| **`starIcon`** | `[BoxGroup("Star Settings", true, false, 0)] public Sprite starIcon` |  |
| **`type`** | `[BoxGroup("Star Settings", true, false, 0)] public StarType type` |  |

:::

## Properties (8)

::: details Click to expand Properties (8)

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`hero`** | `public Hero hero { get; }` |  |
| **`heroType`** | `public virtual Type heroType { get; }` |  |
| **`isMovementSkillType`** | `public virtual bool isMovementSkillType { get; }` |  |
| **`player`** | `public DewPlayer player { get; }` |  |
| **`skill`** | `public SkillTrigger skill { get; }` |  |
| **`skills`** | `public SkillTrigger[] skills { get; }` | This never returns null. |
| **`skillType`** | `public virtual Type skillType { get; }` |  |
| **`strength`** | `[SaveVar] [SaveVar(SaveVarFlags.Default)] public float strength { get; set; }` | Strength of this star effect. Usually 1.0f, but can be lower if non-flexible star is slotted in different category slot. |

:::

## Methods (6)

::: details `DoSkill(Action&lt;SkillTrigger&gt;)`

Do custom action on all matching skill. You can invoke the returned action to immediately call cleanup functions to stop the effect.

```csharp
public SafeAction DoSkill(Action<SkillTrigger> callback)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `callback` | [`System.Action<T><SkillTrigger>`](/api/Global.SkillTrigger) |  |

**Returns:** `SafeAction`

:::

::: details `DoSkill(Func&lt;SkillTrigger, Action&gt;)`

Do custom action on all matching skill and do custom cleanup. You can invoke the returned action to immediately call cleanup functions to stop the effect.

```csharp
public SafeAction DoSkill(Func<SkillTrigger, Action> callback)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `callback` | [`System.Func<T, TResult><SkillTrigger,System.Action>`](/api/Global.SkillTrigger) |  |

**Returns:** `SafeAction`

:::

::: details `DoSkillBonusAll(SkillBonus)`

Note the given bonus will be cloned. You can invoke the returned action to immediately call cleanup functions to stop the effect.

```csharp
public SafeAction DoSkillBonusAll(SkillBonus bonus)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `bonus` | [`SkillBonus`](/api/Global.SkillBonus) |  |

**Returns:** `SafeAction`

:::

::: details `IsIncompatibleWith(Hero, HeroLoadoutData)`

```csharp
public bool IsIncompatibleWith(Hero h, HeroLoadoutData l)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `h` | [`Hero`](/api/Global.Hero) |  |
| `l` | [`HeroLoadoutData`](/api/Global.HeroLoadoutData) |  |

**Returns:** `bool`

:::

::: details `IsSkillRelated(SkillTrigger)`

```csharp
public bool IsSkillRelated(SkillTrigger s)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `s` | [`SkillTrigger`](/api/Global.SkillTrigger) |  |

**Returns:** `bool`

:::

::: details `IsSkillRelated(string)`

```csharp
public bool IsSkillRelated(string s)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `s` | `string` |  |

**Returns:** `bool`

:::


## Architecture & Relationships

::: details Click to expand Architecture & Relationships

### Used By (309)

*Classes and systems that invoke, reference, or depend on `StarEffect`:*

[AbilityInstance](/api/Global.AbilityInstance) · [DewSave](/api/Global.DewSave) · `EveryZoneStarEffect` · `HealthThresholdBonusStarEffect` · `Se_Star_Aurena_D_AbilityPower` · `Se_Star_Aurena_D_AtkSpd` · `Se_Star_Aurena_D_AttackDamage` · `Se_Star_Aurena_F_CR_ChargedCast` · `Se_Star_Aurena_F_CR_EarnGold` · `Se_Star_Aurena_F_CR_GlobalHeal` · `Se_Star_Aurena_F_CR_NoHealCooldownReduction` · `Se_Star_Aurena_F_DT_LowerThresholdBiggerHeals` · `Se_Star_Aurena_F_DT_TwiceWithPenalty` · `Se_Star_Aurena_F_DT_UnstoppableAndRemoveDelusion` · `Se_Star_Aurena_F_GB_LessDamageLessSacrifice` · `Se_Star_Aurena_F_GB_NoSacrificeAfterDodge` · `Se_Star_Aurena_F_GB_NoWitherNoSacrifice` · `Se_Star_Aurena_F_RE_AtkEffect` · `Se_Star_Aurena_F_RE_CooldownButNoHeal` · `Se_Star_Aurena_F_RE_MoreProjMoreSacrifice` · `Se_Star_Aurena_I_BonusFromStones` · `Se_Star_Aurena_I_GoldEveryZone` · `Se_Star_Aurena_I_GoldOnMerchantDamage` · `Se_Star_Aurena_I_PotionGold` · `Se_Star_Aurena_L_Armor` · `Se_Star_Aurena_L_HealAmpOnLowHp` · `Se_Star_Aurena_L_HealAmpWithPenalty` · `Se_Star_Aurena_L_ShareHeal` · `Se_Star_Aurena_L_SpeedOnDamage` · `Se_Star_Bismuth_D_AtkSpd` · `Se_Star_Bismuth_D_AtkSpdFromDismantle` · `Se_Star_Bismuth_D_BonusAttackEffect` · `Se_Star_Bismuth_D_Conquerer` · `Se_Star_Bismuth_D_SkillHasteAndAutoCast` · `Se_Star_Bismuth_F_DM_BonusOnFullCharge` · `Se_Star_Bismuth_F_DM_MoreShootNoMove` · `Se_Star_Bismuth_F_DM_NonFullChargeCooldown` · `Se_Star_Bismuth_F_IN_Elementals` · `Se_Star_Bismuth_F_IN_LessCooldownLessMissiles` · `Se_Star_Bismuth_F_IN_MoreProjByAtkSpd` · `Se_Star_Bismuth_F_IT_AddedDurationOnHit` · `Se_Star_Bismuth_F_IT_InnerDamage` · `Se_Star_Bismuth_F_IT_SmallerRingAddDisplacement` · `Se_Star_Bismuth_F_IT_SmallerRingMoreDamage` · `Se_Star_Bismuth_F_VH_FullCharge` · `Se_Star_Bismuth_F_VH_ResetOnDodge` · `Se_Star_Bismuth_F_VH_Shield` · `Se_Star_Bismuth_I_DismantleMemoryDreamDust` · `Se_Star_Bismuth_I_KnowledgeBook` · `Se_Star_Bismuth_I_SecretJournal` · `Se_Star_Bismuth_I_ShopDiscount` · `Se_Star_Bismuth_I_TreasureWithHealthPenalty` · `Se_Star_Bismuth_L_ContinuousSpeed` · `Se_Star_Bismuth_L_DodgeNoDashMoreCharges` · `Se_Star_Bismuth_L_SecondWindWithPenalty` · `Se_Star_Cetus_D_AdApUpByBonusHp` · `Se_Star_Cetus_D_ApUpByColdSkillCounts` · `Se_Star_Cetus_D_StackStatsOnTakenDamage` · `Se_Star_Cetus_D_StatsUpWhileShielded` · `Se_Star_Cetus_F_BA_CdReductionOnKill` · `Se_Star_Cetus_F_BA_ChargeMsNoShield` · `Se_Star_Cetus_F_BA_LightningEcho` · `Se_Star_Cetus_F_BI_FastChargeTakeDamageUp` · `Se_Star_Cetus_F_BI_MaxChargeTimePerLevel` · `Se_Star_Cetus_F_BI_SelfDamageAoeCold` · `Se_Star_Cetus_F_EM_ChaseTarget` · `Se_Star_Cetus_F_EM_DamageUpSelfDamage` · `Se_Star_Cetus_F_EM_InfiniteDuration` · `Se_Star_Cetus_F_FR_CdReductionOnTakeDamage` · `Se_Star_Cetus_F_FR_ChangeToUltHitReset` · `Se_Star_Cetus_F_FR_RecastCdrNoKnockback` · `Se_Star_Cetus_I_ColdDiscountFireSurcharge` · `Se_Star_Cetus_I_FirstColdGemQualityBoost` · `Se_Star_Cetus_I_GetDreamDustOnBossKill` · `Se_Star_Cetus_I_StartWithResources` · `Se_Star_Cetus_L_ArmorBuffOnShield` · `Se_Star_Cetus_L_DodgeCdReductionOnHit` · `Se_Star_Cetus_L_FrostResistAndBuff` · `Se_Star_Cetus_L_HealOnApDamage` · `Se_Star_Cetus_L_IncreaseDealtShield` · `Se_Star_Cetus_L_MaxHpDamagePenalty` · `Se_Star_Cetus_L_ScalingHealth` · `Se_Star_D_AbilityPower` · `Se_Star_D_AttackDamage` · `Se_Star_D_AttackSpeed` · `Se_Star_D_BossDamageAmp` · `Se_Star_D_CritChance` · `Se_Star_D_CritDamage` · `Se_Star_D_CritUpHitDecay` · `Se_Star_D_DamageBonusOnAllElemental` · `Se_Star_D_DarkAmp` · `Se_Star_D_FireAmp` · `Se_Star_D_LightAmp` · `Se_Star_D_LowerADScalingAP` · `Se_Star_D_LowerAPScalingAD` · `Se_Star_D_LowerASHigherAD` · `Se_Star_D_RiftFirstCastDamageUp` · `Se_Star_D_ScalingAbilityPower` · `Se_Star_D_ScalingAttackDamage` · `Se_Star_D_ScalingAttackSpeedWithPenalty` · `Se_Star_D_ShieldDamageAmp` · `Se_Star_D_TempAbilityPower` · `Se_Star_D_TempAttackDamage` · `Se_Star_D_UltimateChargeSpeed` · `Se_Star_Husk_D_AttackDamage` · `Se_Star_Husk_D_CritAmp` · `Se_Star_Husk_D_DamageAmpOnLowHpTarget` · `Se_Star_Husk_D_DamageOverTimeCritWithPenalty` · `Se_Star_Husk_D_DarkAttackWithPenalty` · `Se_Star_Husk_D_MovementSkillHaste` · `Se_Star_Husk_D_ScalingAdAndAtkSpd` · `Se_Star_Husk_F_AS_AddedDurationOnHit` · `Se_Star_Husk_F_AS_NoShockwaveFasterAttack` · `Se_Star_Husk_F_AS_NonUltimate` · `Se_Star_Husk_F_DC_EndMovespeedToBonusAttackspeed` · `Se_Star_Husk_F_DC_EnhanceMaxStealthTime` · `Se_Star_Husk_F_DC_RecentDamageHoTWhileStealth` · `Se_Star_Husk_F_DE_HighAmpMissReset` · `Se_Star_Husk_F_DE_HitHealMissPenalty` · `Se_Star_Husk_F_DE_MarkHitDodgeCDR` · `Se_Star_Husk_F_LA_BlueFormOnly` · `Se_Star_Husk_F_LA_DodgeResetOnRed` · `Se_Star_Husk_F_LA_QuickBlueForm` · `Se_Star_Husk_F_LA_SingleTargetCooldown` · `Se_Star_Husk_I_BossKillPlatinumCoin` · `Se_Star_Husk_I_ShopIntimidation` · `Se_Star_Husk_L_DodgeChargesAndRangeWithPenalty` · `Se_Star_Husk_L_DodgeCooldownOnKillOrAttack` · `Se_Star_Husk_L_DodgeCooldownOnKillWithEmptyCharges` · `Se_Star_Husk_L_FatalHitProtectionWithPenalty` · `Se_Star_I_AdditionalChaosChance` · `Se_Star_I_DismantleBonus` · `Se_Star_I_DismantleDustToBonusGold` · `Se_Star_I_DismantleReroll` · `Se_Star_I_DreamDustOnKillChance` · `Se_Star_I_ExtraChaosOptionGoldOnUse` · `Se_Star_I_FirstBossGemDrop` · `Se_Star_I_FirstGemUpgrade` · `Se_Star_I_GemOnMiniBossKill` · `Se_Star_I_GoldPerCrit` · `Se_Star_I_GoldRiskAndReturn` · `Se_Star_I_KillGoldBonus` · `Se_Star_I_MawDiscountAndProtection` · `Se_Star_I_MoreShopItems` · `Se_Star_I_MoreShrineItems` · `Se_Star_I_ShopDiscount` · `Se_Star_I_StartGold` · `Se_Star_I_StartSkill` · `Se_Star_L_Armor` · `Se_Star_L_DamageReductionFromChilled` · `Se_Star_L_DodgeCooldown` · `Se_Star_L_DodgeCooldownOnLowHealth` · `Se_Star_L_ElementalResistance` · `Se_Star_L_FatalHitProtection` · `Se_Star_L_GuidanceShrineDiscount` · `Se_Star_L_HealOnAttack` · `Se_Star_L_HealOnKill` · `Se_Star_L_IgnoreDelusion` · `Se_Star_L_IncreaseMaxHealthByGuidance` · `Se_Star_L_MaxHealth` · `Se_Star_L_MaxHealthUpHealDown` · `Se_Star_L_PeriodicScalingArmor` · `Se_Star_L_PostHitDamageImmune` · `Se_Star_L_PotionChance` · `Se_Star_L_PotionHealAmount` · `Se_Star_L_PotionOnBuyOrSell` · `Se_Star_L_ReceivedHealingAndShieldBonus` · `Se_Star_L_ScalingMaxHealth` · `Se_Star_L_TempArmor` · `Se_Star_Lacerta_D_AbilityPower` · `Se_Star_Lacerta_D_AttackDamage` · `Se_Star_Lacerta_D_AttackRange` · `Se_Star_Lacerta_D_AttackSpeed` · `Se_Star_Lacerta_F_HC_KnockbackAndSlow` · `Se_Star_Lacerta_F_HC_NearDamage` · `Se_Star_Lacerta_F_HC_NoDelayDoubleCast` · `Se_Star_Lacerta_F_HC_ResetOnDodge` · `Se_Star_Lacerta_F_IR_AoEDamage` · `Se_Star_Lacerta_F_IR_MoreShots` · `Se_Star_Lacerta_F_IR_RechargeAmmoAmpBurnDamage` · `Se_Star_Lacerta_F_PS_ChargeSpeed` · `Se_Star_Lacerta_F_PS_CooldownReset` · `Se_Star_Lacerta_F_PS_SlowerStronger` · `Se_Star_Lacerta_F_QT_AddedCharges` · `Se_Star_Lacerta_F_QT_AttackEffect` · `Se_Star_Lacerta_F_QT_RapidFire` · `Se_Star_Lacerta_I_BonusFromStones` · `Se_Star_Lacerta_I_BossBounty` · `Se_Star_Lacerta_I_ShopDiscount` · `Se_Star_Lacerta_I_ShopMoreItemsWithPenalty` · `Se_Star_Lacerta_L_DodgeCharges` · `Se_Star_Lacerta_L_SpeedAfterDodge` · `Se_Star_Mist_D_AttackDamage` · `Se_Star_Mist_D_BonusOnDash` · `Se_Star_Mist_D_BossDamageOnHighHp` · `Se_Star_Mist_D_HunterDamage` · `Se_Star_Mist_D_ScalingAD` · `Se_Star_Mist_F_FL_DecreasedCooldownAndCharge` · `Se_Star_Mist_F_FL_Lightning` · `Se_Star_Mist_F_FL_MaxRangeExplosion` · `Se_Star_Mist_F_LG_ChainAttack` · `Se_Star_Mist_F_LG_IncreasedCooldownReduction` · `Se_Star_Mist_F_LG_RangeAndSpeed` · `Se_Star_Mist_F_LG_SingleTarget` · `Se_Star_Mist_F_PR_AllDirections` · `Se_Star_Mist_F_PR_PerfectParry` · `Se_Star_Mist_F_PR_ShieldAndCrit` · `Se_Star_Mist_F_UD_ExplosionDamage` · `Se_Star_Mist_F_UD_HealLostHealth` · `Se_Star_Mist_F_UD_NonUltimate` · `Se_Star_Mist_I_BonusOnCatPet` · `Se_Star_Mist_I_CamillasGift` · `Se_Star_Mist_I_StartGoldWithPenalty` · `Se_Star_Mist_L_AddedDodgeWithPenalty` · `Se_Star_Mist_L_ArmorWithPenalty` · `Se_Star_Mist_L_DodgeCooldownWithPenalty` · `Se_Star_Mist_L_MovSpeed` · `Se_Star_Mist_L_PotionShield` · `Se_Star_Nachia_D_AbilityPower` · `Se_Star_Nachia_D_CanineLover` · `Se_Star_Nachia_D_SkillHaste` · `Se_Star_Nachia_D_SummonAtkSpd` · `Se_Star_Nachia_F_MP_NachiaHeal` · `Se_Star_Nachia_F_MP_NoJump` · `Se_Star_Nachia_F_MP_StrongerFenrirNoCast` · `Se_Star_Nachia_F_NW_LessCooldownLessAtkSpd` · `Se_Star_Nachia_F_NW_MovSpeed` · `Se_Star_Nachia_F_NW_Teleport` · `Se_Star_Nachia_F_SB_DurationBonus` · `Se_Star_Nachia_F_SB_SecondWind` · `Se_Star_Nachia_F_SB_StrongerBuffNoSelf` · `Se_Star_Nachia_F_SC_AtkEffect` · `Se_Star_Nachia_F_SC_AtkSpd` · `Se_Star_Nachia_F_SC_MoreSummons` · `Se_Star_Nachia_F_SC_SummonDmgReduction` · `Se_Star_Nachia_I_ForestKillDreamDust` · `Se_Star_Nachia_I_ForestShopDiscount` · `Se_Star_Nachia_I_SummonKillGold` · `Se_Star_Nachia_L_AllyUnstoppable` · `Se_Star_Nachia_L_HealAndShieldAmp` · `Se_Star_Nachia_L_SelfWaltz` · `Se_Star_Nachia_L_SummonBonus` · `Se_Star_Nachia_L_WaltzArmor` · `Se_Star_Nachia_L_WaltzDurationWithPenalty` · `Se_Star_Vesper_D_ADWithNearbyBurning` · `Se_Star_Vesper_D_AtkSpd` · `Se_Star_Vesper_D_AtkSpdWithPenalty` · `Se_Star_Vesper_D_BossHunterAmpWithPenalty` · `Se_Star_Vesper_D_ConvertAPToAD` · `Se_Star_Vesper_F_BS_ADWithArmor` · `Se_Star_Vesper_F_BS_AddedDurationPerAtk` · `Se_Star_Vesper_F_BS_ExplosionOnEnd` · `Se_Star_Vesper_F_BS_MovSpd` · `Se_Star_Vesper_F_CS_ColdDamage` · `Se_Star_Vesper_F_CS_LingeringBenefits` · `Se_Star_Vesper_F_CS_UnlockMoveWithPenalty` · `Se_Star_Vesper_F_DP_FarTargetBonus` · `Se_Star_Vesper_F_DP_PointCast` · `Se_Star_Vesper_F_DP_SwitchToMelee` · `Se_Star_Vesper_F_SE_FullOffense` · `Se_Star_Vesper_F_SE_Invulnerability` · `Se_Star_Vesper_F_SE_PointCast` · `Se_Star_Vesper_I_ShopDiscount` · `Se_Star_Vesper_I_StartGold` · `Se_Star_Vesper_L_Armor` · `Se_Star_Vesper_L_EmpowerDodgeShield` · `Se_Star_Vesper_L_FireResistance` · `Se_Star_Vesper_L_Health` · `Se_Star_Vesper_L_ScalingArmor` · `Se_Star_Vesper_L_ScalingHealth` · `Se_Star_Vesper_L_SlowSpeedMoreHealth` · `Se_Star_Yubar_D_ADAPWithPenalty` · `Se_Star_Yubar_D_APOnDodge` · `Se_Star_Yubar_D_APPerLightSkill` · `Se_Star_Yubar_D_AbilityPower` · `Se_Star_Yubar_D_BonusDamageToLight` · `Se_Star_Yubar_D_ConvertADToAP` · `Se_Star_Yubar_D_ScalingAP` · `Se_Star_Yubar_D_SkillHaste` · `Se_Star_Yubar_F_CC_DamageOverTime` · `Se_Star_Yubar_F_CC_IncreaseAD` · `Se_Star_Yubar_F_CC_LongerDuration` · `Se_Star_Yubar_F_CC_MeteorPerLightSkill` · `Se_Star_Yubar_F_EI_AutoExplosion` · `Se_Star_Yubar_F_EI_BiggerExplosion` · `Se_Star_Yubar_F_EI_DashNoProjectile` · `Se_Star_Yubar_F_EI_NoRootMoreDamage` · `Se_Star_Yubar_F_SN_Artillery` · `Se_Star_Yubar_F_SN_AutoExplosion` · `Se_Star_Yubar_F_SN_DodgeReset` · `Se_Star_Yubar_F_SN_PullEnemy` · `Se_Star_Yubar_F_TQ_EssenceCooldown` · `Se_Star_Yubar_F_TQ_LowerCooldownNoInvul` · `Se_Star_Yubar_F_TQ_ReducedCooldownAndDuration` · `Se_Star_Yubar_I_DisintegrateDreamDust` · `Se_Star_Yubar_I_MoreDreamDustWithPenalty` · `Se_Star_Yubar_I_StarCookie` · `Se_Star_Yubar_L_DodgeChargeWithLongerCooldown` · `Se_Star_Yubar_L_DodgeCooldownWithShorterRange` · `Se_Star_Yubar_L_DodgeRange` · `UI_Lobby_Constellations` · `UI_Lobby_Constellations_HeroConstellation_StarSlot` · `UI_Lobby_Constellations_StarDetails` · `UI_Lobby_Constellations_StarItem` · `UI_Lobby_Constellations_StarList` · `UI_StarIcon` · `UI_Tooltip_SkillStarDescriber` · `UI_Tooltip_SkillStarDescriber_Item` · `UI_Tooltip_StatusEffectDescription`

### Dependencies (12)

*Types and components that `StarEffect` references or depends upon:*

[AbilityInstance](/api/Global.AbilityInstance) · [Actor](/api/Global.Actor) · [DewPlayer](/api/Global.DewPlayer) · [Entity](/api/Global.Entity) · [EntityAbility](/api/Global.EntityAbility) · [Hero](/api/Global.Hero) · [HeroLoadoutData](/api/Global.HeroLoadoutData) · [HeroSkill](/api/Global.HeroSkill) · [SafeAction](/api/Global.SafeAction) · [SkillBonus](/api/Global.SkillBonus) · [SkillTrigger](/api/Global.SkillTrigger) · [StatusEffect](/api/Global.StatusEffect)

### Related Enums (3)

*Enumerations referenced in fields, properties, or method signatures:*

[`SaveVarFlags`](/enums#savevarflags) · [`SkillType`](/enums#skilltype) · [`StarType`](/enums#startype)

:::
