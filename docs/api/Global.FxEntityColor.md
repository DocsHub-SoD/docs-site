# Class: FxEntityColor

- **Category:** <span class="cat-dot" style="--cat-color: #22c55e" data-cat="Actors & Entities"></span> Actors & Entities
- **Namespace:** `Global`
- **Assembly:** `Dew.Core.dll`
- **Inheritance / Derived:** [FxInterpolatedEffectBase](/api/Global.FxInterpolatedEffectBase)

```csharp
public class FxEntityColor : FxInterpolatedEffectBase, IEffectComponent, IEffectWithSpeed, IAttachableToEntity
```

## Fields (10)

::: details Click to expand Fields (10)

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`baseColor`** | `[ColorUsage] [ColorUsage(false, false)] [ShowIf("doBaseColor", true)] public Color baseColor` |  |
| **`dissolveAmount`** | `[ShowIf("doDissolve", true)] public float dissolveAmount` |  |
| **`dissolveColor`** | `[ColorUsage] [ColorUsage(false, true)] [ShowIf("doDissolveColor", true)] public Color dissolveColor` |  |
| **`doBaseColor`** | `public bool doBaseColor` |  |
| **`doDissolve`** | `public bool doDissolve` |  |
| **`doDissolveColor`** | `public bool doDissolveColor` |  |
| **`doEmission`** | `public bool doEmission` |  |
| **`doOpacity`** | `public bool doOpacity` |  |
| **`emission`** | `[ColorUsage] [ColorUsage(false, true)] [ShowIf("doEmission", true)] public Color emission` |  |
| **`opacity`** | `[ShowIf("doOpacity", true)] public float opacity` |  |

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

*Types and components that `FxEntityColor` references or depends upon:*

[Entity](/api/Global.Entity) · [EntityColorModifier](/api/Global.EntityColorModifier) · [EntityVisual](/api/Global.EntityVisual) · [FxInterpolatedEffectBase](/api/Global.FxInterpolatedEffectBase) · [IAttachableToEntity](/api/Global.IAttachableToEntity)

:::
