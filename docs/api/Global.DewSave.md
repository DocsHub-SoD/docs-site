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
| `q` | [`QualityOff4Levels`](/api/Global.QualityOff4Levels) |  |

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
