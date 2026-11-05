# Class: BasicEffect

- **Namespace:** `Global`
- **Assembly:** `Dew.Core.dll`
- **Inheritance / Derived:** [AttackCriticalEffect](/api/Global.AttackCriticalEffect) → [AttackEmpowerEffect](/api/Global.AttackEmpowerEffect) → [AttackOverrideEffect](/api/Global.AttackOverrideEffect) → [BasicEffectWithStrength](/api/Global.BasicEffectWithStrength) → [BlindEffect](/api/Global.BlindEffect) → [DeathInterruptEffect](/api/Global.DeathInterruptEffect) → [InvisibleEffect](/api/Global.InvisibleEffect) → [InvulnerableEffect](/api/Global.InvulnerableEffect) → [ProtectedEffect](/api/Global.ProtectedEffect) → [RootEffect](/api/Global.RootEffect) → [ShieldEffect](/api/Global.ShieldEffect) → [SilenceEffect](/api/Global.SilenceEffect) → [StunEffect](/api/Global.StunEffect) → [UncollidableEffect](/api/Global.UncollidableEffect) → [UnstoppableEffect](/api/Global.UnstoppableEffect)

```csharp
public abstract class BasicEffect
```

## Properties

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`isAlive`** | `public bool isAlive { get; }` |  |
| **`mask`** | `public abstract BasicEffectMask mask { get; }` |  |
| **`parent`** | `public StatusEffect parent { get; }` |  |
| **`victim`** | `public Entity victim { get; }` |  |
