# Class: DewMod

- **Category:** <span class="cat-dot" style="--cat-color: #64748b" data-cat="Misc & Utility"></span> Misc & Utility
- **Namespace:** `Global`
- **Assembly:** `Dew.Core.dll`

```csharp
public static class DewMod
```

## Fields

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`allJsonOverrideItemsLocal`** | `public static List<JsonOverrideItem> allJsonOverrideItemsLocal` | All JSON override items from local mods. |
| **`allMods`** | `public static List<ModItem> allMods` | All mods that are either subscribed by the user or in mods directory. Contains both enabled and disabled mods. |
| **`currentJsonOverrideProcessorsFromServer`** | `public static Dictionary<string, SafeAction<GameObject>> currentJsonOverrideProcessorsFromServer` | GUID to processor map of current JSON overrides, received from the server. |
| **`currentJsonOverrideProcessorsLocal`** | `public static Dictionary<string, SafeAction<GameObject>> currentJsonOverrideProcessorsLocal` | GUID to processor map of current JSON overrides, from this machine. This will not be applied when playing co-op as a client. |
| **`jsonOverrideTargets`** | `public static Dictionary<string, Dictionary<string, string>> jsonOverrideTargets` | Original values of JSON override targets. This acts as a whitelist for overrides. |
| **`loadedInstances`** | `public static List<LoadedModInstance> loadedInstances` | Currently alive mod instances. |
| **`onModLoadEnded`** | `public static SafeAction onModLoadEnded` |  |
| **`onModLoadStarted`** | `public static SafeAction onModLoadStarted` |  |

## Properties

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`isAutoReloadEnabled`** | `public static bool isAutoReloadEnabled { get; }` |  |
| **`isGameplayAltered`** | `public static bool isGameplayAltered { get; }` | Has the game's gameplay been modified by mods? When this is true, a mod icon will be shown on your lobby when you host a game. |
| **`isLoadingMod`** | `public static bool isLoadingMod { get; }` |  |

## Methods

### `BuildJsonOverrideOriginal(string)`

```csharp
public static void BuildJsonOverrideOriginal(string typeName)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `typeName` | `string` |  |

### `BuildJsonOverrideOriginalsFull()`

```csharp
public static void BuildJsonOverrideOriginalsFull()
```

### `CreateItem()`

```csharp
public static UniTask<CreateItemResult_t> CreateItem()
```

**Returns:** `Cysharp.Threading.Tasks.UniTask<T><CreateItemResult_t>`

### `DeleteItem(PublishedFileId_t)`

```csharp
public static UniTask<DeleteItemResult_t> DeleteItem(PublishedFileId_t id)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `id` | `Steamworks.PublishedFileId_t` |  |

**Returns:** `Cysharp.Threading.Tasks.UniTask<T><DeleteItemResult_t>`

### `DisableAutoReload()`

```csharp
public static void DisableAutoReload()
```

### `EnableAutoReload()`

```csharp
public static void EnableAutoReload()
```

### `EndRegisterJsonOverride()`

```csharp
public static void EndRegisterJsonOverride()
```

### `GetAllLocalModDirectories()`

```csharp
public static List<string> GetAllLocalModDirectories()
```

**Returns:** `System.Collections.Generic.List<T><string>`

### `GetSortedModsList(List<ModItem>)`

```csharp
public static List<ModItem> GetSortedModsList(List<ModItem> list)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `list` | [`System.Collections.Generic.List<T><ModItem>`](/api/Global.ModItem) |  |

**Returns:** `System.Collections.Generic.List<T><ModItem>`

### `Load(string)`

```csharp
public static void Load(string id)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `id` | `string` |  |

### `OpenConfigWindow(LoadedModInstance)`

```csharp
public static void OpenConfigWindow(LoadedModInstance mod)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `mod` | [`LoadedModInstance`](/api/Global.LoadedModInstance) |  |

### `Refresh()`

```csharp
public static void Refresh()
```

### `RegisterJsonOverride(JsonOverrideItem, bool)`

```csharp
public static void RegisterJsonOverride(JsonOverrideItem item, bool isFromServer = false)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `item` | [`JsonOverrideItem`](/api/Global.JsonOverrideItem) |  |
| `isFromServer` | `bool` |  |

### `RegisterJsonOverride(string)`

```csharp
public static void RegisterJsonOverride(string path)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `path` | `string` |  |

### `RegisterJsonOverridesInDirectory(string)`

```csharp
public static void RegisterJsonOverridesInDirectory(string dir)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `dir` | `string` |  |

### `ReloadFromActiveMods()`

```csharp
public static void ReloadFromActiveMods()
```

### `StartRegisterJsonOverride(bool)`

You must call this before registering any overrides.

```csharp
public static void StartRegisterJsonOverride(bool willRegisterAcrossMultipleFrames = false)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `willRegisterAcrossMultipleFrames` | `bool` |  |

### `UpdateItem(PublishedFileId_t, ModItem)`

```csharp
public static UniTask<SubmitItemUpdateResult_t> UpdateItem(PublishedFileId_t id, ModItem item)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `id` | `Steamworks.PublishedFileId_t` |  |
| `item` | [`ModItem`](/api/Global.ModItem) |  |

**Returns:** `Cysharp.Threading.Tasks.UniTask<T><SubmitItemUpdateResult_t>`
