# Class: BasicEffectWithStrength

- **Namespace:** `Global`
- **Assembly:** `Dew.Core.dll`
- **Inheritance / Derived:** [BasicEffect](/api/Global.BasicEffect) → [ArmorBoostEffect](/api/Global.ArmorBoostEffect) → [ArmorReductionEffect](/api/Global.ArmorReductionEffect) → [CrippleEffect](/api/Global.CrippleEffect) → [FakeMaxHealthEffect](/api/Global.FakeMaxHealthEffect) → [HasteEffect](/api/Global.HasteEffect) → [SlowEffect](/api/Global.SlowEffect) → [SpeedEffect](/api/Global.SpeedEffect)

```csharp
public abstract class BasicEffectWithStrength : BasicEffect
```

## Properties

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`decay`** | `public bool decay { get; set; }` | If true, strength will be scaled to remaining duration of the status effect.Works only if the status effect has a timer active. |
| **`strength`** | `public float strength { get; set; }` |  |
