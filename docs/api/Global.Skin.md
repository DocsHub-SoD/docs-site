# Class: Skin

- **Category:** <span class="cat-dot" style="--cat-color: #64748b" data-cat="Misc & Utility"></span> Misc & Utility
- **Namespace:** `Global`
- **Assembly:** `Dew.Core.dll`

```csharp
[DewResourceLink(ResourceLinkBy.Name)]
public class Skin : MonoBehaviour
```

## Fields

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

## Properties

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`stardustPrice`** | `public int stardustPrice { get; }` |  |

## Methods

### `GetDefaultSkin(string)`

```csharp
public static string GetDefaultSkin(string heroType)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `heroType` | `string` |  |

**Returns:** `string`

### `IsValidFor(string)`

```csharp
public bool IsValidFor(string heroType)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `heroType` | `string` |  |

**Returns:** `bool`
