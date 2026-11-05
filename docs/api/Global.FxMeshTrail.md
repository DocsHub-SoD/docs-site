# Class: FxMeshTrail

- **Namespace:** `Global`
- **Assembly:** `Dew.Core.dll`
- **Inheritance / Derived:** [FxInterpolatedEffectBase](/api/Global.FxInterpolatedEffectBase)

```csharp
public class FxMeshTrail : FxInterpolatedEffectBase, IEffectComponent, IEffectWithSpeed, IAttachableToEntity
```

## Fields

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`localVelocity`** | `public Vector3 localVelocity` |  |
| **`meshTrailMaterial`** | `public Material meshTrailMaterial` |  |
| **`trailCount`** | `public int trailCount` |  |
| **`trailGradient`** | `public Gradient trailGradient` |  |
| **`trailInterval`** | `public float trailInterval` |  |
| **`worldVelocity`** | `public Vector3 worldVelocity` |  |

## Methods

### `OnAttachToEntity(Entity)`

```csharp
public void OnAttachToEntity(Entity target)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `target` | [Entity](/api/Global.Entity) |  |

### `ValueSetter(float)`

```csharp
protected override void ValueSetter(float value)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `value` | `float` |  |
