# Class: FxEntityTransform

- **Category:** <span class="cat-dot" style="--cat-color: #22c55e" data-cat="Actors & Entities"></span> Actors & Entities
- **Namespace:** `Global`
- **Assembly:** `Dew.Core.dll`
- **Inheritance / Derived:** [FxInterpolatedEffectBase](/api/Global.FxInterpolatedEffectBase)

```csharp
public class FxEntityTransform : FxInterpolatedEffectBase, IEffectComponent, IEffectWithSpeed, IAttachableToEntity
```

## Fields (4)

::: details Click to expand Fields (4)

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`localOffset`** | `public Vector3 localOffset` |  |
| **`rotation`** | `public Vector3 rotation` |  |
| **`scaleMultiplier`** | `public Vector3 scaleMultiplier` |  |
| **`worldOffset`** | `public Vector3 worldOffset` |  |

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


## Architecture & Relationships

::: details Click to expand Architecture & Relationships

### Used By (0)

*No incoming dependencies recorded.*

### Dependencies (5)

*Types and components that `FxEntityTransform` references or depends upon:*

[Entity](/api/Global.Entity) · [EntityTransformModifier](/api/Global.EntityTransformModifier) · [EntityVisual](/api/Global.EntityVisual) · [FxInterpolatedEffectBase](/api/Global.FxInterpolatedEffectBase) · [IAttachableToEntity](/api/Global.IAttachableToEntity)

:::
