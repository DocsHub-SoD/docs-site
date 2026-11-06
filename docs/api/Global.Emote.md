# Class: Emote

- **Category:** <span class="cat-dot" style="--cat-color: #64748b" data-cat="Misc & Utility"></span> Misc & Utility
- **Namespace:** `Global`
- **Assembly:** `Dew.Core.dll`
- **Attributes:** `[DewResourceLink]`

```csharp
[DewResourceLink(ResourceLinkBy.Name)]
public class Emote : MonoBehaviour
```

## Fields (7)

::: details Click to expand Fields (7)

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`category`** | `public string category` |  |
| **`customDuration`** | `[NonSerialized] public float? customDuration` |  |
| **`DefaultUnlocks`** | `public static readonly string[] DefaultUnlocks` |  |
| **`generatedFromServer`** | `public bool generatedFromServer` |  |
| **`heroType`** | `public string heroType` |  |
| **`posGetter`** | `public Func<Vector3> posGetter` |  |
| **`price`** | `public int price` |  |

:::

## Methods (2)

::: details `SetupPreview()`

```csharp
public void SetupPreview()
```

:::

::: details `SetupStationary()`

```csharp
public void SetupStationary()
```

:::


## Architecture & Relationships

::: details Click to expand Architecture & Relationships

### Used By (5)

*Classes and systems that invoke, reference, or depend on `Emote`:*

`UI_EmoteList_PreviewWindow` · `UI_InGame_PartyDisplay_Item` · [UI_StationaryEmote](/api/Global.UI_StationaryEmote) · `UI_TravelerStoryDetailContainer` · `UI_TravelerStory_Details_Emote`

### Dependencies (4)

*Types and components that `Emote` references or depends upon:*

[Dew](/api/Global.Dew) · [DewEffect](/api/Global.DewEffect) · `ICosmetic` · `TransformDeepChildExtension`

### Related Enums (1)

*Enumerations referenced in fields, properties, or method signatures:*

[`CosmeticPurchasePrerequisite`](/enums#cosmeticpurchaseprerequisite)

:::
