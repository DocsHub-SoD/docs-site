# Struct: EventInfoAttackMissed

- **Category:** <span class="cat-dot" style="--cat-color: #ef4444" data-cat="Combat & Abilities"></span> Combat & Abilities
- **Namespace:** `Global`
- **Assembly:** `Dew.Core.dll`

```csharp
public struct EventInfoAttackMissed
```

## Fields

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`actor`** | `public Actor actor` | The actor who invoked this event in an actor chain. |
| **`attacker`** | `public Entity attacker` | Attacker of this hit. |
| **`isCrit`** | `public bool isCrit` | Is hit attack critical hit? |
| **`victim`** | `public Entity victim` | Victim of this hit. |
