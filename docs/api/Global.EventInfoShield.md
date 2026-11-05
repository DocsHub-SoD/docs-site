# Struct: EventInfoShield

- **Namespace:** `Global`
- **Assembly:** `Dew.Core.dll`

```csharp
public struct EventInfoShield
```

## Fields

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`chain`** | `public ReactionChain chain` |  |
| **`discardedAmount`** | `public float discardedAmount` | The amount of discarded shield due to total max restrictions. |
| **`finalAmount`** | `public float finalAmount` | The amount of shield after being processed by processors. |
| **`originalAmount`** | `public float originalAmount` | The amount of shield before being processed by processors. |
| **`statusEffect`** | `public StatusEffect statusEffect` | The status effect that is giving the entity shield. |
| **`target`** | `public Entity target` | The entity receiving the shield. |
