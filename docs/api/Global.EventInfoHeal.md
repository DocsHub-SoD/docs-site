# Struct: EventInfoHeal

- **Namespace:** `Global`
- **Assembly:** `Dew.Core.dll`

```csharp
public struct EventInfoHeal
```

## Fields

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`actor`** | `public Actor actor` | The actor who invoked this event in an actor chain. |
| **`amount`** | `public float amount` | Actual amount. |
| **`canMerge`** | `public bool canMerge` |  |
| **`chain`** | `public ReactionChain chain` |  |
| **`discardedAmount`** | `public float discardedAmount` | Discarded amount due to going over the maximum. |
| **`heal`** | `public FinalHealData heal` |  |
| **`isCrit`** | `public bool isCrit` |  |
| **`target`** | `public Entity target` |  |
