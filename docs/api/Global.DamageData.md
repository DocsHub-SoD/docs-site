# Struct: DamageData

- **Category:** <span class="cat-dot" style="--cat-color: #ef4444" data-cat="Combat & Abilities"></span> Combat & Abilities
- **Namespace:** `Global`
- **Assembly:** `Dew.Core.dll`

```csharp
public struct DamageData
```

## Fields

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`elemental`** | `public ElementalType? elemental` |  |
| **`source`** | `public DamageData.SourceType source` | Source type of this damage. |

## Properties

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`actor`** | `public readonly Actor actor { get; }` |  |
| **`amplificationMultiplier`** | `public readonly float amplificationMultiplier { get; }` | Damage multiplier for amplications. Amplications are multiplicatively combined. This value will be multiplied to the damage after flatModifier. |
| **`attackEffectStrength`** | `public readonly float attackEffectStrength { get; }` | Attack effect strength (0~1). If this value is above 0, this damage will trigger attack effects. |
| **`attackEffectType`** | `public readonly AttackEffectType attackEffectType { get; }` |  |
| **`attributes`** | `public readonly DamageAttribute attributes { get; }` |  |
| **`currentAmount`** | `public float currentAmount { get; }` | Amount of processed damage with current modifications. |
| **`damageToShieldMultiplier`** | `public readonly float damageToShieldMultiplier { get; }` |  |
| **`direction`** | `public readonly Vector3? direction { get; }` | Direction of this damage. |
| **`flatModifier`** | `public readonly float flatModifier { get; }` | Flat damage modifier. This value will be added to the final damage before any other multipliers. |
| **`isBlockedByImmunity`** | `public readonly bool isBlockedByImmunity { get; }` | Is this damage currently blocked by immunity? |
| **`originalAmount`** | `public readonly float originalAmount { get; }` | Original amount of damage. |
| **`originPosition`** | `public readonly Vector3? originPosition { get; }` | Origin position of this damage. |
| **`overrideElementalStacks`** | `public readonly int? overrideElementalStacks { get; }` |  |
| **`procCoefficient`** | `public readonly float procCoefficient { get; }` | Proc coefficient of damage. |
| **`reductionMultiplier`** | `public readonly float reductionMultiplier { get; }` | Damage multiplier for reductions. Reductions are multiplicatively combined. This value will be multiplied to the damage after flatModifier. |

## Methods

### `AddFlatAmount(float)`

Add a flat amount to this damage.

```csharp
public DamageData AddFlatAmount(float amount)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `amount` | `float` | The amount to add. Must be a positive number or zero. |

**Returns:** `DamageData`

### `ApplyAmplification(float)`

Amplify this damage by the value specified, stacking multiplicatively.e.g. One Amplication by 0.5 will cause 50% increase in damage.Two Amplifications by 0.5 will cause 125% increase in damage.

```csharp
public DamageData ApplyAmplification(float value)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `value` | `float` | Amplification value. Must be a positive number or zero. |

**Returns:** `DamageData`

### `ApplyDamageToShieldMultiplier(float)`

```csharp
public DamageData ApplyDamageToShieldMultiplier(float multiplier)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `multiplier` | `float` |  |

**Returns:** `DamageData`

### `ApplyRawMultiplier(float)`

Apply raw multiplier to this damage's original amount.

```csharp
public DamageData ApplyRawMultiplier(float multiplier)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `multiplier` | `float` |  |

**Returns:** `DamageData`

### `ApplyReduction(float)`

Reduce this damage by the value specified, stacking multiplicatively.e.g. One Reduction by 0.5 will cause 50% decrease in damage.Two Reductions by 0.5 will cause 75% decrease in damage.

```csharp
public DamageData ApplyReduction(float value)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `value` | `float` | Reduction value. This value will be clamped between 0 and 1. |

**Returns:** `DamageData`

### `ApplyStrength(float)`

Apply the given multiplier to the damage and the proc coefficient.

```csharp
public DamageData ApplyStrength(float multiplier)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `multiplier` | `float` |  |

**Returns:** `DamageData`

### `BlockWithImmunity()`

Block this damage with damage immunity. Note this will be ignored ifIgnoreDamageImmunityis set to true.

```csharp
public DamageData BlockWithImmunity()
```

**Returns:** `DamageData`

### `Dispatch(Entity, ReactionChain)`

```csharp
public void Dispatch(Entity victim, ReactionChain chain = default)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `victim` | [`Entity`](/api/Global.Entity) |  |
| `chain` | [`ReactionChain`](/api/Global.ReactionChain) |  |

### `DoAttackEffect(AttackEffectType, float)`

```csharp
public DamageData DoAttackEffect(AttackEffectType type, float strength = 1)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `type` | [`AttackEffectType`](/api/Global.AttackEffectType) |  |
| `strength` | `float` |  |

**Returns:** `DamageData`

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

### `IsAmountModifiedBy(Actor)`

```csharp
public bool IsAmountModifiedBy(Actor actor)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `actor` | [`Actor`](/api/Global.Actor) |  |

**Returns:** `bool`

### `IsAmountModifiedBy(Type)`

```csharp
public bool IsAmountModifiedBy(Type actorType)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `actorType` | `System.Type` |  |

**Returns:** `bool`

### `SetActor(Actor)`

```csharp
public DamageData SetActor(Actor actor)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `actor` | [`Actor`](/api/Global.Actor) |  |

**Returns:** `DamageData`

### `SetAmountModifiedBy(Actor)`

```csharp
public DamageData SetAmountModifiedBy(Actor actor)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `actor` | [`Actor`](/api/Global.Actor) |  |

**Returns:** `DamageData`

### `SetAmountModifiedBy(Type)`

```csharp
public DamageData SetAmountModifiedBy(Type actorType)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `actorType` | `System.Type` |  |

**Returns:** `DamageData`

### `SetAmountOrigin(FinalDamageData)`

If amount of this damage originates from other damage, you can specify it here to make it inherit its modifier flags and attributes.

```csharp
public DamageData SetAmountOrigin(FinalDamageData damage)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `damage` | [`FinalDamageData`](/api/Global.FinalDamageData) |  |

**Returns:** `DamageData`

### `SetAmountOrigin(FinalHealData)`

If amount of this damage originates from other heal, you can specify it here to make it inherit its modifier flags and isCrit.

```csharp
public DamageData SetAmountOrigin(FinalHealData heal)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `heal` | [`FinalHealData`](/api/Global.FinalHealData) |  |

**Returns:** `DamageData`

### `SetAttr(DamageAttribute)`

Add special attribute for this damage.

```csharp
public DamageData SetAttr(DamageAttribute attr)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `attr` | [`DamageAttribute`](/api/Global.DamageAttribute) |  |

**Returns:** `DamageData`

### `SetDirection(Quaternion)`

```csharp
public DamageData SetDirection(Quaternion rot)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `rot` | `UnityEngine.Quaternion` |  |

**Returns:** `DamageData`

### `SetDirection(Vector3)`

```csharp
public DamageData SetDirection(Vector3 dir)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `dir` | `UnityEngine.Vector3` |  |

**Returns:** `DamageData`

### `SetElemental(ElementalType?)`

```csharp
public DamageData SetElemental(ElementalType? type)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `type` | [`ElementalType?`](/api/Global.ElementalType) |  |

**Returns:** `DamageData`

### `SetOriginPosition(Vector3)`

```csharp
public DamageData SetOriginPosition(Vector3 pos)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `pos` | `UnityEngine.Vector3` |  |

**Returns:** `DamageData`

### `SetOverrideElementalStacks(int)`

Set this to override number of elemental stacks this damage applies.

```csharp
public DamageData SetOverrideElementalStacks(int stacks)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `stacks` | `int` |  |

**Returns:** `DamageData`

### `SetSourceType(SourceType)`

```csharp
public DamageData SetSourceType(DamageData.SourceType type)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `type` | [`DamageData.SourceType`](/api/Global.DamageData) |  |

**Returns:** `DamageData`

### `SubtractFlatAmount(float)`

Subtract a flat amount from this damage.

```csharp
public DamageData SubtractFlatAmount(float amount)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `amount` | `float` | The amount to subtract. Must be a positive number or zero. |

**Returns:** `DamageData`
