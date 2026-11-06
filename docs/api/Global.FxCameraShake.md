# Class: FxCameraShake

- **Category:** <span class="cat-dot" style="--cat-color: #3b82f6" data-cat="Managers & Systems"></span> Managers & Systems
- **Namespace:** `Global`
- **Assembly:** `Dew.Core.dll`

```csharp
public class FxCameraShake : MonoBehaviour, IEffectComponent, IEffectWithOwnerContext
```

## Fields (10)

::: details Click to expand Fields (10)

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`amplitude`** | `public float amplitude` |  |
| **`attackTime`** | `public float attackTime` |  |
| **`decayTime`** | `public float decayTime` |  |
| **`delay`** | `public float delay` |  |
| **`frequency`** | `public float frequency` |  |
| **`Global_AmplitudeMultiplier`** | `public const float Global_AmplitudeMultiplier = 1.25` |  |
| **`Global_FrequencyMultiplier`** | `public const float Global_FrequencyMultiplier = 0.9` |  |
| **`Global_TimeMultiplier`** | `public const float Global_TimeMultiplier = 1.25` |  |
| **`signalSource`** | `public SignalSourceAsset signalSource` |  |
| **`sustainTime`** | `public float sustainTime` |  |

:::

## Properties (1)

::: details Click to expand Properties (1)

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`isPlaying`** | `public bool isPlaying { get; }` |  |

:::

## Methods (3)

::: details `Play()`

```csharp
public void Play()
```

:::

::: details `SetOwnerContext(EffectOwnerContext)`

```csharp
public void SetOwnerContext(EffectOwnerContext context)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `context` | <a href="/enums#effectownercontext" class="enum-link" data-tooltip="None=0 · Self=1 · Boss=2 · OtherPlayers=3 · Others=4">EffectOwnerContext</a> |  |

:::

::: details `Stop()`

```csharp
public void Stop()
```

:::


## Architecture & Relationships

::: details Click to expand Architecture & Relationships

### Used By (7)

*Classes and systems that invoke, reference, or depend on `FxCameraShake`:*

`Ai_Gem_E_Fever_Explosion` · `Ai_Mon_DarkCave_BossSeeker_GreenChaserOrb_Explode` · `Ai_Q_GoldenBurst` · `Ai_Q_SuperNova` · `Ai_R_StaticDischarge` · [DewResources](/api/Global.DewResources) · [ShaderManager](/api/Global.ShaderManager)

### Dependencies (6)

*Types and components that `FxCameraShake` references or depends upon:*

[CameraManager](/api/Global.CameraManager) · [DewInput](/api/Global.DewInput) · [IEffectComponent](/api/Global.IEffectComponent) · [IEffectWithOwnerContext](/api/Global.IEffectWithOwnerContext) · [InputManager](/api/Global.InputManager) · [ManagerBase`1](/api/Global.ManagerBase`1)

### Related Enums (1)

*Enumerations referenced in fields, properties, or method signatures:*

<a href="/enums#effectownercontext" class="enum-link" data-tooltip="None=0 · Self=1 · Boss=2 · OtherPlayers=3 · Others=4">EffectOwnerContext</a>

:::
