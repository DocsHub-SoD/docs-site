# Class: DewMath

- **Namespace:** `Global`
- **Assembly:** `Dew.Core.dll`

```csharp
public static class DewMath
```

## Methods

### `Lerp(Vector2, float)`

```csharp
public static float Lerp(this Vector2 vec, float t)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `vec` | `UnityEngine.Vector2` |  |
| `t` | `float` |  |

**Returns:** `float`

### `MultiplyPercentageBonuses(float, float)`

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

### `RandomRange(Vector2)`

```csharp
public static float RandomRange(this Vector2 vec)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `vec` | `UnityEngine.Vector2` |  |

**Returns:** `float`

### `RandomRoundToInt(float, DewRandom)`

```csharp
public static int RandomRoundToInt(float value, DewRandom random = null)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `value` | `float` |  |
| `random` | [DewRandom](/api/Global.DewRandom) |  |

**Returns:** `int`
