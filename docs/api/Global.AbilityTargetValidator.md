# Class: AbilityTargetValidator

- **Category:** <span class="cat-dot" style="--cat-color: #ef4444" data-cat="Combat & Abilities"></span> Combat & Abilities
- **Namespace:** `Global`
- **Assembly:** `Dew.Core.dll`

```csharp
[Serializable]
[InlineProperty]
public class AbilityTargetValidator : IBinaryEntityValidator
```

## Fields

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`targets`** | `[HideLabel] [EnumToggleButtons] public EntityRelation targets` |  |

## Methods

### `Evaluate(Entity, Entity)`

```csharp
public bool Evaluate(Entity self, Entity target)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `self` | [`Entity`](/api/Global.Entity) |  |
| `target` | [`Entity`](/api/Global.Entity) |  |

**Returns:** `bool`
