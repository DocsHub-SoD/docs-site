# Class: FloatingWindowManager

- **Category:** <span class="cat-dot" style="--cat-color: #ec4899" data-cat="User Interface"></span> User Interface
- **Namespace:** `Global`
- **Assembly:** `Dew.Core.dll`
- **Inheritance / Derived:** [LogicBehaviour](/api/Global.LogicBehaviour) → `ManagerBase` → [FloatingWindowManager](/api/Global.FloatingWindowManager)

```csharp
public class FloatingWindowManager : ManagerBase<FloatingWindowManager>, ILogicUpdate
```

## Fields (3)

::: details Click to expand Fields (3)

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`backButtonPriority`** | `public int backButtonPriority` |  |
| **`maxDistance`** | `public float maxDistance` |  |
| **`onTargetChanged`** | `public Action<MonoBehaviour> onTargetChanged` |  |

:::

## Properties (2)

::: details Click to expand Properties (2)

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`currentTarget`** | `public MonoBehaviour currentTarget { get; }` |  |
| **`lastSetTargetUnscaledTime`** | `public float lastSetTargetUnscaledTime { get; }` |  |

:::

## Methods (4)

::: details `ClearTarget()`

```csharp
public void ClearTarget()
```

:::

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

::: details `SetTarget(MonoBehaviour)`

```csharp
public void SetTarget(MonoBehaviour newTarget)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `newTarget` | `UnityEngine.MonoBehaviour` |  |

:::
