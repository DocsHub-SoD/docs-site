# Class: Skin

- **Category:** <span class="cat-dot" style="--cat-color: #64748b" data-cat="Misc & Utility"></span> Misc & Utility
- **Namespace:** `Global`
- **Assembly:** `Dew.Core.dll`

```csharp
[DewResourceLink(ResourceLinkBy.Name)]
public class Skin : MonoBehaviour
```

## Fields (8)

::: details Click to expand Fields (8)

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`category`** | `public string category` |  |
| **`generatedFromServer`** | `public bool generatedFromServer` |  |
| **`previewFovOffset`** | `[LabelText("Field Of View Offset")] public float previewFovOffset` |  |
| **`previewImage`** | `[Title("Preview", null, TitleAlignments.Left, true, true)] [PreviewField(60)] public Sprite previewImage` |  |
| **`previewRotationOffset`** | `[LabelText("Rotation Offset")] public Vector3 previewRotationOffset` |  |
| **`rarity`** | `public SkinRarity rarity` |  |
| **`requiredLevel`** | `public int requiredLevel` |  |
| **`skillVisuals`** | `public SkillVisualOverrideItem[] skillVisuals` |  |

:::

## Properties (1)

::: details Click to expand Properties (1)

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`stardustPrice`** | `public int stardustPrice { get; }` |  |

:::

## Methods (2)

::: details `GetDefaultSkin(string)`

```csharp
public static string GetDefaultSkin(string heroType)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `heroType` | `string` |  |

**Returns:** `string`

:::

::: details `IsValidFor(string)`

```csharp
public bool IsValidFor(string heroType)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `heroType` | `string` |  |

**Returns:** `bool`

:::
