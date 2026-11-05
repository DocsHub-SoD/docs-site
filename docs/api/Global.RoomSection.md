# Class: RoomSection

- **Namespace:** `Global`
- **Assembly:** `Dew.Core.dll`
- **Inheritance / Derived:** [LogicBehaviour](/api/Global.LogicBehaviour)

```csharp
[RequireComponent(typeof(RoomSavedObject))]
[RequireComponent(typeof(Section_Monsters))]
[RequireComponent(typeof(Section_Props))]
public class RoomSection : LogicBehaviour, ILogicUpdate, IPlayerPathablePoint
```

## Fields

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`BanSpotsDistance`** | `public const float BanSpotsDistance = 3.25` |  |
| **`clearRoomOnEnterFirstTime`** | `[ToggleLeft]
public bool clearRoomOnEnterFirstTime` |  |
| **`onEnterFirstTime`** | `[FoldoutGroup("Events", 0)]
public UnityEvent onEnterFirstTime` |  |
| **`onEntitiesChanged`** | `[FoldoutGroup("Events", 0)]
public UnityEvent onEntitiesChanged` |  |
| **`onEntityEnter`** | `[FoldoutGroup("Events", 0)]
public UnityEvent&lt;Entity&gt; onEntityEnter` |  |
| **`onEntityExit`** | `[FoldoutGroup("Events", 0)]
public UnityEvent&lt;Entity&gt; onEntityExit` |  |
| **`onEveryonePresent`** | `[FoldoutGroup("Events", 0)]
public UnityEvent onEveryonePresent` |  |
| **`vectors`** | `public Vector2[] vectors` |  |
| **`waitForAggroedEnemiesToDie`** | `[ToggleLeft]
[ShowIf("clearRoomOnEnterFirstTime", true)]
public bool waitForAggroedEnemiesToDie` |  |

## Properties

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`area`** | `public float area { get; }` |  |
| **`entities`** | `public IReadOnlyList&lt;Entity&gt; entities { get; }` |  |
| **`monsters`** | `public Section_Monsters monsters { get; }` |  |
| **`nodes`** | `public IReadOnlyList&lt;Vector3&gt; nodes { get; }` |  |
| **`numOfHeroes`** | `public int numOfHeroes { get; }` |  |
| **`pathablePivot`** | `public Vector3 pathablePivot { get; }` |  |
| **`props`** | `public Section_Props props { get; }` |  |

## Methods

### `GetAnyRandomNode()`

Get any random node.

```csharp
public Vector3 GetAnyRandomNode()
```

**Returns:** `UnityEngine.Vector3`

### `GetGoodWanderPosition(Vector3)`

```csharp
public Vector3 GetGoodWanderPosition(Vector3 from)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `from` | `UnityEngine.Vector3` |  |

**Returns:** `UnityEngine.Vector3`

### `GetNavDistanceTo(RoomSection)`

```csharp
public float GetNavDistanceTo(RoomSection sec)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `sec` | [RoomSection](/api/Global.RoomSection) |  |

**Returns:** `float`

### `GetRandomLocalPosition(DewRandom)`

```csharp
public Vector3 GetRandomLocalPosition(DewRandom random = null)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `random` | [DewRandom](/api/Global.DewRandom) |  |

**Returns:** `UnityEngine.Vector3`

### `GetRandomWorldPosition(DewRandom)`

```csharp
public Vector3 GetRandomWorldPosition(DewRandom random = null)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `random` | [DewRandom](/api/Global.DewRandom) |  |

**Returns:** `UnityEngine.Vector3`

### `LogicUpdate(float)`

```csharp
public override void LogicUpdate(float dt)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `dt` | `float` |  |

### `OnDisable()`

```csharp
protected override void OnDisable()
```

### `OnEnable()`

```csharp
protected override void OnEnable()
```

### `OverlapPoint(Vector2)`

Available only on runtime.

```csharp
public bool OverlapPoint(Vector2 point)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `point` | `UnityEngine.Vector2` |  |

**Returns:** `bool`

### `ResetUsedNodeIndices()`

```csharp
public void ResetUsedNodeIndices()
```

### `TryGetGoodNodePosition(out Vector3, DewRandom)`

Try to pick a node that hasn't been used that's not too close to previously used node.Returns false if suboptimal position is returned.

```csharp
public bool TryGetGoodNodePosition(out Vector3 position, DewRandom random = null)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `position` | `UnityEngine.Vector3` |  |
| `random` | [DewRandom](/api/Global.DewRandom) |  |

**Returns:** `bool`
