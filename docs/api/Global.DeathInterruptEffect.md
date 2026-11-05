# Class: DeathInterruptEffect

- **Namespace:** `Global`
- **Assembly:** `Dew.Core.dll`
- **Inheritance / Derived:** [BasicEffect](/api/Global.BasicEffect)

```csharp
public class DeathInterruptEffect : BasicEffect
```

## Fields

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`onInterrupt`** | `public Action&lt;EventInfoKill&gt; onInterrupt` |  |
| **`priority`** | `public int priority` | DeathInterrupts with lower priority will be fired/checked earlier. |

## Properties

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`mask`** | `public override BasicEffectMask mask { get; }` |  |
