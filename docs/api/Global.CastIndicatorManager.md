# Class: CastIndicatorManager

- **Category:** <span class="cat-dot" style="--cat-color: #ef4444" data-cat="Combat & Abilities"></span> Combat & Abilities
- **Namespace:** `Global`
- **Assembly:** `Dew.Core.dll`
- **Inheritance / Derived:** [LogicBehaviour](/api/Global.LogicBehaviour) → `ManagerBase` → [CastIndicatorManager](/api/Global.CastIndicatorManager)

```csharp
public class CastIndicatorManager : ManagerBase<CastIndicatorManager>, ILogicUpdate
```

## Fields (5)

::: details Click to expand Fields (5)

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`arcRegion`** | `public ArcRegion arcRegion` |  |
| **`circleRegion`** | `public CircleRegion circleRegion` |  |
| **`lineRegion`** | `public LineRegion lineRegion` |  |
| **`playerOrigin`** | `public Transform playerOrigin` |  |
| **`secondaryCircleRegion`** | `public CircleRegion secondaryCircleRegion` |  |

:::

## Methods (3)

::: details `Awake()`

```csharp
protected override void Awake()
```

:::

::: details `FrameUpdate()`

```csharp
public override void FrameUpdate()
```

:::

::: details `IndicateRangeFailure(float)`

```csharp
public void IndicateRangeFailure(float range)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `range` | `float` |  |

:::


## Architecture & Relationships

::: details Click to expand Architecture & Relationships

### Used By (1)

*Classes and systems that invoke, reference, or depend on `CastIndicatorManager`:*

[ControlManager](/api/Global.ControlManager)

### Dependencies (13)

*Types and components that `CastIndicatorManager` references or depends upon:*

[AbilityTrigger](/api/Global.AbilityTrigger) · [Actor](/api/Global.Actor) · [CastInfo](/api/Global.CastInfo) · [CastMethodData](/api/Global.CastMethodData) · [ControlManager](/api/Global.ControlManager) · [Entity](/api/Global.Entity) · [EntityAbility](/api/Global.EntityAbility) · [ICastMethodDataArrow](/api/Global.ICastMethodDataArrow) · [ICastMethodDataCone](/api/Global.ICastMethodDataCone) · [ICastMethodDataPoint](/api/Global.ICastMethodDataPoint) · [ICastMethodDataTarget](/api/Global.ICastMethodDataTarget) · [LogicBehaviour](/api/Global.LogicBehaviour) · [ManagerBase`1](/api/Global.ManagerBase`1)

:::
