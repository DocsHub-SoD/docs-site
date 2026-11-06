# Class: Skin

- **Category:** <span class="cat-dot" style="--cat-color: #64748b" data-cat="Misc & Utility"></span> Misc & Utility
- **Namespace:** `Global`
- **Assembly:** `Dew.Core.dll`
- **Attributes:** `[DewResourceLink]`

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


## Architecture & Relationships

::: details Click to expand Architecture & Relationships

### Used By (7)

*Classes and systems that invoke, reference, or depend on `Skin`:*

[DewPlayer](/api/Global.DewPlayer) · [DewProfile](/api/Global.DewProfile) · [Hero](/api/Global.Hero) · [PlayLobby_Character](/api/Global.PlayLobby_Character) · [TitleManager](/api/Global.TitleManager) · [Title_LastGameCharacters](/api/Global.Title_LastGameCharacters) · `UI_Lobby_SkinList_Item`

### Dependencies (1)

*Types and components that `Skin` references or depends upon:*

`ICosmetic`

### Related Enums (2)

*Enumerations referenced in fields, properties, or method signatures:*

<a href="/enums#rarity" class="enum-link" data-tooltip="Common=0 · Rare=1 · Epic=2 · Legendary=3 · Character=4 (+2 more)">Rarity</a> · <a href="/enums#skinrarity" class="enum-link" data-tooltip="Default=0 · Rare=1 · Epic=2 · Legendary=3">SkinRarity</a>

:::
