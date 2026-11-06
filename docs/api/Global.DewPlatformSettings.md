# Class: DewPlatformSettings

- **Category:** <span class="cat-dot" style="--cat-color: #f97316" data-cat="Data & Core Math"></span> Data & Core Math
- **Namespace:** `Global`
- **Assembly:** `Dew.Core.dll`

```csharp
public class DewPlatformSettings : IInitializableSettings
```

## Fields

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

## Methods

### `Initialize()`

This is called on new platform settings.

```csharp
public void Initialize()
```

### `Validate()`

Must be called at least once before using this platform settings. Does error checking and validation.

```csharp
public void Validate()
```
