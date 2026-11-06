# Class: ShieldEffect

- **Category:** <span class="cat-dot" style="--cat-color: #ef4444" data-cat="Combat & Abilities"></span> Combat & Abilities
- **Namespace:** `Global`
- **Assembly:** `Dew.Core.dll`
- **Inheritance / Derived:** [BasicEffect](/api/Global.BasicEffect)

```csharp
public class ShieldEffect : BasicEffect
```

## Fields

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`onAmountModified`** | `public Action<float, float> onAmountModified` | Called when the amount of this shield is modified by any means. In code, by damage, etc. |
| **`onDamageNegated`** | `public SafeAction<EventInfoDamageNegatedByShield> onDamageNegated` | Called when this shield negates a damage. Partially or completely. |

## Properties

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`amount`** | `public float amount { get; set; }` |  |
| **`mask`** | `public override BasicEffectMask mask { get; }` |  |

## Methods

### `AddAmount(float, float, bool)`

This will process, add the amount to the effect, and invoke relevant effects.

```csharp
public void AddAmount(float originalAmount, float totalMax = Infinity, bool processTotalMax = true)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `originalAmount` | `float` |  |
| `totalMax` | `float` |  |
| `processTotalMax` | `bool` |  |
