# Class: AbilityTargetValidator

- **Category:** <span class="cat-dot" style="--cat-color: #ef4444" data-cat="Combat & Abilities"></span> Combat & Abilities
- **Namespace:** `Global`
- **Assembly:** `Dew.Core.dll`

```csharp
[Serializable]
[InlineProperty]
public class AbilityTargetValidator : IBinaryEntityValidator
```

## Fields (1)

::: details Click to expand Fields (1)

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`targets`** | `[HideLabel] [EnumToggleButtons] public EntityRelation targets` |  |

:::

## Methods (1)

::: details `Evaluate(Entity, Entity)`

```csharp
public bool Evaluate(Entity self, Entity target)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `self` | [`Entity`](/api/Global.Entity) |  |
| `target` | [`Entity`](/api/Global.Entity) |  |

**Returns:** `bool`

:::
