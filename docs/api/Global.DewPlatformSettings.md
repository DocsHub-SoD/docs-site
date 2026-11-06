# Class: DewPlatformSettings

- **Category:** <span class="cat-dot" style="--cat-color: #f97316" data-cat="Data & Core Math"></span> Data & Core Math
- **Namespace:** `Global`
- **Assembly:** `Dew.Core.dll`

```csharp
public class DewPlatformSettings : IInitializableSettings
```

## Fields (11)

::: details Click to expand Fields (11)

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`activeMods`** | `public List<string> activeMods` |  |
| **`audio`** | `public DewAudioSettings_Platform audio` |  |
| **`controls`** | `public DewControlSettings_Platform controls` |  |
| **`CurrentSaveVersion`** | `public const int CurrentSaveVersion = 1` |  |
| **`dontShowProfileMigration`** | `public bool dontShowProfileMigration` |  |
| **`enableAutoReloadMods`** | `public bool enableAutoReloadMods` |  |
| **`gameplay`** | `public DewGameplaySettings_Platform gameplay` |  |
| **`graphics`** | `public DewGraphicsSettings graphics` |  |
| **`lastAgreedEulaKeyLocal`** | `public string lastAgreedEulaKeyLocal` | This acts as a fallback when online check fails. |
| **`lastProfilePath`** | `public string lastProfilePath` |  |
| **`saveVersion`** | `public int saveVersion` |  |

:::

## Methods (2)

::: details `Initialize()`

This is called on new platform settings.

```csharp
public void Initialize()
```

:::

::: details `Validate()`

Must be called at least once before using this platform settings. Does error checking and validation.

```csharp
public void Validate()
```

:::


## Architecture & Relationships

::: details Click to expand Architecture & Relationships

### Used By (1)

*Classes and systems that invoke, reference, or depend on `DewPlatformSettings`:*

[DewSave](/api/Global.DewSave)

### Dependencies (6)

*Types and components that `DewPlatformSettings` references or depends upon:*

[DewAudioSettings_Platform](/api/Global.DewAudioSettings_Platform) · [DewControlSettings_Platform](/api/Global.DewControlSettings_Platform) · [DewGameplaySettings_Platform](/api/Global.DewGameplaySettings_Platform) · [DewGraphicsSettings](/api/Global.DewGraphicsSettings) · [DewSave](/api/Global.DewSave) · [IInitializableSettings](/api/Global.IInitializableSettings)

:::
