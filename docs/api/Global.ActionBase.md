# Class: ActionBase

- **Category:** <span class="cat-dot" style="--cat-color: #22c55e" data-cat="Actors & Entities"></span> Actors & Entities
- **Namespace:** `Global`
- **Assembly:** `Dew.Core.dll`
- **Inheritance / Derived:** [ActionAttackMove](/api/Global.ActionAttackMove) → [ActionCast](/api/Global.ActionCast) → [ActionInteract](/api/Global.ActionInteract)

```csharp
public class ActionBase
```

## Fields (1)

::: details Click to expand Fields (1)

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`isAllowedToMove`** | `public bool isAllowedToMove` |  |

:::

## Properties (1)

::: details Click to expand Properties (1)

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`isFirstTick`** | `public bool isFirstTick { get; }` |  |

:::

## Methods (4)

::: details `GetMoveDestination()`

```csharp
public virtual Vector3? GetMoveDestination()
```

**Returns:** `UnityEngine.Vector3?`

:::

::: details `GetMoveDestinationRequiredDistance()`

```csharp
public virtual float GetMoveDestinationRequiredDistance()
```

**Returns:** `float`

:::

::: details `ShouldCancelIfDisallowedToMove()`

```csharp
public virtual bool ShouldCancelIfDisallowedToMove()
```

**Returns:** `bool`

:::

::: details `Tick()`

Returns true if complete.

```csharp
public virtual bool Tick()
```

**Returns:** `bool`

:::


## Architecture & Relationships

::: details Click to expand Architecture & Relationships

### Used By (4)

*Classes and systems that invoke, reference, or depend on `ActionBase`:*

[ActionAttackMove](/api/Global.ActionAttackMove) · [ActionCast](/api/Global.ActionCast) · [ActionInteract](/api/Global.ActionInteract) · [EntityControl](/api/Global.EntityControl)

### Dependencies (1)

*Types and components that `ActionBase` references or depends upon:*

[Entity](/api/Global.Entity)

:::
