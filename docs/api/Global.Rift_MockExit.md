# Class: Rift_MockExit

- **Namespace:** `Global`
- **Assembly:** `Dew.Core.dll`
- **Inheritance / Derived:** [DewNetworkBehaviour](/api/Global.DewNetworkBehaviour) → [Actor](/api/Global.Actor) → [Rift](/api/Global.Rift) → [Rift_RoomExit](/api/Global.Rift_RoomExit)

```csharp
public class Rift_MockExit : Rift_RoomExit, ILogicUpdate, ICleanup, ICustomDestroyRoutine, IInteractable, IBanRoomNodesNearby, IBanRoomNodesNearbyMultiple
```

## Fields

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`onTravel`** | `public UnityEvent&lt;int&gt; onTravel` | Called on interacting client. |
