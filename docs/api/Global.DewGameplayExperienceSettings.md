# Class: DewGameplayExperienceSettings

- **Category:** <span class="cat-dot" style="--cat-color: #ef4444" data-cat="Combat & Abilities"></span> Combat & Abilities
- **Namespace:** `Global`
- **Assembly:** `Dew.Core.dll`
- **Attributes:** `[CreateAssetMenu]`

```csharp
[CreateAssetMenu(fileName = "New Dew Game Experience Settings", menuName = "Dew Game Experience Settings")]
public class DewGameplayExperienceSettings : SerializedScriptableObject
```

## Fields (59)

::: details Click to expand Fields (59)

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`bossBonusHealthPercentagePerPlayer`** | `[LabelText("Boss Bonus Health % Per Extra Player")] public float bossBonusHealthPercentagePerPlayer` |  |
| **`bossBonusPowerPercentagePerPlayer`** | `[LabelText("Boss Bonus Power % Per Extra Player")] public float bossBonusPowerPercentagePerPlayer` |  |
| **`bossRewardsDreamDustMax`** | `[LabelText("Dream Dust Max")] public Formula bossRewardsDreamDustMax` |  |
| **`bossRewardsDreamDustMin`** | `[LabelText("Dream Dust Min")] public Formula bossRewardsDreamDustMin` |  |
| **`bossRewardsGoldMax`** | `[LabelText("Gold Max")] public Formula bossRewardsGoldMax` |  |
| **`bossRewardsGoldMin`** | `[Header] [Header("Boss Rewards by Zone Index")] [LabelText("Gold Min")] public Formula bossRewardsGoldMin` |  |
| **`combatRewardFantasyChance`** | `[LabelText("Fantasy")] public Formula combatRewardFantasyChance` |  |
| **`combatRewardMemoryChance`** | `[Header] [Header("Combat Reward Chances By Zone Index")] [LabelText("Memory")] public Formula combatRewardMemoryChance` |  |
| **`cooldownFloorRatioByAbilityHaste`** | `[Header] [Header("Cooldown Reductions")] public float cooldownFloorRatioByAbilityHaste` |  |
| **`cooldownFloorRatioBySkillUpgrade`** | `public float cooldownFloorRatioBySkillUpgrade` |  |
| **`droppedExpMultiplierPerPlayer`** | `public float droppedExpMultiplierPerPlayer` |  |
| **`expDropDeviation`** | `public float expDropDeviation` |  |
| **`expGlobalMultiplier`** | `public float expGlobalMultiplier` |  |
| **`expMultiplier`** | `public PerMonsterTypeData<float> expMultiplier` |  |
| **`gainedSkillHastePerSkillLevel`** | `public float gainedSkillHastePerSkillLevel` |  |
| **`gemAddedQualityOnUpgrade`** | `public int gemAddedQualityOnUpgrade` |  |
| **`gemCleanseCostByQuality`** | `[Header] [Header("Cleanses")] public Formula gemCleanseCostByQuality` |  |
| **`gemCleanseMinQuality`** | `public int gemCleanseMinQuality` |  |
| **`gemDismantleDreamDustByQuality`** | `[Header] [Header("Dismantle, Upgrades")] public Formula gemDismantleDreamDustByQuality` |  |
| **`gemDismantleDreamDustMultiplier`** | `public PerRarityData<float> gemDismantleDreamDustMultiplier` |  |
| **`gemUpgradeDreamDustByQuality`** | `public Formula gemUpgradeDreamDustByQuality` |  |
| **`gemValue`** | `public PerRarityData<int> gemValue` |  |
| **`generalServiceGoldPriceMultiplier`** | `public float generalServiceGoldPriceMultiplier` |  |
| **`generalServiceGoldPriceMultiplierByZoneIndex`** | `public Formula generalServiceGoldPriceMultiplierByZoneIndex` |  |
| **`globalGoldEconomyMultiplierByZoneIndex`** | `[Header] [Header("Gold")] public Formula globalGoldEconomyMultiplierByZoneIndex` |  |
| **`killGold`** | `public PerMonsterTypeData<float> killGold` |  |
| **`killGoldDeviation`** | `public float killGoldDeviation` |  |
| **`killGoldMultiplierByZoneIndex`** | `public Formula killGoldMultiplierByZoneIndex` |  |
| **`maxGlobalPopulation`** | `[Header] [Header("Max Population (Spawned)")] [LabelText("Max Spawned Population")] public float maxGlobalPopulation` |  |
| **`maxGlobalPopulationMultiplierByAmbientLevel`** | `[LabelText("Multiplier By Ambient Level")] public Formula maxGlobalPopulationMultiplierByAmbientLevel` |  |
| **`maxGlobalPopulationMultiplierPerPlayer`** | `[LabelText("Multiplier Per Extra Player")] public float maxGlobalPopulationMultiplierPerPlayer` |  |
| **`maxHeroLevel`** | `[Header] [Header("Experience")] public int maxHeroLevel` |  |
| **`maxSectionPopulation`** | `[Header] [Header("Max Population (Section)")] [LabelText("Max Population")] public float maxSectionPopulation` |  |
| **`maxSectionPopulationMultiplierByAmbientLevel`** | `[LabelText("Multiplier By Ambient Level")] public Formula maxSectionPopulationMultiplierByAmbientLevel` |  |
| **`maxSectionPopulationMultiplierPerPlayerInSection`** | `[LabelText("Multiplier Per Extra Player In Section")] public float maxSectionPopulationMultiplierPerPlayerInSection` |  |
| **`miniBossBonusHealthPercentagePerPlayer`** | `[LabelText("MiniBoss Bonus Health % Per Extra Player")] public float miniBossBonusHealthPercentagePerPlayer` |  |
| **`miniBossBonusPowerPercentagePerPlayer`** | `[LabelText("MiniBoss Bonus Power % Per Extra Player")] public float miniBossBonusPowerPercentagePerPlayer` |  |
| **`miniBossSpawnChanceByNonMiniBossCombatNodesVisited`** | `[Header] [Header("Monsters")] public Formula miniBossSpawnChanceByNonMiniBossCombatNodesVisited` |  |
| **`monsterBonusHealthPercentagePerPlayer`** | `[LabelText("Bonus Health % Per Extra Player")] public float monsterBonusHealthPercentagePerPlayer` |  |
| **`monsterBonusPowerPercentagePerPlayer`** | `[LabelText("Bonus Power % Per Extra Player")] public float monsterBonusPowerPercentagePerPlayer` |  |
| **`monsterSpawnPopulationMultiplierByTurnIndex`** | `[LabelText("Total Spawned Pop Multiplier By Turn Index")] public Formula monsterSpawnPopulationMultiplierByTurnIndex` |  |
| **`monsterSpawnPopulationMultiplierPerPlayer`** | `[LabelText("Total Spawned Pop Multiplier Per Extra Player")] public float monsterSpawnPopulationMultiplierPerPlayer` |  |
| **`monsterWavesMultiplierPerPlayer`** | `[LabelText("Waves Multiplier Per Extra Player")] public float monsterWavesMultiplierPerPlayer` |  |
| **`regenOrbDropChanceOnLowHealth`** | `public PerMonsterTypeData<float> regenOrbDropChanceOnLowHealth` |  |
| **`regenOrbDropChanceOnMaxHealth`** | `[Header] [Header("Regen Orb")] public PerMonsterTypeData<float> regenOrbDropChanceOnMaxHealth` |  |
| **`sellValueMultiplier`** | `public float sellValueMultiplier` |  |
| **`skillCleanseCostByLevel`** | `public Formula skillCleanseCostByLevel` |  |
| **`skillCleanseMinLevel`** | `public int skillCleanseMinLevel` |  |
| **`skillDismantleDreamDustByLevel`** | `public Formula skillDismantleDreamDustByLevel` |  |
| **`skillDismantleDreamDustMultiplier`** | `public PerRarityData<float> skillDismantleDreamDustMultiplier` |  |
| **`skillUpgradeDreamDustByLevel`** | `public Formula skillUpgradeDreamDustByLevel` |  |
| **`skillValue`** | `public PerRarityData<int> skillValue` |  |
| **`stardustBossSoulAmount`** | `[LabelText("Boss Soul Amount")] public Vector2Int stardustBossSoulAmount` |  |
| **`stardustDeathDropAmount`** | `[LabelText("Death Drop Amount Range")] public Vector2Int stardustDeathDropAmount` |  |
| **`stardustDeathDropChance`** | `[Header] [Header("Stardust")] [LabelText("Death Drop Chance")] public PerMonsterTypeData<float> stardustDeathDropChance` |  |
| **`valueGlobalMultiplier`** | `[Header] [Header("Buy, Sell")] public float valueGlobalMultiplier` |  |
| **`valueMultiplierPerGemQuality`** | `public float valueMultiplierPerGemQuality` |  |
| **`valueMultiplierPerSkillLevel`** | `public float valueMultiplierPerSkillLevel` |  |
| **`welcomingSpawnPopMultiplierByArea`** | `[Header] [Header("Hunters")] public AnimationCurve welcomingSpawnPopMultiplierByArea` |  |

:::


## Architecture & Relationships

::: details Click to expand Architecture & Relationships

### Used By (1)

*Classes and systems that invoke, reference, or depend on `DewGameplayExperienceSettings`:*

[GameManager](/api/Global.GameManager)

### Dependencies (3)

*Types and components that `DewGameplayExperienceSettings` references or depends upon:*

[Formula](/api/Global.Formula) · [PerMonsterTypeData`1](/api/Global.PerMonsterTypeData`1) · [PerRarityData`1](/api/Global.PerRarityData`1)

### Related Enums (1)

*Enumerations referenced in fields, properties, or method signatures:*

<a href="/enums#rarity" class="enum-link" data-tooltip="Common=0 · Rare=1 · Epic=2 · Legendary=3 · Character=4 (+2 more)">Rarity</a>

:::
