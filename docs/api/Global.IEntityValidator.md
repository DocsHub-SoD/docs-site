# Interface: IEntityValidator

- **Category:** <span class="cat-dot" style="--cat-color: #22c55e" data-cat="Actors & Entities"></span> Actors & Entities
- **Namespace:** `Global`
- **Assembly:** `Dew.Core.dll`

```csharp
public interface IEntityValidator
```

## Fields (1)

::: details Click to expand Fields (1)

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`AlwaysTrue`** | `public static IEntityValidator AlwaysTrue` |  |

:::

## Methods (1)

::: details `Evaluate(Entity)`

```csharp
bool Evaluate(Entity entity)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `entity` | [`Entity`](/api/Global.Entity) |  |

**Returns:** `bool`

:::


## Architecture & Relationships

::: details Click to expand Architecture & Relationships

### Used By (7)

*Classes and systems that invoke, reference, or depend on `IEntityValidator`:*

[AbilitySelfValidator](/api/Global.AbilitySelfValidator) · [AbilityTargetValidatorWrapper](/api/Global.AbilityTargetValidatorWrapper) · [Channel](/api/Global.Channel) · [ControlManager](/api/Global.ControlManager) · [DewCollider](/api/Global.DewCollider) · [DewPhysics](/api/Global.DewPhysics) · [TriggerChannelData](/api/Global.TriggerChannelData)

### Dependencies (1)

*Types and components that `IEntityValidator` references or depends upon:*

[Entity](/api/Global.Entity)

:::
