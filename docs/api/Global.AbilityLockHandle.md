# Class: AbilityLockHandle

- **Category:** <span class="cat-dot" style="--cat-color: #ef4444" data-cat="Combat & Abilities"></span> Combat & Abilities
- **Namespace:** `Global`
- **Assembly:** `Dew.Core.dll`

```csharp
public class AbilityLockHandle
```

## Properties (1)

::: details Click to expand Properties (1)

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`shouldShowLockEffect`** | `public bool shouldShowLockEffect { get; }` |  |

:::

## Methods (17)

::: details `LockAbilityCast(int)`

```csharp
public AbilityLockHandle LockAbilityCast(int index)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `index` | `int` |  |

**Returns:** `AbilityLockHandle`

:::

::: details `LockAbilityEdit(int)`

```csharp
public AbilityLockHandle LockAbilityEdit(int index)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `index` | `int` |  |

**Returns:** `AbilityLockHandle`

:::

::: details `LockAllAbilitiesCast()`

This includes attack ability and movement ability.

```csharp
public AbilityLockHandle LockAllAbilitiesCast()
```

**Returns:** `AbilityLockHandle`

:::

::: details `LockAllActiveMainSkillsCast()`

Locks Q, W, E, R

```csharp
public AbilityLockHandle LockAllActiveMainSkillsCast()
```

**Returns:** `AbilityLockHandle`

:::

::: details `LockAllMainSkillsCast()`

Locks Q, W, E, R, Trait

```csharp
public AbilityLockHandle LockAllMainSkillsCast()
```

**Returns:** `AbilityLockHandle`

:::

::: details `LockAllMainSkillsEdit()`

Locks Q, W, E, R, Trait

```csharp
public AbilityLockHandle LockAllMainSkillsEdit()
```

**Returns:** `AbilityLockHandle`

:::

::: details `LockAttackAbilityCast()`

```csharp
public AbilityLockHandle LockAttackAbilityCast()
```

**Returns:** `AbilityLockHandle`

:::

::: details `LockMovementSkillCast()`

```csharp
public AbilityLockHandle LockMovementSkillCast()
```

**Returns:** `AbilityLockHandle`

:::

::: details `Stop()`

```csharp
public AbilityLockHandle Stop()
```

**Returns:** `AbilityLockHandle`

:::

::: details `UnlockAbilityCast(int)`

```csharp
public AbilityLockHandle UnlockAbilityCast(int index)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `index` | `int` |  |

**Returns:** `AbilityLockHandle`

:::

::: details `UnlockAbilityEdit(int)`

```csharp
public AbilityLockHandle UnlockAbilityEdit(int index)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `index` | `int` |  |

**Returns:** `AbilityLockHandle`

:::

::: details `UnlockAllAbilitiesCast()`

This includes attack ability and movement ability.

```csharp
public AbilityLockHandle UnlockAllAbilitiesCast()
```

**Returns:** `AbilityLockHandle`

:::

::: details `UnlockAllActiveMainSkillsCast()`

Unlocks Q, W, E, R

```csharp
public AbilityLockHandle UnlockAllActiveMainSkillsCast()
```

**Returns:** `AbilityLockHandle`

:::

::: details `UnlockAllMainSkillsCast()`

Unlocks Q, W, E, R, Trait

```csharp
public AbilityLockHandle UnlockAllMainSkillsCast()
```

**Returns:** `AbilityLockHandle`

:::

::: details `UnlockAllMainSkillsEdit()`

Unlocks Q, W, E, R, Trait

```csharp
public AbilityLockHandle UnlockAllMainSkillsEdit()
```

**Returns:** `AbilityLockHandle`

:::

::: details `UnlockAttackAbilityCast()`

```csharp
public AbilityLockHandle UnlockAttackAbilityCast()
```

**Returns:** `AbilityLockHandle`

:::

::: details `UnlockMovementSkillCast()`

```csharp
public AbilityLockHandle UnlockMovementSkillCast()
```

**Returns:** `AbilityLockHandle`

:::


## Architecture & Relationships

::: details Click to expand Architecture & Relationships

### Used By (20)

*Classes and systems that invoke, reference, or depend on `AbilityLockHandle`:*

`Ai_C_Whirlwind` · [EntityAbility](/api/Global.EntityAbility) · `Gem_L_ChaosApple` · `Primus_Ending` · `Se_Curse_DreamAfflictionParalytic` · `Se_Curse_FaintMemory` · `Se_Curse_SilentNight_Locked` · `Se_D_PrismaticEyes` · `Se_FallenStar_WaveringIdentity` · `Se_Gem_L_Infinity` · `Se_GravityTraining` · `Se_HeroBleedingOut` · `Se_L_PyranasFireball` · `Se_MirageSkin_Oblivion_Silenced` · `Se_Mon_Special_BossPolaris_Monster_Scream_SkillLocked` · `Se_R_FrozenFists` · `Se_U_Burrow` · `Se_U_HerWorld_Blackhole` · `Se_U_Hysteria` · `St_L_HerosReturn`

### Dependencies (1)

*Types and components that `AbilityLockHandle` references or depends upon:*

[EntityAbility](/api/Global.EntityAbility)

:::
