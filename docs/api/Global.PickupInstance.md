# Class: PickupInstance

- **Category:** <span class="cat-dot" style="--cat-color: #ef4444" data-cat="Combat & Abilities"></span> Combat & Abilities
- **Namespace:** `Global`
- **Assembly:** `Dew.Core.dll`
- **Inheritance / Derived:** [DewNetworkBehaviour](/api/Global.DewNetworkBehaviour) → [Actor](/api/Global.Actor) → [AbilityInstance](/api/Global.AbilityInstance) → [Pickup_BaseExpOrb](/api/Global.Pickup_BaseExpOrb) → [Pickup_BaseGoldOrb](/api/Global.Pickup_BaseGoldOrb) → [Pickup_DreamDust](/api/Global.Pickup_DreamDust) → [Pickup_HealthOrb](/api/Global.Pickup_HealthOrb) → [Pickup_ManaOrb](/api/Global.Pickup_ManaOrb) → [Pickup_RegenOrb](/api/Global.Pickup_RegenOrb) → [RandomPickupInstance](/api/Global.RandomPickupInstance)

```csharp
public class PickupInstance : AbilityInstance, ILogicUpdate, ICleanup, ICustomDestroyRoutine
```

## Fields (17)

::: details Click to expand Fields (17)

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`attractionRange`** | `public float attractionRange` |  |
| **`enableTimeoutMagnet`** | `[Header] [Header("Timeout-Magnet")] public bool enableTimeoutMagnet` |  |
| **`expirationTime`** | `public float expirationTime` |  |
| **`fixDirectionMaxSpeedRad`** | `[Header] [Header("Velocity")] public float fixDirectionMaxSpeedRad` |  |
| **`mainEffect`** | `[Header] [Header("Effects")] public GameObject mainEffect` |  |
| **`maxInitialVelocity`** | `public float maxInitialVelocity` |  |
| **`maxVelocity`** | `public float maxVelocity` |  |
| **`pickupDelay`** | `[Header] [Header("Behavior")] public float pickupDelay` |  |
| **`pickupEffect`** | `public GameObject pickupEffect` |  |
| **`pickupEffectOnHero`** | `public GameObject pickupEffectOnHero` |  |
| **`pickupRange`** | `public float pickupRange` |  |
| **`timeoutMagnetTime`** | `public float timeoutMagnetTime` |  |
| **`variationStrength`** | `public float variationStrength` |  |
| **`velocityAccelerationMax`** | `public float velocityAccelerationMax` |  |
| **`velocityAccelerationMin`** | `public float velocityAccelerationMin` |  |
| **`velocityDeceleration`** | `public float velocityDeceleration` |  |
| **`yPosFromGround`** | `public float yPosFromGround` |  |

:::

## Methods (7)

::: details `ActiveFrameUpdate()`

```csharp
protected override void ActiveFrameUpdate()
```

:::

::: details `ActiveLogicUpdate(float)`

```csharp
protected override void ActiveLogicUpdate(float dt)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `dt` | `float` |  |

:::

::: details `CanBeUsedBy(Hero)`

Checked on server.

```csharp
protected virtual bool CanBeUsedBy(Hero hero)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `hero` | [`Hero`](/api/Global.Hero) |  |

**Returns:** `bool`

:::

::: details `OnCreate()`

```csharp
protected override void OnCreate()
```

:::

::: details `OnDestroyActor()`

```csharp
protected override void OnDestroyActor()
```

:::

::: details `OnPickup(Hero)`

Called on server when this pickup instance is picked up. After this function call the instance is immediately destroyed.

```csharp
protected virtual void OnPickup(Hero hero)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `hero` | [`Hero`](/api/Global.Hero) |  |

:::

::: details `OnPrepare()`

```csharp
protected override void OnPrepare()
```

:::


## Architecture & Relationships

::: details Click to expand Architecture & Relationships

### Used By (10)

*Classes and systems that invoke, reference, or depend on `PickupInstance`:*

`Ai_Culinary_Pickup` · `Ai_Gem_E_Predation_Pickup` · [Pickup_BaseExpOrb](/api/Global.Pickup_BaseExpOrb) · [Pickup_BaseGoldOrb](/api/Global.Pickup_BaseGoldOrb) · [Pickup_DreamDust](/api/Global.Pickup_DreamDust) · [Pickup_HealthOrb](/api/Global.Pickup_HealthOrb) · [Pickup_ManaOrb](/api/Global.Pickup_ManaOrb) · [Pickup_RegenOrb](/api/Global.Pickup_RegenOrb) · [RandomPickupInstance](/api/Global.RandomPickupInstance) · `StatusEffectRandomPickupInstance`

### Dependencies (8)

*Types and components that `PickupInstance` references or depends upon:*

[AbilityInstance](/api/Global.AbilityInstance) · [Actor](/api/Global.Actor) · [DewNetworkBehaviour](/api/Global.DewNetworkBehaviour) · [DewPhysics](/api/Global.DewPhysics) · [DewPlayer](/api/Global.DewPlayer) · [EntityCheck](/api/Global.EntityCheck) · [Hero](/api/Global.Hero) · `VectorPlaneTransformExtension`

:::
