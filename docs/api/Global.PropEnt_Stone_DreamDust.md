# Class: PropEnt_Stone_DreamDust

- **Category:** <span class="cat-dot" style="--cat-color: #22c55e" data-cat="Actors & Entities"></span> Actors & Entities
- **Namespace:** `Global`
- **Assembly:** `Dew.Core.dll`
- **Inheritance / Derived:** [DewNetworkBehaviour](/api/Global.DewNetworkBehaviour) → [Actor](/api/Global.Actor) → [Entity](/api/Global.Entity) → [PropEntity](/api/Global.PropEntity)

```csharp
public class PropEnt_Stone_DreamDust : PropEntity, ILogicUpdate, ICleanup, ICustomDestroyRoutine, IProp
```

## Fields

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`amountByZoneIndex`** | `public Formula amountByZoneIndex` |  |
| **`rotSpeed`** | `public float rotSpeed` |  |

## Properties

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`isRegularReward`** | `public override bool isRegularReward { get; }` |  |

## Methods

### `ActiveLogicUpdate(float)`

```csharp
protected override void ActiveLogicUpdate(float dt)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `dt` | `float` |  |

### `GetAmount()`

```csharp
public int GetAmount()
```

**Returns:** `int`

### `OnCreate()`

```csharp
protected override void OnCreate()
```

### `OnDeath(EventInfoKill)`

```csharp
protected override void OnDeath(EventInfoKill info)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `info` | [`EventInfoKill`](/api/Global.EventInfoKill) |  |

### `OnDestroyActor()`

```csharp
protected override void OnDestroyActor()
```
