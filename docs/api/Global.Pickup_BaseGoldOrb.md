# Class: Pickup_BaseGoldOrb

- **Category:** <span class="cat-dot" style="--cat-color: #ef4444" data-cat="Combat & Abilities"></span> Combat & Abilities
- **Namespace:** `Global`
- **Assembly:** `Dew.Core.dll`
- **Inheritance / Derived:** [DewNetworkBehaviour](/api/Global.DewNetworkBehaviour) → [Actor](/api/Global.Actor) → [AbilityInstance](/api/Global.AbilityInstance) → [PickupInstance](/api/Global.PickupInstance) → [Pickup_LargeGoldOrb](/api/Global.Pickup_LargeGoldOrb) → [Pickup_MediumGoldOrb](/api/Global.Pickup_MediumGoldOrb) → [Pickup_SmallGoldOrb](/api/Global.Pickup_SmallGoldOrb)

```csharp
public class Pickup_BaseGoldOrb : PickupInstance, ILogicUpdate, ICleanup, ICustomDestroyRoutine
```

## Fields (4)

::: details Click to expand Fields (4)

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`amount`** | `[NonSerialized] public int amount` |  |
| **`isGivenByOtherPlayer`** | `[NonSerialized] public bool isGivenByOtherPlayer` |  |
| **`isKillGold`** | `[NonSerialized] public bool isKillGold` |  |
| **`target`** | `[NonSerialized] public Hero target` |  |

:::

## Properties (1)

::: details Click to expand Properties (1)

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`isDestroyedOnRoomChange`** | `public override bool isDestroyedOnRoomChange { get; }` |  |

:::

## Methods (4)

::: details `CanBeUsedBy(Hero)`

```csharp
protected override bool CanBeUsedBy(Hero hero)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `hero` | [`Hero`](/api/Global.Hero) |  |

**Returns:** `bool`

:::

::: details `OnCreate()`

```csharp
protected override void OnCreate()
```

:::

::: details `OnDestroyActor()`

```csharp
protected override void OnDestroyActor()
```

:::

::: details `OnPickup(Hero)`

```csharp
protected override void OnPickup(Hero hero)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `hero` | [`Hero`](/api/Global.Hero) |  |

:::
