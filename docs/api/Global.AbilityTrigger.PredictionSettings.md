# Struct: AbilityTrigger.PredictionSettings

- **Category:** <span class="cat-dot" style="--cat-color: #ef4444" data-cat="Combat & Abilities"></span> Combat & Abilities
- **Namespace:** `Global`
- **Assembly:** `Dew.Core.dll`

```csharp
[Serializable]
[InlineProperty]
[HideLabel]
public struct AbilityTrigger.PredictionSettings
```

## Fields (8)

::: details Click to expand Fields (8)

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`acceleration`** | `[ShowIf("_shouldShowSpeedAccelerationParameters", true)] public float acceleration` |  |
| **`Default`** | `public static readonly AbilityTrigger.PredictionSettings Default` |  |
| **`delay`** | `[ShowIf("_shouldShowSimpleParameters", true)] public float delay` |  |
| **`frontDistance`** | `[ShowIf("_shouldShowSpeedAccelerationParameters", true)] public float frontDistance` |  |
| **`initSpeed`** | `[ShowIf("_shouldShowSpeedAccelerationParameters", true)] public float initSpeed` |  |
| **`targetSpeed`** | `[ShowIf("_shouldShowSpeedAccelerationParameters", true)] public float targetSpeed` |  |
| **`type`** | `[LabelText("Prediction")] public AbilityTrigger.PredictionSettings.ModelType type` |  |
| **`useCustomParameters`** | `[ShowIf("_shouldShowCustomParameters", true)] public bool useCustomParameters` |  |

:::
