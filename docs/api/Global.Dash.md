# Class: Dash

- **Category:** <span class="cat-dot" style="--cat-color: #64748b" data-cat="Misc & Utility"></span> Misc & Utility
- **Namespace:** `Global`
- **Assembly:** `Dew.Core.dll`

```csharp
[Serializable]
public class Dash
```

## Fields (7)

::: details Click to expand Fields (7)

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`affectedByMovementSpeed`** | `public bool affectedByMovementSpeed` |  |
| **`canGoOverTerrain`** | `public bool canGoOverTerrain` |  |
| **`distance`** | `public float distance` |  |
| **`duration`** | `public float duration` |  |
| **`ease`** | `public DewEase ease` |  |
| **`rotateForward`** | `public bool rotateForward` |  |
| **`useLinearSweep`** | `public bool useLinearSweep` |  |

:::

## Methods (2)

::: details `ApplyByDestination(Entity, Vector3, Action&lt;DispByDestination&gt;)`

```csharp
public void ApplyByDestination(Entity ent, Vector3 dest, Action<DispByDestination> beforeApply = null)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `ent` | [`Entity`](/api/Global.Entity) |  |
| `dest` | `UnityEngine.Vector3` |  |
| `beforeApply` | [`System.Action<T><DispByDestination>`](/api/Global.DispByDestination) |  |

:::

::: details `ApplyByDirection(Entity, Vector3, Action&lt;DispByDestination&gt;)`

```csharp
public void ApplyByDirection(Entity ent, Vector3 dir, Action<DispByDestination> beforeApply = null)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `ent` | [`Entity`](/api/Global.Entity) |  |
| `dir` | `UnityEngine.Vector3` |  |
| `beforeApply` | [`System.Action<T><DispByDestination>`](/api/Global.DispByDestination) |  |

:::
