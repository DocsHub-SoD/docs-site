# Class: FxEntityShake

- **Category:** <span class="cat-dot" style="--cat-color: #22c55e" data-cat="Actors & Entities"></span> Actors & Entities
- **Namespace:** `Global`
- **Assembly:** `Dew.Core.dll`
- **Inheritance / Derived:** [FxInterpolatedEffectBase](/api/Global.FxInterpolatedEffectBase)

```csharp
public class FxEntityShake : FxInterpolatedEffectBase, IEffectComponent, IEffectWithSpeed, IAttachableToEntity
```

## Fields

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`onlyOnXZPlane`** | `public bool onlyOnXZPlane` |  |
| **`shakeIntensity`** | `public float shakeIntensity` |  |
| **`shakeInterval`** | `public float shakeInterval` |  |
| **`useUnscaledInterval`** | `public bool useUnscaledInterval` |  |

## Methods

### `OnAttachToEntity(Entity)`

```csharp
public void OnAttachToEntity(Entity target)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `target` | [`Entity`](/api/Global.Entity) |  |

### `Update()`

```csharp
protected override void Update()
```

### `ValueSetter(float)`

```csharp
protected override void ValueSetter(float value)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `value` | `float` |  |
