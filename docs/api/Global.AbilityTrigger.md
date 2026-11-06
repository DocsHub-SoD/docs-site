# Class: AbilityTrigger

- **Category:** <span class="cat-dot" style="--cat-color: #ef4444" data-cat="Combat & Abilities"></span> Combat & Abilities
- **Namespace:** `Global`
- **Assembly:** `Dew.Core.dll`
- **Attributes:** `[LogicUpdatePriority]`
- **Inheritance / Derived:** [DewNetworkBehaviour](/api/Global.DewNetworkBehaviour) → [Actor](/api/Global.Actor) → [AttackTrigger](/api/Global.AttackTrigger) → [SkillTrigger](/api/Global.SkillTrigger)

```csharp
[LogicUpdatePriority(-300)]
public class AbilityTrigger : Actor, ILogicUpdate, ICleanup, ICustomDestroyRoutine
```

## Fields (14)

::: details Click to expand Fields (14)

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`ClientEvent_OnOwnerChanged`** | `public SafeAction<Entity, Entity> ClientEvent_OnOwnerChanged` |  |
| **`ClientTriggerEvent_OnCooldownReduced`** | `public SafeAction<int, float> ClientTriggerEvent_OnCooldownReduced` | configIndex, reductionAmount. Note the amount is non-discarded variant. e.g. Applying 100 seconds cooldown reduction to a 3 seconds skill will still report 100 seconds reduction. |
| **`ClientTriggerEvent_OnCooldownReducedByRatio`** | `public SafeAction<int, float> ClientTriggerEvent_OnCooldownReducedByRatio` |  |
| **`ClientTriggerEvent_OnCurrentConfigCharged`** | `public SafeAction ClientTriggerEvent_OnCurrentConfigCharged` |  |
| **`ClientTriggerEvent_OnCurrentConfigCooldownReduced`** | `public SafeAction ClientTriggerEvent_OnCurrentConfigCooldownReduced` |  |
| **`configs`** | `[ListDrawerSettings(Expanded = true)] public TriggerConfig[] configs` |  |
| **`currentCharges`** | `[SaveVar] [SaveVar(SaveVarFlags.ApplyAfterFrameDelay)] [NonSerialized] public int[] currentCharges` |  |
| **`currentMinimumDelays`** | `[SaveVar] [SaveVar(SaveVarFlags.ApplyAfterFrameDelay)] [NonSerialized] public float[] currentMinimumDelays` |  |
| **`currentUnscaledCooldownTimes`** | `[SaveVar] [SaveVar(SaveVarFlags.ApplyAfterFrameDelay)] [NonSerialized] public float[] currentUnscaledCooldownTimes` |  |
| **`takenCooldownReductionByRatioProcessor`** | `public DataProcessorGroup<CooldownReductionByRatioSettings, Actor, AbilityTrigger> takenCooldownReductionByRatioProcessor` |  |
| **`takenCooldownReductionProcessor`** | `public DataProcessorGroup<CooldownReductionSettings, Actor, AbilityTrigger> takenCooldownReductionProcessor` |  |
| **`TriggerEvent_OnCastComplete`** | `public Action<EventInfoCast> TriggerEvent_OnCastComplete` |  |
| **`TriggerEvent_OnCastCompleteBeforePrepare`** | `public Action<EventInfoCast> TriggerEvent_OnCastCompleteBeforePrepare` |  |
| **`TriggerEvent_OnCastStart`** | `public Action<EventInfoCast> TriggerEvent_OnCastStart` |  |

:::

## Properties (15)

::: details Click to expand Properties (15)

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`abilityIndex`** | `public int abilityIndex { get; }` | Ability index of this trigger if equipped to an entity. |
| **`currentConfig`** | `public TriggerConfig currentConfig { get; }` |  |
| **`currentConfigChangeHandle`** | `public AbilityTrigger.ChangedConfigHandle currentConfigChangeHandle { get; }` |  |
| **`currentConfigCooldownTime`** | `public float currentConfigCooldownTime { get; }` |  |
| **`currentConfigCurrentCharge`** | `public int currentConfigCurrentCharge { get; }` |  |
| **`currentConfigCurrentMinimumDelay`** | `public float currentConfigCurrentMinimumDelay { get; }` |  |
| **`currentConfigIndex`** | `public int currentConfigIndex { get; set; }` |  |
| **`currentConfigMaxCooldownTime`** | `public float currentConfigMaxCooldownTime { get; }` |  |
| **`currentConfigUnscaledCooldownTime`** | `public float currentConfigUnscaledCooldownTime { get; }` |  |
| **`currentConfigUnscaledMaxCooldownTime`** | `public float currentConfigUnscaledMaxCooldownTime { get; }` |  |
| **`currentPassiveEffect`** | `public StatusEffect currentPassiveEffect { get; }` |  |
| **`fillAmount`** | `public float fillAmount { get; set; }` |  |
| **`ignoreRangeCheck`** | `public bool ignoreRangeCheck { get; set; }` |  |
| **`isDestroyedOnRoomChange`** | `public override bool isDestroyedOnRoomChange { get; }` |  |
| **`owner`** | `public Entity owner { get; set; }` |  |

:::

## Methods (61)

::: details `Awake()`

```csharp
protected override void Awake()
```

:::

::: details `CanBeCast()`

Can this ability be cast? By default this checks charges/delay/mana cost/self validator/self applied status effects.This must return same value for everyone to ensure consistency.

```csharp
public virtual bool CanBeCast()
```

**Returns:** `bool`

:::

::: details `CanBeReserved()`

Can this ability be reserved? By default this checks everything that CanBeCast() checks but self validators.This must return same value for everyone to ensure consistency.

```csharp
public virtual bool CanBeReserved()
```

**Returns:** `bool`

:::

::: details `ChangeConfigTimed(int, float, Action&lt;EventInfoAbilityInstance&gt;, Action, bool)`

```csharp
public AbilityTrigger.ChangedConfigHandle ChangeConfigTimed(int index, float duration, Action<EventInfoAbilityInstance> onUse = null, Action onExpire = null, bool setFillAmount = true)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `index` | `int` |  |
| `duration` | `float` |  |
| `onUse` | [`System.Action<T><EventInfoAbilityInstance>`](/api/Global.EventInfoAbilityInstance) |  |
| `onExpire` | `System.Action` |  |
| `setFillAmount` | `bool` |  |

**Returns:** `AbilityTrigger.ChangedConfigHandle`

:::

::: details `ChangeConfigTimedOnce(int, float, Action&lt;EventInfoAbilityInstance&gt;, Action, bool)`

```csharp
public AbilityTrigger.ChangedConfigHandle ChangeConfigTimedOnce(int index, float duration, Action<EventInfoAbilityInstance> onUse = null, Action onExpire = null, bool setFillAmount = true)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `index` | `int` |  |
| `duration` | `float` |  |
| `onUse` | [`System.Action<T><EventInfoAbilityInstance>`](/api/Global.EventInfoAbilityInstance) |  |
| `onExpire` | `System.Action` |  |
| `setFillAmount` | `bool` |  |

**Returns:** `AbilityTrigger.ChangedConfigHandle`

:::

::: details `GetActorReadableName()`

```csharp
public override string GetActorReadableName()
```

**Returns:** `string`

:::

::: details `GetAnimationSpeed()`

```csharp
public virtual float GetAnimationSpeed()
```

**Returns:** `float`

:::

::: details `GetCastInfoToTarget(Entity)`

```csharp
public CastInfo GetCastInfoToTarget(Entity target)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `target` | [`Entity`](/api/Global.Entity) |  |

**Returns:** `CastInfo`

:::

::: details `GetChannelDurationMultiplier()`

```csharp
public virtual float GetChannelDurationMultiplier()
```

**Returns:** `float`

:::

::: details `GetCooldownTimeMultiplier(int)`

```csharp
public virtual float GetCooldownTimeMultiplier(int configIndex)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `configIndex` | `int` |  |

**Returns:** `float`

:::

::: details `GetCooldownTimeMultiplierByAbilityHaste(float)`

```csharp
public static float GetCooldownTimeMultiplierByAbilityHaste(float abilityHaste)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `abilityHaste` | `float` |  |

**Returns:** `float`

:::

::: details `GetCooldownTimeOffset(int)`

```csharp
public virtual float GetCooldownTimeOffset(int configIndex)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `configIndex` | `int` |  |

**Returns:** `float`

:::

::: details `GetInstanceSpawnPosition(int, CastInfo)`

```csharp
protected virtual Vector3 GetInstanceSpawnPosition(int configIndex, CastInfo info)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `configIndex` | `int` |  |
| `info` | [`CastInfo`](/api/Global.CastInfo) |  |

**Returns:** `UnityEngine.Vector3`

:::

::: details `GetInstanceSpawnRotation(int, CastInfo)`

```csharp
protected virtual Quaternion? GetInstanceSpawnRotation(int configIndex, CastInfo info)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `configIndex` | `int` |  |
| `info` | [`CastInfo`](/api/Global.CastInfo) |  |

**Returns:** `UnityEngine.Quaternion?`

:::

::: details `GetMaxCooldownTime(int, bool)`

```csharp
public float GetMaxCooldownTime(int configIndex, bool scaled = true)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `configIndex` | `int` |  |
| `scaled` | `bool` |  |

**Returns:** `float`

:::

::: details `GetPostDelayDurationMultiplier()`

```csharp
public virtual float GetPostDelayDurationMultiplier()
```

**Returns:** `float`

:::

::: details `GetPredictedCastInfoToTarget(Entity, float)`

```csharp
public CastInfo GetPredictedCastInfoToTarget(Entity target, float strength)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `target` | [`Entity`](/api/Global.Entity) |  |
| `strength` | `float` |  |

**Returns:** `CastInfo`

:::

::: details `GetPredictedCastInfoToTarget(Entity)`

```csharp
public CastInfo GetPredictedCastInfoToTarget(Entity target)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `target` | [`Entity`](/api/Global.Entity) |  |

**Returns:** `CastInfo`

:::

::: details `IsConfigLocked(int)`

```csharp
public bool IsConfigLocked(int configIndex)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `configIndex` | `int` |  |

**Returns:** `bool`

:::

::: details `IsTargetInRange(Entity)`

```csharp
public bool IsTargetInRange(Entity target)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `target` | [`Entity`](/api/Global.Entity) |  |

**Returns:** `bool`

:::

::: details `LockCooldown(int)`

```csharp
public void LockCooldown(int configIndex)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `configIndex` | `int` |  |

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

::: details `OnCastCancel(int, CastInfo)`

Called on server when this ability's cast channel is canceled.By default, this sets the cooldown time to 1 second if its smaller than 1 second.

```csharp
protected virtual void OnCastCancel(int configIndex, CastInfo info)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `configIndex` | `int` |  |
| `info` | [`CastInfo`](/api/Global.CastInfo) |  |

:::

::: details `OnCastCancelSetCooldownTime(int, CastInfo)`

```csharp
protected virtual void OnCastCancelSetCooldownTime(int configIndex, CastInfo info)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `configIndex` | `int` |  |
| `info` | [`CastInfo`](/api/Global.CastInfo) |  |

:::

::: details `OnCastComplete(int, CastInfo)`

Called on server when this ability's cast channel is completed.By default, this spends mana and ability charge, sets the appropriate cooldown time, delay, and creates the configured ability instance using the owner's position and rotation.If the config is direction-type, the rotation will be based off of the cast direction.

```csharp
public virtual AbilityInstance OnCastComplete(int configIndex, CastInfo info)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `configIndex` | `int` |  |
| `info` | [`CastInfo`](/api/Global.CastInfo) |  |

**Returns:** `AbilityInstance`

:::

::: details `OnCastCompleteBeforePrepare(EventInfoCast)`

```csharp
public virtual void OnCastCompleteBeforePrepare(EventInfoCast cast)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `cast` | [`EventInfoCast`](/api/Global.EventInfoCast) |  |

:::

::: details `OnCastCompleteSetCharge(int, CastInfo)`

```csharp
public virtual void OnCastCompleteSetCharge(int configIndex, CastInfo info)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `configIndex` | `int` |  |
| `info` | [`CastInfo`](/api/Global.CastInfo) |  |

:::

::: details `OnCastCompleteSetCooldownTime(int, CastInfo)`

```csharp
public virtual void OnCastCompleteSetCooldownTime(int configIndex, CastInfo info)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `configIndex` | `int` |  |
| `info` | [`CastInfo`](/api/Global.CastInfo) |  |

:::

::: details `OnCastCompleteSetMinimumDelay(int, CastInfo)`

```csharp
public virtual void OnCastCompleteSetMinimumDelay(int configIndex, CastInfo info)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `configIndex` | `int` |  |
| `info` | [`CastInfo`](/api/Global.CastInfo) |  |

:::

::: details `OnCastCompleteSpendMana(int, CastInfo)`

```csharp
public virtual void OnCastCompleteSpendMana(int configIndex, CastInfo info)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `configIndex` | `int` |  |
| `info` | [`CastInfo`](/api/Global.CastInfo) |  |

:::

::: details `OnCastStart(int, CastInfo)`

Called on server when this ability is cast.By default, this plays the animation and starts the configured channel.IffaceForwardis set to true, it will cause the owner to rotate towards the target/point/direction/cursor position.Target validation will be done on the channel if the cast method is set to Target.

```csharp
public virtual void OnCastStart(int configIndex, CastInfo info)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `configIndex` | `int` |  |
| `info` | [`CastInfo`](/api/Global.CastInfo) |  |

:::

::: details `OnConfigChanged(int, int)`

Called everywhere when current config index is changed or set initial value.

```csharp
protected virtual void OnConfigChanged(int oldIndex, int newIndex)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `oldIndex` | `int` |  |
| `newIndex` | `int` |  |

:::

::: details `OnCreate()`

```csharp
protected override void OnCreate()
```

:::

::: details `OnDeserialize(NetworkReader, bool)`

```csharp
public override void OnDeserialize(NetworkReader reader, bool initialState)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `reader` | `Mirror.NetworkReader` |  |
| `initialState` | `bool` |  |

:::

::: details `OnEquip(Entity)`

Called on everyone when the trigger is being equipped.

```csharp
protected virtual void OnEquip(Entity newOwner)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `newOwner` | [`Entity`](/api/Global.Entity) |  |

:::

::: details `OnRotateForward(int, CastInfo)`

```csharp
protected virtual void OnRotateForward(int configIndex, CastInfo info)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `configIndex` | `int` |  |
| `info` | [`CastInfo`](/api/Global.CastInfo) |  |

:::

::: details `OnSerialize(NetworkWriter, bool)`

```csharp
public override void OnSerialize(NetworkWriter writer, bool initialState)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `writer` | `Mirror.NetworkWriter` |  |
| `initialState` | `bool` |  |

:::

::: details `OnStartChannel(int, CastInfo)`

```csharp
protected virtual void OnStartChannel(int configIndex, CastInfo info)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `configIndex` | `int` |  |
| `info` | [`CastInfo`](/api/Global.CastInfo) |  |

:::

::: details `OnStartServer()`

```csharp
public override void OnStartServer()
```

:::

::: details `OnStopServer()`

```csharp
public override void OnStopServer()
```

:::

::: details `OnUnequip(Entity)`

Called on everyone when the trigger is being unequipped.

```csharp
protected virtual void OnUnequip(Entity formerOwner)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `formerOwner` | [`Entity`](/api/Global.Entity) |  |

:::

::: details `PredictAngle_Simple(float, Entity, Vector3, float)`

```csharp
public static float PredictAngle_Simple(float strength, Entity target, Vector3 startPos, float delay)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `strength` | `float` |  |
| `target` | [`Entity`](/api/Global.Entity) |  |
| `startPos` | `UnityEngine.Vector3` |  |
| `delay` | `float` |  |

**Returns:** `float`

:::

::: details `PredictAngle_SpeedAcceleration(float, Entity, Vector3, float, float, float, float, float)`

```csharp
public static float PredictAngle_SpeedAcceleration(float strength, Entity target, Vector3 startPos, float delay, float frontDistance, float initSpeed, float targetSpeed, float acceleration)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `strength` | `float` |  |
| `target` | [`Entity`](/api/Global.Entity) |  |
| `startPos` | `UnityEngine.Vector3` |  |
| `delay` | `float` |  |
| `frontDistance` | `float` |  |
| `initSpeed` | `float` |  |
| `targetSpeed` | `float` |  |
| `acceleration` | `float` |  |

**Returns:** `float`

:::

::: details `PredictPoint_Simple(float, Entity, float)`

```csharp
public static Vector3 PredictPoint_Simple(float strength, Entity target, float delay)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `strength` | `float` |  |
| `target` | [`Entity`](/api/Global.Entity) |  |
| `delay` | `float` |  |

**Returns:** `UnityEngine.Vector3`

:::

::: details `PredictPoint_SpeedAcceleration(float, Entity, Vector3, float, float, float, float, float)`

```csharp
public static Vector3 PredictPoint_SpeedAcceleration(float strength, Entity target, Vector3 startPos, float delay, float frontDistance, float initSpeed, float targetSpeed, float acceleration)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `strength` | `float` |  |
| `target` | [`Entity`](/api/Global.Entity) |  |
| `startPos` | `UnityEngine.Vector3` |  |
| `delay` | `float` |  |
| `frontDistance` | `float` |  |
| `initSpeed` | `float` |  |
| `targetSpeed` | `float` |  |
| `acceleration` | `float` |  |

**Returns:** `UnityEngine.Vector3`

:::

::: details `PredictPointClamped_Simple(float, Entity, Vector3, float, float)`

```csharp
public static Vector3 PredictPointClamped_Simple(float strength, Entity target, Vector3 startPos, float range, float delay)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `strength` | `float` |  |
| `target` | [`Entity`](/api/Global.Entity) |  |
| `startPos` | `UnityEngine.Vector3` |  |
| `range` | `float` |  |
| `delay` | `float` |  |

**Returns:** `UnityEngine.Vector3`

:::

::: details `PredictPointClamped_SpeedAcceleration(float, Entity, Vector3, float, float, float, float, float, float)`

```csharp
public static Vector3 PredictPointClamped_SpeedAcceleration(float strength, Entity target, Vector3 startPos, float range, float delay, float frontDistance, float initSpeed, float targetSpeed, float acceleration)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `strength` | `float` |  |
| `target` | [`Entity`](/api/Global.Entity) |  |
| `startPos` | `UnityEngine.Vector3` |  |
| `range` | `float` |  |
| `delay` | `float` |  |
| `frontDistance` | `float` |  |
| `initSpeed` | `float` |  |
| `targetSpeed` | `float` |  |
| `acceleration` | `float` |  |

**Returns:** `UnityEngine.Vector3`

:::

::: details `PredictTime_SpeedAcceleration(Entity, Vector3, float, float, float, float, float)`

```csharp
public static float PredictTime_SpeedAcceleration(Entity target, Vector3 startPos, float delay, float frontDistance, float initSpeed, float targetSpeed, float acceleration)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `target` | [`Entity`](/api/Global.Entity) |  |
| `startPos` | `UnityEngine.Vector3` |  |
| `delay` | `float` |  |
| `frontDistance` | `float` |  |
| `initSpeed` | `float` |  |
| `targetSpeed` | `float` |  |
| `acceleration` | `float` |  |

**Returns:** `float`

:::

::: details `ProcessRange(float)`

```csharp
public virtual float ProcessRange(float original)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `original` | `float` |  |

**Returns:** `float`

:::

::: details `ProcessReceivedCooldownReduction(ref CooldownReductionSettings, Actor)`

```csharp
public void ProcessReceivedCooldownReduction(ref CooldownReductionSettings data, Actor actor)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `data` | [`CooldownReductionSettings`](/api/Global.CooldownReductionSettings) |  |
| `actor` | [`Actor`](/api/Global.Actor) |  |

:::

::: details `ProcessReceivedCooldownReductionByRatio(ref CooldownReductionByRatioSettings, Actor)`

```csharp
public void ProcessReceivedCooldownReductionByRatio(ref CooldownReductionByRatioSettings data, Actor actor)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `data` | [`CooldownReductionByRatioSettings`](/api/Global.CooldownReductionByRatioSettings) |  |
| `actor` | [`Actor`](/api/Global.Actor) |  |

:::

::: details `SetCharge(int, int)`

```csharp
public void SetCharge(int configIndex, int charge)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `configIndex` | `int` |  |
| `charge` | `int` |  |

:::

::: details `SetChargeAll(int)`

```csharp
public void SetChargeAll(int charge)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `charge` | `int` |  |

:::

::: details `SetCooldownTime(int, float, bool)`

```csharp
public void SetCooldownTime(int configIndex, float time, bool scaled = true)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `configIndex` | `int` |  |
| `time` | `float` |  |
| `scaled` | `bool` |  |

:::

::: details `SetCooldownTimeAll(float, bool)`

```csharp
public void SetCooldownTimeAll(float time, bool scaled = true)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `time` | `float` |  |
| `scaled` | `bool` |  |

:::

::: details `SetMinimumDelay(int, float)`

```csharp
public void SetMinimumDelay(int configIndex, float delay)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `configIndex` | `int` |  |
| `delay` | `float` |  |

:::

::: details `SetMinimumDelayAll(float)`

```csharp
public void SetMinimumDelayAll(float delay)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `delay` | `float` |  |

:::

::: details `ShouldTickCooldown(int)`

If false, this trigger will not tick cooldowns by itself nor replenish charges.
Delays will tick as usual.
This should return same values in server and clients for consistent behavior.

```csharp
protected virtual bool ShouldTickCooldown(int configIndex)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `configIndex` | `int` |  |

**Returns:** `bool`

:::

::: details `SyncCastMethodChanges(int)`

```csharp
public void SyncCastMethodChanges(int configIndex)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `configIndex` | `int` |  |

:::

::: details `UndoChangeConfig()`

```csharp
public void UndoChangeConfig()
```

:::

::: details `UnlockCooldown(int)`

```csharp
public void UnlockCooldown(int configIndex)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `configIndex` | `int` |  |

:::


## Architecture & Relationships

::: details Click to expand Architecture & Relationships

### Used By (324)

*Classes and systems that invoke, reference, or depend on `AbilityTrigger`:*

[AbilityInstance](/api/Global.AbilityInstance) · [ActionAttackMove](/api/Global.ActionAttackMove) · [ActionCast](/api/Global.ActionCast) · [Actor](/api/Global.Actor) · `Ai_C_BeamOfLight` · `Ai_D_ScarOfTheWind_DashAtk` · `Ai_E_FlameJet` · `Ai_L_MentalCorruption_Projectile` · `Ai_Mon_Despair_BossAzurak_StompBlock` · `Ai_Mon_Despair_Displacer_Blink` · `Ai_Mon_Forest_BossDemon_AltSkill_Stomp` · `Ai_Mon_Ink_BossDarkMoon_Blade` · `Ai_Mon_Ink_BossDarkMoon_ShortDash` · `Ai_Mon_Ink_BossWhiteNight_AltAtk_Ready` · `Ai_Mon_Ink_BossWhiteNight_Oppression` · `Ai_Mon_Primus_BossPrimusAeron_Adapt_Arbalest` · `Ai_Mon_Sky_BossNyx_Atk` · `Ai_Mon_SnowMountain_BossSkoll_Atk` · `Ai_Mon_SnowMountain_VikingWarrior_Atk` · `Ai_Mon_Special_BossErebos_SpawnTormentor_Attacker` · `Ai_Mon_Special_BossMaw_PrecisionShot` · `Ai_Mon_Special_BossMaw_SliceThroat` · `Ai_Mon_Special_BossMaw_SliceThroat_Atk` · `Ai_Mon_Special_BossPolaris_Holy_Purgatory_Spawner` · `Ai_Mon_Special_BossPolaris_Monster_Atk_Spawner` · `Ai_Q_EtherealInfluence` · `Ai_Q_SuperNova` · `Ai_R_SanctuaryOfEl_Ground` · `At_Atk_HuskSword` · `At_Atk_LacertaRifle` · `At_Atk_YubarStardust` · `At_Mon_DarkCave_BossSeeker_Blink` · `At_Mon_DarkCave_BossSeeker_BlinkBarrage` · `At_Mon_DarkCave_BossSeeker_GreenChaserOrb` · `At_Mon_DarkCave_BossSeeker_Hallucination` · `At_Mon_DarkCave_BossSeeker_PurpleOrb` · `At_Mon_DarkCave_BossSeeker_RedFissure` · `At_Mon_DarkCave_BossSeeker_Substitution` · `At_Mon_DarkCave_BossSeeker_TunnelVision` · `At_Mon_DarkCave_BossSeeker_YellowDiagram` · `At_Mon_DarkCave_CaveBat_Dash` · `At_Mon_DarkCave_DarkElemental_Barrage` · `At_Mon_DarkCave_DarkElemental_Teleport` · `At_Mon_DarkCave_Oppressor_Hypnotize` · `At_Mon_Despair_BossAzurak_DoubleStomp` · `At_Mon_Despair_BossAzurak_RoarAtk` · `At_Mon_Despair_BossAzurak_Roll` · `At_Mon_Despair_BossAzurak_SpawnMonsters` · `At_Mon_Despair_BossAzurak_StompBlock` · `At_Mon_Despair_BossAzurak_StompGlobal` · `At_Mon_Despair_BossAzurak_StompProjectile` · `At_Mon_Despair_BossAzurak_StompTargetArea` · `At_Mon_Despair_BossAzurak_SummonDisplacers` · `At_Mon_Despair_Displacer_Blink` · `At_Mon_Despair_Displacer_Dash` · `At_Mon_Despair_Displacer_SpawnEgg` · `At_Mon_Despair_DreadBug_Jump` · `At_Mon_Despair_DreadBug_JumpBack` · `At_Mon_Despair_ParalyticFly_Atk` · `At_Mon_Despair_ParalyticFly_Melee` · `At_Mon_Despair_ParalyticFly_Paralyze` · `At_Mon_Despair_WretchedArtillery_Melee` · `At_Mon_Forest_BossDemon_AltSkill` · `At_Mon_Forest_BossDemon_Blink` · `At_Mon_Forest_BossDemon_DelayedAtk` · `At_Mon_Forest_BossDemon_MainSkill` · `At_Mon_Forest_BossDemon_Spawn` · `At_Mon_Forest_BossDemon_SpecialAtk` · `At_Mon_Forest_Hound_Charge` · `At_Mon_Forest_SpiderSpitter_Atk` · `At_Mon_Forest_SpiderSpitter_Backdash` · `At_Mon_Forest_SpiderSpitter_Melee` · `At_Mon_Forest_SpiderWarrior_Jump` · `At_Mon_Forest_Treant_PowerBomb` · `At_Mon_Forest_Treant_Rage` · `At_Mon_Ink_Archer_Dodge` · `At_Mon_Ink_BossDarkMoon_Eclipse` · `At_Mon_Ink_BossDarkMoon_SpawnEgoSword` · `At_Mon_Ink_BossDarkMoon_Spear` · `At_Mon_Ink_BossDarkMoon_TeleportAtk` · `At_Mon_Ink_BossDarkMoon_TeleportDash` · `At_Mon_Ink_BossDarkMoon_ThrowSpear` · `At_Mon_Ink_BossWhiteNight_BuddhasPalm` · `At_Mon_Ink_BossWhiteNight_Cataclysm` · `At_Mon_Ink_BossWhiteNight_DestructionWave` · `At_Mon_Ink_BossWhiteNight_EnergyWave` · `At_Mon_Ink_BossWhiteNight_OneInchPunch` · `At_Mon_Ink_BossWhiteNight_Oppression` · `At_Mon_Ink_BossWhiteNight_Rage` · `At_Mon_Ink_BossWhiteNight_RageInstance_RockSpawner` · `At_Mon_Ink_BossWhiteNight_Rush` · `At_Mon_Ink_DivineAnimal_Bite` · `At_Mon_Ink_DivineAnimal_Missile` · `At_Mon_Ink_EgoSword_Atk` · `At_Mon_Ink_GhostBlade_DemolitionMan` · `At_Mon_Ink_GhostBlade_SwiftStep` · `At_Mon_Ink_GhostSpear_Dash` · `At_Mon_Ink_Tiger_DashAtk` · `At_Mon_Ink_Tiger_ShadowWalk` · `At_Mon_Ink_Tiger_Walk` · `At_Mon_LavaLand_BossInfernus_BreathFire` · `At_Mon_LavaLand_BossInfernus_Dash` · `At_Mon_LavaLand_BossInfernus_InvulShield` · `At_Mon_LavaLand_BossInfernus_Jump` · `At_Mon_LavaLand_BossInfernus_PowerBomb` · `At_Mon_LavaLand_BossInfernus_Stomp` · `At_Mon_LavaLand_BossInfernus_Swipe` · `At_Mon_LavaLand_FireElemental_BackDash` · `At_Mon_LavaLand_FireElemental_Destruct` · `At_Mon_LavaLand_FireElemental_Explosion` · `At_Mon_LavaLand_InfernoSpider_LavaAtk` · `At_Mon_LavaLand_Magmadon_Charge` · `At_Mon_LavaLand_SuperheatedWolf_SelfDestruct` · `At_Mon_Polaris_Smite` · `At_Mon_Primus_BossPrimusAeron_Adapt_Arbalest` · `At_Mon_Primus_BossPrimusAeron_Adapt_Doom` · `At_Mon_Primus_BossPrimusAeron_Adapt_IceBlock` · `At_Mon_Primus_BossPrimusAeron_Adapt_IceClaw` · `At_Mon_Primus_BossPrimusAeron_Adapt_SmiteStorm` · `At_Mon_Primus_BossPrimusAeron_Adapt_Starfall` · `At_Mon_Primus_BossPrimusAeron_Dash` · `At_Mon_Primus_BossPrimusAeron_Force_GoldRain` · `At_Mon_Primus_BossPrimusAeron_Force_Grab` · `At_Mon_Primus_BossPrimusAeron_Force_JumpAttack` · `At_Mon_Primus_BossPrimusAeron_Rage_DashAttack` · `At_Mon_Primus_BossPrimusAeron_Rage_MassDelusion` · `At_Mon_Primus_BossPrimusAeron_Rage_MassSilence` · `At_Mon_Primus_BossPrimusAeron_Rage_Whirlwind` · `At_Mon_Sky_Baam_Teleport` · `At_Mon_Sky_BigBaam_Main_Buff` · `At_Mon_Sky_BigBaam_Main_Root` · `At_Mon_Sky_BossNyx_AltTeleport` · `At_Mon_Sky_BossNyx_Blackhole` · `At_Mon_Sky_BossNyx_CreateSeeds` · `At_Mon_Sky_BossNyx_LineAtk` · `At_Mon_Sky_BossNyx_PullAtk` · `At_Mon_Sky_BossNyx_StarBuff` · `At_Mon_Sky_BossNyx_Starfall` · `At_Mon_Sky_BossNyx_StellarDash` · `At_Mon_Sky_BossNyx_Swipe` · `At_Mon_Sky_BossNyx_Teleport` · `At_Mon_Sky_LittleBaam_Reposition` · `At_Mon_Sky_StarSeed_Atk` · `At_Mon_Sky_StarSeed_SelfDestruct` · `At_Mon_Sky_StellaMatter_Dash` · `At_Mon_Sky_StellaMatter_Melee` · `At_Mon_Sky_StellaMatter_Throw` · `At_Mon_SnowMountain_BossSkoll_AuraBlade` · `At_Mon_SnowMountain_BossSkoll_AuraBladeRain` · `At_Mon_SnowMountain_BossSkoll_AuraExplosion` · `At_Mon_SnowMountain_BossSkoll_AuraSlice` · `At_Mon_SnowMountain_BossSkoll_Capture` · `At_Mon_SnowMountain_BossSkoll_DeathFromAbove` · `At_Mon_SnowMountain_BossSkoll_SummonArrow` · `At_Mon_SnowMountain_BossSkoll_SummonSword` · `At_Mon_SnowMountain_BossSkoll_Swipe` · `At_Mon_SnowMountain_BossSkoll_Whirlwind` · `At_Mon_SnowMountain_IceElemental_DoubleSwipe` · `At_Mon_SnowMountain_IceElemental_IceBreaker` · `At_Mon_SnowMountain_Scavenger_Jump` · `At_Mon_SnowMountain_Scavenger_Throw` · `At_Mon_SnowMountain_SnowWolf_Pounce` · `At_Mon_SnowMountain_SnowWolf_SlowApproach` · `At_Mon_SnowMountain_VikingWarrior_SpawnSword` · `At_Mon_SnowMountain_VikingWarrior_ThrowShield` · `At_Mon_Special_AmbushSpawner_Spawn` · `At_Mon_Special_BossErebos_AntiGravity` · `At_Mon_Special_BossErebos_Gaze` · `At_Mon_Special_BossErebos_Meteor` · `At_Mon_Special_BossErebos_Ripple` · `At_Mon_Special_BossErebos_SpawnBlackhole` · `At_Mon_Special_BossErebos_SpawnTormentor` · `At_Mon_Special_BossErebos_StarRain` · `At_Mon_Special_BossErebos_Teleport` · `At_Mon_Special_BossLightElemental_BeamBarrage` · `At_Mon_Special_BossLightElemental_Lightning` · `At_Mon_Special_BossLightElemental_Summon` · `At_Mon_Special_BossMaw_AnnihilationStance` · `At_Mon_Special_BossMaw_Catacylsm` · `At_Mon_Special_BossMaw_ChainReaction` · `At_Mon_Special_BossMaw_Chomp` · `At_Mon_Special_BossMaw_DarkSpear` · `At_Mon_Special_BossMaw_MoonlightPact` · `At_Mon_Special_BossMaw_PillarOfFlame` · `At_Mon_Special_BossMaw_PrecisionShot` · `At_Mon_Special_BossMaw_Purgatory` · `At_Mon_Special_BossMaw_ScatterShot` · `At_Mon_Special_BossMaw_ShadowOverdrive` · `At_Mon_Special_BossMaw_ShadowWalk` · `At_Mon_Special_BossMaw_SliceThroat` · `At_Mon_Special_BossObliviax_Artillery` · `At_Mon_Special_BossObliviax_BackStep` · `At_Mon_Special_BossObliviax_ChargeSequence` · `At_Mon_Special_BossObliviax_DashAtk` · `At_Mon_Special_BossObliviax_Laugh` · `At_Mon_Special_BossObliviax_NeedleAtk` · `At_Mon_Special_BossObliviax_ShadowWalk` · `At_Mon_Special_BossObliviax_TurnAtk` · `At_Mon_Special_BossObliviax_TurretMode` · `At_Mon_Special_BossPolaris_Holy_Beam` · `At_Mon_Special_BossPolaris_Holy_CounterSpell` · `At_Mon_Special_BossPolaris_Holy_Dash` · `At_Mon_Special_BossPolaris_Holy_GoldenSpear` · `At_Mon_Special_BossPolaris_Holy_Purgatory` · `At_Mon_Special_BossPolaris_Holy_RainFire` · `At_Mon_Special_BossPolaris_Holy_ScatterFire` · `At_Mon_Special_BossPolaris_Holy_SelfCleanse` · `At_Mon_Special_BossPolaris_Holy_ShortInvul` · `At_Mon_Special_BossPolaris_Holy_Summon` · `At_Mon_Special_BossPolaris_Monster_CircularSwipe` · `At_Mon_Special_BossPolaris_Monster_CursedDive` · `At_Mon_Special_BossPolaris_Monster_Dash` · `At_Mon_Special_BossPolaris_Monster_JumpStomp` · `At_Mon_Special_BossPolaris_Monster_PizzaLightning` · `At_Mon_Special_BossPolaris_Monster_Scream` · `At_Mon_Special_BossPolaris_Monster_SlashDash` · `At_Mon_Special_BossPolaris_Monster_Smite` · `At_MorasDomain_MorasCreation_Boss_Move` · `At_MorasDomain_MorasCreation_Boss_SpawnSwarm` · `At_Prop_Merchant_Flee` · [AttackOverrideEffect](/api/Global.AttackOverrideEffect) · [AttackProjectile](/api/Global.AttackProjectile) · [AttackTrigger](/api/Global.AttackTrigger) · [CastIndicatorManager](/api/Global.CastIndicatorManager) · [CastMethodData](/api/Global.CastMethodData) · [ChargingChannel](/api/Global.ChargingChannel) · [ControlManager](/api/Global.ControlManager) · [EntityAI](/api/Global.EntityAI) · [EntityAbility](/api/Global.EntityAbility) · [EntityControl](/api/Global.EntityControl) · [EntityStatus](/api/Global.EntityStatus) · [EventInfoCast](/api/Global.EventInfoCast) · `Gem_L_ChaosApple` · `Gem_L_Paranoia` · `Hero_Bismuth` · `LucidDream_PrudentJellyfish` · [MeleeAttackInstance](/api/Global.MeleeAttackInstance) · `Mon_Despair_DreadBug` · `Mon_Forest_BossDemon` · `Mon_Ink_BossDarkMoon` · `Mon_Primus_BossPrimusAeron` · `Mon_Special_BossObliviax` · [PingManager](/api/Global.PingManager) · `RoomMod_RiskOfMeteors` · [SampleCastInfoContext](/api/Global.SampleCastInfoContext) · `Se_Curse_DreamAfflictionInductive` · `Se_D_AstridsMasterpiecePriorite` · `Se_D_BeautifulThreat` · `Se_D_BurningFist_EmpowerAttack` · `Se_D_ChargedAnguillian` · `Se_D_ConvergencePoint` · `Se_D_DoubleTap` · `Se_D_ExoticMatter` · `Se_D_FrostTouch_EmpowerAttacks` · `Se_D_IceColdPresence` · `Se_D_PrismaticEyes` · `Se_D_ScarOfTheWind_NextAtkCrit` · `Se_D_TheKillingFlow_Crit` · `Se_GravityTraining` · `Se_HunterBuff` · `Se_L_PyranasFireball` · `Se_MiniBoss_IceAura` · `Se_MiniBoss_OrbSpitter` · `Se_MirageSkin_Delusion` · `Se_MirageSkin_Oblivion` · `Se_MirageSkin_Pulverization` · `Se_Mon_SnowMountain_SnowWolf_SlowApproach` · `Se_MorasDomain_MorasCreation_Boss` · `Se_Nor_ReptilianThirdEye` · `Se_Q_GoldenBurst_Wither` · `Se_R_AnnihilationStance` · `Se_R_Cataclysm` · `Se_R_FrozenFists` · `Se_R_Somersault_CritBonus` · `Se_R_UnbreakableDetermination` · `Se_Star_Lacerta_D_AttackRange` · `Se_Star_Mist_F_LG_ChainAttack` · `Se_Star_Mist_F_LG_RangeAndSpeed` · `Se_Star_Vesper_F_DP_FarTargetBonus` · `Se_Star_Vesper_F_DP_SwitchToMelee` · `Se_Star_Yubar_L_DodgeCooldownWithShorterRange` · `Se_Star_Yubar_L_DodgeRange` · `Se_U_Burrow` · [SkillTrigger](/api/Global.SkillTrigger) · `St_C_Sneeze` · `St_C_Starfall` · `St_D_HeartOfThePack` · `St_D_IceColdPresence` · `St_D_MercyOfEl` · `St_D_QuartetOfDeath` · `St_D_Resolve` · `St_D_SalamanderPowder` · `St_E_ClutchesOfMalice` · `St_E_Harvest` · `St_E_Rewind` · `St_L_ButchersStrike` · `St_L_CoinExplosion` · `St_L_HerosReturn` · `St_L_SmallMoltenCore` · `St_QR_InfernalTales` · `St_QR_ValiantHeart` · `St_Q_DeathMark` · `St_Q_Fleche` · `St_Q_GoldenBurst` · `St_Q_Laceration` · `St_Q_MoonlightPact` · `St_Q_Reduction` · `St_R_DangerousTheory` · `St_U_ShoutOfOblivion` · `Star_Lacerta_AttackRange` · `Star_Mist_LongerLunge` · `Star_Yubar_IncreaseFlickerRange` · [StatusEffect](/api/Global.StatusEffect) · `Sum_Q_SylvanCall_LeafHound` · [Summon](/api/Global.Summon) · [TriggerConfig](/api/Global.TriggerConfig) · `UI_Dev_ConsoleSelectedEntityInfo` · `UI_InGame_CooldownTimeNotification` · `UI_InGame_MovementSkillIndicator` · `UI_InGame_SkillButton` · `UI_Tooltip_SkillCooldown` · `UI_Tooltip_SkillDescription` · `UI_Tooltip_SkillMaxCharges` · `UI_Tooltip_SkillTitle`

### Dependencies (40)

*Types and components that `AbilityTrigger` references or depends upon:*

[AbilityInstance](/api/Global.AbilityInstance) · [AbilitySelfValidator](/api/Global.AbilitySelfValidator) · [AbilityTargetValidatorWrapper](/api/Global.AbilityTargetValidatorWrapper) · [Actor](/api/Global.Actor) · [ActorCheck](/api/Global.ActorCheck) · `ActorRef`1` · `Ai_GenericDodge` · [AssetRef`1](/api/Global.AssetRef`1) · [CastInfo](/api/Global.CastInfo) · [CastMethodData](/api/Global.CastMethodData) · [CastMethodDataSerialization](/api/Global.CastMethodDataSerialization) · [Channel](/api/Global.Channel) · [ClientEventManager](/api/Global.ClientEventManager) · [DataProcessorGroup`3](/api/Global.DataProcessorGroup`3) · [Dew](/api/Global.Dew) · [DewEffect](/api/Global.DewEffect) · [DewNetworkBehaviour](/api/Global.DewNetworkBehaviour) · [Entity](/api/Global.Entity) · [EntityAI](/api/Global.EntityAI) · [EntityAbility](/api/Global.EntityAbility) · [EntityAnimation](/api/Global.EntityAnimation) · [EntityCheck](/api/Global.EntityCheck) · [EntityControl](/api/Global.EntityControl) · [EntitySound](/api/Global.EntitySound) · [EntityStatus](/api/Global.EntityStatus) · [EventInfoCast](/api/Global.EventInfoCast) · [GameManager](/api/Global.GameManager) · [ICastMethodDataPoint](/api/Global.ICastMethodDataPoint) · [Monster](/api/Global.Monster) · [NetworkedManagerBase`1](/api/Global.NetworkedManagerBase`1) · [SafeAction](/api/Global.SafeAction) · [SafeAction`1](/api/Global.SafeAction`1) · [SafeAction`2](/api/Global.SafeAction`2) · [SkillTrigger](/api/Global.SkillTrigger) · [StatusEffect](/api/Global.StatusEffect) · [TriggerChannelData](/api/Global.TriggerChannelData) · [TriggerConfig](/api/Global.TriggerConfig) · `Vector3FlattenExtension` · `VectorPlaneTransformExtension` · `Mirror.GeneratedNetworkCode`

### Related Enums (1)

*Enumerations referenced in fields, properties, or method signatures:*

[`SaveVarFlags`](/enums#savevarflags)

:::
