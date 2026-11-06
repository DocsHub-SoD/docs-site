# Struct: FinalDamageData

- **Category:** <span class="cat-dot" style="--cat-color: #ef4444" data-cat="Combat & Abilities"></span> Combat & Abilities
- **Namespace:** `Global`
- **Assembly:** `Dew.Core.dll`

```csharp
public struct FinalDamageData
```

## Fields

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

## Properties

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`canMerge`** | `public bool canMerge { get; }` |  |

## Methods

### `HasAttr(DamageAttribute)`

Does this damage has specific attribute?

```csharp
public bool HasAttr(DamageAttribute attr)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `attr` | [`DamageAttribute`](/api/Global.DamageAttribute) |  |

**Returns:** `bool`
