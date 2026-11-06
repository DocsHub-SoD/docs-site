# Class: FxEntityColor

- **Category:** <span class="cat-dot" style="--cat-color: #22c55e" data-cat="Actors & Entities"></span> Actors & Entities
- **Namespace:** `Global`
- **Assembly:** `Dew.Core.dll`
- **Inheritance / Derived:** [FxInterpolatedEffectBase](/api/Global.FxInterpolatedEffectBase)

```csharp
public class FxEntityColor : FxInterpolatedEffectBase, IEffectComponent, IEffectWithSpeed, IAttachableToEntity
```

## Fields

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`baseColor`** | `[ColorUsage(false, false)] [ShowIf("doBaseColor", true)] public Color baseColor` |  |
| **`dissolveAmount`** | `[ShowIf("doDissolve", true)] public float dissolveAmount` |  |
| **`dissolveColor`** | `[ColorUsage(false, true)] [ShowIf("doDissolveColor", true)] public Color dissolveColor` |  |
| **`doBaseColor`** | `public bool doBaseColor` |  |
| **`doDissolve`** | `public bool doDissolve` |  |
| **`doDissolveColor`** | `public bool doDissolveColor` |  |
| **`doEmission`** | `public bool doEmission` |  |
| **`doOpacity`** | `public bool doOpacity` |  |
| **`emission`** | `[ColorUsage(false, true)] [ShowIf("doEmission", true)] public Color emission` |  |
| **`opacity`** | `[ShowIf("doOpacity", true)] public float opacity` |  |

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
