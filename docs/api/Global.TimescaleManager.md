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
