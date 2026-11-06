# Class: FxMeshTrail

- **Category:** <span class="cat-dot" style="--cat-color: #22c55e" data-cat="Actors & Entities"></span> Actors & Entities
- **Namespace:** `Global`
- **Assembly:** `Dew.Core.dll`
- **Inheritance / Derived:** [FxInterpolatedEffectBase](/api/Global.FxInterpolatedEffectBase)

```csharp
public class FxMeshTrail : FxInterpolatedEffectBase, IEffectComponent, IEffectWithSpeed, IAttachableToEntity
```

## Fields (6)

::: details Click to expand Fields (6)

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`localVelocity`** | `public Vector3 localVelocity` |  |
| **`meshTrailMaterial`** | `public Material meshTrailMaterial` |  |
| **`trailCount`** | `public int trailCount` |  |
| **`trailGradient`** | `public Gradient trailGradient` |  |
| **`trailInterval`** | `public float trailInterval` |  |
| **`worldVelocity`** | `public Vector3 worldVelocity` |  |

:::

## Methods (2)

::: details `OnAttachToEntity(Entity)`

```csharp
public void OnAttachToEntity(Entity target)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `target` | [`Entity`](/api/Global.Entity) |  |

:::

::: details `ValueSetter(float)`

```csharp
protected override void ValueSetter(float value)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `value` | `float` |  |

:::
