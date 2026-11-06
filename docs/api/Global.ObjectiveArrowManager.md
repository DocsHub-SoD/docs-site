# Class: ObjectiveArrowManager

- **Category:** <span class="cat-dot" style="--cat-color: #3b82f6" data-cat="Managers & Systems"></span> Managers & Systems
- **Namespace:** `Global`
- **Assembly:** `Dew.Core.dll`
- **Attributes:** `[LogicUpdatePriority]`
- **Inheritance / Derived:** [LogicBehaviour](/api/Global.LogicBehaviour) → `ManagerBase` → [ObjectiveArrowManager](/api/Global.ObjectiveArrowManager)

```csharp
[LogicUpdatePriority(3000)]
public class ObjectiveArrowManager : ManagerBase<ObjectiveArrowManager>, ILogicUpdate
```

## Fields (2)

::: details Click to expand Fields (2)

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`arrowPivot`** | `public GameObject arrowPivot` |  |
| **`objectivePosition`** | `public Vector3? objectivePosition` |  |

:::

## Methods (1)

::: details `FrameUpdate()`

```csharp
public override void FrameUpdate()
```

:::


## Architecture & Relationships

::: details Click to expand Architecture & Relationships

### Used By (0)

*No incoming dependencies recorded.*

### Dependencies (8)

*Types and components that `ObjectiveArrowManager` references or depends upon:*

[Actor](/api/Global.Actor) · [CameraManager](/api/Global.CameraManager) · [EntityCheck](/api/Global.EntityCheck) · [LogicBehaviour](/api/Global.LogicBehaviour) · [ManagerBase`1](/api/Global.ManagerBase`1) · [NetworkedManagerBase`1](/api/Global.NetworkedManagerBase`1) · `QuaternionFlattenExtension` · [SafeAction`1](/api/Global.SafeAction`1)

:::
