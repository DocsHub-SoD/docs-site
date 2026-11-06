# Class: AudioManager

- **Category:** <span class="cat-dot" style="--cat-color: #3b82f6" data-cat="Managers & Systems"></span> Managers & Systems
- **Namespace:** `Global`
- **Assembly:** `Dew.Core.dll`
- **Inheritance / Derived:** [LogicBehaviour](/api/Global.LogicBehaviour) → `ManagerBase` → [AudioManager](/api/Global.AudioManager)

```csharp
public class AudioManager : ManagerBase<AudioManager>, ILogicUpdate
```

## Fields (12)

::: details Click to expand Fields (12)

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`defaultCurve`** | `[Title("Volume Roll-offs", null, TitleAlignments.Left, true, true)] public AnimationCurve defaultCurve` |  |
| **`gameBoss`** | `public AudioMixerGroup gameBoss` |  |
| **`gameEnvironment`** | `public AudioMixerGroup gameEnvironment` |  |
| **`gameOtherPlayers`** | `public AudioMixerGroup gameOtherPlayers` |  |
| **`gameOthers`** | `public AudioMixerGroup gameOthers` |  |
| **`gameSelf`** | `public AudioMixerGroup gameSelf` |  |
| **`loudCurve`** | `public AnimationCurve loudCurve` |  |
| **`master`** | `public AudioMixerGroup master` |  |
| **`mixer`** | `public AudioMixer mixer` |  |
| **`music`** | `public AudioMixerGroup music` |  |
| **`sfx`** | `public AudioMixerGroup sfx` |  |
| **`ui`** | `public AudioMixerGroup ui` |  |

:::

## Properties (1)

::: details Click to expand Properties (1)

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`shouldRegisterUpdates`** | `public override bool shouldRegisterUpdates { get; }` |  |

:::

## Methods (7)

::: details `FadeInMasterVolume()`

```csharp
public void FadeInMasterVolume()
```

:::

::: details `FadeOutMasterVolume()`

```csharp
public void FadeOutMasterVolume()
```

:::

::: details `NeedsSetupEverytime(AudioType)`

Does the type needs to be setup everytime before being played?

```csharp
public static bool NeedsSetupEverytime(AudioType type)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `type` | [`AudioType`](/api/Global.AudioType) |  |

**Returns:** `bool`

:::

::: details `PlayUISound(AudioClip)`

```csharp
public void PlayUISound(AudioClip clip)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `clip` | `UnityEngine.AudioClip` |  |

:::

::: details `SetMasterVolumeMultiplier(float)`

```csharp
public void SetMasterVolumeMultiplier(float multiplier)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `multiplier` | `float` |  |

:::

::: details `SetupAudioSource(AudioSource, AudioType, AudioSpaceType, DewAudioRollOffType, bool)`

```csharp
public void SetupAudioSource(AudioSource source, AudioType type, AudioSpaceType space, DewAudioRollOffType rolloff, bool forceCriticalPriority)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `source` | `UnityEngine.AudioSource` |  |
| `type` | [`AudioType`](/api/Global.AudioType) |  |
| `space` | [`AudioSpaceType`](/api/Global.AudioSpaceType) |  |
| `rolloff` | [`DewAudioRollOffType`](/api/Global.DewAudioRollOffType) |  |
| `forceCriticalPriority` | `bool` |  |

:::

::: details `UpdateMixerAttenuations()`

```csharp
public void UpdateMixerAttenuations()
```

:::
