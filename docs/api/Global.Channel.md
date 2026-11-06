# Class: Channel

- **Category:** <span class="cat-dot" style="--cat-color: #ef4444" data-cat="Combat & Abilities"></span> Combat & Abilities
- **Namespace:** `Global`
- **Assembly:** `Dew.Core.dll`

```csharp
public class Channel
```

## Fields (7)

::: details Click to expand Fields (7)

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`blockedActions`** | `public Channel.BlockedAction blockedActions` | Blocked actions for the owner of this channel.This channel will fail if any of the cancelable blocks is disobeyed. |
| **`duration`** | `public float duration` | Total duration of this channel. |
| **`isAttack`** | `public bool isAttack` | Only a single attack channel can exist in an entity. |
| **`onCancel`** | `public Action onCancel` | Callback function to be called when this channel has been canceled.This can be because of either an invalidation flag from any of the validators, or cancelable block being canceled by an entity. |
| **`onComplete`** | `public Action onComplete` | Callback function to be called when this channel has been successfully completed. |
| **`onTick`** | `public Action<float> onTick` | Called every logic update tick while channel is alive. |
| **`uncancellableTime`** | `public float uncancellableTime` | If this channel is cancellable, it won't be cancellable during this period to prevent accidental cancel. |

:::

## Properties (2)

::: details Click to expand Properties (2)

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`elapsedTime`** | `public float elapsedTime { get; }` |  |
| **`isAlive`** | `public bool isAlive { get; }` |  |

:::

## Methods (8)

::: details `AddOnCancel(Action)`

```csharp
public Channel AddOnCancel(Action callback)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `callback` | `System.Action` |  |

**Returns:** `Channel`

:::

::: details `AddOnComplete(Action)`

```csharp
public Channel AddOnComplete(Action callback)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `callback` | `System.Action` |  |

**Returns:** `Channel`

:::

::: details `AddOnTick(Action&lt;float&gt;)`

```csharp
public Channel AddOnTick(Action<float> callback)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `callback` | `System.Action<T><float>` |  |

**Returns:** `Channel`

:::

::: details `AddValidation(IBinaryEntityValidator, Entity)`

Adds an binary entity validation for this channel. This channel will fail if any of the added validators evaluates to false.

```csharp
public Channel AddValidation(IBinaryEntityValidator validator, Entity entity)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `validator` | [`IBinaryEntityValidator`](/api/Global.IBinaryEntityValidator) |  |
| `entity` | [`Entity`](/api/Global.Entity) |  |

**Returns:** `Channel`

:::

::: details `AddValidation(IEntityValidator)`

Adds an entity validation for this channel. This channel will fail if any of the added validators evaluates to false.

```csharp
public Channel AddValidation(IEntityValidator validator)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `validator` | [`IEntityValidator`](/api/Global.IEntityValidator) |  |

**Returns:** `Channel`

:::

::: details `Cancel()`

Cancel this channel next channel update.

```csharp
public Channel Cancel()
```

**Returns:** `Channel`

:::

::: details `Complete()`

Complete this channel next channel update.

```csharp
public Channel Complete()
```

**Returns:** `Channel`

:::

::: details `Dispatch(Entity)`

Dispatch this channel.

```csharp
public Channel Dispatch(Entity e)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `e` | [`Entity`](/api/Global.Entity) |  |

**Returns:** `Channel`

:::


## Architecture & Relationships

::: details Click to expand Architecture & Relationships

### Used By (48)

*Classes and systems that invoke, reference, or depend on `Channel`:*

[AbilityTrigger](/api/Global.AbilityTrigger) · `Ai_C_BeamOfLight` · `Ai_E_SliceThroat` · `Ai_Mon_Despair_BossAzurak_DoubleStomp` · `Ai_Mon_Despair_BossAzurak_RoarAtk` · `Ai_Mon_Despair_BossAzurak_Roll` · `Ai_Mon_Despair_BossAzurak_StompBlock` · `Ai_Mon_Despair_BossAzurak_StompGlobal` · `Ai_Mon_Ink_BossDarkMoon_AltAtk_Spawner` · `Ai_Mon_Ink_BossDarkMoon_AltAtk_StingAtk` · `Ai_Mon_Ink_BossDarkMoon_Blade` · `Ai_Mon_Ink_BossDarkMoon_Eclipse` · `Ai_Mon_Ink_BossDarkMoon_TeleportDash` · `Ai_Mon_Ink_BossDarkMoon_ThrowSpear_Spawner` · `Ai_Mon_Ink_BossWhiteNight_AltAtk_Ready` · `Ai_Mon_Ink_BossWhiteNight_Cataclysm` · `Ai_Mon_Ink_BossWhiteNight_DestructionWave_Wave` · `Ai_Mon_LavaLand_BossInfernus_Roar` · `Ai_Mon_Primus_BossPrimusAeron_Rage_Atk` · `Ai_Mon_Sky_BigBaam_BeamAtk` · `Ai_Mon_Sky_BossNyx_AltTeleport` · `Ai_Mon_Sky_BossNyx_Atk` · `Ai_Mon_Sky_BossNyx_LineAtk_Displacement` · `Ai_Mon_Sky_BossNyx_PullAtk` · `Ai_Mon_SnowMountain_BossSkoll_Atk` · `Ai_Mon_Special_BossErebos_AntiGravity_Spawner` · `Ai_Mon_Special_BossMaw_Atk` · `Ai_Mon_Special_BossMaw_Chomp_Charge` · `Ai_Mon_Special_BossMaw_MoonlightPact` · `Ai_Mon_Special_BossMaw_SliceThroat` · `Ai_Mon_Special_BossObliviax_DashAtk` · `Ai_Mon_Special_BossObliviax_NeedleAtk_Ready` · `Ai_Mon_Special_BossPolaris_Holy_Atk_Spawner` · `Ai_Q_SuperNova` · `Ai_U_WorldCracker` · [AttackTrigger](/api/Global.AttackTrigger) · [ChannelData](/api/Global.ChannelData) · [ChargingChannel](/api/Global.ChargingChannel) · [DamageInstance](/api/Global.DamageInstance) · [EntityControl](/api/Global.EntityControl) · `Se_Mon_Despair_BossAzurak_Hide` · `Se_Mon_Ink_BossWhiteNight_Cataclysm` · `Se_Mon_Sky_BossNyx_StarBuff` · `Se_Mon_Special_BossErebos_PhaseChange` · `Se_R_Parry_Start` · `Se_WaypointTeleport` · `StarlessPath_BossPolarisManager` · [TriggerChannelData](/api/Global.TriggerChannelData)

### Dependencies (4)

*Types and components that `Channel` references or depends upon:*

[Entity](/api/Global.Entity) · [EntityControl](/api/Global.EntityControl) · [IBinaryEntityValidator](/api/Global.IBinaryEntityValidator) · [IEntityValidator](/api/Global.IEntityValidator)

:::
