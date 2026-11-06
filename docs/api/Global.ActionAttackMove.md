# Class: ActionAttackMove

- **Category:** <span class="cat-dot" style="--cat-color: #ef4444" data-cat="Combat & Abilities"></span> Combat & Abilities
- **Namespace:** `Global`
- **Assembly:** `Dew.Core.dll`
- **Inheritance / Derived:** [ActionBase](/api/Global.ActionBase)

```csharp
public class ActionAttackMove : ActionBase
```

## Fields

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`destination`** | `public Vector3 destination` |  |
| **`useDistanceFromDestination`** | `public bool useDistanceFromDestination` |  |

## Methods

### `FindAttackMoveTarget(Entity, Vector3)`

```csharp
public static Entity FindAttackMoveTarget(Entity ent, Vector3 sortPivot)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `ent` | [`Entity`](/api/Global.Entity) |  |
| `sortPivot` | `UnityEngine.Vector3` |  |

**Returns:** `Entity`

### `GetMoveDestination()`

```csharp
public override Vector3? GetMoveDestination()
```

**Returns:** `UnityEngine.Vector3?`

### `GetMoveDestinationRequiredDistance()`

```csharp
public override float GetMoveDestinationRequiredDistance()
```

**Returns:** `float`

### `ShouldCancelIfDisallowedToMove()`

```csharp
public override bool ShouldCancelIfDisallowedToMove()
```

**Returns:** `bool`

### `Tick()`

```csharp
public override bool Tick()
```

**Returns:** `bool`

### `ToString()`

```csharp
public override string ToString()
```

**Returns:** `string`
