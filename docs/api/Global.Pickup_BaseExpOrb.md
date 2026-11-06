# Class: Pickup_BaseExpOrb

- **Category:** <span class="cat-dot" style="--cat-color: #ef4444" data-cat="Combat & Abilities"></span> Combat & Abilities
- **Namespace:** `Global`
- **Assembly:** `Dew.Core.dll`
- **Inheritance / Derived:** [DewNetworkBehaviour](/api/Global.DewNetworkBehaviour) → [Actor](/api/Global.Actor) → [AbilityInstance](/api/Global.AbilityInstance) → [PickupInstance](/api/Global.PickupInstance) → [Pickup_LargeExpOrb](/api/Global.Pickup_LargeExpOrb) → [Pickup_MediumExpOrb](/api/Global.Pickup_MediumExpOrb) → [Pickup_SmallExpOrb](/api/Global.Pickup_SmallExpOrb)

```csharp
public class Pickup_BaseExpOrb : PickupInstance, ILogicUpdate, ICleanup, ICustomDestroyRoutine
```

## Fields

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`amount`** | `[NonSerialized] public float amount` |  |

## Methods

### `OnPickup(Hero)`

```csharp
protected override void OnPickup(Hero hero)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `hero` | [`Hero`](/api/Global.Hero) |  |
