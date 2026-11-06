# Struct: StarScalingValue

- **Category:** <span class="cat-dot" style="--cat-color: #f97316" data-cat="Data & Core Math"></span> Data & Core Math
- **Namespace:** `Global`
- **Assembly:** `Dew.Core.dll`

```csharp
[Serializable]
[InlineProperty]
[LabelWidth(100)]
public struct StarScalingValue
```

## Fields (15)

::: details Click to expand Fields (15)

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`clampMax`** | `[ShowIf("@isClamped", true)] [HideLabel] [HorizontalGroup("C", 0, 0, 0, 0)] public float clampMax` |  |
| **`clampMin`** | `[ShowIf("@isClamped", true)] [HideLabel] [SuffixLabel("-", false)] [HorizontalGroup("C", 0, 0, 0, 0)] public float clampMin` |  |
| **`isClamped`** | `[ToggleLeft] [HorizontalGroup("C", 0, 0, 0, 0)] [LabelText("Clamp")] public bool isClamped` |  |
| **`isInteger`** | `[ToggleLeft] [HorizontalGroup("B", 40, 0, 0, 0)] [LabelText("Int")] public bool isInteger` |  |
| **`isParentStarEffect`** | `[HideInInspector] [HideInInspector] public bool isParentStarEffect` |  |
| **`levels`** | `[HideInInspector] [HideInInspector] public int levels` |  |
| **`strengthScaling`** | `[HideLabel] [HorizontalGroup("B", 0, 0, 0, 0)] public StarScalingValue.StrengthScalingType strengthScaling` |  |
| **`v0`** | `[HorizontalGroup("A", 0, 0, 0, 0)] [HideLabel] public float v0` |  |
| **`v1`** | `[HorizontalGroup("A", 0, 0, 0, 0)] [HideLabel] [ShowIf("@!isParentStarEffect \|\| levels >= 2", true)] public float v1` |  |
| **`v2`** | `[HorizontalGroup("A", 0, 0, 0, 0)] [HideLabel] [ShowIf("@!isParentStarEffect \|\| levels >= 3", true)] public float v2` |  |
| **`v3`** | `[HorizontalGroup("A", 0, 0, 0, 0)] [HideLabel] [ShowIf("@!isParentStarEffect \|\| levels >= 4", true)] public float v3` |  |
| **`v4`** | `[HorizontalGroup("A", 0, 0, 0, 0)] [HideLabel] [ShowIf("@!isParentStarEffect \|\| levels >= 5", true)] public float v4` |  |
| **`v5`** | `[HorizontalGroup("A", 0, 0, 0, 0)] [HideLabel] [ShowIf("@!isParentStarEffect \|\| levels >= 6", true)] public float v5` |  |
| **`v6`** | `[HorizontalGroup("A", 0, 0, 0, 0)] [HideLabel] [ShowIf("@!isParentStarEffect \|\| levels >= 7", true)] public float v6` |  |
| **`v7`** | `[HorizontalGroup("A", 0, 0, 0, 0)] [HideLabel] [ShowIf("@!isParentStarEffect \|\| levels >= 8", true)] public float v7` |  |

:::

## Methods (3)

::: details `Get(int)`

```csharp
public float Get(int index)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `index` | `int` |  |

**Returns:** `float`

:::

::: details `GetValue(int, float)`

```csharp
public float GetValue(int level, float strength)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `level` | `int` |  |
| `strength` | `float` |  |

**Returns:** `float`

:::

::: details `Set(int, float)`

```csharp
public void Set(int index, float value)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `index` | `int` |  |
| `value` | `float` |  |

:::


## Architecture & Relationships

::: details Click to expand Architecture & Relationships

### Used By (188)

*Classes and systems that invoke, reference, or depend on `StarScalingValue`:*

[AbilityInstance](/api/Global.AbilityInstance) · `RevealNodesStarEffect` · `Se_Star_Aurena_D_AbilityPower` · `Se_Star_Aurena_D_AtkSpd` · `Se_Star_Aurena_D_AttackDamage` · `Se_Star_Aurena_D_BonusStatOnLowHp` · `Se_Star_Aurena_I_BonusFromStones` · `Se_Star_Aurena_I_GoldEveryZone` · `Se_Star_Aurena_I_GoldOnMerchantDamage` · `Se_Star_Aurena_I_PotionGold` · `Se_Star_Aurena_L_Armor` · `Se_Star_Aurena_L_ArmorOnLowHp` · `Se_Star_Aurena_L_HealAmpOnLowHp` · `Se_Star_Aurena_L_HealAmpWithPenalty` · `Se_Star_Aurena_L_ShareHeal` · `Se_Star_Aurena_L_SpeedOnDamage` · `Se_Star_Bismuth_D_AtkSpd` · `Se_Star_Bismuth_D_AtkSpdFromDismantle` · `Se_Star_Bismuth_D_BonusAttackEffect` · `Se_Star_Bismuth_D_Conquerer` · `Se_Star_Bismuth_D_SkillHasteAndAutoCast` · `Se_Star_Bismuth_I_DismantleMemoryDreamDust` · `Se_Star_Bismuth_I_KnowledgeBook` · `Se_Star_Bismuth_I_SecretJournal` · `Se_Star_Bismuth_I_ShopDiscount` · `Se_Star_Bismuth_I_TreasureWithHealthPenalty` · `Se_Star_Bismuth_L_ContinuousSpeed` · `Se_Star_Bismuth_L_DodgeNoDashMoreCharges` · `Se_Star_Bismuth_L_SecondWindWithPenalty` · `Se_Star_Cetus_D_AdApUpByBonusHp` · `Se_Star_Cetus_D_ApUpByColdSkillCounts` · `Se_Star_Cetus_D_StackStatsOnTakenDamage` · `Se_Star_Cetus_D_StatsUpWhileShielded` · `Se_Star_Cetus_I_ColdDiscountFireSurcharge` · `Se_Star_Cetus_I_ColdSkillOnEnterWorld` · `Se_Star_Cetus_I_FirstColdGemQualityBoost` · `Se_Star_Cetus_I_GetDreamDustOnBossKill` · `Se_Star_Cetus_I_StartWithResources` · `Se_Star_Cetus_L_ArmorBuffOnShield` · `Se_Star_Cetus_L_DodgeCdReductionOnHit` · `Se_Star_Cetus_L_FrostResistAndBuff` · `Se_Star_Cetus_L_HealOnApDamage` · `Se_Star_Cetus_L_IncreaseDealtShield` · `Se_Star_Cetus_L_MaxHpDamagePenalty` · `Se_Star_Cetus_L_ScalingHealth` · `Se_Star_D_AbilityPower` · `Se_Star_D_AttackDamage` · `Se_Star_D_AttackSpeed` · `Se_Star_D_BossDamageAmp` · `Se_Star_D_CritChance` · `Se_Star_D_CritDamage` · `Se_Star_D_CritUpHitDecay` · `Se_Star_D_DamageBonusOnAllElemental` · `Se_Star_D_DarkAmp` · `Se_Star_D_FireAmp` · `Se_Star_D_LightAmp` · `Se_Star_D_LowerADScalingAP` · `Se_Star_D_LowerAPScalingAD` · `Se_Star_D_LowerASHigherAD` · `Se_Star_D_RiftFirstCastDamageUp` · `Se_Star_D_ScalingAbilityPower` · `Se_Star_D_ScalingAttackDamage` · `Se_Star_D_ScalingAttackSpeedWithPenalty` · `Se_Star_D_ShieldDamageAmp` · `Se_Star_D_TempAbilityPower` · `Se_Star_D_TempAttackDamage` · `Se_Star_D_UltimateChargeSpeed` · `Se_Star_Husk_D_AttackDamage` · `Se_Star_Husk_D_CritAmp` · `Se_Star_Husk_D_DamageAmpOnLowHpTarget` · `Se_Star_Husk_D_DamageOverTimeCritWithPenalty` · `Se_Star_Husk_D_DarkAttackWithPenalty` · `Se_Star_Husk_D_MovementSkillHaste` · `Se_Star_Husk_D_ScalingAdAndAtkSpd` · `Se_Star_Husk_I_BossKillPlatinumCoin` · `Se_Star_Husk_I_ShopIntimidation` · `Se_Star_Husk_L_DodgeChargesAndRangeWithPenalty` · `Se_Star_Husk_L_DodgeCooldownOnKillOrAttack` · `Se_Star_Husk_L_DodgeCooldownOnKillWithEmptyCharges` · `Se_Star_Husk_L_FatalHitProtectionWithPenalty` · `Se_Star_I_AdditionalChaosChance` · `Se_Star_I_DismantleBonus` · `Se_Star_I_DismantleDustToBonusGold` · `Se_Star_I_DismantleReroll` · `Se_Star_I_DreamDustOnKillChance` · `Se_Star_I_ExtraChaosOptionGoldOnUse` · `Se_Star_I_FirstBossGemDrop` · `Se_Star_I_FirstGemUpgrade` · `Se_Star_I_GemOnMiniBossKill` · `Se_Star_I_GoldPerCrit` · `Se_Star_I_GoldRiskAndReturn` · `Se_Star_I_KillGoldBonus` · `Se_Star_I_MawDiscountAndProtection` · `Se_Star_I_MoreShopItems` · `Se_Star_I_MoreShrineItems` · `Se_Star_I_ShopDiscount` · `Se_Star_I_ShopRefreshToken` · `Se_Star_I_StartGold` · `Se_Star_I_StartSkill` · `Se_Star_L_Armor` · `Se_Star_L_ArmorOnTravel` · `Se_Star_L_DamageReductionFromChilled` · `Se_Star_L_DodgeCooldown` · `Se_Star_L_DodgeCooldownOnLowHealth` · `Se_Star_L_ElementalResistance` · `Se_Star_L_FatalHitProtection` · `Se_Star_L_GuidanceShrineDiscount` · `Se_Star_L_HealOnAttack` · `Se_Star_L_HealOnKill` · `Se_Star_L_IgnoreDelusion` · `Se_Star_L_IncreaseMaxHealthByGuidance` · `Se_Star_L_MaxHealth` · `Se_Star_L_MaxHealthUpHealDown` · `Se_Star_L_PeriodicScalingArmor` · `Se_Star_L_PostHitDamageImmune` · `Se_Star_L_PotionChance` · `Se_Star_L_PotionHealAmount` · `Se_Star_L_PotionOnBuyOrSell` · `Se_Star_L_ReceivedHealingAndShieldBonus` · `Se_Star_L_ScalingMaxHealth` · `Se_Star_L_TempArmor` · `Se_Star_Lacerta_D_AbilityPower` · `Se_Star_Lacerta_D_AttackDamage` · `Se_Star_Lacerta_D_AttackRange` · `Se_Star_Lacerta_D_AttackSpeed` · `Se_Star_Lacerta_F_IR_RechargeAmmoAmpBurnDamage` · `Se_Star_Lacerta_I_BonusFromStones` · `Se_Star_Lacerta_I_BossBounty` · `Se_Star_Lacerta_I_ShopDiscount` · `Se_Star_Lacerta_I_ShopMoreItemsWithPenalty` · `Se_Star_Lacerta_L_DodgeCharges` · `Se_Star_Lacerta_L_SpeedAfterDodge` · `Se_Star_Mist_D_AttackDamage` · `Se_Star_Mist_D_BonusOnDash` · `Se_Star_Mist_D_BossDamageOnHighHp` · `Se_Star_Mist_D_HunterDamage` · `Se_Star_Mist_D_ScalingAD` · `Se_Star_Mist_I_BonusOnCatPet` · `Se_Star_Mist_I_CamillasGift` · `Se_Star_Mist_I_StartGoldWithPenalty` · `Se_Star_Mist_L_AddedDodgeWithPenalty` · `Se_Star_Mist_L_ArmorWithPenalty` · `Se_Star_Mist_L_DodgeCooldownWithPenalty` · `Se_Star_Mist_L_MovSpeed` · `Se_Star_Mist_L_PotionShield` · `Se_Star_Nachia_D_AbilityPower` · `Se_Star_Nachia_D_CanineLover` · `Se_Star_Nachia_D_SkillHaste` · `Se_Star_Nachia_D_SummonAtkSpd` · `Se_Star_Nachia_I_ForestKillDreamDust` · `Se_Star_Nachia_I_ForestShopDiscount` · `Se_Star_Nachia_I_ForestStartDreamDust` · `Se_Star_Nachia_I_SummonKillGold` · `Se_Star_Nachia_L_AllyUnstoppable` · `Se_Star_Nachia_L_HealAndShieldAmp` · `Se_Star_Nachia_L_SelfWaltz` · `Se_Star_Nachia_L_SummonBonus` · `Se_Star_Nachia_L_WaltzArmor` · `Se_Star_Nachia_L_WaltzDurationWithPenalty` · `Se_Star_Vesper_D_ADWithNearbyBurning` · `Se_Star_Vesper_D_AtkSpd` · `Se_Star_Vesper_D_AtkSpdWithPenalty` · `Se_Star_Vesper_D_BossHunterAmpWithPenalty` · `Se_Star_Vesper_D_ConvertAPToAD` · `Se_Star_Vesper_I_ShopDiscount` · `Se_Star_Vesper_I_StartGold` · `Se_Star_Vesper_L_Armor` · `Se_Star_Vesper_L_ArmorOnLowHealth` · `Se_Star_Vesper_L_EmpowerDodgeShield` · `Se_Star_Vesper_L_FireResistance` · `Se_Star_Vesper_L_Health` · `Se_Star_Vesper_L_ScalingArmor` · `Se_Star_Vesper_L_ScalingHealth` · `Se_Star_Vesper_L_SlowSpeedMoreHealth` · `Se_Star_Yubar_D_ADAPWithPenalty` · `Se_Star_Yubar_D_APOnDodge_APBonus` · `Se_Star_Yubar_D_APPerLightSkill` · `Se_Star_Yubar_D_AbilityPower` · `Se_Star_Yubar_D_BonusDamageToLight` · `Se_Star_Yubar_D_ConvertADToAP` · `Se_Star_Yubar_D_ScalingAP` · `Se_Star_Yubar_D_SkillHaste` · `Se_Star_Yubar_I_DisintegrateDreamDust` · `Se_Star_Yubar_I_MoreDreamDustWithPenalty` · `Se_Star_Yubar_I_StarCookie` · `Se_Star_Yubar_L_DodgeChargeWithLongerCooldown` · `Se_Star_Yubar_L_DodgeCooldownWithShorterRange` · `Se_Star_Yubar_L_DodgeRange`

### Dependencies (0)

*No outgoing class dependencies recorded.*

:::
