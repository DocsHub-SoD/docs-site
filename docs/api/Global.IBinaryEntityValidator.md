# Interface: IBinaryEntityValidator

- **Category:** <span class="cat-dot" style="--cat-color: #22c55e" data-cat="Actors & Entities"></span> Actors & Entities
- **Namespace:** `Global`
- **Assembly:** `Dew.Core.dll`

```csharp
public interface IBinaryEntityValidator
```

## Methods (1)

::: details `Evaluate(Entity, Entity)`

```csharp
bool Evaluate(Entity self, Entity target)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `self` | [`Entity`](/api/Global.Entity) |  |
| `target` | [`Entity`](/api/Global.Entity) |  |

**Returns:** `bool`

:::


## Architecture & Relationships

::: details Click to expand Architecture & Relationships

### Used By (6)

*Classes and systems that invoke, reference, or depend on `IBinaryEntityValidator`:*

[AbilityTargetValidator](/api/Global.AbilityTargetValidator) · [Channel](/api/Global.Channel) · [ControlManager](/api/Global.ControlManager) · [DewCollider](/api/Global.DewCollider) · [DewPhysics](/api/Global.DewPhysics) · [TriggerChannelData](/api/Global.TriggerChannelData)

### Dependencies (1)

*Types and components that `IBinaryEntityValidator` references or depends upon:*

[Entity](/api/Global.Entity)

:::
