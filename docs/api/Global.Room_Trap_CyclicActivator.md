# Class: Room_Trap_CyclicActivator

- **Category:** <span class="cat-dot" style="--cat-color: #3b82f6" data-cat="Managers & Systems"></span> Managers & Systems
- **Namespace:** `Global`
- **Assembly:** `Dew.Core.dll`
- **Inheritance / Derived:** [DewNetworkBehaviour](/api/Global.DewNetworkBehaviour) → [Room_Trap_ActivatorBase](/api/Global.Room_Trap_ActivatorBase)

```csharp
public class Room_Trap_CyclicActivator : Room_Trap_ActivatorBase, ILogicUpdate
```

## Fields (4)

::: details Click to expand Fields (4)

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`activateTimes`** | `public float[] activateTimes` |  |
| **`cycleInterval`** | `public float cycleInterval` |  |
| **`minDistanceFromPlayerToBeActive`** | `public float minDistanceFromPlayerToBeActive` |  |
| **`timeScale`** | `public float timeScale` |  |

:::

## Methods (1)

::: details `LogicUpdate(float)`

```csharp
public override void LogicUpdate(float dt)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `dt` | `float` |  |

:::


## Architecture & Relationships

::: details Click to expand Architecture & Relationships

### Used By (0)

*No incoming dependencies recorded.*

### Dependencies (5)

*Types and components that `Room_Trap_CyclicActivator` references or depends upon:*

[Dew](/api/Global.Dew) · [DewNetworkBehaviour](/api/Global.DewNetworkBehaviour) · [NetworkedManagerBase`1](/api/Global.NetworkedManagerBase`1) · [Room_Trap_ActivatorBase](/api/Global.Room_Trap_ActivatorBase) · [ZoneManager](/api/Global.ZoneManager)

:::
