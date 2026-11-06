# Class: DewDifficultySettings

- **Category:** <span class="cat-dot" style="--cat-color: #ef4444" data-cat="Combat & Abilities"></span> Combat & Abilities
- **Namespace:** `Global`
- **Assembly:** `Dew.Core.dll`
- **Attributes:** `[CreateAssetMenu] [DewResourceLink]`

```csharp
[HideMonoScript]
[CreateAssetMenu(fileName = "New Dew Difficulty Settings", menuName = "Dew Difficulty Settings")]
[DewResourceLink(ResourceLinkBy.Name)]
public class DewDifficultySettings : ScriptableObject
```

## Fields (29)

::: details Click to expand Fields (29)

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`beneficialNodeMultiplier`** | `[Title("World", null, TitleAlignments.Left, true, true)] public float beneficialNodeMultiplier` |  |
| **`bossKillBonusStardust`** | `public int bossKillBonusStardust` |  |
| **`damageFactorAfterLoop`** | `public float damageFactorAfterLoop` |  |
| **`damageFactorBeforeLoop`** | `public float damageFactorBeforeLoop` |  |
| **`difficultyColor`** | `public Color difficultyColor` |  |
| **`enableBleedOuts`** | `public bool enableBleedOuts` |  |
| **`enemyAbilityHasteFlat`** | `[LabelText("AbilHaste %")] public float enemyAbilityHasteFlat` |  |
| **`enemyAttackSpeedPercentage`** | `[LabelText("AtkSpeed %")] public float enemyAttackSpeedPercentage` |  |
| **`enemyHealthPercentage`** | `[Title("Enemy Base Stats", null, TitleAlignments.Left, true, true)] [LabelText("Health %")] public float enemyHealthPercentage` |  |
| **`enemyMovementSpeedPercentage`** | `[LabelText("MovSpeed %")] public float enemyMovementSpeedPercentage` |  |
| **`enemyPowerPercentage`** | `[LabelText("Power %")] public float enemyPowerPercentage` |  |
| **`harmfulNodeMultiplier`** | `public float harmfulNodeMultiplier` |  |
| **`healRawMultiplier`** | `public float healRawMultiplier` |  |
| **`healthFactorAfterLoop`** | `public float healthFactorAfterLoop` |  |
| **`healthFactorBeforeLoop`** | `[Title("Enemy Scaling Stats", null, TitleAlignments.Left, true, true)] public float healthFactorBeforeLoop` |  |
| **`heroicBossArmor`** | `public float heroicBossArmor` |  |
| **`hunterSpreadChance`** | `public float hunterSpreadChance` |  |
| **`icon`** | `public Sprite icon` |  |
| **`iconScale`** | `public float iconScale` |  |
| **`lostSoulDistance`** | `public Vector2Int lostSoulDistance` |  |
| **`maxPopulationMultiplier`** | `[Title("Generic", null, TitleAlignments.Left, true, true)] public float maxPopulationMultiplier` |  |
| **`miniBossArmor`** | `[Space] [Space(16)] public float miniBossArmor` |  |
| **`positionSampleCount`** | `[Title("Enemy AI", null, TitleAlignments.Left, true, true)] [LabelText("Sample Count")] public int positionSampleCount` |  |
| **`positionSampleInterval`** | `[LabelText("Sample Interval")] public float positionSampleInterval` |  |
| **`positionSampleLagBehindFrames`** | `[LabelText("Lag Behind Count")] public int positionSampleLagBehindFrames` |  |
| **`predictionStrengthCurve`** | `public AnimationCurve predictionStrengthCurve` |  |
| **`regenOrbChanceMultiplier`** | `public float regenOrbChanceMultiplier` |  |
| **`scoreMultiplier`** | `public float scoreMultiplier` |  |
| **`specialSkillChanceMultiplier`** | `public float specialSkillChanceMultiplier` |  |

:::

## Methods (2)

::: details `GetScaledZoneIndexForDamage(float)`

```csharp
public float GetScaledZoneIndexForDamage(float zi = NaN)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `zi` | `float` |  |

**Returns:** `float`

:::

::: details `GetScaledZoneIndexForHealth(float)`

```csharp
public float GetScaledZoneIndexForHealth(float zi = NaN)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `zi` | `float` |  |

**Returns:** `float`

:::


## Architecture & Relationships

::: details Click to expand Architecture & Relationships

### Used By (6)

*Classes and systems that invoke, reference, or depend on `DewDifficultySettings`:*

[GameManager](/api/Global.GameManager) · `NetworkReaderWriterExtensions` · [PlayGameManager](/api/Global.PlayGameManager) · `PlayTutorialManager` · `TestMapGameManager` · `UI_InGame_Difficulty`

### Dependencies (8)

*Types and components that `DewDifficultySettings` references or depends upon:*

[DataProcessorGroup`3](/api/Global.DataProcessorGroup`3) · [DewBuildProfile](/api/Global.DewBuildProfile) · [Entity](/api/Global.Entity) · [EntityStatus](/api/Global.EntityStatus) · [GameManager](/api/Global.GameManager) · [NetworkedManagerBase`1](/api/Global.NetworkedManagerBase`1) · [StatBonus](/api/Global.StatBonus) · [ZoneManager](/api/Global.ZoneManager)

:::
