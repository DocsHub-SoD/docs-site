# Struct: FxMaterialProperty.PropertyEntry

- **Category:** <span class="cat-dot" style="--cat-color: #64748b" data-cat="Misc & Utility"></span> Misc & Utility
- **Namespace:** `Global`
- **Assembly:** `Dew.Core.dll`

```csharp
[Serializable]
public struct FxMaterialProperty.PropertyEntry
```

## Fields (7)

::: details Click to expand Fields (7)

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`endColor`** | `[ColorUsage(true, true)] [ShowIf("@type == FxMaterialProperty.PropertyType.Color", true)] public Color endColor` |  |
| **`property`** | `public string property` |  |
| **`startColor`** | `[ColorUsage(true, true)] [ShowIf("@type == FxMaterialProperty.PropertyType.Color", true)] public Color startColor` |  |
| **`target`** | `[LabelText("Renderer")] [HideIf("@targetUi != null", true)] public Renderer target` |  |
| **`targetUi`** | `[LabelText("UI Graphic")] [HideIf("@target != null", true)] public Graphic targetUi` |  |
| **`type`** | `public FxMaterialProperty.PropertyType type` |  |
| **`valueCurve`** | `public AnimationCurve valueCurve` |  |

:::


## Architecture & Relationships

::: details Click to expand Architecture & Relationships

### Used By (0)

*No incoming dependencies recorded.*

### Dependencies (0)

*No outgoing class dependencies recorded.*

:::
