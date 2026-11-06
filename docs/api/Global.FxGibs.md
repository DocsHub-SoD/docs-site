# Class: FxGibs

- **Category:** <span class="cat-dot" style="--cat-color: #64748b" data-cat="Misc & Utility"></span> Misc & Utility
- **Namespace:** `Global`
- **Assembly:** `Dew.Core.dll`
- **Inheritance / Derived:** [FxInterpolatedEffectBase](/api/Global.FxInterpolatedEffectBase)

```csharp
public class FxGibs : FxInterpolatedEffectBase, IEffectComponent, IEffectWithSpeed
```

## Fields (5)

::: details Click to expand Fields (5)

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`angularSpeed`** | `public float angularSpeed` |  |
| **`info`** | `[HideInInspector] public GibInfo? info` |  |
| **`maxImpulse`** | `public float maxImpulse` |  |
| **`minImpulse`** | `public float minImpulse` |  |
| **`randomImpulse`** | `public float randomImpulse` |  |

:::

## Methods (4)

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

::: details `Stop()`

```csharp
public override void Stop()
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
