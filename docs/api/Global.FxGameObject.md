# Class: FxGameObject

- **Namespace:** `Global`
- **Assembly:** `Dew.Core.dll`
- **Inheritance / Derived:** [FxInterpolatedEffectBase](/api/Global.FxInterpolatedEffectBase)

```csharp
[DisallowMultipleComponent]
public class FxGameObject : FxInterpolatedEffectBase, IEffectComponent, IEffectWithSpeed
```

## Fields

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`disableWhenStopped`** | `public bool disableWhenStopped` |  |

## Methods

### `OnInit()`

```csharp
protected override void OnInit()
```

### `Play()`

```csharp
public override void Play()
```

### `ValueSetter(float)`

```csharp
protected override void ValueSetter(float value)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `value` | `float` |  |
