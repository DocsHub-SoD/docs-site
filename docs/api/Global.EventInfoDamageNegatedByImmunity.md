# Struct: EventInfoDamageNegatedByImmunity

- **Category:** <span class="cat-dot" style="--cat-color: #ef4444" data-cat="Combat & Abilities"></span> Combat & Abilities
- **Namespace:** `Global`
- **Assembly:** `Dew.Core.dll`

```csharp
public struct EventInfoDamageNegatedByImmunity
```

## Fields (4)

::: details Click to expand Fields (4)

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`actor`** | `public Actor actor` | The actor who started the damage. |
| **`data`** | `public FinalDamageData data` | Final damage data that is prevented. |
| **`effect`** | `public BasicEffect effect` | The basic effect responsible for the negated damage. e.g. ProtectedEffect, InvulnerableEffect |
| **`victim`** | `public Entity victim` | Victim of the negated damage. |

:::


## Architecture & Relationships

::: details Click to expand Architecture & Relationships

### Used By (3)

*Classes and systems that invoke, reference, or depend on `EventInfoDamageNegatedByImmunity`:*

[ClientEventManager](/api/Global.ClientEventManager) · `UI_DamageNumberGroup` · `Mirror.GeneratedNetworkCode`

### Dependencies (4)

*Types and components that `EventInfoDamageNegatedByImmunity` references or depends upon:*

[Actor](/api/Global.Actor) · [BasicEffect](/api/Global.BasicEffect) · [Entity](/api/Global.Entity) · [FinalDamageData](/api/Global.FinalDamageData)

:::
