# Class: Entity

- **Category:** <span class="cat-dot" style="--cat-color: #ef4444" data-cat="Combat & Abilities"></span> Combat & Abilities
- **Namespace:** `Global`
- **Assembly:** `Dew.Core.dll`
- **Attributes:** `[LogicUpdatePriority] [RequireComponent] [RequireComponent] [RequireComponent] [RequireComponent] [RequireComponent] [RequireComponent] [RequireComponent]`
- **Inheritance / Derived:** [DewNetworkBehaviour](/api/Global.DewNetworkBehaviour) → [Actor](/api/Global.Actor) → [Hero](/api/Global.Hero) → [MockEntity](/api/Global.MockEntity) → [Monster](/api/Global.Monster) → [PropEntity](/api/Global.PropEntity) → [Summon](/api/Global.Summon)

```csharp
[LogicUpdatePriority(-400)]
[RequireComponent(typeof(EntityAI))]
[RequireComponent(typeof(EntityAnimation))]
[RequireComponent(typeof(EntityControl))]
[RequireComponent(typeof(EntityStatus))]
[RequireComponent(typeof(EntityVisual))]
[RequireComponent(typeof(EntityAbility))]
[RequireComponent(typeof(EntitySound))]
public class Entity : Actor, ILogicUpdate, ICleanup, ICustomDestroyRoutine
```

## Fields (24)

::: details Click to expand Fields (24)

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`ClientEntityEvent_OnIsSleepingChanged`** | `public SafeAction<bool> ClientEntityEvent_OnIsSleepingChanged` |  |
| **`ClientEntityEvent_OnStatusEffectAdded`** | `public SafeAction<EventInfoStatusEffect> ClientEntityEvent_OnStatusEffectAdded` |  |
| **`ClientEntityEvent_OnStatusEffectRemoved`** | `public SafeAction<EventInfoStatusEffect> ClientEntityEvent_OnStatusEffectRemoved` |  |
| **`EntityEvent_OnAttackDodged`** | `public SafeAction<EventInfoAttackMissed> EntityEvent_OnAttackDodged` |  |
| **`EntityEvent_OnAttackEffectTriggered`** | `public SafeAction<EventInfoAttackEffect> EntityEvent_OnAttackEffectTriggered` |  |
| **`EntityEvent_OnAttackFired`** | `public SafeAction<EventInfoAttackFired> EntityEvent_OnAttackFired` |  |
| **`EntityEvent_OnAttackFiredBeforePrepare`** | `public SafeAction<EventInfoAttackFired> EntityEvent_OnAttackFiredBeforePrepare` |  |
| **`EntityEvent_OnAttackHit`** | `public SafeAction<EventInfoAttackHit> EntityEvent_OnAttackHit` |  |
| **`EntityEvent_OnAttackMissed`** | `public SafeAction<EventInfoAttackMissed> EntityEvent_OnAttackMissed` |  |
| **`EntityEvent_OnAttackTaken`** | `public SafeAction<EventInfoAttackHit> EntityEvent_OnAttackTaken` |  |
| **`EntityEvent_OnCastComplete`** | `public SafeAction<EventInfoCast> EntityEvent_OnCastComplete` |  |
| **`EntityEvent_OnCastCompleteBeforePrepare`** | `public SafeAction<EventInfoCast> EntityEvent_OnCastCompleteBeforePrepare` |  |
| **`EntityEvent_OnDamageNegatedByImmunity`** | `public SafeAction<EventInfoDamageNegatedByImmunity> EntityEvent_OnDamageNegatedByImmunity` |  |
| **`EntityEvent_OnDamageNegatedByShield`** | `public SafeAction<EventInfoDamageNegatedByShield> EntityEvent_OnDamageNegatedByShield` |  |
| **`EntityEvent_OnDeath`** | `public SafeAction<EventInfoKill> EntityEvent_OnDeath` |  |
| **`EntityEvent_OnGetManaSpent`** | `public SafeAction<EventInfoSpentMana> EntityEvent_OnGetManaSpent` |  |
| **`EntityEvent_OnTakeDamage`** | `public SafeAction<EventInfoDamage> EntityEvent_OnTakeDamage` |  |
| **`EntityEvent_OnTakeHeal`** | `public SafeAction<EventInfoHeal> EntityEvent_OnTakeHeal` |  |
| **`EntityEvent_OnTakeManaHeal`** | `public SafeAction<EventInfoHeal> EntityEvent_OnTakeManaHeal` |  |
| **`EntityEvent_OnTakeShield`** | `public SafeAction<EventInfoShield> EntityEvent_OnTakeShield` |  |
| **`takenDamageProcessor`** | `public DataProcessorGroup<DamageData, Actor, Entity> takenDamageProcessor` | Processor for all received damages (Except pure damage). This is only valid on server. |
| **`takenHealProcessor`** | `public DataProcessorGroup<HealData, Actor, Entity> takenHealProcessor` | Processor for received heals. This is only valid on server. |
| **`takenManaHealProcessor`** | `public DataProcessorGroup<HealData, Actor, Entity> takenManaHealProcessor` | Processor for received mana heals. This is only valid on server. |
| **`takenShieldProcessor`** | `public DataProcessorGroup<HealData, Actor, Entity> takenShieldProcessor` | Processor for received shields. This is only valid on server. |

:::

## Properties (22)

::: details Click to expand Properties (22)

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`Ability`** | `public EntityAbility Ability { get; }` |  |
| **`agentPosition`** | `public Vector3 agentPosition { get; }` |  |
| **`AI`** | `public EntityAI AI { get; }` |  |
| **`Animation`** | `public EntityAnimation Animation { get; }` |  |
| **`Control`** | `public EntityControl Control { get; }` |  |
| **`currentHealth`** | `public float currentHealth { get; }` |  |
| **`currentMana`** | `public float currentMana { get; }` |  |
| **`defaultOwner`** | `protected virtual DewPlayer defaultOwner { get; }` |  |
| **`isAlive`** | `public bool isAlive { get; }` |  |
| **`isDead`** | `public bool isDead { get; }` |  |
| **`isSleeping`** | `public bool isSleeping { get; }` |  |
| **`lastSection`** | `public RoomSection lastSection { get; }` | Section that this entity resided in. Even though an entity leaves a section, this variable will not be cleared.Available on server. Can be null. |
| **`level`** | `public int level { get; }` |  |
| **`maxHealth`** | `public float maxHealth { get; }` |  |
| **`maxMana`** | `public float maxMana { get; }` |  |
| **`normalizedHealth`** | `public float normalizedHealth { get; }` |  |
| **`normalizedMana`** | `public float normalizedMana { get; }` |  |
| **`owner`** | `[SaveVar] [SaveVar(SaveVarFlags.Default)] public DewPlayer owner { get; set; }` |  |
| **`section`** | `public RoomSection section { get; }` | Section that this entity resides in. Available on server.Can be null. |
| **`Sound`** | `public EntitySound Sound { get; }` |  |
| **`Status`** | `public EntityStatus Status { get; }` |  |
| **`Visual`** | `public EntityVisual Visual { get; }` |  |

:::

## Methods (28)

::: details `ActiveLogicUpdate(float)`

```csharp
protected override void ActiveLogicUpdate(float dt)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `dt` | `float` |  |

:::

::: details `AIUpdate(ref EntityAIContext)`

AI update will not fire if entity is channeling an ability.

```csharp
protected virtual void AIUpdate(ref EntityAIContext context)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `context` | [`EntityAIContext`](/api/Global.EntityAIContext) |  |

:::

::: details `Awake()`

```csharp
protected override void Awake()
```

:::

::: details `CanAggroTo(Entity)`

```csharp
public virtual bool CanAggroTo(Entity target)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `target` | [`Entity`](/api/Global.Entity) |  |

**Returns:** `bool`

:::

::: details `CheckEnemyOrNeutral(Entity)`

```csharp
public bool CheckEnemyOrNeutral(Entity target)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `target` | [`Entity`](/api/Global.Entity) |  |

**Returns:** `bool`

:::

::: details `GetActorReadableName()`

```csharp
public override string GetActorReadableName()
```

**Returns:** `string`

:::

::: details `GetNetworkAuthorityConnection()`

```csharp
protected override NetworkConnectionToClient GetNetworkAuthorityConnection()
```

**Returns:** `Mirror.NetworkConnectionToClient`

:::

::: details `GetRelation(Entity)`

```csharp
public EntityRelation GetRelation(Entity other)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `other` | [`Entity`](/api/Global.Entity) |  |

**Returns:** `EntityRelation`

:::

::: details `GetStaggerSettings()`

```csharp
protected virtual Entity.StaggerSettings GetStaggerSettings()
```

**Returns:** `Entity.StaggerSettings`

:::

::: details `GetTeamRelation(DewPlayer)`

```csharp
public TeamRelation GetTeamRelation(DewPlayer other)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `other` | [`DewPlayer`](/api/Global.DewPlayer) |  |

**Returns:** `TeamRelation`

:::

::: details `Kill()`

Kill this entity. Note this can be prevented by death interrupts.

```csharp
public void Kill()
```

:::

::: details `KillNoInterrupt()`

Kill this entity ignoring any death interrupts.

```csharp
public void KillNoInterrupt()
```

:::

::: details `LoadEntityModelLocal()`

```csharp
public virtual void LoadEntityModelLocal()
```

:::

::: details `OnDeath(EventInfoKill)`

Called everywhere when this entity dies.

```csharp
protected virtual void OnDeath(EventInfoKill info)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `info` | [`EventInfoKill`](/api/Global.EventInfoKill) |  |

:::

::: details `OnDestroyActor()`

```csharp
protected override void OnDestroyActor()
```

:::

::: details `OnDrawGizmos()`

```csharp
protected virtual void OnDrawGizmos()
```

:::

::: details `OnModelLoaded()`

```csharp
public virtual void OnModelLoaded()
```

:::

::: details `OnPrepare()`

```csharp
protected override void OnPrepare()
```

:::

::: details `OnStartServer()`

```csharp
public override void OnStartServer()
```

:::

::: details `OnStopServer()`

```csharp
public override void OnStopServer()
```

:::

::: details `ProcessReceivedDamage(ref DamageData, Actor)`

Process the given damage with this entity's received damage preprocessors.

```csharp
public void ProcessReceivedDamage(ref DamageData data, Actor actor)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `data` | [`DamageData`](/api/Global.DamageData) |  |
| `actor` | [`Actor`](/api/Global.Actor) |  |

:::

::: details `ProcessReceivedHeal(ref HealData, Actor)`

Process the given heal with this entity's received heal preprocessors.

```csharp
public void ProcessReceivedHeal(ref HealData data, Actor actor)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `data` | [`HealData`](/api/Global.HealData) |  |
| `actor` | [`Actor`](/api/Global.Actor) |  |

:::

::: details `ProcessReceivedManaHeal(ref HealData, Actor)`

Process the given mana heal with this entity's received mana heal preprocessors.

```csharp
public void ProcessReceivedManaHeal(ref HealData data, Actor actor)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `data` | [`HealData`](/api/Global.HealData) |  |
| `actor` | [`Actor`](/api/Global.Actor) |  |

:::

::: details `ProcessReceivedShield(ref HealData, Actor)`

```csharp
public void ProcessReceivedShield(ref HealData data, Actor actor)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `data` | [`HealData`](/api/Global.HealData) |  |
| `actor` | [`Actor`](/api/Global.Actor) |  |

:::

::: details `ShouldBeSavedWithRoom()`

```csharp
public override bool ShouldBeSavedWithRoom()
```

**Returns:** `bool`

:::

::: details `Sleep()`

Make this entity sleep.

```csharp
public void Sleep()
```

:::

::: details `Stagger(Vector3?)`

```csharp
public void Stagger(Vector3? dir)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `dir` | `UnityEngine.Vector3?` |  |

:::

::: details `WakeUp()`

Wake this entity up.

```csharp
public void WakeUp()
```

:::


## Architecture & Relationships

::: details Click to expand Architecture & Relationships

### Used By (1153)

*Classes and systems that invoke, reference, or depend on `Entity`:*

`ACH_BLACKCAT_DEJAVU` · `ACH_BURNING_LOVE` · `ACH_NOVICE_TREASURE_HUNTER` · `ACH_PEW_PEW_PEW` · `ACH_PRAISE_THE_SUN` · `ACH_PRAYER_FOR_THE_DREAMERS` · `ACH_REAP_WHAT_YOU_SOW` · `ACH_SHIELD_BATTERY` · `ACH_THE_EIGHTH_TROPHY` · `ACH_THOUSAND_THUNDERS` · [AbilityInstance](/api/Global.AbilityInstance) · [AbilitySelfValidator](/api/Global.AbilitySelfValidator) · [AbilityTargetValidator](/api/Global.AbilityTargetValidator) · [AbilityTargetValidatorWrapper](/api/Global.AbilityTargetValidatorWrapper) · [AbilityTrigger](/api/Global.AbilityTrigger) · [Accessory](/api/Global.Accessory) · [ActionAttackMove](/api/Global.ActionAttackMove) · [ActionBase](/api/Global.ActionBase) · [ActionCast](/api/Global.ActionCast) · [ActionInteract](/api/Global.ActionInteract) · [Actor](/api/Global.Actor) · [ActorManager](/api/Global.ActorManager) · `Ai_Ai_Mon_Ink_BossWhiteNight_OneInchPunch_Atk` · `Ai_ArcticTerritory` · `Ai_Atk_LacertaRifle` · `Ai_Atk_LacertaRifle_Crit` · `Ai_Atk_YubarStardust` · `Ai_C_BeamOfLight` · `Ai_C_CorrosiveTrails_Gas` · `Ai_C_DarkSpear` · `Ai_C_FlashFreeze` · `Ai_C_GlacialStomp` · `Ai_C_IceClaw` · `Ai_C_MagicSword` · `Ai_C_MassProtection` · `Ai_C_PressurePoint` · `Ai_C_ShockTrap_Explosion` · `Ai_C_SparklingWaterGun` · `Ai_C_SwiftSlash` · `Ai_C_Whirlwind` · `Ai_Culinary_Pickup` · `Ai_Curse_AnchorOfMind_Anchor` · `Ai_Curse_DreamAfflictionInductive_Smite` · `Ai_Curse_IntermittentExplosion_Explosion` · `Ai_D_BeautifulThreat_Feather` · `Ai_D_BurningFist_Attack` · `Ai_D_ChargedAnguillian_Lightning` · `Ai_D_ExplosionArtist_DodgeExplosion` · `Ai_D_ExplosionArtist_LargeExplosion` · `Ai_D_IceColdPresence_AOE` · `Ai_D_IcyVeins_Damage` · `Ai_D_ParryMaster_Parry` · `Ai_D_ReactiveShockwave_Shockwave` · `Ai_D_Resolve_Push` · `Ai_D_RoaringFist` · `Ai_D_SalamanderPowder_Projectile` · `Ai_D_ScarOfTheWind_DashAtk` · `Ai_D_SharedPain_Instance` · `Ai_E_Aftershock_Damage` · `Ai_E_AntiGravity` · `Ai_E_Blink_Back` · `Ai_E_ClutchesOfMalice_ReachAndPull` · `Ai_E_CrimsonLance` · `Ai_E_DoomsdayMeteor` · `Ai_E_FinalExplosion_Explosion` · `Ai_E_FlameJet` · `Ai_E_MassCleanse` · `Ai_E_SearingCharge` · `Ai_E_ShadowVolley` · `Ai_E_ShadowVolley_Projectile` · `Ai_E_SliceThroat` · `Ai_E_StygianRush_Rush` · `Ai_E_VileStrike_Damage` · `Ai_E_WinterDive` · `Ai_EmbraceNewIdentity` · `Ai_Gem_C_Charcoal_Projectile` · `Ai_Gem_E_Crimson` · `Ai_Gem_E_Fever_Explosion` · `Ai_Gem_E_Predation_Pickup` · `Ai_Gem_E_Thunder` · `Ai_Gem_L_SuppressedArcanum` · `Ai_Gem_R_Celestial` · `Ai_Gem_U_LastStarlight` · `Ai_GenericDodge` · `Ai_Hatred_Curse` · `Ai_Hatred_InkMapCurse` · `Ai_HunterArtillery_Big` · `Ai_HunterArtillery_Small` · `Ai_L_ButchersStrike` · `Ai_L_CoinExplosion_Coin` · `Ai_L_CoinExplosion_Explosion` · `Ai_L_LightExplosion` · `Ai_L_LightExplosion_Instance` · `Ai_L_MentalCorruption_Projectile` · `Ai_L_SmallMoltenCore_Dragon_Atk` · `Ai_M_DreamyWaltz_BuffExplosion` · `Ai_M_Endure_Shout` · `Ai_M_Sprint` · `Ai_MiniBoss_BloodThorn_MainThorn` · `Ai_MiniBoss_BloodThorn_SubThorn` · `Ai_MiniBoss_IceAura_AoE` · `Ai_MirageSkin_Oblivion_Orb` · `Ai_MirageSkin_Oppression_Explode` · `Ai_MirageSkin_Pulverization_Stomp` · `Ai_Mon_DarkCave_BossSeeker_Atk_Projectile` · `Ai_Mon_DarkCave_BossSeeker_RedFissure` · `Ai_Mon_DarkCave_BossSeeker_TunnelVision_Claw` · `Ai_Mon_DarkCave_BossSeeker_TunnelVision_SecondPoolAtk` · `Ai_Mon_DarkCave_Oppressor_Hypnotize` · `Ai_Mon_Despair_BossAzurak_DoubleStomp` · `Ai_Mon_Despair_BossAzurak_DoubleStomp_Instance` · `Ai_Mon_Despair_BossAzurak_RoarAtk` · `Ai_Mon_Despair_BossAzurak_Roll` · `Ai_Mon_Despair_BossAzurak_StompBlock` · `Ai_Mon_Despair_BossAzurak_StompGlobal` · `Ai_Mon_Despair_BossAzurak_StompProjectile_Projectile` · `Ai_Mon_Despair_Displacer_Blink` · `Ai_Mon_Despair_DreadBug_Jump` · `Ai_Mon_Despair_DreadBug_JumpBack` · `Ai_Mon_Despair_ParalyticFly_Atk` · `Ai_Mon_Despair_UnstableRat_Explosion` · `Ai_Mon_Forest_BossDemon_AltSkill_LineAtk_Spawner` · `Ai_Mon_Forest_BossDemon_AltSkill_Stomp` · `Ai_Mon_Forest_BossDemon_Blink` · `Ai_Mon_Forest_BossDemon_DelayedAtk` · `Ai_Mon_Forest_BossDemon_MainSkill_SpawnMissiles` · `Ai_Mon_Forest_BossDemon_MainSkill_Stomp_Tree` · `Ai_Mon_Forest_Hound_Charge` · `Ai_Mon_Forest_SpiderSpitter_Backdash` · `Ai_Mon_Forest_SpiderWarrior_Jump` · `Ai_Mon_Forest_Treant_PowerBomb` · `Ai_Mon_Ink_BossDarkMoon_Blade` · `Ai_Mon_Ink_BossDarkMoon_Eclipse` · `Ai_Mon_Ink_BossDarkMoon_Hammer` · `Ai_Mon_Ink_BossDarkMoon_ShortDash` · `Ai_Mon_Ink_BossDarkMoon_Spear` · `Ai_Mon_Ink_BossDarkMoon_ThrowSpear_TeleportAtk` · `Ai_Mon_Ink_BossWhiteNight_AltAtk` · `Ai_Mon_Ink_BossWhiteNight_AltAtk_Ready` · `Ai_Mon_Ink_BossWhiteNight_Cataclysm` · `Ai_Mon_Ink_BossWhiteNight_Cataclysm_Eclipse` · `Ai_Mon_Ink_BossWhiteNight_Cataclysm_Instance` · `Ai_Mon_Ink_BossWhiteNight_Cataclysm_SafeZone` · `Ai_Mon_Ink_BossWhiteNight_DestructionWave` · `Ai_Mon_Ink_BossWhiteNight_DestructionWave_Wave` · `Ai_Mon_Ink_BossWhiteNight_EnergyWave_Spawner` · `Ai_Mon_Ink_BossWhiteNight_Oppression` · `Ai_Mon_Ink_Boss_OnDeath` · `Ai_Mon_Ink_GhostBlade_SwiftStep` · `Ai_Mon_LavaLand_BossInfernus_AltAtk_Instance` · `Ai_Mon_LavaLand_BossInfernus_Atk` · `Ai_Mon_LavaLand_BossInfernus_BreathFire` · `Ai_Mon_LavaLand_BossInfernus_BreathFire_Projectile` · `Ai_Mon_LavaLand_BossInfernus_Jump` · `Ai_Mon_LavaLand_BossInfernus_Jump_Land` · `Ai_Mon_LavaLand_BossInfernus_PowerBomb` · `Ai_Mon_LavaLand_BossInfernus_Stomp` · `Ai_Mon_LavaLand_BossInfernus_Stomp_Eruption` · `Ai_Mon_LavaLand_BossInfernus_Swipe` · `Ai_Mon_LavaLand_BossInfernus_WallStunKnockback` · `Ai_Mon_LavaLand_FireElemental_BackDash` · `Ai_Mon_LavaLand_FireElemental_Destruct` · `Ai_Mon_LavaLand_FireElemental_Explosion` · `Ai_Mon_LavaLand_FireElemental_ExplosionSub` · `Ai_Mon_LavaLand_FireElemental_LaserAtk` · `Ai_Mon_Primus_BossPrimusAeron_Adapt_Arbalest` · `Ai_Mon_Primus_BossPrimusAeron_Adapt_Atk` · `Ai_Mon_Primus_BossPrimusAeron_Adapt_Doom_Meteor` · `Ai_Mon_Primus_BossPrimusAeron_Adapt_Doom_PyranasFireball` · `Ai_Mon_Primus_BossPrimusAeron_Adapt_IceClaw` · `Ai_Mon_Primus_BossPrimusAeron_Adapt_SmiteStorm` · `Ai_Mon_Primus_BossPrimusAeron_Adapt_Starfall_Instance` · `Ai_Mon_Primus_BossPrimusAeron_Dash` · `Ai_Mon_Primus_BossPrimusAeron_Force_Grab` · `Ai_Mon_Primus_BossPrimusAeron_Rage_DashAttack` · `Ai_Mon_Primus_BossPrimusAeron_Rage_MassDelusion` · `Ai_Mon_Primus_BossPrimusAeron_Rage_MassSilence_Instance` · `Ai_Mon_Sky_Baam_Teleport` · `Ai_Mon_Sky_Baam_TeleportSequence` · `Ai_Mon_Sky_BigBaam_BeamAtk` · `Ai_Mon_Sky_BigBaam_Main_Root` · `Ai_Mon_Sky_BossNyx_Atk` · `Ai_Mon_Sky_BossNyx_Blackhole` · `Ai_Mon_Sky_BossNyx_PullAtk_AfterAtk` · `Ai_Mon_Sky_BossNyx_StellarDash` · `Ai_Mon_Sky_BossNyx_Teleport` · `Ai_Mon_Sky_LittleBaam_Reposition` · `Ai_Mon_Sky_StarSeed_SelfDestruct` · `Ai_Mon_SnowMountain_BossSkoll_Atk` · `Ai_Mon_SnowMountain_BossSkoll_AuraBladeRain` · `Ai_Mon_SnowMountain_BossSkoll_AuraExplosion_Spawner` · `Ai_Mon_SnowMountain_BossSkoll_AuraSlice` · `Ai_Mon_SnowMountain_BossSkoll_Capture` · `Ai_Mon_SnowMountain_BossSkoll_DeathFromAbove` · `Ai_Mon_SnowMountain_BossSkoll_DeathFromAbove_Land` · `Ai_Mon_SnowMountain_BossSkoll_Whirlwind` · `Ai_Mon_SnowMountain_IceElemental_IceBreaker` · `Ai_Mon_SnowMountain_IceElemental_IceBreaker_SubExplosion` · `Ai_Mon_SnowMountain_Scavenger_Jump` · `Ai_Mon_SnowMountain_VikingWarrior_Atk` · `Ai_Mon_Special_AmbushSpawner_Projectile` · `Ai_Mon_Special_BossErebos_Gaze_Instance` · `Ai_Mon_Special_BossErebos_SpawnBlackhole_Instance` · `Ai_Mon_Special_BossErebos_SpawnTormentor_Slow` · `Ai_Mon_Special_BossErebos_StarRain_Instance` · `Ai_Mon_Special_BossErebos_StarRain_Spawner` · `Ai_Mon_Special_BossErebos_Teleport` · `Ai_Mon_Special_BossMaw_AnnihilationStance` · `Ai_Mon_Special_BossMaw_Cataclysm_Spawner` · `Ai_Mon_Special_BossMaw_ChainReaction` · `Ai_Mon_Special_BossMaw_ChainReaction_Instance` · `Ai_Mon_Special_BossMaw_Chomp_Charge` · `Ai_Mon_Special_BossMaw_DarkSpear` · `Ai_Mon_Special_BossMaw_MoonlightPact` · `Ai_Mon_Special_BossMaw_PillarOfFlame_Projectile` · `Ai_Mon_Special_BossMaw_PrecisionShot` · `Ai_Mon_Special_BossMaw_Purgatory_Heal` · `Ai_Mon_Special_BossMaw_ScatterShot_Spawner` · `Ai_Mon_Special_BossMaw_ShadowOverdrive_Projectile` · `Ai_Mon_Special_BossMaw_SliceThroat` · `Ai_Mon_Special_BossMaw_SliceThroat_Atk` · `Ai_Mon_Special_BossObliviax_BackStep` · `Ai_Mon_Special_BossObliviax_ChargeSequence_MissileAtk` · `Ai_Mon_Special_BossObliviax_ChargeSequence_Ready` · `Ai_Mon_Special_BossObliviax_DashAtk` · `Ai_Mon_Special_BossObliviax_NeedleAtk_Ready` · `Ai_Mon_Special_BossPolaris_Holy_Atk_Explosion` · `Ai_Mon_Special_BossPolaris_Holy_Beam` · `Ai_Mon_Special_BossPolaris_Holy_CounterSpell_DisarmProjectile` · `Ai_Mon_Special_BossPolaris_Holy_Purgatory_BurningFloor` · `Ai_Mon_Special_BossPolaris_Holy_Purgatory_HealProjectile` · `Ai_Mon_Special_BossPolaris_Holy_Purgatory_Instance` · `Ai_Mon_Special_BossPolaris_Holy_Purgatory_Spawner` · `Ai_Mon_Special_BossPolaris_Holy_RainFire_Damage` · `Ai_Mon_Special_BossPolaris_Holy_ScatterFire` · `Ai_Mon_Special_BossPolaris_Holy_SelfCleanse` · `Ai_Mon_Special_BossPolaris_Monster_Atk_FirstAtk` · `Ai_Mon_Special_BossPolaris_Monster_Atk_SecondAtk` · `Ai_Mon_Special_BossPolaris_Monster_Atk_Spawner` · `Ai_Mon_Special_BossPolaris_Monster_CursedDive_Stomp` · `Ai_Mon_Special_BossPolaris_Monster_Dash` · `Ai_Mon_Special_BossPolaris_Monster_JumpStomp` · `Ai_Mon_Special_BossPolaris_Monster_JumpStomp_LargerExplosion` · `Ai_Mon_Special_BossPolaris_Monster_PizzaLightning_Spawner` · `Ai_Mon_Special_BossPolaris_Monster_Scream` · `Ai_Mon_Special_BossPolaris_Monster_Scream_SkillLocker` · `Ai_Mon_Special_BossPolaris_Monster_SlashDash` · `Ai_Mon_Special_BossPolaris_Monster_Smite_Instance` · `Ai_QR_DistortedMind_Damage` · `Ai_QR_DistortedMind_Spawner` · `Ai_QR_InfernalTales` · `Ai_QR_Innocence_Explosion` · `Ai_QR_ValiantHeart` · `Ai_Q_BigBorealChunk_Explosion` · `Ai_Q_BigBorealChunk_Spawner` · `Ai_Q_CruelSun` · `Ai_Q_CruelSun_Shockwave` · `Ai_Q_DeathMark_Projectile` · `Ai_Q_Discipline_Stomp` · `Ai_Q_EmbracingTheChill_AreaDoT` · `Ai_Q_EmbracingTheChill_Explosion` · `Ai_Q_EtherealInfluence` · `Ai_Q_Fleche_Dash` · `Ai_Q_GoldenBurst` · `Ai_Q_HandCannon` · `Ai_Q_Laceration_Circle` · `Ai_Q_Laceration_Dash` · `Ai_Q_Lunge` · `Ai_Q_MoonlightPact` · `Ai_Q_MoonlightPact_Fenrir_Atk` · `Ai_Q_MoonlightPact_Land` · `Ai_Q_Reduction_Projectile` · `Ai_Q_SuperNova` · `Ai_Q_SylvanCall` · `Ai_Q_SylvanCall_LeafHound_Atk` · `Ai_R_BackOff_Damage` · `Ai_R_BackOff_Spawner` · `Ai_R_BaptismOfSun` · `Ai_R_BoneCrusher_Explosion` · `Ai_R_Cataclysm_Meteor` · `Ai_R_ChainReaction` · `Ai_R_Chomp` · `Ai_R_DarkGrenade_Shard` · `Ai_R_FlamingWhip` · `Ai_R_FrozenFists_PunchDash` · `Ai_R_GlacialHammer` · `Ai_R_Ignite` · `Ai_R_Inspire_Roar` · `Ai_R_Lava_LavaField` · `Ai_R_NaturesWhisper` · `Ai_R_Parry_Projectile` · `Ai_R_PhantomBlade` · `Ai_R_RepulsiveShield_Projectile` · `Ai_R_SanctuaryOfEl_Ground` · `Ai_R_Scattershot_Spawner` · `Ai_R_SerpentineBlessing` · `Ai_R_SerpentineBlessing_Projectile` · `Ai_R_Somersault` · `Ai_R_StaticDischarge` · `Ai_R_SummonLittleBaam` · `Ai_R_Tranquility_Damage` · `Ai_R_WarBoomerang` · `Ai_R_WrathOfEl` · `Ai_RandomGemUpgrade` · `Ai_ReviveHero` · `Ai_RoomMod_MeteoricLife_Explosion` · `Ai_Shrine_MawOfDoom_DestroyTarget` · `Ai_Sky_BossIntruder_Instance` · `Ai_Star_Bismuth_F_IT_SmallerRingAddDisplacement_Dash` · `Ai_Star_Cetus_F_BI_SelfDamageAoeCold_AOE` · `Ai_Star_Mist_F_LG_ChainAttack_Phantom` · `Ai_Star_Yubar_F_EI_DashNoProjectile_Dash` · `Ai_Trap_UnstableMushroom` · `Ai_U_BeamOfBalance_Beam` · `Ai_U_BigChomp` · `Ai_U_Burrow_Emerge` · `Ai_U_HerWorld_Explosion` · `Ai_U_Hysteria_Claw` · `Ai_U_ShoutOfOblivion` · `Ai_U_WorldCracker` · `Ai_UnstableRatSwarm_Projectile` · `Ai_VeilOfDark` · [Artifact](/api/Global.Artifact) · `At_Atk_HuskSword` · `At_Atk_LacertaRifle` · `At_Atk_YubarStardust` · `At_Mon_Despair_ParalyticFly_Atk` · `At_Mon_Forest_BossDemon_Spawn` · `At_Mon_Forest_SpiderSpitter_Atk` · `At_Mon_Forest_SpiderSpitter_Melee` · `At_Mon_Ink_BossWhiteNight_OneInchPunch` · `At_Mon_LavaLand_InfernoSpider_LavaAtk` · `At_Mon_Primus_BossPrimusAeron_Rage_MassDelusion` · `At_Mon_Special_BossMaw_Purgatory` · `At_Mon_Special_BossObliviax_Artillery` · `At_Mon_Special_BossObliviax_NeedleAtk` · `At_Mon_Special_BossPolaris_Holy_GoldenSpear` · `At_Mon_Special_BossPolaris_Holy_SelfCleanse` · `At_MorasDomain_MorasCreation_Boss_Move` · `At_MorasDomain_MorasCreation_Boss_SpawnSwarm` · [AttackOverrideEffect](/api/Global.AttackOverrideEffect) · [AttackTrigger](/api/Global.AttackTrigger) · [BasicEffect](/api/Global.BasicEffect) · [BasicEffectWithStrength](/api/Global.BasicEffectWithStrength) · [BossMonster](/api/Global.BossMonster) · `BossSeeker_SpotLightController` · [CameraManager](/api/Global.CameraManager) · [CastIndicatorManager](/api/Global.CastIndicatorManager) · [CastInfo](/api/Global.CastInfo) · [Channel](/api/Global.Channel) · [ChargingChannel](/api/Global.ChargingChannel) · [ChoiceShrine](/api/Global.ChoiceShrine) · [CinematicCameraHelper](/api/Global.CinematicCameraHelper) · [ClearSectionEventData](/api/Global.ClearSectionEventData) · [ClientEventManager](/api/Global.ClientEventManager) · [ConsoleManager](/api/Global.ConsoleManager) · [ControlManager](/api/Global.ControlManager) · [ConversationManager](/api/Global.ConversationManager) · `ConversationShrineBase` · [Cost](/api/Global.Cost) · `CostExtensions` · [CurseStatusEffect](/api/Global.CurseStatusEffect) · [DamageData](/api/Global.DamageData) · [DamageInstance](/api/Global.DamageInstance) · [Dash](/api/Global.Dash) · [DashAttackInstance](/api/Global.DashAttackInstance) · `Despair_FogPositionController` · [Dew](/api/Global.Dew) · [DewCollider](/api/Global.DewCollider) · `DewConsoleCommands` · [DewCutsceneDirector](/api/Global.DewCutsceneDirector) · `DewDamageNumberRenderer` · [DewDifficultySettings](/api/Global.DewDifficultySettings) · [DewEffect](/api/Global.DewEffect) · [DewHeroesTeleporter](/api/Global.DewHeroesTeleporter) · `DewLocalDitherFade` · [DewNetworkBehaviour](/api/Global.DewNetworkBehaviour) · [DewNetworkManager](/api/Global.DewNetworkManager) · [DewPersistence](/api/Global.DewPersistence) · [DewPhysics](/api/Global.DewPhysics) · [DewPlayer](/api/Global.DewPlayer) · `DewStarItemOld` · [DispByTarget](/api/Global.DispByTarget) · [EditSkillManager](/api/Global.EditSkillManager) · [EditSkillShrine](/api/Global.EditSkillShrine) · [EntityAI](/api/Global.EntityAI) · [EntityAIContext](/api/Global.EntityAIContext) · [EntityAbility](/api/Global.EntityAbility) · [EntityAnimation](/api/Global.EntityAnimation) · [EntityCheck](/api/Global.EntityCheck) · [EntityColorModifier](/api/Global.EntityColorModifier) · [EntityComponent](/api/Global.EntityComponent) · [EntityControl](/api/Global.EntityControl) · [EntityGroundMarker](/api/Global.EntityGroundMarker) · [EntityHighlightProvider](/api/Global.EntityHighlightProvider) · [EntityShellModifier](/api/Global.EntityShellModifier) · [EntitySound](/api/Global.EntitySound) · [EntityStatus](/api/Global.EntityStatus) · [EntityTransformModifier](/api/Global.EntityTransformModifier) · [EntityVisual](/api/Global.EntityVisual) · [EventInfoApplyElemental](/api/Global.EventInfoApplyElemental) · [EventInfoAttackEffect](/api/Global.EventInfoAttackEffect) · [EventInfoAttackHit](/api/Global.EventInfoAttackHit) · [EventInfoAttackMissed](/api/Global.EventInfoAttackMissed) · [EventInfoDamage](/api/Global.EventInfoDamage) · [EventInfoDamageNegatedByImmunity](/api/Global.EventInfoDamageNegatedByImmunity) · [EventInfoDamageNegatedByShield](/api/Global.EventInfoDamageNegatedByShield) · [EventInfoHeal](/api/Global.EventInfoHeal) · [EventInfoKill](/api/Global.EventInfoKill) · [EventInfoShield](/api/Global.EventInfoShield) · [EventInfoSpentMana](/api/Global.EventInfoSpentMana) · [EventInfoStartChase](/api/Global.EventInfoStartChase) · [EventInfoStartMove](/api/Global.EventInfoStartMove) · [EventInfoStatusEffect](/api/Global.EventInfoStatusEffect) · [EventInfoStopChase](/api/Global.EventInfoStopChase) · [EventInfoStopMove](/api/Global.EventInfoStopMove) · [FinalDamageData](/api/Global.FinalDamageData) · [FlavourManager](/api/Global.FlavourManager) · `Forest_Fireplace` · `Forest_FogVoid` · `FxAnimatorBoneOffset` · [FxAnimatorSetFloat](/api/Global.FxAnimatorSetFloat) · [FxAnimatorSetTrigger](/api/Global.FxAnimatorSetTrigger) · [FxAttachToEntity](/api/Global.FxAttachToEntity) · [FxCastTelegraph](/api/Global.FxCastTelegraph) · [FxDoFDynamicFocusDistance](/api/Global.FxDoFDynamicFocusDistance) · [FxEntityAnimation](/api/Global.FxEntityAnimation) · [FxEntityColor](/api/Global.FxEntityColor) · [FxEntityDisableRenderer](/api/Global.FxEntityDisableRenderer) · `FxEntityInvoke` · [FxEntityModelTransform](/api/Global.FxEntityModelTransform) · [FxEntityShake](/api/Global.FxEntityShake) · [FxEntityShell](/api/Global.FxEntityShell) · [FxEntityTransform](/api/Global.FxEntityTransform) · [FxMeshTrail](/api/Global.FxMeshTrail) · [FxRepeatedEffect](/api/Global.FxRepeatedEffect) · [FxSelectiveVisibility](/api/Global.FxSelectiveVisibility) · [GameManager](/api/Global.GameManager) · `GameMod_DespairFixStuck` · [GameMod_Limbo](/api/Global.GameMod_Limbo) · [GameMod_MirageSkin](/api/Global.GameMod_MirageSkin) · `GameMod_StarlessPath` · [GameResultManager](/api/Global.GameResultManager) · `Ge_Obliviax_InterruptTravelAndKidnap` · [Gem](/api/Global.Gem) · `Gem_C_Charcoal` · `Gem_C_Confidence` · `Gem_C_Guidance` · `Gem_C_Lethality` · `Gem_C_Love` · `Gem_C_Quicksilver` · `Gem_C_Regeneration` · `Gem_C_Responsibility` · `Gem_C_Shatter` · `Gem_C_Sulfur` · `Gem_C_Talc` · `Gem_C_Vengeance` · `Gem_C_Void` · `Gem_C_Wind` · `Gem_E_Aftershock` · `Gem_E_Apathy` · `Gem_E_Blossom` · `Gem_E_Clemency` · `Gem_E_Direness` · `Gem_E_Domination` · `Gem_E_Fever` · `Gem_E_Flexibility` · `Gem_E_Insensitivity` · `Gem_E_Insight` · `Gem_E_Inversion` · `Gem_E_Might` · `Gem_E_Obsidian` · `Gem_E_OurStory_Completed` · `Gem_E_OurStory_Unfinished` · `Gem_E_Overload` · `Gem_E_Pain` · `Gem_E_Predation` · `Gem_E_Protection` · `Gem_E_Reflex` · `Gem_E_Twilight` · `Gem_E_Umbra` · `Gem_L_CamillasGift` · `Gem_L_ChaosApple` · `Gem_L_Culinary` · `Gem_L_DivineFaith` · `Gem_L_Embertail` · `Gem_L_HeartOfGold` · `Gem_L_Liberty` · `Gem_L_MetalCrystal` · `Gem_L_Paranoia` · `Gem_L_Supersymmetry` · `Gem_L_SuppressedArcanum` · `Gem_R_Abyss` · `Gem_R_Accuracy` · `Gem_R_Blade` · `Gem_R_Bleak` · `Gem_R_Blood` · `Gem_R_Celestial` · `Gem_R_Composure` · `Gem_R_Contempt` · `Gem_R_Control` · `Gem_R_Epiphany` · `Gem_R_Flow` · `Gem_R_Frost` · `Gem_R_Glass` · `Gem_R_Hedgehog` · `Gem_R_Insatiable` · `Gem_R_Lightweight` · `Gem_R_Mortality` · `Gem_R_NightSky` · `Gem_R_Panic` · `Gem_R_Purity` · `Gem_R_Ricochet` · `Gem_R_Rigidity` · `Gem_R_Shock` · `Gem_R_Slippery` · `Gem_R_Snow` · `Gem_R_Spiral` · `Gem_R_Wound` · `Gem_U_EternalFlame` · `Gem_U_GlacialCore` · `Gem_U_GuidingCompass_NotCharged` · `Gem_U_LastStarlight` · `Gem_U_SoulPrison` · [HealData](/api/Global.HealData) · `HealthThresholdBonusStarEffect` · [Hero](/api/Global.Hero) · [HeroSkill](/api/Global.HeroSkill) · `Hero_Aurena` · `Hero_Bismuth` · `Hero_Bismuth_BookController` · `Hero_Cetus` · `Hero_Husk` · `Hero_Lacerta` · `Hero_Vesper` · [IAttachableToEntity](/api/Global.IAttachableToEntity) · [IBinaryEntityValidator](/api/Global.IBinaryEntityValidator) · [IEntityValidator](/api/Global.IEntityValidator) · [IInteractable](/api/Global.IInteractable) · [IItem](/api/Global.IItem) · [ISpawnableAsMiniBoss](/api/Global.ISpawnableAsMiniBoss) · `InGameAnalyticsManager` · `Ink_BossRoomDamageGround` · `Ink_SecondCutscenePlay` · [InvisibleEffect](/api/Global.InvisibleEffect) · `ItemWorldModel` · [KillTracker](/api/Global.KillTracker) · [Knockback](/api/Global.Knockback) · `LavaLand_IcePlace` · `LavaLand_Lava` · `LucidDream_BlandStarSoup` · `LucidDream_EmbraceMortality` · `LucidDream_FishScales` · `LucidDream_GrievousWounds` · `LucidDream_HarmlessWhispers` · `LucidDream_KindArmadillo` · `LucidDream_MarshOfDestiny` · `LucidDream_TheDarkestUrge` · `LucidDream_WILD` · [MeleeAttackInstance](/api/Global.MeleeAttackInstance) · [MirageSkinEffect](/api/Global.MirageSkinEffect) · [MockEntity](/api/Global.MockEntity) · [ModBehaviour](/api/Global.ModBehaviour) · `Mon_DarkCave_BossSeeker` · `Mon_DarkCave_CaveBat` · `Mon_DarkCave_CaveSpider` · `Mon_DarkCave_DarkElemental` · `Mon_DarkCave_NightOlm` · `Mon_DarkCave_Oppressor` · `Mon_DarkCave_SeekerHallucination` · `Mon_Despair_AzurakMonsterSpawner` · `Mon_Despair_BossAzurak` · `Mon_Despair_Displacer` · `Mon_Despair_DreadBug` · `Mon_Despair_ParalyticFly` · `Mon_Despair_UnstableRat` · `Mon_Despair_WretchedArtillery` · [Mon_DreamTeller](/api/Global.Mon_DreamTeller) · `Mon_Forest_BossDemon` · `Mon_Forest_Hound` · `Mon_Forest_Scarab` · `Mon_Forest_SpiderSpitter` · `Mon_Forest_SpiderWarrior` · `Mon_Forest_Treant` · `Mon_GoldenLizard_ElusiveLizard` · `Mon_Ink_Archer` · `Mon_Ink_BossDarkMoon` · `Mon_Ink_BossDarkMoonHallucination` · `Mon_Ink_BossWhiteNight` · `Mon_Ink_BossWhiteNightHallucination` · `Mon_Ink_DivineAnimal` · `Mon_Ink_EgoSword` · `Mon_Ink_GhostBlade` · `Mon_Ink_GhostSpear` · `Mon_LavaLand_BossInfernus` · `Mon_LavaLand_FireElemental` · `Mon_LavaLand_InfernoSpider` · `Mon_LavaLand_InfernusPillar` · `Mon_LavaLand_Magmadon` · `Mon_LavaLand_SuperheatedWolf` · `Mon_Polaris` · `Mon_Primus_BossPrimusAeron` · [Mon_RedGiant](/api/Global.Mon_RedGiant) · [Mon_RedMan](/api/Global.Mon_RedMan) · `Mon_Sky_Baam` · `Mon_Sky_BigBaam_Base` · `Mon_Sky_BigBaam_Regular` · `Mon_Sky_BigBaam_Rooter` · `Mon_Sky_BossNyx` · `Mon_Sky_LittleBaam` · `Mon_Sky_StarSeed` · `Mon_SnowMountain_BossSkoll` · `Mon_SnowMountain_IceElemental` · `Mon_SnowMountain_LivingShards` · `Mon_SnowMountain_Scavenger` · `Mon_SnowMountain_SnowWolf` · `Mon_SnowMountain_VikingWarrior` · `Mon_Special_AmbushSpawner` · `Mon_Special_BossErebos` · `Mon_Special_BossLightElemental` · `Mon_Special_BossMaw` · `Mon_Special_BossObliviax` · `Mon_Special_BossPolaris` · [Monster](/api/Global.Monster) · [PickupManager](/api/Global.PickupManager) · [Pickup_BaseGoldOrb](/api/Global.Pickup_BaseGoldOrb) · [Pickup_DreamDust](/api/Global.Pickup_DreamDust) · [Pickup_HealthOrb](/api/Global.Pickup_HealthOrb) · [Pickup_ManaOrb](/api/Global.Pickup_ManaOrb) · [PingManager](/api/Global.PingManager) · [PlayGameManager](/api/Global.PlayGameManager) · `PlayTutorial_Tutorial` · `PlayTutorial_Tutorial_Hunt` · `PlayTutorial_Tutorial_Intro` · `PlayTutorial_Tutorial_SkillsAndEssences` · `PrimusCutsceneEntityVisualOff` · `Primus_Ending` · `Primus_PureWhiteOpenEffect` · [Projectile](/api/Global.Projectile) · [PropEnt_Merchant_Backpack](/api/Global.PropEnt_Merchant_Backpack) · [PropEnt_Merchant_Base](/api/Global.PropEnt_Merchant_Base) · [PropEnt_Merchant_Jonas](/api/Global.PropEnt_Merchant_Jonas) · [PropEnt_Merchant_Smoothie](/api/Global.PropEnt_Merchant_Smoothie) · `PropEnt_Sky_Orca` · [PropEnt_Stone_DreamDust](/api/Global.PropEnt_Stone_DreamDust) · [PropEnt_Stone_Gold](/api/Global.PropEnt_Stone_Gold) · `PropEnt_Stone_PitchBlackOre` · `PropEnt_Tutorial_Obstacle` · `PropEnt_VigilanteHaven_Obstacle` · [PropEntity](/api/Global.PropEntity) · [ProxyCollider](/api/Global.ProxyCollider) · [QuestManager](/api/Global.QuestManager) · `Quest_LostSoul` · [Rift](/api/Global.Rift) · [Rift_RoomExit](/api/Global.Rift_RoomExit) · [Rift_Sidetrack](/api/Global.Rift_Sidetrack) · [Room](/api/Global.Room) · `RoomMod_Artifact` · `RoomMod_CorruptedChaos_AuraOfPain` · `RoomMod_DistantMemories` · `RoomMod_EngulfedInFlame` · `RoomMod_Hunted` · `RoomMod_InversionSigil` · `RoomMod_LeafPuppies` · `RoomMod_MeteoricLife` · `RoomMod_PureDream` · `RoomMod_RiskOfMeteors` · `RoomMod_StardustEverywhere` · [RoomModifierBase](/api/Global.RoomModifierBase) · [RoomMonsters](/api/Global.RoomMonsters) · [RoomSection](/api/Global.RoomSection) · [Room_Barrier](/api/Global.Room_Barrier) · [Room_Shortcut](/api/Global.Room_Shortcut) · [ScalingValue](/api/Global.ScalingValue) · `Se_AcceleratedTime` · `Se_AutoDetectPresence` · `Se_BarrierPassThrough` · `Se_C_CorrosiveTrails_Spawner` · `Se_C_Hemorrhage_EmpowerAttack` · `Se_Curse_AmplifiedPain` · `Se_Curse_AnchorOfMind` · `Se_Curse_BlissOfIgnorance` · `Se_Curse_DarkUrge` · `Se_Curse_DreamAfflictionHallucinatory` · `Se_Curse_DreamAfflictionParalytic` · `Se_Curse_FateOfGreed` · `Se_Curse_Fragility` · `Se_Curse_FragmentedBeing` · `Se_Curse_GuidingCompass_CripplingAnxiety` · `Se_Curse_IntermittentExplosion` · `Se_Curse_Lethargy` · `Se_Curse_SilentNight` · `Se_Curse_SilentNight_Locked` · `Se_Curse_SoftSkin` · `Se_Curse_UnstableEnergy` · `Se_Curse_VainDream` · `Se_D_AstridsMasterpieceEnGarde` · `Se_D_AstridsMasterpieceEnGarde_Exposed` · `Se_D_AstridsMasterpiecePriorite` · `Se_D_AstridsMasterpiecePriorite_Exposed` · `Se_D_BeautifulThreat` · `Se_D_ChargedAnguillian` · `Se_D_CircleOfLife_Summon` · `Se_D_ConvergencePoint` · `Se_D_DoubleTap` · `Se_D_ExoticMatter` · `Se_D_IceColdPresence` · `Se_D_IceColdPresence_PersistentBuff` · `Se_D_IcyVeins` · `Se_D_MercyOfEl` · `Se_D_PrismaticEyes` · `Se_D_QuartetOfDeath_Buff` · `Se_D_TheKillingFlow` · `Se_D_TrueDuelist_Exposed` · `Se_DarkCondensationZone` · `Se_DistantMemories` · `Se_E_Harvest_OnVictim` · `Se_E_LizardlyBlessing` · `Se_E_Permafrost_Shield` · `Se_E_Permafrost_Stun` · `Se_E_UmbralEdge` · `Se_E_VileStrike` · `Se_Elm_Cold` · `Se_Elm_Dark` · `Se_Elm_Fire` · `Se_Elm_Light` · `Se_EngulfedInFlame` · `Se_FallenStar_MonsterReinforcement` · `Se_FallenStar_WaveringIdentity` · `Se_FatalHitProtection_Invulnerable` · `Se_FishScales` · `Se_Gem_E_Fever_LivingBomb` · `Se_Gem_E_Insensitivity_BombSpawner` · `Se_Gem_R_Frost_Stat` · `Se_Gem_R_Hedgehog_Aura` · `Se_Gem_R_Insatiable` · `Se_GenericEffectContainer` · `Se_GenericHealOverTime` · `Se_GenericRevealed` · `Se_GenericStealth` · `Se_GoldEverywhere` · `Se_GravityTraining` · `Se_HarmlessWhispers` · `Se_HealthCost` · `Se_HeroBleedingOut` · `Se_HeroKnockedOut` · `Se_HeroOneShotProtection` · `Se_HunterBuff` · `Se_HunterBuff_ShadowWalk_Disappear` · `Se_InConversation` · `Se_L_ButchersStrike_KillTimer` · `Se_L_MentalCorruption` · `Se_L_Multishot_Buff` · `Se_L_PyranasFireball` · `Se_LimboBossDecorator` · `Se_LingeringAuraOfGuidance` · `Se_M_Charge` · `Se_M_DreamyWaltz_Buff` · `Se_M_Flicker` · `Se_M_Sprint` · `Se_MiniBoss_BloodThorn` · `Se_MiniBoss_BloodThorn_Bleeding` · `Se_MiniBoss_IceAura` · `Se_MiniBoss_OrbSpitter` · `Se_MiniBoss_SpinningArrow` · `Se_MiniBoss_UnstableExplosive` · `Se_MiniBoss_UnstableExplosive_Explosion` · `Se_MirageSkin_Delusion` · `Se_MirageSkin_Delusion_Delusional` · `Se_MirageSkin_Oblivion` · `Se_MirageSkin_Oblivion_Silenced` · `Se_MirageSkin_Oppression` · `Se_MirageSkin_Pulverization` · `Se_MirageSkin_Sanctification` · `Se_MirageSkin_Sanctification_Protected` · `Se_Mon_DarkCave_BossSeeker_Blink` · `Se_Mon_DarkCave_BossSeeker_Hallucination_Disappear` · `Se_Mon_DarkCave_BossSeeker_Substitution` · `Se_Mon_DarkCave_BossSeeker_TunnelVision` · `Se_Mon_DarkCave_BossSeeker_TunnelVision_Disappear` · `Se_Mon_DarkCave_DarkElemental_Teleport` · `Se_Mon_Despair_BossAzurak_Hide` · `Se_Mon_Despair_BossAzurak_RoarAtk_SafeZoneSpawner` · `Se_Mon_Despair_ParalyticFly_Atk_Instance` · `Se_Mon_Ink_BossWhiteNight_Cataclysm` · `Se_Mon_Ink_BossWhiteNight_Rush` · `Se_Mon_Ink_Boss_Rage` · `Se_Mon_LavaLand_BossInfernus_InvulShield` · `Se_Mon_LavaLand_BossInfernus_Jump_Invul` · `Se_Mon_Polaris_Blink` · `Se_Mon_Polaris_Disappear` · `Se_Mon_Primus_BossPrimusAeron_Adapt_Doom_Initial` · `Se_Mon_Primus_BossPrimusAeron_Adapt_Doom_Ongoing` · `Se_Mon_Primus_BossPrimusAeron_Adapt_IceBlock` · `Se_Mon_Primus_BossPrimusAeron_Adaptation` · `Se_Mon_Primus_BossPrimusAeron_Force_GoldRain` · `Se_Mon_Primus_BossPrimusAeron_Rage_DecayingShield` · `Se_Mon_Sky_BossNyx_PhaseChange` · `Se_Mon_Sky_BossNyx_StarBuff` · `Se_Mon_SnowMountain_BossSkoll_DeathFromAbove_Invulnerable` · `Se_Mon_SnowMountain_SnowWolf_SlowApproach` · `Se_Mon_SnowMountain_VikingWarrior_DmgReducer` · `Se_Mon_Special_BossErebos_SecondPhase` · `Se_Mon_Special_BossMaw_Cataclysm` · `Se_Mon_Special_BossMaw_ShadowOverdrive_Initial` · `Se_Mon_Special_BossMaw_ShieldConversion` · `Se_Mon_Special_BossPolaris_Adaptation` · `Se_Mon_Special_BossPolaris_CleansingFlame` · `Se_Mon_Special_BossPolaris_Holy_CounterSpell` · `Se_Mon_Special_BossPolaris_Holy_Dash` · `Se_Mon_Special_BossPolaris_Holy_PhaseShifter` · `Se_Mon_Special_BossPolaris_Monster_Scream_SkillLocked` · `Se_MonsterSprint` · `Se_Nor_MyOwnLittleNebula` · `Se_Nor_ReptilianThirdEye` · `Se_Nor_WindowToTheSoul_SpiritualDominance` · `Se_Nor_WindowToTheSoul_WeaknessRevealed` · `Se_ObliviaxKidnap` · `Se_PlayTutorialHeroProtection` · `Se_PolarisHallucination` · `Se_PortalTransition` · `Se_PureDream` · `Se_PureDream_Statue` · `Se_Q_DeathMark_Marked` · `Se_Q_Discipline_Jump` · `Se_Q_GoldenBurst_Wither` · `Se_Q_IncendiaryRounds_EmpowerAttacks` · `Se_R_AnnihilationStance` · `Se_R_BaptismOfSun_Buff` · `Se_R_BoneCrusher` · `Se_R_BoneCrusher_Kidnapped` · `Se_R_BoneCrusher_UnstoppableAndShield` · `Se_R_Cataclysm` · `Se_R_Composure_Buff` · `Se_R_DangerousTheory` · `Se_R_Deception` · `Se_R_Frostbite_EmpowerAttacks` · `Se_R_FrozenFists` · `Se_R_Immolation` · `Se_R_Lava_Debuff` · `Se_R_LightningDance` · `Se_R_Parry_Start` · `Se_R_RepulsiveShield` · `Se_R_SerpentineBlessing_Buff` · `Se_R_ShadowOverdrive_Initial` · `Se_R_ShadowWalk_Disappear` · `Se_R_Tranquility` · `Se_R_UnbreakableDetermination` · `Se_RoomMod_BlackRain` · `Se_RoomMod_Symbiote` · `Se_RoomMod_ToxicArea_Debuff` · `Se_RoomMod_UnstableVeilOfTime_ModifyCooldowns` · `Se_RoomMod_WarpingField_Unstable` · `Se_RoomMod_WarpingField_Warp` · `Se_Shrine_Chaos_StatBonus` · `Se_Shrine_Despair_Teleport` · `Se_Shrine_SmallSoul` · `Se_Star_Aurena_F_DT_UnstoppableAndRemoveDelusion` · `Se_Star_Aurena_I_GoldOnMerchantDamage` · `Se_Star_Aurena_L_HealAmpOnLowHp` · `Se_Star_Aurena_L_HealAmpWithPenalty` · `Se_Star_Aurena_L_ShareHeal` · `Se_Star_Aurena_L_SpeedOnDamage` · `Se_Star_Bismuth_D_BonusAttackEffect` · `Se_Star_Bismuth_D_Conquerer_Stacks` · `Se_Star_Bismuth_D_SkillHasteAndAutoCast` · `Se_Star_Bismuth_F_IN_MoreProjByAtkSpd` · `Se_Star_Bismuth_F_IT_SmallerRingAddDisplacement` · `Se_Star_Bismuth_L_ContinuousSpeed` · `Se_Star_Bismuth_L_DodgeNoDashMoreCharges` · `Se_Star_Cetus_D_AdApUpByBonusHp` · `Se_Star_Cetus_D_StatsUpWhileShielded` · `Se_Star_Cetus_F_BA_CdReductionOnKill` · `Se_Star_Cetus_F_FR_CdReductionOnTakeDamage` · `Se_Star_Cetus_F_FR_ChangeToUltHitReset` · `Se_Star_Cetus_L_ArmorBuffOnShield` · `Se_Star_Cetus_L_FrostResistAndBuff` · `Se_Star_Cetus_L_HealOnApDamage` · `Se_Star_Cetus_L_IncreaseDealtShield` · `Se_Star_Cetus_L_MaxHpDamagePenalty` · `Se_Star_Cetus_L_ScalingHealth` · `Se_Star_D_BossDamageAmp` · `Se_Star_D_CritUpHitDecay` · `Se_Star_D_DamageBonusOnAllElemental` · `Se_Star_D_LowerADScalingAP` · `Se_Star_D_LowerAPScalingAD` · `Se_Star_D_RiftFirstCastDamageUp` · `Se_Star_D_ScalingAbilityPower` · `Se_Star_D_ScalingAttackDamage` · `Se_Star_D_ScalingAttackSpeedWithPenalty` · `Se_Star_D_ShieldDamageAmp` · `Se_Star_Husk_D_DamageAmpOnLowHpTarget` · `Se_Star_Husk_D_DamageOverTimeCritWithPenalty` · `Se_Star_Husk_D_DarkAttackWithPenalty` · `Se_Star_Husk_D_ScalingAdAndAtkSpd` · `Se_Star_Husk_F_AS_AddedDurationOnHit` · `Se_Star_Husk_F_DE_MarkHitDodgeCDR` · `Se_Star_Husk_I_ShopIntimidation` · `Se_Star_Husk_L_DodgeChargesAndRangeWithPenalty` · `Se_Star_I_AdditionalChaosChance` · `Se_Star_I_DismantleBonus` · `Se_Star_I_DismantleReroll` · `Se_Star_I_ExtraChaosOptionGoldOnUse` · `Se_Star_I_GemOnMiniBossKill` · `Se_Star_I_GoldPerCrit` · `Se_Star_I_GoldRiskAndReturn` · `Se_Star_I_KillGoldBonus` · `Se_Star_L_DamageReductionFromChilled` · `Se_Star_L_DodgeCooldownOnLowHealth` · `Se_Star_L_ElementalResistance` · `Se_Star_L_HealOnAttack` · `Se_Star_L_HealOnKill` · `Se_Star_L_MaxHealthUpHealDown` · `Se_Star_L_PotionChance` · `Se_Star_L_PotionHealAmount` · `Se_Star_L_PotionOnBuyOrSell` · `Se_Star_L_ReceivedHealingAndShieldBonus` · `Se_Star_L_ScalingMaxHealth` · `Se_Star_Lacerta_D_AttackRange` · `Se_Star_Lacerta_F_HC_NoDelayDoubleCast` · `Se_Star_Lacerta_F_IR_RechargeAmmoAmpBurnDamage` · `Se_Star_Lacerta_I_ShopDiscount` · `Se_Star_Lacerta_I_ShopMoreItemsWithPenalty` · `Se_Star_Mist_D_BonusOnDash` · `Se_Star_Mist_D_BossDamageOnHighHp` · `Se_Star_Mist_D_HunterDamage` · `Se_Star_Mist_D_ScalingAD` · `Se_Star_Mist_F_PR_ShieldAndCrit` · `Se_Star_Mist_I_BonusOnCatPet` · `Se_Star_Mist_L_AddedDodgeWithPenalty` · `Se_Star_Mist_L_MovSpeed` · `Se_Star_Mist_L_PotionShield` · `Se_Star_Nachia_D_CanineLover` · `Se_Star_Nachia_F_SC_AtkSpd` · `Se_Star_Nachia_F_SC_SummonDmgReduction` · `Se_Star_Nachia_I_ForestKillDreamDust` · `Se_Star_Nachia_I_SummonKillGold` · `Se_Star_Nachia_L_AllyUnstoppable` · `Se_Star_Nachia_L_HealAndShieldAmp` · `Se_Star_Nachia_L_SummonBonus` · `Se_Star_Vesper_D_ADWithNearbyBurning` · `Se_Star_Vesper_D_BossHunterAmpWithPenalty` · `Se_Star_Vesper_D_ConvertAPToAD` · `Se_Star_Vesper_F_DP_FarTargetBonus` · `Se_Star_Vesper_L_FireResistance` · `Se_Star_Vesper_L_ScalingArmor` · `Se_Star_Vesper_L_ScalingHealth` · `Se_Star_Yubar_D_APOnDodge` · `Se_Star_Yubar_D_BonusDamageToLight` · `Se_Star_Yubar_D_ConvertADToAP` · `Se_Star_Yubar_D_ScalingAP` · `Se_Star_Yubar_F_TQ_LowerCooldownNoInvul` · `Se_Star_Yubar_I_StarCookie` · `Se_StarlessPath_PowerOfGuidance` · `Se_Treasure_CrimsonElixir_AdBoost` · `Se_Treasure_FragmentOfDetermination_Invulnerable` · `Se_U_BeamOfBalance` · `Se_U_Burrow` · `Se_U_HerWorld_Blackhole` · `Se_U_Hysteria` · `Se_UsingShortcut` · `Se_WaypointTeleport` · [ShieldEffect](/api/Global.ShieldEffect) · [Shrine](/api/Global.Shrine) · `Shrine_AltarOfCleansing` · `Shrine_AncientRemnants` · `Shrine_Anitya` · `Shrine_ArtifactGiver` · `Shrine_Ascension` · `Shrine_BlessedGuidance` · `Shrine_BossSoul` · `Shrine_BrokenWoodenDoll` · `Shrine_CallOfTheRavenous` · `Shrine_Chaos` · `Shrine_Concept` · `Shrine_CookingPot` · `Shrine_CorruptedChaos` · `Shrine_DebugTeleport` · `Shrine_Despair` · `Shrine_Despair_Vestige` · `Shrine_Destiny` · `Shrine_Disintegration` · `Shrine_DreamdustBit` · `Shrine_DreamdustBox` · `Shrine_Entanglement` · `Shrine_FragmentOfRadiance` · `Shrine_GoldBit` · `Shrine_GoldBox` · `Shrine_Guidance` · `Shrine_Hatred` · `Shrine_Hatred_Old` · `Shrine_Hatred_Reward` · `Shrine_HeroSoul` · `Shrine_HiddenStash` · `Shrine_InvitationOfJonasMeeting` · `Shrine_LoopCat` · `Shrine_Luck` · `Shrine_MarshOfDestiny_SeedOfTorment` · `Shrine_MawOfDoom` · `Shrine_Memory` · `Shrine_Merchant_Backpack` · `Shrine_MirrorOfRemorse` · `Shrine_MorasDomain_HerPresence` · `Shrine_PileOfSnow` · `Shrine_Polaris_Teleporter` · `Shrine_PotOfGreed` · `Shrine_PrimusDoor` · `Shrine_PrimusEndingLightPillar` · `Shrine_PyranasLove` · `Shrine_Se_Star_Bismuth_I_KnowledgeBook_Book` · `Shrine_SmallSoul` · `Shrine_StarCookie` · `Shrine_Stardust` · `Shrine_StarlessPath_EndingRift` · `Shrine_StrayMemory_StartProp` · `Shrine_TheConsortOfNight` · `Shrine_TheConsortOfNight_Rift` · `Shrine_WagesOfResolve` · [SkillTrigger](/api/Global.SkillTrigger) · `Sky_BossIntruder` · `Sky_LightFogDamager` · `Sky_NightWaterEffect` · `Sky_NightWaterEffect_RippleCreator` · `SnowMountain_SecretPlaceTriggerInstance` · `SpawnGemStarProp` · [SpawnManager](/api/Global.SpawnManager) · [SpecialEntityRoomModifier](/api/Global.SpecialEntityRoomModifier) · `St_C_LuckyHammer` · `St_C_SpearThrow` · `St_C_Starfall` · `St_D_BurningFist` · `St_D_CircleOfLife` · `St_D_DanceOfValor` · `St_D_DisintegratingClaw` · `St_D_ExplosionArtist` · `St_D_FrostTouch` · `St_D_HeartOfThePack` · `St_D_IceColdPresence` · `St_D_IcyVeins` · `St_D_MercyOfEl` · `St_D_MomentumOfCombat` · `St_D_ParryMaster` · `St_D_QuartetOfDeath` · `St_D_Resolve` · `St_D_RoaringFist` · `St_D_SalamanderPowder` · `St_D_ScarOfTheWind` · `St_D_SharedPain` · `St_D_ThirstOfVengence` · `St_E_ChainLightning` · `St_E_Harvest` · `St_E_Rewind` · `St_L_CoinExplosion` · `St_L_HerosReturn` · `St_L_SmallMoltenCore` · `St_L_SoulKiller` · `St_QR_ValiantHeart` · `St_Q_Discipline` · `St_Q_GoldenBurst` · `St_Q_Laceration` · `St_Q_MoonlightPact` · `St_Q_Reduction` · `St_R_DangerousTheory` · `St_R_FlamingWhip` · `St_R_LightningDance` · `St_R_Somersault` · `St_U_ShoutOfOblivion` · [StarEffect](/api/Global.StarEffect) · `Star_Global_AbilityPower` · `Star_Global_AttackDamage` · `Star_Global_AttackSpeed` · `Star_Global_DarkAmp` · `Star_Global_DecreaseDamageFromChilled` · `Star_Global_ElementResistance` · `Star_Global_FireAmp` · `Star_Global_LightAmp` · `Star_Global_MaxHealth` · `Star_Global_SkillHaste` · `Star_Global_Tenacity` · `Star_Lacerta_AttackRange` · `Star_Lacerta_AttackSpeed` · `Star_Lacerta_FireAmp` · `Star_Lacerta_HandCannon` · `Star_Lacerta_QuickTrigger` · `Star_Mist_AddAttackDamage` · `Star_Mist_LongerLunge` · `Star_Mist_MovementSpeed` · `Star_Vesper_MaxHealth` · `Star_Yubar_AbilityPower` · `Star_Yubar_SkillHaste` · `Star_Yubar_StrongerCataclysm` · `Star_Yubar_StrongerSuperNova` · `Star_Yubar_TranquilityDamage` · `StarlessPath_BossPolarisManager` · [StatusEffect](/api/Global.StatusEffect) · `StatusEffectRandomPickupInstance` · `Sum_L_SmallMoltenCore_Dragon` · `Sum_Q_SylvanCall_LeafHound` · `Sum_R_AnnoyingBanner` · `Sum_R_SummonLittleBaam_Baam` · [Summon](/api/Global.Summon) · `Trap_FlameJet` · `Treasure_SparklingElixir` · `Treasure_SuspiciousHat` · [TriggerChannelData](/api/Global.TriggerChannelData) · [TriggerConfig](/api/Global.TriggerConfig) · `UI_ControllerDisconnectedIndicator` · `UI_DamageNumberGroup` · `UI_DamageNumberText` · `UI_Dev_ConsoleSelectedEntityInfo` · `UI_EntityBar` · `UI_EntityCrowdControl` · `UI_EntityCursed` · `UI_EntityDestroyOnDeath` · `UI_EntityDreamDust` · `UI_EntityElementals` · `UI_EntityFollow` · `UI_EntityGenericStackIndicator` · `UI_EntityGold` · `UI_EntityHealthBar` · `UI_EntityHealthBarGroup` · `UI_EntityHealthBarMain` · `UI_EntityLevel` · `UI_EntityManaBar` · `UI_EntityName` · `UI_EntityPlatinumCoin` · `UI_EntityPrimaryStats` · `UI_EntityProtected` · `UI_EntityProvider` · `UI_EntitySummonDuration` · `UI_EntityTalk` · `UI_EntityUnstoppable` · `UI_HealthBar_Simple` · `UI_InGame_BossBars` · `UI_InGame_BossBars_Item` · `UI_InGame_Conversations_Instance` · `UI_InGame_CooldownTimeNotification` · `UI_InGame_FollowAndFaceHero_Conversation` · `UI_InGame_HeroDetailWindow` · `UI_InGame_HeroDetailWindow_StatItem` · `UI_InGame_HeroInfoBar` · `UI_InGame_Map` · `UI_InGame_Map_Item_Entity` · `UI_InGame_OffscreenIndicator` · `UI_InGame_OffscreenIndicator_Item_Entity` · `UI_InGame_PartyDisplay_Item` · `UI_InGame_Scoreboard_PlayerItem` · `UI_InGame_SkillButton` · `UI_InGame_SpectateIndicator` · `UI_InGame_StatusEffectIcons` · `UI_Tooltip_SkillStarDescriber` · `UI_Tooltip_SkillStarDescriber_Item` · [ZoneManager](/api/Global.ZoneManager)

### Dependencies (28)

*Types and components that `Entity` references or depends upon:*

[Actor](/api/Global.Actor) · [ControlManager](/api/Global.ControlManager) · [CustomAIBehaviors](/api/Global.CustomAIBehaviors) · [DataProcessorGroup`3](/api/Global.DataProcessorGroup`3) · [DataProcessor`3](/api/Global.DataProcessor`3) · [DewPhysics](/api/Global.DewPhysics) · [DewPlayer](/api/Global.DewPlayer) · [DewPool](/api/Global.DewPool) · [EntityAI](/api/Global.EntityAI) · [EntityAIContext](/api/Global.EntityAIContext) · [EntityAbility](/api/Global.EntityAbility) · [EntityAnimation](/api/Global.EntityAnimation) · [EntityComponent](/api/Global.EntityComponent) · [EntityControl](/api/Global.EntityControl) · [EntitySound](/api/Global.EntitySound) · [EntityStatus](/api/Global.EntityStatus) · [EntityVisual](/api/Global.EntityVisual) · [EventInfoDamage](/api/Global.EventInfoDamage) · [EventInfoKill](/api/Global.EventInfoKill) · [IInteractable](/api/Global.IInteractable) · [ListReturnHandle`1](/api/Global.ListReturnHandle`1) · [ManagerBase`1](/api/Global.ManagerBase`1) · [NetworkedManagerBase`1](/api/Global.NetworkedManagerBase`1) · [RoomSection](/api/Global.RoomSection) · [SafeAction`1](/api/Global.SafeAction`1) · `ToListNonAllocExtensions` · `Vector3FlattenExtension` · `Mirror.GeneratedNetworkCode`

### Related Enums (3)

*Enumerations referenced in fields, properties, or method signatures:*

[`EntityRelation`](/enums#entityrelation) · [`SaveVarFlags`](/enums#savevarflags) · [`TeamRelation`](/enums#teamrelation)

:::
