# Class: ConsoleManager

- **Namespace:** `Global`
- **Assembly:** `Dew.Core.dll`
- **Inheritance / Derived:** [DewNetworkBehaviour](/api/Global.DewNetworkBehaviour) → `NetworkedManagerBase` → [ConsoleManager](/api/Global.ConsoleManager)

```csharp
public class ConsoleManager : NetworkedManagerBase<ConsoleManager>, ILogicUpdate
```

## Fields

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`activeCommandBinds`** | `[NonSerialized]
public List&lt;ConsoleBindItem&gt; activeCommandBinds` |  |
| **`ClientEvent_OnCheatEnabledChanged`** | `public SafeAction&lt;bool&gt; ClientEvent_OnCheatEnabledChanged` |  |
| **`executionContext`** | `public ConsoleManager.ExecutionContext executionContext` |  |
| **`glDrawMaterial`** | `public Material glDrawMaterial` |  |
| **`localSelectedEntity`** | `public Entity localSelectedEntity` |  |

## Properties

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`isCheatEnabled`** | `public bool isCheatEnabled { get; }` |  |
| **`isConsoleWindowOpen`** | `public bool isConsoleWindowOpen { get; }` |  |

## Methods

### `DisableCheats()`

```csharp
public void DisableCheats()
```

### `EnableCheats()`

```csharp
public void EnableCheats()
```

### `ExecuteAutoExec(AutoExecKey)`

```csharp
public void ExecuteAutoExec(ConsoleManager.AutoExecKey key)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `key` | [ConsoleManager.AutoExecKey](/api/Global.ConsoleManager) |  |

### `ExecuteServerCommand(char[], Entity, Vector3, NetworkConnectionToClient)`

```csharp
public void ExecuteServerCommand(char[] charCommand, Entity selected, Vector3 cursorWorldPos, NetworkConnectionToClient sender = null)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `charCommand` | `char[]` |  |
| `selected` | [Entity](/api/Global.Entity) |  |
| `cursorWorldPos` | `UnityEngine.Vector3` |  |
| `sender` | `Mirror.NetworkConnectionToClient` |  |

### `FrameUpdate()`

```csharp
public override void FrameUpdate()
```

### `LogicUpdate(float)`

```csharp
public override void LogicUpdate(float dt)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `dt` | `float` |  |

### `OnDestroy()`

```csharp
protected override void OnDestroy()
```

### `OnGameAreaPointerDown(PointerEventData)`

```csharp
public void OnGameAreaPointerDown(PointerEventData eventData)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `eventData` | `UnityEngine.EventSystems.PointerEventData` |  |

### `OnLateStart()`

```csharp
public override void OnLateStart()
```

### `OnStartClient()`

```csharp
public override void OnStartClient()
```

### `ShouldSkipAutoExec()`

```csharp
public bool ShouldSkipAutoExec()
```

**Returns:** `bool`
