# Class: RoomSection

- **Category:** <span class="cat-dot" style="--cat-color: #3b82f6" data-cat="Managers & Systems"></span> Managers & Systems
- **Namespace:** `Global`
- **Assembly:** `Dew.Core.dll`
- **Inheritance / Derived:** [LogicBehaviour](/api/Global.LogicBehaviour)

```csharp
[RequireComponent(typeof(RoomSavedObject))]
[RequireComponent(typeof(Section_Monsters))]
[RequireComponent(typeof(Section_Props))]
public class RoomSection : LogicBehaviour, ILogicUpdate, IPlayerPathablePoint
```

## Fields (9)

::: details Click to expand Fields (9)

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`BanSpotsDistance`** | `public const float BanSpotsDistance = 3.25` |  |
| **`clearRoomOnEnterFirstTime`** | `[ToggleLeft] public bool clearRoomOnEnterFirstTime` |  |
| **`onEnterFirstTime`** | `[FoldoutGroup("Events", 0)] public UnityEvent onEnterFirstTime` |  |
| **`onEntitiesChanged`** | `[FoldoutGroup("Events", 0)] public UnityEvent onEntitiesChanged` |  |
| **`onEntityEnter`** | `[FoldoutGroup("Events", 0)] public UnityEvent<Entity> onEntityEnter` |  |
| **`onEntityExit`** | `[FoldoutGroup("Events", 0)] public UnityEvent<Entity> onEntityExit` |  |
| **`onEveryonePresent`** | `[FoldoutGroup("Events", 0)] public UnityEvent onEveryonePresent` |  |
| **`vectors`** | `public Vector2[] vectors` |  |
| **`waitForAggroedEnemiesToDie`** | `[ToggleLeft] [ShowIf("clearRoomOnEnterFirstTime", true)] public bool waitForAggroedEnemiesToDie` |  |

:::

## Properties (7)

::: details Click to expand Properties (7)

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`area`** | `public float area { get; }` |  |
| **`entities`** | `public IReadOnlyList<Entity> entities { get; }` |  |
| **`monsters`** | `public Section_Monsters monsters { get; }` |  |
| **`nodes`** | `public IReadOnlyList<Vector3> nodes { get; }` |  |
| **`numOfHeroes`** | `public int numOfHeroes { get; }` |  |
| **`pathablePivot`** | `public Vector3 pathablePivot { get; }` |  |
| **`props`** | `public Section_Props props { get; }` |  |

:::

## Methods (11)

::: details `GetAnyRandomNode()`

Get any random node.

```csharp
public Vector3 GetAnyRandomNode()
```

**Returns:** `UnityEngine.Vector3`

:::

::: details `GetGoodWanderPosition(Vector3)`

```csharp
public Vector3 GetGoodWanderPosition(Vector3 from)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `from` | `UnityEngine.Vector3` |  |

**Returns:** `UnityEngine.Vector3`

:::

::: details `GetNavDistanceTo(RoomSection)`

```csharp
public float GetNavDistanceTo(RoomSection sec)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `sec` | [`RoomSection`](/api/Global.RoomSection) |  |

**Returns:** `float`

:::

::: details `GetRandomLocalPosition(DewRandom)`

```csharp
public Vector3 GetRandomLocalPosition(DewRandom random = null)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `random` | [`DewRandom`](/api/Global.DewRandom) |  |

**Returns:** `UnityEngine.Vector3`

:::

::: details `GetRandomWorldPosition(DewRandom)`

```csharp
public Vector3 GetRandomWorldPosition(DewRandom random = null)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `random` | [`DewRandom`](/api/Global.DewRandom) |  |

**Returns:** `UnityEngine.Vector3`

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

::: details `OnDisable()`

```csharp
protected override void OnDisable()
```

:::

::: details `OnEnable()`

```csharp
protected override void OnEnable()
```

:::

::: details `OverlapPoint(Vector2)`

Available only on runtime.

```csharp
public bool OverlapPoint(Vector2 point)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `point` | `UnityEngine.Vector2` |  |

**Returns:** `bool`

:::

::: details `ResetUsedNodeIndices()`

```csharp
public void ResetUsedNodeIndices()
```

:::

::: details `TryGetGoodNodePosition(out Vector3, DewRandom)`

Try to pick a node that hasn't been used that's not too close to previously used node.Returns false if suboptimal position is returned.

```csharp
public bool TryGetGoodNodePosition(out Vector3 position, DewRandom random = null)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `position` | `UnityEngine.Vector3` |  |
| `random` | [`DewRandom`](/api/Global.DewRandom) |  |

**Returns:** `bool`

:::
