# Class: DewResources

- **Category:** <span class="cat-dot" style="--cat-color: #64748b" data-cat="Misc & Utility"></span> Misc & Utility
- **Namespace:** `Global`
- **Assembly:** `Dew.Core.dll`

```csharp
public static class DewResources
```

## Fields

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`EnableVerboseLogging`** | `public static bool EnableVerboseLogging` |  |
| **`onRepairMissingReferences`** | `public static SafeAction onRepairMissingReferences` |  |
| **`onVariantsCleared`** | `public static SafeAction onVariantsCleared` |  |
| **`variantsParent`** | `public static Transform variantsParent` |  |
| **`vOtherPlayersTonedDown`** | `public static int vOtherPlayersTonedDown` |  |
| **`vQualityAdjusted`** | `public static int vQualityAdjusted` |  |

## Properties

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`database`** | `public static DewResourceDatabase database { get; }` |  |
| **`loadedGuids`** | `public static IReadOnlyCollection<string> loadedGuids { get; }` |  |
| **`transparentMat`** | `public static Material transparentMat { get; }` |  |

## Methods

### `AddPreloadRule(MonoBehaviour, Action<PreloadInterface>)`

```csharp
public static void AddPreloadRule(MonoBehaviour owner, Action<PreloadInterface> onPreload)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `owner` | `UnityEngine.MonoBehaviour` |  |
| `onPreload` | [`System.Action<T><PreloadInterface>`](/api/Global.PreloadInterface) |  |

### `ClearAllVariants(bool)`

This will cause serious issues when used in the middle of a run! Use more selective ClearVariants variants to avoid issues.

```csharp
public static int ClearAllVariants(bool repairReferences)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `repairReferences` | `bool` |  |

**Returns:** `int`

### `ClearVariantsOfAsset(string, VariantDef?, bool)`

Destroy loaded variants of the specified asset. This will also clear light version of assets if one exists.

```csharp
public static int ClearVariantsOfAsset(string guid, VariantDef? target, bool repairReferences)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `guid` | `string` |  |
| `target` | [`VariantDef?`](/api/Global.VariantDef) |  |
| `repairReferences` | `bool` |  |

**Returns:** `int`

### `ClearVariantsOfVarDef(VariantDef, bool)`

```csharp
public static int ClearVariantsOfVarDef(VariantDef target, bool repairReferences)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `target` | [`VariantDef`](/api/Global.VariantDef) |  |
| `repairReferences` | `bool` |  |

**Returns:** `int`

### `Convert(Object, Type)`

```csharp
public static Object Convert(Object obj, Type type)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `obj` | `UnityEngine.Object` |  |
| `type` | `System.Type` |  |

**Returns:** `UnityEngine.Object`

### `Convert<T>(Object)`

```csharp
public static T Convert<T>(Object obj) where T : Object
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `obj` | `UnityEngine.Object` |  |
| `` | `T` |  |

**Returns:** `T`

### `FindAllByNameSubstring(string, ResourceLoadSettings)`

```csharp
public static IEnumerable<Object> FindAllByNameSubstring(string substring, ResourceLoadSettings settings = default)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `substring` | `string` |  |
| `settings` | [`ResourceLoadSettings`](/api/Global.ResourceLoadSettings) |  |

**Returns:** `System.Collections.Generic.IEnumerable<T><UnityEngine.Object>`

### `FindAllByNameSubstring<TFilter>(string, ResourceLoadSettings)`

```csharp
public static IEnumerable<TFilter> FindAllByNameSubstring<TFilter>(string substring, ResourceLoadSettings settings = default) where TFilter : Object
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `substring` | `string` |  |
| `settings` | [`ResourceLoadSettings`](/api/Global.ResourceLoadSettings) |  |
| `` | `TFilter` |  |

**Returns:** `System.Collections.Generic.IEnumerable<T><TFilter>`

### `FindAllByType(Type, ResourceLoadSettings)`

```csharp
public static IEnumerable<Object> FindAllByType(Type type, ResourceLoadSettings settings = default)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `type` | `System.Type` |  |
| `settings` | [`ResourceLoadSettings`](/api/Global.ResourceLoadSettings) |  |

**Returns:** `System.Collections.Generic.IEnumerable<T><UnityEngine.Object>`

### `FindAllByType<T>(ResourceLoadSettings)`

```csharp
public static IEnumerable<T> FindAllByType<T>(ResourceLoadSettings settings = default) where T : Object
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `settings` | [`ResourceLoadSettings`](/api/Global.ResourceLoadSettings) |  |
| `` | `T` |  |

**Returns:** `System.Collections.Generic.IEnumerable<T>`

### `FindAllByTypeSubstring(string, ResourceLoadSettings)`

```csharp
public static IEnumerable<Object> FindAllByTypeSubstring(string substring, ResourceLoadSettings settings = default)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `substring` | `string` |  |
| `settings` | [`ResourceLoadSettings`](/api/Global.ResourceLoadSettings) |  |

**Returns:** `System.Collections.Generic.IEnumerable<T><UnityEngine.Object>`

### `FindAllByTypeSubstring<TFilter>(string, ResourceLoadSettings)`

```csharp
public static IEnumerable<TFilter> FindAllByTypeSubstring<TFilter>(string substring, ResourceLoadSettings settings = default) where TFilter : Object
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `substring` | `string` |  |
| `settings` | [`ResourceLoadSettings`](/api/Global.ResourceLoadSettings) |  |
| `` | `TFilter` |  |

**Returns:** `System.Collections.Generic.IEnumerable<T><TFilter>`

### `FindOneByIdSubstring(string, ResourceLoadSettings)`

```csharp
public static Object FindOneByIdSubstring(string substring, ResourceLoadSettings settings = default)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `substring` | `string` |  |
| `settings` | [`ResourceLoadSettings`](/api/Global.ResourceLoadSettings) |  |

**Returns:** `UnityEngine.Object`

### `FindOneByIdSubstring<TFilter>(string, ResourceLoadSettings)`

```csharp
public static TFilter FindOneByIdSubstring<TFilter>(string substring, ResourceLoadSettings settings = default) where TFilter : Object
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `substring` | `string` |  |
| `settings` | [`ResourceLoadSettings`](/api/Global.ResourceLoadSettings) |  |
| `` | `TFilter` |  |

**Returns:** `TFilter`

### `FindOneByTypeSubstring(string, ResourceLoadSettings)`

```csharp
public static Object FindOneByTypeSubstring(string substring, ResourceLoadSettings settings = default)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `substring` | `string` |  |
| `settings` | [`ResourceLoadSettings`](/api/Global.ResourceLoadSettings) |  |

**Returns:** `UnityEngine.Object`

### `FindOneByTypeSubstring<TFilter>(string, ResourceLoadSettings)`

```csharp
public static TFilter FindOneByTypeSubstring<TFilter>(string substring, ResourceLoadSettings settings = default) where TFilter : Object
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `substring` | `string` |  |
| `settings` | [`ResourceLoadSettings`](/api/Global.ResourceLoadSettings) |  |
| `` | `TFilter` |  |

**Returns:** `TFilter`

### `FindRoomNameBySubstring(string)`

```csharp
public static string FindRoomNameBySubstring(string name)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `name` | `string` |  |

**Returns:** `string`

### `GetAllDependencies(out ListReturnHandle<string>, string)`

```csharp
public static List<string> GetAllDependencies(out ListReturnHandle<string> handle, string objName)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `handle` | `ListReturnHandle<string>` |  |
| `objName` | `string` |  |

**Returns:** `System.Collections.Generic.List<T><string>`

### `GetByGuid(string, ResourceLoadSettings)`

```csharp
public static Object GetByGuid(string guid, ResourceLoadSettings settings = default)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `guid` | `string` |  |
| `settings` | [`ResourceLoadSettings`](/api/Global.ResourceLoadSettings) |  |

**Returns:** `UnityEngine.Object`

### `GetByGuid<T>(string, ResourceLoadSettings)`

```csharp
public static T GetByGuid<T>(string guid, ResourceLoadSettings settings = default) where T : Object
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `guid` | `string` |  |
| `settings` | [`ResourceLoadSettings`](/api/Global.ResourceLoadSettings) |  |
| `` | `T` |  |

**Returns:** `T`

### `GetByLinkTypeAndId<T>(ResourceLinkBy, string)`

```csharp
public static T GetByLinkTypeAndId<T>(ResourceLinkBy type, string id) where T : Object
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `type` | [`ResourceLinkBy`](/api/Global.ResourceLinkBy) |  |
| `id` | `string` |  |
| `` | `T` |  |

**Returns:** `T`

### `GetByName(string, ResourceLoadSettings)`

```csharp
public static Object GetByName(string name, ResourceLoadSettings settings = default)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `name` | `string` |  |
| `settings` | [`ResourceLoadSettings`](/api/Global.ResourceLoadSettings) |  |

**Returns:** `UnityEngine.Object`

### `GetByName<T>(string, ResourceLoadSettings)`

```csharp
public static T GetByName<T>(string name, ResourceLoadSettings settings = default) where T : Object
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `name` | `string` |  |
| `settings` | [`ResourceLoadSettings`](/api/Global.ResourceLoadSettings) |  |
| `` | `T` |  |

**Returns:** `T`

### `GetByShortTypeName(string, ResourceLoadSettings)`

```csharp
public static Object GetByShortTypeName(string name, ResourceLoadSettings settings = default)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `name` | `string` |  |
| `settings` | [`ResourceLoadSettings`](/api/Global.ResourceLoadSettings) |  |

**Returns:** `UnityEngine.Object`

### `GetByShortTypeName<T>(string, ResourceLoadSettings)`

```csharp
public static T GetByShortTypeName<T>(string name, ResourceLoadSettings settings = default) where T : Object
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `name` | `string` |  |
| `settings` | [`ResourceLoadSettings`](/api/Global.ResourceLoadSettings) |  |
| `` | `T` |  |

**Returns:** `T`

### `GetByType(Type, ResourceLoadSettings)`

```csharp
public static Object GetByType(Type type, ResourceLoadSettings settings = default)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `type` | `System.Type` |  |
| `settings` | [`ResourceLoadSettings`](/api/Global.ResourceLoadSettings) |  |

**Returns:** `UnityEngine.Object`

### `GetByType<T>(ResourceLoadSettings)`

```csharp
public static T GetByType<T>(ResourceLoadSettings settings = default) where T : Object
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `settings` | [`ResourceLoadSettings`](/api/Global.ResourceLoadSettings) |  |
| `` | `T` |  |

**Returns:** `T`

### `GetByType<T>(Type, ResourceLoadSettings)`

```csharp
public static T GetByType<T>(Type type, ResourceLoadSettings settings = default) where T : Object
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `type` | `System.Type` |  |
| `settings` | [`ResourceLoadSettings`](/api/Global.ResourceLoadSettings) |  |
| `` | `T` |  |

**Returns:** `T`

### `GetGuidOfAsset(Object)`

```csharp
public static string GetGuidOfAsset(Object obj)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `obj` | `UnityEngine.Object` |  |

**Returns:** `string`

### `GetLinkId(Object)`

```csharp
public static string GetLinkId(Object obj)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `obj` | `UnityEngine.Object` |  |

**Returns:** `string`

### `GetLinkType(Type)`

```csharp
public static ResourceLinkBy GetLinkType(Type objType)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `objType` | `System.Type` |  |

**Returns:** `ResourceLinkBy`

### `GetNetworkedPrefab(uint, ResourceLoadSettings)`

```csharp
public static GameObject GetNetworkedPrefab(uint id, ResourceLoadSettings settings = default)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `id` | `uint` |  |
| `settings` | [`ResourceLoadSettings`](/api/Global.ResourceLoadSettings) |  |

**Returns:** `UnityEngine.GameObject`

### `GetNextVariantId()`

```csharp
public static int GetNextVariantId()
```

**Returns:** `int`

### `GetSuggestedResourceLoadSettings(Actor, Type)`

```csharp
public static ResourceLoadSettings GetSuggestedResourceLoadSettings(Actor parentActor, Type childType)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `parentActor` | [`Actor`](/api/Global.Actor) |  |
| `childType` | `System.Type` |  |

**Returns:** `ResourceLoadSettings`

### `GetSuggestedVarDef(Actor, Type)`

```csharp
public static VariantDef GetSuggestedVarDef(Actor parentActor, Type childType)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `parentActor` | [`Actor`](/api/Global.Actor) |  |
| `childType` | `System.Type` |  |

**Returns:** `VariantDef`

### `GetVariantIdForSkin(string)`

```csharp
public static int GetVariantIdForSkin(string skinName)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `skinName` | `string` |  |

**Returns:** `int`

### `Load(string, ResourceLoadSettings)`

```csharp
public static Object Load(string guid, ResourceLoadSettings settings = default)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `guid` | `string` |  |
| `settings` | [`ResourceLoadSettings`](/api/Global.ResourceLoadSettings) |  |

**Returns:** `UnityEngine.Object`

### `Preload(string)`

```csharp
public static void Preload(string guid)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `guid` | `string` |  |

### `RegisterVariantProcessor(int, ResourceVariantProcessor)`

```csharp
public static void RegisterVariantProcessor(int id, ResourceVariantProcessor processor)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `id` | `int` |  |
| `processor` | [`ResourceVariantProcessor`](/api/Global.ResourceVariantProcessor) |  |

### `RepairMissingReferences_Prepare()`

```csharp
public static void RepairMissingReferences_Prepare()
```

### `RepairMissingReferences_Repair()`

```csharp
public static void RepairMissingReferences_Repair()
```

### `TryConvert(Object, Type, out Object)`

```csharp
public static bool TryConvert(Object obj, Type type, out Object result)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `obj` | `UnityEngine.Object` |  |
| `type` | `System.Type` |  |
| `result` | `UnityEngine.Object` |  |

**Returns:** `bool`

### `TryConvert<T>(Object, out T)`

```csharp
public static bool TryConvert<T>(Object obj, out T result) where T : Object
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `obj` | `UnityEngine.Object` |  |
| `result` | `T` |  |
| `` | `T` |  |

**Returns:** `bool`

### `TryGetGuidOfAsset(Object, out string)`

```csharp
public static bool TryGetGuidOfAsset(Object obj, out string guid)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `obj` | `UnityEngine.Object` |  |
| `guid` | `string` |  |

**Returns:** `bool`

### `UnloadUnused()`

```csharp
public static void UnloadUnused()
```

### `UnregisterVariantProcessor(int)`

```csharp
public static void UnregisterVariantProcessor(int id)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `id` | `int` |  |
