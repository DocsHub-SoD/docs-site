# Class: LootManager

- **Category:** <span class="cat-dot" style="--cat-color: #eab308" data-cat="Items & Economy"></span> Items & Economy
- **Namespace:** `Global`
- **Assembly:** `Dew.Core.dll`
- **Inheritance / Derived:** [DewNetworkBehaviour](/api/Global.DewNetworkBehaviour) → `NetworkedManagerBase` → [LootManager](/api/Global.LootManager)

```csharp
public class LootManager : NetworkedManagerBase<LootManager>, ILogicUpdate
```

## Fields (16)

::: details Click to expand Fields (16)

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`gemQualityMaxByZoneIndex`** | `public PerRarityData<Formula> gemQualityMaxByZoneIndex` |  |
| **`gemQualityMinByZoneIndex`** | `public PerRarityData<Formula> gemQualityMinByZoneIndex` |  |
| **`gemQualityRandomCurve`** | `public AnimationCurve gemQualityRandomCurve` |  |
| **`gemRarityChance`** | `[Title("Gem", null, TitleAlignments.Left, true, true)] public PerRarityData<float> gemRarityChance` |  |
| **`gemRarityChanceHigh`** | `public PerRarityData<float> gemRarityChanceHigh` |  |
| **`poolGems`** | `[SaveVar] [SaveVar(SaveVarFlags.Default)] [NonSerialized] public List<string> poolGems` | Available on server. |
| **`poolGemsByRarity`** | `[SaveVar] [SaveVar(SaveVarFlags.Default)] [NonSerialized] public Dictionary<Rarity, List<string>> poolGemsByRarity` | Available on server. |
| **`poolGemsByTag`** | `[SaveVar] [SaveVar(SaveVarFlags.Default)] [NonSerialized] public Dictionary<DescriptionTags, List<string>> poolGemsByTag` | Available on server. |
| **`poolSkills`** | `[SaveVar] [SaveVar(SaveVarFlags.Default)] [NonSerialized] public List<string> poolSkills` | Available on server. |
| **`poolSkillsByRarity`** | `[SaveVar] [SaveVar(SaveVarFlags.Default)] [NonSerialized] public Dictionary<Rarity, List<string>> poolSkillsByRarity` | Available on server. |
| **`poolSkillsByTag`** | `[SaveVar] [SaveVar(SaveVarFlags.Default)] [NonSerialized] public Dictionary<DescriptionTags, List<string>> poolSkillsByTag` | Available on server. |
| **`skillLevelMaxByZoneIndex`** | `public PerRarityData<Formula> skillLevelMaxByZoneIndex` |  |
| **`skillLevelMinByZoneIndex`** | `public PerRarityData<Formula> skillLevelMinByZoneIndex` |  |
| **`skillLevelRandomCurve`** | `public AnimationCurve skillLevelRandomCurve` |  |
| **`skillRarityChance`** | `[Title("Skill", null, TitleAlignments.Left, true, true)] public PerRarityData<float> skillRarityChance` |  |
| **`skillRarityChanceHigh`** | `public PerRarityData<float> skillRarityChanceHigh` |  |

:::

## Methods (8)

::: details `OnStartServer()`

```csharp
public override void OnStartServer()
```

:::

::: details `SelectGemAndQuality(Rarity?, out Gem, out int)`

```csharp
public void SelectGemAndQuality(Rarity? rarity, out Gem gem, out int quality)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `rarity` | [`Rarity?`](/api/Global.Rarity) |  |
| `gem` | [`Gem`](/api/Global.Gem) |  |
| `quality` | `int` |  |

:::

::: details `SelectGemQuality(Rarity)`

```csharp
public int SelectGemQuality(Rarity rarity)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `rarity` | [`Rarity`](/api/Global.Rarity) |  |

**Returns:** `int`

:::

::: details `SelectGemRarity(bool)`

```csharp
public Rarity SelectGemRarity(bool isHigh = false)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `isHigh` | `bool` |  |

**Returns:** `Rarity`

:::

::: details `SelectRarity(PerRarityData&lt;float&gt;)`

```csharp
public static Rarity SelectRarity(PerRarityData<float> chances)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `chances` | `PerRarityData<float>` |  |

**Returns:** `Rarity`

:::

::: details `SelectSkillAndLevel(Rarity?, out SkillTrigger, out int)`

```csharp
public void SelectSkillAndLevel(Rarity? rarity, out SkillTrigger skill, out int level)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `rarity` | [`Rarity?`](/api/Global.Rarity) |  |
| `skill` | [`SkillTrigger`](/api/Global.SkillTrigger) |  |
| `level` | `int` |  |

:::

::: details `SelectSkillLevel(Rarity)`

```csharp
public int SelectSkillLevel(Rarity rarity)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `rarity` | [`Rarity`](/api/Global.Rarity) |  |

**Returns:** `int`

:::

::: details `SelectSkillRarity(bool)`

```csharp
public Rarity SelectSkillRarity(bool isHigh = false)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `isHigh` | `bool` |  |

**Returns:** `Rarity`

:::


## Architecture & Relationships

::: details Click to expand Architecture & Relationships

### Used By (15)

*Classes and systems that invoke, reference, or depend on `LootManager`:*

`Ai_RandomGemUpgrade` · [Gem](/api/Global.Gem) · [PropEnt_Merchant_Jonas](/api/Global.PropEnt_Merchant_Jonas) · `Se_Star_I_FirstBossGemDrop` · `Se_Star_I_GemOnMiniBossKill` · `Shrine_CallOfTheRavenous` · `Shrine_Destiny` · `Shrine_Enlightenment` · `Shrine_FallenStar` · `Shrine_Luck` · `Shrine_MarshOfDestiny_SeedOfTorment` · `Shrine_Paradox` · `Shrine_Retrospection` · `SpawnGemStarProp` · `Treasure_SuspiciousHat`

### Dependencies (11)

*Types and components that `LootManager` references or depends upon:*

[Dew](/api/Global.Dew) · [DewNetworkBehaviour](/api/Global.DewNetworkBehaviour) · [DewPlayer](/api/Global.DewPlayer) · [DewResources](/api/Global.DewResources) · [Formula](/api/Global.Formula) · [ManagerBase`1](/api/Global.ManagerBase`1) · [NetworkedManagerBase`1](/api/Global.NetworkedManagerBase`1) · [PerRarityData`1](/api/Global.PerRarityData`1) · [SkillTrigger](/api/Global.SkillTrigger) · [TransitionManager](/api/Global.TransitionManager) · [ZoneManager](/api/Global.ZoneManager)

### Related Enums (3)

*Enumerations referenced in fields, properties, or method signatures:*

[`DescriptionTags`](/enums#descriptiontags) · [`Rarity`](/enums#rarity) · [`SaveVarFlags`](/enums#savevarflags)

:::
