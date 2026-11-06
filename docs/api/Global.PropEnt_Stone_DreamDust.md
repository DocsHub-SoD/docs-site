# Class: PropEnt_Stone_DreamDust

- **Category:** <span class="cat-dot" style="--cat-color: #22c55e" data-cat="Actors & Entities"></span> Actors & Entities
- **Namespace:** `Global`
- **Assembly:** `Dew.Core.dll`
- **Inheritance / Derived:** [DewNetworkBehaviour](/api/Global.DewNetworkBehaviour) → [Actor](/api/Global.Actor) → [Entity](/api/Global.Entity) → [PropEntity](/api/Global.PropEntity)

```csharp
public class PropEnt_Stone_DreamDust : PropEntity, ILogicUpdate, ICleanup, ICustomDestroyRoutine, IProp
```

## Fields (2)

::: details Click to expand Fields (2)

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`amountByZoneIndex`** | `public Formula amountByZoneIndex` |  |
| **`rotSpeed`** | `public float rotSpeed` |  |

:::

## Properties (1)

::: details Click to expand Properties (1)

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`isRegularReward`** | `public override bool isRegularReward { get; }` |  |

:::

## Methods (5)

::: details `ActiveLogicUpdate(float)`

```csharp
protected override void ActiveLogicUpdate(float dt)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `dt` | `float` |  |

:::

::: details `GetAmount()`

```csharp
public int GetAmount()
```

**Returns:** `int`

:::

::: details `OnCreate()`

```csharp
protected override void OnCreate()
```

:::

::: details `OnDeath(EventInfoKill)`

```csharp
protected override void OnDeath(EventInfoKill info)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `info` | [`EventInfoKill`](/api/Global.EventInfoKill) |  |

:::

::: details `OnDestroyActor()`

```csharp
protected override void OnDestroyActor()
```

:::


## Architecture & Relationships

::: details Click to expand Architecture & Relationships

### Used By (1)

*Classes and systems that invoke, reference, or depend on `PropEnt_Stone_DreamDust`:*

`Se_Star_Aurena_I_BonusFromStones`

### Dependencies (10)

*Types and components that `PropEnt_Stone_DreamDust` references or depends upon:*

[DewMath](/api/Global.DewMath) · [Entity](/api/Global.Entity) · [EntityTransformModifier](/api/Global.EntityTransformModifier) · [EntityVisual](/api/Global.EntityVisual) · [EventInfoKill](/api/Global.EventInfoKill) · [Formula](/api/Global.Formula) · [NetworkedManagerBase`1](/api/Global.NetworkedManagerBase`1) · [PickupManager](/api/Global.PickupManager) · [PropEntity](/api/Global.PropEntity) · [ZoneManager](/api/Global.ZoneManager)

:::
