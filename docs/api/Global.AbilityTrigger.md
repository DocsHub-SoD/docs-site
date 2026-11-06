# Class: AbilityTrigger

- **Category:** <span class="cat-dot" style="--cat-color: #ef4444" data-cat="Combat & Abilities"></span> Combat & Abilities
- **Namespace:** `Global`
- **Assembly:** `Dew.Core.dll`
- **Inheritance / Derived:** [DewNetworkBehaviour](/api/Global.DewNetworkBehaviour) → [Actor](/api/Global.Actor) → [AttackTrigger](/api/Global.AttackTrigger) → [SkillTrigger](/api/Global.SkillTrigger)

```csharp
[LogicUpdatePriority(-300)]
public class AbilityTrigger : Actor, ILogicUpdate, ICleanup, ICustomDestroyRoutine
```

## Fields

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`ClientEvent_OnOwnerChanged`** | `public SafeAction<Entity, Entity> ClientEvent_OnOwnerChanged` |  |
| **`ClientTriggerEvent_OnCooldownReduced`** | `public SafeAction<int, float> ClientTriggerEvent_OnCooldownReduced` | configIndex, reductionAmount. Note the amount is non-discarded variant. e.g. Applying 100 seconds cooldown reduction to a 3 seconds skill will still report 100 seconds reduction. |
| **`ClientTriggerEvent_OnCooldownReducedByRatio`** | `public SafeAction<int, float> ClientTriggerEvent_OnCooldownReducedByRatio` |  |
| **`ClientTriggerEvent_OnCurrentConfigCharged`** | `public SafeAction ClientTriggerEvent_OnCurrentConfigCharged` |  |
| **`ClientTriggerEvent_OnCurrentConfigCooldownReduced`** | `public SafeAction ClientTriggerEvent_OnCurrentConfigCooldownReduced` |  |
| **`configs`** | `[ListDrawerSettings(Expanded = true)] public TriggerConfig[] configs` |  |
| **`currentCharges`** | `[SaveVar(SaveVarFlags.ApplyAfterFrameDelay)] [NonSerialized] public int[] currentCharges` |  |
| **`currentMinimumDelays`** | `[SaveVar(SaveVarFlags.ApplyAfterFrameDelay)] [NonSerialized] public float[] currentMinimumDelays` |  |
| **`currentUnscaledCooldownTimes`** | `[SaveVar(SaveVarFlags.ApplyAfterFrameDelay)] [NonSerialized] public float[] currentUnscaledCooldownTimes` |  |
| **`takenCooldownReductionByRatioProcessor`** | `public DataProcessorGroup<CooldownReductionByRatioSettings, Actor, AbilityTrigger> takenCooldownReductionByRatioProcessor` |  |
| **`takenCooldownReductionProcessor`** | `public DataProcessorGroup<CooldownReductionSettings, Actor, AbilityTrigger> takenCooldownReductionProcessor` |  |
| **`TriggerEvent_OnCastComplete`** | `public Action<EventInfoCast> TriggerEvent_OnCastComplete` |  |
| **`TriggerEvent_OnCastCompleteBeforePrepare`** | `public Action<EventInfoCast> TriggerEvent_OnCastCompleteBeforePrepare` |  |
| **`TriggerEvent_OnCastStart`** | `public Action<EventInfoCast> TriggerEvent_OnCastStart` |  |

## Properties

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

## Methods

### `Awake()`

```csharp
protected override void Awake()
```

### `CanBeCast()`

Can this ability be cast? By default this checks charges/delay/mana cost/self validator/self applied status effects.This must return same value for everyone to ensure consistency.

```csharp
public virtual bool CanBeCast()
```

**Returns:** `bool`

### `CanBeReserved()`

Can this ability be reserved? By default this checks everything that CanBeCast() checks but self validators.This must return same value for everyone to ensure consistency.

```csharp
public virtual bool CanBeReserved()
```

**Returns:** `bool`

### `ChangeConfigTimed(int, float, Action<EventInfoAbilityInstance>, Action, bool)`

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

### `ChangeConfigTimedOnce(int, float, Action<EventInfoAbilityInstance>, Action, bool)`

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

### `GetActorReadableName()`

```csharp
public override string GetActorReadableName()
```

**Returns:** `string`

### `GetAnimationSpeed()`

```csharp
public virtual float GetAnimationSpeed()
```

**Returns:** `float`

### `GetCastInfoToTarget(Entity)`

```csharp
public CastInfo GetCastInfoToTarget(Entity target)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `target` | [`Entity`](/api/Global.Entity) |  |

**Returns:** `CastInfo`

### `GetChannelDurationMultiplier()`

```csharp
public virtual float GetChannelDurationMultiplier()
```

**Returns:** `float`

### `GetCooldownTimeMultiplier(int)`

```csharp
public virtual float GetCooldownTimeMultiplier(int configIndex)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `configIndex` | `int` |  |

**Returns:** `float`

### `GetCooldownTimeMultiplierByAbilityHaste(float)`

```csharp
public static float GetCooldownTimeMultiplierByAbilityHaste(float abilityHaste)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `abilityHaste` | `float` |  |

**Returns:** `float`

### `GetCooldownTimeOffset(int)`

```csharp
public virtual float GetCooldownTimeOffset(int configIndex)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `configIndex` | `int` |  |

**Returns:** `float`

### `GetInstanceSpawnPosition(int, CastInfo)`

```csharp
protected virtual Vector3 GetInstanceSpawnPosition(int configIndex, CastInfo info)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `configIndex` | `int` |  |
| `info` | [`CastInfo`](/api/Global.CastInfo) |  |

**Returns:** `UnityEngine.Vector3`

### `GetInstanceSpawnRotation(int, CastInfo)`

```csharp
protected virtual Quaternion? GetInstanceSpawnRotation(int configIndex, CastInfo info)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `configIndex` | `int` |  |
| `info` | [`CastInfo`](/api/Global.CastInfo) |  |

**Returns:** `UnityEngine.Quaternion?`

### `GetMaxCooldownTime(int, bool)`

```csharp
public float GetMaxCooldownTime(int configIndex, bool scaled = true)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `configIndex` | `int` |  |
| `scaled` | `bool` |  |

**Returns:** `float`

### `GetPostDelayDurationMultiplier()`

```csharp
public virtual float GetPostDelayDurationMultiplier()
```

**Returns:** `float`

### `GetPredictedCastInfoToTarget(Entity, float)`

```csharp
public CastInfo GetPredictedCastInfoToTarget(Entity target, float strength)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `target` | [`Entity`](/api/Global.Entity) |  |
| `strength` | `float` |  |

**Returns:** `CastInfo`

### `GetPredictedCastInfoToTarget(Entity)`

```csharp
public CastInfo GetPredictedCastInfoToTarget(Entity target)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `target` | [`Entity`](/api/Global.Entity) |  |

**Returns:** `CastInfo`

### `IsConfigLocked(int)`

```csharp
public bool IsConfigLocked(int configIndex)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `configIndex` | `int` |  |

**Returns:** `bool`

### `IsTargetInRange(Entity)`

```csharp
public bool IsTargetInRange(Entity target)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `target` | [`Entity`](/api/Global.Entity) |  |

**Returns:** `bool`

### `LockCooldown(int)`

```csharp
public void LockCooldown(int configIndex)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `configIndex` | `int` |  |

### `LogicUpdate(float)`

```csharp
public override void LogicUpdate(float dt)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `dt` | `float` |  |

### `OnCastCancel(int, CastInfo)`

Called on server when this ability's cast channel is canceled.By default, this sets the cooldown time to 1 second if its smaller than 1 second.

```csharp
protected virtual void OnCastCancel(int configIndex, CastInfo info)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `configIndex` | `int` |  |
| `info` | [`CastInfo`](/api/Global.CastInfo) |  |

### `OnCastCancelSetCooldownTime(int, CastInfo)`

```csharp
protected virtual void OnCastCancelSetCooldownTime(int configIndex, CastInfo info)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `configIndex` | `int` |  |
| `info` | [`CastInfo`](/api/Global.CastInfo) |  |

### `OnCastComplete(int, CastInfo)`

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

### `OnCastCompleteBeforePrepare(EventInfoCast)`

```csharp
public virtual void OnCastCompleteBeforePrepare(EventInfoCast cast)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `cast` | [`EventInfoCast`](/api/Global.EventInfoCast) |  |

### `OnCastCompleteSetCharge(int, CastInfo)`

```csharp
public virtual void OnCastCompleteSetCharge(int configIndex, CastInfo info)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `configIndex` | `int` |  |
| `info` | [`CastInfo`](/api/Global.CastInfo) |  |

### `OnCastCompleteSetCooldownTime(int, CastInfo)`

```csharp
public virtual void OnCastCompleteSetCooldownTime(int configIndex, CastInfo info)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `configIndex` | `int` |  |
| `info` | [`CastInfo`](/api/Global.CastInfo) |  |

### `OnCastCompleteSetMinimumDelay(int, CastInfo)`

```csharp
public virtual void OnCastCompleteSetMinimumDelay(int configIndex, CastInfo info)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `configIndex` | `int` |  |
| `info` | [`CastInfo`](/api/Global.CastInfo) |  |

### `OnCastCompleteSpendMana(int, CastInfo)`

```csharp
public virtual void OnCastCompleteSpendMana(int configIndex, CastInfo info)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `configIndex` | `int` |  |
| `info` | [`CastInfo`](/api/Global.CastInfo) |  |

### `OnCastStart(int, CastInfo)`

Called on server when this ability is cast.By default, this plays the animation and starts the configured channel.IffaceForwardis set to true, it will cause the owner to rotate towards the target/point/direction/cursor position.Target validation will be done on the channel if the cast method is set to Target.

```csharp
public virtual void OnCastStart(int configIndex, CastInfo info)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `configIndex` | `int` |  |
| `info` | [`CastInfo`](/api/Global.CastInfo) |  |

### `OnConfigChanged(int, int)`

Called everywhere when current config index is changed or set initial value.

```csharp
protected virtual void OnConfigChanged(int oldIndex, int newIndex)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `oldIndex` | `int` |  |
| `newIndex` | `int` |  |

### `OnCreate()`

```csharp
protected override void OnCreate()
```

### `OnDeserialize(NetworkReader, bool)`

```csharp
public override void OnDeserialize(NetworkReader reader, bool initialState)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `reader` | `Mirror.NetworkReader` |  |
| `initialState` | `bool` |  |

### `OnEquip(Entity)`

Called on everyone when the trigger is being equipped.

```csharp
protected virtual void OnEquip(Entity newOwner)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `newOwner` | [`Entity`](/api/Global.Entity) |  |

### `OnRotateForward(int, CastInfo)`

```csharp
protected virtual void OnRotateForward(int configIndex, CastInfo info)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `configIndex` | `int` |  |
| `info` | [`CastInfo`](/api/Global.CastInfo) |  |

### `OnSerialize(NetworkWriter, bool)`

```csharp
public override void OnSerialize(NetworkWriter writer, bool initialState)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `writer` | `Mirror.NetworkWriter` |  |
| `initialState` | `bool` |  |

### `OnStartChannel(int, CastInfo)`

```csharp
protected virtual void OnStartChannel(int configIndex, CastInfo info)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `configIndex` | `int` |  |
| `info` | [`CastInfo`](/api/Global.CastInfo) |  |

### `OnStartServer()`

```csharp
public override void OnStartServer()
```

### `OnStopServer()`

```csharp
public override void OnStopServer()
```

### `OnUnequip(Entity)`

Called on everyone when the trigger is being unequipped.

```csharp
protected virtual void OnUnequip(Entity formerOwner)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `formerOwner` | [`Entity`](/api/Global.Entity) |  |

### `PredictAngle_Simple(float, Entity, Vector3, float)`

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

### `PredictAngle_SpeedAcceleration(float, Entity, Vector3, float, float, float, float, float)`

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

### `PredictPoint_Simple(float, Entity, float)`

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

### `PredictPoint_SpeedAcceleration(float, Entity, Vector3, float, float, float, float, float)`

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

### `PredictPointClamped_Simple(float, Entity, Vector3, float, float)`

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

### `PredictPointClamped_SpeedAcceleration(float, Entity, Vector3, float, float, float, float, float, float)`

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

### `PredictTime_SpeedAcceleration(Entity, Vector3, float, float, float, float, float)`

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

### `ProcessRange(float)`

```csharp
public virtual float ProcessRange(float original)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `original` | `float` |  |

**Returns:** `float`

### `ProcessReceivedCooldownReduction(ref CooldownReductionSettings, Actor)`

```csharp
public void ProcessReceivedCooldownReduction(ref CooldownReductionSettings data, Actor actor)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `data` | [`CooldownReductionSettings`](/api/Global.CooldownReductionSettings) |  |
| `actor` | [`Actor`](/api/Global.Actor) |  |

### `ProcessReceivedCooldownReductionByRatio(ref CooldownReductionByRatioSettings, Actor)`

```csharp
public void ProcessReceivedCooldownReductionByRatio(ref CooldownReductionByRatioSettings data, Actor actor)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `data` | [`CooldownReductionByRatioSettings`](/api/Global.CooldownReductionByRatioSettings) |  |
| `actor` | [`Actor`](/api/Global.Actor) |  |

### `SetCharge(int, int)`

```csharp
public void SetCharge(int configIndex, int charge)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `configIndex` | `int` |  |
| `charge` | `int` |  |

### `SetChargeAll(int)`

```csharp
public void SetChargeAll(int charge)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `charge` | `int` |  |

### `SetCooldownTime(int, float, bool)`

```csharp
public void SetCooldownTime(int configIndex, float time, bool scaled = true)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `configIndex` | `int` |  |
| `time` | `float` |  |
| `scaled` | `bool` |  |

### `SetCooldownTimeAll(float, bool)`

```csharp
public void SetCooldownTimeAll(float time, bool scaled = true)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `time` | `float` |  |
| `scaled` | `bool` |  |

### `SetMinimumDelay(int, float)`

```csharp
public void SetMinimumDelay(int configIndex, float delay)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `configIndex` | `int` |  |
| `delay` | `float` |  |

### `SetMinimumDelayAll(float)`

```csharp
public void SetMinimumDelayAll(float delay)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `delay` | `float` |  |

### `ShouldTickCooldown(int)`

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

### `SyncCastMethodChanges(int)`

```csharp
public void SyncCastMethodChanges(int configIndex)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `configIndex` | `int` |  |

### `UndoChangeConfig()`

```csharp
public void UndoChangeConfig()
```

### `UnlockCooldown(int)`

```csharp
public void UnlockCooldown(int configIndex)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `configIndex` | `int` |  |
