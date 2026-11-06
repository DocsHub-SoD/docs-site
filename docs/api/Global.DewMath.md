# Class: DewMath

- **Category:** <span class="cat-dot" style="--cat-color: #f97316" data-cat="Data & Core Math"></span> Data & Core Math
- **Namespace:** `Global`
- **Assembly:** `Dew.Core.dll`

```csharp
public static class DewMath
```

## Methods (4)

::: details `Lerp(Vector2, float)`

```csharp
public static float Lerp(this Vector2 vec, float t)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `vec` | `UnityEngine.Vector2` |  |
| `t` | `float` |  |

**Returns:** `float`

:::

::: details `MultiplyPercentageBonuses(float, float)`

Multiply percentage bonuses.This(50, 50) = 125. (1.5 * 1.5 = 2.25)This(100, 100) = 300. (2 * 2 = 4)This(-50, 50) = -25. (0.5 * 1.5 = 0.75)

```csharp
public static float MultiplyPercentageBonuses(float a, float b)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `a` | `float` |  |
| `b` | `float` |  |

**Returns:** `float`

:::

::: details `RandomRange(Vector2)`

```csharp
public static float RandomRange(this Vector2 vec)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `vec` | `UnityEngine.Vector2` |  |

**Returns:** `float`

:::

::: details `RandomRoundToInt(float, DewRandom)`

```csharp
public static int RandomRoundToInt(float value, DewRandom random = null)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `value` | `float` |  |
| `random` | [`DewRandom`](/api/Global.DewRandom) |  |

**Returns:** `int`

:::
