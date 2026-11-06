# Struct: EventInfoDamageNegatedByImmunity

- **Category:** <span class="cat-dot" style="--cat-color: #ef4444" data-cat="Combat & Abilities"></span> Combat & Abilities
- **Namespace:** `Global`
- **Assembly:** `Dew.Core.dll`

```csharp
public struct EventInfoDamageNegatedByImmunity
```

## Fields

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`actor`** | `public Actor actor` | The actor who started the damage. |
| **`data`** | `public FinalDamageData data` | Final damage data that is prevented. |
| **`effect`** | `public BasicEffect effect` | The basic effect responsible for the negated damage. e.g. ProtectedEffect, InvulnerableEffect |
| **`victim`** | `public Entity victim` | Victim of the negated damage. |
