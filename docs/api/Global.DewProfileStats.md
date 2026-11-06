# Class: DewProfileStats

- **Category:** <span class="cat-dot" style="--cat-color: #f97316" data-cat="Data & Core Math"></span> Data & Core Math
- **Namespace:** `Global`
- **Assembly:** `Dew.Core.dll`

```csharp
public class DewProfileStats
```

## Fields (7)

::: details Click to expand Fields (7)

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`gems`** | `public Dictionary<string, DewProfileStats.ItemData> gems` |  |
| **`heroes`** | `public Dictionary<string, DewProfileStats.HeroData> heroes` |  |
| **`monsters`** | `public Dictionary<string, DewProfileStats.MonsterData> monsters` |  |
| **`recoveredLossPoints`** | `public List<string> recoveredLossPoints` |  |
| **`skills`** | `public Dictionary<string, DewProfileStats.ItemData> skills` |  |
| **`total`** | `public DewProfileStats.HeroData total` |  |
| **`zones`** | `public Dictionary<string, DewProfileStats.ZoneData> zones` |  |

:::

## Methods (8)

::: details `AddMasteryPoints(string, long)`

```csharp
public void AddMasteryPoints(string heroType, long points)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `heroType` | `string` |  |
| `points` | `long` |  |

:::

::: details `ApplyRecoveryDelta(DewProfileStats)`

```csharp
public void ApplyRecoveryDelta(DewProfileStats delta)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `delta` | [`DewProfileStats`](/api/Global.DewProfileStats) |  |

:::

::: details `GetItemData(Type)`

```csharp
public DewProfileStats.ItemData GetItemData(Type type)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `type` | `System.Type` |  |

**Returns:** `DewProfileStats.ItemData`

:::

::: details `GetRecoveryDelta(DewProfileStats, DewProfileStats)`

```csharp
public static DewProfileStats GetRecoveryDelta(DewProfileStats beforeLoss, DewProfileStats afterLoss)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `beforeLoss` | [`DewProfileStats`](/api/Global.DewProfileStats) |  |
| `afterLoss` | [`DewProfileStats`](/api/Global.DewProfileStats) |  |

**Returns:** `DewProfileStats`

:::

::: details `RemoveMasteryPoints(string, long)`

```csharp
public void RemoveMasteryPoints(string heroType, long points)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `heroType` | `string` |  |
| `points` | `long` |  |

:::

::: details `TryGetItemData(Type, out ItemData)`

```csharp
public bool TryGetItemData(Type type, out DewProfileStats.ItemData data)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `type` | `System.Type` |  |
| `data` | [`DewProfileStats.ItemData`](/api/Global.DewProfileStats) |  |

**Returns:** `bool`

:::

::: details `UpdateTotalData(long)`

```csharp
public void UpdateTotalData(long minPlayTime = 0)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `minPlayTime` | `long` |  |

:::

::: details `Validate()`

```csharp
public void Validate()
```

:::


## Architecture & Relationships

::: details Click to expand Architecture & Relationships

### Used By (17)

*Classes and systems that invoke, reference, or depend on `DewProfileStats`:*

[Dew](/api/Global.Dew) · `DewCloudSave` · [DewPlayer](/api/Global.DewPlayer) · [DewProfileItem](/api/Global.DewProfileItem) · `DewProfileMerge` · [DewSave](/api/Global.DewSave) · [GameMod_Limbo](/api/Global.GameMod_Limbo) · [TitleManager](/api/Global.TitleManager) · `TravelerStoryPresenter` · `UI_Lobby_DejavuWindow` · `UI_Lobby_DejavuWindow_Item` · `UI_ProfileStatistics` · `UI_ProfileStatistics_ItemBase` · `UI_Title_ProfileSelection_ListWindow_Item` · `UI_Tooltip_DejavuCost` · `UI_Tooltip_DejavuDescription` · `Mirror.GeneratedNetworkCode`

### Dependencies (6)

*Types and components that `DewProfileStats` references or depends upon:*

[Dew](/api/Global.Dew) · [DewBuildProfile](/api/Global.DewBuildProfile) · [DewPool](/api/Global.DewPool) · [DewProfile](/api/Global.DewProfile) · [DewResources](/api/Global.DewResources) · [DictionaryReturnHandle`2](/api/Global.DictionaryReturnHandle`2)

:::
