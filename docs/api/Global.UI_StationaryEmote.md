# Class: UI_StationaryEmote

- **Category:** <span class="cat-dot" style="--cat-color: #ec4899" data-cat="User Interface"></span> User Interface
- **Namespace:** `Global`
- **Assembly:** `Dew.Core.dll`
- **Inheritance / Derived:** [UI_EmoteWheel_Item](/api/Global.UI_EmoteWheel_Item)

```csharp
public class UI_StationaryEmote : MonoBehaviour
```

## Fields (4)

::: details Click to expand Fields (4)

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`currentEmoteInstance`** | `[NonSerialized] public Emote currentEmoteInstance` |  |
| **`currentEmoteName`** | `[NonSerialized] public string currentEmoteName` |  |
| **`currentEmotePrefab`** | `[NonSerialized] public AssetRef<Emote> currentEmotePrefab` |  |
| **`customParent`** | `public RectTransform customParent` |  |

:::

## Methods (1)

::: details `Setup(string)`

```csharp
public virtual void Setup(string emoteName)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `emoteName` | `string` |  |

:::


## Architecture & Relationships

::: details Click to expand Architecture & Relationships

### Used By (8)

*Classes and systems that invoke, reference, or depend on `UI_StationaryEmote`:*

`UI_EmoteList` · `UI_EmoteList_EditEmote` · `UI_EmoteList_EditEmoteWheel_FloatingEmote` · `UI_EmoteList_EditEmoteWheel_Item` · `UI_EmoteList_Item` · [UI_EmoteWheel](/api/Global.UI_EmoteWheel) · [UI_EmoteWheel_Item](/api/Global.UI_EmoteWheel_Item) · `UI_ItemIcon`

### Dependencies (3)

*Types and components that `UI_StationaryEmote` references or depends upon:*

[AssetRef`1](/api/Global.AssetRef`1) · [DewResources](/api/Global.DewResources) · [Emote](/api/Global.Emote)

:::
