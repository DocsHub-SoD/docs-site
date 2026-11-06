# Class: DewCamera

- **Category:** <span class="cat-dot" style="--cat-color: #3b82f6" data-cat="Managers & Systems"></span> Managers & Systems
- **Namespace:** `Global`
- **Assembly:** `Dew.Core.dll`
- **Inheritance / Derived:** [LogicBehaviour](/api/Global.LogicBehaviour) → `ManagerBase` → [DewCamera](/api/Global.DewCamera)

```csharp
[ExecuteAlways]
public class DewCamera : ManagerBase<DewCamera>, ILogicUpdate
```

## Fields

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`mainCamera`** | `public Camera mainCamera` |  |
| **`uiCamera`** | `public Camera uiCamera` |  |

## Properties

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`shouldRegisterUpdates`** | `public override bool shouldRegisterUpdates { get; }` |  |

## Methods

### `Awake()`

```csharp
protected override void Awake()
```
