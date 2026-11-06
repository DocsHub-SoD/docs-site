# Class: FxInterpolatedEffectBase

- **Category:** <span class="cat-dot" style="--cat-color: #a855f7" data-cat="Buffs & Statuses"></span> Buffs & Statuses
- **Namespace:** `Global`
- **Assembly:** `Dew.Core.dll`
- **Inheritance / Derived:** [FxEntityColor](/api/Global.FxEntityColor) → [FxEntityShake](/api/Global.FxEntityShake) → [FxEntityShell](/api/Global.FxEntityShell) → [FxEntityTransform](/api/Global.FxEntityTransform) → [FxGameObject](/api/Global.FxGameObject) → [FxGibs](/api/Global.FxGibs) → [FxMaterialProperty](/api/Global.FxMaterialProperty) → [FxMeshTrail](/api/Global.FxMeshTrail) → [FxPointLight](/api/Global.FxPointLight) → [FxVolume](/api/Global.FxVolume)

```csharp
public abstract class FxInterpolatedEffectBase : MonoBehaviour, IEffectComponent, IEffectWithSpeed
```

## Fields

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`decayTime`** | `[BoxGroup("Interpolated Effect", true, false, 0)] public float decayTime` |  |
| **`delay`** | `[BoxGroup("Interpolated Effect", true, false, 0)] public float delay` |  |
| **`isLoop`** | `[BoxGroup("Interpolated Effect", true, false, 0)] public bool isLoop` |  |
| **`startTime`** | `[BoxGroup("Interpolated Effect", true, false, 0)] public float startTime` |  |
| **`sustainTime`** | `[ShowIf("@!isLoop", true)] [BoxGroup("Interpolated Effect", true, false, 0)] public float sustainTime` |  |

## Properties

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`currentLinearValue`** | `public float currentLinearValue { get; set; }` |  |
| **`currentValue`** | `public float currentValue { get; set; }` |  |
| **`isEmitting`** | `public bool isEmitting { get; }` |  |
| **`isPlaying`** | `public bool isPlaying { get; }` |  |

## Methods

### `ApplySpeedMultiplier(float)`

```csharp
public void ApplySpeedMultiplier(float speed)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `speed` | `float` |  |

### `Awake()`

```csharp
protected void Awake()
```

### `OnInit()`

Guaranteed to be called once when this effect starts, before this effect sets a value.

```csharp
protected virtual void OnInit()
```

### `Play()`

```csharp
public virtual void Play()
```

### `Start()`

```csharp
protected virtual void Start()
```

### `Stop()`

```csharp
public virtual void Stop()
```

### `Update()`

```csharp
protected virtual void Update()
```

### `ValueSetter(float)`

```csharp
protected abstract void ValueSetter(float value)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `value` | `float` |  |
