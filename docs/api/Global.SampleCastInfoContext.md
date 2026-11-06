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
