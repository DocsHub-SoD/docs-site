# Class: BoxTelegraphController

- **Category:** <span class="cat-dot" style="--cat-color: #a855f7" data-cat="Buffs & Statuses"></span> Buffs & Statuses
- **Namespace:** `Global`
- **Assembly:** `Dew.Core.dll`

```csharp
public class BoxTelegraphController : MonoBehaviour, IEffectComponent, IEffectWithSpeed
```

## Fields

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`animateX`** | `public BoxTelegraphAnimType animateX` |  |
| **`animateXEase`** | `[HideLabel] [ShowIf("@animateX != BoxTelegraphAnimType.None", true)] public DewEase animateXEase` |  |
| **`animateY`** | `public BoxTelegraphAnimType animateY` |  |
| **`animateYEase`** | `[HideLabel] [ShowIf("@animateY != BoxTelegraphAnimType.None", true)] public DewEase animateYEase` |  |
| **`duration`** | `public float duration` |  |
| **`height`** | `public float height` |  |
| **`inners`** | `[FoldoutGroup("References", 0)] public SpriteRenderer[] inners` |  |
| **`outers`** | `[FoldoutGroup("References", 0)] public SpriteRenderer[] outers` |  |
| **`reds`** | `[FoldoutGroup("References", 0)] public SpriteRenderer[] reds` |  |
| **`whites`** | `[FoldoutGroup("References", 0)] public SpriteRenderer[] whites` |  |
| **`width`** | `public float width` |  |

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
