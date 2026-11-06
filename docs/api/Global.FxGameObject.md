# Class: FxGameObject

- **Category:** <span class="cat-dot" style="--cat-color: #64748b" data-cat="Misc & Utility"></span> Misc & Utility
- **Namespace:** `Global`
- **Assembly:** `Dew.Core.dll`
- **Attributes:** `[DisallowMultipleComponent]`
- **Inheritance / Derived:** [FxInterpolatedEffectBase](/api/Global.FxInterpolatedEffectBase)

```csharp
[DisallowMultipleComponent]
public class FxGameObject : FxInterpolatedEffectBase, IEffectComponent, IEffectWithSpeed
```

## Fields (1)

::: details Click to expand Fields (1)

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`disableWhenStopped`** | `public bool disableWhenStopped` |  |

:::

## Methods (3)

::: details `OnInit()`

```csharp
protected override void OnInit()
```

:::

::: details `Play()`

```csharp
public override void Play()
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

### Used By (1)

*Classes and systems that invoke, reference, or depend on `FxGameObject`:*

`Ai_Mon_Ink_BossWhiteNight_Cataclysm_SafeZone`

### Dependencies (1)

*Types and components that `FxGameObject` references or depends upon:*

[FxInterpolatedEffectBase](/api/Global.FxInterpolatedEffectBase)

:::
