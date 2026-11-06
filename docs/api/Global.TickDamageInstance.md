# Class: TickDamageInstance

- **Category:** <span class="cat-dot" style="--cat-color: #ef4444" data-cat="Combat & Abilities"></span> Combat & Abilities
- **Namespace:** `Global`
- **Assembly:** `Dew.Core.dll`
- **Inheritance / Derived:** [DewNetworkBehaviour](/api/Global.DewNetworkBehaviour) → [Actor](/api/Global.Actor) → [AbilityInstance](/api/Global.AbilityInstance) → [DamageInstance](/api/Global.DamageInstance)

```csharp
public class TickDamageInstance : DamageInstance, ILogicUpdate, ICleanup, ICustomDestroyRoutine
```

## Fields (6)

::: details Click to expand Fields (6)

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`delay`** | `[Title("Tick Damage Instance", null, TitleAlignments.Left, true, true)] public float delay` |  |
| **`fxLoop`** | `[LabelText("Fx Loop (After Delay)")] public GameObject fxLoop` |  |
| **`fxPerTick`** | `public GameObject fxPerTick` |  |
| **`fxTelegraph`** | `public GameObject fxTelegraph` |  |
| **`tickInterval`** | `public float tickInterval` |  |
| **`ticks`** | `public int ticks` |  |

:::

## Properties (1)

::: details Click to expand Properties (1)

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`duration`** | `[ShowInInspector] public float duration { get; }` |  |

:::

## Methods (3)

::: details `ActiveLogicUpdate(float)`

```csharp
protected override void ActiveLogicUpdate(float dt)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `dt` | `float` |  |

:::

::: details `OnCreateSequenced()`

```csharp
protected override IEnumerator OnCreateSequenced()
```

**Returns:** `System.Collections.IEnumerator`

:::

::: details `OnDestroyActor()`

```csharp
protected override void OnDestroyActor()
```

:::


## Architecture & Relationships

::: details Click to expand Architecture & Relationships

### Used By (19)

*Classes and systems that invoke, reference, or depend on `TickDamageInstance`:*

`Ai_Mon_DarkCave_BossSeeker_TunnelVision_Swarm` · `Ai_Mon_Ink_BossDarkMoon_ThrowSpear_AoE` · `Ai_Mon_Ink_BossWhiteNight_EnergyWave_Instance` · `Ai_Mon_Primus_BossPrimusAeron_Adapt_Doom_PyranasFireball` · `Ai_Mon_Special_BossMaw_ChainReaction_Instance` · `Ai_Mon_Special_BossPolaris_Holy_Beam` · `Ai_Mon_Special_BossPolaris_Holy_Purgatory_BurningFloor` · `Ai_Mon_Special_BossPolaris_Monster_Smite_TickInstance` · `Ai_QR_InfernalTales` · `Ai_Q_EmbracingTheChill_AreaDoT` · `Ai_R_Cataclysm_Meteor_Burn` · `Ai_R_ChainReaction` · `Ai_R_DancingBlades` · `Ai_R_Immolation_Damage` · `Ai_R_Lava_LavaField` · `Ai_R_Tranquility_Damage` · `Ai_RoomMod_FireDevil_Tornado` · `Ai_Star_Cetus_F_BI_SelfDamageAoeCold_AOE` · `St_QR_InfernalTales`

### Dependencies (3)

*Types and components that `TickDamageInstance` references or depends upon:*

[Actor](/api/Global.Actor) · [DamageInstance](/api/Global.DamageInstance) · [DewNetworkBehaviour](/api/Global.DewNetworkBehaviour)

:::
