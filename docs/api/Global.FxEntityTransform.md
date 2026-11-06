# Class: FxEntityTransform

- **Category:** <span class="cat-dot" style="--cat-color: #22c55e" data-cat="Actors & Entities"></span> Actors & Entities
- **Namespace:** `Global`
- **Assembly:** `Dew.Core.dll`
- **Inheritance / Derived:** [FxInterpolatedEffectBase](/api/Global.FxInterpolatedEffectBase)

```csharp
public class FxEntityTransform : FxInterpolatedEffectBase, IEffectComponent, IEffectWithSpeed, IAttachableToEntity
```

## Fields

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`localOffset`** | `public Vector3 localOffset` |  |
| **`rotation`** | `public Vector3 rotation` |  |
| **`scaleMultiplier`** | `public Vector3 scaleMultiplier` |  |
| **`worldOffset`** | `public Vector3 worldOffset` |  |

## Methods

### `OnAttachToEntity(Entity)`

```csharp
public void OnAttachToEntity(Entity target)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `target` | [`Entity`](/api/Global.Entity) |  |

### `ValueSetter(float)`

```csharp
protected override void ValueSetter(float value)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `value` | `float` |  |
