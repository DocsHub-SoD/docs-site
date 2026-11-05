# Class: Pickup_DreamDust

- **Namespace:** `Global`
- **Assembly:** `Dew.Core.dll`
- **Inheritance / Derived:** [DewNetworkBehaviour](/api/Global.DewNetworkBehaviour) → [Actor](/api/Global.Actor) → [AbilityInstance](/api/Global.AbilityInstance) → [PickupInstance](/api/Global.PickupInstance)

```csharp
public class Pickup_DreamDust : PickupInstance, ILogicUpdate, ICleanup, ICustomDestroyRoutine
```

## Fields

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`amount`** | `[NonSerialized]
public int amount` |  |
| **`isGivenByOtherPlayer`** | `[NonSerialized]
public bool isGivenByOtherPlayer` |  |
| **`onGiveDreamDust`** | `public SafeAction&lt;DewPlayer, int&gt; onGiveDreamDust` | Called on server. |
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
