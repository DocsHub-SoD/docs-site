# Class: FxCastTelegraph

- **Category:** <span class="cat-dot" style="--cat-color: #ef4444" data-cat="Combat & Abilities"></span> Combat & Abilities
- **Namespace:** `Global`
- **Assembly:** `Dew.Core.dll`
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
| `method` | [`CastMethodType`](/api/Global.CastMethodType) |  |
| `info` | [`CastInfo`](/api/Global.CastInfo) |  |
| `duration` | `float` |  |

:::
