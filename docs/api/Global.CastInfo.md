# Struct: CastInfo

- **Category:** <span class="cat-dot" style="--cat-color: #ef4444" data-cat="Combat & Abilities"></span> Combat & Abilities
- **Namespace:** `Global`
- **Assembly:** `Dew.Core.dll`

```csharp
public struct CastInfo
```

## Fields (5)

::: details Click to expand Fields (5)

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`angle`** | `public float angle` |  |
| **`animSelectValue`** | `public float animSelectValue` | This is populated on AbilityTrigger.OnCastStart. |
| **`caster`** | `public Entity caster` |  |
| **`point`** | `public Vector3 point` |  |
| **`target`** | `public Entity target` |  |

:::

## Properties (2)

::: details Click to expand Properties (2)

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`forward`** | `public Vector3 forward { get; }` |  |
| **`rotation`** | `public Quaternion rotation { get; }` |  |

:::

## Methods (2)

::: details `GetAngle(Quaternion)`

```csharp
public static float GetAngle(Quaternion rotation)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `rotation` | `UnityEngine.Quaternion` |  |

**Returns:** `float`

:::

::: details `GetAngle(Vector3)`

```csharp
public static float GetAngle(Vector3 forward)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `forward` | `UnityEngine.Vector3` |  |

**Returns:** `float`

:::


## Architecture & Relationships

::: details Click to expand Architecture & Relationships

### Used By (137)

*Classes and systems that invoke, reference, or depend on `CastInfo`:*

[AbilityInstance](/api/Global.AbilityInstance) · [AbilityTrigger](/api/Global.AbilityTrigger) · [ActionCast](/api/Global.ActionCast) · [Actor](/api/Global.Actor) · `Ai_Atk_LacertaRifle` · `Ai_Atk_LacertaRifle_Crit` · `Ai_C_BeamOfLight` · `Ai_C_DarkSpear` · `Ai_C_IceClaw` · `Ai_C_MagicSword` · `Ai_C_Pew_Projectile` · `Ai_C_PressurePoint` · `Ai_C_SparklingWaterGun` · `Ai_D_BurningFist_Attack` · `Ai_D_Resolve_Push` · `Ai_E_CrimsonLance` · `Ai_E_FlameJet` · `Ai_E_MysticDagger` · `Ai_E_SearingCharge` · `Ai_E_ShadowVolley_Projectile` · `Ai_E_StygianRush_Rush` · `Ai_Mon_DarkCave_BossSeeker_YellowDiagram_MainInstance` · `Ai_Mon_DarkCave_CaveBat_Dash` · `Ai_Mon_DarkCave_NightOlm_Atk_Projectile` · `Ai_Mon_Despair_BossAzurak_StompProjectile_Projectile` · `Ai_Mon_Forest_Hound_Charge` · `Ai_Mon_Ink_BossDarkMoon_ThrowSpear_TeleportAtk` · `Ai_Mon_Ink_BossWhiteNight_AltAtk` · `Ai_Mon_LavaLand_BossInfernus_AltAtk_Instance` · `Ai_Mon_LavaLand_BossInfernus_Atk` · `Ai_Mon_LavaLand_BossInfernus_BreathFire_Projectile` · `Ai_Mon_LavaLand_BossInfernus_Roar_Projectile` · `Ai_Mon_Primus_BossPrimusAeron_Adapt_Arbalest_Projectile` · `Ai_Mon_Primus_BossPrimusAeron_Adapt_Doom_Meteor_SubFireball` · `Ai_Mon_Primus_BossPrimusAeron_Rage_DashAttack` · `Ai_Mon_Sky_BigBaam_BeamAtk` · `Ai_Mon_Special_BossErebos_Gaze_Instance` · `Ai_Mon_Special_BossErebos_SpawnTormentor_Attacker` · `Ai_Mon_Special_BossErebos_SpawnTormentor_Attacker_Instance` · `Ai_Mon_Special_BossMaw_AnnihilationStance_Instance` · `Ai_Mon_Special_BossMaw_DarkSpear` · `Ai_Mon_Special_BossMaw_PrecisionShot_Projectile` · `Ai_Mon_Special_BossMaw_ScatterShot_Spawner` · `Ai_Mon_Special_BossObliviax_DashAtk` · `Ai_Mon_Special_BossObliviax_TurretMode_Projectile` · `Ai_Mon_Special_BossPolaris_Monster_Atk_FirstAtk` · `Ai_Mon_Special_BossPolaris_Monster_Atk_SecondAtk` · `Ai_Mon_Special_BossPolaris_Monster_Atk_Spawner` · `Ai_Q_BigBorealChunk_Spawner` · `Ai_Q_CruelSun` · `Ai_Q_DeathMark_Projectile` · `Ai_Q_HandCannon` · `Ai_Q_Reduction_Projectile` · `Ai_R_AnnihilationStance_Projectile` · `Ai_R_BackOff_Spawner` · `Ai_R_BlackArbalest` · `Ai_R_FrozenFists_PunchDash` · `Ai_R_PrecisionShot_Projectile` · `Ai_R_QuickTrigger_Projectile` · `Ai_R_Scattershot_Spawner` · `Ai_R_ShadowOverdrive_Projectile` · `Ai_Star_Bismuth_F_IT_SmallerRingAddDisplacement_Dash` · `Ai_U_Hysteria_Claw` · `Ai_U_ShoutOfOblivion` · `At_Atk_HuskSword` · `At_Atk_LacertaRifle` · `At_Atk_YubarStardust` · `At_Mon_DarkCave_BossSeeker_GreenChaserOrb` · `At_Mon_DarkCave_DarkElemental_Atk` · `At_Mon_Despair_ParalyticFly_Atk` · `At_Mon_Forest_BossDemon_AltSkill` · `At_Mon_Forest_BossDemon_MainSkill` · `At_Mon_Forest_BossDemon_Spawn` · `At_Mon_Forest_SpiderSpitter_Atk` · `At_Mon_Forest_SpiderSpitter_Melee` · `At_Mon_Ink_BossWhiteNight_OneInchPunch` · `At_Mon_LavaLand_BossInfernus_AltAtk` · `At_Mon_LavaLand_InfernoSpider_LavaAtk` · `At_Mon_Primus_BossPrimusAeron_Rage_MassDelusion` · `At_Mon_Sky_BigBaam_BeamAtk` · `At_Mon_Sky_StarSeed_SelfDestruct` · `At_Mon_Special_BossErebos_SpawnTormentor` · `At_Mon_Special_BossMaw_Purgatory` · `At_Mon_Special_BossObliviax_Artillery` · `At_Mon_Special_BossObliviax_NeedleAtk` · `At_Mon_Special_BossPolaris_Holy_Beam` · `At_Mon_Special_BossPolaris_Holy_GoldenSpear` · `At_Mon_Special_BossPolaris_Holy_SelfCleanse` · `At_Mon_Special_BossPolaris_Monster_PizzaLightning` · [AttackTrigger](/api/Global.AttackTrigger) · [CastIndicatorManager](/api/Global.CastIndicatorManager) · [ChargingChannel](/api/Global.ChargingChannel) · [ControlManager](/api/Global.ControlManager) · [DamageInstance](/api/Global.DamageInstance) · [DashAttackInstance](/api/Global.DashAttackInstance) · [Dew](/api/Global.Dew) · [DewEffect](/api/Global.DewEffect) · [DewPlayer](/api/Global.DewPlayer) · [EntityAI](/api/Global.EntityAI) · [EntityControl](/api/Global.EntityControl) · [EventInfoAttackFired](/api/Global.EventInfoAttackFired) · [EventInfoCast](/api/Global.EventInfoCast) · [FxCastTelegraph](/api/Global.FxCastTelegraph) · [Gem](/api/Global.Gem) · `Gem_L_Paranoia` · `Gem_U_LastStarlight` · [MeleeAttackInstance](/api/Global.MeleeAttackInstance) · `Mon_Ink_BossDarkMoonHallucination` · [Projectile](/api/Global.Projectile) · [SampleCastInfoContext](/api/Global.SampleCastInfoContext) · `Se_D_ExoticMatter` · `Se_D_PrismaticEyes` · `Se_E_CrimsonLance_BossDrop` · `Se_MiniBoss_SpinningArrow` · `Se_R_AnnihilationStance` · `Se_R_Parry_Start` · `Se_R_RepulsiveShield` · `Se_Star_Husk_L_DodgeChargesAndRangeWithPenalty` · `Se_U_Hysteria` · [SkillTrigger](/api/Global.SkillTrigger) · `St_C_LuckyHammer` · `St_C_ShockTrap` · `St_C_SpearThrow` · `St_C_Whirlwind` · `St_E_ChainLightning` · `St_L_HerosReturn` · `St_L_SmallMoltenCore` · `St_QR_InfernalTales` · `St_QR_ValiantHeart` · `St_R_AnnoyingBanner` · `St_R_WarBoomerang` · `St_U_ShoutOfOblivion` · [Summon](/api/Global.Summon) · `Trap_ArrowShooter` · [TriggerConfig](/api/Global.TriggerConfig) · `UI_InGame_SkillButton` · `Mirror.GeneratedNetworkCode`

### Dependencies (3)

*Types and components that `CastInfo` references or depends upon:*

[Actor](/api/Global.Actor) · [Entity](/api/Global.Entity) · `Vector3FlattenExtension`

:::
