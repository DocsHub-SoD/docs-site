# Struct: EventInfoAttackFired

- **Category:** <span class="cat-dot" style="--cat-color: #ef4444" data-cat="Combat & Abilities"></span> Combat & Abilities
- **Namespace:** `Global`
- **Assembly:** `Dew.Core.dll`

```csharp
public struct EventInfoAttackFired
```

## Fields

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`actor`** | `public Actor actor` | The actor who invoked this event in an actor chain. |
| **`everyFourAttackNormalizedProgress`** | `public float everyFourAttackNormalizedProgress` | Charge amount of every four attack effect, after firing this basic attack. |
| **`info`** | `public CastInfo info` | Cast info of this attack. Note the attack might be directional cast thus have no target. |
| **`instance`** | `public AbilityInstance instance` | The attack ability instance. |
| **`isCrit`** | `public bool isCrit` | Is fired attack critical hit? |
| **`isNextAttackFourthAttack`** | `public bool isNextAttackFourthAttack` | Is next attack going to be fourth attack? |
| **`isThisAttackFourthAttack`** | `public bool isThisAttackFourthAttack` | Is this attack fourth attack? |
