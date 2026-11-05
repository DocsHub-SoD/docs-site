# Class: MonsterPool.SpawnRuleEntry

- **Namespace:** `Global`
- **Assembly:** `Dew.Core.dll`

```csharp
[Serializable]
public class MonsterPool.SpawnRuleEntry
```

## Fields

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`chance`** | `public float chance` |  |
| **`conditions`** | `public List&lt;MonsterSpawnCondition&gt; conditions` |  |
| **`maxCount`** | `[HorizontalGroup("A", 0, 0, 0, 0)]
public int maxCount` |  |
| **`minCount`** | `[HorizontalGroup("A", 0, 0, 0, 0)]
public int minCount` |  |
| **`monster`** | `[HideLabel]
public AssetRef&lt;Monster&gt; monster` |  |
| **`useAnd`** | `[LabelText("All Conditions Must Match (AND)")]
[ToggleLeft]
[ShowIf("@conditions != null && conditions.Count &gt; 1", true)]
public bool useAnd` |  |

## Methods

### `Clone()`

```csharp
public MonsterPool.SpawnRuleEntry Clone()
```

**Returns:** `MonsterPool.SpawnRuleEntry`

### `EvaluateCondition()`

```csharp
public bool EvaluateCondition()
```

**Returns:** `bool`
