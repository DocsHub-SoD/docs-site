# Class: ChargingChannel

- **Category:** <span class="cat-dot" style="--cat-color: #ef4444" data-cat="Combat & Abilities"></span> Combat & Abilities
- **Namespace:** `Global`
- **Assembly:** `Dew.Core.dll`

```csharp
public class ChargingChannel
```

## Fields (1)

::: details Click to expand Fields (1)

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`castMethod`** | `public CastMethodData castMethod` | You must call UpdateCastMethod after making change to this. |

:::

## Properties (5)

::: details Click to expand Properties (5)

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`castInfo`** | `public CastInfo castInfo { get; }` | Current cast info of this charging channel. |
| **`chargeAmount`** | `public float chargeAmount { get; }` |  |
| **`elapsedTime`** | `public float elapsedTime { get; }` |  |
| **`isActive`** | `public bool isActive { get; }` |  |
| **`normalizedTime`** | `public float normalizedTime { get; }` |  |

:::

## Methods (8)

::: details `Cancel()`

```csharp
public void Cancel()
```

:::

::: details `Dispatch(Entity, AbilityTrigger)`

```csharp
public ChargingChannel Dispatch(Entity entity, AbilityTrigger trigger)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `entity` | [`Entity`](/api/Global.Entity) |  |
| `trigger` | [`AbilityTrigger`](/api/Global.AbilityTrigger) |  |

**Returns:** `ChargingChannel`

:::

::: details `OnCancel(Action&lt;ChargingChannel&gt;)`

```csharp
public ChargingChannel OnCancel(Action<ChargingChannel> callback)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `callback` | [`System.Action<T><ChargingChannel>`](/api/Global.ChargingChannel) |  |

**Returns:** `ChargingChannel`

:::

::: details `OnCast(Action&lt;ChargingChannel&gt;)`

```csharp
public ChargingChannel OnCast(Action<ChargingChannel> callback)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `callback` | [`System.Action<T><ChargingChannel>`](/api/Global.ChargingChannel) |  |

**Returns:** `ChargingChannel`

:::

::: details `OnChargeFull(Action&lt;ChargingChannel&gt;)`

```csharp
public ChargingChannel OnChargeFull(Action<ChargingChannel> callback)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `callback` | [`System.Action<T><ChargingChannel>`](/api/Global.ChargingChannel) |  |

**Returns:** `ChargingChannel`

:::

::: details `OnComplete(Action&lt;ChargingChannel&gt;)`

```csharp
public ChargingChannel OnComplete(Action<ChargingChannel> callback)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `callback` | [`System.Action<T><ChargingChannel>`](/api/Global.ChargingChannel) |  |

**Returns:** `ChargingChannel`

:::

::: details `SetInitialInfo(CastInfo)`

```csharp
public ChargingChannel SetInitialInfo(CastInfo info)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `info` | [`CastInfo`](/api/Global.CastInfo) |  |

**Returns:** `ChargingChannel`

:::

::: details `UpdateCastMethod()`

Send updated cast method to client to reflect the changes.

```csharp
public ChargingChannel UpdateCastMethod()
```

**Returns:** `ChargingChannel`

:::


## Architecture & Relationships

::: details Click to expand Architecture & Relationships

### Used By (15)

*Classes and systems that invoke, reference, or depend on `ChargingChannel`:*

[AbilityInstance](/api/Global.AbilityInstance) · `Ai_C_Pew` · `Ai_E_ShadowVolley` · `Ai_E_StygianRush` · `Ai_QR_DistortedMind_Spawner` · `Ai_Q_BigBorealChunk_Spawner` · `Ai_Q_CruelSun` · `Ai_Q_Laceration_Circle` · `Ai_R_BackOff_Spawner` · `Ai_R_PrecisionShot` · `Ai_R_StaticDischarge` · `Ai_Star_Aurena_F_CR_ChargedCast_InstanceCharger` · [ChargingChannelData](/api/Global.ChargingChannelData) · `Se_R_BoneCrusher` · `Se_U_BeamOfBalance`

### Dependencies (16)

*Types and components that `ChargingChannel` references or depends upon:*

[AbilityTrigger](/api/Global.AbilityTrigger) · [Actor](/api/Global.Actor) · [ActorCheck](/api/Global.ActorCheck) · `ActorRef`1` · [BasicEffectWithStrength](/api/Global.BasicEffectWithStrength) · [CastInfo](/api/Global.CastInfo) · [CastMethodData](/api/Global.CastMethodData) · [Channel](/api/Global.Channel) · [ChargingChannelData](/api/Global.ChargingChannelData) · [DewEffect](/api/Global.DewEffect) · [DewLocalization](/api/Global.DewLocalization) · [DewPlayer](/api/Global.DewPlayer) · [Entity](/api/Global.Entity) · [EntityAnimation](/api/Global.EntityAnimation) · [EntityControl](/api/Global.EntityControl) · [NetworkedOnScreenTimerHandle](/api/Global.NetworkedOnScreenTimerHandle)

:::
