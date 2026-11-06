# Class: CustomLogicBehavior

- **Category:** <span class="cat-dot" style="--cat-color: #64748b" data-cat="Misc & Utility"></span> Misc & Utility
- **Namespace:** `Global`
- **Assembly:** `Dew.Core.dll`
- **Inheritance / Derived:** [LogicBehaviour](/api/Global.LogicBehaviour)

```csharp
public class CustomLogicBehavior : LogicBehaviour, ILogicUpdate
```

## Fields (6)

::: details Click to expand Fields (6)

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`onDestroy`** | `public Action onDestroy` |  |
| **`onDisable`** | `public Action onDisable` |  |
| **`onEnable`** | `public Action onEnable` |  |
| **`onFrameUpdate`** | `public Action onFrameUpdate` |  |
| **`onLogicUpdate`** | `public Action onLogicUpdate` |  |
| **`onStart`** | `public Action onStart` |  |

:::

## Methods (6)

::: details `FrameUpdate()`

```csharp
public override void FrameUpdate()
```

:::

::: details `LogicUpdate(float)`

```csharp
public override void LogicUpdate(float dt)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `dt` | `float` |  |

:::

::: details `OnDestroy()`

```csharp
protected virtual void OnDestroy()
```

:::

::: details `OnDisable()`

```csharp
protected override void OnDisable()
```

:::

::: details `OnEnable()`

```csharp
protected override void OnEnable()
```

:::

::: details `Start()`

```csharp
protected virtual void Start()
```

:::


## Architecture & Relationships

::: details Click to expand Architecture & Relationships

### Used By (0)

*No incoming dependencies recorded.*

### Dependencies (1)

*Types and components that `CustomLogicBehavior` references or depends upon:*

[LogicBehaviour](/api/Global.LogicBehaviour)

:::
