# Struct: FxMaterialProperty.PropertyEntry

- **Namespace:** `Global`
- **Assembly:** `Dew.Core.dll`

```csharp
[Serializable]
public struct FxMaterialProperty.PropertyEntry
```

## Fields

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`endColor`** | `[ColorUsage(true, true)]
[ShowIf("@type == FxMaterialProperty.PropertyType.Color", true)]
public Color endColor` |  |
| **`property`** | `public string property` |  |
| **`startColor`** | `[ColorUsage(true, true)]
[ShowIf("@type == FxMaterialProperty.PropertyType.Color", true)]
public Color startColor` |  |
| **`target`** | `[LabelText("Renderer")]
[HideIf("@targetUi != null", true)]
public Renderer target` |  |
| **`targetUi`** | `[LabelText("UI Graphic")]
[HideIf("@target != null", true)]
public Graphic targetUi` |  |
| **`type`** | `public FxMaterialProperty.PropertyType type` |  |
| **`valueCurve`** | `public AnimationCurve valueCurve` |  |
