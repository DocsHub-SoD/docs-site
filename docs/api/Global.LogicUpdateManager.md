# Class: LogicUpdateManager

- **Namespace:** `Global`
- **Assembly:** `Dew.Core.dll`
- **Inheritance / Derived:** [LogicBehaviour](/api/Global.LogicBehaviour) → `ManagerBase` → [LogicUpdateManager](/api/Global.LogicUpdateManager)

```csharp
public class LogicUpdateManager : ManagerBase<LogicUpdateManager>, ILogicUpdate
```

## Fields

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`DefaultExecutionPriority`** | `public const int DefaultExecutionPriority = 0` |  |
| **`logicDeltaTime`** | `public static float logicDeltaTime` |  |
| **`MinLogicUpdateInterval`** | `public const float MinLogicUpdateInterval = 0.033333335` |  |

## Properties

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`shouldRegisterUpdates`** | `public override bool shouldRegisterUpdates { get; }` |  |

## Methods

### `Awake()`

```csharp
protected override void Awake()
```

### `Register(ILogicUpdate)`

```csharp
public static void Register(ILogicUpdate lobj)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `lobj` | [ILogicUpdate](/api/Global.ILogicUpdate) |  |

### `Unregister(ILogicUpdate)`

```csharp
public static void Unregister(ILogicUpdate lobj)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `lobj` | [ILogicUpdate](/api/Global.ILogicUpdate) |  |
