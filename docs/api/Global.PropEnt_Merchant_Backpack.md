# Class: PropEnt_Merchant_Backpack

- **Category:** <span class="cat-dot" style="--cat-color: #22c55e" data-cat="Actors & Entities"></span> Actors & Entities
- **Namespace:** `Global`
- **Assembly:** `Dew.Core.dll`
- **Inheritance / Derived:** [DewNetworkBehaviour](/api/Global.DewNetworkBehaviour) → [Actor](/api/Global.Actor) → [Entity](/api/Global.Entity) → [PropEntity](/api/Global.PropEntity)

```csharp
public class PropEnt_Merchant_Backpack : PropEntity, ILogicUpdate, ICleanup, ICustomDestroyRoutine, IProp
```

## Fields (3)

::: details Click to expand Fields (3)

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`deathEffect`** | `public GameObject deathEffect` |  |
| **`spawnDelay`** | `public float spawnDelay` |  |
| **`spawnSkillRatio`** | `public float spawnSkillRatio` |  |

:::

## Methods (1)

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

### Used By (0)

*No incoming dependencies recorded.*

### Dependencies (3)

*Types and components that `PropEnt_Merchant_Backpack` references or depends upon:*

[Entity](/api/Global.Entity) · [EventInfoKill](/api/Global.EventInfoKill) · [PropEntity](/api/Global.PropEntity)

:::
