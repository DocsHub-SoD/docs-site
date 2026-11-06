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
| **`poolGems`** | `[SaveVar(SaveVarFlags.Default)] [NonSerialized] public List<string> poolGems` | Available on server. |
| **`poolGemsByRarity`** | `[SaveVar(SaveVarFlags.Default)] [NonSerialized] public Dictionary<Rarity, List<string>> poolGemsByRarity` | Available on server. |
| **`poolGemsByTag`** | `[SaveVar(SaveVarFlags.Default)] [NonSerialized] public Dictionary<DescriptionTags, List<string>> poolGemsByTag` | Available on server. |
| **`poolSkills`** | `[SaveVar(SaveVarFlags.Default)] [NonSerialized] public List<string> poolSkills` | Available on server. |
| **`poolSkillsByRarity`** | `[SaveVar(SaveVarFlags.Default)] [NonSerialized] public Dictionary<Rarity, List<string>> poolSkillsByRarity` | Available on server. |
| **`poolSkillsByTag`** | `[SaveVar(SaveVarFlags.Default)] [NonSerialized] public Dictionary<DescriptionTags, List<string>> poolSkillsByTag` | Available on server. |
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
