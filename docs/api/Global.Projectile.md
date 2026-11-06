# Class: Projectile

- **Category:** <span class="cat-dot" style="--cat-color: #ef4444" data-cat="Combat & Abilities"></span> Combat & Abilities
- **Namespace:** `Global`
- **Assembly:** `Dew.Core.dll`
- **Inheritance / Derived:** [DewNetworkBehaviour](/api/Global.DewNetworkBehaviour) → [Actor](/api/Global.Actor) → [AbilityInstance](/api/Global.AbilityInstance) → [StandardProjectile](/api/Global.StandardProjectile)

```csharp
public abstract class Projectile : AbilityInstance, ILogicUpdate, ICleanup, ICustomDestroyRoutine
```

## Fields (23)

::: details Click to expand Fields (23)

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`_estimatedVelocity`** | `protected Vector3 _estimatedVelocity` |  |
| **`canCollideMidFlight`** | `[BoxGroup("Projectile Settings", true, false, 0)] [LabelText("Can Collide With Entity Mid-Flight")] [ToggleLeft] public bool canCollideMidFlight` |  |
| **`collisionRadius`** | `[Title("Collisions", null, TitleAlignments.Left, true, true)] [BoxGroup("Projectile Settings", true, false, 0)] public float collisionRadius` |  |
| **`collisionTargets`** | `[ShowIf("canCollideMidFlight", true)] [BoxGroup("Projectile Settings", true, false, 0)] public AbilityTargetValidator collisionTargets` |  |
| **`customEndHeight`** | `[ShowIf("@mode != Projectile.ProjectileMode.Target && !endsWithSameHeight", true)] [BoxGroup("Projectile Settings", true, false, 0)] public float customEndHeight` |  |
| **`destroyOnComplete`** | `[FormerlySerializedAs] [FormerlySerializedAs("killOnComplete")] [BoxGroup("Projectile Settings", true, false, 0)] public bool destroyOnComplete` |  |
| **`dissipateOnTerrain`** | `[BoxGroup("Projectile Settings", true, false, 0)] [ToggleLeft] public bool dissipateOnTerrain` |  |
| **`effectOnComplete`** | `[BoxGroup("Projectile Settings", true, false, 0)] [LabelText("Complete")] public GameObject effectOnComplete` |  |
| **`effectOnDissipate`** | `[BoxGroup("Projectile Settings", true, false, 0)] [LabelText("Dissipate")] public GameObject effectOnDissipate` |  |
| **`effectOnEntity`** | `[BoxGroup("Projectile Settings", true, false, 0)] [LabelText("Entity")] public GameObject effectOnEntity` |  |
| **`effectOnFly`** | `[Title("Effects", null, TitleAlignments.Left, true, true)] [BoxGroup("Projectile Settings", true, false, 0)] [LabelText("Fly")] public GameObject effectOnFly` |  |
| **`endDistance`** | `[SyncVar] [ShowIf("@mode == Projectile.ProjectileMode.Direction", true)] [BoxGroup("Projectile Settings", true, false, 0)] public float endDistance` |  |
| **`endsWithSameHeight`** | `[ShowIf("@mode != Projectile.ProjectileMode.Target", true)] [BoxGroup("Projectile Settings", true, false, 0)] public bool endsWithSameHeight` |  |
| **`horizontalOffsetOverTrajectory`** | `[LabelText("Horizontal Offset")] [BoxGroup("Projectile Settings", true, false, 0)] public AnimationCurve horizontalOffsetOverTrajectory` |  |
| **`killOnDissipate`** | `[BoxGroup("Projectile Settings", true, false, 0)] public bool killOnDissipate` |  |
| **`mode`** | `[SyncVar] [Title("Flight", null, TitleAlignments.Left, true, true)] [EnumToggleButtons] [BoxGroup("Projectile Settings", true, false, 0)] public Projectile.ProjectileMode mode` |  |
| **`onEntity`** | `public SafeAction<Projectile.EntityHit> onEntity` |  |
| **`rotationType`** | `[LabelText("Rotation")] [EnumToggleButtons] [BoxGroup("Projectile Settings", true, false, 0)] public Projectile.RotationType rotationType` |  |
| **`scaleHorizontalOffsetOnLength`** | `[LabelText("Scale On Trajectory Length")] [BoxGroup("Projectile Settings", true, false, 0)] public bool scaleHorizontalOffsetOnLength` |  |
| **`scaleVerticalOffsetOnLength`** | `[LabelText("Scale On Trajectory Length")] [BoxGroup("Projectile Settings", true, false, 0)] public bool scaleVerticalOffsetOnLength` |  |
| **`start`** | `[SyncVar] [EnumToggleButtons] [BoxGroup("Projectile Settings", true, false, 0)] public Projectile.StartPositionType start` |  |
| **`startInFrontDistance`** | `[SyncVar] [LabelText("Front Distance")] [BoxGroup("Projectile Settings", true, false, 0)] public float startInFrontDistance` |  |
| **`verticalOffsetOverTrajectory`** | `[LabelText("Vertical Offset")] [BoxGroup("Projectile Settings", true, false, 0)] public AnimationCurve verticalOffsetOverTrajectory` |  |

:::

## Properties (4)

::: details Click to expand Properties (4)

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`isCompleted`** | `public bool isCompleted { get; }` | Did this projectile complete its course? |
| **`isFlying`** | `public bool isFlying { get; }` | Is this projectile still flying over its course? |
| **`targetEntity`** | `protected Entity targetEntity { get; }` |  |
| **`targetPosition`** | `protected Vector3 targetPosition { get; set; }` | It is recommended to edit this only in OnPrepare. |

:::

## Methods (19)

::: details `AddEffect(AddEffectTarget, GameObject)`

Locally add an effect.Given effect will be instantiated and set/added to this projectile.

```csharp
public void AddEffect(Projectile.AddEffectTarget target, GameObject eff)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `target` | [`Projectile.AddEffectTarget`](/api/Global.Projectile) |  |
| `eff` | `UnityEngine.GameObject` |  |

:::

::: details `CalculateOffsetOverTrajectoryInWorldSpace(float, Quaternion)`

```csharp
protected Vector3 CalculateOffsetOverTrajectoryInWorldSpace(float normalizedPosition, Quaternion rotation)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `normalizedPosition` | `float` |  |
| `rotation` | `UnityEngine.Quaternion` |  |

**Returns:** `UnityEngine.Vector3`

:::

::: details `CheckForCompletion()`

```csharp
protected virtual bool CheckForCompletion()
```

**Returns:** `bool`

:::

::: details `Dissipate()`

Dissipate this projectile.

```csharp
public void Dissipate()
```

:::

::: details `FrameUpdate()`

```csharp
public override void FrameUpdate()
```

:::

::: details `GetTargetWorldPosition()`

```csharp
protected virtual Vector3 GetTargetWorldPosition()
```

**Returns:** `UnityEngine.Vector3`

:::

::: details `LogicUpdate(float)`

```csharp
public override void LogicUpdate(float dt)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `dt` | `float` |  |

:::

::: details `OnComplete()`

Called on server when this Projectile fully completes its path without being despawned by itself/dissipated.Default behaviour instantiates a neweffectOnCompleteeffect using the position and rotation of this projectile on every clients, and stopseffectOnFlyeffect.It will also kill this projectile ifkillOnCompleteis set.Note: On targeted projectiles, normallyOnEntitywill be fired beforeOnComplete. It might fire differently if for example the projectile is detached or the target became an invalid target.

```csharp
protected virtual void OnComplete()
```

:::

::: details `OnCreate()`

```csharp
protected override void OnCreate()
```

:::

::: details `OnDestroyActor()`

```csharp
protected override void OnDestroyActor()
```

:::

::: details `OnDisable()`

```csharp
protected override void OnDisable()
```

:::

::: details `OnDissipate()`

Called on server when this Projectile is dissipated by an outer source. e.g. Projectile Absorbing WallDefault behaviour instantiates a neweffectOnDissipateeffect using the position and rotation of this projectile on every clients

```csharp
protected virtual void OnDissipate()
```

:::

::: details `OnEntity(EntityHit)`

Called on server when this Projectile in server detects a collision with an Entity.Default behaviour instantiates a neweffectOnEntityeffect at the hit point with the rotation of this projectile attached to the entity on every clients.

```csharp
protected virtual void OnEntity(Projectile.EntityHit hit)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `hit` | [`Projectile.EntityHit`](/api/Global.Projectile) |  |

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

::: details `PositionSolver(float)`

```csharp
protected abstract Vector3 PositionSolver(float dt)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `dt` | `float` |  |

**Returns:** `UnityEngine.Vector3`

:::

::: details `RotationSolver(float)`

```csharp
protected virtual Quaternion RotationSolver(float dt)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `dt` | `float` |  |

**Returns:** `UnityEngine.Quaternion`

:::

::: details `SetCustomStartPosition(Vector3)`

Set custom start position for projectiles with 'Custom' start position mode. Call this in OnPrepare.

```csharp
public void SetCustomStartPosition(Vector3 pos)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `pos` | `UnityEngine.Vector3` |  |

:::

::: details `StopFlying()`

Stop this projectile and itseffectOnFlyeffect. This will also make this projectile instantly stop checking collisions. Note that this does not callOnCompletenorOnDissipate.

```csharp
protected void StopFlying()
```

:::


## Architecture & Relationships

::: details Click to expand Architecture & Relationships

### Used By (113)

*Classes and systems that invoke, reference, or depend on `Projectile`:*

`Ai_Atk_LacertaRifle` · `Ai_Atk_LacertaRifle_Crit` · `Ai_C_BackStep_Bomb` · `Ai_C_DarkBolt` · `Ai_C_IceBlock_Projectile` · `Ai_C_Pew_Projectile` · `Ai_C_Purgatory_Heal` · `Ai_C_SparklingWaterGun` · `Ai_C_Starfall_Projectile` · `Ai_D_BeautifulThreat_Feather` · `Ai_D_ChargedAnguillian_Lightning` · `Ai_D_ExoticMatter_Projectile` · `Ai_D_SalamanderPowder_Projectile` · `Ai_E_ChainLightning` · `Ai_E_CrimsonLance` · `Ai_E_DoomsdayMeteor_SubProjectile` · `Ai_E_FlameJet_Projectile` · `Ai_E_MysticDagger` · `Ai_E_ShadowVolley_Projectile` · `Ai_Gem_C_Charcoal_Projectile` · `Ai_Gem_C_Sharp_Arrow` · `Ai_Gem_C_Vengence_Projectile` · `Ai_Gem_E_Domination_CritGainEffect` · `Ai_Gem_E_Fangs_Projectile` · `Ai_Gem_L_Embertail_Projectile` · `Ai_Gem_L_PureWhite_Projectile` · `Ai_Gem_R_Accuracy_Projectile` · `Ai_Gem_R_Dusk_Projectile` · `Ai_Gem_R_Ricochet` · `Ai_Gem_R_Shock_Lightning` · `Ai_Gem_R_Snow_Projectile` · `Ai_Gem_R_Spiral_Fireball` · `Ai_Gem_U_GlacialCore_Projectile` · `Ai_Gem_U_GuidingCompass_PowerGainProjectile` · `Ai_L_CoinExplosion_Coin` · `Ai_L_MentalCorruption_Projectile` · `Ai_L_Multishot_Arrow` · `Ai_L_SmallMoltenCore_Dragon_Atk` · `Ai_L_SpectreBullet` · `Ai_MiniBoss_BloodThorn_Projectile` · `Ai_MiniBoss_OrbSpitter_Orb` · `Ai_MiniBoss_SpinningArrow_Arrow` · `Ai_MirageSkin_Delusion_Missile` · `Ai_MirageSkin_Oblivion_Orb` · `Ai_Mon_DarkCave_BossSeeker_Atk_Projectile` · `Ai_Mon_DarkCave_BossSeeker_GreenChaserOrb` · `Ai_Mon_DarkCave_DarkElemental_Atk_Projectile` · `Ai_Mon_DarkCave_DarkElemental_Barrage_Arrow` · `Ai_Mon_DarkCave_NightOlm_Atk_Projectile` · `Ai_Mon_Despair_BossAzurak_StompBlock_Artillery` · `Ai_Mon_Despair_BossAzurak_StompProjectile_Projectile` · `Ai_Mon_Despair_ParalyticFly_Paralyze` · `Ai_Mon_Despair_WretchedArtillery_BarrageAtk_Missile` · `Ai_Mon_Forest_BossDemon_MainSkill_SpawnMissiles_Missile` · `Ai_Mon_Forest_SpiderSpitter_Atk` · `Ai_Mon_Ink_BossDarkMoon_SpawnEgoSword_Projectile` · `Ai_Mon_Ink_BossDarkMoon_ThrowSpear_Projectile` · `Ai_Mon_Ink_BossDarkMoon_ThrowSpear_TeleportAtk_AfterAtk` · `Ai_Mon_Ink_BossWhiteNight_AltAtk` · `Ai_Mon_Ink_Boss_OnDeath` · `Ai_Mon_Ink_GhostBlade_SwiftStep_Projectile` · `Ai_Mon_LavaLand_BossInfernus_BreathFire_Projectile` · `Ai_Mon_LavaLand_BossInfernus_Roar_Projectile` · `Ai_Mon_LavaLand_InfernoSpider_LavaAtk` · `Ai_Mon_LavaLand_Magmadon_Charge_Projectile` · `Ai_Mon_Primus_BossPrimusAeron_Adapt_Arbalest_Projectile` · `Ai_Mon_Primus_BossPrimusAeron_Adapt_Atk` · `Ai_Mon_Primus_BossPrimusAeron_Adapt_Doom_Meteor_SubFireball` · `Ai_Mon_Sky_StarSeed_SelfDestruct_Projectile` · `Ai_Mon_SnowMountain_Scavenger_Throw` · `Ai_Mon_Special_AmbushSpawner_Projectile` · `Ai_Mon_Special_BossErebos_StarRain_Instance` · `Ai_Mon_Special_BossMaw_AnnihilationStance_Instance` · `Ai_Mon_Special_BossMaw_PillarOfFlame_Projectile` · `Ai_Mon_Special_BossMaw_PrecisionShot_Projectile` · `Ai_Mon_Special_BossMaw_Purgatory_Heal` · `Ai_Mon_Special_BossMaw_ScatterShot_ShortProjectile` · `Ai_Mon_Special_BossMaw_ShadowOverdrive_Projectile` · `Ai_Mon_Special_BossObliviax_TurnAtk_Projectile` · `Ai_Mon_Special_BossObliviax_TurretMode_Projectile` · `Ai_Mon_Special_BossPolaris_Holy_Atk_Projectile` · `Ai_Mon_Special_BossPolaris_Holy_CounterSpell_DisarmProjectile` · `Ai_Mon_Special_BossPolaris_Holy_GoldenSpear_Projectile` · `Ai_Mon_Special_BossPolaris_Holy_Purgatory_HealProjectile` · `Ai_QR_Innocence_Projectile` · `Ai_Q_BigBorealChunk_Projectile` · `Ai_Q_DeathMark_Projectile` · `Ai_Q_EtherealInfluence_Projectile_Base` · `Ai_Q_EtherealInfluence_Projectile_Forward` · `Ai_Q_IncendiaryRounds_Attack` · `Ai_Q_Reduction_Projectile` · `Ai_R_AnnihilationStance_Projectile` · `Ai_R_BlackArbalest` · `Ai_R_DarkGrenade_Shard` · `Ai_R_DarkGrenade_ShardSpawner` · `Ai_R_OrbOfLight_BackwardHealing` · `Ai_R_OrbOfLight_ForwardDamaging` · `Ai_R_Parry_Projectile` · `Ai_R_PrecisionShot_Projectile` · `Ai_R_QuickTrigger_Projectile` · `Ai_R_RepulsiveShield_Projectile` · `Ai_R_Scattershot_Projectile` · `Ai_R_SerpentineBlessing_Projectile` · `Ai_R_ShadowOverdrive_Projectile` · `Ai_R_ShadowWalk_Projectile` · `Ai_RandomGemUpgrade` · `Ai_RegenOrb_Projectile` · `Ai_StarCookie_Projectile` · `Ai_Star_Bismuth_D_BonusAttackEffect_Arrow` · `Ai_UnstableRatSwarm_Projectile` · [AttackProjectile](/api/Global.AttackProjectile) · [CollidableHit](/api/Global.CollidableHit) · [StandardProjectile](/api/Global.StandardProjectile)

### Dependencies (18)

*Types and components that `Projectile` references or depends upon:*

[AbilityInstance](/api/Global.AbilityInstance) · [AbilityTargetValidator](/api/Global.AbilityTargetValidator) · [Actor](/api/Global.Actor) · [ArrayReturnHandle`1](/api/Global.ArrayReturnHandle`1) · [CastInfo](/api/Global.CastInfo) · [Dew](/api/Global.Dew) · [DewEffect](/api/Global.DewEffect) · [DewNetworkBehaviour](/api/Global.DewNetworkBehaviour) · [DewPhysics](/api/Global.DewPhysics) · [DewPool](/api/Global.DewPool) · [Entity](/api/Global.Entity) · [EntityStatus](/api/Global.EntityStatus) · [EntityVisual](/api/Global.EntityVisual) · [ICollidableWithProjectile](/api/Global.ICollidableWithProjectile) · [SafeAction`1](/api/Global.SafeAction`1) · `Vector3FlattenExtension` · `VectorPlaneTransformExtension` · `Mirror.GeneratedNetworkCode`

:::
