# Class: Nametag

- **Category:** <span class="cat-dot" style="--cat-color: #64748b" data-cat="Misc & Utility"></span> Misc & Utility
- **Namespace:** `Global`
- **Assembly:** `Dew.Core.dll`
- **Attributes:** `[DewResourceLink] [RequireComponent]`

```csharp
[DewResourceLink(ResourceLinkBy.Name)]
[RequireComponent(typeof(LayoutElement))]
public class Nametag : MonoBehaviour
```

## Fields (10)

::: details Click to expand Fields (10)

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`category`** | `public string category` |  |
| **`condition`** | `[HideIf("generatedFromServer", true)] public CosmeticPurchasePrerequisite condition` |  |
| **`conditionType`** | `[ShowIf("@condition == CosmeticPurchasePrerequisite.NightmareKillCount \|\| condition == CosmeticPurchasePrerequisite.ReachZone", true)] [LabelText("Type")] public string conditionType` |  |
| **`conditionValue`** | `[ShowIf("@condition == CosmeticPurchasePrerequisite.NightmareKillCount \|\| condition == CosmeticPurchasePrerequisite.ReachZone \|\| condition == CosmeticPurchasePrerequisite.NightmarePureWhiteDream \|\| condition == CosmeticPurchasePrerequisite.LimboMaxDepth", true)] [LabelText("Required Amount")] public int conditionValue` |  |
| **`customOrder`** | `public float customOrder` |  |
| **`generatedFromServer`** | `public bool generatedFromServer` |  |
| **`iconNormalizedOffsetY`** | `[Space] [Space(20)] public float iconNormalizedOffsetY` |  |
| **`iconWidthOffset`** | `public float iconWidthOffset` |  |
| **`nametagHorizontalMargin`** | `public Vector2 nametagHorizontalMargin` |  |
| **`price`** | `public int price` |  |

:::

## Methods (2)

::: details `CheckPrerequisites(out bool, out int, out int, out string)`

```csharp
public void CheckPrerequisites(out bool canPurchase, out int currentProgress, out int maxProgress, out string conditionText)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `canPurchase` | `bool` |  |
| `currentProgress` | `int` |  |
| `maxProgress` | `int` |  |
| `conditionText` | `string` |  |

:::

::: details `Setup(RectTransform, bool)`

```csharp
public void Setup(RectTransform target, bool isIcon)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `target` | `UnityEngine.RectTransform` |  |
| `isIcon` | `bool` |  |

:::


## Architecture & Relationships

::: details Click to expand Architecture & Relationships

### Used By (4)

*Classes and systems that invoke, reference, or depend on `Nametag`:*

`UI_ItemIcon` · `UI_Lobby_PlayerNametag` · `UI_NametagList_Item` · `UI_NametagList_PreviewWindow`

### Dependencies (4)

*Types and components that `Nametag` references or depends upon:*

[Dew](/api/Global.Dew) · `ICosmetic` · `RectTransformGetWorldRectExtension` · `Vector3FlattenExtension`

### Related Enums (1)

*Enumerations referenced in fields, properties, or method signatures:*

<a href="/enums#cosmeticpurchaseprerequisite" class="enum-link" data-tooltip="None=0 · NightmareKillCount=1 · ReachZone=2 · HeroMastery=3 · NightmareWin=4 (+2 more)">CosmeticPurchasePrerequisite</a>

:::
