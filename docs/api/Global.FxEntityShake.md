# Class: FxEntityShake

- **Category:** <span class="cat-dot" style="--cat-color: #22c55e" data-cat="Actors & Entities"></span> Actors & Entities
- **Namespace:** `Global`
- **Assembly:** `Dew.Core.dll`
- **Inheritance / Derived:** [FxInterpolatedEffectBase](/api/Global.FxInterpolatedEffectBase)

```csharp
public class FxEntityShake : FxInterpolatedEffectBase, IEffectComponent, IEffectWithSpeed, IAttachableToEntity
```

## Fields (4)

::: details Click to expand Fields (4)

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`onlyOnXZPlane`** | `public bool onlyOnXZPlane` |  |
| **`shakeIntensity`** | `public float shakeIntensity` |  |
| **`shakeInterval`** | `public float shakeInterval` |  |
| **`useUnscaledInterval`** | `public bool useUnscaledInterval` |  |

:::

## Methods (3)

::: details `OnAttachToEntity(Entity)`

```csharp
public void OnAttachToEntity(Entity target)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `target` | [`Entity`](/api/Global.Entity) |  |

:::

::: details `Update()`

```csharp
protected override void Update()
```

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
