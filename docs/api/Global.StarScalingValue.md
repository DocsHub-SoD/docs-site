# Struct: StarScalingValue

- **Category:** <span class="cat-dot" style="--cat-color: #f97316" data-cat="Data & Core Math"></span> Data & Core Math
- **Namespace:** `Global`
- **Assembly:** `Dew.Core.dll`

```csharp
[Serializable]
[InlineProperty]
[LabelWidth(100)]
public struct StarScalingValue
```

## Fields (15)

::: details Click to expand Fields (15)

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`clampMax`** | `[ShowIf("@isClamped", true)] [HideLabel] [HorizontalGroup("C", 0, 0, 0, 0)] public float clampMax` |  |
| **`clampMin`** | `[ShowIf("@isClamped", true)] [HideLabel] [SuffixLabel("-", false)] [HorizontalGroup("C", 0, 0, 0, 0)] public float clampMin` |  |
| **`isClamped`** | `[ToggleLeft] [HorizontalGroup("C", 0, 0, 0, 0)] [LabelText("Clamp")] public bool isClamped` |  |
| **`isInteger`** | `[ToggleLeft] [HorizontalGroup("B", 40, 0, 0, 0)] [LabelText("Int")] public bool isInteger` |  |
| **`isParentStarEffect`** | `[HideInInspector] public bool isParentStarEffect` |  |
| **`levels`** | `[HideInInspector] public int levels` |  |
| **`strengthScaling`** | `[HideLabel] [HorizontalGroup("B", 0, 0, 0, 0)] public StarScalingValue.StrengthScalingType strengthScaling` |  |
| **`v0`** | `[HorizontalGroup("A", 0, 0, 0, 0)] [HideLabel] public float v0` |  |
| **`v1`** | `[HorizontalGroup("A", 0, 0, 0, 0)] [HideLabel] [ShowIf("@!isParentStarEffect \|\| levels >= 2", true)] public float v1` |  |
| **`v2`** | `[HorizontalGroup("A", 0, 0, 0, 0)] [HideLabel] [ShowIf("@!isParentStarEffect \|\| levels >= 3", true)] public float v2` |  |
| **`v3`** | `[HorizontalGroup("A", 0, 0, 0, 0)] [HideLabel] [ShowIf("@!isParentStarEffect \|\| levels >= 4", true)] public float v3` |  |
| **`v4`** | `[HorizontalGroup("A", 0, 0, 0, 0)] [HideLabel] [ShowIf("@!isParentStarEffect \|\| levels >= 5", true)] public float v4` |  |
| **`v5`** | `[HorizontalGroup("A", 0, 0, 0, 0)] [HideLabel] [ShowIf("@!isParentStarEffect \|\| levels >= 6", true)] public float v5` |  |
| **`v6`** | `[HorizontalGroup("A", 0, 0, 0, 0)] [HideLabel] [ShowIf("@!isParentStarEffect \|\| levels >= 7", true)] public float v6` |  |
| **`v7`** | `[HorizontalGroup("A", 0, 0, 0, 0)] [HideLabel] [ShowIf("@!isParentStarEffect \|\| levels >= 8", true)] public float v7` |  |

:::

## Methods (3)

::: details `Get(int)`

```csharp
public float Get(int index)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `index` | `int` |  |

**Returns:** `float`

:::

::: details `GetValue(int, float)`

```csharp
public float GetValue(int level, float strength)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `level` | `int` |  |
| `strength` | `float` |  |

**Returns:** `float`

:::

::: details `Set(int, float)`

```csharp
public void Set(int index, float value)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `index` | `int` |  |
| `value` | `float` |  |

:::
