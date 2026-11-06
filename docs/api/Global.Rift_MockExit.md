# Class: Rift_MockExit

- **Category:** <span class="cat-dot" style="--cat-color: #22c55e" data-cat="Actors & Entities"></span> Actors & Entities
- **Namespace:** `Global`
- **Assembly:** `Dew.Core.dll`
- **Inheritance / Derived:** [DewNetworkBehaviour](/api/Global.DewNetworkBehaviour) → [Actor](/api/Global.Actor) → [Rift](/api/Global.Rift) → [Rift_RoomExit](/api/Global.Rift_RoomExit)

```csharp
public class Rift_MockExit : Rift_RoomExit, ILogicUpdate, ICleanup, ICustomDestroyRoutine, IInteractable, IBanRoomNodesNearby, IBanRoomNodesNearbyMultiple
```

## Fields (1)

::: details Click to expand Fields (1)

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`onTravel`** | `public UnityEvent<int> onTravel` | Called on interacting client. |

:::


## Architecture & Relationships

::: details Click to expand Architecture & Relationships

### Used By (2)

*Classes and systems that invoke, reference, or depend on `Rift_MockExit`:*

[InGameUIManager](/api/Global.InGameUIManager) · `PlayTutorial_Tutorial_Intro`

### Dependencies (1)

*Types and components that `Rift_MockExit` references or depends upon:*

[Rift_RoomExit](/api/Global.Rift_RoomExit)

:::
