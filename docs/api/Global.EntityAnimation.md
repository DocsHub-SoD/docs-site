# Class: EntityAnimation

- **Category:** <span class="cat-dot" style="--cat-color: #22c55e" data-cat="Actors & Entities"></span> Actors & Entities
- **Namespace:** `Global`
- **Assembly:** `Dew.Core.dll`
- **Inheritance / Derived:** [DewNetworkBehaviour](/api/Global.DewNetworkBehaviour) → [EntityComponent](/api/Global.EntityComponent)

```csharp
[HideMonoScript]
public class EntityAnimation : EntityComponent, ILogicUpdate
```

## Fields (2)

::: details Click to expand Fields (2)

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`abilityAnimStatus`** | `public EntityAnimation.AbilityAnimationStatus abilityAnimStatus` |  |
| **`animator`** | `[NonSerialized] public Animator animator` |  |

:::

## Properties (1)

::: details Click to expand Properties (1)

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`model`** | `public EntityModel model { get; }` |  |

:::

## Methods (11)

::: details `FrameUpdate()`

```csharp
public override void FrameUpdate()
```

:::

::: details `LogicUpdate(float)`

```csharp
public override void LogicUpdate(float dt)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `dt` | `float` |  |

:::

::: details `PlayAbilityAnimation(DewAnimationClip, float, float)`

```csharp
public void PlayAbilityAnimation(DewAnimationClip clip, float speed, float clipSelectValue)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `clip` | [`DewAnimationClip`](/api/Global.DewAnimationClip) |  |
| `speed` | `float` |  |
| `clipSelectValue` | `float` |  |

:::

::: details `PlayAbilityAnimation(DewAnimationClip, float)`

```csharp
public void PlayAbilityAnimation(DewAnimationClip clip, float speed = 1)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `clip` | [`DewAnimationClip`](/api/Global.DewAnimationClip) |  |
| `speed` | `float` |  |

:::

::: details `PlayStaggerAnimation()`

```csharp
public void PlayStaggerAnimation()
```

:::

::: details `ReplaceAnimation(ReplaceableAnimationType, AnimationClip)`

```csharp
public void ReplaceAnimation(EntityAnimation.ReplaceableAnimationType type, AnimationClip clip)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `type` | [`EntityAnimation.ReplaceableAnimationType`](/api/Global.EntityAnimation) |  |
| `clip` | `UnityEngine.AnimationClip` |  |

:::

::: details `ReplaceAnimationLocal(ReplaceableAnimationType, AnimationClipWithSpeed)`

```csharp
public void ReplaceAnimationLocal(EntityAnimation.ReplaceableAnimationType type, AnimationClipWithSpeed newData)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `type` | [`EntityAnimation.ReplaceableAnimationType`](/api/Global.EntityAnimation) |  |
| `newData` | [`AnimationClipWithSpeed`](/api/Global.AnimationClipWithSpeed) |  |

:::

::: details `ReplaceAnimationLocal(ReplaceableAnimationType, AnimationClip)`

```csharp
public void ReplaceAnimationLocal(EntityAnimation.ReplaceableAnimationType type, AnimationClip newClip)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `type` | [`EntityAnimation.ReplaceableAnimationType`](/api/Global.EntityAnimation) |  |
| `newClip` | `UnityEngine.AnimationClip` |  |

:::

::: details `SetupModel()`

```csharp
public void SetupModel()
```

:::

::: details `StopAbilityAnimation()`

```csharp
public void StopAbilityAnimation()
```

:::

::: details `StopAbilityAnimation(DewAnimationClip)`

Stop ability animation if currently playing animation is given clip.

```csharp
public void StopAbilityAnimation(DewAnimationClip clip)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `clip` | [`DewAnimationClip`](/api/Global.DewAnimationClip) |  |

:::


## Architecture & Relationships

::: details Click to expand Architecture & Relationships

### Used By (56)

*Classes and systems that invoke, reference, or depend on `EntityAnimation`:*

[AbilityTrigger](/api/Global.AbilityTrigger) · `Ai_C_BeamOfLight` · `Ai_C_Whirlwind` · `Ai_D_ParryMaster_Parry` · `Ai_E_FlameJet` · `Ai_EmbraceNewIdentity` · `Ai_GenericDodge` · `Ai_Mon_DarkCave_BossSeeker_TunnelVision_Claw` · `Ai_Mon_DarkCave_BossSeeker_TunnelVision_SecondPoolAtk` · `Ai_Mon_Forest_Hound_Charge` · `Ai_Mon_Ink_BossDarkMoon_Blade` · `Ai_Mon_Ink_BossDarkMoon_ShortDash` · `Ai_Mon_LavaLand_BossInfernus_BreathFire` · `Ai_Mon_Sky_BossNyx_StellarDash` · `Ai_Mon_SnowMountain_BossSkoll_Atk` · `Ai_Mon_SnowMountain_BossSkoll_Whirlwind` · `Ai_Mon_Special_BossMaw_SliceThroat` · `Ai_Mon_Special_BossMaw_SliceThroat_Atk` · `Ai_Mon_Special_BossObliviax_NeedleAtk_Ready` · `Ai_Q_Fleche_Dash` · `Ai_Q_Laceration_Circle` · `Ai_Q_Laceration_Dash` · `Ai_Q_Lunge` · `Ai_Q_MoonlightPact` · `Ai_Q_SuperNova` · `Ai_R_StaticDischarge` · `Ai_Star_Bismuth_F_IT_SmallerRingAddDisplacement_Dash` · `Ai_U_BigChomp` · `Ai_U_Hysteria_Claw` · `Ai_U_WorldCracker` · `At_Atk_HuskSword` · [ChargingChannel](/api/Global.ChargingChannel) · [Entity](/api/Global.Entity) · [EntityVisual](/api/Global.EntityVisual) · [FxEntityAnimation](/api/Global.FxEntityAnimation) · `Mon_DarkCave_NightOlm` · `Mon_Ink_BossDarkMoon` · `Mon_Ink_BossWhiteNight` · `Mon_Primus_BossPrimusAeron` · `PlayTutorial_Tutorial_Intro` · `Se_FatalHitProtection_Invulnerable` · `Se_M_Charge` · `Se_Mon_DarkCave_BossSeeker_Substitution` · `Se_Mon_Ink_BossWhiteNight_Rush` · `Se_Mon_Sky_BossNyx_StarBuff` · `Se_Mon_SnowMountain_SnowWolf_SlowApproach` · `Se_Mon_Special_BossMaw_ShadowOverdrive_Initial` · `Se_Q_Discipline_Jump` · `Se_R_FrozenFists` · `Se_R_Parry_Start` · `Se_R_RepulsiveShield` · `Se_R_Tranquility` · `Se_U_BeamOfBalance` · `Se_U_HerWorld_Blackhole` · `Se_WaypointTeleport` · `StarlessPath_BossPolarisManager`

### Dependencies (17)

*Types and components that `EntityAnimation` references or depends upon:*

[Actor](/api/Global.Actor) · [AnimationClipWithSpeed](/api/Global.AnimationClipWithSpeed) · [AssetRef`1](/api/Global.AssetRef`1) · [CounterBool](/api/Global.CounterBool) · [Dew](/api/Global.Dew) · [DewAnimationClip](/api/Global.DewAnimationClip) · [DewNetworkBehaviour](/api/Global.DewNetworkBehaviour) · [EasingFunction](/api/Global.EasingFunction) · [Entity](/api/Global.Entity) · [EntityComponent](/api/Global.EntityComponent) · [EntityControl](/api/Global.EntityControl) · [EntityModel](/api/Global.EntityModel) · [EntityStatus](/api/Global.EntityStatus) · [EntityVisual](/api/Global.EntityVisual) · [Hero](/api/Global.Hero) · `NetworkReaderWriterExtensions` · `Mirror.GeneratedNetworkCode`

:::
