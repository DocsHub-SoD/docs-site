# Class: FxPointLight

- **Category:** <span class="cat-dot" style="--cat-color: #64748b" data-cat="Misc & Utility"></span> Misc & Utility
- **Namespace:** `Global`
- **Assembly:** `Dew.Core.dll`
- **Attributes:** `[RequireComponent]`
- **Inheritance / Derived:** [FxInterpolatedEffectBase](/api/Global.FxInterpolatedEffectBase)

```csharp
[RequireComponent(typeof(Light))]
public class FxPointLight : FxInterpolatedEffectBase, IEffectComponent, IEffectWithSpeed
```

## Fields (6)

::: details Click to expand Fields (6)

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`animateColor`** | `public bool animateColor` |  |
| **`animateIntensity`** | `public bool animateIntensity` |  |
| **`animateRange`** | `public bool animateRange` |  |
| **`colorOverValue`** | `[ShowIf("animateColor", true)] public Gradient colorOverValue` |  |
| **`intensityMultiplier`** | `[ShowIf("animateIntensity", true)] public float intensityMultiplier` |  |
| **`rangeMultiplier`** | `[ShowIf("animateRange", true)] public float rangeMultiplier` |  |

:::

## Methods (2)

::: details `OnInit()`

```csharp
protected override void OnInit()
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


## Architecture & Relationships

::: details Click to expand Architecture & Relationships

### Used By (2)

*Classes and systems that invoke, reference, or depend on `FxPointLight`:*

`Ai_Gem_E_Fever_Explosion` · `Ai_R_StaticDischarge`

### Dependencies (1)

*Types and components that `FxPointLight` references or depends upon:*

[FxInterpolatedEffectBase](/api/Global.FxInterpolatedEffectBase)

:::
