# Class: FxAttachToEntity

- **Category:** <span class="cat-dot" style="--cat-color: #22c55e" data-cat="Actors & Entities"></span> Actors & Entities
- **Namespace:** `Global`
- **Assembly:** `Dew.Core.dll`
- **Inheritance / Derived:** [LogicBehaviour](/api/Global.LogicBehaviour)

```csharp
[HideMonoScript]
[LogicUpdatePriority(1000)]
public class FxAttachToEntity : LogicBehaviour, ILogicUpdate, IAttachableToEntity
```

## Fields (5)

::: details Click to expand Fields (5)

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`offset`** | `public FxAttachToEntity.OffsetType offset` |  |
| **`position`** | `public FxAttachToEntity.PositionType position` |  |
| **`rotation`** | `public FxAttachToEntity.RotationType rotation` |  |
| **`scale`** | `public FxAttachToEntity.ScaleType scale` |  |
| **`useFlatRotation`** | `[ToggleLeft] [HideIf("@rotation == RotationType.DoNothing", true)] public bool useFlatRotation` |  |

:::

## Properties (1)

::: details Click to expand Properties (1)

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`targetEntity`** | `public Entity targetEntity { get; }` |  |

:::

## Methods (4)

::: details `FrameUpdate()`

```csharp
public override void FrameUpdate()
```

:::

::: details `OnAttachToEntity(Entity)`

```csharp
public void OnAttachToEntity(Entity target)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `target` | [`Entity`](/api/Global.Entity) |  |

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
