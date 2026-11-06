# Class: DewSave

- **Category:** <span class="cat-dot" style="--cat-color: #64748b" data-cat="Misc & Utility"></span> Misc & Utility
- **Namespace:** `Global`
- **Assembly:** `Dew.Core.dll`

```csharp
public static class DewSave
```

## Fields (8)

::: details Click to expand Fields (8)

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`items`** | `public static DewItemsData items` |  |
| **`onSaveEnded`** | `public static SafeAction onSaveEnded` |  |
| **`onSaveStarted`** | `public static SafeAction onSaveStarted` |  |
| **`onSettingsChanged`** | `public static SafeAction onSettingsChanged` |  |
| **`platformSettings`** | `public static DewPlatformSettings platformSettings` |  |
| **`profileContinue`** | `public static DewProfileContinue profileContinue` |  |
| **`profileMain`** | `public static DewProfile profileMain` |  |
| **`profileStats`** | `public static DewProfileStats profileStats` |  |

:::

## Properties (4)

::: details Click to expand Properties (4)

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`profileContinuePath`** | `public static string profileContinuePath { get; }` |  |
| **`profileMainPath`** | `public static string profileMainPath { get; }` |  |
| **`profileStatsPath`** | `public static string profileStatsPath { get; }` |  |
| **`SavePrefix`** | `public static string SavePrefix { get; }` |  |

:::

## Methods (29)

::: details `AddMissingServerGeneratedItemsToProfile(DewProfile)`

```csharp
public static void AddMissingServerGeneratedItemsToProfile(DewProfile p)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `p` | [`DewProfile`](/api/Global.DewProfile) |  |

:::

::: details `AddServerGeneratedItem(DecryptedItemData)`

```csharp
public static void AddServerGeneratedItem(DecryptedItemData item)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `item` | `DecryptedItemData` |  |

:::

::: details `ApplyCultureSettings()`

```csharp
public static void ApplyCultureSettings()
```

:::

::: details `ApplySettings()`

Apply current profile settings / platform settings to the game.

```csharp
[RuntimeInitializeOnLoadMethod(RuntimeInitializeLoadType.AfterSceneLoad)]
public static void ApplySettings()
```

:::

::: details `ClearItemsFromItemStorage()`

Clear all items from item-storage

```csharp
public static void ClearItemsFromItemStorage()
```

:::

::: details `ConsumeGameResult(DewGameResult, ref LastGamePlayReward)`

```csharp
public static void ConsumeGameResult(DewGameResult result, ref LastGamePlayReward rewardSummary)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `result` | [`DewGameResult`](/api/Global.DewGameResult) |  |
| `rewardSummary` | [`LastGamePlayReward`](/api/Global.LastGamePlayReward) |  |

:::

::: details `ConvertProfile(string)`

Create a new converted profile of different edition to make it compatible with current version.Previous profile will be deleted.

```csharp
public static void ConvertProfile(string path)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `path` | `string` |  |

:::

::: details `CreateProfile(string)`

Create and use new profile.

```csharp
public static void CreateProfile(string name)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `name` | `string` |  |

:::

::: details `CreateSubProfilesIfNonExistent(string)`

```csharp
public static void CreateSubProfilesIfNonExistent(string mainPath)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `mainPath` | `string` |  |

:::

::: details `CreateZipWithJsonFiles(string, string)`

```csharp
public static void CreateZipWithJsonFiles(string sourceDirectory, string zipFilePath)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `sourceDirectory` | `string` |  |
| `zipFilePath` | `string` |  |

:::

::: details `DeleteProfile(string)`

```csharp
public static void DeleteProfile(string path)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `path` | `string` |  |

:::

::: details `Exists(string)`

```csharp
public static bool Exists(string path)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `path` | `string` |  |

**Returns:** `bool`

:::

::: details `GetNormalProfiles()`

```csharp
public static List<DewProfileItem> GetNormalProfiles()
```

**Returns:** `System.Collections.Generic.List<T><DewProfileItem>`

:::

::: details `GetPlatformSettingsFileName()`

```csharp
public static string GetPlatformSettingsFileName()
```

**Returns:** `string`

:::

::: details `GetProfileMainFileName(string)`

```csharp
public static string GetProfileMainFileName(string guid)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `guid` | `string` |  |

**Returns:** `string`

:::

::: details `GetProfiles()`

```csharp
public static List<DewProfileItem> GetProfiles()
```

**Returns:** `System.Collections.Generic.List<T><DewProfileItem>`

:::

::: details `LoadPlatformSettings()`

Loads platform settings. Returns true iif the operation succeeds.

```csharp
public static bool LoadPlatformSettings()
```

**Returns:** `bool`

:::

::: details `LoadProfile()`

Load saved user profile of appropriate index. Can load transient profile. Returns true if succeeds.

```csharp
public static bool LoadProfile()
```

**Returns:** `bool`

:::

::: details `LoadProfile(string)`

Loads saved user profile. Returns true if succeeds.

```csharp
public static bool LoadProfile(string path)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `path` | `string` |  |

**Returns:** `bool`

:::

::: details `ResetPlatformSettings()`

```csharp
public static void ResetPlatformSettings()
```

:::

::: details `SaveItems()`

```csharp
public static void SaveItems()
```

:::

::: details `SavePlatformSettings()`

```csharp
public static void SavePlatformSettings()
```

:::

::: details `SaveProfileAll(bool)`

```csharp
public static void SaveProfileAll(bool immediate = false)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `immediate` | `bool` |  |

:::

::: details `SaveProfileContinue(bool)`

```csharp
public static void SaveProfileContinue(bool immediate = false)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `immediate` | `bool` |  |

:::

::: details `SaveProfileMain(bool)`

```csharp
public static void SaveProfileMain(bool immediate = false)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `immediate` | `bool` |  |

:::

::: details `SaveProfileStats(bool)`

```csharp
public static void SaveProfileStats(bool immediate = false)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `immediate` | `bool` |  |

:::

::: details `SetShadowQuality(QualityOff4Levels)`

```csharp
public static void SetShadowQuality(QualityOff4Levels q)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `q` | <a href="/enums#qualityoff4levels" class="enum-link" data-tooltip="Off=0 · Low=1 · Medium=2 · High=3 · Ultra=4">QualityOff4Levels</a> |  |

:::

::: details `ShowSaveLoadErrorAndExit()`

```csharp
public static void ShowSaveLoadErrorAndExit()
```

:::

::: details `SyncAchievements()`

```csharp
public static void SyncAchievements()
```

:::


## Architecture & Relationships

::: details Click to expand Architecture & Relationships

### Used By (40)

*Classes and systems that invoke, reference, or depend on `DewSave`:*

[AchievementManager](/api/Global.AchievementManager) · [CollectablesManager](/api/Global.CollectablesManager) · [Dew](/api/Global.Dew) · `DewCloudSave` · `DewConsoleCommands` · [DewPlatformSettings](/api/Global.DewPlatformSettings) · [DewPlayer](/api/Global.DewPlayer) · [DewProfile](/api/Global.DewProfile) · [DewReverie](/api/Global.DewReverie) · [DewReverieItem](/api/Global.DewReverieItem) · [GameManager](/api/Global.GameManager) · [GameMod_Limbo](/api/Global.GameMod_Limbo) · [GameResultManager](/api/Global.GameResultManager) · [InGameReverieManager](/api/Global.InGameReverieManager) · [LobbyServiceSteam](/api/Global.LobbyServiceSteam) · [QuestManager](/api/Global.QuestManager) · [TitleManager](/api/Global.TitleManager) · `TravelerStoryPresenter` · `UI_Constellations` · `UI_DiscordBanner` · `UI_Guide_View` · `UI_InGame_FloatingWindow_Shop` · `UI_Lobby_Constellations` · `UI_Lobby_Constellations_StarList` · `UI_ModManager` · `UI_PlayRewardAnnouncer` · `UI_SelectControlPresetWindow` · `UI_Settings_View` · `UI_Title_EULAView` · `UI_Title_LanguageSelectionView` · `UI_Title_PrivateDemoNotice` · `UI_Title_ProfileSelection` · `UI_Title_ProfileSelection_DeleteProfileWindow` · `UI_Title_ProfileSelection_ListWindow` · `UI_Title_ProfileSelection_ListWindow_Item` · `UI_Title_ProfileSelection_NewProfileWindow` · `UI_Title_ProfileSelection_RenameProfileWindow` · `UI_Title_SwitchLobbyServer` · `UI_TravelerStory_Details_Story` · `UI_TravelerStory_StoryViewer`

### Dependencies (31)

*Types and components that `DewSave` references or depends upon:*

[AudioManager](/api/Global.AudioManager) · [CursorManager](/api/Global.CursorManager) · `DateTimeExtensions` · `DecryptedItemData` · [Dew](/api/Global.Dew) · [DewAchievementItem](/api/Global.DewAchievementItem) · [DewBuildProfile](/api/Global.DewBuildProfile) · `DewCloudSave` · [DewGameResult](/api/Global.DewGameResult) · [DewInput](/api/Global.DewInput) · `DewItem` · `DewItemsData` · [DewPlatformSettings](/api/Global.DewPlatformSettings) · [DewPlayer](/api/Global.DewPlayer) · [DewProfile](/api/Global.DewProfile) · [DewProfileContinue](/api/Global.DewProfileContinue) · [DewProfileStats](/api/Global.DewProfileStats) · [DewResources](/api/Global.DewResources) · [DewSteam](/api/Global.DewSteam) · [GlobalLogicPackage](/api/Global.GlobalLogicPackage) · [GlobalUIManager](/api/Global.GlobalUIManager) · [ILangaugeChangedCallback](/api/Global.ILangaugeChangedCallback) · [ISettingsChangedCallback](/api/Global.ISettingsChangedCallback) · [InGameTutorialManager](/api/Global.InGameTutorialManager) · [InputManager](/api/Global.InputManager) · [LobbyManager](/api/Global.LobbyManager) · [ManagerBase`1](/api/Global.ManagerBase`1) · `ResultTypeExtensions` · [SafeAction](/api/Global.SafeAction) · [StarEffect](/api/Global.StarEffect) · [VariantDef](/api/Global.VariantDef)

### Related Enums (3)

*Enumerations referenced in fields, properties, or method signatures:*

<a href="/enums#dewprofilestate" class="enum-link" data-tooltip="Normal=0 · Convertible=1 · UnsupportedEdition=2 · UnsupportedVersion=3 · Corrupted=4">DewProfileState</a> · <a href="/enums#dewsubprofilestate" class="enum-link" data-tooltip="Normal=0 · Corrupted=1 · NonExistent=2">DewSubProfileState</a> · <a href="/enums#qualityoff4levels" class="enum-link" data-tooltip="Off=0 · Low=1 · Medium=2 · High=3 · Ultra=4">QualityOff4Levels</a>

:::
