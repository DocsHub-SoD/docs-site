# Class: ProtectedEffect

- **Category:** <span class="cat-dot" style="--cat-color: #a855f7" data-cat="Buffs & Statuses"></span> Buffs & Statuses
- **Namespace:** `Global`
- **Assembly:** `Dew.Core.dll`
- **Inheritance / Derived:** [BasicEffect](/api/Global.BasicEffect)

```csharp
public class ProtectedEffect : BasicEffect
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
