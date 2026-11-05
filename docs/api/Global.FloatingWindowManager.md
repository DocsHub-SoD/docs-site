# Class: FloatingWindowManager

- **Namespace:** `Global`
- **Assembly:** `Dew.Core.dll`
- **Inheritance / Derived:** [LogicBehaviour](/api/Global.LogicBehaviour) → `ManagerBase` → [FloatingWindowManager](/api/Global.FloatingWindowManager)

```csharp
public class FloatingWindowManager : ManagerBase<FloatingWindowManager>, ILogicUpdate
```

## Fields

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`backButtonPriority`** | `public int backButtonPriority` |  |
| **`maxDistance`** | `public float maxDistance` |  |
| **`onTargetChanged`** | `public Action&lt;MonoBehaviour&gt; onTargetChanged` |  |

## Properties

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`currentTarget`** | `public MonoBehaviour currentTarget { get; }` |  |
| **`lastSetTargetUnscaledTime`** | `public float lastSetTargetUnscaledTime { get; }` |  |

## Methods

### `ClearTarget()`

```csharp
public void ClearTarget()
```

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

### `SetTarget(MonoBehaviour)`

```csharp
public void SetTarget(MonoBehaviour newTarget)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `newTarget` | `UnityEngine.MonoBehaviour` |  |
