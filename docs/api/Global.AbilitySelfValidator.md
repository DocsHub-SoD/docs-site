# Class: AbilitySelfValidator

- **Category:** <span class="cat-dot" style="--cat-color: #ef4444" data-cat="Combat & Abilities"></span> Combat & Abilities
- **Namespace:** `Global`
- **Assembly:** `Dew.Core.dll`

```csharp
[Serializable]
public class AbilitySelfValidator : IEntityValidator
```

## Fields (5)

::: details Click to expand Fields (5)

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`allowWhileDashing`** | `[ToggleLeft] public bool allowWhileDashing` |  |
| **`allowWhileDisabled`** | `[ToggleLeft] public bool allowWhileDisabled` |  |
| **`allowWhileDodging`** | `[ToggleLeft] public bool allowWhileDodging` |  |
| **`Default`** | `public static AbilitySelfValidator Default` |  |
| **`isMovementAbility`** | `[ToggleLeft] public bool isMovementAbility` |  |

:::

## Methods (1)

::: details `Evaluate(Entity)`

```csharp
public bool Evaluate(Entity self)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `self` | [`Entity`](/api/Global.Entity) |  |

**Returns:** `bool`

:::
