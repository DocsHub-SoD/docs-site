# Class: ActionBase

- **Namespace:** `Global`
- **Assembly:** `Dew.Core.dll`
- **Inheritance / Derived:** [ActionAttackMove](/api/Global.ActionAttackMove) → [ActionCast](/api/Global.ActionCast) → [ActionInteract](/api/Global.ActionInteract)

```csharp
public class ActionBase
```

## Fields

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`isAllowedToMove`** | `public bool isAllowedToMove` |  |

## Properties

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`isFirstTick`** | `public bool isFirstTick { get; }` |  |

## Methods

### `GetMoveDestination()`

```csharp
public virtual Vector3? GetMoveDestination()
```

**Returns:** `UnityEngine.Vector3?`

### `GetMoveDestinationRequiredDistance()`

```csharp
public virtual float GetMoveDestinationRequiredDistance()
```

**Returns:** `float`

### `ShouldCancelIfDisallowedToMove()`

```csharp
public virtual bool ShouldCancelIfDisallowedToMove()
```

**Returns:** `bool`

### `Tick()`

Returns true if complete.

```csharp
public virtual bool Tick()
```

**Returns:** `bool`
