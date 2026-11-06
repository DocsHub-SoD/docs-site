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


## Architecture & Relationships

::: details Click to expand Architecture & Relationships

### Used By (9)

*Classes and systems that invoke, reference, or depend on `AbilitySelfValidator`:*

[AbilityTrigger](/api/Global.AbilityTrigger) · `Ai_Mon_Ink_BossWhiteNight_Oppression` · `Ai_Mon_Ink_GhostSpear_Atk` · `Ai_Mon_Sky_BigBaam_BeamAtk` · `At_Atk_YubarStardust` · [ChannelData](/api/Global.ChannelData) · [ChargingChannelData](/api/Global.ChargingChannelData) · `Se_HunterBuff` · [TriggerConfig](/api/Global.TriggerConfig)

### Dependencies (5)

*Types and components that `AbilitySelfValidator` references or depends upon:*

[Actor](/api/Global.Actor) · [Entity](/api/Global.Entity) · [EntityControl](/api/Global.EntityControl) · [EntityStatus](/api/Global.EntityStatus) · [IEntityValidator](/api/Global.IEntityValidator)

:::
