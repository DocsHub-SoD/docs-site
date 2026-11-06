# Class: DewAudioClip

- **Category:** <span class="cat-dot" style="--cat-color: #3b82f6" data-cat="Managers & Systems"></span> Managers & Systems
- **Namespace:** `Global`
- **Assembly:** `Dew.Core.dll`

```csharp
[HideMonoScript]
[DewResourceLink(ResourceLinkBy.Guid)]
[CreateAssetMenu(fileName = "New Dew Audio Clip", menuName = "Dew Audio Clip")]
public class DewAudioClip : ScriptableObject, ILinkedByGuid
```

## Fields (7)

::: details Click to expand Fields (7)

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`clips`** | `public AudioClip[] clips` |  |
| **`maxPitch`** | `[ShowIf("randomizePitch", true)] public float maxPitch` |  |
| **`minPitch`** | `[ShowIf("randomizePitch", true)] public float minPitch` |  |
| **`pitch`** | `[ShowIf("@!randomizePitch", true)] public float pitch` |  |
| **`randomizePitch`** | `public bool randomizePitch` |  |
| **`timeOffset`** | `public float timeOffset` |  |
| **`volume`** | `public float volume` |  |

:::

## Properties (1)

::: details Click to expand Properties (1)

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`resourceId`** | `public string resourceId { get; set; }` |  |

:::

## Methods (2)

::: details `GetAudioClip()`

Get a random audio clip from the pre-configured array of clips.

```csharp
public AudioClip GetAudioClip()
```

**Returns:** `UnityEngine.AudioClip`

:::

::: details `GetPitch()`

Get an appropriate pitch value depending on how its configured.

```csharp
public float GetPitch()
```

**Returns:** `float`

:::
