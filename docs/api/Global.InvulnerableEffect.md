# Class: InvulnerableEffect

- **Category:** <span class="cat-dot" style="--cat-color: #a855f7" data-cat="Buffs & Statuses"></span> Buffs & Statuses
- **Namespace:** `Global`
- **Assembly:** `Dew.Core.dll`
- **Inheritance / Derived:** [BasicEffect](/api/Global.BasicEffect)

```csharp
public class InvulnerableEffect : BasicEffect
```

## Fields (1)

::: details Click to expand Fields (1)

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`onDamageNegated`** | `public Action<EventInfoDamageNegatedByImmunity> onDamageNegated` | If multiple effect is protecting this entity, only the last basic effect's callback will be called prioritizing InvulnerableEffect. |

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

*Classes and systems that invoke, reference, or depend on `InvulnerableEffect`:*

[StatusEffect](/api/Global.StatusEffect)

### Dependencies (1)

*Types and components that `InvulnerableEffect` references or depends upon:*

[BasicEffect](/api/Global.BasicEffect)

### Related Enums (1)

*Enumerations referenced in fields, properties, or method signatures:*

[`BasicEffectMask`](/enums#basiceffectmask)

:::
