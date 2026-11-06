# Class: FxCameraShake

- **Category:** <span class="cat-dot" style="--cat-color: #3b82f6" data-cat="Managers & Systems"></span> Managers & Systems
- **Namespace:** `Global`
- **Assembly:** `Dew.Core.dll`

```csharp
public class FxCameraShake : MonoBehaviour, IEffectComponent, IEffectWithOwnerContext
```

## Fields (10)

::: details Click to expand Fields (10)

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`amplitude`** | `public float amplitude` |  |
| **`attackTime`** | `public float attackTime` |  |
| **`decayTime`** | `public float decayTime` |  |
| **`delay`** | `public float delay` |  |
| **`frequency`** | `public float frequency` |  |
| **`Global_AmplitudeMultiplier`** | `public const float Global_AmplitudeMultiplier = 1.25` |  |
| **`Global_FrequencyMultiplier`** | `public const float Global_FrequencyMultiplier = 0.9` |  |
| **`Global_TimeMultiplier`** | `public const float Global_TimeMultiplier = 1.25` |  |
| **`signalSource`** | `public SignalSourceAsset signalSource` |  |
| **`sustainTime`** | `public float sustainTime` |  |

:::

## Properties (1)

::: details Click to expand Properties (1)

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`isPlaying`** | `public bool isPlaying { get; }` |  |

:::

## Methods (3)

::: details `Play()`

```csharp
public void Play()
```

:::

::: details `SetOwnerContext(EffectOwnerContext)`

```csharp
public void SetOwnerContext(EffectOwnerContext context)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `context` | [`EffectOwnerContext`](/api/Global.EffectOwnerContext) |  |

:::

::: details `Stop()`

```csharp
public void Stop()
```

:::
