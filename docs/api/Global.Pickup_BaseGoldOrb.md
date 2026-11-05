# Class: Pickup_BaseGoldOrb

- **Namespace:** `Global`
- **Assembly:** `Dew.Core.dll`
- **Inheritance / Derived:** [DewNetworkBehaviour](/api/Global.DewNetworkBehaviour) → [Actor](/api/Global.Actor) → [AbilityInstance](/api/Global.AbilityInstance) → [PickupInstance](/api/Global.PickupInstance) → [Pickup_LargeGoldOrb](/api/Global.Pickup_LargeGoldOrb) → [Pickup_MediumGoldOrb](/api/Global.Pickup_MediumGoldOrb) → [Pickup_SmallGoldOrb](/api/Global.Pickup_SmallGoldOrb)

```csharp
public class Pickup_BaseGoldOrb : PickupInstance, ILogicUpdate, ICleanup, ICustomDestroyRoutine
```

## Fields

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`amount`** | `[NonSerialized]
public int amount` |  |
| **`isGivenByOtherPlayer`** | `[NonSerialized]
public bool isGivenByOtherPlayer` |  |
| **`isKillGold`** | `[NonSerialized]
public bool isKillGold` |  |
| **`target`** | `[NonSerialized]
public Hero target` |  |

## Properties

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`isDestroyedOnRoomChange`** | `public override bool isDestroyedOnRoomChange { get; }` |  |

## Methods

### `CanBeUsedBy(Hero)`

```csharp
protected override bool CanBeUsedBy(Hero hero)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `hero` | [Hero](/api/Global.Hero) |  |

**Returns:** `bool`

### `OnCreate()`

```csharp
protected override void OnCreate()
```

### `OnDestroyActor()`

```csharp
protected override void OnDestroyActor()
```

### `OnPickup(Hero)`

```csharp
protected override void OnPickup(Hero hero)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `hero` | [Hero](/api/Global.Hero) |  |
