# Class: RoomComponent

- **Category:** <span class="cat-dot" style="--cat-color: #3b82f6" data-cat="Managers & Systems"></span> Managers & Systems
- **Namespace:** `Global`
- **Assembly:** `Dew.Core.dll`
- **Inheritance / Derived:** [DewNetworkBehaviour](/api/Global.DewNetworkBehaviour) → [RoomMap](/api/Global.RoomMap) → [RoomModifiers](/api/Global.RoomModifiers) → [RoomMonsters](/api/Global.RoomMonsters) → [RoomProps](/api/Global.RoomProps) → [RoomRewards](/api/Global.RoomRewards) → [RoomRifts](/api/Global.RoomRifts)

```csharp
[RequireComponent(typeof(Room))]
public class RoomComponent : DewNetworkBehaviour, ILogicUpdate
```

## Properties (3)

::: details Click to expand Properties (3)

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`isRevisit`** | `public bool isRevisit { get; }` |  |
| **`isRoomActive`** | `public bool isRoomActive { get; }` |  |
| **`room`** | `public Room room { get; }` |  |

:::

## Methods (7)

::: details `ActiveLogicUpdate(float)`

```csharp
protected virtual void ActiveLogicUpdate(float dt)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `dt` | `float` |  |

:::

::: details `Awake()`

```csharp
protected override void Awake()
```

:::

::: details `LogicUpdate(float)`

```csharp
public override void LogicUpdate(float dt)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `dt` | `float` |  |

:::

::: details `OnRoomStart()`

Called everywhere when this room has finished loading and needs setup.

```csharp
public virtual void OnRoomStart()
```

:::

::: details `OnRoomStartServer()`

Called on server when this room has finished loading and needs setup.

```csharp
public virtual void OnRoomStartServer()
```

:::

::: details `OnRoomStop()`

Called everywhere when next room is about to load and this room is cleaning up.

```csharp
public virtual void OnRoomStop()
```

:::

::: details `OnRoomStopServer()`

Called on server when next room is about to load and this room is cleaning up.Populate save data here.

```csharp
public virtual void OnRoomStopServer()
```

:::
