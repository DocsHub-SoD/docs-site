# Class: RoomComponent

- **Namespace:** `Global`
- **Assembly:** `Dew.Core.dll`
- **Inheritance / Derived:** [DewNetworkBehaviour](/api/Global.DewNetworkBehaviour) → [RoomMap](/api/Global.RoomMap) → [RoomModifiers](/api/Global.RoomModifiers) → [RoomMonsters](/api/Global.RoomMonsters) → [RoomProps](/api/Global.RoomProps) → [RoomRewards](/api/Global.RoomRewards) → [RoomRifts](/api/Global.RoomRifts)

```csharp
[RequireComponent(typeof(Room))]
public class RoomComponent : DewNetworkBehaviour, ILogicUpdate
```

## Properties

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`isRevisit`** | `public bool isRevisit { get; }` |  |
| **`isRoomActive`** | `public bool isRoomActive { get; }` |  |
| **`room`** | `public Room room { get; }` |  |

## Methods

### `ActiveLogicUpdate(float)`

```csharp
protected virtual void ActiveLogicUpdate(float dt)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `dt` | `float` |  |

### `Awake()`

```csharp
protected override void Awake()
```

### `LogicUpdate(float)`

```csharp
public override void LogicUpdate(float dt)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `dt` | `float` |  |

### `OnRoomStart()`

Called everywhere when this room has finished loading and needs setup.

```csharp
public virtual void OnRoomStart()
```

### `OnRoomStartServer()`

Called on server when this room has finished loading and needs setup.

```csharp
public virtual void OnRoomStartServer()
```

### `OnRoomStop()`

Called everywhere when next room is about to load and this room is cleaning up.

```csharp
public virtual void OnRoomStop()
```

### `OnRoomStopServer()`

Called on server when next room is about to load and this room is cleaning up.Populate save data here.

```csharp
public virtual void OnRoomStopServer()
```
