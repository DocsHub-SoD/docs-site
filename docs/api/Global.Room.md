# Class: Room

- **Namespace:** `Global`
- **Assembly:** `Dew.Core.dll`
- **Inheritance / Derived:** [DewNetworkBehaviour](/api/Global.DewNetworkBehaviour) → `SingletonDewNetworkBehaviour` → [Room](/api/Global.Room)

```csharp
[RequireComponent(typeof(RoomMap))]
[RequireComponent(typeof(RoomMonsters))]
[RequireComponent(typeof(RoomProps))]
[RequireComponent(typeof(RoomRifts))]
[RequireComponent(typeof(RoomRewards))]
[RequireComponent(typeof(RoomModifiers))]
[RequireComponent(typeof(RoomEditorMaintenance))]
public class Room : SingletonDewNetworkBehaviour<Room>, ILogicUpdate
```

## Fields

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`availableCameraAngles`** | `public float[] availableCameraAngles` |  |
| **`ClientEvent_OnFootstep`** | `public SafeAction&lt;Entity&gt; ClientEvent_OnFootstep` | Called everywhere everytime a footstep is done on an entity. |
| **`ClientEvent_OnPrepareAsNonHostileRoom`** | `public SafeAction ClientEvent_OnPrepareAsNonHostileRoom` |  |
| **`ClientEvent_OnRoomClear`** | `public SafeAction ClientEvent_OnRoomClear` |  |
| **`ClientEvent_OnRoomStart`** | `public SafeAction ClientEvent_OnRoomStart` |  |
| **`ClientEvent_WaypointLocked`** | `public SafeAction&lt;Room_Waypoint&gt; ClientEvent_WaypointLocked` |  |
| **`ClientEvent_WaypointUnlocked`** | `public SafeAction&lt;Room_Waypoint&gt; ClientEvent_WaypointUnlocked` |  |
| **`defaultSurface`** | `public DewSurfaceData defaultSurface` |  |
| **`metadata`** | `[ReadOnly]
public DewRoomMetadata metadata` |  |
| **`music`** | `public DewMusicItem music` |  |
| **`onRemoveObstacles`** | `public SafeAction onRemoveObstacles` | This is called on server when this room needs to clear any progression obstacles.e.g. Barriers, Locked Shrines of Despair |
| **`onRoomClear`** | `[FoldoutGroup("Events", 0)]
public UnityEvent onRoomClear` | Called on server when all combat sections are cleared / a hero steps on clear condition section. |
| **`openRoomExitOnClear`** | `[ToggleLeft]
public bool openRoomExitOnClear` |  |
| **`playerPathablePoints`** | `public readonly List&lt;Vector3&gt; playerPathablePoints` | Available everywhere. |

## Properties

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`didClearRoom`** | `public bool didClearRoom { get; }` | Available on server. |
| **`didRemoveObstacles`** | `public bool didRemoveObstacles { get; set; }` | Available on server. |
| **`heroSpawnPos`** | `public Vector3 heroSpawnPos { get; }` | Available on server. |
| **`heroSpawnRot`** | `public Quaternion heroSpawnRot { get; }` | Available on server. |
| **`isActive`** | `public bool isActive { get; }` |  |
| **`isNonHostileRoom`** | `public bool isNonHostileRoom { get; set; }` | Is this room modified to be a non-hostile room? Available everywhere. |
| **`isRevisit`** | `public bool isRevisit { get; set; }` | Are we revisiting this room? Available everywhere. |
| **`map`** | `public RoomMap map { get; }` |  |
| **`modifiers`** | `public RoomModifiers modifiers { get; }` |  |
| **`monsters`** | `public RoomMonsters monsters { get; }` |  |
| **`numOfActivatedCombatAreas`** | `public int numOfActivatedCombatAreas { get; }` |  |
| **`props`** | `public RoomProps props { get; }` |  |
| **`rewards`** | `public RoomRewards rewards { get; }` |  |
| **`rifts`** | `public RoomRifts rifts { get; }` |  |
| **`sections`** | `public IList&lt;RoomSection&gt; sections { get; }` |  |
| **`unlockedWaypoints`** | `public IReadOnlyList&lt;Room_Waypoint&gt; unlockedWaypoints { get; }` |  |

## Methods

### `AddUnlockedWaypoint(Room_Waypoint)`

```csharp
public void AddUnlockedWaypoint(Room_Waypoint waypoint)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `waypoint` | [Room_Waypoint](/api/Global.Room_Waypoint) |  |

### `Awake()`

```csharp
protected override void Awake()
```

### `ClearRoom()`

```csharp
public void ClearRoom()
```

### `GetFinalSection()`

Get a section closest to exit rift.

```csharp
public RoomSection GetFinalSection()
```

**Returns:** `RoomSection`

### `GetHeroSpawnPosition()`

Get randomly offset spawn position.

```csharp
public Vector3 GetHeroSpawnPosition()
```

**Returns:** `UnityEngine.Vector3`

### `GetHeroSpawnRotation()`

Get spawn rotation.

```csharp
public Quaternion GetHeroSpawnRotation()
```

**Returns:** `UnityEngine.Quaternion`

### `GetRoomRandom(int)`

Get a random instance for this room. States for these random instances are persistent.

```csharp
public DewRandom GetRoomRandom(int offset)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `offset` | `int` |  |

**Returns:** `DewRandom`

### `GetSectionFromWorldPos(Vector3)`

```csharp
public RoomSection GetSectionFromWorldPos(Vector3 pos)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `pos` | `UnityEngine.Vector3` |  |

**Returns:** `RoomSection`

### `OnLateStart()`

```csharp
public override void OnLateStart()
```

### `OnLateStartServer()`

```csharp
public override void OnLateStartServer()
```

### `OnStartClient()`

```csharp
public override void OnStartClient()
```

### `OnStartServer()`

```csharp
public override void OnStartServer()
```

### `OverrideHeroSpawn(Vector3, Quaternion)`

```csharp
public void OverrideHeroSpawn(Vector3 pos, Quaternion rot)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `pos` | `UnityEngine.Vector3` |  |
| `rot` | `UnityEngine.Quaternion` |  |

### `RemoveCombat(bool)`

Disables enemy spawns, and removes any existing enemies or camps.It is recommended to call this with Dew.CallDelayed() if you're calling it in RoomModifierBase.OnCreate().

```csharp
public void RemoveCombat(bool clearRoomOnEnteringLastSection)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `clearRoomOnEnteringLastSection` | `bool` |  |

### `RemoveObstacles()`

Remove any kind of progression-blocking obstacles, like barriers, locked teleport shrines and such.It is recommended to call this with Dew.CallDelayed() if you're calling it in RoomModifierBase.OnCreate().

```csharp
public void RemoveObstacles()
```

### `RemoveUnlockedWaypoint(Room_Waypoint)`

```csharp
public void RemoveUnlockedWaypoint(Room_Waypoint waypoint)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `waypoint` | [Room_Waypoint](/api/Global.Room_Waypoint) |  |

### `SetCameraAngleIndex_Local(int)`

```csharp
public void SetCameraAngleIndex_Local(int index)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `index` | `int` |  |

### `StartRoom()`

```csharp
public void StartRoom()
```

### `StopRoom()`

```csharp
public void StopRoom()
```

### `SyncCameraAngle()`

```csharp
public void SyncCameraAngle()
```
