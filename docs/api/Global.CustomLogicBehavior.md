# Class: CustomLogicBehavior

- **Category:** <span class="cat-dot" style="--cat-color: #64748b" data-cat="Misc & Utility"></span> Misc & Utility
- **Namespace:** `Global`
- **Assembly:** `Dew.Core.dll`
- **Inheritance / Derived:** [LogicBehaviour](/api/Global.LogicBehaviour)

```csharp
public class CustomLogicBehavior : LogicBehaviour, ILogicUpdate
```

## Fields

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`onDestroy`** | `public Action onDestroy` |  |
| **`onDisable`** | `public Action onDisable` |  |
| **`onEnable`** | `public Action onEnable` |  |
| **`onFrameUpdate`** | `public Action onFrameUpdate` |  |
| **`onLogicUpdate`** | `public Action onLogicUpdate` |  |
| **`onStart`** | `public Action onStart` |  |

## Methods

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
protected virtual void OnDestroy()
```

### `OnDisable()`

```csharp
protected override void OnDisable()
```

### `OnEnable()`

```csharp
protected override void OnEnable()
```

### `Start()`

```csharp
protected virtual void Start()
```
