# Class: TimescaleManager

- **Category:** <span class="cat-dot" style="--cat-color: #3b82f6" data-cat="Managers & Systems"></span> Managers & Systems
- **Namespace:** `Global`
- **Assembly:** `Dew.Core.dll`
- **Inheritance / Derived:** [DewNetworkBehaviour](/api/Global.DewNetworkBehaviour) → `NetworkedManagerBase` → [TimescaleManager](/api/Global.TimescaleManager)

```csharp
public class TimescaleManager : NetworkedManagerBase<TimescaleManager>, ILogicUpdate
```

## Properties (3)

::: details Click to expand Properties (3)

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`desiredTimescale`** | `public float desiredTimescale { get; set; }` |  |
| **`effectTimescale`** | `public float effectTimescale { get; }` | Timescale multiplier of DewEffect (FxStopTime and such) induced changes. |
| **`shouldTimeBeSlowedBySpecialMenu`** | `public bool shouldTimeBeSlowedBySpecialMenu { get; }` |  |

:::

## Methods (5)

::: details `ChangeTimescale(float, float)`

Lowest of all changes will apply.

```csharp
public void ChangeTimescale(float timescale, float duration)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `timescale` | `float` |  |
| `duration` | `float` |  |

:::

::: details `FrameUpdate()`

```csharp
public override void FrameUpdate()
```

:::

::: details `OnDestroy()`

```csharp
protected override void OnDestroy()
```

:::

::: details `OnStartServer()`

```csharp
public override void OnStartServer()
```

:::

::: details `TimescaleChanged(float, float)`

```csharp
public void TimescaleChanged(float oldVal, float newVal)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `oldVal` | `float` |  |
| `newVal` | `float` |  |

:::


## Architecture & Relationships

::: details Click to expand Architecture & Relationships

### Used By (2)

*Classes and systems that invoke, reference, or depend on `TimescaleManager`:*

`DewAudioManager` · [FeedbackManager](/api/Global.FeedbackManager)

### Dependencies (5)

*Types and components that `TimescaleManager` references or depends upon:*

[DewNetworkBehaviour](/api/Global.DewNetworkBehaviour) · [DewNetworkManager](/api/Global.DewNetworkManager) · [InGameUIManager](/api/Global.InGameUIManager) · [NetworkedManagerBase`1](/api/Global.NetworkedManagerBase`1) · [UIManager](/api/Global.UIManager)

:::
