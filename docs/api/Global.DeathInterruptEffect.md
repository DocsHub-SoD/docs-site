# Class: DeathInterruptEffect

- **Category:** <span class="cat-dot" style="--cat-color: #a855f7" data-cat="Buffs & Statuses"></span> Buffs & Statuses
- **Namespace:** `Global`
- **Assembly:** `Dew.Core.dll`
- **Inheritance / Derived:** [BasicEffect](/api/Global.BasicEffect)

```csharp
public class DeathInterruptEffect : BasicEffect
```

## Fields (2)

::: details Click to expand Fields (2)

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`onInterrupt`** | `public Action<EventInfoKill> onInterrupt` |  |
| **`priority`** | `public int priority` | DeathInterrupts with lower priority will be fired/checked earlier. |

:::

## Properties (1)

::: details Click to expand Properties (1)

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`mask`** | `public override BasicEffectMask mask { get; }` |  |

:::


## Architecture & Relationships

::: details Click to expand Architecture & Relationships

### Used By (1)

*Classes and systems that invoke, reference, or depend on `DeathInterruptEffect`:*

[StatusEffect](/api/Global.StatusEffect)

### Dependencies (1)

*Types and components that `DeathInterruptEffect` references or depends upon:*

[BasicEffect](/api/Global.BasicEffect)

### Related Enums (1)

*Enumerations referenced in fields, properties, or method signatures:*

[`BasicEffectMask`](/enums#basiceffectmask)

:::
