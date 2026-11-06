# Class: DewPersistence

- **Category:** <span class="cat-dot" style="--cat-color: #64748b" data-cat="Misc & Utility"></span> Misc & Utility
- **Namespace:** `Global`
- **Assembly:** `Dew.Core.dll`

```csharp
public static class DewPersistence
```

## Methods (16)

::: details `ApplyAchievementData(AchievementsData)`

```csharp
public static void ApplyAchievementData(DewPersistence.AchievementsData data)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `data` | [`DewPersistence.AchievementsData`](/api/Global.DewPersistence) |  |

:::

::: details `ApplyGameData(GameData, Action, JsonSerializerSettings)`

```csharp
public static void ApplyGameData(DewPersistence.GameData data, Action onFinish = null, JsonSerializerSettings settings = null)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `data` | [`DewPersistence.GameData`](/api/Global.DewPersistence) |  |
| `onFinish` | `System.Action` |  |
| `settings` | `Newtonsoft.Json.JsonSerializerSettings` |  |

:::

::: details `ApplyPlayerData(DewPlayer, PlayerData, List&lt;(uint, Action)&gt;, JsonSerializerSettings)`

```csharp
public static void ApplyPlayerData(DewPlayer player, DewPersistence.PlayerData data, List<(uint, Action)> batchActions = null, JsonSerializerSettings settings = null)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `player` | [`DewPlayer`](/api/Global.DewPlayer) |  |
| `data` | [`DewPersistence.PlayerData`](/api/Global.DewPersistence) |  |
| `batchActions` | `System.Collections.Generic.List<T><(uint,System.Action)>` |  |
| `settings` | `Newtonsoft.Json.JsonSerializerSettings` |  |

:::

::: details `ApplyRoomDataAfterSpawnObjects(RoomData, JsonSerializerSettings)`

```csharp
public static void ApplyRoomDataAfterSpawnObjects(DewPersistence.RoomData data, JsonSerializerSettings settings = null)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `data` | [`DewPersistence.RoomData`](/api/Global.DewPersistence) |  |
| `settings` | `Newtonsoft.Json.JsonSerializerSettings` |  |

:::

::: details `ApplyRoomDataBeforeSpawnObjects(RoomData, JsonSerializerSettings)`

```csharp
public static void ApplyRoomDataBeforeSpawnObjects(DewPersistence.RoomData data, JsonSerializerSettings settings = null)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `data` | [`DewPersistence.RoomData`](/api/Global.DewPersistence) |  |
| `settings` | `Newtonsoft.Json.JsonSerializerSettings` |  |

:::

::: details `CreateActor&lt;T&gt;(GeneralData, List&lt;(uint, Action)&gt;, JsonSerializerSettings)`

```csharp
public static T CreateActor<T>(DewPersistence.GeneralData data, List<(uint, Action)> batchActions = null, JsonSerializerSettings settings = null) where T : Actor
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `data` | [`DewPersistence.GeneralData`](/api/Global.DewPersistence) |  |
| `batchActions` | `System.Collections.Generic.List<T><(uint,System.Action)>` |  |
| `settings` | `Newtonsoft.Json.JsonSerializerSettings` |  |
| `` | `T` |  |

**Returns:** `T`

:::

::: details `DeserializeOnGameObject(GameObject, Dictionary&lt;string, string&gt;, JsonSerializerSettings, SaveVarFlags, SaveVarFlags)`

```csharp
public static void DeserializeOnGameObject(GameObject gobj, Dictionary<string, string> data, JsonSerializerSettings settings, SaveVarFlags required = SaveVarFlags.Default, SaveVarFlags excluded = SaveVarFlags.Default)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `gobj` | `UnityEngine.GameObject` |  |
| `data` | `System.Collections.Generic.Dictionary<TKey, TValue><string,string>` |  |
| `settings` | `Newtonsoft.Json.JsonSerializerSettings` |  |
| `required` | [`SaveVarFlags`](/api/Global.SaveVarFlags) |  |
| `excluded` | [`SaveVarFlags`](/api/Global.SaveVarFlags) |  |

:::

::: details `FromJson(string, Type, JsonSerializerSettings)`

```csharp
public static object FromJson(string json, Type type, JsonSerializerSettings settings = null)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `json` | `string` |  |
| `type` | `System.Type` |  |
| `settings` | `Newtonsoft.Json.JsonSerializerSettings` |  |

**Returns:** `object`

:::

::: details `FromJson&lt;T&gt;(string, JsonSerializerSettings)`

```csharp
public static T FromJson<T>(string json, JsonSerializerSettings settings = null)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `json` | `string` |  |
| `settings` | `Newtonsoft.Json.JsonSerializerSettings` |  |
| `` | `T` |  |

**Returns:** `T`

:::

::: details `GetNewSettings()`

```csharp
public static JsonSerializerSettings GetNewSettings()
```

**Returns:** `Newtonsoft.Json.JsonSerializerSettings`

:::

::: details `SerializeAchievementData()`

```csharp
public static DewPersistence.AchievementsData SerializeAchievementData()
```

**Returns:** `DewPersistence.AchievementsData`

:::

::: details `SerializeGameData(LoadNodeSettings)`

```csharp
public static DewPersistence.GameData SerializeGameData(LoadNodeSettings settings)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `settings` | [`LoadNodeSettings`](/api/Global.LoadNodeSettings) |  |

**Returns:** `DewPersistence.GameData`

:::

::: details `SerializeGameObject(GameObject)`

```csharp
public static Dictionary<string, string> SerializeGameObject(GameObject gobj)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `gobj` | `UnityEngine.GameObject` |  |

**Returns:** `System.Collections.Generic.Dictionary<TKey, TValue><string,string>`

:::

::: details `SerializePlayerData(DewPlayer)`

```csharp
public static DewPersistence.PlayerData SerializePlayerData(DewPlayer player)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `player` | [`DewPlayer`](/api/Global.DewPlayer) |  |

**Returns:** `DewPersistence.PlayerData`

:::

::: details `SerializeRoomData()`

```csharp
public static DewPersistence.RoomData SerializeRoomData()
```

**Returns:** `DewPersistence.RoomData`

:::

::: details `ToJson(object, JsonSerializerSettings)`

```csharp
public static string ToJson(object obj, JsonSerializerSettings settings = null)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `obj` | `object` |  |
| `settings` | `Newtonsoft.Json.JsonSerializerSettings` |  |

**Returns:** `string`

:::
