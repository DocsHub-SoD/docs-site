# Class: Room_Trap_ActivatorBase

- **Category:** <span class="cat-dot" style="--cat-color: #3b82f6" data-cat="Managers & Systems"></span> Managers & Systems
- **Namespace:** `Global`
- **Assembly:** `Dew.Core.dll`
- **Inheritance / Derived:** [DewNetworkBehaviour](/api/Global.DewNetworkBehaviour) → [Room_Trap_CyclicActivator](/api/Global.Room_Trap_CyclicActivator) → [Room_Trap_ProximityActivator](/api/Global.Room_Trap_ProximityActivator)

```csharp
public abstract class Room_Trap_ActivatorBase : DewNetworkBehaviour, ILogicUpdate
```

## Fields (4)

::: details Click to expand Fields (4)

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`activatedObjects`** | `public GameObject[] activatedObjects` |  |
| **`durationOfToggledTraps`** | `[HideIf("toggleTraps", true)] public float durationOfToggledTraps` |  |
| **`fxActivateEffect`** | `public GameObject fxActivateEffect` |  |
| **`toggleTraps`** | `public bool toggleTraps` |  |

:::

## Methods (1)

::: details `Activate()`

```csharp
public void Activate()
```

:::


## Architecture & Relationships

::: details Click to expand Architecture & Relationships

### Used By (2)

*Classes and systems that invoke, reference, or depend on `Room_Trap_ActivatorBase`:*

[Room_Trap_CyclicActivator](/api/Global.Room_Trap_CyclicActivator) · [Room_Trap_ProximityActivator](/api/Global.Room_Trap_ProximityActivator)

### Dependencies (1)

*Types and components that `Room_Trap_ActivatorBase` references or depends upon:*

[DewNetworkBehaviour](/api/Global.DewNetworkBehaviour)

:::
