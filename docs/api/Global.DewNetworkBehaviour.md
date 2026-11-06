# Class: DewNetworkBehaviour

- **Category:** <span class="cat-dot" style="--cat-color: #22c55e" data-cat="Actors & Entities"></span> Actors & Entities
- **Namespace:** `Global`
- **Assembly:** `Dew.Core.dll`
- **Inheritance / Derived:** [Actor](/api/Global.Actor) → [DewAllHeroesPresentZone](/api/Global.DewAllHeroesPresentZone) → [DewCutsceneDirector](/api/Global.DewCutsceneDirector) → [DewPlayer](/api/Global.DewPlayer) → [EntityComponent](/api/Global.EntityComponent) → [EntityTransformSync](/api/Global.EntityTransformSync) → [GenericTransformSync](/api/Global.GenericTransformSync) → `NetworkedManagerBase<T>` → [Room_Barrier](/api/Global.Room_Barrier) → [Room_Shortcut](/api/Global.Room_Shortcut) → [Room_Trap_ActivatorBase](/api/Global.Room_Trap_ActivatorBase) → [Room_Waypoint](/api/Global.Room_Waypoint) → [RoomComponent](/api/Global.RoomComponent) → `SingletonDewNetworkBehaviour<T>`

```csharp
public class DewNetworkBehaviour : NetworkBehaviour, ILogicUpdate
```

## Methods (34)

::: details `Awake()`

```csharp
protected virtual void Awake()
```

:::

::: details `FrameUpdate()`

```csharp
public virtual void FrameUpdate()
```

:::

::: details `FxApplySpeedMultiplier(GameObject, float)`

Change speed of an effect, affecting ParticleSystems and IEffectWithSpeed inheritors.

```csharp
public void FxApplySpeedMultiplier(GameObject effect, float multiplier)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `effect` | `UnityEngine.GameObject` |  |
| `multiplier` | `float` |  |

:::

::: details `FxApplySpeedMultiplierNetworked(GameObject, float)`

Change speed of an effect, affecting ParticleSystems and IEffectWithSpeed inheritors.

```csharp
public void FxApplySpeedMultiplierNetworked(GameObject effect, float multiplier)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `effect` | `UnityEngine.GameObject` |  |
| `multiplier` | `float` |  |

:::

::: details `FxPlay(GameObject, Entity, Vector3, Quaternion?)`

Play effect locally attached to given entity, positioned.

```csharp
public void FxPlay(GameObject effect, Entity attach, Vector3 position, Quaternion? rotation)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `effect` | `UnityEngine.GameObject` |  |
| `attach` | [`Entity`](/api/Global.Entity) |  |
| `position` | `UnityEngine.Vector3` |  |
| `rotation` | `UnityEngine.Quaternion?` |  |

:::

::: details `FxPlay(GameObject, Entity)`

Play effect locally attached to given entity.

```csharp
public void FxPlay(GameObject effect, Entity attach)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `effect` | `UnityEngine.GameObject` |  |
| `attach` | [`Entity`](/api/Global.Entity) |  |

:::

::: details `FxPlay(GameObject, Vector3, Quaternion?)`

Play effect locally at given position.

```csharp
public void FxPlay(GameObject effect, Vector3 position, Quaternion? rotation)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `effect` | `UnityEngine.GameObject` |  |
| `position` | `UnityEngine.Vector3` |  |
| `rotation` | `UnityEngine.Quaternion?` |  |

:::

::: details `FxPlay(GameObject)`

Play effect locally.

```csharp
public void FxPlay(GameObject effect)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `effect` | `UnityEngine.GameObject` |  |

:::

::: details `FxPlayNetworked(GameObject, Entity, Vector3, Quaternion?)`

Play effect everywhere attached to given entity, positioned. Only callable in server.

```csharp
public void FxPlayNetworked(GameObject effect, Entity entity, Vector3 position, Quaternion? rotation)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `effect` | `UnityEngine.GameObject` |  |
| `entity` | [`Entity`](/api/Global.Entity) |  |
| `position` | `UnityEngine.Vector3` |  |
| `rotation` | `UnityEngine.Quaternion?` |  |

:::

::: details `FxPlayNetworked(GameObject, Entity)`

Play effect everywhere attached to given entity. Only callable in server.

```csharp
public void FxPlayNetworked(GameObject effect, Entity entity)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `effect` | `UnityEngine.GameObject` |  |
| `entity` | [`Entity`](/api/Global.Entity) |  |

:::

::: details `FxPlayNetworked(GameObject, Vector3, Quaternion?)`

Play effect everywhere. Only callable in server.

```csharp
public void FxPlayNetworked(GameObject effect, Vector3 position, Quaternion? rotation)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `effect` | `UnityEngine.GameObject` |  |
| `position` | `UnityEngine.Vector3` |  |
| `rotation` | `UnityEngine.Quaternion?` |  |

:::

::: details `FxPlayNetworked(GameObject)`

Play effect everywhere. Only callable in server.

```csharp
public void FxPlayNetworked(GameObject effect)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `effect` | `UnityEngine.GameObject` |  |

:::

::: details `FxPlayNew(GameObject, Entity, Vector3, Quaternion?)`

Instantiate and play effect locally attached to given entity, positioned.

```csharp
public void FxPlayNew(GameObject effect, Entity attach, Vector3 position, Quaternion? rotation)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `effect` | `UnityEngine.GameObject` |  |
| `attach` | [`Entity`](/api/Global.Entity) |  |
| `position` | `UnityEngine.Vector3` |  |
| `rotation` | `UnityEngine.Quaternion?` |  |

:::

::: details `FxPlayNew(GameObject, Entity)`

Instantiate and play effect locally attached to given entity.

```csharp
public void FxPlayNew(GameObject effect, Entity attach)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `effect` | `UnityEngine.GameObject` |  |
| `attach` | [`Entity`](/api/Global.Entity) |  |

:::

::: details `FxPlayNew(GameObject, Vector3, Quaternion?)`

Instantiate and play effect locally at given position.

```csharp
public void FxPlayNew(GameObject effect, Vector3 position, Quaternion? rotation)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `effect` | `UnityEngine.GameObject` |  |
| `position` | `UnityEngine.Vector3` |  |
| `rotation` | `UnityEngine.Quaternion?` |  |

:::

::: details `FxPlayNew(GameObject)`

Instantiate and play effect locally.

```csharp
public void FxPlayNew(GameObject effect)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `effect` | `UnityEngine.GameObject` |  |

:::

::: details `FxPlayNewNetworked(GameObject, Entity, Vector3, Quaternion?)`

Instantiate and play effect everywhere attached to given entity, positioned. Only callable in server.

```csharp
public void FxPlayNewNetworked(GameObject effect, Entity entity, Vector3 position, Quaternion? rotation)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `effect` | `UnityEngine.GameObject` |  |
| `entity` | [`Entity`](/api/Global.Entity) |  |
| `position` | `UnityEngine.Vector3` |  |
| `rotation` | `UnityEngine.Quaternion?` |  |

:::

::: details `FxPlayNewNetworked(GameObject, Entity)`

Instantiate and play effect everywhere attached to given entity. Only callable in server.

```csharp
public void FxPlayNewNetworked(GameObject effect, Entity entity)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `effect` | `UnityEngine.GameObject` |  |
| `entity` | [`Entity`](/api/Global.Entity) |  |

:::

::: details `FxPlayNewNetworked(GameObject, Vector3, Quaternion?)`

Instantiate and play effect everywhere at given position. Only callable in server.

```csharp
public void FxPlayNewNetworked(GameObject effect, Vector3 position, Quaternion? rotation)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `effect` | `UnityEngine.GameObject` |  |
| `position` | `UnityEngine.Vector3` |  |
| `rotation` | `UnityEngine.Quaternion?` |  |

:::

::: details `FxPlayNewNetworked(GameObject)`

Instantiate and play effect everywhere. Only callable in server.

```csharp
public void FxPlayNewNetworked(GameObject effect)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `effect` | `UnityEngine.GameObject` |  |

:::

::: details `FxStop(GameObject)`

Stop effect locally.

```csharp
public void FxStop(GameObject effect)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `effect` | `UnityEngine.GameObject` |  |

:::

::: details `FxStopNetworked(GameObject)`

Stop effect everywhere. Only callable in server. Use non-networked variant in DewEffect if you want to stop effect locally.

```csharp
public void FxStopNetworked(GameObject effect)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `effect` | `UnityEngine.GameObject` |  |

:::

::: details `GetComponent&lt;T&gt;(out T)`

```csharp
protected void GetComponent<T>(out T comp)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `comp` | `T` |  |
| `` | `T` |  |

:::

::: details `InvalidateInstance()`

Invalidate an instance from pool, preventing it from being reused.

```csharp
public void InvalidateInstance()
```

:::

::: details `LogicUpdate(float)`

```csharp
public virtual void LogicUpdate(float dt)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `dt` | `float` |  |

:::

::: details `OnDestroy()`

```csharp
protected virtual void OnDestroy()
```

:::

::: details `OnLateStart()`

```csharp
public virtual void OnLateStart()
```

:::

::: details `OnLateStartServer()`

```csharp
public virtual void OnLateStartServer()
```

:::

::: details `OnStart()`

```csharp
public virtual void OnStart()
```

:::

::: details `OnStartClient()`

```csharp
public override void OnStartClient()
```

:::

::: details `OnStartServer()`

```csharp
public override void OnStartServer()
```

:::

::: details `OnStop()`

```csharp
public virtual void OnStop()
```

:::

::: details `OnStopClient()`

```csharp
public override void OnStopClient()
```

:::

::: details `OnStopServer()`

```csharp
public override void OnStopServer()
```

:::


## Architecture & Relationships

::: details Click to expand Architecture & Relationships

### Used By (459)

*Classes and systems that invoke, reference, or depend on `DewNetworkBehaviour`:*

[AbilityInstance](/api/Global.AbilityInstance) · [AbilityTrigger](/api/Global.AbilityTrigger) · [Actor](/api/Global.Actor) · [ActorManager](/api/Global.ActorManager) · `ActorTransformSync` · `Ai_Ai_Mon_Ink_BossWhiteNight_OneInchPunch_Atk` · `Ai_ArcticTerritory` · `Ai_C_BackStep_Bomb` · `Ai_C_BeamOfLight` · `Ai_C_DarkBolt` · `Ai_C_DarkSpear` · `Ai_C_FlashFreeze` · `Ai_C_IceBlock_Projectile` · `Ai_C_MassProtection` · `Ai_C_PressurePoint` · `Ai_Culinary_Pickup` · `Ai_Curse_AnchorOfMind_Anchor` · `Ai_D_BurningFist_Attack` · `Ai_D_ExoticMatter_Projectile` · `Ai_D_Resolve_Push` · `Ai_E_Blink` · `Ai_E_Blink_Back` · `Ai_E_ChainLightning` · `Ai_E_CrimsonLance` · `Ai_E_FlameJet_Projectile` · `Ai_E_JusticeGuillotine` · `Ai_E_MassCleanse` · `Ai_E_MysticDagger` · `Ai_E_SearingCharge` · `Ai_E_SliceThroat` · `Ai_E_StygianRush_Rush` · `Ai_Gem_C_Charcoal_Projectile` · `Ai_Gem_C_Void_Explosion` · `Ai_Gem_E_Domination_CritGainEffect` · `Ai_Gem_R_Blade` · `Ai_Gem_R_Shock_Lightning` · `Ai_Gem_U_LastStarlight` · `Ai_Hatred_Curse` · `Ai_Hatred_InkMapCurse` · `Ai_L_Blizzard_Instance` · `Ai_L_BloodStrike_Meat` · `Ai_L_SmallMoltenCore_Dragon_Atk` · `Ai_MiniBoss_IceAura_AoE` · `Ai_MiniBoss_OrbSpitter_Orb` · `Ai_Mon_DarkCave_BossSeeker_GreenChaserOrb_Explode` · `Ai_Mon_DarkCave_BossSeeker_PurpleOrb` · `Ai_Mon_DarkCave_BossSeeker_PurpleOrb_Instance` · `Ai_Mon_DarkCave_BossSeeker_TunnelVision_SecondPoolAtk` · `Ai_Mon_DarkCave_BossSeeker_YellowDiagram_MainInstance` · `Ai_Mon_DarkCave_BossSeeker_YellowDiagram_SubInstance` · `Ai_Mon_DarkCave_CaveBat_Dash` · `Ai_Mon_DarkCave_DarkElemental_Barrage_Arrow` · `Ai_Mon_DarkCave_NightOlm_Atk_Projectile` · `Ai_Mon_Despair_BossAzurak_DoubleStomp` · `Ai_Mon_Despair_BossAzurak_DoubleStomp_Instance` · `Ai_Mon_Despair_BossAzurak_RoarAtk` · `Ai_Mon_Despair_BossAzurak_Roll` · `Ai_Mon_Despair_BossAzurak_StompBlock` · `Ai_Mon_Despair_BossAzurak_StompBlock_Artillery` · `Ai_Mon_Despair_BossAzurak_StompGlobal` · `Ai_Mon_Despair_BossAzurak_StompProjectile` · `Ai_Mon_Despair_BossAzurak_StompProjectile_FirstAtk` · `Ai_Mon_Despair_DreadBug_Jump` · `Ai_Mon_Despair_DreadBug_JumpBack` · `Ai_Mon_Despair_WretchedArtillery_BarrageAtk_Missile` · `Ai_Mon_Forest_BossDemon_AltSkill_LineAtk` · `Ai_Mon_Forest_BossDemon_AltSkill_Stomp` · `Ai_Mon_Forest_BossDemon_AltSkill_Stomp_Tree` · `Ai_Mon_Forest_BossDemon_DelayedAtk` · `Ai_Mon_Forest_BossDemon_SpecialAtk` · `Ai_Mon_Forest_Hound_Charge` · `Ai_Mon_Forest_SpiderSpitter_Backdash` · `Ai_Mon_Forest_SpiderWarrior_Jump` · `Ai_Mon_Ink_Archer_Atk` · `Ai_Mon_Ink_BossDarkMoon_AltAtk_Spawner` · `Ai_Mon_Ink_BossDarkMoon_Blade` · `Ai_Mon_Ink_BossDarkMoon_Eclipse` · `Ai_Mon_Ink_BossDarkMoon_Hammer` · `Ai_Mon_Ink_BossDarkMoon_ShortDash` · `Ai_Mon_Ink_BossDarkMoon_SpawnEgoSword` · `Ai_Mon_Ink_BossDarkMoon_SpawnEgoSword_Projectile` · `Ai_Mon_Ink_BossDarkMoon_Spear` · `Ai_Mon_Ink_BossDarkMoon_Spear_Instance` · `Ai_Mon_Ink_BossDarkMoon_TeleportAtk` · `Ai_Mon_Ink_BossDarkMoon_TeleportDash` · `Ai_Mon_Ink_BossDarkMoon_ThrowSpear_Projectile` · `Ai_Mon_Ink_BossDarkMoon_ThrowSpear_Spawner` · `Ai_Mon_Ink_BossDarkMoon_ThrowSpear_TeleportAtk_AfterAtk` · `Ai_Mon_Ink_BossWhiteNight_AltAtk` · `Ai_Mon_Ink_BossWhiteNight_AltAtk_Ready` · `Ai_Mon_Ink_BossWhiteNight_Cataclysm` · `Ai_Mon_Ink_BossWhiteNight_Cataclysm_Eclipse` · `Ai_Mon_Ink_BossWhiteNight_Cataclysm_SafeZone` · `Ai_Mon_Ink_BossWhiteNight_DestructionWave_Wave` · `Ai_Mon_Ink_BossWhiteNight_Oppression` · `Ai_Mon_Ink_BossWhiteNight_RageInstance_Rock` · `Ai_Mon_Ink_DivineAnimal_Bite` · `Ai_Mon_Ink_GhostSpear_Atk` · `Ai_Mon_LavaLand_BossInfernus_BreathFire_Projectile` · `Ai_Mon_LavaLand_BossInfernus_PowerBomb_FlamePillar` · `Ai_Mon_LavaLand_BossInfernus_Roar_Projectile` · `Ai_Mon_LavaLand_FireElemental_BackDash` · `Ai_Mon_LavaLand_FireElemental_Destruct` · `Ai_Mon_LavaLand_FireElemental_DestructSub` · `Ai_Mon_LavaLand_FireElemental_ExplosionSub` · `Ai_Mon_LavaLand_FireElemental_LaserAtk` · `Ai_Mon_LavaLand_Magmadon_Charge_Projectile` · `Ai_Mon_LavaLand_SuperheatedWolf_SelfDestruct` · `Ai_Mon_Polaris_Smite` · `Ai_Mon_Primus_BossPrimusAeron_Adapt_Arbalest` · `Ai_Mon_Primus_BossPrimusAeron_Adapt_Atk` · `Ai_Mon_Primus_BossPrimusAeron_Adapt_IceClaw` · `Ai_Mon_Primus_BossPrimusAeron_Dash` · `Ai_Mon_Primus_BossPrimusAeron_Force_DropGiantSword` · `Ai_Mon_Primus_BossPrimusAeron_Force_Grab` · `Ai_Mon_Primus_BossPrimusAeron_Rage_Atk` · `Ai_Mon_Primus_BossPrimusAeron_Rage_MassDelusion` · `Ai_Mon_Sky_Baam_Teleport` · `Ai_Mon_Sky_Baam_TeleportSequence` · `Ai_Mon_Sky_BigBaam_BeamAtk` · `Ai_Mon_Sky_BossNyx_Blackhole` · `Ai_Mon_Sky_BossNyx_LaserAtk_Instance` · `Ai_Mon_Sky_BossNyx_LineAtk` · `Ai_Mon_Sky_BossNyx_PillarOfStars` · `Ai_Mon_Sky_BossNyx_StellarDash` · `Ai_Mon_Sky_LittleBaam_Atk` · `Ai_Mon_SnowMountain_BossSkoll_Atk` · `Ai_Mon_SnowMountain_BossSkoll_AuraBladeRain` · `Ai_Mon_SnowMountain_BossSkoll_AuraBladeRain_Instance` · `Ai_Mon_SnowMountain_BossSkoll_AuraExplosion_Spawner` · `Ai_Mon_SnowMountain_BossSkoll_SummonArrow_Instance` · `Ai_Mon_SnowMountain_LivingShards_Atk` · `Ai_Mon_SnowMountain_Scavenger_Jump` · `Ai_Mon_SnowMountain_VikingWarrior_Sword` · `Ai_Mon_Special_BossErebos_AntiGravity_Instance` · `Ai_Mon_Special_BossErebos_AntiGravity_Spawner` · `Ai_Mon_Special_BossErebos_Gaze_Instance` · `Ai_Mon_Special_BossErebos_Meteor` · `Ai_Mon_Special_BossErebos_SpawnBlackhole_Instance` · `Ai_Mon_Special_BossErebos_SpawnTormentor_Attacker` · `Ai_Mon_Special_BossErebos_SpawnTormentor_Attacker_Instance` · `Ai_Mon_Special_BossErebos_SpawnTormentor_Slow` · `Ai_Mon_Special_BossErebos_StarRain_Instance` · `Ai_Mon_Special_BossErebos_StarRain_Spawner` · `Ai_Mon_Special_BossLightElemental_Beam` · `Ai_Mon_Special_BossLightElemental_BeamAtk_Spawner` · `Ai_Mon_Special_BossLightElemental_BeamBarrage` · `Ai_Mon_Special_BossMaw_AnnihilationStance` · `Ai_Mon_Special_BossMaw_Atk` · `Ai_Mon_Special_BossMaw_Cataclysm_Spawner` · `Ai_Mon_Special_BossMaw_ChainReaction` · `Ai_Mon_Special_BossMaw_ChainReaction_Instance` · `Ai_Mon_Special_BossMaw_MoonlightPact` · `Ai_Mon_Special_BossMaw_PillarOfFlame_Projectile` · `Ai_Mon_Special_BossMaw_PrecisionShot` · `Ai_Mon_Special_BossMaw_Purgatory_Trap` · `Ai_Mon_Special_BossMaw_ScatterShot_Spawner` · `Ai_Mon_Special_BossMaw_ShadowOverdrive_Projectile` · `Ai_Mon_Special_BossMaw_SliceThroat` · `Ai_Mon_Special_BossMaw_SliceThroat_Atk` · `Ai_Mon_Special_BossObliviax_Artillery` · `Ai_Mon_Special_BossObliviax_Artillery_Instance` · `Ai_Mon_Special_BossObliviax_ChargeSequence_MissileAtk` · `Ai_Mon_Special_BossObliviax_DashAtk` · `Ai_Mon_Special_BossPolaris_Holy_Atk_Spawner` · `Ai_Mon_Special_BossPolaris_Holy_Summon` · `Ai_Mon_Special_BossPolaris_Monster_Atk_FirstAtk` · `Ai_Mon_Special_BossPolaris_Monster_Scream` · `Ai_QR_DistortedMind_Spawner` · `Ai_Q_BigBorealChunk_Spawner` · `Ai_Q_CruelSun_Shockwave` · `Ai_Q_DeathMark_Projectile` · `Ai_Q_Discipline_Stomp` · `Ai_Q_EmbracingTheChill_AreaDoT` · `Ai_Q_EtherealInfluence` · `Ai_Q_Fleche_Dash` · `Ai_Q_HandCannon` · `Ai_Q_IncendiaryRounds_Attack` · `Ai_Q_Laceration_Circle` · `Ai_Q_Lunge` · `Ai_Q_SuperNova` · `Ai_R_BlackArbalest` · `Ai_R_ChainReaction` · `Ai_R_Chomp` · `Ai_R_DarkGrenade_Shard` · `Ai_R_DarkGrenade_ShardSpawner` · `Ai_R_Ignite` · `Ai_R_NaturesWhisper` · `Ai_R_Scattershot_Projectile` · `Ai_R_Scattershot_Spawner` · `Ai_R_ShadowOverdrive_Projectile` · `Ai_R_ShadowWalk_Projectile` · `Ai_R_StaticDischarge` · `Ai_Shrine_SmallSoul_Attack` · `Ai_Sky_BossIntruder_Instance` · `Ai_Star_Aurena_F_CR_ChargedCast_InstanceCharger` · `Ai_Star_Bismuth_F_IT_SmallerRingAddDisplacement_Dash` · `Ai_Star_Cetus_F_BA_LightningEcho_Lightning` · `Ai_Star_Cetus_F_BI_SelfDamageAoeCold_AOE` · `Ai_U_BeamOfBalance_Beam` · `Ai_U_BigChomp` · `Ai_U_Hysteria_Claw` · `Ai_U_WorldCracker` · `Ai_UnstableRatSwarm_Projectile` · `Ai_VeilOfDark` · [Artifact](/api/Global.Artifact) · `At_Mon_Ink_BossWhiteNight_OneInchPunch` · `At_Mon_Sky_StarSeed_Atk` · `BossLightElementalKillBehavior` · `BossSeekerKillBehavior` · [ChatManager](/api/Global.ChatManager) · [ClientEventManager](/api/Global.ClientEventManager) · [ConsoleManager](/api/Global.ConsoleManager) · [ConversationManager](/api/Global.ConversationManager) · [DamageInstance](/api/Global.DamageInstance) · `DarkCave_RandomOpenBarrier` · `Despair_FogPositionController` · [DevGameManager](/api/Global.DevGameManager) · [DewAllHeroesPresentZone](/api/Global.DewAllHeroesPresentZone) · [DewCutsceneDirector](/api/Global.DewCutsceneDirector) · [DewPlayer](/api/Global.DewPlayer) · [EditSkillShrine](/api/Global.EditSkillShrine) · [EntityAI](/api/Global.EntityAI) · [EntityAbility](/api/Global.EntityAbility) · [EntityAnimation](/api/Global.EntityAnimation) · [EntityComponent](/api/Global.EntityComponent) · [EntityControl](/api/Global.EntityControl) · [EntitySound](/api/Global.EntitySound) · [EntityStatus](/api/Global.EntityStatus) · [EntityTransformSync](/api/Global.EntityTransformSync) · [EntityVisual](/api/Global.EntityVisual) · [FlavourManager](/api/Global.FlavourManager) · `Forest_Fireplace` · [GameEffect](/api/Global.GameEffect) · [GameManager](/api/Global.GameManager) · [GameResultManager](/api/Global.GameResultManager) · [GameSettingsManager](/api/Global.GameSettingsManager) · `Gem_C_Confidence` · `Gem_C_Responsibility` · `Gem_C_Shatter` · `Gem_C_Sulfur` · `Gem_C_Talc` · `Gem_C_Vengeance` · `Gem_E_Blossom` · `Gem_E_Clemency` · `Gem_E_Crimson` · `Gem_E_Domination` · `Gem_E_Fangs` · `Gem_E_Flexibility` · `Gem_E_Insight` · `Gem_E_Metal` · `Gem_E_Omega` · `Gem_E_Opportunity` · `Gem_E_Overload` · `Gem_E_Pain` · `Gem_E_Thunder` · `Gem_E_Umbra` · `Gem_L_CamillasGift` · `Gem_L_Embertail` · `Gem_L_HeartOfGold` · `Gem_L_Paranoia` · `Gem_L_PureWhite` · `Gem_L_SolarEye` · `Gem_L_Supersymmetry` · `Gem_R_Abyss` · `Gem_R_Accuracy` · `Gem_R_Bleak` · `Gem_R_Blood` · `Gem_R_Celestial` · `Gem_R_Crucible` · `Gem_R_Epiphany` · `Gem_R_Flow` · `Gem_R_Glass` · `Gem_R_Lightweight` · `Gem_R_Mortality` · `Gem_R_Purity` · `Gem_R_Rigidity` · `Gem_R_Shock` · `Gem_R_Slippery` · `Gem_U_GuidingCompass_NotCharged` · `Gem_U_LastStarlight` · [GenericTransformSync](/api/Global.GenericTransformSync) · [Hero](/api/Global.Hero) · [HeroSkill](/api/Global.HeroSkill) · `Hero_Aurena` · `Hero_Bismuth_BookController` · `Hero_Husk` · `Ink_BossRoomDamageGround` · `Ink_BossSelector` · `Ink_CraneSpawner` · `Ink_SecondCutscenePlay` · `LavaLand_Lava` · [LootManager](/api/Global.LootManager) · `LucidDream_TheDarkestUrge` · [MeleeAttackInstance](/api/Global.MeleeAttackInstance) · `Mon_DarkCave_CaveSpider` · `Mon_DarkCave_NightOlm` · `Mon_Despair_AzurakMonsterSpawner` · `Mon_Ink_BossDarkMoon` · `Mon_Ink_BossWhiteNight` · `Mon_Primus_BossPrimusAeron` · `Mon_Special_AmbushSpawner` · `Mon_Special_BossErebos` · [NetworkedManagerBase`1](/api/Global.NetworkedManagerBase`1) · [PickupInstance](/api/Global.PickupInstance) · [PickupManager](/api/Global.PickupManager) · [PingManager](/api/Global.PingManager) · [PlayGameManager](/api/Global.PlayGameManager) · `PlayTutorialManager` · `Primus_Ending` · `Primus_Pizza0` · [Projectile](/api/Global.Projectile) · [PropEnt_Merchant_Base](/api/Global.PropEnt_Merchant_Base) · [QuestManager](/api/Global.QuestManager) · `Quest_HuntedByObliviax` · [Rift](/api/Global.Rift) · [Rift_Sidetrack](/api/Global.Rift_Sidetrack) · [Room](/api/Global.Room) · [RoomComponent](/api/Global.RoomComponent) · [RoomMap](/api/Global.RoomMap) · `RoomMod_Ambush` · [RoomModifierBase](/api/Global.RoomModifierBase) · [Room_Barrier](/api/Global.Room_Barrier) · [Room_Shortcut](/api/Global.Room_Shortcut) · [Room_Trap_ActivatorBase](/api/Global.Room_Trap_ActivatorBase) · [Room_Trap_CyclicActivator](/api/Global.Room_Trap_CyclicActivator) · [Room_Trap_ProximityActivator](/api/Global.Room_Trap_ProximityActivator) · [Room_Trap_Toggleable](/api/Global.Room_Trap_Toggleable) · [Room_Waypoint](/api/Global.Room_Waypoint) · `RotateCircle` · `Se_C_CorrosiveTrails_Poisoned` · `Se_C_IceBlock` · `Se_Curse_Electrified` · `Se_Curse_FateOfGreed` · `Se_Curse_UnstableEnergy` · `Se_Curse_VainDream` · `Se_D_AstridsMasterpieceEnGarde` · `Se_D_AstridsMasterpiecePriorite` · `Se_D_AstridsMasterpiecePriorite_Exposed` · `Se_D_BeautifulThreat` · `Se_D_ChargedAnguillian` · `Se_D_ConvergencePoint` · `Se_D_DoubleTap` · `Se_D_MercyOfEl` · `Se_D_QuartetOfDeath_Buff` · `Se_D_QuartetOfDeath_DeathMark` · `Se_E_Harvest_OnVictim` · `Se_E_LizardlyBlessing` · `Se_E_Rewind` · `Se_EngulfedInFlame` · `Se_FallenStar_MonsterReinforcement` · `Se_FatalHitProtection_Invulnerable` · `Se_Gem_L_Liberty_Buff` · `Se_Gem_R_Control_Debuff` · `Se_Gem_R_Hedgehog_Aura` · `Se_Gem_R_Wound_Wounded` · `Se_GenericHealOverTime` · `Se_GenericShield_Stacking` · `Se_GenericStealth` · `Se_GoldEverywhere` · `Se_HealthCost` · `Se_HeroKnockedOut` · `Se_L_MentalCorruption` · `Se_L_PyranasFireball` · `Se_LimboBossDecorator` · `Se_M_Charge` · `Se_MiniBoss_BloodThorn` · `Se_MiniBoss_BloodThorn_Bleeding` · `Se_MiniBoss_OrbSpitter` · `Se_MiniBoss_SpinningArrow` · `Se_MiniBoss_UnstableExplosive_Explosion` · `Se_MirageSkin_Delusion` · `Se_MirageSkin_Oppression` · `Se_MirageSkin_Pulverization` · `Se_MirageSkin_Sanctification_Protected` · `Se_Mon_DarkCave_BossSeeker_Substitution` · `Se_Mon_Despair_BossAzurak_Hide` · `Se_Mon_Ink_BossWhiteNight_Rush` · `Se_Mon_Ink_Boss_PhaseChange` · `Se_Mon_Sky_BossNyx_IntrudeErebos` · `Se_Mon_SnowMountain_VikingWarrior_DmgReducer` · `Se_Mon_Special_BossErebos_PhaseChange` · `Se_Mon_Special_BossPolaris_Holy_CounterSpell` · `Se_Mon_Special_BossPolaris_Holy_ShortInvul` · `Se_PortalTransition` · `Se_PureDream` · `Se_Q_Fleche_VictimTracker` · `Se_R_AnnihilationStance` · `Se_R_BoneCrusher` · `Se_R_DangerousTheory` · `Se_R_Parry_Start` · `Se_R_RepulsiveShield` · `Se_R_SerpentineBlessing_Buff` · `Se_R_ShadowOverdrive_Initial` · `Se_R_UnbreakableDetermination` · `Se_Shrine_Despair_Teleport` · `Se_Shrine_SmallSoul` · `Se_Star_Aurena_I_GoldOnMerchantDamage` · `Se_Star_Aurena_L_ShareHeal` · `Se_Star_Husk_I_ShopIntimidation` · `Se_Star_Husk_L_DodgeChargesAndRangeWithPenalty` · `Se_Star_I_GoldPerCrit` · `Se_Star_I_GoldRiskAndReturn` · `Se_Star_Lacerta_F_HC_NearDamage` · `Se_Star_Lacerta_F_HC_NoDelayDoubleCast` · `Se_Star_Lacerta_F_HC_ResetOnDodge` · `Se_Star_Nachia_F_MP_NoJump` · `Se_Star_Nachia_F_SC_SummonDmgReduction` · `Se_Treasure_FragmentOfDetermination_Invulnerable` · `Se_U_EternalFlame_Curse` · `Se_U_HerWorld_Blackhole` · `Se_WaypointTeleport` · [Shrine](/api/Global.Shrine) · `Shrine_BossSoul` · `Shrine_CallOfTheRavenous` · `Shrine_Chaos` · `Shrine_CookingPot` · `Shrine_CorruptedChaos` · `Shrine_Destiny` · `Shrine_FallenStar` · `Shrine_Guidance` · `Shrine_HeroSoul` · `Shrine_HiddenStash` · `Shrine_LoopCat` · `Shrine_Luck` · `Shrine_MirrorOfRemorse` · `Shrine_Se_Star_Bismuth_I_KnowledgeBook_Book` · `Shrine_TheConsortOfNight_Rift` · [SingletonDewNetworkBehaviour`1](/api/Global.SingletonDewNetworkBehaviour`1) · [SkillTrigger](/api/Global.SkillTrigger) · `SkyNightFishProp` · `Sky_BossIntruder` · `Sky_LightFogDamager` · `SnowMountain_OpenSecretPlace` · `SnowMountain_SecretPlaceTriggerInstance` · `SpawnGemStarProp` · `St_D_CircleOfLife` · `St_D_DisintegratingClaw` · `St_D_ExplosionArtist` · `St_D_IcyVeins` · `St_D_MercyOfEl` · `St_D_QuartetOfDeath` · `St_D_Resolve` · `St_D_SalamanderPowder` · `St_L_HerosReturn` · `St_L_SmallMoltenCore` · `St_Q_Fleche` · `St_Q_Laceration` · `St_U_ShoutOfOblivion` · `StarlessPath_BossPolarisManager` · [StatusEffect](/api/Global.StatusEffect) · `Sum_R_AnnoyingBanner` · [TickDamageInstance](/api/Global.TickDamageInstance) · [TimescaleManager](/api/Global.TimescaleManager) · `Trap_FlameJet` · `Trap_UnstableMushroom` · `UI_InGame_Map` · `UI_InGame_Map_Item_NetBehaviour` · [ZoneManager](/api/Global.ZoneManager)

### Dependencies (8)

*Types and components that `DewNetworkBehaviour` references or depends upon:*

[Dew](/api/Global.Dew) · [DewEffect](/api/Global.DewEffect) · [DewNetworkManager](/api/Global.DewNetworkManager) · [Entity](/api/Global.Entity) · [ILogicUpdate](/api/Global.ILogicUpdate) · [LogicUpdateManager](/api/Global.LogicUpdateManager) · [SafeAction`1](/api/Global.SafeAction`1) · [SpawnManager](/api/Global.SpawnManager)

:::
