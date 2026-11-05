# Class: DewAudioSource

- **Namespace:** `Global`
- **Assembly:** `Dew.Core.dll`

```csharp
public class DewAudioSource : MonoBehaviour, IEffectComponent, IEffectWithOwnerContext
```

## Fields

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`clip`** | `[ShowIf("@rawClip == null \|\| clip != null", true)]
public DewAudioClip clip` |  |
| **`delay`** | `public float delay` |  |
| **`fadeInTime`** | `public float fadeInTime` |  |
| **`fadeOutTime`** | `public float fadeOutTime` |  |
| **`forceHighestPriority`** | `[ToggleLeft]
public bool forceHighestPriority` |  |
| **`ignoreTimescale`** | `[ToggleLeft]
public bool ignoreTimescale` |  |
| **`isLoop`** | `[ToggleLeft]
public bool isLoop` |  |
| **`PitchChangeByTimescaleMultiplier`** | `public const float PitchChangeByTimescaleMultiplier = 0.75` |  |
| **`pitchMultiplier`** | `public float pitchMultiplier` |  |
| **`playOnEnable`** | `[Space(20)]
[ToggleLeft]
public bool playOnEnable` |  |
| **`rawClip`** | `[ShowIf("@clip == null", true)]
public AudioClip rawClip` |  |
| **`rolloff`** | `[ShowIf("@space != AudioSpaceType.Global", true)]
public DewAudioRollOffType rolloff` |  |
| **`space`** | `public AudioSpaceType space` |  |
| **`stopWhenEffectStop`** | `[HideIf("isLoop", true)]
[ToggleLeft]
public bool stopWhenEffectStop` |  |
| **`type`** | `public AudioType type` |  |
| **`volumeMultiplier`** | `[Space(20)]
public float volumeMultiplier` |  |

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
