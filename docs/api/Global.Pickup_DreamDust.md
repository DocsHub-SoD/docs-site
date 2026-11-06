# Class: Pickup_DreamDust

- **Category:** <span class="cat-dot" style="--cat-color: #ef4444" data-cat="Combat & Abilities"></span> Combat & Abilities
- **Namespace:** `Global`
- **Assembly:** `Dew.Core.dll`
- **Inheritance / Derived:** [DewNetworkBehaviour](/api/Global.DewNetworkBehaviour) → [Actor](/api/Global.Actor) → [AbilityInstance](/api/Global.AbilityInstance) → [PickupInstance](/api/Global.PickupInstance)

```csharp
public class Pickup_DreamDust : PickupInstance, ILogicUpdate, ICleanup, ICustomDestroyRoutine
```

## Fields (4)

::: details Click to expand Fields (4)

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`amount`** | `[NonSerialized] public int amount` |  |
| **`isGivenByOtherPlayer`** | `[NonSerialized] public bool isGivenByOtherPlayer` |  |
| **`onGiveDreamDust`** | `public SafeAction<DewPlayer, int> onGiveDreamDust` | Called on server. |
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
