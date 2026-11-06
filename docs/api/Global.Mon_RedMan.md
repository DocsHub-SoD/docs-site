# Class: Mon_RedMan

- **Category:** <span class="cat-dot" style="--cat-color: #22c55e" data-cat="Actors & Entities"></span> Actors & Entities
- **Namespace:** `Global`
- **Assembly:** `Dew.Core.dll`
- **Inheritance / Derived:** [DewNetworkBehaviour](/api/Global.DewNetworkBehaviour) → [Actor](/api/Global.Actor) → [Entity](/api/Global.Entity) → [Monster](/api/Global.Monster)

```csharp
public class Mon_RedMan : Monster, ILogicUpdate, ICleanup, ICustomDestroyRoutine
```

## Fields

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`deathEffects`** | `public GameObject deathEffects` |  |

## Methods

### `OnDeath(EventInfoKill)`

```csharp
protected override void OnDeath(EventInfoKill info)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `info` | [`EventInfoKill`](/api/Global.EventInfoKill) |  |
