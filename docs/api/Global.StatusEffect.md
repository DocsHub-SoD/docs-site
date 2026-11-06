# Class: StatusEffect

- **Category:** <span class="cat-dot" style="--cat-color: #ef4444" data-cat="Combat & Abilities"></span> Combat & Abilities
- **Namespace:** `Global`
- **Assembly:** `Dew.Core.dll`
- **Inheritance / Derived:** [DewNetworkBehaviour](/api/Global.DewNetworkBehaviour) → [Actor](/api/Global.Actor) → [AbilityInstance](/api/Global.AbilityInstance) → [CurseStatusEffect](/api/Global.CurseStatusEffect) → [MiniBossEffect](/api/Global.MiniBossEffect) → [MirageSkinEffect](/api/Global.MirageSkinEffect) → [PersistentStatBonusEffect](/api/Global.PersistentStatBonusEffect) → [StackedStatusEffect](/api/Global.StackedStatusEffect) → [StarEffect](/api/Global.StarEffect)

```csharp
public abstract class StatusEffect : AbilityInstance, ILogicUpdate, ICleanup, ICustomDestroyRoutine
```

## Fields (13)

::: details Click to expand Fields (13)

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`addedMaterials`** | `[BoxGroup("StatusEffect Settings", true, false, 0)] public Material[] addedMaterials` |  |
| **`bottomColor`** | `[BoxGroup("StatusEffect Settings", true, false, 0)] [ShowIf("_showIcon", true)] public Color bottomColor` |  |
| **`endEffectVictim`** | `[BoxGroup("StatusEffect Settings", true, false, 0)] [LabelText("End Effect")] public GameObject endEffectVictim` |  |
| **`HarmfulEffects`** | `public const BasicEffectMask HarmfulEffects = Slow \| Cripple \| Root \| Silence \| Stun \| Blind \| ArmorReduction \| HealReduction` |  |
| **`hideOnWorldHealthBar`** | `[BoxGroup("StatusEffect Settings", true, false, 0)] [ShowIf("_showIcon", true)] [ToggleLeft] public bool hideOnWorldHealthBar` |  |
| **`icon`** | `[BoxGroup("StatusEffect Settings", true, false, 0)] [ShowIf("_showIcon", true)] public Sprite icon` |  |
| **`iconOrder`** | `[BoxGroup("StatusEffect Settings", true, false, 0)] [ShowIf("_showIcon", true)] public int iconOrder` |  |
| **`isBeneficialBuff`** | `[FormerlySerializedAs("isBeneficial")] [BoxGroup("StatusEffect Settings", true, false, 0)] [ToggleLeft] public bool isBeneficialBuff` |  |
| **`isCleansable`** | `[BoxGroup("StatusEffect Settings", true, false, 0)] [ToggleLeft] public bool isCleansable` |  |
| **`isKilledByCrowdControlImmunity`** | `[BoxGroup("StatusEffect Settings", true, false, 0)] [ToggleLeft] public bool isKilledByCrowdControlImmunity` |  |
| **`scaleDurationByTenacity`** | `[BoxGroup("StatusEffect Settings", true, false, 0)] [ToggleLeft] public bool scaleDurationByTenacity` |  |
| **`startEffectVictim`** | `[Title("Effects On Victim", null, TitleAlignments.Left, true, true)] [BoxGroup("StatusEffect Settings", true, false, 0)] [LabelText("Start Effect")] public GameObject startEffectVictim` |  |
| **`topColor`** | `[BoxGroup("StatusEffect Settings", true, false, 0)] [ShowIf("_showIcon", true)] public Color topColor` |  |

:::

## Properties (8)

::: details Click to expand Properties (8)

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`basicEffects`** | `public IReadOnlyList<BasicEffect> basicEffects { get; }` | List of BasicEffects this status effect is applying to the victim entity. Only available on server. |
| **`isDestroyedOnRoomChange`** | `public override bool isDestroyedOnRoomChange { get; }` |  |
| **`maxDuration`** | `public float? maxDuration { get; }` |  |
| **`normalizedDuration`** | `public float? normalizedDuration { get; }` | Normalized remaining duration. Starts on 1.0f and ends on 0.0f. |
| **`numberDisplay`** | `public int? numberDisplay { get; set; }` |  |
| **`remainingDuration`** | `public float? remainingDuration { get; }` |  |
| **`showIcon`** | `public bool showIcon { get; set; }` |  |
| **`victim`** | `[SaveVar(SaveVarFlags.Default)] public Entity victim { get; }` |  |

:::

## Methods (44)

::: details `ActiveLogicUpdate(float)`

```csharp
protected override void ActiveLogicUpdate(float dt)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `dt` | `float` |  |

:::

::: details `DoAbility(Func&lt;AbilityTrigger, bool&gt;, Func&lt;AbilityTrigger, Action&gt;)`

Do custom action on all matching ability and do custom cleanup. You can invoke the returned action to immediately call cleanup functions to stop the effect.

```csharp
public SafeAction DoAbility(Func<AbilityTrigger, bool> condition, Func<AbilityTrigger, Action> callback)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `condition` | [`System.Func<T, TResult><AbilityTrigger,bool>`](/api/Global.AbilityTrigger) |  |
| `callback` | [`System.Func<T, TResult><AbilityTrigger,System.Action>`](/api/Global.AbilityTrigger) |  |

**Returns:** `SafeAction`

:::

::: details `DoArmorBoost(float)`

ArmorBoost reduces all taken damage.

```csharp
public ArmorBoostEffect DoArmorBoost(float strength)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `strength` | `float` |  |

**Returns:** `ArmorBoostEffect`

:::

::: details `DoArmorReduction(float)`

ArmorReduction increases all taken damage.

```csharp
public ArmorReductionEffect DoArmorReduction(float strength)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `strength` | `float` |  |

**Returns:** `ArmorReductionEffect`

:::

::: details `DoAttackCritical(Action)`

AttackCritical makes the entity's attacks to always do a critical hit.

```csharp
public AttackCriticalEffect DoAttackCritical(Action onUse)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `onUse` | `System.Action` |  |

**Returns:** `AttackCriticalEffect`

:::

::: details `DoAttackEmpower(Action&lt;EventInfoAttackEffect, int&gt;, int, Action)`

Note this will lock the status effect until basic attack instance is destroyed.

```csharp
public AttackEmpowerEffect DoAttackEmpower(Action<EventInfoAttackEffect, int> onAttackEffect, int maxTriggerCount = 2147483647, Action onDepleted = null)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `onAttackEffect` | [`System.Action<T1, T2><EventInfoAttackEffect,int>`](/api/Global.EventInfoAttackEffect) |  |
| `maxTriggerCount` | `int` |  |
| `onDepleted` | `System.Action` |  |

**Returns:** `AttackEmpowerEffect`

:::

::: details `DoAttackOverride(AbilityTrigger, Action)`

AttackOverride replaces the entity's attack AbilityTrigger with something else.This version uses an existing ability trigger.

```csharp
public AttackOverrideEffect DoAttackOverride(AbilityTrigger trigger, Action onUse)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `trigger` | [`AbilityTrigger`](/api/Global.AbilityTrigger) |  |
| `onUse` | `System.Action` |  |

**Returns:** `AttackOverrideEffect`

:::

::: details `DoAttackOverride&lt;T&gt;(Action)`

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

:::

::: details `DoBasicEffect(BasicEffect)`

```csharp
public void DoBasicEffect(BasicEffect eff)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `eff` | [`BasicEffect`](/api/Global.BasicEffect) |  |

:::

::: details `DoBlind()`

Blind makes the entity miss its attacks.

```csharp
public BlindEffect DoBlind()
```

**Returns:** `BlindEffect`

:::

::: details `DoCripple(float)`

Cripple reduces the entity's attack speed.

```csharp
public CrippleEffect DoCripple(float strength)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `strength` | `float` |  |

**Returns:** `CrippleEffect`

:::

::: details `DoDeathInterrupt(Action&lt;EventInfoKill&gt;, int)`

Death Interrupt fires before entity's imminent death.DeathInterrupts with lower priority will be fired/checked earlier.Healing entity by any amount in an interrupt will prevent entity's death.If an interrupt prevents the death, other interrupts will not be fired.Note that interrupts can be ignored byEntity.KillNoInterrupt()

```csharp
public DeathInterruptEffect DoDeathInterrupt(Action<EventInfoKill> onInterrupt, int priority)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `onInterrupt` | [`System.Action<T><EventInfoKill>`](/api/Global.EventInfoKill) |  |
| `priority` | `int` |  |

**Returns:** `DeathInterruptEffect`

:::

::: details `DoFakeMaxHealthEffect(float)`

FakeMaxHealth increases shown max health only in health bars.

```csharp
public FakeMaxHealthEffect DoFakeMaxHealthEffect(float amount)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `amount` | `float` |  |

**Returns:** `FakeMaxHealthEffect`

:::

::: details `DoHaste(float)`

Haste increases the entity's attack speed.

```csharp
public HasteEffect DoHaste(float strength)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `strength` | `float` |  |

**Returns:** `HasteEffect`

:::

::: details `DoInvisible()`

Invisible makes the entity untargetable by targeted abilities and undetectable to enemies. Note this doesn't change the entity's graphical visibility.

```csharp
public InvisibleEffect DoInvisible()
```

**Returns:** `InvisibleEffect`

:::

::: details `DoInvulnerable(Action&lt;EventInfoDamageNegatedByImmunity&gt;)`

Invulnerable makes the entity immune to damage and crowd controls.

```csharp
public InvulnerableEffect DoInvulnerable(Action<EventInfoDamageNegatedByImmunity> onDamageNegated = null)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `onDamageNegated` | [`System.Action<T><EventInfoDamageNegatedByImmunity>`](/api/Global.EventInfoDamageNegatedByImmunity) |  |

**Returns:** `InvulnerableEffect`

:::

::: details `DoProtected(Action&lt;EventInfoDamageNegatedByImmunity&gt;)`

Protected makes the entity immune to damage.

```csharp
public ProtectedEffect DoProtected(Action<EventInfoDamageNegatedByImmunity> onDamageNegated)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `onDamageNegated` | [`System.Action<T><EventInfoDamageNegatedByImmunity>`](/api/Global.EventInfoDamageNegatedByImmunity) |  |

**Returns:** `ProtectedEffect`

:::

::: details `DoRoot()`

Root impairs the entity's movement/movement ability.

```csharp
public RootEffect DoRoot()
```

**Returns:** `RootEffect`

:::

::: details `DoShield(float, Action&lt;EventInfoDamageNegatedByShield&gt;)`

```csharp
public ShieldEffect DoShield(float amount, Action<EventInfoDamageNegatedByShield> onDamageNegated = null)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `amount` | `float` |  |
| `onDamageNegated` | [`System.Action<T><EventInfoDamageNegatedByShield>`](/api/Global.EventInfoDamageNegatedByShield) |  |

**Returns:** `ShieldEffect`

:::

::: details `DoSilence()`

Silence prevents the entity from using abilities.

```csharp
public SilenceEffect DoSilence()
```

**Returns:** `SilenceEffect`

:::

::: details `DoSkill&lt;T&gt;(Action&lt;T&gt;)`

Do custom action on all matching skill. You can invoke the returned action to immediately call cleanup functions to stop the effect.

```csharp
public SafeAction DoSkill<T>(Action<T> callback) where T : SkillTrigger
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `callback` | `System.Action<T>` |  |
| `` | `T` |  |

**Returns:** `SafeAction`

:::

::: details `DoSkill&lt;T&gt;(Func&lt;T, Action&gt;)`

Do custom action on all matching skill and do custom cleanup. You can invoke the returned action to immediately call cleanup functions to stop the effect.

```csharp
public SafeAction DoSkill<T>(Func<T, Action> callback) where T : SkillTrigger
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `callback` | `System.Func<T, TResult><T,System.Action>` |  |
| `` | `T` |  |

**Returns:** `SafeAction`

:::

::: details `DoSlow(float)`

Slow reduces the entity's movement speed.

```csharp
public SlowEffect DoSlow(float strength)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `strength` | `float` |  |

**Returns:** `SlowEffect`

:::

::: details `DoSpeed(float)`

Speed increases the entity's movement speed.

```csharp
public SpeedEffect DoSpeed(float strength)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `strength` | `float` |  |

**Returns:** `SpeedEffect`

:::

::: details `DoStatBonus()`

Do a stat bonus to victim that expires on destruction of this status effect.

```csharp
public StatBonus DoStatBonus()
```

**Returns:** `StatBonus`

:::

::: details `DoStatBonus(StatBonus)`

Do a stat bonus to victim that expires on destruction of this status effect.

```csharp
public StatBonus DoStatBonus(StatBonus bonus)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `bonus` | [`StatBonus`](/api/Global.StatBonus) |  |

**Returns:** `StatBonus`

:::

::: details `DoStun()`

Stun prevents the entity from moving/using abilities/attacking.

```csharp
public StunEffect DoStun()
```

**Returns:** `StunEffect`

:::

::: details `DoUncollidable()`

Uncollidable makes the entity uncollidable by non-targeted projectiles and abilities.

```csharp
public UncollidableEffect DoUncollidable()
```

**Returns:** `UncollidableEffect`

:::

::: details `DoUnstoppable()`

Unstoppable makes the entity immune to crowd controls.

```csharp
public UnstoppableEffect DoUnstoppable()
```

**Returns:** `UnstoppableEffect`

:::

::: details `FrameUpdate()`

```csharp
public override void FrameUpdate()
```

:::

::: details `GetActorReadableName()`

```csharp
public override string GetActorReadableName()
```

**Returns:** `string`

:::

::: details `GetCustomTooltipDescription()`

Called on the local client hovering over the status effect icon.

```csharp
public virtual string GetCustomTooltipDescription()
```

**Returns:** `string`

:::

::: details `GetCustomTooltipName()`

Called on the local client hovering over the status effect icon.

```csharp
public virtual string GetCustomTooltipName()
```

**Returns:** `string`

:::

::: details `HideOnScreenTimer()`

Hide this status effect's timer on the screen of the victim. Has no effect on non-player victim

```csharp
public void HideOnScreenTimer()
```

:::

::: details `OnCreate()`

```csharp
protected override void OnCreate()
```

:::

::: details `OnDestroyActor()`

```csharp
protected override void OnDestroyActor()
```

:::

::: details `OnStartServer()`

```csharp
public override void OnStartServer()
```

:::

::: details `ResetTimer()`

Reset a timer set bySetTimerto its initial duration.

```csharp
public void ResetTimer()
```

:::

::: details `SetTimer(float, float)`

Set a timer that kills this status effect on expiration. The timer will update fillAmount automatically.

```csharp
public void SetTimer(float maxDuration, float duration)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `maxDuration` | `float` |  |
| `duration` | `float` |  |

:::

::: details `SetTimer(float)`

Set a timer that kills this status effect on expiration. The timer will update fillAmount automatically.

```csharp
public void SetTimer(float duration)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `duration` | `float` |  |

:::

::: details `ShowOnScreenTimer(string, Color, bool)`

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

:::

::: details `StopAllBasicEffects()`

```csharp
protected void StopAllBasicEffects()
```

:::

::: details `StopBasicEffect(BasicEffect)`

```csharp
protected void StopBasicEffect(BasicEffect eff)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `eff` | [`BasicEffect`](/api/Global.BasicEffect) |  |

:::

::: details `StopTimer()`

```csharp
public void StopTimer()
```

:::
