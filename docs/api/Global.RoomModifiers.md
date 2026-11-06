# Class: RoomModifiers

- **Category:** <span class="cat-dot" style="--cat-color: #3b82f6" data-cat="Managers & Systems"></span> Managers & Systems
- **Namespace:** `Global`
- **Assembly:** `Dew.Core.dll`
- **Inheritance / Derived:** [DewNetworkBehaviour](/api/Global.DewNetworkBehaviour) → [RoomComponent](/api/Global.RoomComponent)

```csharp
public class RoomModifiers : RoomComponent, ILogicUpdate
```

## Fields (1)

::: details Click to expand Fields (1)

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`modifierInstances`** | `[NonSerialized] public List<RoomModifierBase> modifierInstances` | Available on server. |

:::

## Methods (1)

::: details `OnRoomStartServer()`

```csharp
public override void OnRoomStartServer()
```

:::
