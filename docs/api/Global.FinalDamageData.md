# Struct: FinalDamageData

- **Category:** <span class="cat-dot" style="--cat-color: #ef4444" data-cat="Combat & Abilities"></span> Combat & Abilities
- **Namespace:** `Global`
- **Assembly:** `Dew.Core.dll`

```csharp
public struct FinalDamageData
```

## Fields (10)

::: details Click to expand Fields (10)

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`amount`** | `public float amount` |  |
| **`attackEffectStrength`** | `public float attackEffectStrength` |  |
| **`attackEffectType`** | `public AttackEffectType attackEffectType` |  |
| **`attributes`** | `public DamageAttribute attributes` |  |
| **`direction`** | `public Vector3? direction` |  |
| **`discardedAmount`** | `public float discardedAmount` |  |
| **`elemental`** | `public ElementalType? elemental` |  |
| **`overrideElementalStacks`** | `public int? overrideElementalStacks` |  |
| **`procCoefficient`** | `public float procCoefficient` |  |
| **`type`** | `public DamageData.SourceType type` |  |

:::

## Properties (1)

::: details Click to expand Properties (1)

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`canMerge`** | `public bool canMerge { get; }` |  |

:::

## Methods (1)

::: details `HasAttr(DamageAttribute)`

Does this damage has specific attribute?

```csharp
public bool HasAttr(DamageAttribute attr)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `attr` | [`DamageAttribute`](/api/Global.DamageAttribute) |  |

**Returns:** `bool`

:::
