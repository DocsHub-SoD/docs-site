# Class: MonsterPool.SpawnRuleEntry

- **Category:** <span class="cat-dot" style="--cat-color: #22c55e" data-cat="Actors & Entities"></span> Actors & Entities
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
| **`conditions`** | `public List<MonsterSpawnCondition> conditions` |  |
| **`maxCount`** | `[HorizontalGroup("A", 0, 0, 0, 0)] public int maxCount` |  |
| **`minCount`** | `[HorizontalGroup("A", 0, 0, 0, 0)] public int minCount` |  |
| **`monster`** | `[HideLabel] public AssetRef<Monster> monster` |  |
| **`useAnd`** | `[LabelText("All Conditions Must Match (AND)")] [ToggleLeft] [ShowIf("@conditions != null && conditions.Count > 1", true)] public bool useAnd` |  |

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
