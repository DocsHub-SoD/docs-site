# Class: BasicEffect

- **Category:** <span class="cat-dot" style="--cat-color: #a855f7" data-cat="Buffs & Statuses"></span> Buffs & Statuses
- **Namespace:** `Global`
- **Assembly:** `Dew.Core.dll`
- **Inheritance / Derived:** [AttackCriticalEffect](/api/Global.AttackCriticalEffect) → [AttackEmpowerEffect](/api/Global.AttackEmpowerEffect) → [AttackOverrideEffect](/api/Global.AttackOverrideEffect) → [BasicEffectWithStrength](/api/Global.BasicEffectWithStrength) → [BlindEffect](/api/Global.BlindEffect) → [DeathInterruptEffect](/api/Global.DeathInterruptEffect) → [InvisibleEffect](/api/Global.InvisibleEffect) → [InvulnerableEffect](/api/Global.InvulnerableEffect) → [ProtectedEffect](/api/Global.ProtectedEffect) → [RootEffect](/api/Global.RootEffect) → [ShieldEffect](/api/Global.ShieldEffect) → [SilenceEffect](/api/Global.SilenceEffect) → [StunEffect](/api/Global.StunEffect) → [UncollidableEffect](/api/Global.UncollidableEffect) → [UnstoppableEffect](/api/Global.UnstoppableEffect)

```csharp
public abstract class BasicEffect
```

## Properties (4)

::: details Click to expand Properties (4)

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`isAlive`** | `public bool isAlive { get; }` |  |
| **`mask`** | `public abstract BasicEffectMask mask { get; }` |  |
| **`parent`** | `public StatusEffect parent { get; }` |  |
| **`victim`** | `public Entity victim { get; }` |  |

:::


## Architecture & Relationships

::: details Click to expand Architecture & Relationships

### Used By (26)

*Classes and systems that invoke, reference, or depend on `BasicEffect`:*

[Actor](/api/Global.Actor) · `Ai_E_MassCleanse` · [AttackCriticalEffect](/api/Global.AttackCriticalEffect) · [AttackEmpowerEffect](/api/Global.AttackEmpowerEffect) · [AttackOverrideEffect](/api/Global.AttackOverrideEffect) · [BasicEffectWithStrength](/api/Global.BasicEffectWithStrength) · [BlindEffect](/api/Global.BlindEffect) · [DeathInterruptEffect](/api/Global.DeathInterruptEffect) · [EntityStatus](/api/Global.EntityStatus) · [EventInfoDamageNegatedByImmunity](/api/Global.EventInfoDamageNegatedByImmunity) · [Gem](/api/Global.Gem) · `Gem_L_Supersymmetry` · [InvisibleEffect](/api/Global.InvisibleEffect) · [InvulnerableEffect](/api/Global.InvulnerableEffect) · `NetworkReaderWriterExtensions` · [ProtectedEffect](/api/Global.ProtectedEffect) · `RevealEffect` · [RootEffect](/api/Global.RootEffect) · `Se_GenericEffectContainer` · [ShieldEffect](/api/Global.ShieldEffect) · [SilenceEffect](/api/Global.SilenceEffect) · [StatusEffect](/api/Global.StatusEffect) · [StunEffect](/api/Global.StunEffect) · [UncollidableEffect](/api/Global.UncollidableEffect) · [UnstoppableEffect](/api/Global.UnstoppableEffect) · `UntargetableEffect`

### Dependencies (2)

*Types and components that `BasicEffect` references or depends upon:*

[Entity](/api/Global.Entity) · [StatusEffect](/api/Global.StatusEffect)

### Related Enums (1)

*Enumerations referenced in fields, properties, or method signatures:*

[`BasicEffectMask`](/enums#basiceffectmask)

:::
