# Class: FxPointLight

- **Namespace:** `Global`
- **Assembly:** `Dew.Core.dll`
- **Inheritance / Derived:** [FxInterpolatedEffectBase](/api/Global.FxInterpolatedEffectBase)

```csharp
[RequireComponent(typeof(Light))]
public class FxPointLight : FxInterpolatedEffectBase, IEffectComponent, IEffectWithSpeed
```

## Fields

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`animateColor`** | `public bool animateColor` |  |
| **`animateIntensity`** | `public bool animateIntensity` |  |
| **`animateRange`** | `public bool animateRange` |  |
| **`colorOverValue`** | `[ShowIf("animateColor", true)]
public Gradient colorOverValue` |  |
| **`intensityMultiplier`** | `[ShowIf("animateIntensity", true)]
public float intensityMultiplier` |  |
| **`rangeMultiplier`** | `[ShowIf("animateRange", true)]
public float rangeMultiplier` |  |

## Methods

### `OnInit()`

```csharp
protected override void OnInit()
```

### `ValueSetter(float)`

```csharp
protected override void ValueSetter(float value)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `value` | `float` |  |
