# Class: DewAudioSourceSetup

- **Namespace:** `Global`
- **Assembly:** `Dew.Core.dll`

```csharp
public class DewAudioSourceSetup : MonoBehaviour
```

## Fields

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`rolloff`** | `public DewAudioRollOffType rolloff` |  |
| **`space`** | `public AudioSpaceType space` |  |
| **`type`** | `[InfoBox("Warning: Dynamic setup type selected. The type requires setup every time it plays, and it is not for the intended use-case of DewAudioSourceSetup component.", InfoMessageType.Warning, "_isDynamic")]
[InfoBox("This component requires AudioSource", InfoMessageType.Error, "_hasNoAudioSource")]
public AudioType type` |  |
