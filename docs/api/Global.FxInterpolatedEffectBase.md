# Class: FxInterpolatedEffectBase

- **Category:** <span class="cat-dot" style="--cat-color: #a855f7" data-cat="Buffs & Statuses"></span> Buffs & Statuses
- **Namespace:** `Global`
- **Assembly:** `Dew.Core.dll`
- **Inheritance / Derived:** [FxEntityColor](/api/Global.FxEntityColor) → [FxEntityShake](/api/Global.FxEntityShake) → [FxEntityShell](/api/Global.FxEntityShell) → [FxEntityTransform](/api/Global.FxEntityTransform) → [FxGameObject](/api/Global.FxGameObject) → [FxGibs](/api/Global.FxGibs) → [FxMaterialProperty](/api/Global.FxMaterialProperty) → [FxMeshTrail](/api/Global.FxMeshTrail) → [FxPointLight](/api/Global.FxPointLight) → [FxVolume](/api/Global.FxVolume)

```csharp
public abstract class FxInterpolatedEffectBase : MonoBehaviour, IEffectComponent, IEffectWithSpeed
```

## Fields (5)

::: details Click to expand Fields (5)

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`decayTime`** | `[BoxGroup("Interpolated Effect", true, false, 0)] public float decayTime` |  |
| **`delay`** | `[BoxGroup("Interpolated Effect", true, false, 0)] public float delay` |  |
| **`isLoop`** | `[BoxGroup("Interpolated Effect", true, false, 0)] public bool isLoop` |  |
| **`startTime`** | `[BoxGroup("Interpolated Effect", true, false, 0)] public float startTime` |  |
| **`sustainTime`** | `[ShowIf("@!isLoop", true)] [BoxGroup("Interpolated Effect", true, false, 0)] public float sustainTime` |  |

:::

## Properties (4)

::: details Click to expand Properties (4)

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`currentLinearValue`** | `public float currentLinearValue { get; set; }` |  |
| **`currentValue`** | `public float currentValue { get; set; }` |  |
| **`isEmitting`** | `public bool isEmitting { get; }` |  |
| **`isPlaying`** | `public bool isPlaying { get; }` |  |

:::

## Methods (8)

::: details `ApplySpeedMultiplier(float)`

```csharp
public void ApplySpeedMultiplier(float speed)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `speed` | `float` |  |

:::

::: details `Awake()`

```csharp
protected void Awake()
```

:::

::: details `OnInit()`

Guaranteed to be called once when this effect starts, before this effect sets a value.

```csharp
protected virtual void OnInit()
```

:::

::: details `Play()`

```csharp
public virtual void Play()
```

:::

::: details `Start()`

```csharp
protected virtual void Start()
```

:::

::: details `Stop()`

```csharp
public virtual void Stop()
```

:::

::: details `Update()`

```csharp
protected virtual void Update()
```

:::

::: details `ValueSetter(float)`

```csharp
protected abstract void ValueSetter(float value)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `value` | `float` |  |

:::


## Architecture & Relationships

::: details Click to expand Architecture & Relationships

### Used By (15)

*Classes and systems that invoke, reference, or depend on `FxInterpolatedEffectBase`:*

`BossSeekerKillBehavior` · [DewEffect](/api/Global.DewEffect) · `FxAnimatorBoneOffset` · `FxCanvasGroup` · [FxEntityColor](/api/Global.FxEntityColor) · [FxEntityShake](/api/Global.FxEntityShake) · [FxEntityShell](/api/Global.FxEntityShell) · [FxEntityTransform](/api/Global.FxEntityTransform) · [FxGameObject](/api/Global.FxGameObject) · [FxGibs](/api/Global.FxGibs) · `FxGibs_Kinematic` · [FxMaterialProperty](/api/Global.FxMaterialProperty) · [FxMeshTrail](/api/Global.FxMeshTrail) · [FxPointLight](/api/Global.FxPointLight) · [FxVolume](/api/Global.FxVolume)

### Dependencies (4)

*Types and components that `FxInterpolatedEffectBase` references or depends upon:*

[EaseFunction](/api/Global.EaseFunction) · [EasingFunction](/api/Global.EasingFunction) · [IEffectComponent](/api/Global.IEffectComponent) · [IEffectWithSpeed](/api/Global.IEffectWithSpeed)

:::
