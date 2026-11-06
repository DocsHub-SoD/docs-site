# Class: Knockback

- **Category:** <span class="cat-dot" style="--cat-color: #64748b" data-cat="Misc & Utility"></span> Misc & Utility
- **Namespace:** `Global`
- **Assembly:** `Dew.Core.dll`

```csharp
[Serializable]
public class Knockback
```

## Fields (3)

::: details Click to expand Fields (3)

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`distance`** | `public float distance` |  |
| **`duration`** | `public float duration` |  |
| **`ignoreTenacity`** | `public bool ignoreTenacity` |  |

:::

## Methods (3)

::: details `ApplyWithDirection(Quaternion, Entity)`

```csharp
public void ApplyWithDirection(Quaternion rot, Entity to)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `rot` | `UnityEngine.Quaternion` |  |
| `to` | [`Entity`](/api/Global.Entity) |  |

:::

::: details `ApplyWithDirection(Vector3, Entity)`

```csharp
public void ApplyWithDirection(Vector3 dir, Entity to)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `dir` | `UnityEngine.Vector3` |  |
| `to` | [`Entity`](/api/Global.Entity) |  |

:::

::: details `ApplyWithOrigin(Vector3, Entity)`

```csharp
public void ApplyWithOrigin(Vector3 origin, Entity to)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `origin` | `UnityEngine.Vector3` |  |
| `to` | [`Entity`](/api/Global.Entity) |  |

:::
