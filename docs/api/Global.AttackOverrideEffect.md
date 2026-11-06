# Class: AttackOverrideEffect

- **Category:** <span class="cat-dot" style="--cat-color: #ef4444" data-cat="Combat & Abilities"></span> Combat & Abilities
- **Namespace:** `Global`
- **Assembly:** `Dew.Core.dll`
- **Inheritance / Derived:** [BasicEffect](/api/Global.BasicEffect)

```csharp
public class AttackOverrideEffect : BasicEffect
```

## Fields (1)

::: details Click to expand Fields (1)

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`onUse`** | `public Action onUse` |  |

:::

## Properties (2)

::: details Click to expand Properties (2)

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`mask`** | `public override BasicEffectMask mask { get; }` |  |
| **`trigger`** | `public AbilityTrigger trigger { get; set; }` |  |

:::


## Architecture & Relationships

::: details Click to expand Architecture & Relationships

### Used By (2)

*Classes and systems that invoke, reference, or depend on `AttackOverrideEffect`:*

[EntityStatus](/api/Global.EntityStatus) · [StatusEffect](/api/Global.StatusEffect)

### Dependencies (4)

*Types and components that `AttackOverrideEffect` references or depends upon:*

[AbilityTrigger](/api/Global.AbilityTrigger) · [BasicEffect](/api/Global.BasicEffect) · [Entity](/api/Global.Entity) · [EntityStatus](/api/Global.EntityStatus)

### Related Enums (1)

*Enumerations referenced in fields, properties, or method signatures:*

[`BasicEffectMask`](/enums#basiceffectmask)

:::
