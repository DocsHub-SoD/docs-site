# Class: DewMusicItem

- **Category:** <span class="cat-dot" style="--cat-color: #eab308" data-cat="Items & Economy"></span> Items & Economy
- **Namespace:** `Global`
- **Assembly:** `Dew.Core.dll`
- **Attributes:** `[DewResourceLink] [CreateAssetMenu]`

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


## Architecture & Relationships

::: details Click to expand Architecture & Relationships

### Used By (5)

*Classes and systems that invoke, reference, or depend on `DewMusicItem`:*

[FxChangeMusic](/api/Global.FxChangeMusic) · [MusicManager](/api/Global.MusicManager) · `PlayTutorial_Tutorial_Hunt` · [Room](/api/Global.Room) · `UI_CreditsView`

### Dependencies (3)

*Types and components that `DewMusicItem` references or depends upon:*

[ILinkedByGuid](/api/Global.ILinkedByGuid) · [ManagerBase`1](/api/Global.ManagerBase`1) · [MusicManager](/api/Global.MusicManager)

:::
