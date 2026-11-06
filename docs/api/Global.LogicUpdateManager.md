# Class: LogicUpdateManager

- **Category:** <span class="cat-dot" style="--cat-color: #3b82f6" data-cat="Managers & Systems"></span> Managers & Systems
- **Namespace:** `Global`
- **Assembly:** `Dew.Core.dll`
- **Inheritance / Derived:** [LogicBehaviour](/api/Global.LogicBehaviour) → `ManagerBase` → [LogicUpdateManager](/api/Global.LogicUpdateManager)

```csharp
public class LogicUpdateManager : ManagerBase<LogicUpdateManager>, ILogicUpdate
```

## Fields (3)

::: details Click to expand Fields (3)

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`DefaultExecutionPriority`** | `public const int DefaultExecutionPriority = 0` |  |
| **`logicDeltaTime`** | `public static float logicDeltaTime` |  |
| **`MinLogicUpdateInterval`** | `public const float MinLogicUpdateInterval = 0.033333335` |  |

:::

## Properties (1)

::: details Click to expand Properties (1)

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`shouldRegisterUpdates`** | `public override bool shouldRegisterUpdates { get; }` |  |

:::

## Methods (3)

::: details `Awake()`

```csharp
protected override void Awake()
```

:::

::: details `Register(ILogicUpdate)`

```csharp
public static void Register(ILogicUpdate lobj)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `lobj` | [`ILogicUpdate`](/api/Global.ILogicUpdate) |  |

:::

::: details `Unregister(ILogicUpdate)`

```csharp
public static void Unregister(ILogicUpdate lobj)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `lobj` | [`ILogicUpdate`](/api/Global.ILogicUpdate) |  |

:::


## Architecture & Relationships

::: details Click to expand Architecture & Relationships

### Used By (2)

*Classes and systems that invoke, reference, or depend on `LogicUpdateManager`:*

[DewNetworkBehaviour](/api/Global.DewNetworkBehaviour) · [LogicBehaviour](/api/Global.LogicBehaviour)

### Dependencies (3)

*Types and components that `LogicUpdateManager` references or depends upon:*

[Actor](/api/Global.Actor) · [ILogicUpdate](/api/Global.ILogicUpdate) · [ManagerBase`1](/api/Global.ManagerBase`1)

:::
