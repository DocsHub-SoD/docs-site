# Class: Pickup_RegenOrb

- **Category:** <span class="cat-dot" style="--cat-color: #ef4444" data-cat="Combat & Abilities"></span> Combat & Abilities
- **Namespace:** `Global`
- **Assembly:** `Dew.Core.dll`
- **Inheritance / Derived:** [DewNetworkBehaviour](/api/Global.DewNetworkBehaviour) → [Actor](/api/Global.Actor) → [AbilityInstance](/api/Global.AbilityInstance) → [PickupInstance](/api/Global.PickupInstance)

```csharp
public class Pickup_RegenOrb : PickupInstance, ILogicUpdate, ICleanup, ICustomDestroyRoutine
```

## Fields

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`range`** | `public DewCollider range` |  |

## Methods

### `CanBeUsedBy(Hero)`

```csharp
protected override bool CanBeUsedBy(Hero hero)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `hero` | [`Hero`](/api/Global.Hero) |  |

**Returns:** `bool`

### `OnPickup(Hero)`

```csharp
protected override void OnPickup(Hero hero)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `hero` | [`Hero`](/api/Global.Hero) |  |
