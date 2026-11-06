# Class: FxEffect

- **Category:** <span class="cat-dot" style="--cat-color: #a855f7" data-cat="Buffs & Statuses"></span> Buffs & Statuses
- **Namespace:** `Global`
- **Assembly:** `Dew.Core.dll`

```csharp
public class FxEffect : MonoBehaviour
```

## Fields (5)

::: details Click to expand Fields (5)

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`bindToEntity`** | `public EffectBindEntityType bindToEntity` |  |
| **`delayOnEnablePlayOneFrame`** | `[ShowIf("playOnEnable", true)] public bool delayOnEnablePlayOneFrame` |  |
| **`playNew`** | `public bool playNew` |  |
| **`playOnEnable`** | `public bool playOnEnable` |  |
| **`typeSubstring`** | `[ShowIf("@bindToEntity == EffectBindEntityType.FindType", true)] public string typeSubstring` |  |

:::

## Methods (2)

::: details `Play()`

```csharp
public void Play()
```

:::

::: details `Stop()`

```csharp
public void Stop()
```

:::


## Architecture & Relationships

::: details Click to expand Architecture & Relationships

### Used By (0)

*No incoming dependencies recorded.*

### Dependencies (3)

*Types and components that `FxEffect` references or depends upon:*

[DewEffect](/api/Global.DewEffect) · [DewPlayer](/api/Global.DewPlayer) · [NetworkedManagerBase`1](/api/Global.NetworkedManagerBase`1)

### Related Enums (1)

*Enumerations referenced in fields, properties, or method signatures:*

[`EffectBindEntityType`](/enums#effectbindentitytype)

:::
