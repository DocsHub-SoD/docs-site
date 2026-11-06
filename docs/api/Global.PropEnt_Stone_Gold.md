# Class: PropEnt_Stone_Gold

- **Category:** <span class="cat-dot" style="--cat-color: #22c55e" data-cat="Actors & Entities"></span> Actors & Entities
- **Namespace:** `Global`
- **Assembly:** `Dew.Core.dll`
- **Inheritance / Derived:** [DewNetworkBehaviour](/api/Global.DewNetworkBehaviour) → [Actor](/api/Global.Actor) → [Entity](/api/Global.Entity) → [PropEntity](/api/Global.PropEntity)

```csharp
public class PropEnt_Stone_Gold : PropEntity, ILogicUpdate, ICleanup, ICustomDestroyRoutine, IProp
```

## Fields

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`amountByZoneIndex`** | `public Formula amountByZoneIndex` |  |

## Properties

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`isRegularReward`** | `public override bool isRegularReward { get; }` |  |

## Methods

### `GetAmount()`

```csharp
public int GetAmount()
```

**Returns:** `int`

### `OnDeath(EventInfoKill)`

```csharp
protected override void OnDeath(EventInfoKill info)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `info` | [`EventInfoKill`](/api/Global.EventInfoKill) |  |
