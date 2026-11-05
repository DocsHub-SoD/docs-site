# Class: CastIndicatorManager

- **Namespace:** `Global`
- **Assembly:** `Dew.Core.dll`
- **Inheritance / Derived:** [LogicBehaviour](/api/Global.LogicBehaviour) → `ManagerBase` → [CastIndicatorManager](/api/Global.CastIndicatorManager)

```csharp
public class CastIndicatorManager : ManagerBase<CastIndicatorManager>, ILogicUpdate
```

## Fields

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`arcRegion`** | `public ArcRegion arcRegion` |  |
| **`circleRegion`** | `public CircleRegion circleRegion` |  |
| **`lineRegion`** | `public LineRegion lineRegion` |  |
| **`playerOrigin`** | `public Transform playerOrigin` |  |
| **`secondaryCircleRegion`** | `public CircleRegion secondaryCircleRegion` |  |

## Methods

### `Awake()`

```csharp
protected override void Awake()
```

### `FrameUpdate()`

```csharp
public override void FrameUpdate()
```

### `IndicateRangeFailure(float)`

```csharp
public void IndicateRangeFailure(float range)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `range` | `float` |  |
