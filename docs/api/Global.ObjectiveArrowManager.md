# Class: ObjectiveArrowManager

- **Category:** <span class="cat-dot" style="--cat-color: #3b82f6" data-cat="Managers & Systems"></span> Managers & Systems
- **Namespace:** `Global`
- **Assembly:** `Dew.Core.dll`
- **Inheritance / Derived:** [LogicBehaviour](/api/Global.LogicBehaviour) → `ManagerBase` → [ObjectiveArrowManager](/api/Global.ObjectiveArrowManager)

```csharp
[LogicUpdatePriority(3000)]
public class ObjectiveArrowManager : ManagerBase<ObjectiveArrowManager>, ILogicUpdate
```

## Fields

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`arrowPivot`** | `public GameObject arrowPivot` |  |
| **`objectivePosition`** | `public Vector3? objectivePosition` |  |

## Methods

### `FrameUpdate()`

```csharp
public override void FrameUpdate()
```
