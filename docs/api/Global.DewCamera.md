# Class: DewCamera

- **Category:** <span class="cat-dot" style="--cat-color: #3b82f6" data-cat="Managers & Systems"></span> Managers & Systems
- **Namespace:** `Global`
- **Assembly:** `Dew.Core.dll`
- **Inheritance / Derived:** [LogicBehaviour](/api/Global.LogicBehaviour) → `ManagerBase` → [DewCamera](/api/Global.DewCamera)

```csharp
[ExecuteAlways]
public class DewCamera : ManagerBase<DewCamera>, ILogicUpdate
```

## Fields (2)

::: details Click to expand Fields (2)

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`mainCamera`** | `public Camera mainCamera` |  |
| **`uiCamera`** | `public Camera uiCamera` |  |

:::

## Properties (1)

::: details Click to expand Properties (1)

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`shouldRegisterUpdates`** | `public override bool shouldRegisterUpdates { get; }` |  |

:::

## Methods (1)

::: details `Awake()`

```csharp
protected override void Awake()
```

:::
