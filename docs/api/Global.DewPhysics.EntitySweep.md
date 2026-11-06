# Class: DewPhysics.EntitySweep

- **Category:** <span class="cat-dot" style="--cat-color: #22c55e" data-cat="Actors & Entities"></span> Actors & Entities
- **Namespace:** `Global`
- **Assembly:** `Dew.Core.dll`

```csharp
public class DewPhysics.EntitySweep
```

## Fields (5)

::: details Click to expand Fields (5)

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`ignoreDuplicateHits`** | `public bool ignoreDuplicateHits` |  |
| **`includeUncollidable`** | `public bool includeUncollidable` |  |
| **`radius`** | `public float radius` |  |
| **`validator`** | `public AbilityTargetValidator validator` |  |
| **`validatorSelf`** | `public Entity validatorSelf` |  |

:::

## Properties (2)

::: details Click to expand Properties (2)

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`current`** | `public IReadOnlyList<Entity> current { get; }` |  |
| **`lastPosition`** | `public Vector3 lastPosition { get; }` |  |

:::

## Methods (1)

::: details `Next(Vector3)`

```csharp
public IReadOnlyList<Entity> Next(Vector3 position)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `position` | `UnityEngine.Vector3` |  |

**Returns:** `System.Collections.Generic.IReadOnlyList<T><Entity>`

:::
