# Class: EntityStatus

- **Category:** <span class="cat-dot" style="--cat-color: #ef4444" data-cat="Combat & Abilities"></span> Combat & Abilities
- **Namespace:** `Global`
- **Assembly:** `Dew.Core.dll`
- **Inheritance / Derived:** [DewNetworkBehaviour](/api/Global.DewNetworkBehaviour) → [EntityComponent](/api/Global.EntityComponent)

```csharp
[HideMonoScript]
public class EntityStatus : EntityComponent, ILogicUpdate, ICleanup
```

## Fields (10)

::: details Click to expand Fields (10)

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`baseStats`** | `[BoxGroup("Stat Settings", true, false, 0)] public BaseStats baseStats` |  |
| **`bonusStats`** | `[BoxGroup("Stat Settings", true, false, 0)] [NonSerialized] [ShowInInspector] [ReadOnly] [HideIn(PrefabKind.PrefabInstance\|PrefabKind.PrefabAsset)] public BonusStats bonusStats` |  |
| **`ClientEvent_OnOnFinalStatsUpdated`** | `public SafeAction ClientEvent_OnOnFinalStatsUpdated` |  |
| **`finalStats`** | `public FinalStats finalStats` | Base stats + scaling stats + bonus stats + basic effect stats |
| **`finalStatsProcessors`** | `public DataProcessorGroup<FinalStats> finalStatsProcessors` |  |
| **`manaTypeKey`** | `public string manaTypeKey` |  |
| **`MaximumArmorValue`** | `public const float MaximumArmorValue = 100000` |  |
| **`MinimumArmorValue`** | `public const float MinimumArmorValue = -300` |  |
| **`scalingStats`** | `[BoxGroup("Stat Settings", true, false, 0)] public BonusStats scalingStats` |  |
| **`statusEffects`** | `public readonly List<StatusEffect> statusEffects` | List of status effects this entity has. |

:::

## Properties (66)

::: details Click to expand Properties (66)

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
| **`currentHealth`** | `[SaveVar(SaveVarFlags.ApplyAfterFrameDelay)] public float currentHealth { get; }` |  |
| **`currentMana`** | `[SaveVar(SaveVarFlags.ApplyAfterFrameDelay)] public float currentMana { get; }` |  |
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
| **`level`** | `[SaveVar(SaveVarFlags.Default)] public int level { get; set; }` |  |
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

:::

## Methods (28)

::: details `AddStatBonus(StatBonus)`

Add the given bonus stats to this entity.

```csharp
public StatBonus AddStatBonus(StatBonus bonus)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `bonus` | [`StatBonus`](/api/Global.StatBonus) |  |

**Returns:** `StatBonus`

:::

::: details `CalculateTotalBonusStat(float, float, float)`

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

:::

::: details `DisableSectionTriggering()`

This entity will not trigger section colliders. Note EnableSectionTriggering() must be done after calling this function.

```csharp
public void DisableSectionTriggering()
```

:::

::: details `EnableSectionTriggering()`

This entity will trigger section colliders. Note this has to be done AFTER calling DisableSectionTriggering().

```csharp
public void EnableSectionTriggering()
```

:::

::: details `FindStatusEffect(Type, Func&lt;StatusEffect, bool&gt;)`

Find a status effect of given type with predicate.

```csharp
public StatusEffect FindStatusEffect(Type type, Func<StatusEffect, bool> predicate)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `type` | `System.Type` |  |
| `predicate` | [`System.Func<T, TResult><StatusEffect,bool>`](/api/Global.StatusEffect) |  |

**Returns:** `StatusEffect`

:::

::: details `FindStatusEffect&lt;T&gt;(Func&lt;T, bool&gt;)`

Find a status effect of given type with predicate.

```csharp
public T FindStatusEffect<T>(Func<T, bool> predicate) where T : StatusEffect
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `predicate` | `System.Func<T, TResult><T,bool>` |  |
| `` | `T` |  |

**Returns:** `T`

:::

::: details `GetBonusAbilityPower()`

```csharp
public float GetBonusAbilityPower()
```

**Returns:** `float`

:::

::: details `GetBonusArmor()`

```csharp
public float GetBonusArmor()
```

**Returns:** `float`

:::

::: details `GetBonusAttackDamage()`

```csharp
public float GetBonusAttackDamage()
```

**Returns:** `float`

:::

::: details `GetBonusHealth()`

```csharp
public float GetBonusHealth()
```

**Returns:** `float`

:::

::: details `GetElementalAmp(ElementalType)`

```csharp
public float GetElementalAmp(ElementalType type)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `type` | [`ElementalType`](/api/Global.ElementalType) |  |

**Returns:** `float`

:::

::: details `GetElementalStack(ElementalType)`

```csharp
public int GetElementalStack(ElementalType type)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `type` | [`ElementalType`](/api/Global.ElementalType) |  |

**Returns:** `int`

:::

::: details `GetStatusEffect(Type)`

Get a status effect of given type.

```csharp
public StatusEffect GetStatusEffect(Type type)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `type` | `System.Type` |  |

**Returns:** `StatusEffect`

:::

::: details `GetStatusEffect&lt;T&gt;()`

Get a status effect of given type.

```csharp
public T GetStatusEffect<T>() where T : StatusEffect
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `` | `T` |  |

**Returns:** `T`

:::

::: details `GetStatusEffects(Type)`

Enumerate all status effects of given type.

```csharp
public IEnumerable<StatusEffect> GetStatusEffects(Type type)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `type` | `System.Type` |  |

**Returns:** `System.Collections.Generic.IEnumerable<T><StatusEffect>`

:::

::: details `GetStatusEffects&lt;T&gt;()`

Enumerate all status effects of given type.

```csharp
public IEnumerable<T> GetStatusEffects<T>() where T : StatusEffect
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `` | `T` |  |

**Returns:** `System.Collections.Generic.IEnumerable<T>`

:::

::: details `HasElemental(ElementalType)`

```csharp
public bool HasElemental(ElementalType type)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `type` | [`ElementalType`](/api/Global.ElementalType) |  |

**Returns:** `bool`

:::

::: details `HasStatusEffect(Type)`

Does this entity has a status effect of a certain type?

```csharp
public bool HasStatusEffect(Type statusEffectType)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `statusEffectType` | `System.Type` |  |

**Returns:** `bool`

:::

::: details `HasStatusEffect&lt;T&gt;()`

Does this entity has a status effect of a certain type?

```csharp
public bool HasStatusEffect<T>() where T : StatusEffect
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `` | `T` |  |

**Returns:** `bool`

:::

::: details `HideHealth()`

```csharp
public void HideHealth()
```

:::

::: details `LogicUpdate(float)`

```csharp
public override void LogicUpdate(float dt)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `dt` | `float` |  |

:::

::: details `RemoveStatBonus(StatBonus)`

Remove the given bonus stats from this entity. Throws if the provided bonus did not exist on this entity.

```csharp
public void RemoveStatBonus(StatBonus bonus)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `bonus` | [`StatBonus`](/api/Global.StatBonus) |  |

:::

::: details `SetHealth(float)`

```csharp
public void SetHealth(float amount)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `amount` | `float` |  |

:::

::: details `SetMana(float)`

```csharp
public void SetMana(float amount)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `amount` | `float` |  |

:::

::: details `ShowHealth()`

```csharp
public void ShowHealth()
```

:::

::: details `TryGetStatusEffect(Type, out StatusEffect)`

Try to get an existing status effect instance on this entity.

```csharp
public bool TryGetStatusEffect(Type type, out StatusEffect effect)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `type` | `System.Type` |  |
| `effect` | [`StatusEffect`](/api/Global.StatusEffect) |  |

**Returns:** `bool`

:::

::: details `TryGetStatusEffect&lt;T&gt;(out T)`

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

:::

::: details `UpdateStats()`

Recalculate entity stats + stat processors + basic effects + bonus stats immediately.

```csharp
public void UpdateStats()
```

:::
