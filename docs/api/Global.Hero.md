# Class: Hero

- **Category:** <span class="cat-dot" style="--cat-color: #22c55e" data-cat="Actors & Entities"></span> Actors & Entities
- **Namespace:** `Global`
- **Assembly:** `Dew.Core.dll`
- **Attributes:** `[RequireComponent]`
- **Inheritance / Derived:** [DewNetworkBehaviour](/api/Global.DewNetworkBehaviour) → [Actor](/api/Global.Actor) → [Entity](/api/Global.Entity)

```csharp
[RequireComponent(typeof(HeroSkill))]
public class Hero : Entity, ILogicUpdate, ICleanup, ICustomDestroyRoutine, IExcludeFromPool
```

## Fields (26)

::: details Click to expand Fields (26)

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`accessories`** | `[SaveVar] [SaveVar(SaveVarFlags.Default)] public readonly SyncList<string> accessories` |  |
| **`cDestruction`** | `[BoxGroup("Constellation Settings", true, false, 0)] public HeroConstellationSettings cDestruction` |  |
| **`cDisplayBaseAngle`** | `[BoxGroup("Constellation Settings", true, false, 0)] public float cDisplayBaseAngle` |  |
| **`cFlexible`** | `[BoxGroup("Constellation Settings", true, false, 0)] public HeroConstellationSettings cFlexible` |  |
| **`cImagination`** | `[BoxGroup("Constellation Settings", true, false, 0)] public HeroConstellationSettings cImagination` |  |
| **`classType`** | `[BoxGroup("Hero Settings", true, false, 0)] public Hero.HeroClassType classType` |  |
| **`ClientHeroEvent_OnIsInCombatChanged`** | `public SafeAction<bool> ClientHeroEvent_OnIsInCombatChanged` |  |
| **`ClientHeroEvent_OnKillOrAssist`** | `public SafeAction<EventInfoKill> ClientHeroEvent_OnKillOrAssist` |  |
| **`ClientHeroEvent_OnKnockedOut`** | `public SafeAction<EventInfoKill> ClientHeroEvent_OnKnockedOut` |  |
| **`ClientHeroEvent_OnLevelChanged`** | `public SafeAction<EventInfoHeroLevelUp> ClientHeroEvent_OnLevelChanged` |  |
| **`ClientHeroEvent_OnRevive`** | `public SafeAction<Hero> ClientHeroEvent_OnRevive` |  |
| **`ClientHeroEvent_OnSkillUse`** | `public SafeAction<EventInfoSkillUse> ClientHeroEvent_OnSkillUse` |  |
| **`cLife`** | `[BoxGroup("Constellation Settings", true, false, 0)] public HeroConstellationSettings cLife` |  |
| **`decoConstellationPrefab`** | `[BoxGroup("Hero Settings", true, false, 0)] public GameObject decoConstellationPrefab` |  |
| **`difficulty`** | `[BoxGroup("Hero Settings", true, false, 0)] public Hero.HeroDifficulty difficulty` |  |
| **`dismantleProcessor`** | `public DataProcessorGroup<int, Hero, Actor> dismantleProcessor` |  |
| **`excludeFromPool`** | `[BoxGroup("Hero Settings", true, false, 0)] public bool excludeFromPool` |  |
| **`HeroEvent_OnAbilityInstanceBeforePrepareFromSkill`** | `public SafeAction<EventInfoSkillAbilityInstance> HeroEvent_OnAbilityInstanceBeforePrepareFromSkill` |  |
| **`HeroEvent_OnAbilityInstanceCreatedFromSkill`** | `public SafeAction<EventInfoSkillAbilityInstance> HeroEvent_OnAbilityInstanceCreatedFromSkill` |  |
| **`icon`** | `[BoxGroup("Hero Settings", true, false, 0)] public Sprite icon` |  |
| **`InCombatCheckInterval`** | `public const float InCombatCheckInterval = 0.5` |  |
| **`isWeaponHolstered`** | `[NonSerialized] public bool isWeaponHolstered` | Checked locally. |
| **`mainColor`** | `[BoxGroup("Hero Settings", true, false, 0)] public Color mainColor` |  |
| **`MarkAsInCombatDuration`** | `public const float MarkAsInCombatDuration = 2` |  |
| **`maxLevelOverride`** | `public int? maxLevelOverride` |  |
| **`summons`** | `[NonSerialized] public List<Summon> summons` | Available everywhere. |

:::

## Properties (9)

::: details Click to expand Properties (9)

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`exp`** | `[SaveVar] [SaveVar(SaveVarFlags.ApplyAfterCreation)] public int exp { get; }` |  |
| **`isDestroyedOnRoomChange`** | `public override bool isDestroyedOnRoomChange { get; }` |  |
| **`isInCombat`** | `public bool isInCombat { get; }` | Did this hero dealt damage to an enemy or took damage from an enemy?Available everywhere. |
| **`isKnockedOut`** | `public bool isKnockedOut { get; }` |  |
| **`loadout`** | `public HeroLoadoutData loadout { get; set; }` |  |
| **`maxExp`** | `public int maxExp { get; }` |  |
| **`maxLevel`** | `public int maxLevel { get; }` |  |
| **`Skill`** | `public HeroSkill Skill { get; }` |  |
| **`skin`** | `public string skin { get; set; }` |  |

:::

## Methods (19)

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

```csharp
protected override void AIUpdate(ref EntityAIContext context)
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

::: details `CmdTeleportToWaypoint(Room_Waypoint)`

```csharp
public void CmdTeleportToWaypoint(Room_Waypoint waypoint)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `waypoint` | [`Room_Waypoint`](/api/Global.Room_Waypoint) |  |

:::

::: details `FrameUpdate()`

```csharp
public override void FrameUpdate()
```

:::

::: details `GetConstellationSettings(StarType)`

```csharp
public HeroConstellationSettings GetConstellationSettings(StarType type)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `type` | [`StarType`](/api/Global.StarType) |  |

**Returns:** `HeroConstellationSettings`

:::

::: details `GetStaggerSettings()`

```csharp
protected override Entity.StaggerSettings GetStaggerSettings()
```

**Returns:** `Entity.StaggerSettings`

:::

::: details `IsMeleeHero()`

```csharp
public bool IsMeleeHero()
```

**Returns:** `bool`

:::

::: details `IsRangedHero()`

```csharp
public bool IsRangedHero()
```

**Returns:** `bool`

:::

::: details `LoadEntityModelLocal()`

```csharp
public override void LoadEntityModelLocal()
```

:::

::: details `MarkAsInCombat()`

```csharp
public void MarkAsInCombat()
```

:::

::: details `OnDestroyActor()`

```csharp
protected override void OnDestroyActor()
```

:::

::: details `OnLateStartServer()`

```csharp
public override void OnLateStartServer()
```

:::

::: details `OnModelLoaded()`

```csharp
public override void OnModelLoaded()
```

:::

::: details `OnStart()`

```csharp
public override void OnStart()
```

:::

::: details `OnStartAuthority()`

```csharp
public override void OnStartAuthority()
```

:::

::: details `OnStartServer()`

```csharp
public override void OnStartServer()
```

:::

::: details `OnStopAuthority()`

```csharp
public override void OnStopAuthority()
```

:::

::: details `ReceiveExperience(int)`

Add to experience of this hero.

```csharp
public void ReceiveExperience(int amount)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `amount` | `int` |  |

:::


## Architecture & Relationships

::: details Click to expand Architecture & Relationships

### Used By (242)

*Classes and systems that invoke, reference, or depend on `Hero`:*

`ACH_IN_CARNAGE_I_BLOOM` · `ACH_THE_EIGHTH_TROPHY` · [AbilityInstance](/api/Global.AbilityInstance) · [AchievementManager](/api/Global.AchievementManager) · [ActorManager](/api/Global.ActorManager) · `Ai_Culinary_Pickup` · `Ai_E_MysticDagger` · `Ai_Gem_E_Predation_Pickup` · `Ai_Mon_Special_BossPolaris_Holy_CounterSpell_DisarmProjectile` · `Ai_Q_DeathMark_Projectile` · `Ai_Q_EmbracingTheChill_AreaDoT` · `Ai_Q_Lunge` · `Ai_Q_SuperNova` · `Ai_RandomGemUpgrade` · [AnalyticsEquipmentData](/api/Global.AnalyticsEquipmentData) · [CameraManager](/api/Global.CameraManager) · [CinematicCameraHelper](/api/Global.CinematicCameraHelper) · [ClientEventManager](/api/Global.ClientEventManager) · [ControlManager](/api/Global.ControlManager) · [Dew](/api/Global.Dew) · [DewAllHeroesPresentZone](/api/Global.DewAllHeroesPresentZone) · [DewGameObserverWithProgress](/api/Global.DewGameObserverWithProgress) · [DewNetworkManager](/api/Global.DewNetworkManager) · [DewPersistence](/api/Global.DewPersistence) · [DewPlayer](/api/Global.DewPlayer) · `DewStarItemOld` · [EditSkillManager](/api/Global.EditSkillManager) · [EditSkillShrine](/api/Global.EditSkillShrine) · [EntityAI](/api/Global.EntityAI) · [EntityAnimation](/api/Global.EntityAnimation) · [EntityCheck](/api/Global.EntityCheck) · [EntityControl](/api/Global.EntityControl) · [EntityGroundMarker](/api/Global.EntityGroundMarker) · `EventInfoDismantle` · [GameManager](/api/Global.GameManager) · [GameResultManager](/api/Global.GameResultManager) · [Gem](/api/Global.Gem) · `Gem_C_Confidence` · `Gem_C_Regeneration` · `Gem_C_Sulfur` · `Gem_C_Vengeance` · `Gem_E_Aftershock` · `Gem_E_Crimson` · `Gem_E_Domination` · `Gem_E_Fangs` · `Gem_E_Flexibility` · `Gem_E_Insensitivity` · `Gem_E_Metal` · `Gem_E_Omega` · `Gem_E_Opportunity` · `Gem_E_OurStory_Completed` · `Gem_E_OurStory_Unfinished` · `Gem_E_Predation` · `Gem_E_Reflex` · `Gem_E_Thunder` · `Gem_E_Twilight` · `Gem_L_CamillasGift` · `Gem_L_ChaosApple` · `Gem_L_DivineFaith` · `Gem_L_Embertail` · `Gem_L_Liberty` · `Gem_L_MetalCrystal` · `Gem_L_Paranoia` · `Gem_L_Perfect` · `Gem_L_Supersymmetry` · `Gem_R_Accuracy` · `Gem_R_Adventure` · `Gem_R_Blood` · `Gem_R_Composure` · `Gem_R_Crucible` · `Gem_R_Flow` · `Gem_R_Frost` · `Gem_R_Glass` · `Gem_R_Hedgehog` · `Gem_R_Momentum` · `Gem_R_NightSky` · `Gem_R_Panic` · `Gem_R_Shock` · `Gem_R_Slippery` · `Gem_R_Snow` · `Gem_R_Spiral` · `Gem_U_GlacialCore` · `Gem_U_GuidingCompass_Charged` · `Gem_U_GuidingCompass_NotCharged` · `Gem_U_SoulPrison` · [HeroComponent](/api/Global.HeroComponent) · [HeroSkill](/api/Global.HeroSkill) · `Hero_Aurena` · `Hero_Bismuth` · `Hero_Cetus` · `Hero_Husk` · `Hero_Lacerta` · `Hero_Mist` · `Hero_Nachia` · `Hero_Vesper` · `Hero_Yubar` · [IItem](/api/Global.IItem) · `InGameAnalyticsManager` · [InGameCrashReportManager](/api/Global.InGameCrashReportManager) · `ItemWorldModel` · `LucidDream_FishScales` · `NetworkConnectionToClientExtension` · [PickupInstance](/api/Global.PickupInstance) · [PickupManager](/api/Global.PickupManager) · [Pickup_BaseExpOrb](/api/Global.Pickup_BaseExpOrb) · [Pickup_BaseGoldOrb](/api/Global.Pickup_BaseGoldOrb) · [Pickup_DreamDust](/api/Global.Pickup_DreamDust) · [Pickup_HealthOrb](/api/Global.Pickup_HealthOrb) · [Pickup_ManaOrb](/api/Global.Pickup_ManaOrb) · [Pickup_RegenOrb](/api/Global.Pickup_RegenOrb) · [PingManager](/api/Global.PingManager) · [PlayGameManager](/api/Global.PlayGameManager) · `PlayTutorialManager` · `PlayTutorial_NextTutorialRift` · `PlayTutorial_StartGameRift` · `PlayTutorial_Tutorial` · [PropEnt_Merchant_Base](/api/Global.PropEnt_Merchant_Base) · `Quest_LostSoul` · [Rift](/api/Global.Rift) · [Rift_RoomExit](/api/Global.Rift_RoomExit) · [Rift_Sidetrack](/api/Global.Rift_Sidetrack) · `RoomMod_HeroSoul` · [RoomMonsters](/api/Global.RoomMonsters) · [Room_Shortcut](/api/Global.Room_Shortcut) · `Se_AutoDetectPresence` · `Se_Curse_IntermittentExplosion` · `Se_Curse_LossOfIdentity` · `Se_Curse_SoftSkin` · `Se_D_ConvergencePoint` · `Se_D_DoubleTap` · `Se_D_ExoticMatter` · `Se_D_IceColdPresence` · `Se_DarkCondensationZone` · `Se_E_Rewind` · `Se_E_UmbralEdge` · `Se_FallenStar_WaveringIdentity` · `Se_FishScales` · `Se_GenericHealOverTime` · `Se_HeroBleedingOut` · `Se_HeroInCombatIcon` · `Se_HeroKnockedOut` · `Se_LingeringAuraOfGuidance` · `Se_MirageSkin_Delusion` · `Se_Mon_Special_BossPolaris_Holy_CounterSpell` · `Se_Mon_Special_BossPolaris_Monster_Scream_SkillLocked` · `Se_Nor_MyOwnLittleNebula` · `Se_R_AnnihilationStance` · `Se_R_Tranquility` · `Se_R_UnbreakableDetermination` · `Se_RoomMod_UnstableVeilOfTime_ModifyCooldowns` · `Se_Shrine_Chaos_StatBonus` · `Se_Star_Aurena_F_GB_NoSacrificeAfterDodge` · `Se_Star_Bismuth_D_AtkSpdFromDismantle` · `Se_Star_Bismuth_D_BonusAttackEffect` · `Se_Star_Bismuth_D_SkillHasteAndAutoCast` · `Se_Star_Bismuth_F_IN_MoreProjByAtkSpd` · `Se_Star_Cetus_D_ApUpByColdSkillCounts` · `Se_Star_Cetus_I_FirstColdGemQualityBoost` · `Se_Star_Cetus_L_DodgeCdReductionOnHit` · `Se_Star_Husk_D_MovementSkillHaste` · `Se_Star_Husk_F_DE_MarkHitDodgeCDR` · `Se_Star_Husk_F_LA_DodgeResetOnRed` · `Se_Star_Husk_I_ShopIntimidation` · `Se_Star_I_DismantleReroll` · `Se_Star_I_FirstGemUpgrade` · `Se_Star_L_DodgeCooldown` · `Se_Star_L_DodgeCooldownOnLowHealth` · `Se_Star_L_PotionOnBuyOrSell` · `Se_Star_Lacerta_L_DodgeCharges` · `Se_Star_Mist_L_AddedDodgeWithPenalty` · `Se_Star_Mist_L_DodgeCooldownWithPenalty` · `Se_Star_Yubar_D_APPerLightSkill` · `Se_Star_Yubar_F_CC_MeteorPerLightSkill` · `Se_Star_Yubar_L_DodgeChargeWithLongerCooldown` · `Se_Star_Yubar_L_DodgeCooldownWithShorterRange` · `Se_Star_Yubar_L_DodgeRange` · [Shrine](/api/Global.Shrine) · `Shrine_Ascension` · `Shrine_BossSoul` · `Shrine_Chaos` · `Shrine_CookingPot` · `Shrine_CorruptedChaos` · `Shrine_Entanglement` · `Shrine_FallenStar` · `Shrine_Hatred` · `Shrine_Hatred_Old` · `Shrine_HeroSoul` · `Shrine_PrimusEndingLightPillar` · [SkillTrigger](/api/Global.SkillTrigger) · [SpawnMonsterSettings](/api/Global.SpawnMonsterSettings) · `St_C_SparklingWaterGun` · `St_D_ParryMaster` · `St_E_Rewind` · `St_L_HerosReturn` · `St_Q_GoldenBurst` · [StarEffect](/api/Global.StarEffect) · `Star_Global_DodgeAbilityCooldown` · `Star_Global_FirstGemUpgrade` · `Star_Mist_AddDodgeCharge` · `Star_Yubar_IncreaseFlickerRange` · `StarlessPath_BossPolarisManager` · `StatusEffectRandomPickupInstance` · [Summon](/api/Global.Summon) · [Treasure](/api/Global.Treasure) · `Tut_Cleanse` · `Tut_ShopSell` · `UI_EntityExpBar` · `UI_EntityHealthBar` · `UI_EntityHealthBarMain` · `UI_EntityProvider_LocalHero` · `UI_InGame_CurseNotifications` · `UI_InGame_FloatingWindow_Shop_Item` · `UI_InGame_GemSlot` · `UI_InGame_GemSlot_EditSkill` · `UI_InGame_HeroDetailWindow` · `UI_InGame_HeroInfoBar` · `UI_InGame_Interact_Gem` · `UI_InGame_KnockedOutIndicator` · `UI_InGame_MovementSkillIndicator` · `UI_InGame_OffscreenIndicator_Item_Entity` · `UI_InGame_PartyDisplay` · `UI_InGame_PartyDisplay_Item` · `UI_InGame_ScoreboardView` · `UI_InGame_Scoreboard_PlayerItem` · `UI_InGame_Scoreboard_PlayerItem_Skill` · `UI_InGame_Scoreboard_PlayerItem_Skill_Gem` · `UI_InGame_SkillButton` · `UI_InGame_SkillButton_EditSkill` · `UI_InGame_SkillButton_GemGroup` · `UI_InGame_SkillNotifications` · `UI_Lobby_Constellations_HeroConstellation_StarSlot` · `UI_Lobby_Constellations_StarItem` · `UI_Lobby_SelectedHeroInfo_Base` · `UI_TooltipManager` · `UI_Tooltip_EditSkillShrineTooltip` · `UI_Tooltip_EquippedGemDescriber` · `UI_Tooltip_EquippedGemDescriber_Item` · `UI_Tooltip_ObjEditSkillActions` · `UI_Tooltip_SkillStarDescriber` · `UI_Tooltip_SkillTitle` · `UI_TravelerStory_HeroConstellation` · [ZoneManager](/api/Global.ZoneManager)

### Dependencies (33)

*Types and components that `Hero` references or depends upon:*

[Actor](/api/Global.Actor) · [DataProcessorGroup`3](/api/Global.DataProcessorGroup`3) · [Dew](/api/Global.Dew) · [DewLocalization](/api/Global.DewLocalization) · [DewNetworkBehaviour](/api/Global.DewNetworkBehaviour) · [DewPlayer](/api/Global.DewPlayer) · [DewResources](/api/Global.DewResources) · [Entity](/api/Global.Entity) · [EntityAI](/api/Global.EntityAI) · [EntityAIContext](/api/Global.EntityAIContext) · [EntityComponent](/api/Global.EntityComponent) · [EntityControl](/api/Global.EntityControl) · [EntityStatus](/api/Global.EntityStatus) · [EntityVisual](/api/Global.EntityVisual) · [EventInfoHeroLevelUp](/api/Global.EventInfoHeroLevelUp) · [EventInfoKill](/api/Global.EventInfoKill) · `GetComponentsNonAllocExtension` · [HealData](/api/Global.HealData) · [HeroConstellationSettings](/api/Global.HeroConstellationSettings) · [HeroLoadoutData](/api/Global.HeroLoadoutData) · [HeroSkill](/api/Global.HeroSkill) · [IExcludeFromPool](/api/Global.IExcludeFromPool) · [InGameUIManager](/api/Global.InGameUIManager) · [KillTracker](/api/Global.KillTracker) · [ListReturnHandle`1](/api/Global.ListReturnHandle`1) · [NetworkedManagerBase`1](/api/Global.NetworkedManagerBase`1) · [RoomSection](/api/Global.RoomSection) · [Room_Waypoint](/api/Global.Room_Waypoint) · [SafeAction`1](/api/Global.SafeAction`1) · [Section_Monsters](/api/Global.Section_Monsters) · [Skin](/api/Global.Skin) · `VectorPlaneTransformExtension` · `Mirror.GeneratedNetworkCode`

### Related Enums (2)

*Enumerations referenced in fields, properties, or method signatures:*

[`SaveVarFlags`](/enums#savevarflags) · [`StarType`](/enums#startype)

:::
