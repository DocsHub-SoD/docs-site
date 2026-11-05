# Class: DewProfileStats

- **Namespace:** `Global`
- **Assembly:** `Dew.Core.dll`

```csharp
public class DewProfileStats
```

## Fields

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`gems`** | `public Dictionary&lt;string, DewProfileStats.ItemData&gt; gems` |  |
| **`heroes`** | `public Dictionary&lt;string, DewProfileStats.HeroData&gt; heroes` |  |
| **`monsters`** | `public Dictionary&lt;string, DewProfileStats.MonsterData&gt; monsters` |  |
| **`recoveredLossPoints`** | `public List&lt;string&gt; recoveredLossPoints` |  |
| **`skills`** | `public Dictionary&lt;string, DewProfileStats.ItemData&gt; skills` |  |
| **`total`** | `public DewProfileStats.HeroData total` |  |
| **`zones`** | `public Dictionary&lt;string, DewProfileStats.ZoneData&gt; zones` |  |

## Methods

### `AddMasteryPoints(string, long)`

```csharp
public void AddMasteryPoints(string heroType, long points)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `heroType` | `string` |  |
| `points` | `long` |  |

### `ApplyRecoveryDelta(DewProfileStats)`

```csharp
public void ApplyRecoveryDelta(DewProfileStats delta)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `delta` | [DewProfileStats](/api/Global.DewProfileStats) |  |

### `GetItemData(Type)`

```csharp
public DewProfileStats.ItemData GetItemData(Type type)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `type` | `System.Type` |  |

**Returns:** `DewProfileStats.ItemData`

### `GetRecoveryDelta(DewProfileStats, DewProfileStats)`

```csharp
public static DewProfileStats GetRecoveryDelta(DewProfileStats beforeLoss, DewProfileStats afterLoss)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `beforeLoss` | [DewProfileStats](/api/Global.DewProfileStats) |  |
| `afterLoss` | [DewProfileStats](/api/Global.DewProfileStats) |  |

**Returns:** `DewProfileStats`

### `RemoveMasteryPoints(string, long)`

```csharp
public void RemoveMasteryPoints(string heroType, long points)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `heroType` | `string` |  |
| `points` | `long` |  |

### `TryGetItemData(Type, out ItemData)`

```csharp
public bool TryGetItemData(Type type, out DewProfileStats.ItemData data)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `type` | `System.Type` |  |
| `data` | [DewProfileStats.ItemData](/api/Global.DewProfileStats) |  |

**Returns:** `bool`

### `UpdateTotalData(long)`

```csharp
public void UpdateTotalData(long minPlayTime = 0)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `minPlayTime` | `long` |  |

### `Validate()`

```csharp
public void Validate()
```
