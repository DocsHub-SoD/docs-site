# Class: EntityVisual

- **Category:** <span class="cat-dot" style="--cat-color: #22c55e" data-cat="Actors & Entities"></span> Actors & Entities
- **Namespace:** `Global`
- **Assembly:** `Dew.Core.dll`
- **Attributes:** `[RequireComponent] [LogicUpdatePriority]`
- **Inheritance / Derived:** [DewNetworkBehaviour](/api/Global.DewNetworkBehaviour) → [EntityComponent](/api/Global.EntityComponent)

```csharp
[HideMonoScript]
[RequireComponent(typeof(EntityHighlightProvider))]
[LogicUpdatePriority(-299)]
public class EntityVisual : EntityComponent, ILogicUpdate, ICleanup
```

## Fields (31)

::: details Click to expand Fields (31)

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`accessoryInstances`** | `[NonSerialized] public List<Accessory> accessoryInstances` |  |
| **`ClientEvent_OnGroundMarkerHiddenChanged`** | `public SafeAction<bool> ClientEvent_OnGroundMarkerHiddenChanged` |  |
| **`ClientEvent_OnModelLoaded`** | `public SafeAction ClientEvent_OnModelLoaded` |  |
| **`ClientEvent_OnRendererEnabledChanged`** | `public SafeAction<bool> ClientEvent_OnRendererEnabledChanged` |  |
| **`ClientEvent_OnSpawnComplete`** | `public SafeAction ClientEvent_OnSpawnComplete` | Called when the entity finishes spawning or spawning is skipped. |
| **`dazeAfterSpawnDuration`** | `public float dazeAfterSpawnDuration` |  |
| **`delayLoopEffectTilSpawned`** | `[FormerlySerializedAs] [LabelText("Delay Loop Effect Until Spawned")] [FormerlySerializedAs("delayStartEffectTilSpawned")] [ToggleLeft] public bool delayLoopEffectTilSpawned` |  |
| **`delaySpawnEffectOnGroundTilSpawned`** | `[LabelText("Delay Until Spawned")] [ShowIf("@spawnEffectOnGround != null", true)] public bool delaySpawnEffectOnGroundTilSpawned` |  |
| **`delaySpawnEffectUntilSpawned`** | `[LabelText("Delay Until Spawned")] [ShowIf("@spawnEffect != null", true)] public bool delaySpawnEffectUntilSpawned` |  |
| **`disableModelTransformUpdate`** | `[NonSerialized] public bool disableModelTransformUpdate` |  |
| **`doPositionOffset`** | `public bool doPositionOffset` |  |
| **`doScaling`** | `public bool doScaling` |  |
| **`invisibleByDefault`** | `[SyncVar] [NonSerialized] public bool invisibleByDefault` | Set this true on before spawn to make entities invisible by default, appearing after EnableRenderers is called. |
| **`invulnerableWhileSpawning`** | `public bool invulnerableWhileSpawning` |  |
| **`mirageSkinObjects`** | `public Dictionary<string, List<GameObject>> mirageSkinObjects` |  |
| **`model`** | `[NonSerialized] public EntityModel model` |  |
| **`modelTransform`** | `[NonSerialized] public Transform modelTransform` |  |
| **`renderers`** | `[NonSerialized] public List<Renderer> renderers` |  |
| **`skipSpawning`** | `[SyncVar] [NonSerialized] public bool skipSpawning` | Set this true on before spawn to make entities pop in instead of play its spawning effects, voices and animations. |
| **`solidRenderers`** | `[NonSerialized] public List<Renderer> solidRenderers` |  |
| **`spawnAnim`** | `public DewAnimationClip spawnAnim` |  |
| **`spawnDuration`** | `[SyncVar] [Title("Spawn", null, TitleAlignments.Left, true, true)] public float spawnDuration` |  |
| **`spawnEffect`** | `[Title("Effects", null, TitleAlignments.Left, true, true)] public GameObject spawnEffect` |  |
| **`spawnEffectOnGround`** | `public GameObject spawnEffectOnGround` |  |
| **`spawnXOffset`** | `[ShowIf("doPositionOffset", true)] public AnimationCurve spawnXOffset` |  |
| **`spawnXScale`** | `[ShowIf("doScaling", true)] [LabelText("@useSeparateAxis ? \"Spawn X Scale\" : \"Spawn Scale\"")] public AnimationCurve spawnXScale` |  |
| **`spawnYOffset`** | `[ShowIf("doPositionOffset", true)] public AnimationCurve spawnYOffset` |  |
| **`spawnYScale`** | `[ShowIf("@doScaling && useSeparateAxis", true)] public AnimationCurve spawnYScale` |  |
| **`spawnZOffset`** | `[ShowIf("doPositionOffset", true)] public AnimationCurve spawnZOffset` |  |
| **`spawnZScale`** | `[ShowIf("@doScaling && useSeparateAxis", true)] public AnimationCurve spawnZScale` |  |
| **`useSeparateAxis`** | `[ShowIf("doScaling", true)] public bool useSeparateAxis` |  |

:::

## Properties (13)

::: details Click to expand Properties (13)

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`currentYOffset`** | `public float currentYOffset { get; }` |  |
| **`currentYVelocity`** | `public float currentYVelocity { get; }` |  |
| **`etLocalOffset`** | `public Vector3 etLocalOffset { get; }` |  |
| **`etRotation`** | `public Quaternion etRotation { get; }` |  |
| **`etScaleMultiplier`** | `public Vector3 etScaleMultiplier { get; }` |  |
| **`etWorldOffset`** | `public Vector3 etWorldOffset { get; }` |  |
| **`genericStackIndicatorMax`** | `public int genericStackIndicatorMax { get; set; }` |  |
| **`genericStackIndicatorValue`** | `public int genericStackIndicatorValue { get; set; }` |  |
| **`highlight`** | `public EntityHighlightProvider highlight { get; }` |  |
| **`isGroundMarkerHidden`** | `public bool isGroundMarkerHidden { get; }` |  |
| **`isRendererOff`** | `public bool isRendererOff { get; }` |  |
| **`isSpawning`** | `public bool isSpawning { get; }` |  |
| **`materials`** | `public IReadOnlyList<Material> materials { get; }` | List of this entity's materials. (Instantiated) |

:::

## Methods (53)

::: details `AddSharedMaterialLocal(Material)`

Locally add a material to all mesh renderers of this entity.

```csharp
public void AddSharedMaterialLocal(Material material)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `material` | `UnityEngine.Material` |  |

:::

::: details `Awake()`

```csharp
protected override void Awake()
```

:::

::: details `DisableRenderers()`

Make this entity invisible by turning off all renderers everywhere.

```csharp
public void DisableRenderers()
```

:::

::: details `DisableRenderersLocal()`

Locally make this entity invisible by turning off all renderers.

```csharp
public void DisableRenderersLocal()
```

:::

::: details `EnableRenderers()`

Undo this entity'sDisableRenderers()and make it visible again everywhere.

```csharp
public void EnableRenderers()
```

:::

::: details `EnableRenderersLocal()`

Locally undo this entity'sDisableRenderers()and make it visible again.

```csharp
public void EnableRenderersLocal()
```

:::

::: details `FixClothes()`

```csharp
public void FixClothes()
```

:::

::: details `FixTails()`

```csharp
public void FixTails()
```

:::

::: details `FixTailsAndClothes()`

Reset tails and clothes.

```csharp
public void FixTailsAndClothes()
```

:::

::: details `FrameUpdate()`

```csharp
public override void FrameUpdate()
```

:::

::: details `GetAbovePosition()`

```csharp
public Vector3 GetAbovePosition()
```

**Returns:** `UnityEngine.Vector3`

:::

::: details `GetBasePosition()`

```csharp
public Vector3 GetBasePosition()
```

**Returns:** `UnityEngine.Vector3`

:::

::: details `GetBodyBounds()`

Get bounds of renderers specified as "body" of this entity.

```csharp
public Bounds GetBodyBounds()
```

**Returns:** `UnityEngine.Bounds`

:::

::: details `GetBonePosition(HumanBodyBones)`

This will return center position if the bone couldn't be found.

```csharp
public Vector3 GetBonePosition(HumanBodyBones bone)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `bone` | `UnityEngine.HumanBodyBones` |  |

**Returns:** `UnityEngine.Vector3`

:::

::: details `GetBoneRotation(HumanBodyBones)`

This will return entity's rotation if the bone couldn't be found.

```csharp
public Quaternion GetBoneRotation(HumanBodyBones bone)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `bone` | `UnityEngine.HumanBodyBones` |  |

**Returns:** `UnityEngine.Quaternion`

:::

::: details `GetCenterPosition()`

```csharp
public Vector3 GetCenterPosition()
```

**Returns:** `UnityEngine.Vector3`

:::

::: details `GetMuzzlePosition()`

```csharp
public Vector3 GetMuzzlePosition()
```

**Returns:** `UnityEngine.Vector3`

:::

::: details `GetMuzzleRotation()`

```csharp
public Quaternion GetMuzzleRotation()
```

**Returns:** `UnityEngine.Quaternion`

:::

::: details `GetNewColorModifier()`

Gets a new color modifier for this entity. The color is applied locally.

```csharp
public EntityColorModifier GetNewColorModifier()
```

**Returns:** `EntityColorModifier`

:::

::: details `GetNewShellModifier()`

Gets a new color modifier for this entity. The color is applied locally.

```csharp
public EntityShellModifier GetNewShellModifier()
```

**Returns:** `EntityShellModifier`

:::

::: details `GetNewTransformModifier()`

Gets a new transform modifier for this entity. The transform is applied locally to its model.

```csharp
public EntityTransformModifier GetNewTransformModifier()
```

**Returns:** `EntityTransformModifier`

:::

::: details `GetRenderBounds()`

Get bounds of all solid renderers.

```csharp
public Bounds GetRenderBounds()
```

**Returns:** `UnityEngine.Bounds`

:::

::: details `GetWeaponPosition()`

```csharp
public Vector3 GetWeaponPosition()
```

**Returns:** `UnityEngine.Vector3`

:::

::: details `GetWeaponRotation()`

```csharp
public Quaternion GetWeaponRotation()
```

**Returns:** `UnityEngine.Quaternion`

:::

::: details `HideGroundMarker()`

```csharp
public void HideGroundMarker()
```

:::

::: details `HideGroundMarkerLocal()`

```csharp
public void HideGroundMarkerLocal()
```

:::

::: details `KnockUp(KnockUpStrength, bool)`

Knock up this entity everywhere.

```csharp
public void KnockUp(KnockUpStrength strength, bool isFriendly)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `strength` | [`KnockUpStrength`](/api/Global.KnockUpStrength) |  |
| `isFriendly` | `bool` |  |

:::

::: details `KnockUp(float, bool)`

Knock up this entity everywhere. Strength: 0.8(Small), 1.1(Normal), 1.5(Big)

```csharp
public void KnockUp(float strength, bool isFriendly)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `strength` | `float` |  |
| `isFriendly` | `bool` |  |

:::

::: details `LoadModelDefault()`

```csharp
public void LoadModelDefault()
```

:::

::: details `LoadModelDefaultLocal()`

```csharp
public void LoadModelDefaultLocal()
```

:::

::: details `LoadModelLocal(EntityModel)`

Locally change model of this entity. You can provide either a model in a prefab, or the default one in the spawned entity.The provided model must be fresh; it must never be the already initialized instance of EntityModel.

```csharp
public void LoadModelLocal(EntityModel m)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `m` | [`EntityModel`](/api/Global.EntityModel) |  |

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

::: details `OnDestroy()`

```csharp
protected override void OnDestroy()
```

:::

::: details `OnLateStartServer()`

```csharp
public override void OnLateStartServer()
```

:::

::: details `OnStart()`

```csharp
public override void OnStart()
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
public override void OnStop()
```

:::

::: details `OnStopServer()`

```csharp
public override void OnStopServer()
```

:::

::: details `RemoveMaterialLocal(Material)`

Locally remove a material from all mesh renderers of this entity.

```csharp
public void RemoveMaterialLocal(Material material)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `material` | `UnityEngine.Material` |  |

:::

::: details `SetShaderProperty(string, float)`

```csharp
public void SetShaderProperty(string key, float value)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `key` | `string` |  |
| `value` | `float` |  |

:::

::: details `SetShaderProperty(string, Color)`

```csharp
public void SetShaderProperty(string key, Color value)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `key` | `string` |  |
| `value` | `UnityEngine.Color` |  |

:::

::: details `SetShaderPropertyLocal(int, float)`

```csharp
public void SetShaderPropertyLocal(int propertyId, float value)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `propertyId` | `int` |  |
| `value` | `float` |  |

:::

::: details `SetShaderPropertyLocal(int, Color)`

```csharp
public void SetShaderPropertyLocal(int propertyId, Color value)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `propertyId` | `int` |  |
| `value` | `UnityEngine.Color` |  |

:::

::: details `SetShaderPropertyLocal(string, float)`

```csharp
public void SetShaderPropertyLocal(string key, float value)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `key` | `string` |  |
| `value` | `float` |  |

:::

::: details `SetShaderPropertyLocal(string, Color)`

```csharp
public void SetShaderPropertyLocal(string key, Color value)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `key` | `string` |  |
| `value` | `UnityEngine.Color` |  |

:::

::: details `SetYOffset(float)`

```csharp
public void SetYOffset(float offset)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `offset` | `float` |  |

:::

::: details `SetYOffsetLocal(float)`

```csharp
public void SetYOffsetLocal(float offset)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `offset` | `float` |  |

:::

::: details `SetYVelocity(float)`

```csharp
public void SetYVelocity(float velocity)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `velocity` | `float` |  |

:::

::: details `SetYVelocityLocal(float)`

```csharp
public void SetYVelocityLocal(float velocity)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `velocity` | `float` |  |

:::

::: details `ShowGroundMarker()`

```csharp
public void ShowGroundMarker()
```

:::

::: details `ShowGroundMarkerLocal()`

```csharp
public void ShowGroundMarkerLocal()
```

:::

::: details `SkipSpawning()`

Cancels ongoing spawn animation of this entity.

```csharp
public void SkipSpawning()
```

:::


## Architecture & Relationships

::: details Click to expand Architecture & Relationships

### Used By (180)

*Classes and systems that invoke, reference, or depend on `EntityVisual`:*

[ActorManager](/api/Global.ActorManager) · `Ai_Atk_LacertaRifle` · `Ai_Atk_LacertaRifle_Crit` · `Ai_C_BeamOfLight` · `Ai_C_GlacialStomp` · `Ai_C_MassProtection` · `Ai_C_Whirlwind` · `Ai_Curse_AnchorOfMind_Anchor` · `Ai_E_ClutchesOfMalice_ReachAndPull` · `Ai_E_ShadowVolley_Projectile` · `Ai_E_WinterDive` · `Ai_Gem_E_Thunder` · `Ai_Gem_R_Celestial` · `Ai_L_MentalCorruption_Projectile` · `Ai_Mon_Despair_BossAzurak_DoubleStomp_Instance` · `Ai_Mon_Despair_Displacer_Blink` · `Ai_Mon_Despair_DreadBug_Jump` · `Ai_Mon_Despair_DreadBug_JumpBack` · `Ai_Mon_Despair_UnstableRat_Explosion` · `Ai_Mon_Forest_Hound_Charge` · `Ai_Mon_Forest_SpiderSpitter_Backdash` · `Ai_Mon_Forest_SpiderWarrior_Jump` · `Ai_Mon_Ink_BossDarkMoon_Blade` · `Ai_Mon_Ink_BossDarkMoon_Eclipse` · `Ai_Mon_Ink_BossDarkMoon_Hammer` · `Ai_Mon_Ink_BossWhiteNight_AltAtk` · `Ai_Mon_Ink_BossWhiteNight_DestructionWave` · `Ai_Mon_Ink_BossWhiteNight_EnergyWave_Spawner` · `Ai_Mon_Ink_Boss_OnDeath` · `Ai_Mon_Ink_GhostBlade_SwiftStep` · `Ai_Mon_LavaLand_FireElemental_Destruct` · `Ai_Mon_LavaLand_FireElemental_Explosion` · `Ai_Mon_Sky_BigBaam_BeamAtk` · `Ai_Mon_Sky_BossNyx_Blackhole` · `Ai_Mon_Sky_BossNyx_Teleport` · `Ai_Mon_Sky_LittleBaam_Reposition` · `Ai_Mon_SnowMountain_BossSkoll_Whirlwind` · `Ai_Mon_SnowMountain_IceElemental_IceBreaker` · `Ai_Mon_SnowMountain_IceElemental_IceBreaker_SubExplosion` · `Ai_Mon_SnowMountain_Scavenger_Jump` · `Ai_Mon_Special_BossErebos_StarRain_Instance` · `Ai_Mon_Special_BossMaw_AnnihilationStance` · `Ai_Mon_Special_BossMaw_Cataclysm_Spawner` · `Ai_Mon_Special_BossMaw_ChainReaction` · `Ai_Mon_Special_BossMaw_MoonlightPact` · `Ai_Mon_Special_BossMaw_PillarOfFlame_Projectile` · `Ai_Mon_Special_BossMaw_PrecisionShot` · `Ai_Mon_Special_BossObliviax_NeedleAtk_Ready` · `Ai_Mon_Special_BossPolaris_Holy_Purgatory_BurningFloor` · `Ai_Mon_Special_BossPolaris_Holy_Purgatory_Instance` · `Ai_QR_DistortedMind_Spawner` · `Ai_QR_InfernalTales` · `Ai_Q_Discipline_Stomp` · `Ai_Q_Lunge` · `Ai_Q_MoonlightPact` · `Ai_R_Scattershot_Spawner` · `Ai_RoomMod_MeteoricLife_Explosion` · `Ai_Shrine_MawOfDoom_DestroyTarget` · `Ai_UnstableRatSwarm_Projectile` · `At_Atk_YubarStardust` · `BossSeeker_SpotLightController` · [CameraManager](/api/Global.CameraManager) · [CinematicCameraHelper](/api/Global.CinematicCameraHelper) · [ControlManager](/api/Global.ControlManager) · [DamageInstance](/api/Global.DamageInstance) · `DewConsoleCommands` · [DewCutsceneDirector](/api/Global.DewCutsceneDirector) · `DewDamageNumberRenderer` · [Entity](/api/Global.Entity) · [EntityAI](/api/Global.EntityAI) · [EntityAnimation](/api/Global.EntityAnimation) · [EntityColorModifier](/api/Global.EntityColorModifier) · [EntityControl](/api/Global.EntityControl) · [EntityGroundMarker](/api/Global.EntityGroundMarker) · [EntityShellModifier](/api/Global.EntityShellModifier) · [EntitySound](/api/Global.EntitySound) · [EntityTransformModifier](/api/Global.EntityTransformModifier) · [FlavourManager](/api/Global.FlavourManager) · [FxAttachToEntity](/api/Global.FxAttachToEntity) · [FxDoFDynamicFocusDistance](/api/Global.FxDoFDynamicFocusDistance) · [FxEntityColor](/api/Global.FxEntityColor) · [FxEntityDisableRenderer](/api/Global.FxEntityDisableRenderer) · [FxEntityShake](/api/Global.FxEntityShake) · [FxEntityShell](/api/Global.FxEntityShell) · [FxEntityTransform](/api/Global.FxEntityTransform) · [FxMeshTrail](/api/Global.FxMeshTrail) · `Gem_E_Insight` · `Gem_L_Embertail` · `Gem_R_Ricochet` · [GlobalLogicPackage](/api/Global.GlobalLogicPackage) · [Hero](/api/Global.Hero) · `Hero_Bismuth_BookController` · [ISpawnableAsMiniBoss](/api/Global.ISpawnableAsMiniBoss) · `LavaLand_Lava` · [MirageSkinEffect](/api/Global.MirageSkinEffect) · `Mon_DarkCave_CaveSpider` · `Mon_DarkCave_NightOlm` · `Mon_Forest_SpiderSpitter` · `Mon_Forest_SpiderWarrior` · `Mon_GoldenLizard_ElusiveLizard` · `Mon_Ink_BossDarkMoon` · `Mon_Ink_BossDarkMoonHallucination` · `Mon_Ink_BossWhiteNight` · `Mon_Ink_BossWhiteNightHallucination` · `Mon_LavaLand_InfernoSpider` · `Mon_LavaLand_InfernusPillar` · [Mon_RedGiant](/api/Global.Mon_RedGiant) · [Mon_RedMan](/api/Global.Mon_RedMan) · `Mon_Special_AmbushSpawner` · `Mon_Special_BossPolaris` · `PrimusCutsceneEntityVisualOff` · [Projectile](/api/Global.Projectile) · [PropEnt_Stone_DreamDust](/api/Global.PropEnt_Stone_DreamDust) · `RoomMod_Hunted` · `RoomMod_LeafPuppies` · `RoomMod_MeteoricLife` · [Room_Barrier](/api/Global.Room_Barrier) · `Se_AutoDetectPresence` · `Se_D_AstridsMasterpieceEnGarde` · `Se_D_AstridsMasterpieceEnGarde_Exposed` · `Se_D_AstridsMasterpiecePriorite` · `Se_D_ChargedAnguillian` · `Se_D_ConvergencePoint` · `Se_D_ExoticMatter` · `Se_D_IcyVeins` · `Se_D_MercyOfEl` · `Se_DarkCondensationZone` · `Se_E_VileStrike` · `Se_EngulfedInFlame` · `Se_FallenStar_MonsterReinforcement` · `Se_GoldEverywhere` · `Se_HeroKnockedOut` · `Se_HunterBuff_ShadowWalk_Disappear` · `Se_LimboBossDecorator` · `Se_M_Charge` · `Se_M_Flicker` · `Se_MiniBoss_BloodThorn` · `Se_MiniBoss_IceAura` · `Se_MiniBoss_OrbSpitter` · `Se_MiniBoss_SpinningArrow` · `Se_MiniBoss_UnstableExplosive` · `Se_MirageSkin_Sanctification_Protected` · `Se_Mon_DarkCave_BossSeeker_Blink` · `Se_Mon_DarkCave_BossSeeker_Hallucination_Disappear` · `Se_Mon_DarkCave_BossSeeker_TunnelVision_Disappear` · `Se_Mon_DarkCave_DarkElemental_Teleport` · `Se_Mon_Despair_BossAzurak_Hide` · `Se_Mon_Ink_Boss_Rage` · `Se_Mon_Polaris_Blink` · `Se_Mon_Polaris_Disappear` · `Se_Mon_Special_BossPolaris_Holy_Dash` · `Se_ObliviaxKidnap` · `Se_PortalTransition` · `Se_PureDream` · `Se_PureDream_Statue` · `Se_Q_DeathMark_Marked` · `Se_Q_Discipline_Jump` · `Se_Q_GoldenBurst_Wither` · `Se_R_LightningDance` · `Se_R_SerpentineBlessing_Buff` · `Se_R_ShadowWalk_Disappear` · `Se_Shrine_Despair_Teleport` · `Se_Shrine_SmallSoul` · `Se_Star_Husk_I_ShopIntimidation` · `Shrine_HeroSoul` · `Sky_LightFogDamager` · `Sky_NightWaterEffect` · [SpawnManager](/api/Global.SpawnManager) · `St_E_ChainLightning` · `St_QR_ValiantHeart` · `StarlessPath_BossPolarisManager` · [StatusEffect](/api/Global.StatusEffect) · `UI_DamageNumberText` · `UI_EntityFollow` · `UI_EntityGenericStackIndicator` · `UI_EntityHealthBar` · `UI_EntityHealthBarMain` · `UI_HealthBar_Simple` · `UI_InGame_FollowAndFaceHero_Conversation` · `UI_InGame_OffscreenIndicator_Item_Entity`

### Dependencies (36)

*Types and components that `EntityVisual` references or depends upon:*

[Accessory](/api/Global.Accessory) · [Actor](/api/Global.Actor) · [ActorCheck](/api/Global.ActorCheck) · [Dew](/api/Global.Dew) · [DewAnimationClip](/api/Global.DewAnimationClip) · [DewEffect](/api/Global.DewEffect) · [DewNetworkBehaviour](/api/Global.DewNetworkBehaviour) · [DewPlayer](/api/Global.DewPlayer) · [DewPool](/api/Global.DewPool) · [DewResources](/api/Global.DewResources) · [Entity](/api/Global.Entity) · [EntityAI](/api/Global.EntityAI) · [EntityAnimation](/api/Global.EntityAnimation) · [EntityColorModifier](/api/Global.EntityColorModifier) · [EntityComponent](/api/Global.EntityComponent) · [EntityControl](/api/Global.EntityControl) · [EntityHighlightProvider](/api/Global.EntityHighlightProvider) · [EntityModel](/api/Global.EntityModel) · [EntityShellModifier](/api/Global.EntityShellModifier) · [EntityStatus](/api/Global.EntityStatus) · [EntityTransformModifier](/api/Global.EntityTransformModifier) · [EventInfoDamage](/api/Global.EventInfoDamage) · [EventInfoKill](/api/Global.EventInfoKill) · `GetComponentsNonAllocExtension` · [GibInfo](/api/Global.GibInfo) · `GraphicsManager` · [ICleanup](/api/Global.ICleanup) · [InvisibleEffect](/api/Global.InvisibleEffect) · [ListReturnHandle`1](/api/Global.ListReturnHandle`1) · [ManagerBase`1](/api/Global.ManagerBase`1) · [MeshHighlightProvider](/api/Global.MeshHighlightProvider) · [SafeAction](/api/Global.SafeAction) · [SafeAction`1](/api/Global.SafeAction`1) · `TransformExtensions` · `Vector3FlattenExtension` · `Mirror.GeneratedNetworkCode`

### Related Enums (1)

*Enumerations referenced in fields, properties, or method signatures:*

[`KnockUpStrength`](/enums#knockupstrength)

:::
