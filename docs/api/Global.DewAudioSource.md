# Class: DewAudioSource

- **Category:** <span class="cat-dot" style="--cat-color: #3b82f6" data-cat="Managers & Systems"></span> Managers & Systems
- **Namespace:** `Global`
- **Assembly:** `Dew.Core.dll`

```csharp
public class DewAudioSource : MonoBehaviour, IEffectComponent, IEffectWithOwnerContext
```

## Fields (16)

::: details Click to expand Fields (16)

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`clip`** | `[ShowIf("@rawClip == null \|\| clip != null", true)] public DewAudioClip clip` |  |
| **`delay`** | `public float delay` |  |
| **`fadeInTime`** | `public float fadeInTime` |  |
| **`fadeOutTime`** | `public float fadeOutTime` |  |
| **`forceHighestPriority`** | `[ToggleLeft] public bool forceHighestPriority` |  |
| **`ignoreTimescale`** | `[ToggleLeft] public bool ignoreTimescale` |  |
| **`isLoop`** | `[ToggleLeft] public bool isLoop` |  |
| **`PitchChangeByTimescaleMultiplier`** | `public const float PitchChangeByTimescaleMultiplier = 0.75` |  |
| **`pitchMultiplier`** | `public float pitchMultiplier` |  |
| **`playOnEnable`** | `[Space] [Space(20)] [ToggleLeft] public bool playOnEnable` |  |
| **`rawClip`** | `[ShowIf("@clip == null", true)] public AudioClip rawClip` |  |
| **`rolloff`** | `[ShowIf("@space != AudioSpaceType.Global", true)] public DewAudioRollOffType rolloff` |  |
| **`space`** | `public AudioSpaceType space` |  |
| **`stopWhenEffectStop`** | `[HideIf("isLoop", true)] [ToggleLeft] public bool stopWhenEffectStop` |  |
| **`type`** | `public AudioType type` |  |
| **`volumeMultiplier`** | `[Space] [Space(20)] public float volumeMultiplier` |  |

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
| `context` | [`EffectOwnerContext`](/api/Global.EffectOwnerContext) |  |

:::

::: details `Stop()`

```csharp
public void Stop()
```

:::


## Architecture & Relationships

::: details Click to expand Architecture & Relationships

### Used By (11)

*Classes and systems that invoke, reference, or depend on `DewAudioSource`:*

`Ai_Mon_DarkCave_BossSeeker_GreenChaserOrb_Explode` · `Ai_Mon_Sky_LittleBaam_Atk` · `Ai_Q_GoldenBurst` · `Ai_R_PrecisionShot_Projectile` · `DewAudioManager` · [EditSkillManager](/api/Global.EditSkillManager) · [EntitySound](/api/Global.EntitySound) · `UI_Common_ChatBox` · `UI_InGame_Conversations_Instance` · `UI_InGame_CurrentArtifact` · `UI_PlayRewardAnnouncer`

### Dependencies (5)

*Types and components that `DewAudioSource` references or depends upon:*

[DewAudioClip](/api/Global.DewAudioClip) · `DewAudioManager` · [IEffectComponent](/api/Global.IEffectComponent) · [IEffectWithOwnerContext](/api/Global.IEffectWithOwnerContext) · [ManagerBase`1](/api/Global.ManagerBase`1)

### Related Enums (4)

*Enumerations referenced in fields, properties, or method signatures:*

[`AudioSpaceType`](/enums#audiospacetype) · [`AudioType`](/enums#audiotype) · [`DewAudioRollOffType`](/enums#dewaudiorollofftype) · [`EffectOwnerContext`](/enums#effectownercontext)

:::
