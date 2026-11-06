# Class: DewGameResult.PlayerData

- **Category:** <span class="cat-dot" style="--cat-color: #ef4444" data-cat="Combat & Abilities"></span> Combat & Abilities
- **Namespace:** `Global`
- **Assembly:** `Dew.Core.dll`

```csharp
public class DewGameResult.PlayerData
```

## Fields (35)

::: details Click to expand Fields (35)

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`abilityPower`** | `public float abilityPower` |  |
| **`addedHp`** | `public float addedHp` |  |
| **`armor`** | `public float armor` |  |
| **`attackDamage`** | `public float attackDamage` |  |
| **`attackSpeed`** | `public float attackSpeed` |  |
| **`capturedStarTooltipFields`** | `public Dictionary<string, string> capturedStarTooltipFields` |  |
| **`causeOfDeathActor`** | `public string causeOfDeathActor` |  |
| **`causeOfDeathEntity`** | `public string causeOfDeathEntity` |  |
| **`combatTime`** | `public int combatTime` |  |
| **`critChance`** | `public float critChance` |  |
| **`dealtDamageToEnemies`** | `public float dealtDamageToEnemies` |  |
| **`deaths`** | `public int deaths` |  |
| **`fireAmp`** | `public float fireAmp` |  |
| **`gems`** | `public List<DewGameResult.GemData> gems` |  |
| **`healToOthers`** | `public float healToOthers` |  |
| **`healToSelf`** | `public float healToSelf` |  |
| **`heroicBossKills`** | `public int heroicBossKills` |  |
| **`heroType`** | `public string heroType` |  |
| **`hunterKills`** | `public int hunterKills` |  |
| **`isLocalPlayer`** | `public bool isLocalPlayer` |  |
| **`kills`** | `public int kills` |  |
| **`level`** | `public int level` |  |
| **`loadout`** | `public HeroLoadoutData loadout` |  |
| **`maxDealtSingleDamageToEnemy`** | `public float maxDealtSingleDamageToEnemy` |  |
| **`maxGemCounts`** | `public List<int> maxGemCounts` |  |
| **`maxHealth`** | `public float maxHealth` |  |
| **`miniBossKills`** | `public int miniBossKills` |  |
| **`playerGuid`** | `public string playerGuid` |  |
| **`playerProfileName`** | `public string playerProfileName` |  |
| **`receivedDamage`** | `public float receivedDamage` |  |
| **`skillHaste`** | `public float skillHaste` |  |
| **`skills`** | `public List<DewGameResult.SkillData> skills` |  |
| **`totalDreamDustIncome`** | `public int totalDreamDustIncome` |  |
| **`totalGoldIncome`** | `public int totalGoldIncome` |  |
| **`totalStardustIncome`** | `public int totalStardustIncome` |  |

:::

## Methods (2)

::: details `TryGetGemData(GemLocation, out GemData)`

```csharp
public bool TryGetGemData(GemLocation location, out DewGameResult.GemData data)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `location` | [`GemLocation`](/api/Global.GemLocation) |  |
| `data` | [`DewGameResult.GemData`](/api/Global.DewGameResult) |  |

**Returns:** `bool`

:::

::: details `TryGetSkillData(HeroSkillLocation, out SkillData)`

```csharp
public bool TryGetSkillData(HeroSkillLocation type, out DewGameResult.SkillData data)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `type` | [`HeroSkillLocation`](/api/Global.HeroSkillLocation) |  |
| `data` | [`DewGameResult.SkillData`](/api/Global.DewGameResult) |  |

**Returns:** `bool`

:::


## Architecture & Relationships

::: details Click to expand Architecture & Relationships

### Used By (0)

*No incoming dependencies recorded.*

### Dependencies (0)

*No outgoing class dependencies recorded.*

### Related Enums (1)

*Enumerations referenced in fields, properties, or method signatures:*

[`HeroSkillLocation`](/enums#heroskilllocation)

:::
