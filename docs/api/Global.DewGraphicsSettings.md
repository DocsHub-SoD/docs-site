# Class: DewGraphicsSettings

- **Category:** <span class="cat-dot" style="--cat-color: #f97316" data-cat="Data & Core Math"></span> Data & Core Math
- **Namespace:** `Global`
- **Assembly:** `Dew.Core.dll`

```csharp
public class DewGraphicsSettings : IInitializableSettings, IValidatableSettings
```

## Fields (15)

::: details Click to expand Fields (15)

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`displayIndex`** | `public int displayIndex` |  |
| **`fogQuality`** | `public QualityOff3Levels fogQuality` |  |
| **`fullScreenMode`** | `public FullScreenMode fullScreenMode` |  |
| **`gameFrameLimit`** | `public int gameFrameLimit` |  |
| **`menuFrameLimit`** | `public int menuFrameLimit` |  |
| **`particleEffectQuality`** | `public Quality3Levels particleEffectQuality` |  |
| **`playerAbilityCount`** | `public Quality4Levels playerAbilityCount` |  |
| **`resolutionHeight`** | `public int resolutionHeight` |  |
| **`resolutionWidth`** | `public int resolutionWidth` |  |
| **`shaderQuality`** | `public Quality3Levels shaderQuality` |  |
| **`shadowQuality`** | `public QualityOff4Levels shadowQuality` |  |
| **`terrainQuality`** | `public Quality3Levels terrainQuality` |  |
| **`textureQuality`** | `public Quality3Levels textureQuality` |  |
| **`vegetationQuality`** | `public Quality3Levels vegetationQuality` |  |
| **`vSync`** | `public bool vSync` |  |

:::

## Methods (3)

::: details `Clone()`

```csharp
public object Clone()
```

**Returns:** `object`

:::

::: details `Initialize()`

```csharp
public void Initialize()
```

:::

::: details `Validate()`

```csharp
public void Validate()
```

:::


## Architecture & Relationships

::: details Click to expand Architecture & Relationships

### Used By (2)

*Classes and systems that invoke, reference, or depend on `DewGraphicsSettings`:*

[DewPlatformSettings](/api/Global.DewPlatformSettings) · `UI_Settings_View`

### Dependencies (2)

*Types and components that `DewGraphicsSettings` references or depends upon:*

[IInitializableSettings](/api/Global.IInitializableSettings) · [IValidatableSettings](/api/Global.IValidatableSettings)

### Related Enums (4)

*Enumerations referenced in fields, properties, or method signatures:*

[`Quality3Levels`](/enums#quality3levels) · [`Quality4Levels`](/enums#quality4levels) · [`QualityOff3Levels`](/enums#qualityoff3levels) · [`QualityOff4Levels`](/enums#qualityoff4levels)

:::
