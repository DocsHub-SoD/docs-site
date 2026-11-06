# Class: StandardProjectile

- **Category:** <span class="cat-dot" style="--cat-color: #ef4444" data-cat="Combat & Abilities"></span> Combat & Abilities
- **Namespace:** `Global`
- **Assembly:** `Dew.Core.dll`
- **Inheritance / Derived:** [DewNetworkBehaviour](/api/Global.DewNetworkBehaviour) → [Actor](/api/Global.Actor) → [AbilityInstance](/api/Global.AbilityInstance) → [Projectile](/api/Global.Projectile) → [AttackProjectile](/api/Global.AttackProjectile)

```csharp
public abstract class StandardProjectile : Projectile, ILogicUpdate, ICleanup, ICustomDestroyRoutine
```

## Fields (7)

::: details Click to expand Fields (7)

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`_acceleration`** | `[SyncVar] [BoxGroup("Projectile Settings", true, false, 0)] public float _acceleration` |  |
| **`_initialSpeed`** | `[SyncVar] [BoxGroup("Projectile Settings", true, false, 0)] public float _initialSpeed` |  |
| **`_targetSpeed`** | `[SyncVar] [BoxGroup("Projectile Settings", true, false, 0)] public float _targetSpeed` |  |
| **`enableRandomCurve`** | `[BoxGroup("Projectile Settings", true, false, 0)] [Title("Random Curve", null, TitleAlignments.Left, true, true)] public bool enableRandomCurve` |  |
| **`ensurePositiveY`** | `[BoxGroup("Projectile Settings", true, false, 0)] [ShowIf("enableRandomCurve", true)] public bool ensurePositiveY` |  |
| **`randomCurveMagnitude`** | `[BoxGroup("Projectile Settings", true, false, 0)] [LabelText("Random Magnitude")] [ShowIf("enableRandomCurve", true)] public float randomCurveMagnitude` |  |
| **`use3DVelocity`** | `[Title("Standard Projectile", null, TitleAlignments.Left, true, true)] [LabelText("Use 3D Velocity")] [BoxGroup("Projectile Settings", true, false, 0)] public bool use3DVelocity` |  |

:::

## Properties (4)

::: details Click to expand Properties (4)

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`acceleration`** | `public float acceleration { get; set; }` |  |
| **`initialSpeed`** | `public float initialSpeed { get; set; }` |  |
| **`normalizedPosition`** | `public float normalizedPosition { get; }` | Represents progress of this projectile's trajectory. This value starts from 0 to 1 and never decreases. |
| **`targetSpeed`** | `public float targetSpeed { get; set; }` |  |

:::

## Methods (5)

::: details `ActiveFrameUpdate()`

```csharp
protected override void ActiveFrameUpdate()
```

:::

::: details `CheckForCompletion()`

```csharp
protected override bool CheckForCompletion()
```

**Returns:** `bool`

:::

::: details `OnCreate()`

```csharp
protected override void OnCreate()
```

:::

::: details `OnDisable()`

```csharp
protected override void OnDisable()
```

:::

::: details `PositionSolver(float)`

```csharp
protected override Vector3 PositionSolver(float dt)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `dt` | `float` |  |

**Returns:** `UnityEngine.Vector3`

:::


## Architecture & Relationships

::: details Click to expand Architecture & Relationships

### Used By (144)

*Classes and systems that invoke, reference, or depend on `StandardProjectile`:*

`Ai_ArtifactWorldModel_Projectile` · `Ai_C_BackStep_Bomb` · `Ai_C_DarkBolt` · `Ai_C_IceBlock_Projectile` · `Ai_C_IceBolt` · `Ai_C_LuckyHammer` · `Ai_C_Pew_Projectile` · `Ai_C_Purgatory_Heal` · `Ai_C_SparklingWaterGun` · `Ai_C_SpearThrow` · `Ai_C_Starfall_Projectile` · `Ai_D_BeautifulThreat_Feather` · `Ai_D_ChargedAnguillian_Lightning` · `Ai_D_DanceOfValor_Projectile` · `Ai_D_ExoticMatter_Projectile` · `Ai_D_FrostTouch_FrostProjectile` · `Ai_D_SalamanderPowder_Projectile` · `Ai_E_ChainLightning` · `Ai_E_CrimsonLance` · `Ai_E_DoomsdayMeteor_SubProjectile` · `Ai_E_FlameJet_Projectile` · `Ai_E_MysticDagger` · `Ai_E_ShadowVolley_Projectile` · `Ai_Gem_C_Charcoal_Projectile` · `Ai_Gem_C_Sharp_Arrow` · `Ai_Gem_C_Vengence_Projectile` · `Ai_Gem_E_Domination_CritGainEffect` · `Ai_Gem_E_Fangs_Projectile` · `Ai_Gem_L_Embertail_Projectile` · `Ai_Gem_L_PureWhite_Projectile` · `Ai_Gem_R_Accuracy_Projectile` · `Ai_Gem_R_Dusk_Projectile` · `Ai_Gem_R_Ricochet` · `Ai_Gem_R_Shock_Lightning` · `Ai_Gem_R_Snow_Projectile` · `Ai_Gem_R_Spiral_Fireball` · `Ai_Gem_U_GlacialCore_Projectile` · `Ai_Gem_U_GuidingCompass_PowerGainProjectile` · `Ai_L_CoinExplosion_Coin` · `Ai_L_MentalCorruption_Projectile` · `Ai_L_Multishot_Arrow` · `Ai_L_SmallMoltenCore_Dragon_Atk` · `Ai_L_SpectreBullet` · `Ai_MiniBoss_BloodThorn_Projectile` · `Ai_MiniBoss_OrbSpitter_Orb` · `Ai_MiniBoss_SpinningArrow_Arrow` · `Ai_MirageSkin_Delusion_Missile` · `Ai_MirageSkin_Oblivion_Orb` · `Ai_Mon_DarkCave_BossSeeker_Atk_Projectile` · `Ai_Mon_DarkCave_BossSeeker_GreenChaserOrb` · `Ai_Mon_DarkCave_DarkElemental_Atk_Projectile` · `Ai_Mon_DarkCave_DarkElemental_Barrage_Arrow` · `Ai_Mon_DarkCave_NightOlm_Atk_Projectile` · `Ai_Mon_Despair_BossAzurak_StompBlock_Artillery` · `Ai_Mon_Despair_BossAzurak_StompProjectile_Projectile` · `Ai_Mon_Despair_ParalyticFly_Paralyze` · `Ai_Mon_Despair_WretchedArtillery_BarrageAtk_Missile` · `Ai_Mon_Forest_BossDemon_MainSkill_SpawnMissiles_Missile` · `Ai_Mon_Forest_SpiderSpitter_Atk` · `Ai_Mon_Ink_BossDarkMoon_SpawnEgoSword_Projectile` · `Ai_Mon_Ink_BossDarkMoon_ThrowSpear_Projectile` · `Ai_Mon_Ink_BossDarkMoon_ThrowSpear_TeleportAtk_AfterAtk` · `Ai_Mon_Ink_BossWhiteNight_AltAtk` · `Ai_Mon_Ink_Boss_OnDeath` · `Ai_Mon_Ink_GhostBlade_Atk` · `Ai_Mon_Ink_GhostBlade_SwiftStep_Projectile` · `Ai_Mon_LavaLand_BossInfernus_AltAtk_Projectile` · `Ai_Mon_LavaLand_BossInfernus_BreathFire_Projectile` · `Ai_Mon_LavaLand_BossInfernus_Roar_Projectile` · `Ai_Mon_LavaLand_InfernoSpider_LavaAtk` · `Ai_Mon_LavaLand_InfernusPillar_Projectile` · `Ai_Mon_LavaLand_Magmadon_Charge_Projectile` · `Ai_Mon_LavaLand_Magmadon_Projectile` · `Ai_Mon_Primus_BossPrimusAeron_Adapt_Arbalest` · `Ai_Mon_Primus_BossPrimusAeron_Adapt_Arbalest_Projectile` · `Ai_Mon_Primus_BossPrimusAeron_Adapt_Atk` · `Ai_Mon_Primus_BossPrimusAeron_Adapt_Doom_Meteor_SubFireball` · `Ai_Mon_Primus_BossPrimusAeron_PhaseSwitcher_DualSword` · `Ai_Mon_Primus_BossPrimusAeron_PhaseSwitcher_GreatSword` · `Ai_Mon_Sky_BigBaam_RangedAtk` · `Ai_Mon_Sky_BossNyx_StarBuff_Projectile` · `Ai_Mon_Sky_StarSeed_SelfDestruct_Projectile` · `Ai_Mon_Sky_StellaMatter_Die` · `Ai_Mon_Sky_StellaMatter_Throw` · `Ai_Mon_SnowMountain_Scavenger_Throw` · `Ai_Mon_SnowMountain_VikingWarrior_Shield` · `Ai_Mon_Special_AmbushSpawner_Projectile` · `Ai_Mon_Special_BossErebos_StarRain_Instance` · `Ai_Mon_Special_BossMaw_AnnihilationStance_Instance` · `Ai_Mon_Special_BossMaw_PillarOfFlame_Projectile` · `Ai_Mon_Special_BossMaw_PrecisionShot` · `Ai_Mon_Special_BossMaw_PrecisionShot_Projectile` · `Ai_Mon_Special_BossMaw_Purgatory_Heal` · `Ai_Mon_Special_BossMaw_ScatterShot_ShortProjectile` · `Ai_Mon_Special_BossMaw_ShadowOverdrive_Projectile` · `Ai_Mon_Special_BossObliviax_NeedleAtk_Instance` · `Ai_Mon_Special_BossObliviax_TurnAtk_Projectile` · `Ai_Mon_Special_BossObliviax_TurretMode_Projectile` · `Ai_Mon_Special_BossPolaris_Holy_Atk_Projectile` · `Ai_Mon_Special_BossPolaris_Holy_CounterSpell_DisarmProjectile` · `Ai_Mon_Special_BossPolaris_Holy_CounterSpell_SkillProjectile` · `Ai_Mon_Special_BossPolaris_Holy_GoldenSpear_Projectile` · `Ai_Mon_Special_BossPolaris_Holy_Purgatory_HealProjectile` · `Ai_MorasDomain_SpawnMonsterProjectile` · `Ai_Nor_CosmicBlast` · `Ai_Nor_MyOwnLittleNebula_Missile` · `Ai_QR_Innocence_Projectile` · `Ai_QR_TwistedTales_Projectile` · `Ai_Q_BigBorealChunk_Projectile` · `Ai_Q_DeathMark_Projectile` · `Ai_Q_EtherealInfluence_Projectile_Base` · `Ai_Q_Reduction_Projectile` · `Ai_R_AnnihilationStance_Projectile` · `Ai_R_BlackArbalest` · `Ai_R_DancingBlades_MockProjectile` · `Ai_R_DarkGrenade_Shard` · `Ai_R_DarkGrenade_ShardSpawner` · `Ai_R_Fireball` · `Ai_R_Frostbite_Freeze_Projectile` · `Ai_R_Ignite_FakeProjectile` · `Ai_R_NaturesWhisper_MockProjectile` · `Ai_R_OrbOfLight_BackwardHealing` · `Ai_R_OrbOfLight_ForwardDamaging` · `Ai_R_Parry_Projectile` · `Ai_R_PrecisionShot_Projectile` · `Ai_R_QuickTrigger_Projectile` · `Ai_R_RepulsiveShield_Projectile` · `Ai_R_Scattershot_Projectile` · `Ai_R_SerpentineBlessing_Projectile` · `Ai_R_ShadowOverdrive_Projectile` · `Ai_R_ShadowWalk_Projectile` · `Ai_R_WarBoomerang` · `Ai_RandomGemUpgrade` · `Ai_RegenOrb_Projectile` · `Ai_Shrine_CallOfTheRavenous_Projectile` · `Ai_StarCookie_Projectile` · `Ai_Star_Bismuth_D_BonusAttackEffect_Arrow` · `Ai_StarlessPath_PowerOfGuidance_MockProjectile` · `Ai_Trap_ArrowShooter_Arrow` · `Ai_UnstableRatSwarm_Projectile` · [AttackProjectile](/api/Global.AttackProjectile) · `Se_MirageSkin_Oblivion` · `Se_MirageSkin_Pulverization` · `Se_Star_Husk_F_AS_NoShockwaveFasterAttack`

### Dependencies (3)

*Types and components that `StandardProjectile` references or depends upon:*

[AbilityInstance](/api/Global.AbilityInstance) · [Actor](/api/Global.Actor) · [Projectile](/api/Global.Projectile)

:::
