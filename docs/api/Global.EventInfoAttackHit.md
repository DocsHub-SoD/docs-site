# Struct: EventInfoAttackHit

- **Namespace:** `Global`
- **Assembly:** `Dew.Core.dll`

```csharp
public struct EventInfoAttackHit
```

## Fields

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`actor`** | `public Actor actor` | The actor who invoked this event in an actor chain. |
| **`attacker`** | `public Entity attacker` | Attacker of this hit. |
| **`isCrit`** | `public bool isCrit` | Is hit attack critical hit? |
| **`strength`** | `public float strength` | Strength of this attack. Set to 1 by default. |
| **`victim`** | `public Entity victim` | Victim of this hit. |
