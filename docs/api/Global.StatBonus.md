# Class: StatBonus

- **Category:** <span class="cat-dot" style="--cat-color: #ef4444" data-cat="Combat & Abilities"></span> Combat & Abilities
- **Namespace:** `Global`
- **Assembly:** `Dew.Core.dll`

```csharp
[Serializable]
public class StatBonus
```

## Properties (31)

::: details Click to expand Properties (31)

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`abilityHasteFlat`** | `public float abilityHasteFlat { get; set; }` |  |
| **`abilityHastePercentage`** | `public float abilityHastePercentage { get; set; }` |  |
| **`abilityPowerFlat`** | `public float abilityPowerFlat { get; set; }` |  |
| **`abilityPowerPercentage`** | `public float abilityPowerPercentage { get; set; }` |  |
| **`armorFlat`** | `public float armorFlat { get; set; }` |  |
| **`armorPercentage`** | `public float armorPercentage { get; set; }` |  |
| **`attackDamageFlat`** | `public float attackDamageFlat { get; set; }` |  |
| **`attackDamagePercentage`** | `public float attackDamagePercentage { get; set; }` |  |
| **`attackRangeFlat`** | `public float attackRangeFlat { get; set; }` |  |
| **`attackRangePercentage`** | `public float attackRangePercentage { get; set; }` |  |
| **`attackSpeedPercentage`** | `public float attackSpeedPercentage { get; set; }` |  |
| **`coldEffectAmpFlat`** | `public float coldEffectAmpFlat { get; set; }` |  |
| **`critAmpFlat`** | `public float critAmpFlat { get; set; }` |  |
| **`critAmpPercentage`** | `public float critAmpPercentage { get; set; }` |  |
| **`critChanceFlat`** | `public float critChanceFlat { get; set; }` |  |
| **`critChancePercentage`** | `public float critChancePercentage { get; set; }` |  |
| **`darkEffectAmpFlat`** | `public float darkEffectAmpFlat { get; set; }` |  |
| **`everyFourAttackStartIndexFlat`** | `public int everyFourAttackStartIndexFlat { get; set; }` |  |
| **`fireEffectAmpFlat`** | `public float fireEffectAmpFlat { get; set; }` |  |
| **`healthRegenFlat`** | `public float healthRegenFlat { get; set; }` |  |
| **`healthRegenPercentage`** | `public float healthRegenPercentage { get; set; }` |  |
| **`lightEffectAmpFlat`** | `public float lightEffectAmpFlat { get; set; }` |  |
| **`manaRegenFlat`** | `public float manaRegenFlat { get; set; }` |  |
| **`manaRegenPercentage`** | `public float manaRegenPercentage { get; set; }` |  |
| **`maxHealthFlat`** | `public float maxHealthFlat { get; set; }` |  |
| **`maxHealthPercentage`** | `public float maxHealthPercentage { get; set; }` |  |
| **`maxManaFlat`** | `public float maxManaFlat { get; set; }` |  |
| **`maxManaPercentage`** | `public float maxManaPercentage { get; set; }` |  |
| **`movementSpeedPercentage`** | `public float movementSpeedPercentage { get; set; }` |  |
| **`tenacityFlat`** | `public float tenacityFlat { get; set; }` |  |
| **`tenacityPercentage`** | `public float tenacityPercentage { get; set; }` |  |

:::

## Methods (3)

::: details `Add(StatBonus)`

```csharp
public void Add(StatBonus bonus)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `bonus` | [`StatBonus`](/api/Global.StatBonus) |  |

:::

::: details `Clone()`

```csharp
public StatBonus Clone()
```

**Returns:** `StatBonus`

:::

::: details `Multiply(float)`

Multiplies all stat bonuses by the given multiplier. Useful for scaling bonuses based on level, rarity, or other factors.

```csharp
public void Multiply(float multiplier)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `multiplier` | `float` | The value to multiply all stat bonuses by |

:::


## Architecture & Relationships

::: details Click to expand Architecture & Relationships

### Used By (191)

*Classes and systems that invoke, reference, or depend on `StatBonus`:*

`Ai_Gem_E_Predation_Pickup` · `Ai_Mon_Special_AmbushSpawner_Projectile` · [BonusStats](/api/Global.BonusStats) · [DewDifficultySettings](/api/Global.DewDifficultySettings) · `DewStarItemOld` · [EntityStatus](/api/Global.EntityStatus) · [GameMod_Limbo](/api/Global.GameMod_Limbo) · [Gem](/api/Global.Gem) · `Gem_C_Sulfur` · `Gem_E_Domination` · `Gem_E_Might` · `Gem_E_OurStory_Completed` · `Gem_E_Predation` · `Gem_L_DivineFaith` · `Gem_L_MetalCrystal` · `Gem_L_Perfect` · `Gem_R_Crucible` · [ISpawnableAsMiniBoss](/api/Global.ISpawnableAsMiniBoss) · `LucidDream_MarshOfDestiny` · `LucidDream_TheDarkestUrge` · [MirageSkinEffect](/api/Global.MirageSkinEffect) · `Mon_DarkCave_CaveSpider` · `Mon_Despair_Displacer` · `Mon_Despair_DreadBug` · `Mon_Despair_WretchedArtillery` · `Mon_Forest_SpiderSpitter` · `Mon_Ink_Archer` · `Mon_Ink_DivineAnimal` · `Mon_Ink_GhostBlade` · `Mon_Ink_GhostSpear` · `Mon_LavaLand_FireElemental` · `Mon_LavaLand_InfernoSpider` · `Mon_LavaLand_SuperheatedWolf` · `Mon_Sky_StarSeed` · `Mon_Special_BossErebos` · [Monster](/api/Global.Monster) · [PersistentStatBonusEffect](/api/Global.PersistentStatBonusEffect) · [PlayGameManager](/api/Global.PlayGameManager) · `RoomMod_Hunted` · `RoomMod_LeafPuppies` · `RoomMod_MeteoricLife` · `Se_AcceleratedTime` · `Se_Curse_BrainFog` · `Se_Curse_DreamAfflictionHallucinatory` · `Se_Curse_GuidingCompass_CripplingAnxiety` · `Se_D_ChargedAnguillian` · `Se_D_CircleOfLife_Summon` · `Se_D_ConvergencePoint` · `Se_D_DoubleTap` · `Se_D_IceColdPresence_PersistentBuff` · `Se_D_MercyOfEl` · `Se_D_ParryMaster_Buff` · `Se_D_QuartetOfDeath_Buff` · `Se_D_Resolve` · `Se_E_Permafrost_Shield` · `Se_E_UmbralEdge` · `Se_FallenStar_MonsterReinforcement` · `Se_FishScales` · `Se_Gem_E_Insight_Buff` · `Se_Gem_L_Liberty_Buff` · `Se_Gem_R_Epiphany_ApBuff` · `Se_Gem_R_Frost_Stat` · `Se_Gem_R_Insatiable` · `Se_GoldEverywhere` · `Se_HarmlessWhispers` · `Se_HunterBuff` · `Se_MiniBoss_BloodThorn` · `Se_MiniBoss_IceAura_Slow` · `Se_MiniBoss_UnstableExplosive` · `Se_Mon_Ink_BossWhiteNight_Cataclysm` · `Se_Mon_Ink_Boss_Rage` · `Se_Mon_Primus_BossPrimusAeron_Adaptation` · `Se_Mon_Primus_BossPrimusAeron_Rage_DecayingShield` · `Se_Mon_Special_BossMaw_Cataclysm` · `Se_Mon_Special_BossPolaris_Adaptation` · `Se_Pickup_AbilityPower` · `Se_Pickup_AttackDamage` · `Se_Pickup_SkillHaste` · `Se_PureDream` · `Se_R_AnnihilationStance` · `Se_R_Cataclysm` · `Se_R_Composure_Buff` · `Se_R_Somersault_CritBonus` · `Se_R_UnbreakableDetermination` · `Se_RoomMod_Symbiote` · `Se_Shrine_Chaos_StatBonus` · `Se_Star_Aurena_D_AbilityPower` · `Se_Star_Aurena_D_AtkSpd` · `Se_Star_Aurena_D_AttackDamage` · `Se_Star_Aurena_D_BonusStatOnLowHp` · `Se_Star_Aurena_L_Armor` · `Se_Star_Aurena_L_ArmorOnLowHp` · `Se_Star_Bismuth_D_AtkSpd` · `Se_Star_Bismuth_D_AtkSpdFromDismantle` · `Se_Star_Bismuth_D_BonusAttackEffect` · `Se_Star_Bismuth_D_Conquerer_Stacks` · `Se_Star_Bismuth_D_SkillHasteAndAutoCast` · `Se_Star_Bismuth_I_TreasureWithHealthPenalty` · `Se_Star_Cetus_D_ApUpByColdSkillCounts` · `Se_Star_Cetus_D_StackStatsOnTakenDamage` · `Se_Star_Cetus_D_StatsUpWhileShielded` · `Se_Star_Cetus_L_FrostResistAndBuff` · `Se_Star_Cetus_L_MaxHpDamagePenalty` · `Se_Star_Cetus_L_ScalingHealth` · `Se_Star_D_AbilityPower` · `Se_Star_D_AttackDamage` · `Se_Star_D_AttackSpeed` · `Se_Star_D_CritChance` · `Se_Star_D_CritDamage` · `Se_Star_D_CritUpHitDecay` · `Se_Star_D_DarkAmp` · `Se_Star_D_FireAmp` · `Se_Star_D_LightAmp` · `Se_Star_D_LowerADScalingAP` · `Se_Star_D_LowerAPScalingAD` · `Se_Star_D_LowerASHigherAD` · `Se_Star_D_ScalingAbilityPower` · `Se_Star_D_ScalingAttackDamage` · `Se_Star_D_ScalingAttackSpeedWithPenalty` · `Se_Star_D_TempAbilityPower` · `Se_Star_D_TempAttackDamage` · `Se_Star_Husk_D_AttackDamage` · `Se_Star_Husk_D_CritAmp` · `Se_Star_Husk_D_DarkAttackWithPenalty` · `Se_Star_Husk_D_ScalingAdAndAtkSpd` · `Se_Star_L_ArmorOnTravel` · `Se_Star_L_IncreaseMaxHealthByGuidance` · `Se_Star_L_MaxHealth` · `Se_Star_L_MaxHealthUpHealDown` · `Se_Star_L_PeriodicScalingArmor` · `Se_Star_L_ScalingMaxHealth` · `Se_Star_L_TempArmor` · `Se_Star_Lacerta_D_AbilityPower` · `Se_Star_Lacerta_D_AttackDamage` · `Se_Star_Lacerta_D_AttackSpeed` · `Se_Star_Mist_D_AttackDamage` · `Se_Star_Mist_D_BonusOnDash` · `Se_Star_Mist_D_ScalingAD` · `Se_Star_Mist_L_MovSpeed` · `Se_Star_Nachia_D_AbilityPower` · `Se_Star_Nachia_D_SkillHaste` · `Se_Star_Nachia_F_SC_SummonDmgReduction` · `Se_Star_Vesper_D_ADWithNearbyBurning` · `Se_Star_Vesper_D_AtkSpd` · `Se_Star_Vesper_D_AtkSpdWithPenalty` · `Se_Star_Vesper_D_BossHunterAmpWithPenalty` · `Se_Star_Vesper_F_BS_ADWithArmor` · `Se_Star_Vesper_F_DP_FarTargetBonus` · `Se_Star_Vesper_F_SE_FullOffense` · `Se_Star_Vesper_L_Armor` · `Se_Star_Vesper_L_ArmorOnLowHealth` · `Se_Star_Vesper_L_Health` · `Se_Star_Vesper_L_ScalingArmor` · `Se_Star_Vesper_L_ScalingHealth` · `Se_Star_Vesper_L_SlowSpeedMoreHealth` · `Se_Star_Yubar_D_ADAPWithPenalty` · `Se_Star_Yubar_D_APOnDodge_APBonus` · `Se_Star_Yubar_D_APPerLightSkill` · `Se_Star_Yubar_D_AbilityPower` · `Se_Star_Yubar_D_ScalingAP` · `Se_Star_Yubar_D_SkillHaste` · `Se_Star_Yubar_I_MoreDreamDustWithPenalty` · `Se_Treasure_BlueElixir_ApBoost` · `Se_Treasure_CrimsonElixir_AdBoost` · `Shrine_Chaos` · `Shrine_CorruptedChaos` · `Shrine_MarshOfDestiny_SeedOfTorment` · `Shrine_Se_Star_Bismuth_I_KnowledgeBook_Book` · [SkillTrigger](/api/Global.SkillTrigger) · `St_D_SalamanderPowder` · `St_D_ThirstOfVengence` · `St_L_HerosReturn` · `Star_Global_AbilityPower` · `Star_Global_AttackDamage` · `Star_Global_AttackSpeed` · `Star_Global_DarkAmp` · `Star_Global_FireAmp` · `Star_Global_LightAmp` · `Star_Global_MaxHealth` · `Star_Global_SkillHaste` · `Star_Global_Tenacity` · `Star_Lacerta_AttackSpeed` · `Star_Lacerta_FireAmp` · `Star_Mist_AddAttackDamage` · `Star_Mist_MovementSpeed` · `Star_Vesper_MaxHealth` · `Star_Yubar_AbilityPower` · `Star_Yubar_SkillHaste` · [StatusEffect](/api/Global.StatusEffect) · [Summon](/api/Global.Summon) · `Mirror.GeneratedNetworkCode`

### Dependencies (1)

*Types and components that `StatBonus` references or depends upon:*

[BonusStats](/api/Global.BonusStats)

:::
