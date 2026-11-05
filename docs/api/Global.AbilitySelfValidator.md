# Class: AbilitySelfValidator

- **Namespace:** `Global`
- **Assembly:** `Dew.Core.dll`

```csharp
[Serializable]
public class AbilitySelfValidator : IEntityValidator
```

## Fields

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`allowWhileDashing`** | `[ToggleLeft]
public bool allowWhileDashing` |  |
| **`allowWhileDisabled`** | `[ToggleLeft]
public bool allowWhileDisabled` |  |
| **`allowWhileDodging`** | `[ToggleLeft]
public bool allowWhileDodging` |  |
| **`Default`** | `public static AbilitySelfValidator Default` |  |
| **`isMovementAbility`** | `[ToggleLeft]
public bool isMovementAbility` |  |

## Methods

### `Evaluate(Entity)`

```csharp
public bool Evaluate(Entity self)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `self` | [Entity](/api/Global.Entity) |  |

**Returns:** `bool`
