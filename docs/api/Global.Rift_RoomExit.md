# Class: Rift_RoomExit

- **Category:** <span class="cat-dot" style="--cat-color: #22c55e" data-cat="Actors & Entities"></span> Actors & Entities
- **Namespace:** `Global`
- **Assembly:** `Dew.Core.dll`
- **Inheritance / Derived:** [DewNetworkBehaviour](/api/Global.DewNetworkBehaviour) → [Actor](/api/Global.Actor) → [Rift](/api/Global.Rift) → [Rift_MockExit](/api/Global.Rift_MockExit)

```csharp
public class Rift_RoomExit : Rift, ILogicUpdate, ICleanup, ICustomDestroyRoutine, IInteractable, IBanRoomNodesNearby, IBanRoomNodesNearbyMultiple
```

## Fields (3)

::: details Click to expand Fields (3)

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`forceTravelToNextZone`** | `public bool forceTravelToNextZone` |  |
| **`nextNodeIndex`** | `public int nextNodeIndex` |  |
| **`softInstance`** | `public static Rift_RoomExit softInstance` |  |

:::

## Properties (1)

::: details Click to expand Properties (1)

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`instance`** | `public static Rift_RoomExit instance { get; }` | If you expect the instance to be null, you MUST USE softInstance in Update loops.This will call FindObjectOfType if current instance is null, which can be very expensive. |

:::

## Methods (6)

::: details `Awake()`

```csharp
protected override void Awake()
```

:::

::: details `GetBanSpots()`

```csharp
public Vector3[] GetBanSpots()
```

**Returns:** `UnityEngine.Vector3[]`

:::

::: details `GetSidetrackPortalPositions(List&lt;(Vector3, Quaternion)&gt;)`

```csharp
public void GetSidetrackPortalPositions(List<(Vector3, Quaternion)> list)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `list` | `System.Collections.Generic.List<T><(UnityEngine.Vector3,UnityEngine.Quaternion)>` |  |

:::

::: details `OnCreate()`

```csharp
protected override void OnCreate()
```

:::

::: details `OnInteractRift(Hero)`

```csharp
protected override bool OnInteractRift(Hero hero)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `hero` | [`Hero`](/api/Global.Hero) |  |

**Returns:** `bool`

:::

::: details `TpcInteract(NetworkConnectionToClient)`

```csharp
public void TpcInteract(NetworkConnectionToClient target)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `target` | `Mirror.NetworkConnectionToClient` |  |

:::
