# Class: DewMusicItem

- **Category:** <span class="cat-dot" style="--cat-color: #eab308" data-cat="Items & Economy"></span> Items & Economy
- **Namespace:** `Global`
- **Assembly:** `Dew.Core.dll`

```csharp
[DewResourceLink(ResourceLinkBy.Guid)]
[CreateAssetMenu(fileName = "mus", menuName = "Dew Music Item")]
public class DewMusicItem : ScriptableObject, ILinkedByGuid
```

## Fields (6)

::: details Click to expand Fields (6)

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`clip`** | `public AudioClip clip` |  |
| **`delay`** | `public float delay` |  |
| **`fadeInTime`** | `public float fadeInTime` |  |
| **`pitch`** | `public float pitch` |  |
| **`startTime`** | `public float startTime` |  |
| **`volumeMultiplier`** | `public float volumeMultiplier` |  |

:::

## Properties (1)

::: details Click to expand Properties (1)

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`resourceId`** | `public string resourceId { get; set; }` |  |

:::

## Methods (1)

::: details `Play()`

```csharp
[Button]
public void Play()
```

:::
