# Class: ColorSmoothDamp

- **Category:** <span class="cat-dot" style="--cat-color: #64748b" data-cat="Misc & Utility"></span> Misc & Utility
- **Namespace:** `Global`
- **Assembly:** `Dew.Core.dll`

```csharp
public static class ColorSmoothDamp
```

## Methods (3)

::: details `SmoothDamp(Color, Color, ref Vector4, float, float, float)`

```csharp
public static Color SmoothDamp(Color current, Color target, ref Vector4 currentVelocity, float smoothTime, float maxSpeed, float deltaTime)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `current` | `UnityEngine.Color` |  |
| `target` | `UnityEngine.Color` |  |
| `currentVelocity` | `UnityEngine.Vector4` |  |
| `smoothTime` | `float` |  |
| `maxSpeed` | `float` |  |
| `deltaTime` | `float` |  |

**Returns:** `UnityEngine.Color`

:::

::: details `SmoothDamp(Color, Color, ref Vector4, float, float)`

```csharp
public static Color SmoothDamp(Color current, Color target, ref Vector4 currentVelocity, float smoothTime, float maxSpeed)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `current` | `UnityEngine.Color` |  |
| `target` | `UnityEngine.Color` |  |
| `currentVelocity` | `UnityEngine.Vector4` |  |
| `smoothTime` | `float` |  |
| `maxSpeed` | `float` |  |

**Returns:** `UnityEngine.Color`

:::

::: details `SmoothDamp(Color, Color, ref Vector4, float)`

```csharp
public static Color SmoothDamp(Color current, Color target, ref Vector4 currentVelocity, float smoothTime)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `current` | `UnityEngine.Color` |  |
| `target` | `UnityEngine.Color` |  |
| `currentVelocity` | `UnityEngine.Vector4` |  |
| `smoothTime` | `float` |  |

**Returns:** `UnityEngine.Color`

:::


## Architecture & Relationships

::: details Click to expand Architecture & Relationships

### Used By (1)

*Classes and systems that invoke, reference, or depend on `ColorSmoothDamp`:*

`UI_AnimatedValueText`

### Dependencies (0)

*No outgoing class dependencies recorded.*

:::
