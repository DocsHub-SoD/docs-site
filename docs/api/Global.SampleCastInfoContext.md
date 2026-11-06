# Struct: SampleCastInfoContext

- **Category:** <span class="cat-dot" style="--cat-color: #ef4444" data-cat="Combat & Abilities"></span> Combat & Abilities
- **Namespace:** `Global`
- **Assembly:** `Dew.Core.dll`

```csharp
public struct SampleCastInfoContext
```

## Fields (12)

::: details Click to expand Fields (12)

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`angleSpeedLimit`** | `public float angleSpeedLimit` |  |
| **`cancelCallback`** | `[NonSerialized] public Action cancelCallback` |  |
| **`castCallback`** | `[NonSerialized] public Action<CastInfo> castCallback` |  |
| **`castKey`** | `[NonSerialized] public DewInputTrigger castKey` |  |
| **`castMethod`** | `public CastMethodData castMethod` |  |
| **`castOnButton`** | `public SampleCastInfoContext.CastOnButtonType castOnButton` |  |
| **`currentInfo`** | `public CastInfo currentInfo` |  |
| **`isInitialInfoSet`** | `public bool isInitialInfoSet` |  |
| **`showCastIndicator`** | `public bool showCastIndicator` |  |
| **`targetValidator`** | `public AbilityTargetValidator targetValidator` |  |
| **`trigger`** | `public AbilityTrigger trigger` |  |
| **`updateCallback`** | `[NonSerialized] public Action<CastInfo> updateCallback` |  |

:::


## Architecture & Relationships

::: details Click to expand Architecture & Relationships

### Used By (2)

*Classes and systems that invoke, reference, or depend on `SampleCastInfoContext`:*

[DewPlayer](/api/Global.DewPlayer) · `Mirror.GeneratedNetworkCode`

### Dependencies (5)

*Types and components that `SampleCastInfoContext` references or depends upon:*

[AbilityTargetValidator](/api/Global.AbilityTargetValidator) · [AbilityTrigger](/api/Global.AbilityTrigger) · [CastInfo](/api/Global.CastInfo) · [CastMethodData](/api/Global.CastMethodData) · [DewInputTrigger](/api/Global.DewInputTrigger)

:::
