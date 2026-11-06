# Class: PunishmentInstance

- **Category:** <span class="cat-dot" style="--cat-color: #ef4444" data-cat="Combat & Abilities"></span> Combat & Abilities
- **Namespace:** `Global`
- **Assembly:** `Dew.Core.dll`
- **Inheritance / Derived:** [DewNetworkBehaviour](/api/Global.DewNetworkBehaviour) → [Actor](/api/Global.Actor) → [AbilityInstance](/api/Global.AbilityInstance)

```csharp
public class PunishmentInstance : AbilityInstance, ILogicUpdate, ICleanup, ICustomDestroyRoutine
```

## Fields (1)

::: details Click to expand Fields (1)

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`chanceWeight`** | `public float chanceWeight` |  |

:::


## Architecture & Relationships

::: details Click to expand Architecture & Relationships

### Used By (5)

*Classes and systems that invoke, reference, or depend on `PunishmentInstance`:*

`Ai_Hatred_Curse` · `Ai_Hatred_Explosion` · `Ai_Hatred_InkMapCurse` · `Ai_Hatred_Monsters` · `Ai_Hatred_SpawnLightning`

### Dependencies (1)

*Types and components that `PunishmentInstance` references or depends upon:*

[AbilityInstance](/api/Global.AbilityInstance)

:::
