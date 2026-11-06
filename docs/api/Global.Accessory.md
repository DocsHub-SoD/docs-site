# Class: Accessory

- **Category:** <span class="cat-dot" style="--cat-color: #eab308" data-cat="Items & Economy"></span> Items & Economy
- **Namespace:** `Global`
- **Assembly:** `Dew.Core.dll`

```csharp
[DewResourceLink(ResourceLinkBy.Name)]
public class Accessory : MonoBehaviour
```

## Fields (8)

::: details Click to expand Fields (8)

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`category`** | `public string category` |  |
| **`customOffsets`** | `public List<Accessory.AttachOffset> customOffsets` |  |
| **`generatedFromServer`** | `public bool generatedFromServer` |  |
| **`previewCustomCenter`** | `[LabelText("Custom Center")] public Transform previewCustomCenter` |  |
| **`previewImage`** | `[Space(30)] [PreviewField(60)] [LabelText("Thumbnail")] public Sprite previewImage` |  |
| **`previewOffset`** | `[LabelText("Normalized Offset")] [ReadOnly] public Vector2 previewOffset` |  |
| **`previewPadding`** | `[Range(-0.25, 0.25)] [LabelText("Padding")] public float previewPadding` |  |
| **`type`** | `public AccType type` |  |

:::

## Methods (1)

::: details `Setup(Transform, string)`

```csharp
public void Setup(Transform target, string entityOrSkinName)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `target` | `UnityEngine.Transform` |  |
| `entityOrSkinName` | `string` |  |

:::
