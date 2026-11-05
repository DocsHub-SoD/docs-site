# Class: RoomModifiers

- **Namespace:** `Global`
- **Assembly:** `Dew.Core.dll`
- **Inheritance / Derived:** [DewNetworkBehaviour](/api/Global.DewNetworkBehaviour) → [RoomComponent](/api/Global.RoomComponent)

```csharp
public class RoomModifiers : RoomComponent, ILogicUpdate
```

## Fields

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`modifierInstances`** | `[NonSerialized]
public List&lt;RoomModifierBase&gt; modifierInstances` | Available on server. |

## Methods

### `OnRoomStartServer()`

```csharp
public override void OnRoomStartServer()
```
