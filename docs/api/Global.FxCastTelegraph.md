# Class: FxCastTelegraph

- **Namespace:** `Global`
- **Assembly:** `Dew.Core.dll`
- **Inheritance / Derived:** [LogicBehaviour](/api/Global.LogicBehaviour)

```csharp
[HideMonoScript]
[LogicUpdatePriority(1000)]
public class FxCastTelegraph : LogicBehaviour, ILogicUpdate
```

## Fields

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`adjustSimulationSpeed`** | `public bool adjustSimulationSpeed` |  |
| **`offset`** | `[HideIf("@position == FxCastTelegraph.PositionType.None", true)]
public FxCastTelegraph.OffsetType offset` |  |
| **`position`** | `public FxCastTelegraph.PositionType position` |  |
| **`rotation`** | `public FxCastTelegraph.RotationType rotation` |  |

## Properties

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`castInfo`** | `public CastInfo castInfo { get; }` |  |
| **`castMethod`** | `public CastMethodType castMethod { get; }` |  |

## Methods

### `FrameUpdate()`

```csharp
public override void FrameUpdate()
```

### `Setup(CastMethodType, CastInfo, float)`

```csharp
public void Setup(CastMethodType method, CastInfo info, float duration)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `method` | [CastMethodType](/api/Global.CastMethodType) |  |
| `info` | [CastInfo](/api/Global.CastInfo) |  |
| `duration` | `float` |  |
