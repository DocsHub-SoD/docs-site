# Class: GameManager

- **Category:** <span class="cat-dot" style="--cat-color: #ef4444" data-cat="Combat & Abilities"></span> Combat & Abilities
- **Namespace:** `Global`
- **Assembly:** `Dew.Core.dll`
- **Inheritance / Derived:** [DewNetworkBehaviour](/api/Global.DewNetworkBehaviour) → `NetworkedManagerBase` → [GameManager](/api/Global.GameManager) → [DevGameManager](/api/Global.DevGameManager) → [PlayGameManager](/api/Global.PlayGameManager)

```csharp
public class GameManager : NetworkedManagerBase<GameManager>, ILogicUpdate
```

## Fields

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`ClientEvent_OnAmbientLevelChanged`** | `public SafeAction<int, int> ClientEvent_OnAmbientLevelChanged` | Called everywhere when ambient level changes |
| **`ClientEvent_OnDifficultyChanged`** | `public SafeAction<DewDifficultySettings, DewDifficultySettings> ClientEvent_OnDifficultyChanged` | Called everywhere when threat level changes |
| **`ClientEvent_OnGameConcluded`** | `public SafeAction ClientEvent_OnGameConcluded` | Called everywhere when game is concluded |
| **`disableStuckCheck`** | `public bool disableStuckCheck` |  |
| **`gainedExpMultiplier`** | `[NonSerialized] public float gainedExpMultiplier` |  |
| **`ges`** | `public DewGameplayExperienceSettings ges` |  |
| **`gesTemplate`** | `[FormerlySerializedAs("gss")] public DewGameplayExperienceSettings gesTemplate` |  |
| **`goldCostMultiplier`** | `[NonSerialized] public float goldCostMultiplier` |  |
| **`goldIncomeMultiplier`** | `[NonSerialized] public float goldIncomeMultiplier` |  |
| **`playerRejoinData`** | `[SaveVar(SaveVarFlags.Default)] public Dictionary<string, DewPersistence.PlayerData> playerRejoinData` |  |
| **`predictionStrengthOverride`** | `public Func<float> predictionStrengthOverride` |  |

## Properties

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`ambientLevel`** | `[SaveVar(SaveVarFlags.Default)] public int ambientLevel { get; set; }` |  |
| **`difficulty`** | `[SaveVar(SaveVarFlags.Default)] public DewDifficultySettings difficulty { get; set; }` |  |
| **`elapsedGameTime`** | `[SaveVar(SaveVarFlags.Default)] public float elapsedGameTime { get; set; }` | Elapsed game time in seconds. |
| **`isGameConcluded`** | `public bool isGameConcluded { get; }` |  |
| **`isGameOverEnabled`** | `public bool isGameOverEnabled { get; set; }` |  |
| **`isGameTimePaused`** | `public bool isGameTimePaused { get; }` |  |
| **`isGameTimePausedByAfk`** | `public bool isGameTimePausedByAfk { get; set; }` |  |
| **`isGameTimePausedByGame`** | `public bool isGameTimePausedByGame { get; set; }` |  |
| **`isMidRunSaveLocked`** | `public bool isMidRunSaveLocked { get; }` | Is continue save blocked by LockMidRunSave()? Available everywhere. |
| **`isSpawnOverPopulation`** | `public bool isSpawnOverPopulation { get; }` |  |
| **`maxAndSpawnedPopulationMultiplier`** | `public float maxAndSpawnedPopulationMultiplier { get; set; }` |  |
| **`maxSpawnedPopulation`** | `public float maxSpawnedPopulation { get; }` |  |
| **`runId`** | `[SaveVar(SaveVarFlags.Default)] public string runId { get; set; }` | Globally unique identifier of this run. This is consistent across all clients. |
| **`spawnedPopulation`** | `public float spawnedPopulation { get; }` | Total population excluding env spawns. =&gt; Spawns from combat areas. |

## Methods

### `Awake()`

```csharp
protected override void Awake()
```

### `CallOnReady(Action)`

Call provided function if the game is ready. (Client is ready, Server is not loading scene, has local hero, map is loaded, screen is shown)If not ready, the function call will be delayed until it is.Available on server and clients.

```csharp
public static void CallOnReady(Action action)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `action` | `System.Action` |  |

### `CollectAllPlayersRejoinData()`

```csharp
public void CollectAllPlayersRejoinData()
```

### `CollectPlayerRejoinData(DewPlayer)`

```csharp
public void CollectPlayerRejoinData(DewPlayer p)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `p` | [`DewPlayer`](/api/Global.DewPlayer) |  |

### `ConcludePureWhiteDream()`

```csharp
public void ConcludePureWhiteDream()
```

### `ConcludeUnknownFate()`

```csharp
public void ConcludeUnknownFate()
```

### `GetAdjustedDroppedExperienceAmount(float)`

```csharp
public float GetAdjustedDroppedExperienceAmount(float original)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `original` | `float` |  |

**Returns:** `float`

### `GetAdjustedGoldAmount_Cost_Service(float)`

```csharp
public float GetAdjustedGoldAmount_Cost_Service(float baseAmount)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `baseAmount` | `float` |  |

**Returns:** `float`

### `GetAdjustedGoldAmount_Cost(float)`

```csharp
public float GetAdjustedGoldAmount_Cost(float amount)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `amount` | `float` |  |

**Returns:** `float`

### `GetAdjustedGoldAmount_Income(float)`

```csharp
public float GetAdjustedGoldAmount_Income(float amount)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `amount` | `float` |  |

**Returns:** `float`

### `GetAdjustedGoldAmount(float)`

```csharp
public float GetAdjustedGoldAmount(float amount)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `amount` | `float` |  |

**Returns:** `float`

### `GetAdjustedMonsterSpawnPopulation(float, bool, bool)`

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

### `GetAdjustedMonsterWaves(int, DewRandom)`

```csharp
public int GetAdjustedMonsterWaves(int original, DewRandom random = null)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `original` | `int` |  |
| `random` | [`DewRandom`](/api/Global.DewRandom) |  |

**Returns:** `int`

### `GetAdjustedMonsterWavesMultiplier()`

```csharp
public float GetAdjustedMonsterWavesMultiplier()
```

**Returns:** `float`

### `GetBossMonsterDamageMultiplierByScaling(float)`

```csharp
public float GetBossMonsterDamageMultiplierByScaling(float customZoneIndex = NaN)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `customZoneIndex` | `float` |  |

**Returns:** `float`

### `GetBossMonsterHealthMultiplierByScaling(float)`

```csharp
public float GetBossMonsterHealthMultiplierByScaling(float customZoneIndex = NaN)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `customZoneIndex` | `float` |  |

**Returns:** `float`

### `GetCleanseGemMinQuality()`

```csharp
public int GetCleanseGemMinQuality()
```

**Returns:** `int`

### `GetCleanseGoldCost(Gem)`

```csharp
public int GetCleanseGoldCost(Gem gem)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `gem` | [`Gem`](/api/Global.Gem) |  |

**Returns:** `int`

### `GetCleanseGoldCost(SkillTrigger)`

```csharp
public int GetCleanseGoldCost(SkillTrigger skill)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `skill` | [`SkillTrigger`](/api/Global.SkillTrigger) |  |

**Returns:** `int`

### `GetCleanseReturnedDreamDust(DewPlayer, Gem)`

```csharp
public int GetCleanseReturnedDreamDust(DewPlayer player, Gem gem)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `player` | [`DewPlayer`](/api/Global.DewPlayer) |  |
| `gem` | [`Gem`](/api/Global.Gem) |  |

**Returns:** `int`

### `GetCleanseReturnedDreamDust(DewPlayer, SkillTrigger)`

```csharp
public int GetCleanseReturnedDreamDust(DewPlayer player, SkillTrigger skill)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `player` | [`DewPlayer`](/api/Global.DewPlayer) |  |
| `skill` | [`SkillTrigger`](/api/Global.SkillTrigger) |  |

**Returns:** `int`

### `GetCleanseSkillMinLevel()`

```csharp
public int GetCleanseSkillMinLevel()
```

**Returns:** `int`

### `GetDifficulty()`

```csharp
protected virtual DewDifficultySettings GetDifficulty()
```

**Returns:** `DewDifficultySettings`

### `GetExpDropFromEntity(Entity)`

```csharp
public float GetExpDropFromEntity(Entity ent)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `ent` | [`Entity`](/api/Global.Entity) |  |

**Returns:** `float`

### `GetGainedSkillHastePerSkillLevel(SkillTrigger)`

```csharp
public float GetGainedSkillHastePerSkillLevel(SkillTrigger skillTrigger)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `skillTrigger` | [`SkillTrigger`](/api/Global.SkillTrigger) |  |

**Returns:** `float`

### `GetGemUpgradeAddedQuality()`

```csharp
public int GetGemUpgradeAddedQuality()
```

**Returns:** `int`

### `GetGemUpgradeDreamDustCost(Gem)`

```csharp
public int GetGemUpgradeDreamDustCost(Gem gem)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `gem` | [`Gem`](/api/Global.Gem) |  |

**Returns:** `int`

### `GetGemUpgradeDreamDustCost(int)`

```csharp
public int GetGemUpgradeDreamDustCost(int quality)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `quality` | `int` |  |

**Returns:** `int`

### `GetKillGoldAmount(Entity)`

```csharp
public int GetKillGoldAmount(Entity ent)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `ent` | [`Entity`](/api/Global.Entity) |  |

**Returns:** `int`

### `GetLucidDreams()`

```csharp
public virtual IList<string> GetLucidDreams()
```

**Returns:** `System.Collections.Generic.IList<T><string>`

### `GetMiniBossMonsterDamageMultiplierByScaling(float)`

```csharp
public float GetMiniBossMonsterDamageMultiplierByScaling(float customZoneIndex = NaN)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `customZoneIndex` | `float` |  |

**Returns:** `float`

### `GetMiniBossMonsterHealthMultiplierByScaling(float)`

```csharp
public float GetMiniBossMonsterHealthMultiplierByScaling(float customZoneIndex = NaN)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `customZoneIndex` | `float` |  |

**Returns:** `float`

### `GetMonsterBonusHealthPercentageByMultiplayer(Monster)`

```csharp
public float GetMonsterBonusHealthPercentageByMultiplayer(Monster m)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `m` | [`Monster`](/api/Global.Monster) |  |

**Returns:** `float`

### `GetMonsterBonusPowerPercentage(Monster)`

```csharp
public float GetMonsterBonusPowerPercentage(Monster m)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `m` | [`Monster`](/api/Global.Monster) |  |

**Returns:** `float`

### `GetMultiplayerDifficultyFactor(bool)`

Get amount of extra players. Solo: 0, Two: 1, ...If reduceWhenDead is set, dead player will contribute 55% percent instead of 100% to the factor.

```csharp
public float GetMultiplayerDifficultyFactor(bool reduceWhenDead)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `reduceWhenDead` | `bool` |  |

**Returns:** `float`

### `GetMultiplier_Imp(double, double, double, double, double, int)`

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

### `GetPredictionStrength()`

```csharp
public float GetPredictionStrength()
```

**Returns:** `float`

### `GetRegularMonsterDamageMultiplierByScaling(float)`

```csharp
public float GetRegularMonsterDamageMultiplierByScaling(float customZoneIndex = NaN)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `customZoneIndex` | `float` |  |

**Returns:** `float`

### `GetRegularMonsterHealthMultiplierByScaling(float)`

```csharp
public float GetRegularMonsterHealthMultiplierByScaling(float customZoneIndex = NaN)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `customZoneIndex` | `float` |  |

**Returns:** `float`

### `GetSkillUpgradeDreamDustCost(SkillTrigger)`

```csharp
public int GetSkillUpgradeDreamDustCost(SkillTrigger skill)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `skill` | [`SkillTrigger`](/api/Global.SkillTrigger) |  |

**Returns:** `int`

### `GetSkillUpgradeDreamDustCost(int)`

```csharp
public int GetSkillUpgradeDreamDustCost(int level)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `level` | `int` |  |

**Returns:** `int`

### `GetSpecialRewardAmount_DreamDust()`

```csharp
public float GetSpecialRewardAmount_DreamDust()
```

**Returns:** `float`

### `GetSpecialRewardAmount_Gold()`

```csharp
public float GetSpecialRewardAmount_Gold()
```

**Returns:** `float`

### `GetSpecialSkillChanceMultiplier()`

```csharp
public float GetSpecialSkillChanceMultiplier()
```

**Returns:** `float`

### `GetStrongHealthScalingMultiplier_Imp(float)`

```csharp
public static float GetStrongHealthScalingMultiplier_Imp(float zi)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `zi` | `float` |  |

**Returns:** `float`

### `GetUniversalDamageScalingMultiplier_Imp(float)`

```csharp
public static float GetUniversalDamageScalingMultiplier_Imp(float zi)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `zi` | `float` |  |

**Returns:** `float`

### `GetWeakHealthScalingMultiplier_Imp(float)`

```csharp
public static float GetWeakHealthScalingMultiplier_Imp(float zi)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `zi` | `float` |  |

**Returns:** `float`

### `IsContinueSaveSupported()`

Is continue-saving a normal thing in this game manager? If not, no continue save will be made, and user will not be notified with any save-related things.Used to tell apart from normal game and special games like tutorial.

```csharp
public virtual bool IsContinueSaveSupported()
```

**Returns:** `bool`

### `IsEligibleForMidRunSave()`

Can the game be saved mid-run right now? Usually save is made every travel, but after clearing the room, the game can be saved mid-run e.g. before exiting the game.

```csharp
public bool IsEligibleForMidRunSave()
```

**Returns:** `bool`

### `IsLazyCallReady()`

```csharp
public virtual bool IsLazyCallReady()
```

**Returns:** `bool`

### `LoadNextZone()`

```csharp
public virtual void LoadNextZone()
```

### `LockMidRunSave()`

Calling this will lock mid-run save.If a continue save hasn't been made for more than 20 seconds, a continue save will be immediately made.This call MUST BE ACCOMPANIED by the same number of UnlockMidRunSave() calls.

```csharp
public void LockMidRunSave()
```

### `LogicUpdate(float)`

```csharp
public override void LogicUpdate(float dt)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `dt` | `float` |  |

### `OnDestroy()`

```csharp
protected override void OnDestroy()
```

### `OnStart()`

```csharp
public override void OnStart()
```

### `OnStartServer()`

```csharp
public override void OnStartServer()
```

### `ResetGameplayExperienceSettings()`

```csharp
public void ResetGameplayExperienceSettings()
```

### `SaveContinueData(LoadNodeSettings)`

```csharp
public void SaveContinueData(LoadNodeSettings s)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `s` | [`LoadNodeSettings`](/api/Global.LoadNodeSettings) |  |

### `SaveContinueDataMidRun()`

```csharp
public void SaveContinueDataMidRun()
```

### `SetAmbientLevel(int)`

Level will be clamped accordingly to GSS.

```csharp
public void SetAmbientLevel(int newLevel)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `newLevel` | `int` |  |

### `SetDisconnectedForEveryoneElse()`

```csharp
public void SetDisconnectedForEveryoneElse()
```

### `SetElapsedGameTime(float)`

```csharp
public void SetElapsedGameTime(float newTime)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `newTime` | `float` |  |

### `UnlockMidRunSave()`

Calling this will unlock and allow mid-run saves.This call MUST BE DONE AFTER LockMidRunSave() calls.

```csharp
public void UnlockMidRunSave()
```

### `UpdateSpawnedPopulation()`

```csharp
public void UpdateSpawnedPopulation()
```

### `WrapUpAndShowResult(ResultType)`

```csharp
public void WrapUpAndShowResult(DewGameResult.ResultType type)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `type` | [`DewGameResult.ResultType`](/api/Global.DewGameResult) |  |
