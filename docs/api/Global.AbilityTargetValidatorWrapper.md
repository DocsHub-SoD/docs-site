# Class: AbilityTargetValidatorWrapper

- **Category:** <span class="cat-dot" style="--cat-color: #ef4444" data-cat="Combat & Abilities"></span> Combat & Abilities
- **Namespace:** `Global`
- **Assembly:** `Dew.Core.dll`

```csharp
public class AbilityTargetValidatorWrapper : IEntityValidator
```

## Fields (1)

::: details Click to expand Fields (1)

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`self`** | `public Entity self` |  |

:::

## Methods (1)

::: details `Evaluate(Entity)`

```csharp
public bool Evaluate(Entity entity)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `entity` | [`Entity`](/api/Global.Entity) |  |

**Returns:** `bool`

:::


## Architecture & Relationships

::: details Click to expand Architecture & Relationships

### Used By (4)

*Classes and systems that invoke, reference, or depend on `AbilityTargetValidatorWrapper`:*

[AbilityInstance](/api/Global.AbilityInstance) · [AbilityTrigger](/api/Global.AbilityTrigger) · [Gem](/api/Global.Gem) · [Summon](/api/Global.Summon)

### Dependencies (3)

*Types and components that `AbilityTargetValidatorWrapper` references or depends upon:*

[AbilityTargetValidator](/api/Global.AbilityTargetValidator) · [Entity](/api/Global.Entity) · [IEntityValidator](/api/Global.IEntityValidator)

### Related Enums (1)

*Enumerations referenced in fields, properties, or method signatures:*

<a href="/enums#entityrelation" class="enum-link" data-tooltip="Self=1 · Neutral=2 · Enemy=4 · Ally=8">EntityRelation</a>

:::
