# Class: DewAudioClip

- **Namespace:** `Global`
- **Assembly:** `Dew.Core.dll`

```csharp
[HideMonoScript]
[DewResourceLink(ResourceLinkBy.Guid)]
[CreateAssetMenu(fileName = "New Dew Audio Clip", menuName = "Dew Audio Clip")]
public class DewAudioClip : ScriptableObject, ILinkedByGuid
```

## Fields

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`clips`** | `public AudioClip[] clips` |  |
| **`maxPitch`** | `[ShowIf("randomizePitch", true)]
public float maxPitch` |  |
| **`minPitch`** | `[ShowIf("randomizePitch", true)]
public float minPitch` |  |
| **`pitch`** | `[ShowIf("@!randomizePitch", true)]
public float pitch` |  |
| **`randomizePitch`** | `public bool randomizePitch` |  |
| **`timeOffset`** | `public float timeOffset` |  |
| **`volume`** | `public float volume` |  |

## Properties

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`resourceId`** | `public string resourceId { get; set; }` |  |

## Methods

### `GetAudioClip()`

Get a random audio clip from the pre-configured array of clips.

```csharp
public AudioClip GetAudioClip()
```

**Returns:** `UnityEngine.AudioClip`

### `GetPitch()`

Get an appropriate pitch value depending on how its configured.

```csharp
public float GetPitch()
```

**Returns:** `float`
