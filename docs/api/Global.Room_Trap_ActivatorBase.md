# Class: Room_Trap_ActivatorBase

- **Namespace:** `Global`
- **Assembly:** `Dew.Core.dll`
- **Inheritance / Derived:** [DewNetworkBehaviour](/api/Global.DewNetworkBehaviour) → [Room_Trap_CyclicActivator](/api/Global.Room_Trap_CyclicActivator) → [Room_Trap_ProximityActivator](/api/Global.Room_Trap_ProximityActivator)

```csharp
public abstract class Room_Trap_ActivatorBase : DewNetworkBehaviour, ILogicUpdate
```

## Fields

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`activatedObjects`** | `public GameObject[] activatedObjects` |  |
| **`durationOfToggledTraps`** | `[HideIf("toggleTraps", true)]
public float durationOfToggledTraps` |  |
| **`fxActivateEffect`** | `public GameObject fxActivateEffect` |  |
| **`toggleTraps`** | `public bool toggleTraps` |  |

## Methods

### `Activate()`

```csharp
public void Activate()
```
