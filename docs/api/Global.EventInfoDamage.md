# Struct: EventInfoDamage

- **Category:** <span class="cat-dot" style="--cat-color: #ef4444" data-cat="Combat & Abilities"></span> Combat & Abilities
- **Namespace:** `Global`
- **Assembly:** `Dew.Core.dll`

```csharp
public struct EventInfoDamage
```

## Fields

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`actor`** | `public Actor actor` | The actor who invoked this event in an actor chain. |
| **`chain`** | `[NonSerialized] public ReactionChain chain` |  |
| **`damage`** | `public FinalDamageData damage` |  |
| **`negatedAmountByShield`** | `public float negatedAmountByShield` |  |
| **`victim`** | `public Entity victim` |  |
