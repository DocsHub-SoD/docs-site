# Class: ColorSmoothDamp

- **Namespace:** `Global`
- **Assembly:** `Dew.Core.dll`

```csharp
public static class ColorSmoothDamp
```

## Methods

### `SmoothDamp(Color, Color, ref Vector4, float, float, float)`

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

### `SmoothDamp(Color, Color, ref Vector4, float, float)`

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

### `SmoothDamp(Color, Color, ref Vector4, float)`

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
