# Class: DewGameplaySettings_Platform

- **Category:** <span class="cat-dot" style="--cat-color: #3b82f6" data-cat="Managers & Systems"></span> Managers & Systems
- **Namespace:** `Global`
- **Assembly:** `Dew.Core.dll`

```csharp
public class DewGameplaySettings_Platform : IInitializableSettings
```

## Fields (4)

::: details Click to expand Fields (4)

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`disableSoftwareCursor`** | `public bool disableSoftwareCursor` |  |
| **`enableDeveloperMode`** | `public bool enableDeveloperMode` |  |
| **`skipIntro`** | `public bool skipIntro` |  |
| **`skipPhotosensitivityWarning`** | `public bool skipPhotosensitivityWarning` |  |

:::

## Methods (2)

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


## Architecture & Relationships

::: details Click to expand Architecture & Relationships

### Used By (2)

*Classes and systems that invoke, reference, or depend on `DewGameplaySettings_Platform`:*

[DewPlatformSettings](/api/Global.DewPlatformSettings) · `UI_Settings_View`

### Dependencies (2)

*Types and components that `DewGameplaySettings_Platform` references or depends upon:*

[IInitializableSettings](/api/Global.IInitializableSettings) · [IValidatableSettings](/api/Global.IValidatableSettings)

:::
