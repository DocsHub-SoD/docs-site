# Class: FxVolume

- **Category:** <span class="cat-dot" style="--cat-color: #64748b" data-cat="Misc & Utility"></span> Misc & Utility
- **Namespace:** `Global`
- **Assembly:** `Dew.Core.dll`
- **Inheritance / Derived:** [FxInterpolatedEffectBase](/api/Global.FxInterpolatedEffectBase)

```csharp
[RequireComponent(typeof(Volume))]
public class FxVolume : FxInterpolatedEffectBase, IEffectComponent, IEffectWithSpeed, IEffectWithOwnerContext
```

## Fields (3)

::: details Click to expand Fields (3)

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`otherPlayersMultiplier`** | `[ShowIf("useCustomOtherPlayersMultiplier", true)] public float otherPlayersMultiplier` |  |
| **`targetStrength`** | `public float targetStrength` |  |
| **`useCustomOtherPlayersMultiplier`** | `[ToggleLeft] public bool useCustomOtherPlayersMultiplier` |  |

:::

## Methods (6)

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

::: details `SetOwnerContext(EffectOwnerContext)`

```csharp
public void SetOwnerContext(EffectOwnerContext context)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `context` | [`EffectOwnerContext`](/api/Global.EffectOwnerContext) |  |

:::

::: details `Start()`

```csharp
protected override void Start()
```

:::

::: details `UpdateVolume()`

```csharp
public void UpdateVolume()
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
