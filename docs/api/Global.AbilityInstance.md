# Class: AbilityInstance

- **Category:** <span class="cat-dot" style="--cat-color: #ef4444" data-cat="Combat & Abilities"></span> Combat & Abilities
- **Namespace:** `Global`
- **Assembly:** `Dew.Core.dll`
- **Inheritance / Derived:** [DewNetworkBehaviour](/api/Global.DewNetworkBehaviour) → [Actor](/api/Global.Actor) → [DamageInstance](/api/Global.DamageInstance) → [MeleeAttackInstance](/api/Global.MeleeAttackInstance) → [MockAbilityInstance](/api/Global.MockAbilityInstance) → [PickupInstance](/api/Global.PickupInstance) → [Projectile](/api/Global.Projectile) → [PunishmentInstance](/api/Global.PunishmentInstance) → [StatusEffect](/api/Global.StatusEffect)

```csharp
[LogicUpdatePriority(-200)]
public abstract class AbilityInstance : Actor, ILogicUpdate, ICleanup, ICustomDestroyRoutine
```

## Fields (12)

::: details Click to expand Fields (12)

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`budgetCost`** | `[BoxGroup("Ability Instance Settings", true, false, 0)] public int budgetCost` |  |
| **`chain`** | `[NonSerialized] public ReactionChain chain` | If this instance is part of reaction, you can provide ReactionChain in this variable. Available only on server. |
| **`currentCostSum`** | `public static int currentCostSum` |  |
| **`currentCostSumPerPlayer`** | `public static Dictionary<DewPlayer, int> currentCostSumPerPlayer` |  |
| **`endEffect`** | `[BoxGroup("Ability Instance Settings", true, false, 0)] [LabelText("End Effect (Attached To Caster)")] public GameObject endEffect` |  |
| **`maxBudget`** | `public static int maxBudget` |  |
| **`startEffect`** | `[BoxGroup("Ability Instance Settings", true, false, 0)] [LabelText("Loop Effect (Attached To Caster)")] public GameObject startEffect` |  |
| **`startEffectNoStop`** | `[BoxGroup("Ability Instance Settings", true, false, 0)] [LabelText("Start Effect (Attached To Caster)")] public GameObject startEffectNoStop` |  |
| **`tvDefaultAllExceptSelf`** | `protected AbilityTargetValidatorWrapper tvDefaultAllExceptSelf` |  |
| **`tvDefaultHarmfulEffectTargets`** | `protected AbilityTargetValidatorWrapper tvDefaultHarmfulEffectTargets` |  |
| **`tvDefaultUsefulEffectTargets`** | `protected AbilityTargetValidatorWrapper tvDefaultUsefulEffectTargets` |  |
| **`useBudgetSystem`** | `public static bool useBudgetSystem` |  |

:::

## Properties (7)

::: details Click to expand Properties (7)

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`budgetPressure`** | `public BudgetPressure budgetPressure { get; }` | Returns current budget pressure. Costly ability instances must adjust their resource spending according to this value.Requires budgetCost to be set to non-zero value. |
| **`effectiveLevel`** | `public int effectiveLevel { get; }` |  |
| **`gem`** | `public Gem gem { get; set; }` | If this instance is from a gem, you can access the gem from here. |
| **`hasOngoingSequences`** | `public bool hasOngoingSequences { get; }` |  |
| **`info`** | `[SaveVar(SaveVarFlags.Default)] public CastInfo info { get; set; }` |  |
| **`skillLevel`** | `[SaveVar(SaveVarFlags.Default)] public int skillLevel { get; set; }` | Level of its origin skill trigger at the time this instance was cast. Defaults to -1 or that of parent's level.Parent type can either be SkillTrigger, AbilityInstance, or Gem.You can override level by setting this field when the instance is preparing. |
| **`statEntity`** | `public Entity statEntity { get; }` |  |

:::

## Methods (29)

::: details `Budget_ShouldDoFullCalculations()`

Should this instance skip calculations? Based on current budget pressure.Use this as a default suggested behavior.

```csharp
public bool Budget_ShouldDoFullCalculations()
```

**Returns:** `bool`

:::

::: details `Budget_ShouldPlayEffects()`

Should this instance play effects? Based on current budget pressure.Use this as a default suggested behavior.

```csharp
public bool Budget_ShouldPlayEffects()
```

**Returns:** `bool`

:::

::: details `CreateDamage(SourceType, ScalingValue, float)`

```csharp
public DamageData CreateDamage(DamageData.SourceType type, ScalingValue value, float procCoefficient = 1)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `type` | [`DamageData.SourceType`](/api/Global.DamageData) |  |
| `value` | [`ScalingValue`](/api/Global.ScalingValue) |  |
| `procCoefficient` | `float` |  |

**Returns:** `DamageData`

:::

::: details `CreateStatusEffect&lt;T&gt;(T, Entity, Action&lt;T&gt;)`

Create a new status effect and attach it to an entity.This can return null if the creation fails:e.g. Trying to apply a status effect with isKilledByUnstoppable flag to an unstoppable/invulnerable entity.

```csharp
public T CreateStatusEffect<T>(T prefab, Entity victim, Action<T> beforePrepare = null) where T : StatusEffect
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `prefab` | `T` |  |
| `victim` | [`Entity`](/api/Global.Entity) |  |
| `beforePrepare` | `System.Action<T>` |  |
| `` | `T` |  |

**Returns:** `T`

:::

::: details `CreateStatusEffect&lt;T&gt;(Entity, Action&lt;T&gt;)`

Create a new status effect and attach it to an entity.This can return null if the creation fails:e.g. Trying to apply a status effect with isKilledByUnstoppable flag to an unstoppable/invulnerable entity.

```csharp
public T CreateStatusEffect<T>(Entity victim, Action<T> beforePrepare = null) where T : StatusEffect
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `victim` | [`Entity`](/api/Global.Entity) |  |
| `beforePrepare` | `System.Action<T>` |  |
| `` | `T` |  |

**Returns:** `T`

:::

::: details `Damage(ScalingValue, float)`

```csharp
public DamageData Damage(ScalingValue value, float procCoefficient = 1)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `value` | [`ScalingValue`](/api/Global.ScalingValue) |  |
| `procCoefficient` | `float` |  |

**Returns:** `DamageData`

:::

::: details `DefaultDamage(ScalingValue, float)`

```csharp
public DamageData DefaultDamage(ScalingValue value, float procCoefficient = 1)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `value` | [`ScalingValue`](/api/Global.ScalingValue) |  |
| `procCoefficient` | `float` |  |

**Returns:** `DamageData`

:::

::: details `DestroyOnCondition(Func&lt;bool&gt;)`

Kill this instance when condition is met.

```csharp
public AbilityInstance.WatchedCondition DestroyOnCondition(Func<bool> condition)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `condition` | `System.Func<TResult><bool>` |  |

**Returns:** `AbilityInstance.WatchedCondition`

:::

::: details `DestroyOnDeath(Entity, bool)`

Kill this instance when the specified entity dies/gets destroyed.

```csharp
public void DestroyOnDeath(Entity entity, bool includeKnockOuts = false)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `entity` | [`Entity`](/api/Global.Entity) |  |
| `includeKnockOuts` | `bool` |  |

:::

::: details `DestroyOnDestroy(Actor)`

Remove this instance when the specified actor gets destroyed.

```csharp
public void DestroyOnDestroy(Actor actor)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `actor` | [`Actor`](/api/Global.Actor) |  |

:::

::: details `GetActorReadableName()`

```csharp
public override string GetActorReadableName()
```

**Returns:** `string`

:::

::: details `GetValue(ScalingValue)`

```csharp
public float GetValue(ScalingValue val)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `val` | [`ScalingValue`](/api/Global.ScalingValue) |  |

**Returns:** `float`

:::

::: details `GetValue(StarScalingValue)`

```csharp
public float GetValue(StarScalingValue value)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `value` | [`StarScalingValue`](/api/Global.StarScalingValue) |  |

**Returns:** `float`

:::

::: details `GetValue&lt;T&gt;(T[])`

```csharp
public T GetValue<T>(T[] val)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `val` | `T[]` |  |
| `` | `T` |  |

**Returns:** `T`

:::

::: details `GetValueInt(StarScalingValue)`

```csharp
public int GetValueInt(StarScalingValue value)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `value` | [`StarScalingValue`](/api/Global.StarScalingValue) |  |

**Returns:** `int`

:::

::: details `Heal(ScalingValue)`

```csharp
public HealData Heal(ScalingValue amount)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `amount` | [`ScalingValue`](/api/Global.ScalingValue) |  |

**Returns:** `HealData`

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

::: details `MagicDamage(ScalingValue, float)`

```csharp
public DamageData MagicDamage(ScalingValue value, float procCoefficient = 1)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `value` | [`ScalingValue`](/api/Global.ScalingValue) |  |
| `procCoefficient` | `float` |  |

**Returns:** `DamageData`

:::

::: details `OnCreate()`

```csharp
protected override void OnCreate()
```

:::

::: details `OnCreateSequenced()`

Started everywhere when this ability instance is created, running on LogicUpdates.This will stop running when this instance gets killed.Return SequenceInstructions (e.g.new SI.WaitForSeconds()) to yield this sequence.Returning null has same effect ofnew SI.WaitForNextLogicUpdate().

```csharp
protected virtual IEnumerator OnCreateSequenced()
```

**Returns:** `System.Collections.IEnumerator`

:::

::: details `OnDestroyActor()`

```csharp
protected override void OnDestroyActor()
```

:::

::: details `OnPrepare()`

Called on server right before this instance to be spawned.Configure this instance's initial state here.By default this sets skillLevel to parent's level.Parent type can either be SkillTrigger, AbilityInstance, or Gem.

```csharp
protected override void OnPrepare()
```

:::

::: details `OnStart()`

```csharp
public override void OnStart()
```

:::

::: details `PhysicalDamage(ScalingValue, float)`

```csharp
public DamageData PhysicalDamage(ScalingValue value, float procCoefficient = 1)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `value` | [`ScalingValue`](/api/Global.ScalingValue) |  |
| `procCoefficient` | `float` |  |

**Returns:** `DamageData`

:::

::: details `PhysicalMagicDamage(ScalingValue, float)`

```csharp
public DamageData PhysicalMagicDamage(ScalingValue value, float procCoefficient = 1)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `value` | [`ScalingValue`](/api/Global.ScalingValue) |  |
| `procCoefficient` | `float` |  |

**Returns:** `DamageData`

:::

::: details `PureDamage(ScalingValue, float)`

```csharp
public DamageData PureDamage(ScalingValue value, float procCoefficient = 1)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `value` | [`ScalingValue`](/api/Global.ScalingValue) |  |
| `procCoefficient` | `float` |  |

**Returns:** `DamageData`

:::

::: details `ResetBudget()`

```csharp
public static void ResetBudget()
```

:::

::: details `StartChargingChannel(ChargingChannel)`

```csharp
public void StartChargingChannel(ChargingChannel channel)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `channel` | [`ChargingChannel`](/api/Global.ChargingChannel) |  |

:::

::: details `StartSequence(IEnumerator)`

Start a sequence that will run while this instance is alive on LogicUpdates.

```csharp
protected void StartSequence(IEnumerator sequence)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `sequence` | `System.Collections.IEnumerator` |  |

:::
