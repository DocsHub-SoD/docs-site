# Class: Dew

- **Namespace:** `Global`
- **Assembly:** `Dew.Core.dll`

```csharp
public static class Dew
```

## Fields

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`CharacterColor`** | `public static readonly Color CharacterColor` |  |
| **`CharacterColorHex`** | `public static readonly string CharacterColorHex` |  |
| **`CommonColor`** | `public static readonly Color CommonColor` |  |
| **`CommonColorHex`** | `public static readonly string CommonColorHex` |  |
| **`DestroyDelay`** | `public const float DestroyDelay = 0.3` |  |
| **`DestructionColor`** | `public static readonly Color DestructionColor` |  |
| **`DreamDustColor`** | `public static readonly Color DreamDustColor` |  |
| **`EpicColor`** | `public static readonly Color EpicColor` |  |
| **`EpicColorHex`** | `public static readonly string EpicColorHex` |  |
| **`FlexibleColor`** | `public static readonly Color FlexibleColor` |  |
| **`GoldColor`** | `public static readonly Color GoldColor` |  |
| **`HealthColor`** | `public static readonly Color HealthColor` |  |
| **`HeroOrder`** | `public static readonly List&lt;string&gt; HeroOrder` |  |
| **`IdentityColor`** | `public static readonly Color IdentityColor` |  |
| **`IdentityColorHex`** | `public static readonly string IdentityColorHex` |  |
| **`ImaginationColor`** | `public static readonly Color ImaginationColor` |  |
| **`LegendaryColor`** | `public static readonly Color LegendaryColor` |  |
| **`LegendaryColorHex`** | `public static readonly string LegendaryColorHex` |  |
| **`LifeColor`** | `public static readonly Color LifeColor` |  |
| **`ObliterationSlotPrice`** | `public static readonly int[] ObliterationSlotPrice` |  |
| **`PlatinumCoinColor`** | `public static readonly Color PlatinumCoinColor` |  |
| **`RareColor`** | `public static readonly Color RareColor` |  |
| **`RareColorHex`** | `public static readonly string RareColorHex` |  |
| **`StardustColor`** | `public static readonly Color StardustColor` |  |
| **`UniqueColor`** | `public static readonly Color UniqueColor` |  |
| **`UniqueColorHex`** | `public static readonly string UniqueColorHex` |  |

## Properties

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`achievementsByName`** | `public static IReadOnlyDictionary&lt;string, Type&gt; achievementsByName { get; }` |  |
| **`allAchievements`** | `public static IReadOnlyList&lt;Type&gt; allAchievements { get; }` |  |
| **`allArtifacts`** | `public static IReadOnlyList&lt;Type&gt; allArtifacts { get; }` |  |
| **`allGameModifiers`** | `public static IReadOnlyList&lt;Type&gt; allGameModifiers { get; }` |  |
| **`allGems`** | `public static IReadOnlyList&lt;Type&gt; allGems { get; }` |  |
| **`allHeroes`** | `public static IReadOnlyList&lt;Type&gt; allHeroes { get; }` |  |
| **`allHeroSkills`** | `public static IReadOnlyList&lt;Type&gt; allHeroSkills { get; }` |  |
| **`allLucidDreams`** | `public static IReadOnlyList&lt;Type&gt; allLucidDreams { get; }` |  |
| **`allMonsters`** | `public static IReadOnlyList&lt;Type&gt; allMonsters { get; }` |  |
| **`allOldStars`** | `public static IReadOnlyList&lt;DewStarItemOld&gt; allOldStars { get; }` |  |
| **`allReveries`** | `public static IReadOnlyList&lt;DewReverieItem&gt; allReveries { get; }` |  |
| **`allRoomModifiers`** | `public static IReadOnlyList&lt;Type&gt; allRoomModifiers { get; }` |  |
| **`allSkills`** | `public static IReadOnlyList&lt;Type&gt; allSkills { get; }` |  |
| **`allStarTypes`** | `public static IReadOnlyList&lt;Type&gt; allStarTypes { get; }` |  |
| **`allTutorialItems`** | `public static IReadOnlyList&lt;Type&gt; allTutorialItems { get; }` |  |
| **`gameCanvas`** | `public static Canvas gameCanvas { get; }` |  |
| **`heroTypeOfOldStar`** | `public static IReadOnlyDictionary&lt;DewStarItemOld, Type&gt; heroTypeOfOldStar { get; }` | Contains all stars. Non-hero stars will have value of null. |
| **`mainCamera`** | `public static Camera mainCamera { get; }` |  |
| **`resourceLinkTypes`** | `public static IReadOnlyList&lt;(Type, DewResourceLinkAttribute)&gt; resourceLinkTypes { get; }` |  |
| **`reveriesByName`** | `public static IReadOnlyDictionary&lt;string, DewReverieItem&gt; reveriesByName { get; }` |  |

## Methods

### `CallDelayed(Action, int)`

Call a function delayed by one frame.

```csharp
public static void CallDelayed(Action func, int frameCount = 1)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `func` | `System.Action` |  |
| `frameCount` | `int` |  |

### `CallOnReady(MonoBehaviour, Func&lt;bool&gt;, Action)`

```csharp
public static void CallOnReady(MonoBehaviour caller, Func<bool> condition, Action func)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `caller` | `UnityEngine.MonoBehaviour` |  |
| `condition` | `System.Func&lt;TResult&gt;&lt;bool&gt;` |  |
| `func` | `System.Action` |  |

### `ClearTypeReferences()`

```csharp
public static void ClearTypeReferences()
```

### `ContainsData(IDictionary&lt;string, string&gt;, string, string, string)`

```csharp
public static bool ContainsData(this IDictionary<string, string> dict, string key0, string key1, string key2)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `dict` | `System.Collections.Generic.IDictionary&lt;TKey, TValue&gt;&lt;string,string&gt;` |  |
| `key0` | `string` |  |
| `key1` | `string` |  |
| `key2` | `string` |  |

**Returns:** `bool`

### `ContainsData(IDictionary&lt;string, string&gt;, string, string)`

```csharp
public static bool ContainsData(this IDictionary<string, string> dict, string key0, string key1)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `dict` | `System.Collections.Generic.IDictionary&lt;TKey, TValue&gt;&lt;string,string&gt;` |  |
| `key0` | `string` |  |
| `key1` | `string` |  |

**Returns:** `bool`

### `ContainsData(IDictionary&lt;string, string&gt;, string)`

```csharp
public static bool ContainsData(this IDictionary<string, string> dict, string key0)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `dict` | `System.Collections.Generic.IDictionary&lt;TKey, TValue&gt;&lt;string,string&gt;` |  |
| `key0` | `string` |  |

**Returns:** `bool`

### `ConvertToStringInvariantCulture(object)`

```csharp
public static string ConvertToStringInvariantCulture(object value)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `value` | `object` |  |

**Returns:** `string`

### `CreateAbilityInstance&lt;T&gt;(T, Vector3, Quaternion?, Actor, CastInfo, Action&lt;T&gt;)`

```csharp
public static T CreateAbilityInstance<T>(T prefab, Vector3 position, Quaternion? rotation, Actor parent, CastInfo info, Action<T> beforePrepare = null) where T : AbilityInstance
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `prefab` | `T` |  |
| `position` | `UnityEngine.Vector3` |  |
| `rotation` | `UnityEngine.Quaternion?` |  |
| `parent` | [Actor](/api/Global.Actor) |  |
| `info` | [CastInfo](/api/Global.CastInfo) |  |
| `beforePrepare` | `System.Action&lt;T&gt;&lt;T&gt;` |  |
| `` | `T` |  |

**Returns:** `T`

### `CreateAbilityInstance&lt;T&gt;(Vector3, Quaternion?, Actor, CastInfo, Action&lt;T&gt;)`

```csharp
public static T CreateAbilityInstance<T>(Vector3 position, Quaternion? rotation, Actor parent, CastInfo info, Action<T> beforePrepare = null) where T : AbilityInstance
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `position` | `UnityEngine.Vector3` |  |
| `rotation` | `UnityEngine.Quaternion?` |  |
| `parent` | [Actor](/api/Global.Actor) |  |
| `info` | [CastInfo](/api/Global.CastInfo) |  |
| `beforePrepare` | `System.Action&lt;T&gt;&lt;T&gt;` |  |
| `` | `T` |  |

**Returns:** `T`

### `CreateAbilityTrigger&lt;T&gt;(T, Action&lt;T&gt;)`

```csharp
public static T CreateAbilityTrigger<T>(T trigger, Action<T> beforePrepare = null) where T : AbilityTrigger
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `trigger` | `T` |  |
| `beforePrepare` | `System.Action&lt;T&gt;&lt;T&gt;` |  |
| `` | `T` |  |

**Returns:** `T`

### `CreateAbilityTrigger&lt;T&gt;(Action&lt;T&gt;)`

```csharp
public static T CreateAbilityTrigger<T>(Action<T> beforeSpawn = null) where T : AbilityTrigger
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `beforeSpawn` | `System.Action&lt;T&gt;&lt;T&gt;` |  |
| `` | `T` |  |

**Returns:** `T`

### `CreateActor&lt;T&gt;()`

```csharp
public static T CreateActor<T>() where T : Actor
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `` | `T` |  |

**Returns:** `T`

### `CreateActor&lt;T&gt;(T, Vector3, Quaternion?, Actor, Action&lt;T&gt;)`

```csharp
public static T CreateActor<T>(T prefab, Vector3 position, Quaternion? rotation, Actor parent = null, Action<T> beforePrepare = null) where T : Actor
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `prefab` | `T` |  |
| `position` | `UnityEngine.Vector3` |  |
| `rotation` | `UnityEngine.Quaternion?` |  |
| `parent` | [Actor](/api/Global.Actor) |  |
| `beforePrepare` | `System.Action&lt;T&gt;&lt;T&gt;` |  |
| `` | `T` |  |

**Returns:** `T`

### `CreateActor&lt;T&gt;(Action&lt;T&gt;)`

```csharp
public static T CreateActor<T>(Action<T> beforePrepare = null) where T : Actor
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `beforePrepare` | `System.Action&lt;T&gt;&lt;T&gt;` |  |
| `` | `T` |  |

**Returns:** `T`

### `CreateActor&lt;T&gt;(Vector3, Quaternion?, Actor, Action&lt;T&gt;)`

```csharp
public static T CreateActor<T>(Vector3 position, Quaternion? rotation, Actor parent = null, Action<T> beforePrepare = null) where T : Actor
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `position` | `UnityEngine.Vector3` |  |
| `rotation` | `UnityEngine.Quaternion?` |  |
| `parent` | [Actor](/api/Global.Actor) |  |
| `beforePrepare` | `System.Action&lt;T&gt;&lt;T&gt;` |  |
| `` | `T` |  |

**Returns:** `T`

### `CreateGem&lt;T&gt;(T, Vector3, int, DewPlayer, Action&lt;T&gt;)`

```csharp
public static T CreateGem<T>(T gem, Vector3 position, int quality, DewPlayer tempOwner = null, Action<T> beforePrepare = null) where T : Gem
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `gem` | `T` |  |
| `position` | `UnityEngine.Vector3` |  |
| `quality` | `int` |  |
| `tempOwner` | [DewPlayer](/api/Global.DewPlayer) |  |
| `beforePrepare` | `System.Action&lt;T&gt;&lt;T&gt;` |  |
| `` | `T` |  |

**Returns:** `T`

### `CreateGem&lt;T&gt;(Vector3, int, DewPlayer, Action&lt;T&gt;)`

```csharp
public static T CreateGem<T>(Vector3 position, int quality, DewPlayer tempOwner = null, Action<T> beforePrepare = null) where T : Gem
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `position` | `UnityEngine.Vector3` |  |
| `quality` | `int` |  |
| `tempOwner` | [DewPlayer](/api/Global.DewPlayer) |  |
| `beforePrepare` | `System.Action&lt;T&gt;&lt;T&gt;` |  |
| `` | `T` |  |

**Returns:** `T`

### `CreateSkillTrigger&lt;T&gt;(T, Vector3, int, DewPlayer, Action&lt;T&gt;)`

```csharp
public static T CreateSkillTrigger<T>(T trigger, Vector3 position, int level, DewPlayer tempOwner = null, Action<T> beforePrepare = null) where T : SkillTrigger
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `trigger` | `T` |  |
| `position` | `UnityEngine.Vector3` |  |
| `level` | `int` |  |
| `tempOwner` | [DewPlayer](/api/Global.DewPlayer) |  |
| `beforePrepare` | `System.Action&lt;T&gt;&lt;T&gt;` |  |
| `` | `T` |  |

**Returns:** `T`

### `CreateSkillTrigger&lt;T&gt;(Vector3, int, DewPlayer, Action&lt;T&gt;)`

```csharp
public static T CreateSkillTrigger<T>(Vector3 position, int level, DewPlayer tempOwner = null, Action<T> beforePrepare = null) where T : SkillTrigger
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `position` | `UnityEngine.Vector3` |  |
| `level` | `int` |  |
| `tempOwner` | [DewPlayer](/api/Global.DewPlayer) |  |
| `beforePrepare` | `System.Action&lt;T&gt;&lt;T&gt;` |  |
| `` | `T` |  |

**Returns:** `T`

### `CreateStatusEffect&lt;T&gt;(T, Entity, Actor, CastInfo, Action&lt;T&gt;)`

Create a new status effect and attach it to an entity.This can return null if the creation fails:e.g. Trying to apply a status effect with isKilledByUnstoppable flag to an unstoppable/invulnerable entity.

```csharp
public static T CreateStatusEffect<T>(T prefab, Entity victim, Actor parent, CastInfo info, Action<T> beforePrepare = null) where T : StatusEffect
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `prefab` | `T` |  |
| `victim` | [Entity](/api/Global.Entity) |  |
| `parent` | [Actor](/api/Global.Actor) |  |
| `info` | [CastInfo](/api/Global.CastInfo) |  |
| `beforePrepare` | `System.Action&lt;T&gt;&lt;T&gt;` |  |
| `` | `T` |  |

**Returns:** `T`

### `CreateStatusEffect&lt;T&gt;(Entity, Actor, CastInfo, Action&lt;T&gt;)`

Create a new status effect and attach it to an entity.This can return null if the creation fails:e.g. Trying to apply a status effect with isKilledByUnstoppable flag to an unstoppable/invulnerable entity.

```csharp
public static T CreateStatusEffect<T>(Entity victim, Actor parent, CastInfo info, Action<T> beforePrepare = null) where T : StatusEffect
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `victim` | [Entity](/api/Global.Entity) |  |
| `parent` | [Actor](/api/Global.Actor) |  |
| `info` | [CastInfo](/api/Global.CastInfo) |  |
| `beforePrepare` | `System.Action&lt;T&gt;&lt;T&gt;` |  |
| `` | `T` |  |

**Returns:** `T`

### `Debounce(Object, float, Action, object)`

```csharp
public static void Debounce(Object owner, float unscaledTime, Action callback, object id = null)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `owner` | `UnityEngine.Object` |  |
| `unscaledTime` | `float` |  |
| `callback` | `System.Action` |  |
| `id` | `object` |  |

### `Destroy(GameObject)`

Destroy a networked game object. Despawning and destroying will be delayed for network RPCs and cleanups.

```csharp
public static void Destroy(GameObject gameObject)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `gameObject` | `UnityEngine.GameObject` |  |

### `FilterNonOkayValues(ref float, float)`

```csharp
public static void FilterNonOkayValues(ref float v, float fallback = 0)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `v` | `float` |  |
| `fallback` | `float` |  |

### `FilterNonOkayValues(ref Vector2, Vector2)`

```csharp
public static void FilterNonOkayValues(ref Vector2 v, Vector2 fallback = default)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `v` | `UnityEngine.Vector2` |  |
| `fallback` | `UnityEngine.Vector2` |  |

### `FilterNonOkayValues(ref Vector3, Vector3)`

```csharp
public static void FilterNonOkayValues(ref Vector3 v, Vector3 fallback = default)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `v` | `UnityEngine.Vector3` |  |
| `fallback` | `UnityEngine.Vector3` |  |

### `FindActorOfType&lt;T&gt;()`

```csharp
public static T FindActorOfType<T>() where T : Actor
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `` | `T` |  |

**Returns:** `T`

### `FindAllActorsOfType&lt;T&gt;(out ListReturnHandle&lt;T&gt;)`

```csharp
public static List<T> FindAllActorsOfType<T>(out ListReturnHandle<T> handle) where T : Actor
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `handle` | `ListReturnHandle&lt;T&gt;` |  |
| `` | `T` |  |

**Returns:** `System.Collections.Generic.List&lt;T&gt;&lt;T&gt;`

### `FindInterfaceOfType&lt;T&gt;(bool)`

```csharp
public static T FindInterfaceOfType<T>(bool includeInactive) where T : class
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `includeInactive` | `bool` |  |
| `` | `T` |  |

**Returns:** `T`

### `FindInterfacesOfType&lt;T&gt;(bool)`

```csharp
public static T[] FindInterfacesOfType<T>(bool includeInactive) where T : class
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `includeInactive` | `bool` |  |
| `` | `T` |  |

**Returns:** `T[]`

### `FormatBigNumbers(float, float, string)`

```csharp
public static string FormatBigNumbers(float number, float threshold, string format)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `number` | `float` |  |
| `threshold` | `float` |  |
| `format` | `string` |  |

**Returns:** `string`

### `GetAchievementColor(Type)`

```csharp
public static Color GetAchievementColor(Type achievementType)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `achievementType` | `System.Type` |  |

**Returns:** `UnityEngine.Color`

### `GetAchievementColorHex(Type)`

```csharp
public static string GetAchievementColorHex(Type achievementType)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `achievementType` | `System.Type` |  |

**Returns:** `string`

### `GetAliveHeroCount()`

```csharp
public static int GetAliveHeroCount()
```

**Returns:** `int`

### `GetClosestAliveHero(Vector3, bool)`

```csharp
public static Hero GetClosestAliveHero(Vector3 pivot, bool fallbackToDead = true)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `pivot` | `UnityEngine.Vector3` |  |
| `fallbackToDead` | `bool` |  |

**Returns:** `Hero`

### `GetClosestHeroDistance(Vector3, bool)`

```csharp
public static float GetClosestHeroDistance(Vector3 pivot, bool fallbackToDead = true)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `pivot` | `UnityEngine.Vector3` |  |
| `fallbackToDead` | `bool` |  |

**Returns:** `float`

### `GetControlPresetWindow()`

```csharp
public static IControlPresetWindow GetControlPresetWindow()
```

**Returns:** `IControlPresetWindow`

### `GetCoroutiner()`

```csharp
public static Coroutiner GetCoroutiner()
```

**Returns:** `Coroutiner`

### `GetCurrencyColor(CurrencyType)`

```csharp
public static Color GetCurrencyColor(CurrencyType type)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `type` | [CurrencyType](/api/Global.CurrencyType) |  |

**Returns:** `UnityEngine.Color`

### `GetCurrencyColorHex(CurrencyType)`

```csharp
public static string GetCurrencyColorHex(CurrencyType type)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `type` | [CurrencyType](/api/Global.CurrencyType) |  |

**Returns:** `string`

### `GetCurrentMultiplayerCompatibilityVersion()`

Used to check game compatibility between multiplayer host/clients.This special version is used to allow cross-platform multiplayer (DRM-Free, STOVE, Steam, e.g.)

```csharp
public static string GetCurrentMultiplayerCompatibilityVersion()
```

**Returns:** `string`

### `GetData&lt;T&gt;(IDictionary&lt;string, string&gt;, string, string, string)`

```csharp
public static T GetData<T>(this IDictionary<string, string> dict, string key0, string key1, string key2)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `dict` | `System.Collections.Generic.IDictionary&lt;TKey, TValue&gt;&lt;string,string&gt;` |  |
| `key0` | `string` |  |
| `key1` | `string` |  |
| `key2` | `string` |  |
| `` | `T` |  |

**Returns:** `T`

### `GetData&lt;T&gt;(IDictionary&lt;string, string&gt;, string, string)`

```csharp
public static T GetData<T>(this IDictionary<string, string> dict, string key0, string key1)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `dict` | `System.Collections.Generic.IDictionary&lt;TKey, TValue&gt;&lt;string,string&gt;` |  |
| `key0` | `string` |  |
| `key1` | `string` |  |
| `` | `T` |  |

**Returns:** `T`

### `GetData&lt;T&gt;(IDictionary&lt;string, string&gt;, string)`

```csharp
public static T GetData<T>(this IDictionary<string, string> dict, string key0)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `dict` | `System.Collections.Generic.IDictionary&lt;TKey, TValue&gt;&lt;string,string&gt;` |  |
| `key0` | `string` |  |
| `` | `T` |  |

**Returns:** `T`

### `GetDataKey(string, string, string)`

```csharp
public static string GetDataKey(string key0, string key1, string key2)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `key0` | `string` |  |
| `key1` | `string` |  |
| `key2` | `string` |  |

**Returns:** `string`

### `GetDataKey(string, string)`

```csharp
public static string GetDataKey(string key0, string key1)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `key0` | `string` |  |
| `key1` | `string` |  |

**Returns:** `string`

### `GetDataKey(string)`

```csharp
public static string GetDataKey(string key0)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `key0` | `string` |  |

**Returns:** `string`

### `GetDataOrDefault&lt;T&gt;(IDictionary&lt;string, string&gt;, string, T)`

```csharp
public static T GetDataOrDefault<T>(this IDictionary<string, string> dict, string key0, T defaultValue = default)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `dict` | `System.Collections.Generic.IDictionary&lt;TKey, TValue&gt;&lt;string,string&gt;` |  |
| `key0` | `string` |  |
| `defaultValue` | `T` |  |
| `` | `T` |  |

**Returns:** `T`

### `GetDataOrDefault&lt;T&gt;(IDictionary&lt;string, string&gt;, string, string, T)`

```csharp
public static T GetDataOrDefault<T>(this IDictionary<string, string> dict, string key0, string key1, T defaultValue = default)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `dict` | `System.Collections.Generic.IDictionary&lt;TKey, TValue&gt;&lt;string,string&gt;` |  |
| `key0` | `string` |  |
| `key1` | `string` |  |
| `defaultValue` | `T` |  |
| `` | `T` |  |

**Returns:** `T`

### `GetDataOrDefault&lt;T&gt;(IDictionary&lt;string, string&gt;, string, string, string, T)`

```csharp
public static T GetDataOrDefault<T>(this IDictionary<string, string> dict, string key0, string key1, string key2, T defaultValue = default)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `dict` | `System.Collections.Generic.IDictionary&lt;TKey, TValue&gt;&lt;string,string&gt;` |  |
| `key0` | `string` |  |
| `key1` | `string` |  |
| `key2` | `string` |  |
| `defaultValue` | `T` |  |
| `` | `T` |  |

**Returns:** `T`

### `GetDefaultObliterationSlots()`

```csharp
public static int GetDefaultObliterationSlots()
```

**Returns:** `int`

### `GetDejavuCost(Object, int)`

```csharp
public static int GetDejavuCost(Object target, int wins = -1)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `target` | `UnityEngine.Object` |  |
| `wins` | `int` |  |

**Returns:** `int`

### `GetDejavuMaxWins(Object)`

```csharp
public static int GetDejavuMaxWins(Object target)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `target` | `UnityEngine.Object` |  |

**Returns:** `int`

### `GetGoodRewardPosition(Vector3, float)`

This applies random offset to pivot and avoids nearby IBanRoomNodesNearby, items and interactables.The position will be traversable by nearest hero.

```csharp
public static Vector3 GetGoodRewardPosition(Vector3 pivot, float randomOffset = 2)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `pivot` | `UnityEngine.Vector3` |  |
| `randomOffset` | `float` |  |

**Returns:** `UnityEngine.Vector3`

### `GetHex(Color)`

```csharp
public static string GetHex(Color color)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `color` | `UnityEngine.Color` |  |

**Returns:** `string`

### `GetMaxObliterationSlots()`

```csharp
public static int GetMaxObliterationSlots()
```

**Returns:** `int`

### `GetMultiplayerCompatibilityVersion(string)`

```csharp
public static string GetMultiplayerCompatibilityVersion(string bundleVersion)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `bundleVersion` | `string` |  |

**Returns:** `string`

### `GetNavMeshPath(Vector3, Vector3)`

```csharp
public static NavMeshPath GetNavMeshPath(Vector3 start, Vector3 end)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `start` | `UnityEngine.Vector3` |  |
| `end` | `UnityEngine.Vector3` |  |

**Returns:** `UnityEngine.AI.NavMeshPath`

### `GetNavMeshPathStatus(Vector3, Vector3)`

```csharp
public static NavMeshPathStatus GetNavMeshPathStatus(Vector3 start, Vector3 end)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `start` | `UnityEngine.Vector3` |  |
| `end` | `UnityEngine.Vector3` |  |

**Returns:** `UnityEngine.AI.NavMeshPathStatus`

### `GetObliterationMinAllowedHeroes()`

```csharp
public static int GetObliterationMinAllowedHeroes()
```

**Returns:** `int`

### `GetObliterationMinAllowedItemsPerRarity()`

```csharp
public static int GetObliterationMinAllowedItemsPerRarity()
```

**Returns:** `int`

### `GetObliterationSlotPrice(int)`

```csharp
public static int GetObliterationSlotPrice(int slotIndex)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `slotIndex` | `int` |  |

**Returns:** `int`

### `GetOriginalName(string)`

Clean the given name removing (Clone) or variant suffixes.Useful when trying to figure out id of name-linked resources.

```csharp
public static string GetOriginalName(string name)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `name` | `string` |  |

**Returns:** `string`

### `GetParentDirectory(string)`

```csharp
public static string GetParentDirectory(string path)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `path` | `string` |  |

**Returns:** `string`

### `GetPositionOnGround(Vector3, float)`

```csharp
public static Vector3 GetPositionOnGround(Vector3 position, float yDiffRange = 50)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `position` | `UnityEngine.Vector3` |  |
| `yDiffRange` | `float` |  |

**Returns:** `UnityEngine.Vector3`

### `GetProjectRootPath()`

```csharp
public static string GetProjectRootPath()
```

**Returns:** `string`

### `GetRarityColor(Rarity)`

```csharp
public static Color GetRarityColor(Rarity rarity)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `rarity` | [Rarity](/api/Global.Rarity) |  |

**Returns:** `UnityEngine.Color`

### `GetRarityColor(SkinRarity)`

```csharp
public static Color GetRarityColor(SkinRarity rarity)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `rarity` | [SkinRarity](/api/Global.SkinRarity) |  |

**Returns:** `UnityEngine.Color`

### `GetRarityColorHex(Rarity)`

Gets rarity color with prefix #.

```csharp
public static string GetRarityColorHex(Rarity rarity)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `rarity` | [Rarity](/api/Global.Rarity) |  |

**Returns:** `string`

### `GetRarityColorHex(SkinRarity)`

```csharp
public static string GetRarityColorHex(SkinRarity rarity)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `rarity` | [SkinRarity](/api/Global.SkinRarity) |  |

**Returns:** `string`

### `GetReadableTimespanConcise(TimeSpan)`

```csharp
public static string GetReadableTimespanConcise(TimeSpan t)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `t` | `System.TimeSpan` |  |

**Returns:** `string`

### `GetReadableTimespanDetailed(TimeSpan)`

```csharp
public static string GetReadableTimespanDetailed(TimeSpan t)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `t` | `System.TimeSpan` |  |

**Returns:** `string`

### `GetRequiredAchievementOfTarget(string)`

```csharp
public static Type GetRequiredAchievementOfTarget(string targetTypeName)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `targetTypeName` | `string` |  |

**Returns:** `System.Type`

### `GetRequiredAchievementOfTarget(Type)`

```csharp
public static Type GetRequiredAchievementOfTarget(Type targetType)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `targetType` | `System.Type` |  |

**Returns:** `System.Type`

### `GetRequiredMasteryLevelForStarSlotUnlock(int)`

```csharp
public static int GetRequiredMasteryLevelForStarSlotUnlock(int index)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `index` | `int` |  |

**Returns:** `int`

### `GetRequiredMasteryPointsToLevelUp(int)`

```csharp
public static long GetRequiredMasteryPointsToLevelUp(int currentLevel)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `currentLevel` | `int` |  |

**Returns:** `long`

### `GetRequiredStardustForStarSlotUnlock(int)`

```csharp
public static int GetRequiredStardustForStarSlotUnlock(int index)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `index` | `int` |  |

**Returns:** `int`

### `GetRewardedMasteryPoints(float)`

```csharp
public static long GetRewardedMasteryPoints(float minutes)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `minutes` | `float` |  |

**Returns:** `long`

### `GetStarCategoryColor(StarType)`

```csharp
public static Color GetStarCategoryColor(StarType type)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `type` | [StarType](/api/Global.StarType) |  |

**Returns:** `UnityEngine.Color`

### `GetStardustRewardOnLevelUpAmount(int)`

```csharp
public static int GetStardustRewardOnLevelUpAmount(int nextLevel)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `nextLevel` | `int` |  |

**Returns:** `int`

### `GetTypeFromShortName(string)`

```csharp
public static Type GetTypeFromShortName(string typeName)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `typeName` | `string` |  |

**Returns:** `System.Type`

### `GetUIComponentBelowCursor&lt;T&gt;(bool)`

```csharp
public static T GetUIComponentBelowCursor<T>(bool includeParent = true) where T : Component
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `includeParent` | `bool` |  |
| `` | `T` |  |

**Returns:** `T`

### `GetUnlockedTargetsOfAchievement(Type)`

```csharp
public static List<Type> GetUnlockedTargetsOfAchievement(Type achievementType)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `achievementType` | `System.Type` |  |

**Returns:** `System.Collections.Generic.List&lt;T&gt;&lt;System.Type&gt;`

### `GetValidAgentDestination_Closest(Vector3, Vector3)`

Returns a point that is pathable from start position that is the closest to the end point.

```csharp
public static Vector3 GetValidAgentDestination_Closest(Vector3 start, Vector3 end)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `start` | `UnityEngine.Vector3` |  |
| `end` | `UnityEngine.Vector3` |  |

**Returns:** `UnityEngine.Vector3`

### `GetValidAgentDestination_LinearSweep(Vector3, Vector3)`

Returns a point that is pathable from start position, sweeping linearly across two points.

```csharp
public static Vector3 GetValidAgentDestination_LinearSweep(Vector3 start, Vector3 end)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `start` | `UnityEngine.Vector3` |  |
| `end` | `UnityEngine.Vector3` |  |

**Returns:** `UnityEngine.Vector3`

### `GetValidAgentPosition(Vector3, float)`

```csharp
public static Vector3 GetValidAgentPosition(Vector3 pos, float threshold = 10)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `pos` | `UnityEngine.Vector3` |  |
| `threshold` | `float` |  |

**Returns:** `UnityEngine.Vector3`

### `Helper_GetInstanceOfActor&lt;T&gt;(ref T)`

This is a helper function for instance / softInstance management of actors.

```csharp
public static T Helper_GetInstanceOfActor<T>(ref T softInstance) where T : Actor
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `softInstance` | `T` |  |
| `` | `T` |  |

**Returns:** `T`

### `InitAllTypeReferences()`

```csharp
[RuntimeInitializeOnLoadMethod(RuntimeInitializeLoadType.AfterAssembliesLoaded)]
public static void InitAllTypeReferences()
```

### `InstantiateActor_Imp&lt;T&gt;(T, Vector3, Quaternion?, Actor)`

```csharp
public static T InstantiateActor_Imp<T>(T prefab, Vector3 position, Quaternion? rotation, Actor parent) where T : Actor
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `prefab` | `T` |  |
| `position` | `UnityEngine.Vector3` |  |
| `rotation` | `UnityEngine.Quaternion?` |  |
| `parent` | [Actor](/api/Global.Actor) |  |
| `` | `T` |  |

**Returns:** `T`

### `InstantiateAndSpawn&lt;T&gt;(T, Action&lt;T&gt;)`

```csharp
public static T InstantiateAndSpawn<T>(T prefab, Action<T> beforeSpawn = null) where T : Component
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `prefab` | `T` |  |
| `beforeSpawn` | `System.Action&lt;T&gt;&lt;T&gt;` |  |
| `` | `T` |  |

**Returns:** `T`

### `InstantiateAndSpawn&lt;T&gt;(T, Vector3, Quaternion?, Action&lt;T&gt;)`

```csharp
public static T InstantiateAndSpawn<T>(T prefab, Vector3 position, Quaternion? rotation, Action<T> beforeSpawn = null) where T : Component
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `prefab` | `T` |  |
| `position` | `UnityEngine.Vector3` |  |
| `rotation` | `UnityEngine.Quaternion?` |  |
| `beforeSpawn` | `System.Action&lt;T&gt;&lt;T&gt;` |  |
| `` | `T` |  |

**Returns:** `T`

### `InstantiateAndSpawn&lt;T&gt;(Action&lt;T&gt;)`

```csharp
public static T InstantiateAndSpawn<T>(Action<T> beforeSpawn = null) where T : Component
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `beforeSpawn` | `System.Action&lt;T&gt;&lt;T&gt;` |  |
| `` | `T` |  |

**Returns:** `T`

### `InstantiateAndSpawn&lt;T&gt;(Vector3, Quaternion?, Action&lt;T&gt;)`

```csharp
public static T InstantiateAndSpawn<T>(Vector3 position, Quaternion? rotation, Action<T> beforeSpawn = null) where T : Component
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `position` | `UnityEngine.Vector3` |  |
| `rotation` | `UnityEngine.Quaternion?` |  |
| `beforeSpawn` | `System.Action&lt;T&gt;&lt;T&gt;` |  |
| `` | `T` |  |

**Returns:** `T`

### `IntToRoman(int)`

```csharp
public static string IntToRoman(int num)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `num` | `int` |  |

**Returns:** `string`

### `IsAccessoryIncludedInGame(string)`

```csharp
public static bool IsAccessoryIncludedInGame(string type)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `type` | `string` |  |

**Returns:** `bool`

### `IsAchievementIncludedInGame(string)`

```csharp
public static bool IsAchievementIncludedInGame(string typeStr)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `typeStr` | `string` |  |

**Returns:** `bool`

### `IsAnyActorBeingDestroyed()`

```csharp
public static bool IsAnyActorBeingDestroyed()
```

**Returns:** `bool`

### `IsArtifactIncludedInGame(string)`

```csharp
public static bool IsArtifactIncludedInGame(string type)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `type` | `string` |  |

**Returns:** `bool`

### `IsBeingDestroyed(GameObject)`

```csharp
public static bool IsBeingDestroyed(GameObject gameObject)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `gameObject` | `UnityEngine.GameObject` |  |

**Returns:** `bool`

### `IsChristmas()`

```csharp
public static bool IsChristmas()
```

**Returns:** `bool`

### `IsCurseIncludedInGame(string)`

```csharp
public static bool IsCurseIncludedInGame(string type)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `type` | `string` |  |

**Returns:** `bool`

### `IsDejavuFree(string)`

```csharp
public static bool IsDejavuFree(string typeName)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `typeName` | `string` |  |

**Returns:** `bool`

### `IsDejavuFree(Object)`

```csharp
public static bool IsDejavuFree(Object target)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `target` | `UnityEngine.Object` |  |

**Returns:** `bool`

### `IsEmoteIncludedInGame(string)`

```csharp
public static bool IsEmoteIncludedInGame(string type)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `type` | `string` |  |

**Returns:** `bool`

### `IsExcludedFromPool(string)`

```csharp
public static bool IsExcludedFromPool(string type)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `type` | `string` |  |

**Returns:** `bool`

### `IsGameModifierIncludedInGame(string)`

```csharp
public static bool IsGameModifierIncludedInGame(string type)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `type` | `string` |  |

**Returns:** `bool`

### `IsGemIncludedInGame(string)`

```csharp
public static bool IsGemIncludedInGame(string type)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `type` | `string` |  |

**Returns:** `bool`

### `IsHeroIncludedInGame(string)`

```csharp
public static bool IsHeroIncludedInGame(string type)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `type` | `string` |  |

**Returns:** `bool`

### `IsLucidDreamIncludedInGame(string)`

```csharp
public static bool IsLucidDreamIncludedInGame(string type)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `type` | `string` |  |

**Returns:** `bool`

### `IsMeleeHero(HeroClassType)`

```csharp
public static bool IsMeleeHero(Hero.HeroClassType type)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `type` | [Hero.HeroClassType](/api/Global.Hero) |  |

**Returns:** `bool`

### `IsMonsterIncludedInGame(string)`

```csharp
public static bool IsMonsterIncludedInGame(string type)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `type` | `string` |  |

**Returns:** `bool`

### `IsNametagIncludedInGame(string)`

```csharp
public static bool IsNametagIncludedInGame(string type)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `type` | `string` |  |

**Returns:** `bool`

### `IsNearChristmas()`

```csharp
public static bool IsNearChristmas()
```

**Returns:** `bool`

### `IsNotPlayableOnTop(Vector3)`

```csharp
public static bool IsNotPlayableOnTop(Vector3 pos)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `pos` | `UnityEngine.Vector3` |  |

**Returns:** `bool`

### `IsOkay(Displacement)`

Check floating values if they're not infinity nor NaNs.This will print out exceptions for getting stack traces in Cloud Diagnostics.

```csharp
public static bool IsOkay(Displacement d)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `d` | [Displacement](/api/Global.Displacement) |  |

**Returns:** `bool`

### `IsOkay(double)`

Check floating values if they're not infinity nor NaNs.This will print out exceptions for getting stack traces in Cloud Diagnostics.

```csharp
public static bool IsOkay(double d)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `d` | `double` |  |

**Returns:** `bool`

### `IsOkay(float)`

Check floating values if they're not infinity nor NaNs.This will print out exceptions for getting stack traces in Cloud Diagnostics.

```csharp
public static bool IsOkay(float f)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `f` | `float` |  |

**Returns:** `bool`

### `IsOkay(Vector2)`

Check floating values if they're not infinity nor NaNs.This will print out exceptions for getting stack traces in Cloud Diagnostics.

```csharp
public static bool IsOkay(Vector2 v)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `v` | `UnityEngine.Vector2` |  |

**Returns:** `bool`

### `IsOkay(Vector3)`

Check floating values if they're not infinity nor NaNs.This will print out exceptions for getting stack traces in Cloud Diagnostics.

```csharp
public static bool IsOkay(Vector3 v)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `v` | `UnityEngine.Vector3` |  |

**Returns:** `bool`

### `IsOkay(Vector4)`

Check floating values if they're not infinity nor NaNs.This will print out exceptions for getting stack traces in Cloud Diagnostics.

```csharp
public static bool IsOkay(Vector4 v)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `v` | `UnityEngine.Vector4` |  |

**Returns:** `bool`

### `IsRangedHero(HeroClassType)`

```csharp
public static bool IsRangedHero(Hero.HeroClassType type)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `type` | [Hero.HeroClassType](/api/Global.Hero) |  |

**Returns:** `bool`

### `IsRoomModifierIncludedInGame(string)`

```csharp
public static bool IsRoomModifierIncludedInGame(string type)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `type` | `string` |  |

**Returns:** `bool`

### `IsSkillIncludedInGame(string)`

```csharp
public static bool IsSkillIncludedInGame(string type)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `type` | `string` |  |

**Returns:** `bool`

### `IsSkinIncludedInGame(string)`

```csharp
public static bool IsSkinIncludedInGame(string type)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `type` | `string` |  |

**Returns:** `bool`

### `IsStarIncludedInGame(string)`

```csharp
public static bool IsStarIncludedInGame(string type)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `type` | `string` |  |

**Returns:** `bool`

### `IsTreasureIncludedInGame(string)`

```csharp
public static bool IsTreasureIncludedInGame(string type)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `type` | `string` |  |

**Returns:** `bool`

### `IsZoneIncludedInGame(string)`

```csharp
public static bool IsZoneIncludedInGame(string type)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `type` | `string` |  |

**Returns:** `bool`

### `NicifyVariableName(string)`

Converts a variable name string into a human-readable label.
Example: "helloThere_fella" becomes "Hello There Fella".

```csharp
public static string NicifyVariableName(this string input)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `input` | `string` |  |

**Returns:** `string`

### `OpenURL(string, OpenURLSettings)`

```csharp
public static void OpenURL(string url, OpenURLSettings settings = null)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `url` | `string` |  |
| `settings` | [OpenURLSettings](/api/Global.OpenURLSettings) |  |

### `PrepareAndSpawnActor_Imp&lt;T&gt;(T, Action&lt;T&gt;)`

```csharp
public static T PrepareAndSpawnActor_Imp<T>(T newActor, Action<T> beforePrepare) where T : Actor
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `newActor` | `T` |  |
| `beforePrepare` | `System.Action&lt;T&gt;&lt;T&gt;` |  |
| `` | `T` |  |

**Returns:** `T`

### `PrepareAndSpawnHero_Imp&lt;T&gt;(T, DewPlayer, int, HeroLoadoutData, string, Action&lt;T&gt;)`

```csharp
public static T PrepareAndSpawnHero_Imp<T>(T newEntity, DewPlayer owner, int level, HeroLoadoutData loadout, string skin, Action<T> beforePrepare) where T : Hero
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `newEntity` | `T` |  |
| `owner` | [DewPlayer](/api/Global.DewPlayer) |  |
| `level` | `int` |  |
| `loadout` | [HeroLoadoutData](/api/Global.HeroLoadoutData) |  |
| `skin` | `string` |  |
| `beforePrepare` | `System.Action&lt;T&gt;&lt;T&gt;` |  |
| `` | `T` |  |

**Returns:** `T`

### `PrepareAndSpawnStatusEffect_Imp&lt;T&gt;(T, Entity, Actor, CastInfo, Action&lt;T&gt;)`

```csharp
public static T PrepareAndSpawnStatusEffect_Imp<T>(T newSe, Entity victim, Actor parent, CastInfo info, Action<T> beforePrepare) where T : StatusEffect
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `newSe` | `T` |  |
| `victim` | [Entity](/api/Global.Entity) |  |
| `parent` | [Actor](/api/Global.Actor) |  |
| `info` | [CastInfo](/api/Global.CastInfo) |  |
| `beforePrepare` | `System.Action&lt;T&gt;&lt;T&gt;` |  |
| `` | `T` |  |

**Returns:** `T`

### `QuitApplication(bool)`

```csharp
public static void QuitApplication(bool dontSave = false)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `dontSave` | `bool` |  |

### `RaycastAllUIElementsBelowCursor(out ListReturnHandle&lt;RaycastResult&gt;)`

```csharp
public static List<RaycastResult> RaycastAllUIElementsBelowCursor(out ListReturnHandle<RaycastResult> handle)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `handle` | `ListReturnHandle&lt;RaycastResult&gt;` |  |

**Returns:** `System.Collections.Generic.List&lt;T&gt;&lt;RaycastResult&gt;`

### `RaycastAllUIElementsBelowCursor(List&lt;RaycastResult&gt;)`

```csharp
public static void RaycastAllUIElementsBelowCursor(List<RaycastResult> results)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `results` | `System.Collections.Generic.List&lt;T&gt;&lt;RaycastResult&gt;` |  |

### `RaycastAllUIElementsBelowScreenPoint(Vector2, out ListReturnHandle&lt;RaycastResult&gt;)`

```csharp
public static List<RaycastResult> RaycastAllUIElementsBelowScreenPoint(Vector2 screenPoint, out ListReturnHandle<RaycastResult> handle)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `screenPoint` | `UnityEngine.Vector2` |  |
| `handle` | `ListReturnHandle&lt;RaycastResult&gt;` |  |

**Returns:** `System.Collections.Generic.List&lt;T&gt;&lt;RaycastResult&gt;`

### `RaycastAllUIElementsBelowScreenPoint(Vector2, List&lt;RaycastResult&gt;)`

```csharp
public static void RaycastAllUIElementsBelowScreenPoint(Vector2 screenPoint, List<RaycastResult> results)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `screenPoint` | `UnityEngine.Vector2` |  |
| `results` | `System.Collections.Generic.List&lt;T&gt;&lt;RaycastResult&gt;` |  |

### `RefreshRenderer()`

```csharp
public static void RefreshRenderer()
```

### `RemoveData(IDictionary&lt;string, string&gt;, string, string, string)`

```csharp
public static bool RemoveData(this IDictionary<string, string> dict, string key0, string key1, string key2)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `dict` | `System.Collections.Generic.IDictionary&lt;TKey, TValue&gt;&lt;string,string&gt;` |  |
| `key0` | `string` |  |
| `key1` | `string` |  |
| `key2` | `string` |  |

**Returns:** `bool`

### `RemoveData(IDictionary&lt;string, string&gt;, string, string)`

```csharp
public static bool RemoveData(this IDictionary<string, string> dict, string key0, string key1)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `dict` | `System.Collections.Generic.IDictionary&lt;TKey, TValue&gt;&lt;string,string&gt;` |  |
| `key0` | `string` |  |
| `key1` | `string` |  |

**Returns:** `bool`

### `RemoveData(IDictionary&lt;string, string&gt;, string)`

```csharp
public static bool RemoveData(this IDictionary<string, string> dict, string key0)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `dict` | `System.Collections.Generic.IDictionary&lt;TKey, TValue&gt;&lt;string,string&gt;` |  |
| `key0` | `string` |  |

**Returns:** `bool`

### `ResolveLocalizedFormatArgs(string[])`

```csharp
public static void ResolveLocalizedFormatArgs(string[] localizedFormatArgs)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `localizedFormatArgs` | `string[]` |  |

### `SelectBestIndexWithScore&lt;T&gt;(IList&lt;T&gt;, Func&lt;T, int, float&gt;, float, DewRandom)`

Item with best score will be returned. If fuzziness is set, score will be multiplied by a random value between (1+fuzziness) ~ (1-fuzziness)

```csharp
public static int SelectBestIndexWithScore<T>(IList<T> list, Func<T, int, float> scoreFunc, float fuzziness = 0, DewRandom random = null)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `list` | `System.Collections.Generic.IList&lt;T&gt;&lt;T&gt;` |  |
| `scoreFunc` | `System.Func&lt;T1, T2, TResult&gt;&lt;T,int,float&gt;` |  |
| `fuzziness` | `float` |  |
| `random` | [DewRandom](/api/Global.DewRandom) |  |
| `` | `T` |  |

**Returns:** `int`

### `SelectBestIndexWithScore&lt;T&gt;(ReadOnlySpan&lt;T&gt;, Func&lt;T, int, float&gt;, float, DewRandom)`

Item with best score will be returned. If fuzziness is set, score will be multiplied by a random value between (1+fuzziness) ~ (1-fuzziness)

```csharp
public static int SelectBestIndexWithScore<T>(ReadOnlySpan<T> list, Func<T, int, float> scoreFunc, float fuzziness = 0, DewRandom random = null)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `list` | `System.ReadOnlySpan&lt;T&gt;&lt;T&gt;` |  |
| `scoreFunc` | `System.Func&lt;T1, T2, TResult&gt;&lt;T,int,float&gt;` |  |
| `fuzziness` | `float` |  |
| `random` | [DewRandom](/api/Global.DewRandom) |  |
| `` | `T` |  |

**Returns:** `int`

### `SelectBestWithScore&lt;T&gt;(HashSet&lt;T&gt;, Func&lt;T, float&gt;, float, DewRandom)`

Item with best score will be returned. If fuzziness is set, score will be multiplied by a random value between (1+fuzziness) ~ (1-fuzziness)

```csharp
public static T SelectBestWithScore<T>(HashSet<T> list, Func<T, float> scoreFunc, float fuzziness = 0, DewRandom random = null)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `list` | `System.Collections.Generic.HashSet&lt;T&gt;&lt;T&gt;` |  |
| `scoreFunc` | `System.Func&lt;T, TResult&gt;&lt;T,float&gt;` |  |
| `fuzziness` | `float` |  |
| `random` | [DewRandom](/api/Global.DewRandom) |  |
| `` | `T` |  |

**Returns:** `T`

### `SelectBestWithScore&lt;T&gt;(IList&lt;T&gt;, Func&lt;T, int, float&gt;, float, DewRandom)`

Item with best score will be returned. If fuzziness is set, score will be multiplied by a random value between (1+fuzziness) ~ (1-fuzziness)

```csharp
public static T SelectBestWithScore<T>(IList<T> list, Func<T, int, float> scoreFunc, float fuzziness = 0, DewRandom random = null)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `list` | `System.Collections.Generic.IList&lt;T&gt;&lt;T&gt;` |  |
| `scoreFunc` | `System.Func&lt;T1, T2, TResult&gt;&lt;T,int,float&gt;` |  |
| `fuzziness` | `float` |  |
| `random` | [DewRandom](/api/Global.DewRandom) |  |
| `` | `T` |  |

**Returns:** `T`

### `SelectBestWithScore&lt;T&gt;(ReadOnlySpan&lt;T&gt;, Func&lt;T, int, float&gt;, float, DewRandom)`

Item with best score will be returned. If fuzziness is set, score will be multiplied by a random value between (1+fuzziness) ~ (1-fuzziness)

```csharp
public static T SelectBestWithScore<T>(ReadOnlySpan<T> list, Func<T, int, float> scoreFunc, float fuzziness = 0, DewRandom random = null)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `list` | `System.ReadOnlySpan&lt;T&gt;&lt;T&gt;` |  |
| `scoreFunc` | `System.Func&lt;T1, T2, TResult&gt;&lt;T,int,float&gt;` |  |
| `fuzziness` | `float` |  |
| `random` | [DewRandom](/api/Global.DewRandom) |  |
| `` | `T` |  |

**Returns:** `T`

### `SelectRandomAliveHero(bool)`

```csharp
public static Hero SelectRandomAliveHero(bool fallbackToDead = true)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `fallbackToDead` | `bool` |  |

**Returns:** `Hero`

### `SelectRandomWeightedIndexInParams(params float[])`

```csharp
public static int SelectRandomWeightedIndexInParams(params float[] weights)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `weights` | `float[]` |  |

**Returns:** `int`

### `SelectRandomWeightedInList&lt;T&gt;(IList&lt;T&gt;, Func&lt;T, float&gt;, DewRandom)`

```csharp
public static T SelectRandomWeightedInList<T>(IList<T> list, Func<T, float> weightGetter, DewRandom random = null)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `list` | `System.Collections.Generic.IList&lt;T&gt;&lt;T&gt;` |  |
| `weightGetter` | `System.Func&lt;T, TResult&gt;&lt;T,float&gt;` |  |
| `random` | [DewRandom](/api/Global.DewRandom) |  |
| `` | `T` |  |

**Returns:** `T`

### `SelectRandomWeightedInList&lt;T&gt;(ReadOnlySpan&lt;T&gt;, Func&lt;T, float&gt;)`

```csharp
public static T SelectRandomWeightedInList<T>(ReadOnlySpan<T> list, Func<T, float> weightGetter)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `list` | `System.ReadOnlySpan&lt;T&gt;&lt;T&gt;` |  |
| `weightGetter` | `System.Func&lt;T, TResult&gt;&lt;T,float&gt;` |  |
| `` | `T` |  |

**Returns:** `T`

### `SelectRandomWeightedInParams&lt;T&gt;(params (float, T)[])`

```csharp
public static T SelectRandomWeightedInParams<T>(params (float, T)[] elements)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `elements` | `(float, T)[]` |  |
| `` | `T` |  |

**Returns:** `T`

### `SelectRandomWeightedInReadOnlyList&lt;T&gt;(IReadOnlyList&lt;T&gt;, Func&lt;T, float&gt;)`

Without the postfix, you won't be able to feed in Lists because of ambiguity.

```csharp
public static T SelectRandomWeightedInReadOnlyList<T>(IReadOnlyList<T> list, Func<T, float> weightGetter)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `list` | `System.Collections.Generic.IReadOnlyList&lt;T&gt;&lt;T&gt;` |  |
| `weightGetter` | `System.Func&lt;T, TResult&gt;&lt;T,float&gt;` |  |
| `` | `T` |  |

**Returns:** `T`

### `SetData&lt;T&gt;(IDictionary&lt;string, string&gt;, string, T)`

```csharp
public static void SetData<T>(this IDictionary<string, string> dict, string key0, T value)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `dict` | `System.Collections.Generic.IDictionary&lt;TKey, TValue&gt;&lt;string,string&gt;` |  |
| `key0` | `string` |  |
| `value` | `T` |  |
| `` | `T` |  |

### `SetData&lt;T&gt;(IDictionary&lt;string, string&gt;, string, string, T)`

```csharp
public static void SetData<T>(this IDictionary<string, string> dict, string key0, string key1, T value)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `dict` | `System.Collections.Generic.IDictionary&lt;TKey, TValue&gt;&lt;string,string&gt;` |  |
| `key0` | `string` |  |
| `key1` | `string` |  |
| `value` | `T` |  |
| `` | `T` |  |

### `SetData&lt;T&gt;(IDictionary&lt;string, string&gt;, string, string, string, T)`

```csharp
public static void SetData<T>(this IDictionary<string, string> dict, string key0, string key1, string key2, T value)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `dict` | `System.Collections.Generic.IDictionary&lt;TKey, TValue&gt;&lt;string,string&gt;` |  |
| `key0` | `string` |  |
| `key1` | `string` |  |
| `key2` | `string` |  |
| `value` | `T` |  |
| `` | `T` |  |

### `SetUnscaledTimeUpdate(GameObject)`

```csharp
public static void SetUnscaledTimeUpdate(GameObject gobj)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `gobj` | `UnityEngine.GameObject` |  |

### `ShowJsonWithEditor(string)`

```csharp
public static void ShowJsonWithEditor(string json)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `json` | `string` |  |

### `SpawnEntity&lt;T&gt;(T, Vector3, Quaternion?, Actor, DewPlayer, int, Action&lt;T&gt;)`

```csharp
public static T SpawnEntity<T>(T entity, Vector3 position, Quaternion? rotation, Actor parent, DewPlayer owner, int level, Action<T> beforeSpawn = null) where T : Entity
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `entity` | `T` |  |
| `position` | `UnityEngine.Vector3` |  |
| `rotation` | `UnityEngine.Quaternion?` |  |
| `parent` | [Actor](/api/Global.Actor) |  |
| `owner` | [DewPlayer](/api/Global.DewPlayer) |  |
| `level` | `int` |  |
| `beforeSpawn` | `System.Action&lt;T&gt;&lt;T&gt;` |  |
| `` | `T` |  |

**Returns:** `T`

### `SpawnEntity&lt;T&gt;(Vector3, Quaternion?, Actor, DewPlayer, int, Action&lt;T&gt;)`

```csharp
public static T SpawnEntity<T>(Vector3 position, Quaternion? rotation, Actor parent, DewPlayer owner, int level, Action<T> beforeSpawn = null) where T : Entity
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `position` | `UnityEngine.Vector3` |  |
| `rotation` | `UnityEngine.Quaternion?` |  |
| `parent` | [Actor](/api/Global.Actor) |  |
| `owner` | [DewPlayer](/api/Global.DewPlayer) |  |
| `level` | `int` |  |
| `beforeSpawn` | `System.Action&lt;T&gt;&lt;T&gt;` |  |
| `` | `T` |  |

**Returns:** `T`

### `SpawnHero&lt;T&gt;(T, Vector3, Quaternion?, DewPlayer, int, HeroLoadoutData, string, Action&lt;T&gt;)`

```csharp
public static T SpawnHero<T>(T hero, Vector3 position, Quaternion? rotation, DewPlayer owner, int level, HeroLoadoutData loadout, string skin, Action<T> beforeSpawn = null) where T : Hero
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `hero` | `T` |  |
| `position` | `UnityEngine.Vector3` |  |
| `rotation` | `UnityEngine.Quaternion?` |  |
| `owner` | [DewPlayer](/api/Global.DewPlayer) |  |
| `level` | `int` |  |
| `loadout` | [HeroLoadoutData](/api/Global.HeroLoadoutData) |  |
| `skin` | `string` |  |
| `beforeSpawn` | `System.Action&lt;T&gt;&lt;T&gt;` |  |
| `` | `T` |  |

**Returns:** `T`

### `SpawnHero&lt;T&gt;(Vector3, Quaternion?, DewPlayer, int, HeroLoadoutData, string, Action&lt;T&gt;)`

```csharp
public static T SpawnHero<T>(Vector3 position, Quaternion? rotation, DewPlayer owner, int level, HeroLoadoutData loadout, string skin, Action<T> beforeSpawn = null) where T : Hero
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `position` | `UnityEngine.Vector3` |  |
| `rotation` | `UnityEngine.Quaternion?` |  |
| `owner` | [DewPlayer](/api/Global.DewPlayer) |  |
| `level` | `int` |  |
| `loadout` | [HeroLoadoutData](/api/Global.HeroLoadoutData) |  |
| `skin` | `string` |  |
| `beforeSpawn` | `System.Action&lt;T&gt;&lt;T&gt;` |  |
| `` | `T` |  |

**Returns:** `T`

### `TryGetData&lt;T&gt;(IDictionary&lt;string, string&gt;, string, out T)`

```csharp
public static bool TryGetData<T>(this IDictionary<string, string> dict, string key0, out T value)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `dict` | `System.Collections.Generic.IDictionary&lt;TKey, TValue&gt;&lt;string,string&gt;` |  |
| `key0` | `string` |  |
| `value` | `T` |  |
| `` | `T` |  |

**Returns:** `bool`

### `TryGetData&lt;T&gt;(IDictionary&lt;string, string&gt;, string, string, out T)`

```csharp
public static bool TryGetData<T>(this IDictionary<string, string> dict, string key0, string key1, out T value)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `dict` | `System.Collections.Generic.IDictionary&lt;TKey, TValue&gt;&lt;string,string&gt;` |  |
| `key0` | `string` |  |
| `key1` | `string` |  |
| `value` | `T` |  |
| `` | `T` |  |

**Returns:** `bool`

### `TryGetData&lt;T&gt;(IDictionary&lt;string, string&gt;, string, string, string, out T)`

```csharp
public static bool TryGetData<T>(this IDictionary<string, string> dict, string key0, string key1, string key2, out T value)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `dict` | `System.Collections.Generic.IDictionary&lt;TKey, TValue&gt;&lt;string,string&gt;` |  |
| `key0` | `string` |  |
| `key1` | `string` |  |
| `key2` | `string` |  |
| `value` | `T` |  |
| `` | `T` |  |

**Returns:** `bool`

### `TryGetTypeFromShortName(string, out Type)`

```csharp
public static bool TryGetTypeFromShortName(string typeName, out Type type)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `typeName` | `string` |  |
| `type` | `System.Type` |  |

**Returns:** `bool`

### `WaitForAggroedEnemiesRoutine()`

Wait until no enemies aggroed to any player exists.

```csharp
public static IEnumerator WaitForAggroedEnemiesRoutine()
```

**Returns:** `System.Collections.IEnumerator`

### `WaitForClientsReadyRoutine(List&lt;DewPlayer&gt;)`

Wait until all connections are ready.

```csharp
public static IEnumerator WaitForClientsReadyRoutine(List<DewPlayer> players = null)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `players` | [System.Collections.Generic.List&lt;T&gt;&lt;DewPlayer&gt;](/api/Global.DewPlayer) |  |

**Returns:** `System.Collections.IEnumerator`
