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
