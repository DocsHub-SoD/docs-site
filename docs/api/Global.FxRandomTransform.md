# Class: FxRandomTransform

- **Category:** <span class="cat-dot" style="--cat-color: #64748b" data-cat="Misc & Utility"></span> Misc & Utility
- **Namespace:** `Global`
- **Assembly:** `Dew.Core.dll`

```csharp
public class FxRandomTransform : MonoBehaviour, IEffectComponent
```

## Fields

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`localPositions`** | `[ShowIf("randomizePosition", true)] public Vector3[] localPositions` |  |
| **`localRotations`** | `[ShowIf("randomizeRotation", true)] public Vector3[] localRotations` |  |
| **`localScales`** | `[ShowIf("randomizeScale", true)] public Vector3[] localScales` |  |
| **`randomizePosition`** | `public bool randomizePosition` |  |
| **`randomizeRotation`** | `public bool randomizeRotation` |  |
| **`randomizeScale`** | `public bool randomizeScale` |  |

## Properties

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`isPlaying`** | `public bool isPlaying { get; }` |  |

## Methods

### `Play()`

```csharp
public void Play()
```

### `Stop()`

```csharp
public void Stop()
```
