# Class: RoomModifiers

- **Category:** <span class="cat-dot" style="--cat-color: #3b82f6" data-cat="Managers & Systems"></span> Managers & Systems
- **Namespace:** `Global`
- **Assembly:** `Dew.Core.dll`
- **Inheritance / Derived:** [DewNetworkBehaviour](/api/Global.DewNetworkBehaviour) → [RoomComponent](/api/Global.RoomComponent)

```csharp
public class RoomModifiers : RoomComponent, ILogicUpdate
```

## Fields

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`modifierInstances`** | `[NonSerialized] public List<RoomModifierBase> modifierInstances` | Available on server. |

## Methods

### `OnRoomStartServer()`

```csharp
public override void OnRoomStartServer()
```
