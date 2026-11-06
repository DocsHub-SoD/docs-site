# Class: MonsterSpawnCondition

- **Category:** <span class="cat-dot" style="--cat-color: #22c55e" data-cat="Actors & Entities"></span> Actors & Entities
- **Namespace:** `Global`
- **Assembly:** `Dew.Core.dll`

```csharp
[Serializable]
public class MonsterSpawnCondition
```

## Fields (3)

::: details Click to expand Fields (3)

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`conditionValueMax`** | `[LabelText("Max")] [HorizontalGroup("C", 0, 0, 0, 0)] public float conditionValueMax` |  |
| **`conditionValueMin`** | `[LabelText("Min")] [HorizontalGroup("C", 0, 0, 0, 0)] public float conditionValueMin` |  |
| **`type`** | `[HideLabel] public MonsterSpawnConditionType type` |  |

:::

## Properties (2)

::: details Click to expand Properties (2)

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`conditionValueMaxInt`** | `public int conditionValueMaxInt { get; }` |  |
| **`conditionValueMinInt`** | `public int conditionValueMinInt { get; }` |  |

:::

## Methods (1)

::: details `EvaluateCondition()`

```csharp
public bool EvaluateCondition()
```

**Returns:** `bool`

:::
