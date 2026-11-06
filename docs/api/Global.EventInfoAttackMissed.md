# Struct: EventInfoAttackMissed

- **Category:** <span class="cat-dot" style="--cat-color: #ef4444" data-cat="Combat & Abilities"></span> Combat & Abilities
- **Namespace:** `Global`
- **Assembly:** `Dew.Core.dll`

```csharp
public struct EventInfoAttackMissed
```

## Fields (4)

::: details Click to expand Fields (4)

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`actor`** | `public Actor actor` | The actor who invoked this event in an actor chain. |
| **`attacker`** | `public Entity attacker` | Attacker of this hit. |
| **`isCrit`** | `public bool isCrit` | Is hit attack critical hit? |
| **`victim`** | `public Entity victim` | Victim of this hit. |

:::


## Architecture & Relationships

::: details Click to expand Architecture & Relationships

### Used By (2)

*Classes and systems that invoke, reference, or depend on `EventInfoAttackMissed`:*

[ClientEventManager](/api/Global.ClientEventManager) · `Mirror.GeneratedNetworkCode`

### Dependencies (2)

*Types and components that `EventInfoAttackMissed` references or depends upon:*

[Actor](/api/Global.Actor) · [Entity](/api/Global.Entity)

:::
