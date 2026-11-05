# Class: EntityStatus

- **Namespace:** `Global`
- **Assembly:** `Dew.Core.dll`
- **Inheritance / Derived:** [DewNetworkBehaviour](/api/Global.DewNetworkBehaviour) → [EntityComponent](/api/Global.EntityComponent)

```csharp
[HideMonoScript]
public class EntityStatus : EntityComponent, ILogicUpdate, ICleanup
```

## Fields

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`baseStats`** | `[BoxGroup("Stat Settings", true, false, 0)]
public BaseStats baseStats` |  |
| **`bonusStats`** | `[BoxGroup("Stat Settings", true, false, 0)]
[NonSerialized]
[ShowInInspector]
[ReadOnly]
[HideIn(PrefabKind.PrefabInstance\|PrefabKind.PrefabAsset)]
public BonusStats bonusStats` |  |
| **`ClientEvent_OnOnFinalStatsUpdated`** | `public SafeAction ClientEvent_OnOnFinalStatsUpdated` |  |
| **`finalStats`** | `public FinalStats finalStats` | Base stats + scaling stats + bonus stats + basic effect stats |
| **`finalStatsProcessors`** | `public DataProcessorGroup&lt;FinalStats&gt; finalStatsProcessors` |  |
| **`manaTypeKey`** | `public string manaTypeKey` |  |
| **`MaximumArmorValue`** | `public const float MaximumArmorValue = 100000` |  |
| **`MinimumArmorValue`** | `public const float MinimumArmorValue = -300` |  |
| **`scalingStats`** | `[BoxGroup("Stat Settings", true, false, 0)]
public BonusStats scalingStats` |  |
| **`statusEffects`** | `public readonly List&lt;StatusEffect&gt; statusEffects` | List of status effects this entity has. |

## Properties

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`abilityHaste`** | `public float abilityHaste { get; }` |  |
| **`abilityPower`** | `public float abilityPower { get; }` |  |
| **`armor`** | `public float armor { get; }` |  |
| **`attackDamage`** | `public float attackDamage { get; }` |  |
| **`attackSpeedMultiplier`** | `public float attackSpeedMultiplier { get; }` |  |
| **`basicEffectMask`** | `public BasicEffectMask basicEffectMask { get; }` |  |
| **`coldEffectAmp`** | `public float coldEffectAmp { get; }` |  |
| **`critAmp`** | `public float critAmp { get; }` |  |
| **`critChance`** | `public float critChance { get; }` |  |
| **`currentHealth`** | `[SaveVar(SaveVarFlags.ApplyAfterFrameDelay)]
public float currentHealth { get; }` |  |
| **`currentMana`** | `[SaveVar(SaveVarFlags.ApplyAfterFrameDelay)]
public float currentMana { get; }` |  |
| **`currentShield`** | `public float currentShield { get; }` |  |
| **`darkEffectAmp`** | `public float darkEffectAmp { get; }` |  |
| **`darkStack`** | `public int darkStack { get; }` |  |
| **`fireEffectAmp`** | `public float fireEffectAmp { get; }` |  |
| **`fireStack`** | `public int fireStack { get; }` |  |
| **`hasArmorBoost`** | `public bool hasArmorBoost { get; }` |  |
| **`hasArmorReduction`** | `public bool hasArmorReduction { get; }` |  |
| **`hasAttackCritical`** | `public bool hasAttackCritical { get; }` |  |
| **`hasAttackOverride`** | `public bool hasAttackOverride { get; }` |  |
| **`hasBlind`** | `public bool hasBlind { get; }` |  |
| **`hasCold`** | `public bool hasCold { get; }` |  |
| **`hasCripple`** | `public bool hasCripple { get; }` |  |
| **`hasCrowdControlImmunity`** | `public bool hasCrowdControlImmunity { get; }` |  |
| **`hasDamageImmunity`** | `public bool hasDamageImmunity { get; }` |  |
| **`hasDeathInterrupt`** | `public bool hasDeathInterrupt { get; }` |  |
| **`hasHaste`** | `public bool hasHaste { get; }` |  |
| **`hasImmobility`** | `public bool hasImmobility { get; }` |  |
| **`hasInvisible`** | `public bool hasInvisible { get; }` |  |
| **`hasInvulnerable`** | `public bool hasInvulnerable { get; }` |  |
| **`hasMirageSkin`** | `public bool hasMirageSkin { get; }` |  |
| **`hasProtected`** | `public bool hasProtected { get; }` |  |
| **`hasRoot`** | `public bool hasRoot { get; }` |  |
| **`hasSilence`** | `public bool hasSilence { get; }` |  |
| **`hasSlow`** | `public bool hasSlow { get; }` |  |
| **`hasSpeed`** | `public bool hasSpeed { get; }` |  |
| **`hasStun`** | `public bool hasStun { get; }` |  |
| **`hasUncollidable`** | `public bool hasUncollidable { get; }` |  |
| **`hasUnstoppable`** | `public bool hasUnstoppable { get; }` |  |
| **`healthRegen`** | `public float healthRegen { get; }` |  |
| **`isAlive`** | `public bool isAlive { get; }` |  |
| **`isDead`** | `public bool isDead { get; }` |  |
| **`isHealthHidden`** | `public bool isHealthHidden { get; }` |  |
| **`isInConversation`** | `public bool isInConversation { get; }` |  |
| **`isSectionTriggeringDisabled`** | `public CounterBool isSectionTriggeringDisabled { get; }` |  |
| **`level`** | `[SaveVar(SaveVarFlags.Default)]
public int level { get; set; }` |  |
| **`lightEffectAmp`** | `public float lightEffectAmp { get; }` |  |
| **`lightStack`** | `public int lightStack { get; }` |  |
| **`manaRegen`** | `public float manaRegen { get; }` |  |
| **`maxHealth`** | `public float maxHealth { get; }` |  |
| **`maxMana`** | `public float maxMana { get; }` |  |
| **`mirageSkinInitAmount`** | `public float mirageSkinInitAmount { get; }` |  |
| **`missingHealth`** | `public float missingHealth { get; }` |  |
| **`missingMana`** | `public float missingMana { get; }` |  |
| **`movementSpeedMultiplier`** | `public float movementSpeedMultiplier { get; }` |  |
| **`normalizedHealth`** | `public float normalizedHealth { get; }` |  |
| **`normalizedMana`** | `public float normalizedMana { get; }` |  |
| **`overridenAttack`** | `public AbilityTrigger overridenAttack { get; }` |  |
| **`specialFill`** | `public Vector2 specialFill { get; set; }` |  |
| **`tenacity`** | `public float tenacity { get; }` |  |
| **`totalArmorFromStatusEffects`** | `public float totalArmorFromStatusEffects { get; }` |  |
| **`totalCripple`** | `public float totalCripple { get; }` |  |
| **`totalFakeMaxHealth`** | `public float totalFakeMaxHealth { get; }` |  |
| **`totalHaste`** | `public float totalHaste { get; }` |  |
| **`totalSlow`** | `public float totalSlow { get; }` |  |
| **`totalSpeed`** | `public float totalSpeed { get; }` |  |

## Methods

### `AddStatBonus(StatBonus)`

Add the given bonus stats to this entity.

```csharp
public StatBonus AddStatBonus(StatBonus bonus)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `bonus` | [StatBonus](/api/Global.StatBonus) |  |

**Returns:** `StatBonus`

### `CalculateTotalBonusStat(float, float, float)`

```csharp
public float CalculateTotalBonusStat(float current, float bonusFlat, float bonusPercentage)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `current` | `float` |  |
| `bonusFlat` | `float` |  |
| `bonusPercentage` | `float` |  |

**Returns:** `float`

### `DisableSectionTriggering()`

This entity will not trigger section colliders. Note EnableSectionTriggering() must be done after calling this function.

```csharp
public void DisableSectionTriggering()
```

### `EnableSectionTriggering()`

This entity will trigger section colliders. Note this has to be done AFTER calling DisableSectionTriggering().

```csharp
public void EnableSectionTriggering()
```

### `FindStatusEffect(Type, Func&lt;StatusEffect, bool&gt;)`

Find a status effect of given type with predicate.

```csharp
public StatusEffect FindStatusEffect(Type type, Func<StatusEffect, bool> predicate)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `type` | `System.Type` |  |
| `predicate` | [System.Func&lt;T, TResult&gt;&lt;StatusEffect,bool&gt;](/api/Global.StatusEffect) |  |

**Returns:** `StatusEffect`

### `FindStatusEffect&lt;T&gt;(Func&lt;T, bool&gt;)`

Find a status effect of given type with predicate.

```csharp
public T FindStatusEffect<T>(Func<T, bool> predicate) where T : StatusEffect
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `predicate` | `System.Func&lt;T, TResult&gt;&lt;T,bool&gt;` |  |
| `` | `T` |  |

**Returns:** `T`

### `GetBonusAbilityPower()`

```csharp
public float GetBonusAbilityPower()
```

**Returns:** `float`

### `GetBonusArmor()`

```csharp
public float GetBonusArmor()
```

**Returns:** `float`

### `GetBonusAttackDamage()`

```csharp
public float GetBonusAttackDamage()
```

**Returns:** `float`

### `GetBonusHealth()`

```csharp
public float GetBonusHealth()
```

**Returns:** `float`

### `GetElementalAmp(ElementalType)`

```csharp
public float GetElementalAmp(ElementalType type)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `type` | [ElementalType](/api/Global.ElementalType) |  |

**Returns:** `float`

### `GetElementalStack(ElementalType)`

```csharp
public int GetElementalStack(ElementalType type)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `type` | [ElementalType](/api/Global.ElementalType) |  |

**Returns:** `int`

### `GetStatusEffect(Type)`

Get a status effect of given type.

```csharp
public StatusEffect GetStatusEffect(Type type)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `type` | `System.Type` |  |

**Returns:** `StatusEffect`

### `GetStatusEffect&lt;T&gt;()`

Get a status effect of given type.

```csharp
public T GetStatusEffect<T>() where T : StatusEffect
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `` | `T` |  |

**Returns:** `T`

### `GetStatusEffects(Type)`

Enumerate all status effects of given type.

```csharp
public IEnumerable<StatusEffect> GetStatusEffects(Type type)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `type` | `System.Type` |  |

**Returns:** `System.Collections.Generic.IEnumerable&lt;T&gt;&lt;StatusEffect&gt;`

### `GetStatusEffects&lt;T&gt;()`

Enumerate all status effects of given type.

```csharp
public IEnumerable<T> GetStatusEffects<T>() where T : StatusEffect
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `` | `T` |  |

**Returns:** `System.Collections.Generic.IEnumerable&lt;T&gt;&lt;T&gt;`

### `HasElemental(ElementalType)`

```csharp
public bool HasElemental(ElementalType type)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `type` | [ElementalType](/api/Global.ElementalType) |  |

**Returns:** `bool`

### `HasStatusEffect(Type)`

Does this entity has a status effect of a certain type?

```csharp
public bool HasStatusEffect(Type statusEffectType)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `statusEffectType` | `System.Type` |  |

**Returns:** `bool`

### `HasStatusEffect&lt;T&gt;()`

Does this entity has a status effect of a certain type?

```csharp
public bool HasStatusEffect<T>() where T : StatusEffect
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `` | `T` |  |

**Returns:** `bool`

### `HideHealth()`

```csharp
public void HideHealth()
```

### `LogicUpdate(float)`

```csharp
public override void LogicUpdate(float dt)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `dt` | `float` |  |

### `RemoveStatBonus(StatBonus)`

Remove the given bonus stats from this entity. Throws if the provided bonus did not exist on this entity.

```csharp
public void RemoveStatBonus(StatBonus bonus)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `bonus` | [StatBonus](/api/Global.StatBonus) |  |

### `SetHealth(float)`

```csharp
public void SetHealth(float amount)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `amount` | `float` |  |

### `SetMana(float)`

```csharp
public void SetMana(float amount)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `amount` | `float` |  |

### `ShowHealth()`

```csharp
public void ShowHealth()
```

### `TryGetStatusEffect(Type, out StatusEffect)`

Try to get an existing status effect instance on this entity.

```csharp
public bool TryGetStatusEffect(Type type, out StatusEffect effect)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `type` | `System.Type` |  |
| `effect` | [StatusEffect](/api/Global.StatusEffect) |  |

**Returns:** `bool`

### `TryGetStatusEffect&lt;T&gt;(out T)`

Try to get an existing status effect instance on this entity.

```csharp
public bool TryGetStatusEffect<T>(out T effect) where T : StatusEffect
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `effect` | `T` |  |
| `` | `T` |  |

**Returns:** `bool`

### `UpdateStats()`

Recalculate entity stats + stat processors + basic effects + bonus stats immediately.

```csharp
public void UpdateStats()
```
