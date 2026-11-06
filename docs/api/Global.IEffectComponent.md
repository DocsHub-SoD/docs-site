# Interface: IEffectComponent

- **Category:** <span class="cat-dot" style="--cat-color: #a855f7" data-cat="Buffs & Statuses"></span> Buffs & Statuses
- **Namespace:** `Global`
- **Assembly:** `Dew.Core.dll`

```csharp
public interface IEffectComponent
```

## Properties (1)

::: details Click to expand Properties (1)

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`isPlaying`** | `bool isPlaying { get; }` |  |

:::

## Methods (2)

::: details `Play()`

```csharp
void Play()
```

:::

::: details `Stop()`

```csharp
void Stop()
```

:::


## Architecture & Relationships

::: details Click to expand Architecture & Relationships

### Used By (23)

*Classes and systems that invoke, reference, or depend on `IEffectComponent`:*

[ArcTelegraphController](/api/Global.ArcTelegraphController) · [BoxTelegraphController](/api/Global.BoxTelegraphController) · [CommandMarker](/api/Global.CommandMarker) · [DewAudioSource](/api/Global.DewAudioSource) · [DewEffect](/api/Global.DewEffect) · [EffectAutoDestroy](/api/Global.EffectAutoDestroy) · [FxAnimatorSetFloat](/api/Global.FxAnimatorSetFloat) · [FxAnimatorSetTrigger](/api/Global.FxAnimatorSetTrigger) · [FxCameraShake](/api/Global.FxCameraShake) · [FxChangeMaterial](/api/Global.FxChangeMaterial) · [FxChangeMusic](/api/Global.FxChangeMusic) · [FxEntityAnimation](/api/Global.FxEntityAnimation) · [FxEntityDisableRenderer](/api/Global.FxEntityDisableRenderer) · `FxEntityInvoke` · [FxEntityModelTransform](/api/Global.FxEntityModelTransform) · [FxFeedbackEffect](/api/Global.FxFeedbackEffect) · [FxInterpolatedEffectBase](/api/Global.FxInterpolatedEffectBase) · [FxRandomTransform](/api/Global.FxRandomTransform) · [FxRepeatedEffect](/api/Global.FxRepeatedEffect) · [FxSimulateParticleSystem](/api/Global.FxSimulateParticleSystem) · [FxStopTime](/api/Global.FxStopTime) · `FxUnityEvent` · `Shrine_FallenStar_Visual`

### Dependencies (0)

*No outgoing class dependencies recorded.*

:::
