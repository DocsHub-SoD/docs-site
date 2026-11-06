# Class: MonsterSpawnCondition

- **Category:** <span class="cat-dot" style="--cat-color: #22c55e" data-cat="Actors & Entities"></span> Actors & Entities
- **Namespace:** `Global`
- **Assembly:** `Dew.Core.dll`

```csharp
[Serializable]
public class MonsterSpawnCondition
```

## Fields

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`conditionValueMax`** | `[LabelText("Max")] [HorizontalGroup("C", 0, 0, 0, 0)] public float conditionValueMax` |  |
| **`conditionValueMin`** | `[LabelText("Min")] [HorizontalGroup("C", 0, 0, 0, 0)] public float conditionValueMin` |  |
| **`type`** | `[HideLabel] public MonsterSpawnConditionType type` |  |

## Properties

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`conditionValueMaxInt`** | `public int conditionValueMaxInt { get; }` |  |
| **`conditionValueMinInt`** | `public int conditionValueMinInt { get; }` |  |

## Methods

### `EvaluateCondition()`

```csharp
public bool EvaluateCondition()
```

**Returns:** `bool`
