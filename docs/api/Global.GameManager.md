# Class: GameManager

- **Category:** <span class="cat-dot" style="--cat-color: #ef4444" data-cat="Combat & Abilities"></span> Combat & Abilities
- **Namespace:** `Global`
- **Assembly:** `Dew.Core.dll`
- **Inheritance / Derived:** [DewNetworkBehaviour](/api/Global.DewNetworkBehaviour) → `NetworkedManagerBase` → [GameManager](/api/Global.GameManager) → [DevGameManager](/api/Global.DevGameManager) → [PlayGameManager](/api/Global.PlayGameManager)

```csharp
public class GameManager : NetworkedManagerBase<GameManager>, ILogicUpdate
```

## Fields (11)

::: details Click to expand Fields (11)

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`ClientEvent_OnAmbientLevelChanged`** | `public SafeAction<int, int> ClientEvent_OnAmbientLevelChanged` | Called everywhere when ambient level changes |
| **`ClientEvent_OnDifficultyChanged`** | `public SafeAction<DewDifficultySettings, DewDifficultySettings> ClientEvent_OnDifficultyChanged` | Called everywhere when threat level changes |
| **`ClientEvent_OnGameConcluded`** | `public SafeAction ClientEvent_OnGameConcluded` | Called everywhere when game is concluded |
| **`disableStuckCheck`** | `public bool disableStuckCheck` |  |
| **`gainedExpMultiplier`** | `[SyncVar] [NonSerialized] public float gainedExpMultiplier` |  |
| **`ges`** | `public DewGameplayExperienceSettings ges` |  |
| **`gesTemplate`** | `[FormerlySerializedAs] [FormerlySerializedAs("gss")] public DewGameplayExperienceSettings gesTemplate` |  |
| **`goldCostMultiplier`** | `[SyncVar] [NonSerialized] public float goldCostMultiplier` |  |
| **`goldIncomeMultiplier`** | `[SyncVar] [NonSerialized] public float goldIncomeMultiplier` |  |
| **`playerRejoinData`** | `[SaveVar] [SaveVar(SaveVarFlags.Default)] public Dictionary<string, DewPersistence.PlayerData> playerRejoinData` |  |
| **`predictionStrengthOverride`** | `public Func<float> predictionStrengthOverride` |  |

:::

## Properties (14)

::: details Click to expand Properties (14)

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`ambientLevel`** | `[SaveVar] [SaveVar(SaveVarFlags.Default)] public int ambientLevel { get; set; }` |  |
| **`difficulty`** | `[SaveVar] [SaveVar(SaveVarFlags.Default)] public DewDifficultySettings difficulty { get; set; }` |  |
| **`elapsedGameTime`** | `[SaveVar] [SaveVar(SaveVarFlags.Default)] public float elapsedGameTime { get; set; }` | Elapsed game time in seconds. |
| **`isGameConcluded`** | `public bool isGameConcluded { get; }` |  |
| **`isGameOverEnabled`** | `public bool isGameOverEnabled { get; set; }` |  |
| **`isGameTimePaused`** | `public bool isGameTimePaused { get; }` |  |
| **`isGameTimePausedByAfk`** | `public bool isGameTimePausedByAfk { get; set; }` |  |
| **`isGameTimePausedByGame`** | `public bool isGameTimePausedByGame { get; set; }` |  |
| **`isMidRunSaveLocked`** | `public bool isMidRunSaveLocked { get; }` | Is continue save blocked by LockMidRunSave()? Available everywhere. |
| **`isSpawnOverPopulation`** | `public bool isSpawnOverPopulation { get; }` |  |
| **`maxAndSpawnedPopulationMultiplier`** | `public float maxAndSpawnedPopulationMultiplier { get; set; }` |  |
| **`maxSpawnedPopulation`** | `public float maxSpawnedPopulation { get; }` |  |
| **`runId`** | `[SaveVar] [SaveVar(SaveVarFlags.Default)] public string runId { get; set; }` | Globally unique identifier of this run. This is consistent across all clients. |
| **`spawnedPopulation`** | `public float spawnedPopulation { get; }` | Total population excluding env spawns. =&gt; Spawns from combat areas. |

:::

## Methods (65)

::: details `Awake()`

```csharp
protected override void Awake()
```

:::

::: details `CallOnReady(Action)`

Call provided function if the game is ready. (Client is ready, Server is not loading scene, has local hero, map is loaded, screen is shown)If not ready, the function call will be delayed until it is.Available on server and clients.

```csharp
public static void CallOnReady(Action action)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `action` | `System.Action` |  |

:::

::: details `CollectAllPlayersRejoinData()`

```csharp
public void CollectAllPlayersRejoinData()
```

:::

::: details `CollectPlayerRejoinData(DewPlayer)`

```csharp
public void CollectPlayerRejoinData(DewPlayer p)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `p` | [`DewPlayer`](/api/Global.DewPlayer) |  |

:::

::: details `ConcludePureWhiteDream()`

```csharp
public void ConcludePureWhiteDream()
```

:::

::: details `ConcludeUnknownFate()`

```csharp
public void ConcludeUnknownFate()
```

:::

::: details `GetAdjustedDroppedExperienceAmount(float)`

```csharp
public float GetAdjustedDroppedExperienceAmount(float original)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `original` | `float` |  |

**Returns:** `float`

:::

::: details `GetAdjustedGoldAmount_Cost_Service(float)`

```csharp
public float GetAdjustedGoldAmount_Cost_Service(float baseAmount)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `baseAmount` | `float` |  |

**Returns:** `float`

:::

::: details `GetAdjustedGoldAmount_Cost(float)`

```csharp
public float GetAdjustedGoldAmount_Cost(float amount)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `amount` | `float` |  |

**Returns:** `float`

:::

::: details `GetAdjustedGoldAmount_Income(float)`

```csharp
public float GetAdjustedGoldAmount_Income(float amount)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `amount` | `float` |  |

**Returns:** `float`

:::

::: details `GetAdjustedGoldAmount(float)`

```csharp
public float GetAdjustedGoldAmount(float amount)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `amount` | `float` |  |

**Returns:** `float`

:::

::: details `GetAdjustedMonsterSpawnPopulation(float, bool, bool)`

```csharp
public float GetAdjustedMonsterSpawnPopulation(float original, bool ignoreTurnMultiplier = false, bool ignoreCoopMultiplier = false)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `original` | `float` |  |
| `ignoreTurnMultiplier` | `bool` |  |
| `ignoreCoopMultiplier` | `bool` |  |

**Returns:** `float`

:::

::: details `GetAdjustedMonsterWaves(int, DewRandom)`

```csharp
public int GetAdjustedMonsterWaves(int original, DewRandom random = null)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `original` | `int` |  |
| `random` | [`DewRandom`](/api/Global.DewRandom) |  |

**Returns:** `int`

:::

::: details `GetAdjustedMonsterWavesMultiplier()`

```csharp
public float GetAdjustedMonsterWavesMultiplier()
```

**Returns:** `float`

:::

::: details `GetBossMonsterDamageMultiplierByScaling(float)`

```csharp
public float GetBossMonsterDamageMultiplierByScaling(float customZoneIndex = NaN)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `customZoneIndex` | `float` |  |

**Returns:** `float`

:::

::: details `GetBossMonsterHealthMultiplierByScaling(float)`

```csharp
public float GetBossMonsterHealthMultiplierByScaling(float customZoneIndex = NaN)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `customZoneIndex` | `float` |  |

**Returns:** `float`

:::

::: details `GetCleanseGemMinQuality()`

```csharp
public int GetCleanseGemMinQuality()
```

**Returns:** `int`

:::

::: details `GetCleanseGoldCost(Gem)`

```csharp
public int GetCleanseGoldCost(Gem gem)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `gem` | [`Gem`](/api/Global.Gem) |  |

**Returns:** `int`

:::

::: details `GetCleanseGoldCost(SkillTrigger)`

```csharp
public int GetCleanseGoldCost(SkillTrigger skill)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `skill` | [`SkillTrigger`](/api/Global.SkillTrigger) |  |

**Returns:** `int`

:::

::: details `GetCleanseReturnedDreamDust(DewPlayer, Gem)`

```csharp
public int GetCleanseReturnedDreamDust(DewPlayer player, Gem gem)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `player` | [`DewPlayer`](/api/Global.DewPlayer) |  |
| `gem` | [`Gem`](/api/Global.Gem) |  |

**Returns:** `int`

:::

::: details `GetCleanseReturnedDreamDust(DewPlayer, SkillTrigger)`

```csharp
public int GetCleanseReturnedDreamDust(DewPlayer player, SkillTrigger skill)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `player` | [`DewPlayer`](/api/Global.DewPlayer) |  |
| `skill` | [`SkillTrigger`](/api/Global.SkillTrigger) |  |

**Returns:** `int`

:::

::: details `GetCleanseSkillMinLevel()`

```csharp
public int GetCleanseSkillMinLevel()
```

**Returns:** `int`

:::

::: details `GetDifficulty()`

```csharp
protected virtual DewDifficultySettings GetDifficulty()
```

**Returns:** `DewDifficultySettings`

:::

::: details `GetExpDropFromEntity(Entity)`

```csharp
public float GetExpDropFromEntity(Entity ent)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `ent` | [`Entity`](/api/Global.Entity) |  |

**Returns:** `float`

:::

::: details `GetGainedSkillHastePerSkillLevel(SkillTrigger)`

```csharp
public float GetGainedSkillHastePerSkillLevel(SkillTrigger skillTrigger)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `skillTrigger` | [`SkillTrigger`](/api/Global.SkillTrigger) |  |

**Returns:** `float`

:::

::: details `GetGemUpgradeAddedQuality()`

```csharp
public int GetGemUpgradeAddedQuality()
```

**Returns:** `int`

:::

::: details `GetGemUpgradeDreamDustCost(Gem)`

```csharp
public int GetGemUpgradeDreamDustCost(Gem gem)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `gem` | [`Gem`](/api/Global.Gem) |  |

**Returns:** `int`

:::

::: details `GetGemUpgradeDreamDustCost(int)`

```csharp
public int GetGemUpgradeDreamDustCost(int quality)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `quality` | `int` |  |

**Returns:** `int`

:::

::: details `GetKillGoldAmount(Entity)`

```csharp
public int GetKillGoldAmount(Entity ent)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `ent` | [`Entity`](/api/Global.Entity) |  |

**Returns:** `int`

:::

::: details `GetLucidDreams()`

```csharp
public virtual IList<string> GetLucidDreams()
```

**Returns:** `System.Collections.Generic.IList<T><string>`

:::

::: details `GetMiniBossMonsterDamageMultiplierByScaling(float)`

```csharp
public float GetMiniBossMonsterDamageMultiplierByScaling(float customZoneIndex = NaN)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `customZoneIndex` | `float` |  |

**Returns:** `float`

:::

::: details `GetMiniBossMonsterHealthMultiplierByScaling(float)`

```csharp
public float GetMiniBossMonsterHealthMultiplierByScaling(float customZoneIndex = NaN)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `customZoneIndex` | `float` |  |

**Returns:** `float`

:::

::: details `GetMonsterBonusHealthPercentageByMultiplayer(Monster)`

```csharp
public float GetMonsterBonusHealthPercentageByMultiplayer(Monster m)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `m` | [`Monster`](/api/Global.Monster) |  |

**Returns:** `float`

:::

::: details `GetMonsterBonusPowerPercentage(Monster)`

```csharp
public float GetMonsterBonusPowerPercentage(Monster m)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `m` | [`Monster`](/api/Global.Monster) |  |

**Returns:** `float`

:::

::: details `GetMultiplayerDifficultyFactor(bool)`

Get amount of extra players. Solo: 0, Two: 1, ...If reduceWhenDead is set, dead player will contribute 55% percent instead of 100% to the factor.

```csharp
public float GetMultiplayerDifficultyFactor(bool reduceWhenDead)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `reduceWhenDead` | `bool` |  |

**Returns:** `float`

:::

::: details `GetMultiplier_Imp(double, double, double, double, double, int)`

```csharp
public static float GetMultiplier_Imp(double x, double a, double b, double c, double d, int linearStart)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `x` | `double` |  |
| `a` | `double` |  |
| `b` | `double` |  |
| `c` | `double` |  |
| `d` | `double` |  |
| `linearStart` | `int` |  |

**Returns:** `float`

:::

::: details `GetPredictionStrength()`

```csharp
public float GetPredictionStrength()
```

**Returns:** `float`

:::

::: details `GetRegularMonsterDamageMultiplierByScaling(float)`

```csharp
public float GetRegularMonsterDamageMultiplierByScaling(float customZoneIndex = NaN)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `customZoneIndex` | `float` |  |

**Returns:** `float`

:::

::: details `GetRegularMonsterHealthMultiplierByScaling(float)`

```csharp
public float GetRegularMonsterHealthMultiplierByScaling(float customZoneIndex = NaN)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `customZoneIndex` | `float` |  |

**Returns:** `float`

:::

::: details `GetSkillUpgradeDreamDustCost(SkillTrigger)`

```csharp
public int GetSkillUpgradeDreamDustCost(SkillTrigger skill)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `skill` | [`SkillTrigger`](/api/Global.SkillTrigger) |  |

**Returns:** `int`

:::

::: details `GetSkillUpgradeDreamDustCost(int)`

```csharp
public int GetSkillUpgradeDreamDustCost(int level)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `level` | `int` |  |

**Returns:** `int`

:::

::: details `GetSpecialRewardAmount_DreamDust()`

```csharp
public float GetSpecialRewardAmount_DreamDust()
```

**Returns:** `float`

:::

::: details `GetSpecialRewardAmount_Gold()`

```csharp
public float GetSpecialRewardAmount_Gold()
```

**Returns:** `float`

:::

::: details `GetSpecialSkillChanceMultiplier()`

```csharp
public float GetSpecialSkillChanceMultiplier()
```

**Returns:** `float`

:::

::: details `GetStrongHealthScalingMultiplier_Imp(float)`

```csharp
public static float GetStrongHealthScalingMultiplier_Imp(float zi)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `zi` | `float` |  |

**Returns:** `float`

:::

::: details `GetUniversalDamageScalingMultiplier_Imp(float)`

```csharp
public static float GetUniversalDamageScalingMultiplier_Imp(float zi)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `zi` | `float` |  |

**Returns:** `float`

:::

::: details `GetWeakHealthScalingMultiplier_Imp(float)`

```csharp
public static float GetWeakHealthScalingMultiplier_Imp(float zi)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `zi` | `float` |  |

**Returns:** `float`

:::

::: details `IsContinueSaveSupported()`

Is continue-saving a normal thing in this game manager? If not, no continue save will be made, and user will not be notified with any save-related things.Used to tell apart from normal game and special games like tutorial.

```csharp
public virtual bool IsContinueSaveSupported()
```

**Returns:** `bool`

:::

::: details `IsEligibleForMidRunSave()`

Can the game be saved mid-run right now? Usually save is made every travel, but after clearing the room, the game can be saved mid-run e.g. before exiting the game.

```csharp
public bool IsEligibleForMidRunSave()
```

**Returns:** `bool`

:::

::: details `IsLazyCallReady()`

```csharp
public virtual bool IsLazyCallReady()
```

**Returns:** `bool`

:::

::: details `LoadNextZone()`

```csharp
public virtual void LoadNextZone()
```

:::

::: details `LockMidRunSave()`

Calling this will lock mid-run save.If a continue save hasn't been made for more than 20 seconds, a continue save will be immediately made.This call MUST BE ACCOMPANIED by the same number of UnlockMidRunSave() calls.

```csharp
public void LockMidRunSave()
```

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

::: details `OnStart()`

```csharp
public override void OnStart()
```

:::

::: details `OnStartServer()`

```csharp
public override void OnStartServer()
```

:::

::: details `ResetGameplayExperienceSettings()`

```csharp
public void ResetGameplayExperienceSettings()
```

:::

::: details `SaveContinueData(LoadNodeSettings)`

```csharp
public void SaveContinueData(LoadNodeSettings s)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `s` | [`LoadNodeSettings`](/api/Global.LoadNodeSettings) |  |

:::

::: details `SaveContinueDataMidRun()`

```csharp
public void SaveContinueDataMidRun()
```

:::

::: details `SetAmbientLevel(int)`

Level will be clamped accordingly to GSS.

```csharp
public void SetAmbientLevel(int newLevel)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `newLevel` | `int` |  |

:::

::: details `SetDisconnectedForEveryoneElse()`

```csharp
public void SetDisconnectedForEveryoneElse()
```

:::

::: details `SetElapsedGameTime(float)`

```csharp
public void SetElapsedGameTime(float newTime)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `newTime` | `float` |  |

:::

::: details `UnlockMidRunSave()`

Calling this will unlock and allow mid-run saves.This call MUST BE DONE AFTER LockMidRunSave() calls.

```csharp
public void UnlockMidRunSave()
```

:::

::: details `UpdateSpawnedPopulation()`

```csharp
public void UpdateSpawnedPopulation()
```

:::

::: details `WrapUpAndShowResult(ResultType)`

```csharp
public void WrapUpAndShowResult(DewGameResult.ResultType type)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `type` | [`DewGameResult.ResultType`](/api/Global.DewGameResult) |  |

:::


## Architecture & Relationships

::: details Click to expand Architecture & Relationships

### Used By (121)

*Classes and systems that invoke, reference, or depend on `GameManager`:*

`ACH_GOD_PROTECTS_ME` · `ACH_HOME_SWEET_HOME` · `ACH_RAGE_WITHOUT_BOUNDS` · [AbilityTrigger](/api/Global.AbilityTrigger) · [AchievementManager](/api/Global.AchievementManager) · [ActorManager](/api/Global.ActorManager) · `Ai_MiniBoss_BloodThorn_MainThorn` · `Ai_Mon_Despair_BossAzurak_Roll` · `Ai_Mon_Ink_BossDarkMoon_Blade` · `Ai_Mon_Ink_BossWhiteNight_AltAtk_Ready` · `Ai_Mon_Ink_BossWhiteNight_Cataclysm` · `Ai_Mon_Ink_BossWhiteNight_Oppression` · `Ai_Mon_LavaLand_BossInfernus_PowerBomb` · `Ai_Mon_LavaLand_BossInfernus_WallStunKnockback` · `Ai_Mon_Sky_BossNyx_Atk` · `Ai_Mon_SnowMountain_BossSkoll_Atk` · `Ai_Mon_Special_AmbushSpawner_Projectile` · `Ai_Mon_Special_BossErebos_SpawnTormentor_Attacker` · `Ai_Mon_Special_BossMaw_SliceThroat` · `Ai_Mon_Special_BossMaw_SliceThroat_Atk` · `Ai_Mon_Special_BossObliviax_Atk` · `Ai_Mon_Special_BossPolaris_Holy_Purgatory_Spawner` · `Ai_Mon_Special_BossPolaris_Monster_Atk_Spawner` · `Ai_UnstableRatSwarm_Projectile` · `At_Mon_Special_BossLightElemental_Summon` · [BossMonster](/api/Global.BossMonster) · [CameraManager](/api/Global.CameraManager) · [DevGameManager](/api/Global.DevGameManager) · `DewConsoleCommands` · [DewDifficultySettings](/api/Global.DewDifficultySettings) · [DewNetworkManager](/api/Global.DewNetworkManager) · [DewPersistence](/api/Global.DewPersistence) · [DewPlayer](/api/Global.DewPlayer) · [FlavourManager](/api/Global.FlavourManager) · `Forest_FogAlphaControl` · `Forest_FogVoid` · [GameMod_Limbo](/api/Global.GameMod_Limbo) · `GameMod_Obliviax` · [GameResultManager](/api/Global.GameResultManager) · `Ge_CallOfTheRavenous` · [Gem](/api/Global.Gem) · `InGameAnalyticsManager` · [InGameCrashReportManager](/api/Global.InGameCrashReportManager) · [InGameReverieManager](/api/Global.InGameReverieManager) · [InGameTutorialManager](/api/Global.InGameTutorialManager) · [InGameUIManager](/api/Global.InGameUIManager) · `Ink_BossSelector` · `LobbyServiceEOS` · `LucidDream_Overpopulation` · `Mon_Despair_BossAzurak` · `Mon_Despair_DreadBug` · `Mon_Forest_BossDemon` · `Mon_GoldenLizard_ElusiveLizard` · `Mon_Ink_BossDarkMoon` · `Mon_Primus_BossPrimusAeron` · `Mon_Sky_BossNyx` · `Mon_Special_AmbushSpawner` · `Mon_Special_BossLightElemental` · `Mon_Special_BossObliviax` · `Mon_Special_BossPolaris` · [Monster](/api/Global.Monster) · [PickupManager](/api/Global.PickupManager) · [PlayGameManager](/api/Global.PlayGameManager) · `PlayTutorialManager` · [PropEnt_Merchant_Base](/api/Global.PropEnt_Merchant_Base) · `PropEnt_Stone_PitchBlackOre` · [Rift_RoomExit](/api/Global.Rift_RoomExit) · `RoomMod_Ambush` · `RoomMod_Anitya` · `RoomMod_ArcticTerritory` · `RoomMod_DistantMemories` · `RoomMod_Hunted` · `RoomMod_InkStrikeWarning` · `RoomMod_PureDream` · `RoomMod_StarCookie` · `RoomMod_UnstableRatSwarm` · `RoomMod_VeilOfDark` · [RoomModifierBase](/api/Global.RoomModifierBase) · [RoomMonsters](/api/Global.RoomMonsters) · [RoomProps](/api/Global.RoomProps) · [RoomSection](/api/Global.RoomSection) · `Se_Curse_DreamAfflictionInductive` · `Se_Elm_Fire` · `Se_HarmlessWhispers` · `Se_HeroKnockedOut` · `Se_MiniBoss_IceAura` · `Se_MirageSkin_Pulverization` · `Se_Mon_LavaLand_BossInfernus_InvulShield` · `Se_Star_I_StartSkill` · `Se_Star_Mist_I_CamillasGift` · [Section_Monsters](/api/Global.Section_Monsters) · [Shrine](/api/Global.Shrine) · `Shrine_AltarOfCleansing` · `Shrine_Ascension` · `Shrine_Disintegration` · `Shrine_DreamdustBox` · `Shrine_GoldBox` · `Shrine_MarshOfDestiny_SeedOfTorment` · `Shrine_MawOfDoom` · `Shrine_Polaris_Teleporter` · `Shrine_TheConsortOfNight_Rift` · `Shrine_UpgradeWell` · [SkillTrigger](/api/Global.SkillTrigger) · `SnowMountain_RotateFogVolume` · `StarlessPath_BossPolarisManager` · [Summon](/api/Global.Summon) · `TestMapGameManager` · [Treasure](/api/Global.Treasure) · `UI_EntityProvider_LocalHero` · `UI_InGame_AmbientLevel` · `UI_InGame_Difficulty` · `UI_InGame_GameTimer` · `UI_InGame_KnockedOutIndicator` · `UI_InGame_Location` · `UI_InGame_Map` · `UI_InGame_PickupNumbers` · `UI_InGame_QuestDisplay_Item` · `UI_InGame_ResultView` · `UI_InGame_StardustGroup` · `UI_InGame_VoteDisplay` · [ZoneManager](/api/Global.ZoneManager)

### Dependencies (41)

*Types and components that `GameManager` references or depends upon:*

[ActorManager](/api/Global.ActorManager) · `DateTimeExtensions` · [Dew](/api/Global.Dew) · [DewBuildProfile](/api/Global.DewBuildProfile) · [DewDifficultySettings](/api/Global.DewDifficultySettings) · [DewGameplayExperienceSettings](/api/Global.DewGameplayExperienceSettings) · [DewMath](/api/Global.DewMath) · [DewNetworkBehaviour](/api/Global.DewNetworkBehaviour) · [DewNetworkManager](/api/Global.DewNetworkManager) · [DewPersistence](/api/Global.DewPersistence) · [DewPlayer](/api/Global.DewPlayer) · [DewRandom](/api/Global.DewRandom) · [DewResources](/api/Global.DewResources) · [DewSave](/api/Global.DewSave) · [DewSessionError](/api/Global.DewSessionError) · [EffectAutoDestroy](/api/Global.EffectAutoDestroy) · [Entity](/api/Global.Entity) · [EntityCheck](/api/Global.EntityCheck) · [Formula](/api/Global.Formula) · [GameSettingsManager](/api/Global.GameSettingsManager) · [Gem](/api/Global.Gem) · [Hero](/api/Global.Hero) · [LoadNodeSettings](/api/Global.LoadNodeSettings) · [LobbyManager](/api/Global.LobbyManager) · [LobbyServiceProvider](/api/Global.LobbyServiceProvider) · [ManagerBase`1](/api/Global.ManagerBase`1) · [Monster](/api/Global.Monster) · [NetworkedManagerBase`1](/api/Global.NetworkedManagerBase`1) · [PerMonsterTypeData`1](/api/Global.PerMonsterTypeData`1) · [PerRarityData`1](/api/Global.PerRarityData`1) · [Room](/api/Global.Room) · [RoomMonsters](/api/Global.RoomMonsters) · [SafeAction](/api/Global.SafeAction) · [SafeAction`1](/api/Global.SafeAction`1) · [SafeAction`2](/api/Global.SafeAction`2) · [SingletonDewNetworkBehaviour`1](/api/Global.SingletonDewNetworkBehaviour`1) · [SkillTrigger](/api/Global.SkillTrigger) · [SyncableAssetRef](/api/Global.SyncableAssetRef) · [TransitionManager](/api/Global.TransitionManager) · [ZoneManager](/api/Global.ZoneManager) · `Mirror.GeneratedNetworkCode`

### Related Enums (1)

*Enumerations referenced in fields, properties, or method signatures:*

<a href="/enums#savevarflags" class="enum-link" data-tooltip="Default=0 · ApplyAfterCreation=1 · ApplyAfterFrameDelay=2">SaveVarFlags</a>

:::
