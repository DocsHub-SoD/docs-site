# Class: ModBehaviour

- **Category:** <span class="cat-dot" style="--cat-color: #64748b" data-cat="Misc & Utility"></span> Misc & Utility
- **Namespace:** `Global`
- **Assembly:** `Dew.Core.dll`

```csharp
public class ModBehaviour : MonoBehaviour
```

## Fields (1)

::: details Click to expand Fields (1)

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`instance`** | `[NonSerialized] public LoadedModInstance instance` |  |

:::

## Properties (3)

::: details Click to expand Properties (3)

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`harmony`** | `public Harmony harmony { get; }` |  |
| **`mod`** | `public ModItem mod { get; }` |  |
| **`modConfigFields`** | `public FieldInfo[] modConfigFields { get; }` |  |

:::

## Methods (16)

::: details `CallOnManager&lt;T&gt;(Action, Action)`

```csharp
public void CallOnManager<T>(Action onEnable, Action onDisable = null) where T : ManagerBase<T>
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `onEnable` | `System.Action` |  |
| `onDisable` | `System.Action` |  |
| `` | `T` |  |

:::

::: details `CallOnNetworkedManager&lt;T&gt;(Action, Action)`

```csharp
public void CallOnNetworkedManager<T>(Action onStartClient, Action onStopClient = null) where T : NetworkedManagerBase<T>
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `onStartClient` | `System.Action` |  |
| `onStopClient` | `System.Action` |  |
| `` | `T` |  |

:::

::: details `GetConsoleSelectedEntity()`

```csharp
protected static Entity GetConsoleSelectedEntity()
```

**Returns:** `Entity`

:::

::: details `GetModConfigFilePath(FieldInfo)`

```csharp
public virtual string GetModConfigFilePath(FieldInfo modConfigInfo)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `modConfigInfo` | `System.Reflection.FieldInfo` |  |

**Returns:** `string`

:::

::: details `LoadConfigsToDisk()`

```csharp
public virtual void LoadConfigsToDisk()
```

:::

::: details `MakeSureClientNonServer()`

Returns false and logs to console if user is not a non-server client.Meant to be used in custom console commands.

```csharp
protected static bool MakeSureClientNonServer()
```

**Returns:** `bool`

:::

::: details `MakeSureInGame()`

Returns false and logs to console if not in a game.Meant to be used in custom console commands.

```csharp
protected static bool MakeSureInGame()
```

**Returns:** `bool`

:::

::: details `MakeSureNetworked()`

Returns false and logs to console if not in a networking context.Meant to be used in custom console commands.

```csharp
protected static bool MakeSureNetworked()
```

**Returns:** `bool`

:::

::: details `MakeSureNotInGame()`

Returns false and logs to console if in a game.Meant to be used in custom console commands.

```csharp
protected static bool MakeSureNotInGame()
```

**Returns:** `bool`

:::

::: details `MakeSureServer()`

Returns false and logs to console if user is not a server.Meant to be used in custom console commands.

```csharp
protected static bool MakeSureServer()
```

**Returns:** `bool`

:::

::: details `OnConfigChanged()`

```csharp
public virtual void OnConfigChanged()
```

:::

::: details `PrintNoEntitySelected()`

```csharp
protected static void PrintNoEntitySelected()
```

:::

::: details `RegisterConsoleCommand(MethodInfo, string, string)`

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

:::

::: details `RegisterConsoleCommand(string, string, string)`

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

:::

::: details `SaveConfigsToDisk()`

```csharp
public virtual void SaveConfigsToDisk()
```

:::

::: details `TryGetConsoleSelectedEntity(out Entity)`

```csharp
protected static bool TryGetConsoleSelectedEntity(out Entity ent)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `ent` | [`Entity`](/api/Global.Entity) |  |

**Returns:** `bool`

:::


## Architecture & Relationships

::: details Click to expand Architecture & Relationships

### Used By (1)

*Classes and systems that invoke, reference, or depend on `ModBehaviour`:*

[DewMod](/api/Global.DewMod)

### Dependencies (6)

*Types and components that `ModBehaviour` references or depends upon:*

[DewPersistence](/api/Global.DewPersistence) · [Entity](/api/Global.Entity) · [LoadedModInstance](/api/Global.LoadedModInstance) · [ManagerBase`1](/api/Global.ManagerBase`1) · [ModItem](/api/Global.ModItem) · [NetworkedManagerBase`1](/api/Global.NetworkedManagerBase`1)

:::
