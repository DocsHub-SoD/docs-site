# Class: RoomRifts

- **Namespace:** `Global`
- **Assembly:** `Dew.Core.dll`
- **Inheritance / Derived:** [DewNetworkBehaviour](/api/Global.DewNetworkBehaviour) → [RoomComponent](/api/Global.RoomComponent)

```csharp
public class RoomRifts : RoomComponent, ILogicUpdate
```

## Fields

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`openedSidetrackRifts`** | `public List&lt;string&gt; openedSidetrackRifts` |  |

## Methods

### `CreateSidetrackRift(Rift_Sidetrack)`

Create a sidetrack rift on adequate position. This can fail if there's no position to spawn the new rift.

```csharp
public void CreateSidetrackRift(Rift_Sidetrack prefab)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `prefab` | [Rift_Sidetrack](/api/Global.Rift_Sidetrack) |  |

### `OnRoomStartServer()`

```csharp
public override void OnRoomStartServer()
```

### `OpenRifts()`

Open room exit rift.Can also spawn sidetrack rifts if combat node.

```csharp
public void OpenRifts()
```
