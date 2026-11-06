# Class: ArcTelegraphController

- **Category:** <span class="cat-dot" style="--cat-color: #a855f7" data-cat="Buffs & Statuses"></span> Buffs & Statuses
- **Namespace:** `Global`
- **Assembly:** `Dew.Core.dll`

```csharp
public class ArcTelegraphController : MonoBehaviour, IEffectComponent, IEffectWithSpeed
```

## Fields (8)

::: details Click to expand Fields (8)

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`arcAngle`** | `public float arcAngle` |  |
| **`duration`** | `public float duration` |  |
| **`fillArea`** | `[FoldoutGroup("References", false, 0)] public MeshRenderer fillArea` |  |
| **`fillBorder`** | `[FoldoutGroup("References", false, 0)] public MeshRenderer fillBorder` |  |
| **`innerRadius`** | `public float innerRadius` |  |
| **`maxBorder`** | `[FoldoutGroup("References", false, 0)] public MeshRenderer maxBorder` |  |
| **`outerRadius`** | `public float outerRadius` |  |
| **`whiteBorder`** | `[FoldoutGroup("References", false, 0)] public MeshRenderer whiteBorder` |  |

:::

## Properties (2)

::: details Click to expand Properties (2)

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`isPlaying`** | `public bool isPlaying { get; }` |  |
| **`value`** | `public float value { get; set; }` |  |

:::

## Methods (3)

::: details `ApplySpeedMultiplier(float)`

```csharp
public void ApplySpeedMultiplier(float speed)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `speed` | `float` |  |

:::

::: details `Play()`

```csharp
public void Play()
```

:::

::: details `Stop()`

```csharp
public void Stop()
```

:::
