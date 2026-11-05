# Class: FxGibs

- **Namespace:** `Global`
- **Assembly:** `Dew.Core.dll`
- **Inheritance / Derived:** [FxInterpolatedEffectBase](/api/Global.FxInterpolatedEffectBase)

```csharp
public class FxGibs : FxInterpolatedEffectBase, IEffectComponent, IEffectWithSpeed
```

## Fields

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`angularSpeed`** | `public float angularSpeed` |  |
| **`info`** | `[HideInInspector]
public GibInfo? info` |  |
| **`maxImpulse`** | `public float maxImpulse` |  |
| **`minImpulse`** | `public float minImpulse` |  |
| **`randomImpulse`** | `public float randomImpulse` |  |

## Methods

### `OnInit()`

```csharp
protected override void OnInit()
```

### `Play()`

```csharp
public override void Play()
```

### `Stop()`

```csharp
public override void Stop()
```

### `ValueSetter(float)`

```csharp
protected override void ValueSetter(float value)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `value` | `float` |  |
