# Class: Rift_RoomExit

- **Category:** <span class="cat-dot" style="--cat-color: #22c55e" data-cat="Actors & Entities"></span> Actors & Entities
- **Namespace:** `Global`
- **Assembly:** `Dew.Core.dll`
- **Inheritance / Derived:** [DewNetworkBehaviour](/api/Global.DewNetworkBehaviour) → [Actor](/api/Global.Actor) → [Rift](/api/Global.Rift) → [Rift_MockExit](/api/Global.Rift_MockExit)

```csharp
public class Rift_RoomExit : Rift, ILogicUpdate, ICleanup, ICustomDestroyRoutine, IInteractable, IBanRoomNodesNearby, IBanRoomNodesNearbyMultiple
```

## Fields

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`forceTravelToNextZone`** | `public bool forceTravelToNextZone` |  |
| **`nextNodeIndex`** | `public int nextNodeIndex` |  |
| **`softInstance`** | `public static Rift_RoomExit softInstance` |  |

## Properties

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`instance`** | `public static Rift_RoomExit instance { get; }` | If you expect the instance to be null, you MUST USE softInstance in Update loops.This will call FindObjectOfType if current instance is null, which can be very expensive. |

## Methods

### `Awake()`

```csharp
protected override void Awake()
```

### `GetBanSpots()`

```csharp
public Vector3[] GetBanSpots()
```

**Returns:** `UnityEngine.Vector3[]`

### `GetSidetrackPortalPositions(List<(Vector3, Quaternion)>)`

```csharp
public void GetSidetrackPortalPositions(List<(Vector3, Quaternion)> list)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `list` | `System.Collections.Generic.List<T><(UnityEngine.Vector3,UnityEngine.Quaternion)>` |  |

### `OnCreate()`

```csharp
protected override void OnCreate()
```

### `OnInteractRift(Hero)`

```csharp
protected override bool OnInteractRift(Hero hero)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `hero` | [`Hero`](/api/Global.Hero) |  |

**Returns:** `bool`

### `TpcInteract(NetworkConnectionToClient)`

```csharp
public void TpcInteract(NetworkConnectionToClient target)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `target` | `Mirror.NetworkConnectionToClient` |  |
