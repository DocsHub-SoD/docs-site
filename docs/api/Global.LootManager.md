# Class: LootManager

- **Namespace:** `Global`
- **Assembly:** `Dew.Core.dll`
- **Inheritance / Derived:** [DewNetworkBehaviour](/api/Global.DewNetworkBehaviour) → `NetworkedManagerBase` → [LootManager](/api/Global.LootManager)

```csharp
public class LootManager : NetworkedManagerBase<LootManager>, ILogicUpdate
```

## Fields

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`gemQualityMaxByZoneIndex`** | `public PerRarityData&lt;Formula&gt; gemQualityMaxByZoneIndex` |  |
| **`gemQualityMinByZoneIndex`** | `public PerRarityData&lt;Formula&gt; gemQualityMinByZoneIndex` |  |
| **`gemQualityRandomCurve`** | `public AnimationCurve gemQualityRandomCurve` |  |
| **`gemRarityChance`** | `[Title("Gem", null, TitleAlignments.Left, true, true)]
public PerRarityData&lt;float&gt; gemRarityChance` |  |
| **`gemRarityChanceHigh`** | `public PerRarityData&lt;float&gt; gemRarityChanceHigh` |  |
| **`poolGems`** | `[SaveVar(SaveVarFlags.Default)]
[NonSerialized]
public List&lt;string&gt; poolGems` | Available on server. |
| **`poolGemsByRarity`** | `[SaveVar(SaveVarFlags.Default)]
[NonSerialized]
public Dictionary&lt;Rarity, List&lt;string&gt;&gt; poolGemsByRarity` | Available on server. |
| **`poolGemsByTag`** | `[SaveVar(SaveVarFlags.Default)]
[NonSerialized]
public Dictionary&lt;DescriptionTags, List&lt;string&gt;&gt; poolGemsByTag` | Available on server. |
| **`poolSkills`** | `[SaveVar(SaveVarFlags.Default)]
[NonSerialized]
public List&lt;string&gt; poolSkills` | Available on server. |
| **`poolSkillsByRarity`** | `[SaveVar(SaveVarFlags.Default)]
[NonSerialized]
public Dictionary&lt;Rarity, List&lt;string&gt;&gt; poolSkillsByRarity` | Available on server. |
| **`poolSkillsByTag`** | `[SaveVar(SaveVarFlags.Default)]
[NonSerialized]
public Dictionary&lt;DescriptionTags, List&lt;string&gt;&gt; poolSkillsByTag` | Available on server. |
| **`skillLevelMaxByZoneIndex`** | `public PerRarityData&lt;Formula&gt; skillLevelMaxByZoneIndex` |  |
| **`skillLevelMinByZoneIndex`** | `public PerRarityData&lt;Formula&gt; skillLevelMinByZoneIndex` |  |
| **`skillLevelRandomCurve`** | `public AnimationCurve skillLevelRandomCurve` |  |
| **`skillRarityChance`** | `[Title("Skill", null, TitleAlignments.Left, true, true)]
public PerRarityData&lt;float&gt; skillRarityChance` |  |
| **`skillRarityChanceHigh`** | `public PerRarityData&lt;float&gt; skillRarityChanceHigh` |  |

## Methods

### `OnStartServer()`

```csharp
public override void OnStartServer()
```

### `SelectGemAndQuality(Rarity?, out Gem, out int)`

```csharp
public void SelectGemAndQuality(Rarity? rarity, out Gem gem, out int quality)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `rarity` | [Rarity?](/api/Global.Rarity) |  |
| `gem` | [Gem](/api/Global.Gem) |  |
| `quality` | `int` |  |

### `SelectGemQuality(Rarity)`

```csharp
public int SelectGemQuality(Rarity rarity)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `rarity` | [Rarity](/api/Global.Rarity) |  |

**Returns:** `int`

### `SelectGemRarity(bool)`

```csharp
public Rarity SelectGemRarity(bool isHigh = false)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `isHigh` | `bool` |  |

**Returns:** `Rarity`

### `SelectRarity(PerRarityData&lt;float&gt;)`

```csharp
public static Rarity SelectRarity(PerRarityData<float> chances)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `chances` | `PerRarityData&lt;float&gt;` |  |

**Returns:** `Rarity`

### `SelectSkillAndLevel(Rarity?, out SkillTrigger, out int)`

```csharp
public void SelectSkillAndLevel(Rarity? rarity, out SkillTrigger skill, out int level)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `rarity` | [Rarity?](/api/Global.Rarity) |  |
| `skill` | [SkillTrigger](/api/Global.SkillTrigger) |  |
| `level` | `int` |  |

### `SelectSkillLevel(Rarity)`

```csharp
public int SelectSkillLevel(Rarity rarity)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `rarity` | [Rarity](/api/Global.Rarity) |  |

**Returns:** `int`

### `SelectSkillRarity(bool)`

```csharp
public Rarity SelectSkillRarity(bool isHigh = false)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `isHigh` | `bool` |  |

**Returns:** `Rarity`
