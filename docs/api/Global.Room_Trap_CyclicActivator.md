# Class: Room_Trap_CyclicActivator

- **Namespace:** `Global`
- **Assembly:** `Dew.Core.dll`
- **Inheritance / Derived:** [DewNetworkBehaviour](/api/Global.DewNetworkBehaviour) → [Room_Trap_ActivatorBase](/api/Global.Room_Trap_ActivatorBase)

```csharp
public class Room_Trap_CyclicActivator : Room_Trap_ActivatorBase, ILogicUpdate
```

## Fields

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`activateTimes`** | `public float[] activateTimes` |  |
| **`cycleInterval`** | `public float cycleInterval` |  |
| **`minDistanceFromPlayerToBeActive`** | `public float minDistanceFromPlayerToBeActive` |  |
| **`timeScale`** | `public float timeScale` |  |

## Methods

### `LogicUpdate(float)`

```csharp
public override void LogicUpdate(float dt)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `dt` | `float` |  |
