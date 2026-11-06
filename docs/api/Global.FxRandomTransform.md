# Class: FxRandomTransform

- **Category:** <span class="cat-dot" style="--cat-color: #64748b" data-cat="Misc & Utility"></span> Misc & Utility
- **Namespace:** `Global`
- **Assembly:** `Dew.Core.dll`

```csharp
public class FxRandomTransform : MonoBehaviour, IEffectComponent
```

## Fields (6)

::: details Click to expand Fields (6)

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`localPositions`** | `[ShowIf("randomizePosition", true)] public Vector3[] localPositions` |  |
| **`localRotations`** | `[ShowIf("randomizeRotation", true)] public Vector3[] localRotations` |  |
| **`localScales`** | `[ShowIf("randomizeScale", true)] public Vector3[] localScales` |  |
| **`randomizePosition`** | `public bool randomizePosition` |  |
| **`randomizeRotation`** | `public bool randomizeRotation` |  |
| **`randomizeScale`** | `public bool randomizeScale` |  |

:::

## Properties (1)

::: details Click to expand Properties (1)

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`isPlaying`** | `public bool isPlaying { get; }` |  |

:::

## Methods (2)

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
