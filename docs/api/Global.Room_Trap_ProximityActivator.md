# Class: Room_Trap_ProximityActivator

- **Category:** <span class="cat-dot" style="--cat-color: #ef4444" data-cat="Combat & Abilities"></span> Combat & Abilities
- **Namespace:** `Global`
- **Assembly:** `Dew.Core.dll`
- **Inheritance / Derived:** [DewNetworkBehaviour](/api/Global.DewNetworkBehaviour) → [Room_Trap_ActivatorBase](/api/Global.Room_Trap_ActivatorBase)

```csharp
public class Room_Trap_ProximityActivator : Room_Trap_ActivatorBase, ILogicUpdate
```

## Fields (4)

::: details Click to expand Fields (4)

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`activationCooldown`** | `public float activationCooldown` |  |
| **`isActivatedByHeroes`** | `public bool isActivatedByHeroes` |  |
| **`isActivatedByMonster`** | `public bool isActivatedByMonster` |  |
| **`range`** | `public DewCollider range` |  |

:::

## Methods (2)

::: details `Awake()`

```csharp
protected override void Awake()
```

:::

::: details `LogicUpdate(float)`

```csharp
public override void LogicUpdate(float dt)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `dt` | `float` |  |

:::
