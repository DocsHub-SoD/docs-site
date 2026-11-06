# Class: Nametag

- **Category:** <span class="cat-dot" style="--cat-color: #64748b" data-cat="Misc & Utility"></span> Misc & Utility
- **Namespace:** `Global`
- **Assembly:** `Dew.Core.dll`

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
| **`iconNormalizedOffsetY`** | `[Space(20)] public float iconNormalizedOffsetY` |  |
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
