# Struct: ScalingValue

- **Category:** <span class="cat-dot" style="--cat-color: #ef4444" data-cat="Combat & Abilities"></span> Combat & Abilities
- **Namespace:** `Global`
- **Assembly:** `Dew.Core.dll`

```csharp
[Serializable]
public struct ScalingValue
```

## Fields (12)

::: details Click to expand Fields (12)

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`addedHpFactor`** | `public float addedHpFactor` |  |
| **`adFactor`** | `public float adFactor` |  |
| **`apFactor`** | `public float apFactor` |  |
| **`armorFactor`** | `public float armorFactor` |  |
| **`baseValue`** | `public float baseValue` |  |
| **`critPercentageFactor`** | `public float critPercentageFactor` |  |
| **`GemDefaultPerLevelMultiplier`** | `public const float GemDefaultPerLevelMultiplier = 1.01` |  |
| **`leveling`** | `public LevelScaling leveling` |  |
| **`levelOverride`** | `public static int? levelOverride` |  |
| **`lvlFactor`** | `public float lvlFactor` |  |
| **`scalingMultiplier`** | `public float scalingMultiplier` |  |
| **`SkillDefaultPerLevelMultiplier`** | `public const float SkillDefaultPerLevelMultiplier = 1.25` |  |

:::

## Properties (1)

::: details Click to expand Properties (1)

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`valueString`** | `[JsonProperty] [JsonProperty] public string valueString { get; set; }` |  |

:::

## Methods (10)

::: details `EditorParse(string, ref float, ref float, ref float, ref float, ref float, ref float, ref float)`

```csharp
public static void EditorParse(string input, ref float baseVal, ref float ad, ref float ap, ref float lvl, ref float arm, ref float ahp, ref float critp)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `input` | `string` |  |
| `baseVal` | `float` |  |
| `ad` | `float` |  |
| `ap` | `float` |  |
| `lvl` | `float` |  |
| `arm` | `float` |  |
| `ahp` | `float` |  |
| `critp` | `float` |  |

:::

::: details `EditorToString(float, float, float, float, float, float, float)`

```csharp
public static string EditorToString(float baseVal, float ad, float ap, float lvl, float arm, float ahp, float critp)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `baseVal` | `float` |  |
| `ad` | `float` |  |
| `ap` | `float` |  |
| `lvl` | `float` |  |
| `arm` | `float` |  |
| `ahp` | `float` |  |
| `critp` | `float` |  |

**Returns:** `string`

:::

::: details `GetAddedScalingMultiplierPerLevel()`

```csharp
public float GetAddedScalingMultiplierPerLevel()
```

**Returns:** `float`

:::

::: details `GetScalingMultiplier(int)`

```csharp
public float GetScalingMultiplier(int level)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `level` | `int` |  |

**Returns:** `float`

:::

::: details `GetValue(int, Entity)`

```csharp
public float GetValue(int level, Entity self)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `level` | `int` |  |
| `self` | [`Entity`](/api/Global.Entity) |  |

**Returns:** `float`

:::

::: details `GetValue(int, float, float, float, float, float)`

```csharp
public float GetValue(int level, float attackDamage, float abilityPower, float armor, float addedHp, float critChance)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `level` | `int` |  |
| `attackDamage` | `float` |  |
| `abilityPower` | `float` |  |
| `armor` | `float` |  |
| `addedHp` | `float` |  |
| `critChance` | `float` |  |

**Returns:** `float`

:::

::: details `Lerp(ScalingValue, ScalingValue, float)`

```csharp
public static ScalingValue Lerp(ScalingValue a, ScalingValue b, float t)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `a` | [`ScalingValue`](/api/Global.ScalingValue) |  |
| `b` | [`ScalingValue`](/api/Global.ScalingValue) |  |
| `t` | `float` |  |

**Returns:** `ScalingValue`

:::

::: details `OnAfterDeserialize()`

```csharp
public void OnAfterDeserialize()
```

:::

::: details `OnBeforeSerialize()`

```csharp
public void OnBeforeSerialize()
```

:::

::: details `ToString()`

```csharp
public override string ToString()
```

**Returns:** `string`

:::


## Architecture & Relationships

::: details Click to expand Architecture & Relationships

### Used By (478)

*Classes and systems that invoke, reference, or depend on `ScalingValue`:*

[AbilityInstance](/api/Global.AbilityInstance) · `Ai_C_BackStep` · `Ai_C_BackStep_Bomb` · `Ai_C_BeamOfLight` · `Ai_C_DarkBolt` · `Ai_C_DarkSpear` · `Ai_C_FlashFreeze` · `Ai_C_GlacialStomp` · `Ai_C_IceBolt` · `Ai_C_LuckyHammer` · `Ai_C_MagicSword` · `Ai_C_MassProtection` · `Ai_C_Pew_Projectile` · `Ai_C_PressurePoint` · `Ai_C_Purgatory` · `Ai_C_Purgatory_Heal` · `Ai_C_SparklingWaterGun` · `Ai_C_SpearThrow` · `Ai_C_Starfall` · `Ai_C_Starfall_Projectile` · `Ai_D_BeautifulThreat_Feather` · `Ai_D_BurningFist_Attack` · `Ai_D_BurningFist_Attack_Instance` · `Ai_D_ChargedAnguillian_Lightning` · `Ai_D_DanceOfValor_Projectile` · `Ai_D_ExoticMatter_Projectile` · `Ai_D_FrostTouch_FrostProjectile` · `Ai_D_IceColdPresence_AOE` · `Ai_D_IcyVeins_Damage` · `Ai_D_PrismaticEyes_Attack` · `Ai_D_QuartetOfDeath_Explosion` · `Ai_D_Resolve_Push` · `Ai_D_SalamanderPowder_Projectile` · `Ai_D_ScarOfTheWind_DashAtk` · `Ai_D_SharedPain_Instance` · `Ai_E_AntiGravity` · `Ai_E_Blink` · `Ai_E_ChainLightning` · `Ai_E_ClutchesOfMalice` · `Ai_E_ClutchesOfMalice_ReachAndPull` · `Ai_E_CrimsonLance` · `Ai_E_DoomsdayMeteor_SubProjectile` · `Ai_E_FinalExplosion_Explosion` · `Ai_E_FlameJet_Projectile` · `Ai_E_JusticeGuillotine` · `Ai_E_MassCleanse` · `Ai_E_MysticDagger` · `Ai_E_Permafrost` · `Ai_E_SearingCharge` · `Ai_E_ShadowVolley` · `Ai_E_ShadowVolley_Projectile` · `Ai_E_SliceThroat` · `Ai_E_StygianRush` · `Ai_E_StygianRush_Rush` · `Ai_E_WinterDive` · `Ai_Gem_C_Charcoal_Projectile` · `Ai_Gem_C_Sharp_Arrow` · `Ai_Gem_C_Vengence_Projectile` · `Ai_Gem_C_Void_Explosion` · `Ai_Gem_E_Crimson` · `Ai_Gem_E_Fangs_Projectile` · `Ai_Gem_E_Insight_Damage` · `Ai_Gem_E_Predation_Pickup` · `Ai_Gem_E_Thunder` · `Ai_Gem_L_Embertail_Projectile` · `Ai_Gem_L_PureWhite_Projectile` · `Ai_Gem_L_SolarEye` · `Ai_Gem_L_SuppressedArcanum` · `Ai_Gem_R_Accuracy_Projectile` · `Ai_Gem_R_Blade` · `Ai_Gem_R_Celestial` · `Ai_Gem_R_Dusk_Projectile` · `Ai_Gem_R_Glaciate` · `Ai_Gem_R_Ricochet` · `Ai_Gem_R_Shock_Lightning` · `Ai_Gem_R_Snow_Projectile` · `Ai_Gem_R_Spiral_Fireball` · `Ai_Gem_R_Stillness` · `Ai_Gem_U_LastStarlight` · `Ai_L_Blizzard` · `Ai_L_Blizzard_Instance` · `Ai_L_BloodStrike_Meat` · `Ai_L_ButchersStrike` · `Ai_L_CoinExplosion_Coin` · `Ai_L_MentalCorruption_Projectile` · `Ai_L_Multishot_Arrow` · `Ai_L_SmallMoltenCore_Dragon_Atk` · `Ai_L_SoulKiller` · `Ai_L_SoulKiller_Soul` · `Ai_L_SpectreBullet` · `Ai_M_FrostyCharge` · `Ai_MiniBoss_IceAura_AoE` · `Ai_MiniBoss_OrbSpitter_Orb` · `Ai_MiniBoss_SpinningArrow_Arrow` · `Ai_Mon_DarkCave_BossSeeker_PurpleOrb` · `Ai_Mon_DarkCave_CaveBat_Dash` · `Ai_Mon_DarkCave_DarkElemental_Atk_Projectile` · `Ai_Mon_DarkCave_DarkElemental_Barrage_Arrow` · `Ai_Mon_DarkCave_NightOlm_Atk_Projectile` · `Ai_Mon_Despair_BossAzurak_AltAtk` · `Ai_Mon_Despair_BossAzurak_DoubleStomp_Instance` · `Ai_Mon_Despair_BossAzurak_RoarAtk` · `Ai_Mon_Despair_BossAzurak_Roll` · `Ai_Mon_Despair_BossAzurak_StompBlock` · `Ai_Mon_Despair_BossAzurak_StompGlobal` · `Ai_Mon_Despair_BossAzurak_StompProjectile` · `Ai_Mon_Despair_BossAzurak_StompProjectile_Projectile` · `Ai_Mon_Despair_Displacer_SpawnEgg` · `Ai_Mon_Despair_ParalyticFly_Paralyze` · `Ai_Mon_Despair_WretchedArtillery_BarrageAtk_AoE` · `Ai_Mon_Despair_WretchedArtillery_BarrageAtk_Missile` · `Ai_Mon_Forest_BossDemon_AltSkill_Stomp` · `Ai_Mon_Forest_BossDemon_MainSkill_SpawnMissiles_Missile` · `Ai_Mon_Forest_BossDemon_MainSkill_Stomp` · `Ai_Mon_Forest_Hound_Charge` · `Ai_Mon_Forest_SpiderSpitter_Atk` · `Ai_Mon_Ink_Archer_Atk` · `Ai_Mon_Ink_Archer_Dodge` · `Ai_Mon_Ink_BossDarkMoon_Blade_Instance` · `Ai_Mon_Ink_BossDarkMoon_Blade_RageInstance` · `Ai_Mon_Ink_BossDarkMoon_Eclipse_Instance` · `Ai_Mon_Ink_BossDarkMoon_Hammer` · `Ai_Mon_Ink_BossDarkMoon_ShortDash_Atk` · `Ai_Mon_Ink_BossDarkMoon_SpawnEgoSword_Projectile` · `Ai_Mon_Ink_BossDarkMoon_Spear_Instance` · `Ai_Mon_Ink_BossDarkMoon_ThrowSpear_Projectile` · `Ai_Mon_Ink_BossDarkMoon_ThrowSpear_TeleportAtk_AfterAtk` · `Ai_Mon_Ink_BossWhiteNight_AltAtk` · `Ai_Mon_Ink_BossWhiteNight_BuddhasPalm_Instance` · `Ai_Mon_Ink_BossWhiteNight_Cataclysm_Eclipse` · `Ai_Mon_Ink_BossWhiteNight_Cataclysm_Instance` · `Ai_Mon_Ink_BossWhiteNight_DestructionWave_Wave` · `Ai_Mon_Ink_BossWhiteNight_OneInchPunch_Pull` · `Ai_Mon_Ink_BossWhiteNight_Oppression` · `Ai_Mon_Ink_BossWhiteNight_RageInstance` · `Ai_Mon_Ink_BossWhiteNight_RageInstance_Rock` · `Ai_Mon_Ink_BossWhiteNight_Ready` · `Ai_Mon_Ink_DivineAnimal_Bite` · `Ai_Mon_Ink_DivineAnimal_Missile_Sub` · `Ai_Mon_Ink_DivineAnimal_Stomp` · `Ai_Mon_Ink_EgoSword_Atk` · `Ai_Mon_Ink_GhostBlade_Atk` · `Ai_Mon_Ink_GhostBlade_DemolitionMan` · `Ai_Mon_Ink_GhostBlade_MeleeAtk` · `Ai_Mon_Ink_GhostBlade_SwiftStep_Atk` · `Ai_Mon_Ink_GhostBlade_SwiftStep_Projectile` · `Ai_Mon_Ink_GhostSpear_Atk` · `Ai_Mon_Ink_Tiger_DashAtk` · `Ai_Mon_LavaLand_BossInfernus_BreathFire_Projectile` · `Ai_Mon_LavaLand_BossInfernus_Dash` · `Ai_Mon_LavaLand_BossInfernus_PowerBomb_FlamePillar` · `Ai_Mon_LavaLand_BossInfernus_Roar_Projectile` · `Ai_Mon_LavaLand_BossInfernus_WallStunKnockback` · `Ai_Mon_LavaLand_FireElemental_DestructSub` · `Ai_Mon_LavaLand_FireElemental_ExplosionSub` · `Ai_Mon_LavaLand_FireElemental_LaserAtk` · `Ai_Mon_LavaLand_InfernoSpider_LavaAtk` · `Ai_Mon_LavaLand_Magmadon_Charge` · `Ai_Mon_LavaLand_Magmadon_Charge_Projectile` · `Ai_Mon_LavaLand_SuperheatedWolf_SelfDestruct` · `Ai_Mon_Polaris_Smite` · `Ai_Mon_Primus_BossPrimusAeron_Adapt_Arbalest_Projectile` · `Ai_Mon_Primus_BossPrimusAeron_Adapt_Atk` · `Ai_Mon_Primus_BossPrimusAeron_Adapt_Doom_Meteor_SubFireball` · `Ai_Mon_Primus_BossPrimusAeron_Adapt_IceClaw` · `Ai_Mon_Primus_BossPrimusAeron_Adapt_IceClaw_Frost` · `Ai_Mon_Primus_BossPrimusAeron_Rage_DashAttack` · `Ai_Mon_Primus_SpawnAttack` · `Ai_Mon_Sky_Baam_Teleport` · `Ai_Mon_Sky_BigBaam_BeamAtk` · `Ai_Mon_Sky_BigBaam_Main_Root` · `Ai_Mon_Sky_BigBaam_RangedAtk` · `Ai_Mon_Sky_BossNyx_LineAtk_Displacement` · `Ai_Mon_Sky_BossNyx_PillarOfStars` · `Ai_Mon_Sky_BossNyx_PullAtk` · `Ai_Mon_Sky_BossNyx_StarBuff_Projectile` · `Ai_Mon_Sky_BossNyx_StellarDash` · `Ai_Mon_Sky_LittleBaam_Atk` · `Ai_Mon_Sky_StarSeed_SelfDestruct_Projectile` · `Ai_Mon_Sky_StellaMatter_AtkSub` · `Ai_Mon_Sky_StellaMatter_Die` · `Ai_Mon_Sky_StellaMatter_Throw` · `Ai_Mon_Sky_StellaMatter_ThrowSub` · `Ai_Mon_SnowMountain_BossSkoll_AuraBlade` · `Ai_Mon_SnowMountain_BossSkoll_AuraSlice` · `Ai_Mon_SnowMountain_BossSkoll_SummonArrow_Instance` · `Ai_Mon_SnowMountain_IceElemental_DoubleSwipe` · `Ai_Mon_SnowMountain_LivingShards_Atk` · `Ai_Mon_SnowMountain_Scavenger_Throw` · `Ai_Mon_SnowMountain_VikingWarrior_Shield` · `Ai_Mon_SnowMountain_VikingWarrior_ThrowShield` · `Ai_Mon_Special_BossErebos_AntiGravity_Instance` · `Ai_Mon_Special_BossErebos_AtkInstance` · `Ai_Mon_Special_BossErebos_Gaze_Instance` · `Ai_Mon_Special_BossErebos_Meteor` · `Ai_Mon_Special_BossErebos_Ripple` · `Ai_Mon_Special_BossErebos_SpawnTormentor_Attacker_Instance` · `Ai_Mon_Special_BossErebos_StarRain_Instance` · `Ai_Mon_Special_BossErebos_Teleport_Instance` · `Ai_Mon_Special_BossLightElemental_Beam` · `Ai_Mon_Special_BossMaw_AnnihilationStance_Instance` · `Ai_Mon_Special_BossMaw_Chomp_DashAtk` · `Ai_Mon_Special_BossMaw_PrecisionShot_Projectile` · `Ai_Mon_Special_BossMaw_Purgatory_Instance` · `Ai_Mon_Special_BossMaw_ScatterShot_ShortProjectile` · `Ai_Mon_Special_BossMaw_ShadowOverdrive_Projectile` · `Ai_Mon_Special_BossMaw_ShadowWalk_Projectile` · `Ai_Mon_Special_BossMaw_SliceThroat_Atk` · `Ai_Mon_Special_BossObliviax_Artillery_Instance` · `Ai_Mon_Special_BossObliviax_BackStep_Instance` · `Ai_Mon_Special_BossObliviax_ChargeSequence_MissileAtk` · `Ai_Mon_Special_BossObliviax_ChargeSequence_Spawner` · `Ai_Mon_Special_BossObliviax_DashAtk` · `Ai_Mon_Special_BossObliviax_NeedleAtk_AtkInstance` · `Ai_Mon_Special_BossObliviax_NeedleAtk_Instance` · `Ai_Mon_Special_BossObliviax_TurnAtk` · `Ai_Mon_Special_BossObliviax_TurnAtk_DelayedAtk` · `Ai_Mon_Special_BossObliviax_TurretMode_Projectile` · `Ai_Mon_Special_BossPolaris_Holy_GoldenSpear_Projectile` · `Ai_Nor_CosmicBlast` · `Ai_Nor_MyOwnLittleNebula_Missile` · `Ai_QR_DistortedMind_Spawner` · `Ai_QR_InfernalTales` · `Ai_QR_Innocence_Spawner` · `Ai_QR_TwistedTales_Projectile` · `Ai_QR_TwistedTales_Spawner` · `Ai_QR_ValiantHeart` · `Ai_Q_BigBorealChunk_Explosion` · `Ai_Q_BigBorealChunk_Spawner` · `Ai_Q_CruelSun_Shockwave` · `Ai_Q_DeathMark_Projectile` · `Ai_Q_EmbracingTheChill_AreaDoT` · `Ai_Q_EtherealInfluence` · `Ai_Q_EtherealInfluence_Projectile_Base` · `Ai_Q_Fleche_Dash` · `Ai_Q_GoldenBurst` · `Ai_Q_HandCannon` · `Ai_Q_IncendiaryRounds_Attack` · `Ai_Q_Laceration_Circle` · `Ai_Q_Lunge` · `Ai_Q_MoonlightPact_Fenrir_Atk` · `Ai_Q_MoonlightPact_Land` · `Ai_Q_Reduction_Projectile` · `Ai_Q_Riposte` · `Ai_Q_SuperNova` · `Ai_R_AnnihilationStance_Projectile` · `Ai_R_BackOff_Damage` · `Ai_R_BaptismOfSun` · `Ai_R_BlackArbalest` · `Ai_R_BladeFan` · `Ai_R_ChainReaction` · `Ai_R_Chomp` · `Ai_R_DancingBlades` · `Ai_R_DarkGrenade_Shard` · `Ai_R_DarkGrenade_ShardSpawner` · `Ai_R_Fireball` · `Ai_R_Frostbite_Freeze_Projectile` · `Ai_R_FrozenFists_PunchDash` · `Ai_R_GreatFrostSword` · `Ai_R_Ignite` · `Ai_R_OrbOfLight_BackwardHealing` · `Ai_R_OrbOfLight_ForwardDamaging` · `Ai_R_Parry_Projectile` · `Ai_R_PhantomBlade` · `Ai_R_PhaseShift` · `Ai_R_PillarOfFlame` · `Ai_R_PrecisionShot_Projectile` · `Ai_R_QuickTrigger_Projectile` · `Ai_R_RepulsiveShield_Projectile` · `Ai_R_SanctuaryOfEl_Ground` · `Ai_R_Scattershot_Projectile` · `Ai_R_Scattershot_Spawner` · `Ai_R_SerpentineBlessing_Projectile` · `Ai_R_ShadowOverdrive_Projectile` · `Ai_R_ShadowWalk` · `Ai_R_ShadowWalk_Projectile` · `Ai_R_Smite` · `Ai_R_Somersault` · `Ai_R_StaticDischarge` · `Ai_R_SummonLittleBaam_Baam_Atk` · `Ai_R_UnbreakableDetermination_SubExplosion` · `Ai_R_WarBoomerang` · `Ai_R_WrathOfEl` · `Ai_Shrine_SmallSoul_Attack` · `Ai_U_BeamOfBalance_Beam` · `Ai_U_BigChomp` · `Ai_U_Hysteria_Claw` · `Ai_U_WorldCracker` · `Ai_UnstableRatSwarm_Projectile` · [DamageData](/api/Global.DamageData) · [DamageInstance](/api/Global.DamageInstance) · [Gem](/api/Global.Gem) · `Gem_C_Confidence` · `Gem_C_Efficiency` · `Gem_C_Guidance` · `Gem_C_Lethality` · `Gem_C_Nap` · `Gem_C_Responsibility` · `Gem_C_Shatter` · `Gem_C_Sulfur` · `Gem_C_Talc` · `Gem_C_Vengeance` · `Gem_E_Blossom` · `Gem_E_Clemency` · `Gem_E_Direness` · `Gem_E_Domination` · `Gem_E_Fangs` · `Gem_E_Flexibility` · `Gem_E_Insight` · `Gem_E_Inversion` · `Gem_E_Metal` · `Gem_E_Might` · `Gem_E_Omega` · `Gem_E_Opportunity` · `Gem_E_Overload` · `Gem_E_Pain` · `Gem_E_Predation` · `Gem_E_Thunder` · `Gem_E_Twilight` · `Gem_E_Umbra` · `Gem_L_ChaosApple` · `Gem_L_Culinary` · `Gem_L_DivineFaith` · `Gem_L_Embertail` · `Gem_L_HeartOfGold` · `Gem_L_Paranoia` · `Gem_L_Perfect` · `Gem_L_SolarEye` · `Gem_L_Supersymmetry` · `Gem_R_Adventure` · `Gem_R_Blade` · `Gem_R_Bleak` · `Gem_R_Contempt` · `Gem_R_Crucible` · `Gem_R_Epiphany` · `Gem_R_Flow` · `Gem_R_Frost` · `Gem_R_Glass` · `Gem_R_Lightweight` · `Gem_R_Momentum` · `Gem_R_Mortality` · `Gem_R_NightSky` · `Gem_R_Purity` · `Gem_R_Rejuvenation` · `Gem_R_Rigidity` · `Gem_R_Scorched` · `Gem_R_Slippery` · `Gem_R_Snow` · `Gem_R_Spiral` · `Gem_R_Wealth` · `Gem_U_EternalFlame` · `Gem_U_GlacialCore` · `Se_C_CorrosiveTrails_Poisoned` · `Se_C_CorrosiveTrails_Spawner` · `Se_C_Hemorrhage_Bleed` · `Se_C_IceBlock` · `Se_D_AstridsMasterpieceEnGarde` · `Se_D_AstridsMasterpiecePriorite` · `Se_D_BeautifulThreat` · `Se_D_ChargedAnguillian` · `Se_D_CircleOfLife_Summon` · `Se_D_ConvergencePoint` · `Se_D_CrystalsInOrbit` · `Se_D_DoubleTap` · `Se_D_IcyVeins` · `Se_D_MasterOfAssassination_DoT` · `Se_D_MercyOfEl` · `Se_D_ParryMaster_Buff` · `Se_D_PrismaticEyes` · `Se_D_Resolve` · `Se_D_TheKillingFlow` · `Se_D_TrueDuelist_Exposed` · `Se_E_Aftershock_Armor` · `Se_E_FinalExplosion` · `Se_E_Harvest_OnVictim` · `Se_E_LizardlyBlessing` · `Se_E_Permafrost_Shield` · `Se_E_Rewind` · `Se_E_Rewind_Damage` · `Se_E_UmbralEdge` · `Se_EngulfedInFlame` · `Se_Gem_C_Love` · `Se_Gem_C_Quicksilver` · `Se_Gem_C_Wind` · `Se_Gem_E_Apathy_Armor` · `Se_Gem_E_Insight_Buff` · `Se_Gem_E_Obsidian_EmpowerAttack` · `Se_Gem_E_Protection` · `Se_Gem_E_Reflex_ArmorBonus` · `Se_Gem_L_Liberty_Buff` · `Se_Gem_R_Control_Debuff` · `Se_Gem_R_Epiphany_ApBuff` · `Se_Gem_R_Hedgehog_Aura` · `Se_Gem_R_Insatiable` · `Se_Gem_R_Panic` · `Se_Gem_R_Wound_Wounded` · `Se_Gem_Regeneration` · `Se_Gem_U_SoulPrison_DeathInterrupt` · `Se_L_MentalCorruption` · `Se_L_Multishot_Buff` · `Se_L_PyranasFireball` · `Se_MiniBoss_UnstableExplosive_Explosion` · `Se_Mon_Despair_ParalyticFly_Atk_Instance` · `Se_Mon_Despair_ParalyticFly_Paralyze` · `Se_Mon_Forest_Treant_Rage` · `Se_Mon_Ink_BossWhiteNight_Rush` · `Se_Mon_Sky_BossNyx_PhaseChange` · `Se_Nor_ReptilianThirdEye` · `Se_Nor_WindowToTheSoul_SpiritualDominance` · `Se_QR_ValiantHeart_Speed` · `Se_Q_CruelSun_Armored` · `Se_Q_Fleche` · `Se_Q_Fleche_VictimTracker` · `Se_Q_IncendiaryRounds_EmpowerAttacks` · `Se_Q_PerfectExecution` · `Se_Q_SuperNova_Slow` · `Se_Q_Suppression_Old` · `Se_R_AnnihilationStance` · `Se_R_BackOff_Shielded` · `Se_R_BaptismOfSun_Buff` · `Se_R_BoneCrusher` · `Se_R_BoneCrusher_UnstoppableAndShield` · `Se_R_Cataclysm` · `Se_R_Composure_Buff` · `Se_R_DangerousTheory` · `Se_R_Deception` · `Se_R_Frostbite_EmpowerAttacks` · `Se_R_FrozenFists` · `Se_R_Immolation` · `Se_R_Inspire_Buff` · `Se_R_Lava_Debuff` · `Se_R_LightningDance` · `Se_R_NaturesWhisper_Buff` · `Se_R_Parry_Start` · `Se_R_RepulsiveShield` · `Se_R_SanctuaryOfEl_Buff` · `Se_R_SerpentineBlessing_Buff` · `Se_R_ShadowOverdrive_AtkSpd` · `Se_R_ShadowOverdrive_Initial` · `Se_R_ShadowWalk_EmpowerAttacks` · `Se_R_Somersault_CritBonus` · `Se_R_Tranquility` · `Se_R_UnbreakableDetermination` · `Se_Star_Aurena_F_DT_LowerThresholdBiggerHeals` · `Se_Star_Aurena_F_GB_LessDamageLessSacrifice` · `Se_Star_Bismuth_F_IT_InnerDamage` · `Se_Star_Bismuth_F_IT_SmallerRingMoreDamage` · `Se_Star_Husk_F_AS_NoShockwaveFasterAttack` · `Se_Star_Husk_F_AS_NonUltimate` · `Se_Star_Husk_F_DE_HitHealMissPenalty` · `Se_Star_Mist_F_UD_NonUltimate` · `Se_Star_Nachia_F_MP_StrongerFenrirNoCast` · `Se_Star_Nachia_F_NW_LessCooldownLessAtkSpd` · `Se_Star_Nachia_F_SB_StrongerBuffNoSelf` · `Se_Star_Vesper_F_BS_ExplosionOnEnd` · `Se_Star_Vesper_F_CS_ColdDamage` · `Se_Star_Vesper_F_CS_UnlockMoveWithPenalty` · `Se_Star_Vesper_F_SE_FullOffense` · `Se_Star_Yubar_F_SN_DodgeReset` · `Se_Star_Yubar_F_SN_PullEnemy` · `Se_U_Burrow` · `Se_U_EternalFlame_Curse` · `Se_U_HerWorld_Blackhole` · [SkillTrigger](/api/Global.SkillTrigger) · `St_D_CircleOfLife` · `St_D_DisintegratingClaw` · `St_D_MomentumOfCombat` · `St_D_ParryMaster` · `St_D_SalamanderPowder` · `St_D_SharedPain` · `St_D_ThirstOfVengence` · `St_E_ClutchesOfMalice` · `St_L_ButchersStrike` · `St_L_HerosReturn` · `St_L_SoulKiller` · `St_R_Somersault` · `Sum_R_AnnoyingBanner` · [Summon](/api/Global.Summon)

### Dependencies (2)

*Types and components that `ScalingValue` references or depends upon:*

[Entity](/api/Global.Entity) · [EntityStatus](/api/Global.EntityStatus)

### Related Enums (1)

*Enumerations referenced in fields, properties, or method signatures:*

<a href="/enums#levelscaling" class="enum-link" data-tooltip="NoScaling=0 · SkillDefault=1 · GemDefault=2">LevelScaling</a>

:::
