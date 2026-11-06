# Class: DispByTarget

- **Category:** <span class="cat-dot" style="--cat-color: #22c55e" data-cat="Actors & Entities"></span> Actors & Entities
- **Namespace:** `Global`
- **Assembly:** `Dew.Core.dll`
- **Inheritance / Derived:** [Displacement](/api/Global.Displacement)

```csharp
public class DispByTarget : Displacement
```

## Fields (4)

::: details Click to expand Fields (4)

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`cancelTime`** | `public float cancelTime` | Max duration of this displacement until it cancels itself.Default value is Infinity. |
| **`goalDistance`** | `public float goalDistance` | Goal distance. The displacement will finish when it reaches this distance to the target entity. |
| **`speed`** | `public float speed` | This displacement's speed in unit/s. |
| **`target`** | `public Entity target` | Target entity that this displacement will chase after. |

:::


## Architecture & Relationships

::: details Click to expand Architecture & Relationships

### Used By (0)

*No incoming dependencies recorded.*

### Dependencies (2)

*Types and components that `DispByTarget` references or depends upon:*

[Displacement](/api/Global.Displacement) · [Entity](/api/Global.Entity)

:::
