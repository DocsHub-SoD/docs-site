# Struct: HealData

- **Namespace:** `Global`
- **Assembly:** `Dew.Core.dll`

```csharp
public struct HealData
```

## Properties

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`actor`** | `public readonly Actor actor { get; }` |  |
| **`amplificationMultiplier`** | `public readonly float amplificationMultiplier { get; }` | Heal multiplier for amplications. |
| **`canMerge`** | `public readonly bool canMerge { get; }` | Can this heal number be merged into single number |
| **`currentAmount`** | `public float currentAmount { get; }` | Amount of processed damage with current modifications. |
| **`flatModifier`** | `public readonly float flatModifier { get; }` | Flat heal modifier. This value will be added to the final heal before any other multipliers. |
| **`isCrit`** | `public readonly bool isCrit { get; }` | Should this heal show a critical hit marker? |
| **`originalAmount`** | `public readonly float originalAmount { get; }` | Original amount of heal. |
| **`reductionMultiplier`** | `public readonly float reductionMultiplier { get; }` | Heal multiplier for reductions. |

## Methods

### `AddAmount(float)`

Add a flat amount to this heal.

```csharp
public HealData AddAmount(float amount)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `amount` | `float` | The amount to add. Must be a positive number or zero. |

**Returns:** `HealData`

### `ApplyAmplification(float)`

Amplify this heal by the value specified, stacking additively.e.g. One Amplication by 0.5 will cause 50% increase in heal.Two Amplifications by 0.5 will cause 125% increase in heal.

```csharp
public HealData ApplyAmplification(float value)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `value` | `float` | Amplification value. Must be a positive number or zero. |

**Returns:** `HealData`

### `ApplyRawMultiplier(float)`

Apply raw multiplier to this heal's original amount.

```csharp
public HealData ApplyRawMultiplier(float multiplier)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `multiplier` | `float` |  |

**Returns:** `HealData`

### `ApplyReduction(float)`

Reduce this heal by the value specified, stacking multiplicatively.e.g. One Reduction by 0.5 will cause 50% decrease in heal.Two Reductions by 0.5 will cause 75% decrease in heal.

```csharp
public HealData ApplyReduction(float value)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `value` | `float` | Reduction value. This value will be clamped between 0 and 1. |

**Returns:** `HealData`

### `Dispatch(Entity, ReactionChain)`

```csharp
public void Dispatch(Entity victim, ReactionChain chain = default)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `victim` | [Entity](/api/Global.Entity) |  |
| `chain` | [ReactionChain](/api/Global.ReactionChain) |  |

### `IsAmountModifiedBy(Actor)`

```csharp
public bool IsAmountModifiedBy(Actor actor)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `actor` | [Actor](/api/Global.Actor) |  |

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
public HealData SetActor(Actor actor)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `actor` | [Actor](/api/Global.Actor) |  |

**Returns:** `HealData`

### `SetAmountModifiedBy(Actor)`

```csharp
public HealData SetAmountModifiedBy(Actor actor)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `actor` | [Actor](/api/Global.Actor) |  |

**Returns:** `HealData`

### `SetAmountModifiedBy(Type)`

```csharp
public HealData SetAmountModifiedBy(Type actorType)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `actorType` | `System.Type` |  |

**Returns:** `HealData`

### `SetAmountOrigin(FinalDamageData)`

If amount of this heal originates from other damage, you can specify it here to make it inherit its flags and isCrit.

```csharp
public HealData SetAmountOrigin(FinalDamageData damage)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `damage` | [FinalDamageData](/api/Global.FinalDamageData) |  |

**Returns:** `HealData`

### `SetAmountOrigin(FinalHealData)`

If amount of this heal originates from other heal, you can specify it here to make it inherit its flags and isCrit.

```csharp
public HealData SetAmountOrigin(FinalHealData heal)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `heal` | [FinalHealData](/api/Global.FinalHealData) |  |

**Returns:** `HealData`

### `SetCanMerge()`

Make this heal mergeable into one damage number in UI.

```csharp
public HealData SetCanMerge()
```

**Returns:** `HealData`

### `SetCrit()`

Make this heal show a critical hit marker.

```csharp
public HealData SetCrit()
```

**Returns:** `HealData`

### `SetOriginalAmount(float)`

```csharp
public HealData SetOriginalAmount(float newAmount)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `newAmount` | `float` |  |

**Returns:** `HealData`

### `SubtractAmount(float)`

Subtract a flat amount from this heal.

```csharp
public HealData SubtractAmount(float amount)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `amount` | `float` | The amount to subtract. Must be a positive number or zero. |

**Returns:** `HealData`
