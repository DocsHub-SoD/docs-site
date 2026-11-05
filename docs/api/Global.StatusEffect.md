# Class: StatusEffect

- **Namespace:** `Global`
- **Assembly:** `Dew.Core.dll`
- **Inheritance / Derived:** [DewNetworkBehaviour](/api/Global.DewNetworkBehaviour) → [Actor](/api/Global.Actor) → [AbilityInstance](/api/Global.AbilityInstance) → [CurseStatusEffect](/api/Global.CurseStatusEffect) → [MiniBossEffect](/api/Global.MiniBossEffect) → [MirageSkinEffect](/api/Global.MirageSkinEffect) → [PersistentStatBonusEffect](/api/Global.PersistentStatBonusEffect) → [StackedStatusEffect](/api/Global.StackedStatusEffect) → [StarEffect](/api/Global.StarEffect)

```csharp
public abstract class StatusEffect : AbilityInstance, ILogicUpdate, ICleanup, ICustomDestroyRoutine
```

## Fields

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`addedMaterials`** | `[BoxGroup("StatusEffect Settings", true, false, 0)]
public Material[] addedMaterials` |  |
| **`bottomColor`** | `[BoxGroup("StatusEffect Settings", true, false, 0)]
[ShowIf("_showIcon", true)]
public Color bottomColor` |  |
| **`endEffectVictim`** | `[BoxGroup("StatusEffect Settings", true, false, 0)]
[LabelText("End Effect")]
public GameObject endEffectVictim` |  |
| **`HarmfulEffects`** | `public const BasicEffectMask HarmfulEffects = Slow \| Cripple \| Root \| Silence \| Stun \| Blind \| ArmorReduction \| HealReduction` |  |
| **`hideOnWorldHealthBar`** | `[BoxGroup("StatusEffect Settings", true, false, 0)]
[ShowIf("_showIcon", true)]
[ToggleLeft]
public bool hideOnWorldHealthBar` |  |
| **`icon`** | `[BoxGroup("StatusEffect Settings", true, false, 0)]
[ShowIf("_showIcon", true)]
public Sprite icon` |  |
| **`iconOrder`** | `[BoxGroup("StatusEffect Settings", true, false, 0)]
[ShowIf("_showIcon", true)]
public int iconOrder` |  |
| **`isBeneficialBuff`** | `[FormerlySerializedAs("isBeneficial")]
[BoxGroup("StatusEffect Settings", true, false, 0)]
[ToggleLeft]
public bool isBeneficialBuff` |  |
| **`isCleansable`** | `[BoxGroup("StatusEffect Settings", true, false, 0)]
[ToggleLeft]
public bool isCleansable` |  |
| **`isKilledByCrowdControlImmunity`** | `[BoxGroup("StatusEffect Settings", true, false, 0)]
[ToggleLeft]
public bool isKilledByCrowdControlImmunity` |  |
| **`scaleDurationByTenacity`** | `[BoxGroup("StatusEffect Settings", true, false, 0)]
[ToggleLeft]
public bool scaleDurationByTenacity` |  |
| **`startEffectVictim`** | `[Title("Effects On Victim", null, TitleAlignments.Left, true, true)]
[BoxGroup("StatusEffect Settings", true, false, 0)]
[LabelText("Start Effect")]
public GameObject startEffectVictim` |  |
| **`topColor`** | `[BoxGroup("StatusEffect Settings", true, false, 0)]
[ShowIf("_showIcon", true)]
public Color topColor` |  |

## Properties

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`basicEffects`** | `public IReadOnlyList&lt;BasicEffect&gt; basicEffects { get; }` | List of BasicEffects this status effect is applying to the victim entity. Only available on server. |
| **`isDestroyedOnRoomChange`** | `public override bool isDestroyedOnRoomChange { get; }` |  |
| **`maxDuration`** | `public float? maxDuration { get; }` |  |
| **`normalizedDuration`** | `public float? normalizedDuration { get; }` | Normalized remaining duration. Starts on 1.0f and ends on 0.0f. |
| **`numberDisplay`** | `public int? numberDisplay { get; set; }` |  |
| **`remainingDuration`** | `public float? remainingDuration { get; }` |  |
| **`showIcon`** | `public bool showIcon { get; set; }` |  |
| **`victim`** | `[SaveVar(SaveVarFlags.Default)]
public Entity victim { get; }` |  |

## Methods

### `ActiveLogicUpdate(float)`

```csharp
protected override void ActiveLogicUpdate(float dt)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `dt` | `float` |  |

### `DoAbility(Func&lt;AbilityTrigger, bool&gt;, Func&lt;AbilityTrigger, Action&gt;)`

Do custom action on all matching ability and do custom cleanup. You can invoke the returned action to immediately call cleanup functions to stop the effect.

```csharp
public SafeAction DoAbility(Func<AbilityTrigger, bool> condition, Func<AbilityTrigger, Action> callback)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `condition` | [System.Func&lt;T, TResult&gt;&lt;AbilityTrigger,bool&gt;](/api/Global.AbilityTrigger) |  |
| `callback` | [System.Func&lt;T, TResult&gt;&lt;AbilityTrigger,System.Action&gt;](/api/Global.AbilityTrigger) |  |

**Returns:** `SafeAction`

### `DoArmorBoost(float)`

ArmorBoost reduces all taken damage.

```csharp
public ArmorBoostEffect DoArmorBoost(float strength)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `strength` | `float` |  |

**Returns:** `ArmorBoostEffect`

### `DoArmorReduction(float)`

ArmorReduction increases all taken damage.

```csharp
public ArmorReductionEffect DoArmorReduction(float strength)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `strength` | `float` |  |

**Returns:** `ArmorReductionEffect`

### `DoAttackCritical(Action)`

AttackCritical makes the entity's attacks to always do a critical hit.

```csharp
public AttackCriticalEffect DoAttackCritical(Action onUse)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `onUse` | `System.Action` |  |

**Returns:** `AttackCriticalEffect`

### `DoAttackEmpower(Action&lt;EventInfoAttackEffect, int&gt;, int, Action)`

Note this will lock the status effect until basic attack instance is destroyed.

```csharp
public AttackEmpowerEffect DoAttackEmpower(Action<EventInfoAttackEffect, int> onAttackEffect, int maxTriggerCount = 2147483647, Action onDepleted = null)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `onAttackEffect` | [System.Action&lt;T1, T2&gt;&lt;EventInfoAttackEffect,int&gt;](/api/Global.EventInfoAttackEffect) |  |
| `maxTriggerCount` | `int` |  |
| `onDepleted` | `System.Action` |  |

**Returns:** `AttackEmpowerEffect`

### `DoAttackOverride(AbilityTrigger, Action)`

AttackOverride replaces the entity's attack AbilityTrigger with something else.This version uses an existing ability trigger.

```csharp
public AttackOverrideEffect DoAttackOverride(AbilityTrigger trigger, Action onUse)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `trigger` | [AbilityTrigger](/api/Global.AbilityTrigger) |  |
| `onUse` | `System.Action` |  |

**Returns:** `AttackOverrideEffect`

### `DoAttackOverride&lt;T&gt;(Action)`

AttackOverride replaces the entity's attack AbilityTrigger with something else.This version creates a new ability trigger of the given type and automatically disposes after use.

```csharp
public AttackOverrideEffect DoAttackOverride<T>(Action onUse) where T : AbilityTrigger
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `onUse` | `System.Action` |  |
| `` | `T` |  |

**Returns:** `AttackOverrideEffect`

### `DoBasicEffect(BasicEffect)`

```csharp
public void DoBasicEffect(BasicEffect eff)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `eff` | [BasicEffect](/api/Global.BasicEffect) |  |

### `DoBlind()`

Blind makes the entity miss its attacks.

```csharp
public BlindEffect DoBlind()
```

**Returns:** `BlindEffect`

### `DoCripple(float)`

Cripple reduces the entity's attack speed.

```csharp
public CrippleEffect DoCripple(float strength)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `strength` | `float` |  |

**Returns:** `CrippleEffect`

### `DoDeathInterrupt(Action&lt;EventInfoKill&gt;, int)`

Death Interrupt fires before entity's imminent death.DeathInterrupts with lower priority will be fired/checked earlier.Healing entity by any amount in an interrupt will prevent entity's death.If an interrupt prevents the death, other interrupts will not be fired.Note that interrupts can be ignored byEntity.KillNoInterrupt()

```csharp
public DeathInterruptEffect DoDeathInterrupt(Action<EventInfoKill> onInterrupt, int priority)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `onInterrupt` | [System.Action&lt;T&gt;&lt;EventInfoKill&gt;](/api/Global.EventInfoKill) |  |
| `priority` | `int` |  |

**Returns:** `DeathInterruptEffect`

### `DoFakeMaxHealthEffect(float)`

FakeMaxHealth increases shown max health only in health bars.

```csharp
public FakeMaxHealthEffect DoFakeMaxHealthEffect(float amount)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `amount` | `float` |  |

**Returns:** `FakeMaxHealthEffect`

### `DoHaste(float)`

Haste increases the entity's attack speed.

```csharp
public HasteEffect DoHaste(float strength)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `strength` | `float` |  |

**Returns:** `HasteEffect`

### `DoInvisible()`

Invisible makes the entity untargetable by targeted abilities and undetectable to enemies. Note this doesn't change the entity's graphical visibility.

```csharp
public InvisibleEffect DoInvisible()
```

**Returns:** `InvisibleEffect`

### `DoInvulnerable(Action&lt;EventInfoDamageNegatedByImmunity&gt;)`

Invulnerable makes the entity immune to damage and crowd controls.

```csharp
public InvulnerableEffect DoInvulnerable(Action<EventInfoDamageNegatedByImmunity> onDamageNegated = null)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `onDamageNegated` | [System.Action&lt;T&gt;&lt;EventInfoDamageNegatedByImmunity&gt;](/api/Global.EventInfoDamageNegatedByImmunity) |  |

**Returns:** `InvulnerableEffect`

### `DoProtected(Action&lt;EventInfoDamageNegatedByImmunity&gt;)`

Protected makes the entity immune to damage.

```csharp
public ProtectedEffect DoProtected(Action<EventInfoDamageNegatedByImmunity> onDamageNegated)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `onDamageNegated` | [System.Action&lt;T&gt;&lt;EventInfoDamageNegatedByImmunity&gt;](/api/Global.EventInfoDamageNegatedByImmunity) |  |

**Returns:** `ProtectedEffect`

### `DoRoot()`

Root impairs the entity's movement/movement ability.

```csharp
public RootEffect DoRoot()
```

**Returns:** `RootEffect`

### `DoShield(float, Action&lt;EventInfoDamageNegatedByShield&gt;)`

```csharp
public ShieldEffect DoShield(float amount, Action<EventInfoDamageNegatedByShield> onDamageNegated = null)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `amount` | `float` |  |
| `onDamageNegated` | [System.Action&lt;T&gt;&lt;EventInfoDamageNegatedByShield&gt;](/api/Global.EventInfoDamageNegatedByShield) |  |

**Returns:** `ShieldEffect`

### `DoSilence()`

Silence prevents the entity from using abilities.

```csharp
public SilenceEffect DoSilence()
```

**Returns:** `SilenceEffect`

### `DoSkill&lt;T&gt;(Action&lt;T&gt;)`

Do custom action on all matching skill. You can invoke the returned action to immediately call cleanup functions to stop the effect.

```csharp
public SafeAction DoSkill<T>(Action<T> callback) where T : SkillTrigger
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `callback` | `System.Action&lt;T&gt;&lt;T&gt;` |  |
| `` | `T` |  |

**Returns:** `SafeAction`

### `DoSkill&lt;T&gt;(Func&lt;T, Action&gt;)`

Do custom action on all matching skill and do custom cleanup. You can invoke the returned action to immediately call cleanup functions to stop the effect.

```csharp
public SafeAction DoSkill<T>(Func<T, Action> callback) where T : SkillTrigger
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `callback` | `System.Func&lt;T, TResult&gt;&lt;T,System.Action&gt;` |  |
| `` | `T` |  |

**Returns:** `SafeAction`

### `DoSlow(float)`

Slow reduces the entity's movement speed.

```csharp
public SlowEffect DoSlow(float strength)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `strength` | `float` |  |

**Returns:** `SlowEffect`

### `DoSpeed(float)`

Speed increases the entity's movement speed.

```csharp
public SpeedEffect DoSpeed(float strength)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `strength` | `float` |  |

**Returns:** `SpeedEffect`

### `DoStatBonus()`

Do a stat bonus to victim that expires on destruction of this status effect.

```csharp
public StatBonus DoStatBonus()
```

**Returns:** `StatBonus`

### `DoStatBonus(StatBonus)`

Do a stat bonus to victim that expires on destruction of this status effect.

```csharp
public StatBonus DoStatBonus(StatBonus bonus)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `bonus` | [StatBonus](/api/Global.StatBonus) |  |

**Returns:** `StatBonus`

### `DoStun()`

Stun prevents the entity from moving/using abilities/attacking.

```csharp
public StunEffect DoStun()
```

**Returns:** `StunEffect`

### `DoUncollidable()`

Uncollidable makes the entity uncollidable by non-targeted projectiles and abilities.

```csharp
public UncollidableEffect DoUncollidable()
```

**Returns:** `UncollidableEffect`

### `DoUnstoppable()`

Unstoppable makes the entity immune to crowd controls.

```csharp
public UnstoppableEffect DoUnstoppable()
```

**Returns:** `UnstoppableEffect`

### `FrameUpdate()`

```csharp
public override void FrameUpdate()
```

### `GetActorReadableName()`

```csharp
public override string GetActorReadableName()
```

**Returns:** `string`

### `GetCustomTooltipDescription()`

Called on the local client hovering over the status effect icon.

```csharp
public virtual string GetCustomTooltipDescription()
```

**Returns:** `string`

### `GetCustomTooltipName()`

Called on the local client hovering over the status effect icon.

```csharp
public virtual string GetCustomTooltipName()
```

**Returns:** `string`

### `HideOnScreenTimer()`

Hide this status effect's timer on the screen of the victim. Has no effect on non-player victim

```csharp
public void HideOnScreenTimer()
```

### `OnCreate()`

```csharp
protected override void OnCreate()
```

### `OnDestroyActor()`

```csharp
protected override void OnDestroyActor()
```

### `OnStartServer()`

```csharp
public override void OnStartServer()
```

### `ResetTimer()`

Reset a timer set bySetTimerto its initial duration.

```csharp
public void ResetTimer()
```

### `SetTimer(float, float)`

Set a timer that kills this status effect on expiration. The timer will update fillAmount automatically.

```csharp
public void SetTimer(float maxDuration, float duration)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `maxDuration` | `float` |  |
| `duration` | `float` |  |

### `SetTimer(float)`

Set a timer that kills this status effect on expiration. The timer will update fillAmount automatically.

```csharp
public void SetTimer(float duration)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `duration` | `float` |  |

### `ShowOnScreenTimer(string, Color, bool)`

Show this status effect's timer on the screen of the victim. Has no effect on non-player victim

```csharp
public void ShowOnScreenTimer(string customNameKey = null, Color color = default, bool invertValue = false)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `customNameKey` | `string` |  |
| `color` | `UnityEngine.Color` |  |
| `invertValue` | `bool` |  |

### `StopAllBasicEffects()`

```csharp
protected void StopAllBasicEffects()
```

### `StopBasicEffect(BasicEffect)`

```csharp
protected void StopBasicEffect(BasicEffect eff)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `eff` | [BasicEffect](/api/Global.BasicEffect) |  |

### `StopTimer()`

```csharp
public void StopTimer()
```
