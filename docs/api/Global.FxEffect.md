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
