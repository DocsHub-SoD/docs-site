# Class: DewMusicItem

- **Namespace:** `Global`
- **Assembly:** `Dew.Core.dll`

```csharp
[DewResourceLink(ResourceLinkBy.Guid)]
[CreateAssetMenu(fileName = "mus", menuName = "Dew Music Item")]
public class DewMusicItem : ScriptableObject, ILinkedByGuid
```

## Fields

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`clip`** | `public AudioClip clip` |  |
| **`delay`** | `public float delay` |  |
| **`fadeInTime`** | `public float fadeInTime` |  |
| **`pitch`** | `public float pitch` |  |
| **`startTime`** | `public float startTime` |  |
| **`volumeMultiplier`** | `public float volumeMultiplier` |  |

## Properties

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`resourceId`** | `public string resourceId { get; set; }` |  |

## Methods

### `Play()`

```csharp
[Button]
public void Play()
```
