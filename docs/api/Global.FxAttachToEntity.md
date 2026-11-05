# Class: FxAttachToEntity

- **Namespace:** `Global`
- **Assembly:** `Dew.Core.dll`
- **Inheritance / Derived:** [LogicBehaviour](/api/Global.LogicBehaviour)

```csharp
[HideMonoScript]
[LogicUpdatePriority(1000)]
public class FxAttachToEntity : LogicBehaviour, ILogicUpdate, IAttachableToEntity
```

## Fields

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`offset`** | `public FxAttachToEntity.OffsetType offset` |  |
| **`position`** | `public FxAttachToEntity.PositionType position` |  |
| **`rotation`** | `public FxAttachToEntity.RotationType rotation` |  |
| **`scale`** | `public FxAttachToEntity.ScaleType scale` |  |
| **`useFlatRotation`** | `[ToggleLeft]
[HideIf("@rotation == RotationType.DoNothing", true)]
public bool useFlatRotation` |  |

## Properties

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`targetEntity`** | `public Entity targetEntity { get; }` |  |

## Methods

### `FrameUpdate()`

```csharp
public override void FrameUpdate()
```

### `OnAttachToEntity(Entity)`

```csharp
public void OnAttachToEntity(Entity target)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `target` | [Entity](/api/Global.Entity) |  |

### `OnDisable()`

```csharp
protected override void OnDisable()
```

### `OnEnable()`

```csharp
protected override void OnEnable()
```
