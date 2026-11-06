# Class: DeathInterruptEffect

- **Category:** <span class="cat-dot" style="--cat-color: #a855f7" data-cat="Buffs & Statuses"></span> Buffs & Statuses
- **Namespace:** `Global`
- **Assembly:** `Dew.Core.dll`
- **Inheritance / Derived:** [BasicEffect](/api/Global.BasicEffect)

```csharp
public class DeathInterruptEffect : BasicEffect
```

## Fields

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`onInterrupt`** | `public Action<EventInfoKill> onInterrupt` |  |
| **`priority`** | `public int priority` | DeathInterrupts with lower priority will be fired/checked earlier. |

## Properties

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`mask`** | `public override BasicEffectMask mask { get; }` |  |
