# Struct: AbilityTrigger.PredictionSettings

- **Namespace:** `Global`
- **Assembly:** `Dew.Core.dll`

```csharp
[Serializable]
[InlineProperty]
[HideLabel]
public struct AbilityTrigger.PredictionSettings
```

## Fields

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`acceleration`** | `[ShowIf("_shouldShowSpeedAccelerationParameters", true)]
public float acceleration` |  |
| **`Default`** | `public static readonly AbilityTrigger.PredictionSettings Default` |  |
| **`delay`** | `[ShowIf("_shouldShowSimpleParameters", true)]
public float delay` |  |
| **`frontDistance`** | `[ShowIf("_shouldShowSpeedAccelerationParameters", true)]
public float frontDistance` |  |
| **`initSpeed`** | `[ShowIf("_shouldShowSpeedAccelerationParameters", true)]
public float initSpeed` |  |
| **`targetSpeed`** | `[ShowIf("_shouldShowSpeedAccelerationParameters", true)]
public float targetSpeed` |  |
| **`type`** | `[LabelText("Prediction")]
public AbilityTrigger.PredictionSettings.ModelType type` |  |
| **`useCustomParameters`** | `[ShowIf("_shouldShowCustomParameters", true)]
public bool useCustomParameters` |  |
