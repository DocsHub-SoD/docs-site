# Class: FxVolume

- **Category:** <span class="cat-dot" style="--cat-color: #64748b" data-cat="Misc & Utility"></span> Misc & Utility
- **Namespace:** `Global`
- **Assembly:** `Dew.Core.dll`
- **Inheritance / Derived:** [FxInterpolatedEffectBase](/api/Global.FxInterpolatedEffectBase)

```csharp
[RequireComponent(typeof(Volume))]
public class FxVolume : FxInterpolatedEffectBase, IEffectComponent, IEffectWithSpeed, IEffectWithOwnerContext
```

## Fields

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`otherPlayersMultiplier`** | `[ShowIf("useCustomOtherPlayersMultiplier", true)] public float otherPlayersMultiplier` |  |
| **`targetStrength`** | `public float targetStrength` |  |
| **`useCustomOtherPlayersMultiplier`** | `[ToggleLeft] public bool useCustomOtherPlayersMultiplier` |  |

## Methods

### `OnInit()`

```csharp
protected override void OnInit()
```

### `Play()`

```csharp
public override void Play()
```

### `SetOwnerContext(EffectOwnerContext)`

```csharp
public void SetOwnerContext(EffectOwnerContext context)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `context` | [`EffectOwnerContext`](/api/Global.EffectOwnerContext) |  |

### `Start()`

```csharp
protected override void Start()
```

### `UpdateVolume()`

```csharp
public void UpdateVolume()
```

### `ValueSetter(float)`

```csharp
protected override void ValueSetter(float value)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `value` | `float` |  |
