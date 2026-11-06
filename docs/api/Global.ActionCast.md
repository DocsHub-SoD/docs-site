# Class: ActionCast

- **Category:** <span class="cat-dot" style="--cat-color: #ef4444" data-cat="Combat & Abilities"></span> Combat & Abilities
- **Namespace:** `Global`
- **Assembly:** `Dew.Core.dll`
- **Inheritance / Derived:** [ActionBase](/api/Global.ActionBase)

```csharp
public class ActionCast : ActionBase
```

## Fields (6)

::: details Click to expand Fields (6)

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`configIndex`** | `public int configIndex` |  |
| **`info`** | `public CastInfo info` |  |
| **`isPredictedOnCast`** | `public bool isPredictedOnCast` |  |
| **`predictTarget`** | `public Entity predictTarget` |  |
| **`skipRangeCheck`** | `public bool skipRangeCheck` |  |
| **`trigger`** | `public AbilityTrigger trigger` |  |

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
