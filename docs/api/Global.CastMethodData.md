# Class: CastMethodData

- **Category:** <span class="cat-dot" style="--cat-color: #ef4444" data-cat="Combat & Abilities"></span> Combat & Abilities
- **Namespace:** `Global`
- **Assembly:** `Dew.Core.dll`

```csharp
[Serializable]
public class CastMethodData : ICastMethodDataArrow, ICastMethodDataCone, ICastMethodDataNone, ICastMethodDataPoint, ICastMethodDataTarget
```

## Fields (7)

::: details Click to expand Fields (7)

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`_angle`** | `[SerializeField] [SerializeField] [ShowIf("ShouldAngleFieldShow", true)] public float _angle` |  |
| **`_isClamping`** | `[SerializeField] [SerializeField] [ShowIf("ShouldIsClampingFieldShow", true)] public bool _isClamping` |  |
| **`_length`** | `[SerializeField] [SerializeField] [ShowIf("ShouldLengthFieldShow", true)] public float _length` |  |
| **`_radius`** | `[SerializeField] [SerializeField] [ShowIf("ShouldRadiusFieldShow", true)] public float _radius` |  |
| **`_range`** | `[SerializeField] [SerializeField] [ShowIf("ShouldRangeFieldShow", true)] public float _range` |  |
| **`_width`** | `[SerializeField] [SerializeField] [ShowIf("ShouldWidthFieldShow", true)] public float _width` |  |
| **`type`** | `[HideLabel] [EnumToggleButtons] public CastMethodType type` |  |

:::

## Properties (5)

::: details Click to expand Properties (5)

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`arrowData`** | `public ICastMethodDataArrow arrowData { get; }` |  |
| **`coneData`** | `public ICastMethodDataCone coneData { get; }` |  |
| **`noneData`** | `public ICastMethodDataNone noneData { get; }` |  |
| **`pointData`** | `public ICastMethodDataPoint pointData { get; }` |  |
| **`targetData`** | `public ICastMethodDataTarget targetData { get; }` |  |

:::

## Methods (1)

::: details `GetEffectiveRange(AbilityTrigger)`

```csharp
public float GetEffectiveRange(AbilityTrigger parent)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `parent` | [`AbilityTrigger`](/api/Global.AbilityTrigger) |  |

**Returns:** `float`

:::


## Architecture & Relationships

::: details Click to expand Architecture & Relationships

### Used By (11)

*Classes and systems that invoke, reference, or depend on `CastMethodData`:*

[AbilityTrigger](/api/Global.AbilityTrigger) · [ActionCast](/api/Global.ActionCast) · [CastIndicatorManager](/api/Global.CastIndicatorManager) · [CastMethodDataSerialization](/api/Global.CastMethodDataSerialization) · [ChargingChannel](/api/Global.ChargingChannel) · [ChargingChannelData](/api/Global.ChargingChannelData) · [ControlManager](/api/Global.ControlManager) · [DewPlayer](/api/Global.DewPlayer) · [SampleCastInfoContext](/api/Global.SampleCastInfoContext) · `St_Q_Laceration` · [TriggerConfig](/api/Global.TriggerConfig)

### Dependencies (6)

*Types and components that `CastMethodData` references or depends upon:*

[AbilityTrigger](/api/Global.AbilityTrigger) · [ICastMethodDataArrow](/api/Global.ICastMethodDataArrow) · [ICastMethodDataCone](/api/Global.ICastMethodDataCone) · [ICastMethodDataNone](/api/Global.ICastMethodDataNone) · [ICastMethodDataPoint](/api/Global.ICastMethodDataPoint) · [ICastMethodDataTarget](/api/Global.ICastMethodDataTarget)

### Related Enums (1)

*Enumerations referenced in fields, properties, or method signatures:*

[`CastMethodType`](/enums#castmethodtype)

:::
