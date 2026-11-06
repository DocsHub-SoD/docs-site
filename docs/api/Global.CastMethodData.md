# Class: CastMethodData

- **Category:** <span class="cat-dot" style="--cat-color: #ef4444" data-cat="Combat & Abilities"></span> Combat & Abilities
- **Namespace:** `Global`
- **Assembly:** `Dew.Core.dll`

```csharp
[Serializable]
public class CastMethodData : ICastMethodDataArrow, ICastMethodDataCone, ICastMethodDataNone, ICastMethodDataPoint, ICastMethodDataTarget
```

## Fields

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`_angle`** | `[SerializeField] [ShowIf("ShouldAngleFieldShow", true)] public float _angle` |  |
| **`_isClamping`** | `[SerializeField] [ShowIf("ShouldIsClampingFieldShow", true)] public bool _isClamping` |  |
| **`_length`** | `[SerializeField] [ShowIf("ShouldLengthFieldShow", true)] public float _length` |  |
| **`_radius`** | `[SerializeField] [ShowIf("ShouldRadiusFieldShow", true)] public float _radius` |  |
| **`_range`** | `[SerializeField] [ShowIf("ShouldRangeFieldShow", true)] public float _range` |  |
| **`_width`** | `[SerializeField] [ShowIf("ShouldWidthFieldShow", true)] public float _width` |  |
| **`type`** | `[HideLabel] [EnumToggleButtons] public CastMethodType type` |  |

## Properties

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`arrowData`** | `public ICastMethodDataArrow arrowData { get; }` |  |
| **`coneData`** | `public ICastMethodDataCone coneData { get; }` |  |
| **`noneData`** | `public ICastMethodDataNone noneData { get; }` |  |
| **`pointData`** | `public ICastMethodDataPoint pointData { get; }` |  |
| **`targetData`** | `public ICastMethodDataTarget targetData { get; }` |  |

## Methods

### `GetEffectiveRange(AbilityTrigger)`

```csharp
public float GetEffectiveRange(AbilityTrigger parent)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `parent` | [`AbilityTrigger`](/api/Global.AbilityTrigger) |  |

**Returns:** `float`
