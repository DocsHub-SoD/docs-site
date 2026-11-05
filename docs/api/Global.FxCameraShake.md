# Class: FxCameraShake

- **Namespace:** `Global`
- **Assembly:** `Dew.Core.dll`

```csharp
public class FxCameraShake : MonoBehaviour, IEffectComponent, IEffectWithOwnerContext
```

## Fields

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

## Properties

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`isPlaying`** | `public bool isPlaying { get; }` |  |

## Methods

### `Play()`

```csharp
public void Play()
```

### `SetOwnerContext(EffectOwnerContext)`

```csharp
public void SetOwnerContext(EffectOwnerContext context)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `context` | [EffectOwnerContext](/api/Global.EffectOwnerContext) |  |

### `Stop()`

```csharp
public void Stop()
```
