# Class: UI_StationaryEmote

- **Category:** <span class="cat-dot" style="--cat-color: #ec4899" data-cat="User Interface"></span> User Interface
- **Namespace:** `Global`
- **Assembly:** `Dew.Core.dll`
- **Inheritance / Derived:** [UI_EmoteWheel_Item](/api/Global.UI_EmoteWheel_Item)

```csharp
public class UI_StationaryEmote : MonoBehaviour
```

## Fields

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`currentEmoteInstance`** | `[NonSerialized] public Emote currentEmoteInstance` |  |
| **`currentEmoteName`** | `[NonSerialized] public string currentEmoteName` |  |
| **`currentEmotePrefab`** | `[NonSerialized] public AssetRef<Emote> currentEmotePrefab` |  |
| **`customParent`** | `public RectTransform customParent` |  |

## Methods

### `Setup(string)`

```csharp
public virtual void Setup(string emoteName)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `emoteName` | `string` |  |
