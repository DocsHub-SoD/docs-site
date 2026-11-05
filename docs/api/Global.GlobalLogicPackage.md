# Class: GlobalLogicPackage

- **Namespace:** `Global`
- **Assembly:** `Dew.Core.dll`
- **Inheritance / Derived:** [LogicBehaviour](/api/Global.LogicBehaviour) → `ManagerBase` → [GlobalLogicPackage](/api/Global.GlobalLogicPackage)

```csharp
public class GlobalLogicPackage : ManagerBase<GlobalLogicPackage>, ILogicUpdate
```

## Fields

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`showFps`** | `[NonSerialized]
public bool showFps` |  |

## Methods

### `Awake()`

```csharp
protected override void Awake()
```

### `CallOnReady(Action)`

Call the action after global package has been added. If the global package already exists, it will be called immediately.

```csharp
public static void CallOnReady(Action callback)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `callback` | `System.Action` |  |
