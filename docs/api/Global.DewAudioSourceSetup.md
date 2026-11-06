# Class: DewAudioSourceSetup

- **Category:** <span class="cat-dot" style="--cat-color: #3b82f6" data-cat="Managers & Systems"></span> Managers & Systems
- **Namespace:** `Global`
- **Assembly:** `Dew.Core.dll`

```csharp
public class DewAudioSourceSetup : MonoBehaviour
```

## Fields (3)

::: details Click to expand Fields (3)

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`rolloff`** | `public DewAudioRollOffType rolloff` |  |
| **`space`** | `public AudioSpaceType space` |  |
| **`type`** | `[InfoBox("Warning: Dynamic setup type selected. The type requires setup every time it plays, and it is not for the intended use-case of DewAudioSourceSetup component.", InfoMessageType.Warning, "_isDynamic")] [InfoBox("This component requires AudioSource", InfoMessageType.Error, "_hasNoAudioSource")] public AudioType type` |  |

:::


## Architecture & Relationships

::: details Click to expand Architecture & Relationships

### Used By (0)

*No incoming dependencies recorded.*

### Dependencies (2)

*Types and components that `DewAudioSourceSetup` references or depends upon:*

[AudioManager](/api/Global.AudioManager) · `TransformGetScenePathExtension`

### Related Enums (3)

*Enumerations referenced in fields, properties, or method signatures:*

<a href="/enums#audiospacetype" class="enum-link" data-tooltip="Normal=0 · Global=1">AudioSpaceType</a> · <a href="/enums#audiotype" class="enum-link" data-tooltip="UI=0 · Music=1 · SFX=2 · GameBoss=3 · GameSelf=4 (+3 more)">AudioType</a> · <a href="/enums#dewaudiorollofftype" class="enum-link" data-tooltip="Default=0 · Loud=1 · Unity=2">DewAudioRollOffType</a>

:::
