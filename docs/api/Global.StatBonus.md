# Class: StatBonus

- **Category:** <span class="cat-dot" style="--cat-color: #ef4444" data-cat="Combat & Abilities"></span> Combat & Abilities
- **Namespace:** `Global`
- **Assembly:** `Dew.Core.dll`

```csharp
[Serializable]
public class StatBonus
```

## Properties (31)

::: details Click to expand Properties (31)

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`abilityHasteFlat`** | `public float abilityHasteFlat { get; set; }` |  |
| **`abilityHastePercentage`** | `public float abilityHastePercentage { get; set; }` |  |
| **`abilityPowerFlat`** | `public float abilityPowerFlat { get; set; }` |  |
| **`abilityPowerPercentage`** | `public float abilityPowerPercentage { get; set; }` |  |
| **`armorFlat`** | `public float armorFlat { get; set; }` |  |
| **`armorPercentage`** | `public float armorPercentage { get; set; }` |  |
| **`attackDamageFlat`** | `public float attackDamageFlat { get; set; }` |  |
| **`attackDamagePercentage`** | `public float attackDamagePercentage { get; set; }` |  |
| **`attackRangeFlat`** | `public float attackRangeFlat { get; set; }` |  |
| **`attackRangePercentage`** | `public float attackRangePercentage { get; set; }` |  |
| **`attackSpeedPercentage`** | `public float attackSpeedPercentage { get; set; }` |  |
| **`coldEffectAmpFlat`** | `public float coldEffectAmpFlat { get; set; }` |  |
| **`critAmpFlat`** | `public float critAmpFlat { get; set; }` |  |
| **`critAmpPercentage`** | `public float critAmpPercentage { get; set; }` |  |
| **`critChanceFlat`** | `public float critChanceFlat { get; set; }` |  |
| **`critChancePercentage`** | `public float critChancePercentage { get; set; }` |  |
| **`darkEffectAmpFlat`** | `public float darkEffectAmpFlat { get; set; }` |  |
| **`everyFourAttackStartIndexFlat`** | `public int everyFourAttackStartIndexFlat { get; set; }` |  |
| **`fireEffectAmpFlat`** | `public float fireEffectAmpFlat { get; set; }` |  |
| **`healthRegenFlat`** | `public float healthRegenFlat { get; set; }` |  |
| **`healthRegenPercentage`** | `public float healthRegenPercentage { get; set; }` |  |
| **`lightEffectAmpFlat`** | `public float lightEffectAmpFlat { get; set; }` |  |
| **`manaRegenFlat`** | `public float manaRegenFlat { get; set; }` |  |
| **`manaRegenPercentage`** | `public float manaRegenPercentage { get; set; }` |  |
| **`maxHealthFlat`** | `public float maxHealthFlat { get; set; }` |  |
| **`maxHealthPercentage`** | `public float maxHealthPercentage { get; set; }` |  |
| **`maxManaFlat`** | `public float maxManaFlat { get; set; }` |  |
| **`maxManaPercentage`** | `public float maxManaPercentage { get; set; }` |  |
| **`movementSpeedPercentage`** | `public float movementSpeedPercentage { get; set; }` |  |
| **`tenacityFlat`** | `public float tenacityFlat { get; set; }` |  |
| **`tenacityPercentage`** | `public float tenacityPercentage { get; set; }` |  |

:::

## Methods (3)

::: details `Add(StatBonus)`

```csharp
public void Add(StatBonus bonus)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `bonus` | [`StatBonus`](/api/Global.StatBonus) |  |

:::

::: details `Clone()`

```csharp
public StatBonus Clone()
```

**Returns:** `StatBonus`

:::

::: details `Multiply(float)`

Multiplies all stat bonuses by the given multiplier. Useful for scaling bonuses based on level, rarity, or other factors.

```csharp
public void Multiply(float multiplier)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `multiplier` | `float` | The value to multiply all stat bonuses by |

:::
