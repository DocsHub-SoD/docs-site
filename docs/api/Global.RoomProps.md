# Class: RoomProps

- **Category:** <span class="cat-dot" style="--cat-color: #3b82f6" data-cat="Managers & Systems"></span> Managers & Systems
- **Namespace:** `Global`
- **Assembly:** `Dew.Core.dll`
- **Inheritance / Derived:** [DewNetworkBehaviour](/api/Global.DewNetworkBehaviour) → [RoomComponent](/api/Global.RoomComponent)

```csharp
[RoomComponentStartDependency(typeof(RoomModifiers))]
public class RoomProps : RoomComponent, ILogicUpdate
```

## Fields

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`defaultPerSectionRule`** | `public PropSpawnRule defaultPerSectionRule` |  |
| **`globalRule`** | `public PropSpawnRule globalRule` |  |

## Methods

### `OnRoomStartServer()`

```csharp
public override void OnRoomStartServer()
```

### `TryGetGoodNodePosition(out Vector3, DewRandom)`

Returns false if suboptimal position is returned.

```csharp
public bool TryGetGoodNodePosition(out Vector3 position, DewRandom random = null)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `position` | `UnityEngine.Vector3` |  |
| `random` | [`DewRandom`](/api/Global.DewRandom) |  |

**Returns:** `bool`
