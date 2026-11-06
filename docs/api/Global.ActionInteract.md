# Class: ActionInteract

- **Category:** <span class="cat-dot" style="--cat-color: #22c55e" data-cat="Actors & Entities"></span> Actors & Entities
- **Namespace:** `Global`
- **Assembly:** `Dew.Core.dll`
- **Inheritance / Derived:** [ActionBase](/api/Global.ActionBase)

```csharp
public class ActionInteract : ActionBase
```

## Fields (3)

::: details Click to expand Fields (3)

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`interactable`** | `public IInteractable interactable` |  |
| **`isAlt`** | `public bool isAlt` |  |
| **`noActivation`** | `public bool noActivation` |  |

:::

## Methods (4)

::: details `GetMoveDestination()`

```csharp
public override Vector3? GetMoveDestination()
```

**Returns:** `UnityEngine.Vector3?`

:::

::: details `GetMoveDestinationRequiredDistance()`

```csharp
public override float GetMoveDestinationRequiredDistance()
```

**Returns:** `float`

:::

::: details `Tick()`

```csharp
public override bool Tick()
```

**Returns:** `bool`

:::

::: details `ToString()`

```csharp
public override string ToString()
```

**Returns:** `string`

:::


## Architecture & Relationships

::: details Click to expand Architecture & Relationships

### Used By (0)

*No incoming dependencies recorded.*

### Dependencies (10)

*Types and components that `ActionInteract` references or depends upon:*

[ActionBase](/api/Global.ActionBase) · [Actor](/api/Global.Actor) · [Entity](/api/Global.Entity) · [EntityControl](/api/Global.EntityControl) · [EntityStatus](/api/Global.EntityStatus) · `GetComponentsNonAllocExtension` · [IInteractable](/api/Global.IInteractable) · `IInteractableUnityNullCheckExtension` · [ListReturnHandle`1](/api/Global.ListReturnHandle`1) · `VectorPlaneTransformExtension`

:::
