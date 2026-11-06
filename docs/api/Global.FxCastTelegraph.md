# Class: FxCastTelegraph

- **Category:** <span class="cat-dot" style="--cat-color: #ef4444" data-cat="Combat & Abilities"></span> Combat & Abilities
- **Namespace:** `Global`
- **Assembly:** `Dew.Core.dll`
- **Attributes:** `[LogicUpdatePriority]`
- **Inheritance / Derived:** [LogicBehaviour](/api/Global.LogicBehaviour)

```csharp
[HideMonoScript]
[LogicUpdatePriority(1000)]
public class FxCastTelegraph : LogicBehaviour, ILogicUpdate
```

## Fields (4)

::: details Click to expand Fields (4)

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`adjustSimulationSpeed`** | `public bool adjustSimulationSpeed` |  |
| **`offset`** | `[HideIf("@position == FxCastTelegraph.PositionType.None", true)] public FxCastTelegraph.OffsetType offset` |  |
| **`position`** | `public FxCastTelegraph.PositionType position` |  |
| **`rotation`** | `public FxCastTelegraph.RotationType rotation` |  |

:::

## Properties (2)

::: details Click to expand Properties (2)

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`castInfo`** | `public CastInfo castInfo { get; }` |  |
| **`castMethod`** | `public CastMethodType castMethod { get; }` |  |

:::

## Methods (2)

::: details `FrameUpdate()`

```csharp
public override void FrameUpdate()
```

:::

::: details `Setup(CastMethodType, CastInfo, float)`

```csharp
public void Setup(CastMethodType method, CastInfo info, float duration)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `method` | <a href="/enums#castmethodtype" class="enum-link" data-tooltip="None=0 · Cone=1 · Arrow=2 · Target=3 · Point=4">CastMethodType</a> |  |
| `info` | [`CastInfo`](/api/Global.CastInfo) |  |
| `duration` | `float` |  |

:::


## Architecture & Relationships

::: details Click to expand Architecture & Relationships

### Used By (1)

*Classes and systems that invoke, reference, or depend on `FxCastTelegraph`:*

[DewEffect](/api/Global.DewEffect)

### Dependencies (8)

*Types and components that `FxCastTelegraph` references or depends upon:*

[Actor](/api/Global.Actor) · [CastInfo](/api/Global.CastInfo) · [Entity](/api/Global.Entity) · [EntityControl](/api/Global.EntityControl) · `GetComponentsNonAllocExtension` · [ListReturnHandle`1](/api/Global.ListReturnHandle`1) · [LogicBehaviour](/api/Global.LogicBehaviour) · `QuaternionFlattenExtension`

### Related Enums (1)

*Enumerations referenced in fields, properties, or method signatures:*

<a href="/enums#castmethodtype" class="enum-link" data-tooltip="None=0 · Cone=1 · Arrow=2 · Target=3 · Point=4">CastMethodType</a>

:::
