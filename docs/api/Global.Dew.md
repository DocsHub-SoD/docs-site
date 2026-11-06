# Class: Dew

- **Category:** <span class="cat-dot" style="--cat-color: #ef4444" data-cat="Combat & Abilities"></span> Combat & Abilities
- **Namespace:** `Global`
- **Assembly:** `Dew.Core.dll`

```csharp
public static class Dew
```

## Fields (26)

::: details Click to expand Fields (26)

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
| **`HeroOrder`** | `public static readonly List<string> HeroOrder` |  |
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

:::

## Properties (20)

::: details Click to expand Properties (20)

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`achievementsByName`** | `public static IReadOnlyDictionary<string, Type> achievementsByName { get; }` |  |
| **`allAchievements`** | `public static IReadOnlyList<Type> allAchievements { get; }` |  |
| **`allArtifacts`** | `public static IReadOnlyList<Type> allArtifacts { get; }` |  |
| **`allGameModifiers`** | `public static IReadOnlyList<Type> allGameModifiers { get; }` |  |
| **`allGems`** | `public static IReadOnlyList<Type> allGems { get; }` |  |
| **`allHeroes`** | `public static IReadOnlyList<Type> allHeroes { get; }` |  |
| **`allHeroSkills`** | `public static IReadOnlyList<Type> allHeroSkills { get; }` |  |
| **`allLucidDreams`** | `public static IReadOnlyList<Type> allLucidDreams { get; }` |  |
| **`allMonsters`** | `public static IReadOnlyList<Type> allMonsters { get; }` |  |
| **`allOldStars`** | `public static IReadOnlyList<DewStarItemOld> allOldStars { get; }` |  |
| **`allReveries`** | `public static IReadOnlyList<DewReverieItem> allReveries { get; }` |  |
| **`allRoomModifiers`** | `public static IReadOnlyList<Type> allRoomModifiers { get; }` |  |
| **`allSkills`** | `public static IReadOnlyList<Type> allSkills { get; }` |  |
| **`allStarTypes`** | `public static IReadOnlyList<Type> allStarTypes { get; }` |  |
| **`allTutorialItems`** | `public static IReadOnlyList<Type> allTutorialItems { get; }` |  |
| **`gameCanvas`** | `public static Canvas gameCanvas { get; }` |  |
| **`heroTypeOfOldStar`** | `public static IReadOnlyDictionary<DewStarItemOld, Type> heroTypeOfOldStar { get; }` | Contains all stars. Non-hero stars will have value of null. |
| **`mainCamera`** | `public static Camera mainCamera { get; }` |  |
| **`resourceLinkTypes`** | `public static IReadOnlyList<(Type, DewResourceLinkAttribute)> resourceLinkTypes { get; }` |  |
| **`reveriesByName`** | `public static IReadOnlyDictionary<string, DewReverieItem> reveriesByName { get; }` |  |

:::

## Methods (168)

::: details `CallDelayed(Action, int)`

Call a function delayed by one frame.

```csharp
public static void CallDelayed(Action func, int frameCount = 1)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `func` | `System.Action` |  |
| `frameCount` | `int` |  |

:::

::: details `CallOnReady(MonoBehaviour, Func&lt;bool&gt;, Action)`

```csharp
public static void CallOnReady(MonoBehaviour caller, Func<bool> condition, Action func)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `caller` | `UnityEngine.MonoBehaviour` |  |
| `condition` | `System.Func<TResult><bool>` |  |
| `func` | `System.Action` |  |

:::

::: details `ClearTypeReferences()`

```csharp
public static void ClearTypeReferences()
```

:::

::: details `ContainsData(IDictionary&lt;string, string&gt;, string, string, string)`

```csharp
public static bool ContainsData(this IDictionary<string, string> dict, string key0, string key1, string key2)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `dict` | `System.Collections.Generic.IDictionary<TKey, TValue><string,string>` |  |
| `key0` | `string` |  |
| `key1` | `string` |  |
| `key2` | `string` |  |

**Returns:** `bool`

:::

::: details `ContainsData(IDictionary&lt;string, string&gt;, string, string)`

```csharp
public static bool ContainsData(this IDictionary<string, string> dict, string key0, string key1)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `dict` | `System.Collections.Generic.IDictionary<TKey, TValue><string,string>` |  |
| `key0` | `string` |  |
| `key1` | `string` |  |

**Returns:** `bool`

:::

::: details `ContainsData(IDictionary&lt;string, string&gt;, string)`

```csharp
public static bool ContainsData(this IDictionary<string, string> dict, string key0)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `dict` | `System.Collections.Generic.IDictionary<TKey, TValue><string,string>` |  |
| `key0` | `string` |  |

**Returns:** `bool`

:::

::: details `ConvertToStringInvariantCulture(object)`

```csharp
public static string ConvertToStringInvariantCulture(object value)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `value` | `object` |  |

**Returns:** `string`

:::

::: details `CreateAbilityInstance&lt;T&gt;(T, Vector3, Quaternion?, Actor, CastInfo, Action&lt;T&gt;)`

```csharp
public static T CreateAbilityInstance<T>(T prefab, Vector3 position, Quaternion? rotation, Actor parent, CastInfo info, Action<T> beforePrepare = null) where T : AbilityInstance
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `prefab` | `T` |  |
| `position` | `UnityEngine.Vector3` |  |
| `rotation` | `UnityEngine.Quaternion?` |  |
| `parent` | [`Actor`](/api/Global.Actor) |  |
| `info` | [`CastInfo`](/api/Global.CastInfo) |  |
| `beforePrepare` | `System.Action<T>` |  |
| `` | `T` |  |

**Returns:** `T`

:::

::: details `CreateAbilityInstance&lt;T&gt;(Vector3, Quaternion?, Actor, CastInfo, Action&lt;T&gt;)`

```csharp
public static T CreateAbilityInstance<T>(Vector3 position, Quaternion? rotation, Actor parent, CastInfo info, Action<T> beforePrepare = null) where T : AbilityInstance
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `position` | `UnityEngine.Vector3` |  |
| `rotation` | `UnityEngine.Quaternion?` |  |
| `parent` | [`Actor`](/api/Global.Actor) |  |
| `info` | [`CastInfo`](/api/Global.CastInfo) |  |
| `beforePrepare` | `System.Action<T>` |  |
| `` | `T` |  |

**Returns:** `T`

:::

::: details `CreateAbilityTrigger&lt;T&gt;(T, Action&lt;T&gt;)`

```csharp
public static T CreateAbilityTrigger<T>(T trigger, Action<T> beforePrepare = null) where T : AbilityTrigger
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `trigger` | `T` |  |
| `beforePrepare` | `System.Action<T>` |  |
| `` | `T` |  |

**Returns:** `T`

:::

::: details `CreateAbilityTrigger&lt;T&gt;(Action&lt;T&gt;)`

```csharp
public static T CreateAbilityTrigger<T>(Action<T> beforeSpawn = null) where T : AbilityTrigger
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `beforeSpawn` | `System.Action<T>` |  |
| `` | `T` |  |

**Returns:** `T`

:::

::: details `CreateActor&lt;T&gt;()`

```csharp
public static T CreateActor<T>() where T : Actor
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `` | `T` |  |

**Returns:** `T`

:::

::: details `CreateActor&lt;T&gt;(T, Vector3, Quaternion?, Actor, Action&lt;T&gt;)`

```csharp
public static T CreateActor<T>(T prefab, Vector3 position, Quaternion? rotation, Actor parent = null, Action<T> beforePrepare = null) where T : Actor
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `prefab` | `T` |  |
| `position` | `UnityEngine.Vector3` |  |
| `rotation` | `UnityEngine.Quaternion?` |  |
| `parent` | [`Actor`](/api/Global.Actor) |  |
| `beforePrepare` | `System.Action<T>` |  |
| `` | `T` |  |

**Returns:** `T`

:::

::: details `CreateActor&lt;T&gt;(Action&lt;T&gt;)`

```csharp
public static T CreateActor<T>(Action<T> beforePrepare = null) where T : Actor
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `beforePrepare` | `System.Action<T>` |  |
| `` | `T` |  |

**Returns:** `T`

:::

::: details `CreateActor&lt;T&gt;(Vector3, Quaternion?, Actor, Action&lt;T&gt;)`

```csharp
public static T CreateActor<T>(Vector3 position, Quaternion? rotation, Actor parent = null, Action<T> beforePrepare = null) where T : Actor
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `position` | `UnityEngine.Vector3` |  |
| `rotation` | `UnityEngine.Quaternion?` |  |
| `parent` | [`Actor`](/api/Global.Actor) |  |
| `beforePrepare` | `System.Action<T>` |  |
| `` | `T` |  |

**Returns:** `T`

:::

::: details `CreateGem&lt;T&gt;(T, Vector3, int, DewPlayer, Action&lt;T&gt;)`

```csharp
public static T CreateGem<T>(T gem, Vector3 position, int quality, DewPlayer tempOwner = null, Action<T> beforePrepare = null) where T : Gem
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `gem` | `T` |  |
| `position` | `UnityEngine.Vector3` |  |
| `quality` | `int` |  |
| `tempOwner` | [`DewPlayer`](/api/Global.DewPlayer) |  |
| `beforePrepare` | `System.Action<T>` |  |
| `` | `T` |  |

**Returns:** `T`

:::

::: details `CreateGem&lt;T&gt;(Vector3, int, DewPlayer, Action&lt;T&gt;)`

```csharp
public static T CreateGem<T>(Vector3 position, int quality, DewPlayer tempOwner = null, Action<T> beforePrepare = null) where T : Gem
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `position` | `UnityEngine.Vector3` |  |
| `quality` | `int` |  |
| `tempOwner` | [`DewPlayer`](/api/Global.DewPlayer) |  |
| `beforePrepare` | `System.Action<T>` |  |
| `` | `T` |  |

**Returns:** `T`

:::

::: details `CreateSkillTrigger&lt;T&gt;(T, Vector3, int, DewPlayer, Action&lt;T&gt;)`

```csharp
public static T CreateSkillTrigger<T>(T trigger, Vector3 position, int level, DewPlayer tempOwner = null, Action<T> beforePrepare = null) where T : SkillTrigger
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `trigger` | `T` |  |
| `position` | `UnityEngine.Vector3` |  |
| `level` | `int` |  |
| `tempOwner` | [`DewPlayer`](/api/Global.DewPlayer) |  |
| `beforePrepare` | `System.Action<T>` |  |
| `` | `T` |  |

**Returns:** `T`

:::

::: details `CreateSkillTrigger&lt;T&gt;(Vector3, int, DewPlayer, Action&lt;T&gt;)`

```csharp
public static T CreateSkillTrigger<T>(Vector3 position, int level, DewPlayer tempOwner = null, Action<T> beforePrepare = null) where T : SkillTrigger
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `position` | `UnityEngine.Vector3` |  |
| `level` | `int` |  |
| `tempOwner` | [`DewPlayer`](/api/Global.DewPlayer) |  |
| `beforePrepare` | `System.Action<T>` |  |
| `` | `T` |  |

**Returns:** `T`

:::

::: details `CreateStatusEffect&lt;T&gt;(T, Entity, Actor, CastInfo, Action&lt;T&gt;)`

Create a new status effect and attach it to an entity.This can return null if the creation fails:e.g. Trying to apply a status effect with isKilledByUnstoppable flag to an unstoppable/invulnerable entity.

```csharp
public static T CreateStatusEffect<T>(T prefab, Entity victim, Actor parent, CastInfo info, Action<T> beforePrepare = null) where T : StatusEffect
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `prefab` | `T` |  |
| `victim` | [`Entity`](/api/Global.Entity) |  |
| `parent` | [`Actor`](/api/Global.Actor) |  |
| `info` | [`CastInfo`](/api/Global.CastInfo) |  |
| `beforePrepare` | `System.Action<T>` |  |
| `` | `T` |  |

**Returns:** `T`

:::

::: details `CreateStatusEffect&lt;T&gt;(Entity, Actor, CastInfo, Action&lt;T&gt;)`

Create a new status effect and attach it to an entity.This can return null if the creation fails:e.g. Trying to apply a status effect with isKilledByUnstoppable flag to an unstoppable/invulnerable entity.

```csharp
public static T CreateStatusEffect<T>(Entity victim, Actor parent, CastInfo info, Action<T> beforePrepare = null) where T : StatusEffect
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `victim` | [`Entity`](/api/Global.Entity) |  |
| `parent` | [`Actor`](/api/Global.Actor) |  |
| `info` | [`CastInfo`](/api/Global.CastInfo) |  |
| `beforePrepare` | `System.Action<T>` |  |
| `` | `T` |  |

**Returns:** `T`

:::

::: details `Debounce(Object, float, Action, object)`

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

:::

::: details `Destroy(GameObject)`

Destroy a networked game object. Despawning and destroying will be delayed for network RPCs and cleanups.

```csharp
public static void Destroy(GameObject gameObject)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `gameObject` | `UnityEngine.GameObject` |  |

:::

::: details `FilterNonOkayValues(ref float, float)`

```csharp
public static void FilterNonOkayValues(ref float v, float fallback = 0)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `v` | `float` |  |
| `fallback` | `float` |  |

:::

::: details `FilterNonOkayValues(ref Vector2, Vector2)`

```csharp
public static void FilterNonOkayValues(ref Vector2 v, Vector2 fallback = default)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `v` | `UnityEngine.Vector2` |  |
| `fallback` | `UnityEngine.Vector2` |  |

:::

::: details `FilterNonOkayValues(ref Vector3, Vector3)`

```csharp
public static void FilterNonOkayValues(ref Vector3 v, Vector3 fallback = default)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `v` | `UnityEngine.Vector3` |  |
| `fallback` | `UnityEngine.Vector3` |  |

:::

::: details `FindActorOfType&lt;T&gt;()`

```csharp
public static T FindActorOfType<T>() where T : Actor
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `` | `T` |  |

**Returns:** `T`

:::

::: details `FindAllActorsOfType&lt;T&gt;(out ListReturnHandle&lt;T&gt;)`

```csharp
public static List<T> FindAllActorsOfType<T>(out ListReturnHandle<T> handle) where T : Actor
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `handle` | `ListReturnHandle<T>` |  |
| `` | `T` |  |

**Returns:** `System.Collections.Generic.List<T>`

:::

::: details `FindInterfaceOfType&lt;T&gt;(bool)`

```csharp
public static T FindInterfaceOfType<T>(bool includeInactive) where T : class
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `includeInactive` | `bool` |  |
| `` | `T` |  |

**Returns:** `T`

:::

::: details `FindInterfacesOfType&lt;T&gt;(bool)`

```csharp
public static T[] FindInterfacesOfType<T>(bool includeInactive) where T : class
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `includeInactive` | `bool` |  |
| `` | `T` |  |

**Returns:** `T[]`

:::

::: details `FormatBigNumbers(float, float, string)`

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

:::

::: details `GetAchievementColor(Type)`

```csharp
public static Color GetAchievementColor(Type achievementType)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `achievementType` | `System.Type` |  |

**Returns:** `UnityEngine.Color`

:::

::: details `GetAchievementColorHex(Type)`

```csharp
public static string GetAchievementColorHex(Type achievementType)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `achievementType` | `System.Type` |  |

**Returns:** `string`

:::

::: details `GetAliveHeroCount()`

```csharp
public static int GetAliveHeroCount()
```

**Returns:** `int`

:::

::: details `GetClosestAliveHero(Vector3, bool)`

```csharp
public static Hero GetClosestAliveHero(Vector3 pivot, bool fallbackToDead = true)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `pivot` | `UnityEngine.Vector3` |  |
| `fallbackToDead` | `bool` |  |

**Returns:** `Hero`

:::

::: details `GetClosestHeroDistance(Vector3, bool)`

```csharp
public static float GetClosestHeroDistance(Vector3 pivot, bool fallbackToDead = true)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `pivot` | `UnityEngine.Vector3` |  |
| `fallbackToDead` | `bool` |  |

**Returns:** `float`

:::

::: details `GetControlPresetWindow()`

```csharp
public static IControlPresetWindow GetControlPresetWindow()
```

**Returns:** `IControlPresetWindow`

:::

::: details `GetCoroutiner()`

```csharp
public static Coroutiner GetCoroutiner()
```

**Returns:** `Coroutiner`

:::

::: details `GetCurrencyColor(CurrencyType)`

```csharp
public static Color GetCurrencyColor(CurrencyType type)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `type` | [`CurrencyType`](/api/Global.CurrencyType) |  |

**Returns:** `UnityEngine.Color`

:::

::: details `GetCurrencyColorHex(CurrencyType)`

```csharp
public static string GetCurrencyColorHex(CurrencyType type)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `type` | [`CurrencyType`](/api/Global.CurrencyType) |  |

**Returns:** `string`

:::

::: details `GetCurrentMultiplayerCompatibilityVersion()`

Used to check game compatibility between multiplayer host/clients.This special version is used to allow cross-platform multiplayer (DRM-Free, STOVE, Steam, e.g.)

```csharp
public static string GetCurrentMultiplayerCompatibilityVersion()
```

**Returns:** `string`

:::

::: details `GetData&lt;T&gt;(IDictionary&lt;string, string&gt;, string, string, string)`

```csharp
public static T GetData<T>(this IDictionary<string, string> dict, string key0, string key1, string key2)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `dict` | `System.Collections.Generic.IDictionary<TKey, TValue><string,string>` |  |
| `key0` | `string` |  |
| `key1` | `string` |  |
| `key2` | `string` |  |
| `` | `T` |  |

**Returns:** `T`

:::

::: details `GetData&lt;T&gt;(IDictionary&lt;string, string&gt;, string, string)`

```csharp
public static T GetData<T>(this IDictionary<string, string> dict, string key0, string key1)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `dict` | `System.Collections.Generic.IDictionary<TKey, TValue><string,string>` |  |
| `key0` | `string` |  |
| `key1` | `string` |  |
| `` | `T` |  |

**Returns:** `T`

:::

::: details `GetData&lt;T&gt;(IDictionary&lt;string, string&gt;, string)`

```csharp
public static T GetData<T>(this IDictionary<string, string> dict, string key0)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `dict` | `System.Collections.Generic.IDictionary<TKey, TValue><string,string>` |  |
| `key0` | `string` |  |
| `` | `T` |  |

**Returns:** `T`

:::

::: details `GetDataKey(string, string, string)`

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

:::

::: details `GetDataKey(string, string)`

```csharp
public static string GetDataKey(string key0, string key1)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `key0` | `string` |  |
| `key1` | `string` |  |

**Returns:** `string`

:::

::: details `GetDataKey(string)`

```csharp
public static string GetDataKey(string key0)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `key0` | `string` |  |

**Returns:** `string`

:::

::: details `GetDataOrDefault&lt;T&gt;(IDictionary&lt;string, string&gt;, string, T)`

```csharp
public static T GetDataOrDefault<T>(this IDictionary<string, string> dict, string key0, T defaultValue = default)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `dict` | `System.Collections.Generic.IDictionary<TKey, TValue><string,string>` |  |
| `key0` | `string` |  |
| `defaultValue` | `T` |  |
| `` | `T` |  |

**Returns:** `T`

:::

::: details `GetDataOrDefault&lt;T&gt;(IDictionary&lt;string, string&gt;, string, string, T)`

```csharp
public static T GetDataOrDefault<T>(this IDictionary<string, string> dict, string key0, string key1, T defaultValue = default)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `dict` | `System.Collections.Generic.IDictionary<TKey, TValue><string,string>` |  |
| `key0` | `string` |  |
| `key1` | `string` |  |
| `defaultValue` | `T` |  |
| `` | `T` |  |

**Returns:** `T`

:::

::: details `GetDataOrDefault&lt;T&gt;(IDictionary&lt;string, string&gt;, string, string, string, T)`

```csharp
public static T GetDataOrDefault<T>(this IDictionary<string, string> dict, string key0, string key1, string key2, T defaultValue = default)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `dict` | `System.Collections.Generic.IDictionary<TKey, TValue><string,string>` |  |
| `key0` | `string` |  |
| `key1` | `string` |  |
| `key2` | `string` |  |
| `defaultValue` | `T` |  |
| `` | `T` |  |

**Returns:** `T`

:::

::: details `GetDefaultObliterationSlots()`

```csharp
public static int GetDefaultObliterationSlots()
```

**Returns:** `int`

:::

::: details `GetDejavuCost(Object, int)`

```csharp
public static int GetDejavuCost(Object target, int wins = -1)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `target` | `UnityEngine.Object` |  |
| `wins` | `int` |  |

**Returns:** `int`

:::

::: details `GetDejavuMaxWins(Object)`

```csharp
public static int GetDejavuMaxWins(Object target)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `target` | `UnityEngine.Object` |  |

**Returns:** `int`

:::

::: details `GetGoodRewardPosition(Vector3, float)`

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

:::

::: details `GetHex(Color)`

```csharp
public static string GetHex(Color color)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `color` | `UnityEngine.Color` |  |

**Returns:** `string`

:::

::: details `GetMaxObliterationSlots()`

```csharp
public static int GetMaxObliterationSlots()
```

**Returns:** `int`

:::

::: details `GetMultiplayerCompatibilityVersion(string)`

```csharp
public static string GetMultiplayerCompatibilityVersion(string bundleVersion)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `bundleVersion` | `string` |  |

**Returns:** `string`

:::

::: details `GetNavMeshPath(Vector3, Vector3)`

```csharp
public static NavMeshPath GetNavMeshPath(Vector3 start, Vector3 end)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `start` | `UnityEngine.Vector3` |  |
| `end` | `UnityEngine.Vector3` |  |

**Returns:** `UnityEngine.AI.NavMeshPath`

:::

::: details `GetNavMeshPathStatus(Vector3, Vector3)`

```csharp
public static NavMeshPathStatus GetNavMeshPathStatus(Vector3 start, Vector3 end)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `start` | `UnityEngine.Vector3` |  |
| `end` | `UnityEngine.Vector3` |  |

**Returns:** `UnityEngine.AI.NavMeshPathStatus`

:::

::: details `GetObliterationMinAllowedHeroes()`

```csharp
public static int GetObliterationMinAllowedHeroes()
```

**Returns:** `int`

:::

::: details `GetObliterationMinAllowedItemsPerRarity()`

```csharp
public static int GetObliterationMinAllowedItemsPerRarity()
```

**Returns:** `int`

:::

::: details `GetObliterationSlotPrice(int)`

```csharp
public static int GetObliterationSlotPrice(int slotIndex)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `slotIndex` | `int` |  |

**Returns:** `int`

:::

::: details `GetOriginalName(string)`

Clean the given name removing (Clone) or variant suffixes.Useful when trying to figure out id of name-linked resources.

```csharp
public static string GetOriginalName(string name)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `name` | `string` |  |

**Returns:** `string`

:::

::: details `GetParentDirectory(string)`

```csharp
public static string GetParentDirectory(string path)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `path` | `string` |  |

**Returns:** `string`

:::

::: details `GetPositionOnGround(Vector3, float)`

```csharp
public static Vector3 GetPositionOnGround(Vector3 position, float yDiffRange = 50)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `position` | `UnityEngine.Vector3` |  |
| `yDiffRange` | `float` |  |

**Returns:** `UnityEngine.Vector3`

:::

::: details `GetProjectRootPath()`

```csharp
public static string GetProjectRootPath()
```

**Returns:** `string`

:::

::: details `GetRarityColor(Rarity)`

```csharp
public static Color GetRarityColor(Rarity rarity)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `rarity` | [`Rarity`](/api/Global.Rarity) |  |

**Returns:** `UnityEngine.Color`

:::

::: details `GetRarityColor(SkinRarity)`

```csharp
public static Color GetRarityColor(SkinRarity rarity)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `rarity` | [`SkinRarity`](/api/Global.SkinRarity) |  |

**Returns:** `UnityEngine.Color`

:::

::: details `GetRarityColorHex(Rarity)`

Gets rarity color with prefix #.

```csharp
public static string GetRarityColorHex(Rarity rarity)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `rarity` | [`Rarity`](/api/Global.Rarity) |  |

**Returns:** `string`

:::

::: details `GetRarityColorHex(SkinRarity)`

```csharp
public static string GetRarityColorHex(SkinRarity rarity)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `rarity` | [`SkinRarity`](/api/Global.SkinRarity) |  |

**Returns:** `string`

:::

::: details `GetReadableTimespanConcise(TimeSpan)`

```csharp
public static string GetReadableTimespanConcise(TimeSpan t)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `t` | `System.TimeSpan` |  |

**Returns:** `string`

:::

::: details `GetReadableTimespanDetailed(TimeSpan)`

```csharp
public static string GetReadableTimespanDetailed(TimeSpan t)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `t` | `System.TimeSpan` |  |

**Returns:** `string`

:::

::: details `GetRequiredAchievementOfTarget(string)`

```csharp
public static Type GetRequiredAchievementOfTarget(string targetTypeName)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `targetTypeName` | `string` |  |

**Returns:** `System.Type`

:::

::: details `GetRequiredAchievementOfTarget(Type)`

```csharp
public static Type GetRequiredAchievementOfTarget(Type targetType)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `targetType` | `System.Type` |  |

**Returns:** `System.Type`

:::

::: details `GetRequiredMasteryLevelForStarSlotUnlock(int)`

```csharp
public static int GetRequiredMasteryLevelForStarSlotUnlock(int index)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `index` | `int` |  |

**Returns:** `int`

:::

::: details `GetRequiredMasteryPointsToLevelUp(int)`

```csharp
public static long GetRequiredMasteryPointsToLevelUp(int currentLevel)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `currentLevel` | `int` |  |

**Returns:** `long`

:::

::: details `GetRequiredStardustForStarSlotUnlock(int)`

```csharp
public static int GetRequiredStardustForStarSlotUnlock(int index)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `index` | `int` |  |

**Returns:** `int`

:::

::: details `GetRewardedMasteryPoints(float)`

```csharp
public static long GetRewardedMasteryPoints(float minutes)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `minutes` | `float` |  |

**Returns:** `long`

:::

::: details `GetStarCategoryColor(StarType)`

```csharp
public static Color GetStarCategoryColor(StarType type)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `type` | [`StarType`](/api/Global.StarType) |  |

**Returns:** `UnityEngine.Color`

:::

::: details `GetStardustRewardOnLevelUpAmount(int)`

```csharp
public static int GetStardustRewardOnLevelUpAmount(int nextLevel)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `nextLevel` | `int` |  |

**Returns:** `int`

:::

::: details `GetTypeFromShortName(string)`

```csharp
public static Type GetTypeFromShortName(string typeName)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `typeName` | `string` |  |

**Returns:** `System.Type`

:::

::: details `GetUIComponentBelowCursor&lt;T&gt;(bool)`

```csharp
public static T GetUIComponentBelowCursor<T>(bool includeParent = true) where T : Component
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `includeParent` | `bool` |  |
| `` | `T` |  |

**Returns:** `T`

:::

::: details `GetUnlockedTargetsOfAchievement(Type)`

```csharp
public static List<Type> GetUnlockedTargetsOfAchievement(Type achievementType)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `achievementType` | `System.Type` |  |

**Returns:** `System.Collections.Generic.List<T><System.Type>`

:::

::: details `GetValidAgentDestination_Closest(Vector3, Vector3)`

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

:::

::: details `GetValidAgentDestination_LinearSweep(Vector3, Vector3)`

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

:::

::: details `GetValidAgentPosition(Vector3, float)`

```csharp
public static Vector3 GetValidAgentPosition(Vector3 pos, float threshold = 10)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `pos` | `UnityEngine.Vector3` |  |
| `threshold` | `float` |  |

**Returns:** `UnityEngine.Vector3`

:::

::: details `Helper_GetInstanceOfActor&lt;T&gt;(ref T)`

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

:::

::: details `InitAllTypeReferences()`

```csharp
[RuntimeInitializeOnLoadMethod(RuntimeInitializeLoadType.AfterAssembliesLoaded)]
public static void InitAllTypeReferences()
```

:::

::: details `InstantiateActor_Imp&lt;T&gt;(T, Vector3, Quaternion?, Actor)`

```csharp
public static T InstantiateActor_Imp<T>(T prefab, Vector3 position, Quaternion? rotation, Actor parent) where T : Actor
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `prefab` | `T` |  |
| `position` | `UnityEngine.Vector3` |  |
| `rotation` | `UnityEngine.Quaternion?` |  |
| `parent` | [`Actor`](/api/Global.Actor) |  |
| `` | `T` |  |

**Returns:** `T`

:::

::: details `InstantiateAndSpawn&lt;T&gt;(T, Action&lt;T&gt;)`

```csharp
public static T InstantiateAndSpawn<T>(T prefab, Action<T> beforeSpawn = null) where T : Component
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `prefab` | `T` |  |
| `beforeSpawn` | `System.Action<T>` |  |
| `` | `T` |  |

**Returns:** `T`

:::

::: details `InstantiateAndSpawn&lt;T&gt;(T, Vector3, Quaternion?, Action&lt;T&gt;)`

```csharp
public static T InstantiateAndSpawn<T>(T prefab, Vector3 position, Quaternion? rotation, Action<T> beforeSpawn = null) where T : Component
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `prefab` | `T` |  |
| `position` | `UnityEngine.Vector3` |  |
| `rotation` | `UnityEngine.Quaternion?` |  |
| `beforeSpawn` | `System.Action<T>` |  |
| `` | `T` |  |

**Returns:** `T`

:::

::: details `InstantiateAndSpawn&lt;T&gt;(Action&lt;T&gt;)`

```csharp
public static T InstantiateAndSpawn<T>(Action<T> beforeSpawn = null) where T : Component
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `beforeSpawn` | `System.Action<T>` |  |
| `` | `T` |  |

**Returns:** `T`

:::

::: details `InstantiateAndSpawn&lt;T&gt;(Vector3, Quaternion?, Action&lt;T&gt;)`

```csharp
public static T InstantiateAndSpawn<T>(Vector3 position, Quaternion? rotation, Action<T> beforeSpawn = null) where T : Component
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `position` | `UnityEngine.Vector3` |  |
| `rotation` | `UnityEngine.Quaternion?` |  |
| `beforeSpawn` | `System.Action<T>` |  |
| `` | `T` |  |

**Returns:** `T`

:::

::: details `IntToRoman(int)`

```csharp
public static string IntToRoman(int num)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `num` | `int` |  |

**Returns:** `string`

:::

::: details `IsAccessoryIncludedInGame(string)`

```csharp
public static bool IsAccessoryIncludedInGame(string type)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `type` | `string` |  |

**Returns:** `bool`

:::

::: details `IsAchievementIncludedInGame(string)`

```csharp
public static bool IsAchievementIncludedInGame(string typeStr)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `typeStr` | `string` |  |

**Returns:** `bool`

:::

::: details `IsAnyActorBeingDestroyed()`

```csharp
public static bool IsAnyActorBeingDestroyed()
```

**Returns:** `bool`

:::

::: details `IsArtifactIncludedInGame(string)`

```csharp
public static bool IsArtifactIncludedInGame(string type)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `type` | `string` |  |

**Returns:** `bool`

:::

::: details `IsBeingDestroyed(GameObject)`

```csharp
public static bool IsBeingDestroyed(GameObject gameObject)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `gameObject` | `UnityEngine.GameObject` |  |

**Returns:** `bool`

:::

::: details `IsChristmas()`

```csharp
public static bool IsChristmas()
```

**Returns:** `bool`

:::

::: details `IsCurseIncludedInGame(string)`

```csharp
public static bool IsCurseIncludedInGame(string type)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `type` | `string` |  |

**Returns:** `bool`

:::

::: details `IsDejavuFree(string)`

```csharp
public static bool IsDejavuFree(string typeName)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `typeName` | `string` |  |

**Returns:** `bool`

:::

::: details `IsDejavuFree(Object)`

```csharp
public static bool IsDejavuFree(Object target)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `target` | `UnityEngine.Object` |  |

**Returns:** `bool`

:::

::: details `IsEmoteIncludedInGame(string)`

```csharp
public static bool IsEmoteIncludedInGame(string type)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `type` | `string` |  |

**Returns:** `bool`

:::

::: details `IsExcludedFromPool(string)`

```csharp
public static bool IsExcludedFromPool(string type)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `type` | `string` |  |

**Returns:** `bool`

:::

::: details `IsGameModifierIncludedInGame(string)`

```csharp
public static bool IsGameModifierIncludedInGame(string type)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `type` | `string` |  |

**Returns:** `bool`

:::

::: details `IsGemIncludedInGame(string)`

```csharp
public static bool IsGemIncludedInGame(string type)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `type` | `string` |  |

**Returns:** `bool`

:::

::: details `IsHeroIncludedInGame(string)`

```csharp
public static bool IsHeroIncludedInGame(string type)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `type` | `string` |  |

**Returns:** `bool`

:::

::: details `IsLucidDreamIncludedInGame(string)`

```csharp
public static bool IsLucidDreamIncludedInGame(string type)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `type` | `string` |  |

**Returns:** `bool`

:::

::: details `IsMeleeHero(HeroClassType)`

```csharp
public static bool IsMeleeHero(Hero.HeroClassType type)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `type` | [`Hero.HeroClassType`](/api/Global.Hero) |  |

**Returns:** `bool`

:::

::: details `IsMonsterIncludedInGame(string)`

```csharp
public static bool IsMonsterIncludedInGame(string type)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `type` | `string` |  |

**Returns:** `bool`

:::

::: details `IsNametagIncludedInGame(string)`

```csharp
public static bool IsNametagIncludedInGame(string type)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `type` | `string` |  |

**Returns:** `bool`

:::

::: details `IsNearChristmas()`

```csharp
public static bool IsNearChristmas()
```

**Returns:** `bool`

:::

::: details `IsNotPlayableOnTop(Vector3)`

```csharp
public static bool IsNotPlayableOnTop(Vector3 pos)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `pos` | `UnityEngine.Vector3` |  |

**Returns:** `bool`

:::

::: details `IsOkay(Displacement)`

Check floating values if they're not infinity nor NaNs.This will print out exceptions for getting stack traces in Cloud Diagnostics.

```csharp
public static bool IsOkay(Displacement d)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `d` | [`Displacement`](/api/Global.Displacement) |  |

**Returns:** `bool`

:::

::: details `IsOkay(double)`

Check floating values if they're not infinity nor NaNs.This will print out exceptions for getting stack traces in Cloud Diagnostics.

```csharp
public static bool IsOkay(double d)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `d` | `double` |  |

**Returns:** `bool`

:::

::: details `IsOkay(float)`

Check floating values if they're not infinity nor NaNs.This will print out exceptions for getting stack traces in Cloud Diagnostics.

```csharp
public static bool IsOkay(float f)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `f` | `float` |  |

**Returns:** `bool`

:::

::: details `IsOkay(Vector2)`

Check floating values if they're not infinity nor NaNs.This will print out exceptions for getting stack traces in Cloud Diagnostics.

```csharp
public static bool IsOkay(Vector2 v)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `v` | `UnityEngine.Vector2` |  |

**Returns:** `bool`

:::

::: details `IsOkay(Vector3)`

Check floating values if they're not infinity nor NaNs.This will print out exceptions for getting stack traces in Cloud Diagnostics.

```csharp
public static bool IsOkay(Vector3 v)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `v` | `UnityEngine.Vector3` |  |

**Returns:** `bool`

:::

::: details `IsOkay(Vector4)`

Check floating values if they're not infinity nor NaNs.This will print out exceptions for getting stack traces in Cloud Diagnostics.

```csharp
public static bool IsOkay(Vector4 v)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `v` | `UnityEngine.Vector4` |  |

**Returns:** `bool`

:::

::: details `IsRangedHero(HeroClassType)`

```csharp
public static bool IsRangedHero(Hero.HeroClassType type)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `type` | [`Hero.HeroClassType`](/api/Global.Hero) |  |

**Returns:** `bool`

:::

::: details `IsRoomModifierIncludedInGame(string)`

```csharp
public static bool IsRoomModifierIncludedInGame(string type)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `type` | `string` |  |

**Returns:** `bool`

:::

::: details `IsSkillIncludedInGame(string)`

```csharp
public static bool IsSkillIncludedInGame(string type)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `type` | `string` |  |

**Returns:** `bool`

:::

::: details `IsSkinIncludedInGame(string)`

```csharp
public static bool IsSkinIncludedInGame(string type)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `type` | `string` |  |

**Returns:** `bool`

:::

::: details `IsStarIncludedInGame(string)`

```csharp
public static bool IsStarIncludedInGame(string type)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `type` | `string` |  |

**Returns:** `bool`

:::

::: details `IsTreasureIncludedInGame(string)`

```csharp
public static bool IsTreasureIncludedInGame(string type)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `type` | `string` |  |

**Returns:** `bool`

:::

::: details `IsZoneIncludedInGame(string)`

```csharp
public static bool IsZoneIncludedInGame(string type)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `type` | `string` |  |

**Returns:** `bool`

:::

::: details `NicifyVariableName(string)`

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

:::

::: details `OpenURL(string, OpenURLSettings)`

```csharp
public static void OpenURL(string url, OpenURLSettings settings = null)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `url` | `string` |  |
| `settings` | [`OpenURLSettings`](/api/Global.OpenURLSettings) |  |

:::

::: details `PrepareAndSpawnActor_Imp&lt;T&gt;(T, Action&lt;T&gt;)`

```csharp
public static T PrepareAndSpawnActor_Imp<T>(T newActor, Action<T> beforePrepare) where T : Actor
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `newActor` | `T` |  |
| `beforePrepare` | `System.Action<T>` |  |
| `` | `T` |  |

**Returns:** `T`

:::

::: details `PrepareAndSpawnHero_Imp&lt;T&gt;(T, DewPlayer, int, HeroLoadoutData, string, Action&lt;T&gt;)`

```csharp
public static T PrepareAndSpawnHero_Imp<T>(T newEntity, DewPlayer owner, int level, HeroLoadoutData loadout, string skin, Action<T> beforePrepare) where T : Hero
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `newEntity` | `T` |  |
| `owner` | [`DewPlayer`](/api/Global.DewPlayer) |  |
| `level` | `int` |  |
| `loadout` | [`HeroLoadoutData`](/api/Global.HeroLoadoutData) |  |
| `skin` | `string` |  |
| `beforePrepare` | `System.Action<T>` |  |
| `` | `T` |  |

**Returns:** `T`

:::

::: details `PrepareAndSpawnStatusEffect_Imp&lt;T&gt;(T, Entity, Actor, CastInfo, Action&lt;T&gt;)`

```csharp
public static T PrepareAndSpawnStatusEffect_Imp<T>(T newSe, Entity victim, Actor parent, CastInfo info, Action<T> beforePrepare) where T : StatusEffect
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `newSe` | `T` |  |
| `victim` | [`Entity`](/api/Global.Entity) |  |
| `parent` | [`Actor`](/api/Global.Actor) |  |
| `info` | [`CastInfo`](/api/Global.CastInfo) |  |
| `beforePrepare` | `System.Action<T>` |  |
| `` | `T` |  |

**Returns:** `T`

:::

::: details `QuitApplication(bool)`

```csharp
public static void QuitApplication(bool dontSave = false)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `dontSave` | `bool` |  |

:::

::: details `RaycastAllUIElementsBelowCursor(out ListReturnHandle&lt;RaycastResult&gt;)`

```csharp
public static List<RaycastResult> RaycastAllUIElementsBelowCursor(out ListReturnHandle<RaycastResult> handle)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `handle` | `ListReturnHandle<RaycastResult>` |  |

**Returns:** `System.Collections.Generic.List<T><RaycastResult>`

:::

::: details `RaycastAllUIElementsBelowCursor(List&lt;RaycastResult&gt;)`

```csharp
public static void RaycastAllUIElementsBelowCursor(List<RaycastResult> results)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `results` | `System.Collections.Generic.List<T><RaycastResult>` |  |

:::

::: details `RaycastAllUIElementsBelowScreenPoint(Vector2, out ListReturnHandle&lt;RaycastResult&gt;)`

```csharp
public static List<RaycastResult> RaycastAllUIElementsBelowScreenPoint(Vector2 screenPoint, out ListReturnHandle<RaycastResult> handle)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `screenPoint` | `UnityEngine.Vector2` |  |
| `handle` | `ListReturnHandle<RaycastResult>` |  |

**Returns:** `System.Collections.Generic.List<T><RaycastResult>`

:::

::: details `RaycastAllUIElementsBelowScreenPoint(Vector2, List&lt;RaycastResult&gt;)`

```csharp
public static void RaycastAllUIElementsBelowScreenPoint(Vector2 screenPoint, List<RaycastResult> results)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `screenPoint` | `UnityEngine.Vector2` |  |
| `results` | `System.Collections.Generic.List<T><RaycastResult>` |  |

:::

::: details `RefreshRenderer()`

```csharp
public static void RefreshRenderer()
```

:::

::: details `RemoveData(IDictionary&lt;string, string&gt;, string, string, string)`

```csharp
public static bool RemoveData(this IDictionary<string, string> dict, string key0, string key1, string key2)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `dict` | `System.Collections.Generic.IDictionary<TKey, TValue><string,string>` |  |
| `key0` | `string` |  |
| `key1` | `string` |  |
| `key2` | `string` |  |

**Returns:** `bool`

:::

::: details `RemoveData(IDictionary&lt;string, string&gt;, string, string)`

```csharp
public static bool RemoveData(this IDictionary<string, string> dict, string key0, string key1)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `dict` | `System.Collections.Generic.IDictionary<TKey, TValue><string,string>` |  |
| `key0` | `string` |  |
| `key1` | `string` |  |

**Returns:** `bool`

:::

::: details `RemoveData(IDictionary&lt;string, string&gt;, string)`

```csharp
public static bool RemoveData(this IDictionary<string, string> dict, string key0)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `dict` | `System.Collections.Generic.IDictionary<TKey, TValue><string,string>` |  |
| `key0` | `string` |  |

**Returns:** `bool`

:::

::: details `ResolveLocalizedFormatArgs(string[])`

```csharp
public static void ResolveLocalizedFormatArgs(string[] localizedFormatArgs)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `localizedFormatArgs` | `string[]` |  |

:::

::: details `SelectBestIndexWithScore&lt;T&gt;(IList&lt;T&gt;, Func&lt;T, int, float&gt;, float, DewRandom)`

Item with best score will be returned. If fuzziness is set, score will be multiplied by a random value between (1+fuzziness) ~ (1-fuzziness)

```csharp
public static int SelectBestIndexWithScore<T>(IList<T> list, Func<T, int, float> scoreFunc, float fuzziness = 0, DewRandom random = null)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `list` | `System.Collections.Generic.IList<T>` |  |
| `scoreFunc` | `System.Func<T1, T2, TResult><T,int,float>` |  |
| `fuzziness` | `float` |  |
| `random` | [`DewRandom`](/api/Global.DewRandom) |  |
| `` | `T` |  |

**Returns:** `int`

:::

::: details `SelectBestIndexWithScore&lt;T&gt;(ReadOnlySpan&lt;T&gt;, Func&lt;T, int, float&gt;, float, DewRandom)`

Item with best score will be returned. If fuzziness is set, score will be multiplied by a random value between (1+fuzziness) ~ (1-fuzziness)

```csharp
public static int SelectBestIndexWithScore<T>(ReadOnlySpan<T> list, Func<T, int, float> scoreFunc, float fuzziness = 0, DewRandom random = null)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `list` | `System.ReadOnlySpan<T>` |  |
| `scoreFunc` | `System.Func<T1, T2, TResult><T,int,float>` |  |
| `fuzziness` | `float` |  |
| `random` | [`DewRandom`](/api/Global.DewRandom) |  |
| `` | `T` |  |

**Returns:** `int`

:::

::: details `SelectBestWithScore&lt;T&gt;(HashSet&lt;T&gt;, Func&lt;T, float&gt;, float, DewRandom)`

Item with best score will be returned. If fuzziness is set, score will be multiplied by a random value between (1+fuzziness) ~ (1-fuzziness)

```csharp
public static T SelectBestWithScore<T>(HashSet<T> list, Func<T, float> scoreFunc, float fuzziness = 0, DewRandom random = null)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `list` | `System.Collections.Generic.HashSet<T>` |  |
| `scoreFunc` | `System.Func<T, TResult><T,float>` |  |
| `fuzziness` | `float` |  |
| `random` | [`DewRandom`](/api/Global.DewRandom) |  |
| `` | `T` |  |

**Returns:** `T`

:::

::: details `SelectBestWithScore&lt;T&gt;(IList&lt;T&gt;, Func&lt;T, int, float&gt;, float, DewRandom)`

Item with best score will be returned. If fuzziness is set, score will be multiplied by a random value between (1+fuzziness) ~ (1-fuzziness)

```csharp
public static T SelectBestWithScore<T>(IList<T> list, Func<T, int, float> scoreFunc, float fuzziness = 0, DewRandom random = null)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `list` | `System.Collections.Generic.IList<T>` |  |
| `scoreFunc` | `System.Func<T1, T2, TResult><T,int,float>` |  |
| `fuzziness` | `float` |  |
| `random` | [`DewRandom`](/api/Global.DewRandom) |  |
| `` | `T` |  |

**Returns:** `T`

:::

::: details `SelectBestWithScore&lt;T&gt;(ReadOnlySpan&lt;T&gt;, Func&lt;T, int, float&gt;, float, DewRandom)`

Item with best score will be returned. If fuzziness is set, score will be multiplied by a random value between (1+fuzziness) ~ (1-fuzziness)

```csharp
public static T SelectBestWithScore<T>(ReadOnlySpan<T> list, Func<T, int, float> scoreFunc, float fuzziness = 0, DewRandom random = null)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `list` | `System.ReadOnlySpan<T>` |  |
| `scoreFunc` | `System.Func<T1, T2, TResult><T,int,float>` |  |
| `fuzziness` | `float` |  |
| `random` | [`DewRandom`](/api/Global.DewRandom) |  |
| `` | `T` |  |

**Returns:** `T`

:::

::: details `SelectRandomAliveHero(bool)`

```csharp
public static Hero SelectRandomAliveHero(bool fallbackToDead = true)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `fallbackToDead` | `bool` |  |

**Returns:** `Hero`

:::

::: details `SelectRandomWeightedIndexInParams(params float[])`

```csharp
public static int SelectRandomWeightedIndexInParams(params float[] weights)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `weights` | `float[]` |  |

**Returns:** `int`

:::

::: details `SelectRandomWeightedInList&lt;T&gt;(IList&lt;T&gt;, Func&lt;T, float&gt;, DewRandom)`

```csharp
public static T SelectRandomWeightedInList<T>(IList<T> list, Func<T, float> weightGetter, DewRandom random = null)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `list` | `System.Collections.Generic.IList<T>` |  |
| `weightGetter` | `System.Func<T, TResult><T,float>` |  |
| `random` | [`DewRandom`](/api/Global.DewRandom) |  |
| `` | `T` |  |

**Returns:** `T`

:::

::: details `SelectRandomWeightedInList&lt;T&gt;(ReadOnlySpan&lt;T&gt;, Func&lt;T, float&gt;)`

```csharp
public static T SelectRandomWeightedInList<T>(ReadOnlySpan<T> list, Func<T, float> weightGetter)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `list` | `System.ReadOnlySpan<T>` |  |
| `weightGetter` | `System.Func<T, TResult><T,float>` |  |
| `` | `T` |  |

**Returns:** `T`

:::

::: details `SelectRandomWeightedInParams&lt;T&gt;(params (float, T)[])`

```csharp
public static T SelectRandomWeightedInParams<T>(params (float, T)[] elements)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `elements` | `(float, T)[]` |  |
| `` | `T` |  |

**Returns:** `T`

:::

::: details `SelectRandomWeightedInReadOnlyList&lt;T&gt;(IReadOnlyList&lt;T&gt;, Func&lt;T, float&gt;)`

Without the postfix, you won't be able to feed in Lists because of ambiguity.

```csharp
public static T SelectRandomWeightedInReadOnlyList<T>(IReadOnlyList<T> list, Func<T, float> weightGetter)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `list` | `System.Collections.Generic.IReadOnlyList<T>` |  |
| `weightGetter` | `System.Func<T, TResult><T,float>` |  |
| `` | `T` |  |

**Returns:** `T`

:::

::: details `SetData&lt;T&gt;(IDictionary&lt;string, string&gt;, string, T)`

```csharp
public static void SetData<T>(this IDictionary<string, string> dict, string key0, T value)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `dict` | `System.Collections.Generic.IDictionary<TKey, TValue><string,string>` |  |
| `key0` | `string` |  |
| `value` | `T` |  |
| `` | `T` |  |

:::

::: details `SetData&lt;T&gt;(IDictionary&lt;string, string&gt;, string, string, T)`

```csharp
public static void SetData<T>(this IDictionary<string, string> dict, string key0, string key1, T value)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `dict` | `System.Collections.Generic.IDictionary<TKey, TValue><string,string>` |  |
| `key0` | `string` |  |
| `key1` | `string` |  |
| `value` | `T` |  |
| `` | `T` |  |

:::

::: details `SetData&lt;T&gt;(IDictionary&lt;string, string&gt;, string, string, string, T)`

```csharp
public static void SetData<T>(this IDictionary<string, string> dict, string key0, string key1, string key2, T value)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `dict` | `System.Collections.Generic.IDictionary<TKey, TValue><string,string>` |  |
| `key0` | `string` |  |
| `key1` | `string` |  |
| `key2` | `string` |  |
| `value` | `T` |  |
| `` | `T` |  |

:::

::: details `SetUnscaledTimeUpdate(GameObject)`

```csharp
public static void SetUnscaledTimeUpdate(GameObject gobj)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `gobj` | `UnityEngine.GameObject` |  |

:::

::: details `ShowJsonWithEditor(string)`

```csharp
public static void ShowJsonWithEditor(string json)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `json` | `string` |  |

:::

::: details `SpawnEntity&lt;T&gt;(T, Vector3, Quaternion?, Actor, DewPlayer, int, Action&lt;T&gt;)`

```csharp
public static T SpawnEntity<T>(T entity, Vector3 position, Quaternion? rotation, Actor parent, DewPlayer owner, int level, Action<T> beforeSpawn = null) where T : Entity
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `entity` | `T` |  |
| `position` | `UnityEngine.Vector3` |  |
| `rotation` | `UnityEngine.Quaternion?` |  |
| `parent` | [`Actor`](/api/Global.Actor) |  |
| `owner` | [`DewPlayer`](/api/Global.DewPlayer) |  |
| `level` | `int` |  |
| `beforeSpawn` | `System.Action<T>` |  |
| `` | `T` |  |

**Returns:** `T`

:::

::: details `SpawnEntity&lt;T&gt;(Vector3, Quaternion?, Actor, DewPlayer, int, Action&lt;T&gt;)`

```csharp
public static T SpawnEntity<T>(Vector3 position, Quaternion? rotation, Actor parent, DewPlayer owner, int level, Action<T> beforeSpawn = null) where T : Entity
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `position` | `UnityEngine.Vector3` |  |
| `rotation` | `UnityEngine.Quaternion?` |  |
| `parent` | [`Actor`](/api/Global.Actor) |  |
| `owner` | [`DewPlayer`](/api/Global.DewPlayer) |  |
| `level` | `int` |  |
| `beforeSpawn` | `System.Action<T>` |  |
| `` | `T` |  |

**Returns:** `T`

:::

::: details `SpawnHero&lt;T&gt;(T, Vector3, Quaternion?, DewPlayer, int, HeroLoadoutData, string, Action&lt;T&gt;)`

```csharp
public static T SpawnHero<T>(T hero, Vector3 position, Quaternion? rotation, DewPlayer owner, int level, HeroLoadoutData loadout, string skin, Action<T> beforeSpawn = null) where T : Hero
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `hero` | `T` |  |
| `position` | `UnityEngine.Vector3` |  |
| `rotation` | `UnityEngine.Quaternion?` |  |
| `owner` | [`DewPlayer`](/api/Global.DewPlayer) |  |
| `level` | `int` |  |
| `loadout` | [`HeroLoadoutData`](/api/Global.HeroLoadoutData) |  |
| `skin` | `string` |  |
| `beforeSpawn` | `System.Action<T>` |  |
| `` | `T` |  |

**Returns:** `T`

:::

::: details `SpawnHero&lt;T&gt;(Vector3, Quaternion?, DewPlayer, int, HeroLoadoutData, string, Action&lt;T&gt;)`

```csharp
public static T SpawnHero<T>(Vector3 position, Quaternion? rotation, DewPlayer owner, int level, HeroLoadoutData loadout, string skin, Action<T> beforeSpawn = null) where T : Hero
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `position` | `UnityEngine.Vector3` |  |
| `rotation` | `UnityEngine.Quaternion?` |  |
| `owner` | [`DewPlayer`](/api/Global.DewPlayer) |  |
| `level` | `int` |  |
| `loadout` | [`HeroLoadoutData`](/api/Global.HeroLoadoutData) |  |
| `skin` | `string` |  |
| `beforeSpawn` | `System.Action<T>` |  |
| `` | `T` |  |

**Returns:** `T`

:::

::: details `TryGetData&lt;T&gt;(IDictionary&lt;string, string&gt;, string, out T)`

```csharp
public static bool TryGetData<T>(this IDictionary<string, string> dict, string key0, out T value)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `dict` | `System.Collections.Generic.IDictionary<TKey, TValue><string,string>` |  |
| `key0` | `string` |  |
| `value` | `T` |  |
| `` | `T` |  |

**Returns:** `bool`

:::

::: details `TryGetData&lt;T&gt;(IDictionary&lt;string, string&gt;, string, string, out T)`

```csharp
public static bool TryGetData<T>(this IDictionary<string, string> dict, string key0, string key1, out T value)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `dict` | `System.Collections.Generic.IDictionary<TKey, TValue><string,string>` |  |
| `key0` | `string` |  |
| `key1` | `string` |  |
| `value` | `T` |  |
| `` | `T` |  |

**Returns:** `bool`

:::

::: details `TryGetData&lt;T&gt;(IDictionary&lt;string, string&gt;, string, string, string, out T)`

```csharp
public static bool TryGetData<T>(this IDictionary<string, string> dict, string key0, string key1, string key2, out T value)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `dict` | `System.Collections.Generic.IDictionary<TKey, TValue><string,string>` |  |
| `key0` | `string` |  |
| `key1` | `string` |  |
| `key2` | `string` |  |
| `value` | `T` |  |
| `` | `T` |  |

**Returns:** `bool`

:::

::: details `TryGetTypeFromShortName(string, out Type)`

```csharp
public static bool TryGetTypeFromShortName(string typeName, out Type type)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `typeName` | `string` |  |
| `type` | `System.Type` |  |

**Returns:** `bool`

:::

::: details `WaitForAggroedEnemiesRoutine()`

Wait until no enemies aggroed to any player exists.

```csharp
public static IEnumerator WaitForAggroedEnemiesRoutine()
```

**Returns:** `System.Collections.IEnumerator`

:::

::: details `WaitForClientsReadyRoutine(List&lt;DewPlayer&gt;)`

Wait until all connections are ready.

```csharp
public static IEnumerator WaitForClientsReadyRoutine(List<DewPlayer> players = null)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `players` | [`System.Collections.Generic.List<T><DewPlayer>`](/api/Global.DewPlayer) |  |

**Returns:** `System.Collections.IEnumerator`

:::
