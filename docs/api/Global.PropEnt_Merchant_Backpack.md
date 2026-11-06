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
