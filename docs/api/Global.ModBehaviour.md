# Class: ModBehaviour

- **Namespace:** `Global`
- **Assembly:** `Dew.Core.dll`

```csharp
public class ModBehaviour : MonoBehaviour
```

## Fields

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`instance`** | `[NonSerialized]
public LoadedModInstance instance` |  |

## Properties

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`harmony`** | `public Harmony harmony { get; }` |  |
| **`mod`** | `public ModItem mod { get; }` |  |
| **`modConfigFields`** | `public FieldInfo[] modConfigFields { get; }` |  |

## Methods

### `CallOnManager&lt;T&gt;(Action, Action)`

```csharp
public void CallOnManager<T>(Action onEnable, Action onDisable = null) where T : ManagerBase<T>
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `onEnable` | `System.Action` |  |
| `onDisable` | `System.Action` |  |
| `` | `T` |  |

### `CallOnNetworkedManager&lt;T&gt;(Action, Action)`

```csharp
public void CallOnNetworkedManager<T>(Action onStartClient, Action onStopClient = null) where T : NetworkedManagerBase<T>
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `onStartClient` | `System.Action` |  |
| `onStopClient` | `System.Action` |  |
| `` | `T` |  |

### `GetConsoleSelectedEntity()`

```csharp
protected static Entity GetConsoleSelectedEntity()
```

**Returns:** `Entity`

### `GetModConfigFilePath(FieldInfo)`

```csharp
public virtual string GetModConfigFilePath(FieldInfo modConfigInfo)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `modConfigInfo` | `System.Reflection.FieldInfo` |  |

**Returns:** `string`

### `LoadConfigsToDisk()`

```csharp
public virtual void LoadConfigsToDisk()
```

### `MakeSureClientNonServer()`

Returns false and logs to console if user is not a non-server client.Meant to be used in custom console commands.

```csharp
protected static bool MakeSureClientNonServer()
```

**Returns:** `bool`

### `MakeSureInGame()`

Returns false and logs to console if not in a game.Meant to be used in custom console commands.

```csharp
protected static bool MakeSureInGame()
```

**Returns:** `bool`

### `MakeSureNetworked()`

Returns false and logs to console if not in a networking context.Meant to be used in custom console commands.

```csharp
protected static bool MakeSureNetworked()
```

**Returns:** `bool`

### `MakeSureNotInGame()`

Returns false and logs to console if in a game.Meant to be used in custom console commands.

```csharp
protected static bool MakeSureNotInGame()
```

**Returns:** `bool`

### `MakeSureServer()`

Returns false and logs to console if user is not a server.Meant to be used in custom console commands.

```csharp
protected static bool MakeSureServer()
```

**Returns:** `bool`

### `OnConfigChanged()`

```csharp
public virtual void OnConfigChanged()
```

### `PrintNoEntitySelected()`

```csharp
protected static void PrintNoEntitySelected()
```

### `RegisterConsoleCommand(MethodInfo, string, string)`

Register a command by method info. The method can be either static or not.Command with same name and signature will get a number appended.The command will be automatically unregistered on mod unload.

```csharp
public void RegisterConsoleCommand(MethodInfo m, string customName = null, string description = null)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `m` | `System.Reflection.MethodInfo` |  |
| `customName` | `string` |  |
| `description` | `string` |  |

### `RegisterConsoleCommand(string, string, string)`

Register a command by method name. The method can be either static or not.Command with same name and signature will get a number appended.The command will be automatically unregistered on mod unload.

```csharp
public void RegisterConsoleCommand(string methodName, string customName = null, string description = null)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `methodName` | `string` |  |
| `customName` | `string` |  |
| `description` | `string` |  |

### `SaveConfigsToDisk()`

```csharp
public virtual void SaveConfigsToDisk()
```

### `TryGetConsoleSelectedEntity(out Entity)`

```csharp
protected static bool TryGetConsoleSelectedEntity(out Entity ent)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `ent` | [Entity](/api/Global.Entity) |  |

**Returns:** `bool`
