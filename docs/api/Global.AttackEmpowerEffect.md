# Class: AttackEmpowerEffect

- **Category:** <span class="cat-dot" style="--cat-color: #ef4444" data-cat="Combat & Abilities"></span> Combat & Abilities
- **Namespace:** `Global`
- **Assembly:** `Dew.Core.dll`
- **Inheritance / Derived:** [BasicEffect](/api/Global.BasicEffect)

```csharp
public class AttackEmpowerEffect : BasicEffect
```

## Fields (3)

::: details Click to expand Fields (3)

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`maxTriggerCount`** | `public int maxTriggerCount` |  |
| **`onAttackEffect`** | `public Action<EventInfoAttackEffect, int> onAttackEffect` |  |
| **`onDepleted`** | `public Action onDepleted` |  |

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

*Classes and systems that invoke, reference, or depend on `AttackEmpowerEffect`:*

[StatusEffect](/api/Global.StatusEffect)

### Dependencies (1)

*Types and components that `AttackEmpowerEffect` references or depends upon:*

[BasicEffect](/api/Global.BasicEffect)

### Related Enums (1)

*Enumerations referenced in fields, properties, or method signatures:*

[`BasicEffectMask`](/enums#basiceffectmask)

:::
