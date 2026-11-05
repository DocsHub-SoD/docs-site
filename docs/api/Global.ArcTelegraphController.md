# Class: ArcTelegraphController

- **Namespace:** `Global`
- **Assembly:** `Dew.Core.dll`

```csharp
public class ArcTelegraphController : MonoBehaviour, IEffectComponent, IEffectWithSpeed
```

## Fields

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`arcAngle`** | `public float arcAngle` |  |
| **`duration`** | `public float duration` |  |
| **`fillArea`** | `[FoldoutGroup("References", false, 0)]
public MeshRenderer fillArea` |  |
| **`fillBorder`** | `[FoldoutGroup("References", false, 0)]
public MeshRenderer fillBorder` |  |
| **`innerRadius`** | `public float innerRadius` |  |
| **`maxBorder`** | `[FoldoutGroup("References", false, 0)]
public MeshRenderer maxBorder` |  |
| **`outerRadius`** | `public float outerRadius` |  |
| **`whiteBorder`** | `[FoldoutGroup("References", false, 0)]
public MeshRenderer whiteBorder` |  |

## Properties

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`isPlaying`** | `public bool isPlaying { get; }` |  |
| **`value`** | `public float value { get; set; }` |  |

## Methods

### `ApplySpeedMultiplier(float)`

```csharp
public void ApplySpeedMultiplier(float speed)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `speed` | `float` |  |

### `Play()`

```csharp
public void Play()
```

### `Stop()`

```csharp
public void Stop()
```
