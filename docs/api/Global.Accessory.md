# Class: Accessory

- **Namespace:** `Global`
- **Assembly:** `Dew.Core.dll`

```csharp
[DewResourceLink(ResourceLinkBy.Name)]
public class Accessory : MonoBehaviour
```

## Fields

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`category`** | `public string category` |  |
| **`customOffsets`** | `public List&lt;Accessory.AttachOffset&gt; customOffsets` |  |
| **`generatedFromServer`** | `public bool generatedFromServer` |  |
| **`previewCustomCenter`** | `[LabelText("Custom Center")]
public Transform previewCustomCenter` |  |
| **`previewImage`** | `[Space(30)]
[PreviewField(60)]
[LabelText("Thumbnail")]
public Sprite previewImage` |  |
| **`previewOffset`** | `[LabelText("Normalized Offset")]
[ReadOnly]
public Vector2 previewOffset` |  |
| **`previewPadding`** | `[Range(-0.25, 0.25)]
[LabelText("Padding")]
public float previewPadding` |  |
| **`type`** | `public AccType type` |  |

## Methods

### `Setup(Transform, string)`

```csharp
public void Setup(Transform target, string entityOrSkinName)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `target` | `UnityEngine.Transform` |  |
| `entityOrSkinName` | `string` |  |
