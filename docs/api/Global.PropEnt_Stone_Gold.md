# Class: PropEnt_Stone_Gold

- **Category:** <span class="cat-dot" style="--cat-color: #22c55e" data-cat="Actors & Entities"></span> Actors & Entities
- **Namespace:** `Global`
- **Assembly:** `Dew.Core.dll`
- **Inheritance / Derived:** [DewNetworkBehaviour](/api/Global.DewNetworkBehaviour) → [Actor](/api/Global.Actor) → [Entity](/api/Global.Entity) → [PropEntity](/api/Global.PropEntity)

```csharp
public class PropEnt_Stone_Gold : PropEntity, ILogicUpdate, ICleanup, ICustomDestroyRoutine, IProp
```

## Fields (1)

::: details Click to expand Fields (1)

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`amountByZoneIndex`** | `public Formula amountByZoneIndex` |  |

:::

## Properties (1)

::: details Click to expand Properties (1)

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`isRegularReward`** | `public override bool isRegularReward { get; }` |  |

:::

## Methods (2)

::: details `GetAmount()`

```csharp
public int GetAmount()
```

**Returns:** `int`

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


## Architecture & Relationships

::: details Click to expand Architecture & Relationships

### Used By (1)

*Classes and systems that invoke, reference, or depend on `PropEnt_Stone_Gold`:*

`Se_Star_Aurena_I_BonusFromStones`

### Dependencies (8)

*Types and components that `PropEnt_Stone_Gold` references or depends upon:*

[DewMath](/api/Global.DewMath) · [Entity](/api/Global.Entity) · [EventInfoKill](/api/Global.EventInfoKill) · [Formula](/api/Global.Formula) · [NetworkedManagerBase`1](/api/Global.NetworkedManagerBase`1) · [PickupManager](/api/Global.PickupManager) · [PropEntity](/api/Global.PropEntity) · [ZoneManager](/api/Global.ZoneManager)

:::
