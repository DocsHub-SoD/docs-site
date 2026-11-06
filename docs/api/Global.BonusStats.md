# Struct: BonusStats

- **Category:** <span class="cat-dot" style="--cat-color: #ef4444" data-cat="Combat & Abilities"></span> Combat & Abilities
- **Namespace:** `Global`
- **Assembly:** `Dew.Core.dll`

```csharp
[Serializable]
public struct BonusStats
```

## Fields (32)

::: details Click to expand Fields (32)

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`abilityHasteFlat`** | `public float abilityHasteFlat` |  |
| **`abilityHastePercentage`** | `public float abilityHastePercentage` |  |
| **`abilityPowerFlat`** | `public float abilityPowerFlat` |  |
| **`abilityPowerPercentage`** | `public float abilityPowerPercentage` |  |
| **`armorFlat`** | `public float armorFlat` |  |
| **`armorPercentage`** | `[FormerlySerializedAs] [FormerlySerializedAs("armorPercetnage")] public float armorPercentage` |  |
| **`attackDamageFlat`** | `public float attackDamageFlat` |  |
| **`attackDamagePercentage`** | `public float attackDamagePercentage` |  |
| **`attackRangeFlat`** | `public float attackRangeFlat` |  |
| **`attackRangePercentage`** | `public float attackRangePercentage` |  |
| **`attackSpeedPercentage`** | `public float attackSpeedPercentage` |  |
| **`coldEffectAmpFlat`** | `public float coldEffectAmpFlat` |  |
| **`critAmpFlat`** | `public float critAmpFlat` |  |
| **`critAmpPercentage`** | `public float critAmpPercentage` |  |
| **`critChanceFlat`** | `public float critChanceFlat` |  |
| **`critChancePercentage`** | `public float critChancePercentage` |  |
| **`darkEffectAmpFlat`** | `public float darkEffectAmpFlat` |  |
| **`Default`** | `public static readonly BonusStats Default` |  |
| **`everyFourAttackStartIndexFlat`** | `public int everyFourAttackStartIndexFlat` |  |
| **`fireEffectAmpFlat`** | `public float fireEffectAmpFlat` |  |
| **`healthRegenFlat`** | `public float healthRegenFlat` |  |
| **`healthRegenPercentage`** | `public float healthRegenPercentage` |  |
| **`lightEffectAmpFlat`** | `public float lightEffectAmpFlat` |  |
| **`manaRegenFlat`** | `public float manaRegenFlat` |  |
| **`manaRegenPercentage`** | `public float manaRegenPercentage` |  |
| **`maxHealthFlat`** | `public float maxHealthFlat` |  |
| **`maxHealthPercentage`** | `public float maxHealthPercentage` |  |
| **`maxManaFlat`** | `public float maxManaFlat` |  |
| **`maxManaPercentage`** | `public float maxManaPercentage` |  |
| **`movementSpeedPercentage`** | `public float movementSpeedPercentage` |  |
| **`tenacityFlat`** | `public float tenacityFlat` |  |
| **`tenacityPercentage`** | `public float tenacityPercentage` |  |

:::

## Methods (3)

::: details `Equals(BonusStats)`

```csharp
public bool Equals(BonusStats other)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `other` | [`BonusStats`](/api/Global.BonusStats) |  |

**Returns:** `bool`

:::

::: details `Equals(object)`

```csharp
public override bool Equals(object obj)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `obj` | `object` |  |

**Returns:** `bool`

:::

::: details `GetHashCode()`

```csharp
public override int GetHashCode()
```

**Returns:** `int`

:::


## Architecture & Relationships

::: details Click to expand Architecture & Relationships

### Used By (4)

*Classes and systems that invoke, reference, or depend on `BonusStats`:*

[EntityStatus](/api/Global.EntityStatus) · `LucidDream_MarshOfDestiny` · [StatBonus](/api/Global.StatBonus) · `Mirror.GeneratedNetworkCode`

### Dependencies (2)

*Types and components that `BonusStats` references or depends upon:*

[DewMath](/api/Global.DewMath) · [StatBonus](/api/Global.StatBonus)

:::
