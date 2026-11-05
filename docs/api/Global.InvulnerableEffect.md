# Class: InvulnerableEffect

- **Namespace:** `Global`
- **Assembly:** `Dew.Core.dll`
- **Inheritance / Derived:** [BasicEffect](/api/Global.BasicEffect)

```csharp
public class InvulnerableEffect : BasicEffect
```

## Fields

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`onDamageNegated`** | `public Action&lt;EventInfoDamageNegatedByImmunity&gt; onDamageNegated` | If multiple effect is protecting this entity, only the last basic effect's callback will be called prioritizing InvulnerableEffect. |

## Properties

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`mask`** | `public override BasicEffectMask mask { get; }` |  |
