# Class: EntityAI

- **Category:** <span class="cat-dot" style="--cat-color: #ef4444" data-cat="Combat & Abilities"></span> Combat & Abilities
- **Namespace:** `Global`
- **Assembly:** `Dew.Core.dll`
- **Inheritance / Derived:** [DewNetworkBehaviour](/api/Global.DewNetworkBehaviour) → [EntityComponent](/api/Global.EntityComponent)

```csharp
[HideMonoScript]
[LogicUpdatePriority(-301)]
public class EntityAI : EntityComponent, ILogicUpdate
```

## Fields

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`AggroPropagationDelayMax`** | `public const float AggroPropagationDelayMax = 0.7` |  |
| **`AggroPropagationDelayMin`** | `public const float AggroPropagationDelayMin = 0.1` |  |
| **`AggroPropagationRange`** | `public const float AggroPropagationRange = 17` |  |
| **`AITickCongestionThreshold`** | `public const int AITickCongestionThreshold = 5000` |  |
| **`BossAITickInterval`** | `public const float BossAITickInterval = 0.25` |  |
| **`BossDetectionRange`** | `public const float BossDetectionRange = 25` |  |
| **`CombatAITickInterval`** | `public const float CombatAITickInterval = 0.5` |  |
| **`customBehaviors`** | `public CustomAIBehaviors customBehaviors` | You can customize AI behavior of this entity externally using this.Available only on server. Null on clients. |
| **`DefaultDetectionRange`** | `public const float DefaultDetectionRange = 15` |  |
| **`disableAI`** | `public bool disableAI` |  |
| **`DisableAI`** | `public static bool DisableAI` |  |
| **`excludeFromAutoTargeting`** | `public bool excludeFromAutoTargeting` |  |
| **`IdleAITickInterval`** | `public const float IdleAITickInterval = 1` |  |
| **`LoseTargetedEnemyTime`** | `public const float LoseTargetedEnemyTime = 5` |  |
| **`PositionSampleCount`** | `public static int PositionSampleCount` |  |
| **`PositionSampleInterval`** | `public static float PositionSampleInterval` |  |
| **`PositionSampleLagBehindFrames`** | `public static int PositionSampleLagBehindFrames` |  |
| **`predictionStrengthOverride`** | `[NonSerialized] public Func<float> predictionStrengthOverride` |  |
| **`RetargetingDistanceFuzziness`** | `public const float RetargetingDistanceFuzziness = 0.3` |  |
| **`RetargetingMaxTime`** | `public const float RetargetingMaxTime = 4` |  |
| **`RetargetingMinTime`** | `public const float RetargetingMinTime = 1` |  |
| **`WanderIntervalMax`** | `public const float WanderIntervalMax = 15` |  |
| **`WanderIntervalMin`** | `public const float WanderIntervalMin = 4` |  |
| **`WanderSpeedMultiplier`** | `public const float WanderSpeedMultiplier = 0.6` |  |

## Properties

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`context`** | `public EntityAIContext context { get; }` |  |
| **`detectionRange`** | `public float detectionRange { get; }` |  |
| **`estimatedVelocity`** | `public Vector3 estimatedVelocity { get; }` | Available only on server. |
| **`estimatedVelocityUnclamped`** | `public Vector3 estimatedVelocityUnclamped { get; }` | Available only on server. |
| **`isAITicking`** | `public bool isAITicking { get; set; }` |  |

## Methods

### `Aggro(Entity, bool)`

```csharp
public void Aggro(Entity target, bool doPropagation = false)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `target` | [`Entity`](/api/Global.Entity) |  |
| `doPropagation` | `bool` |  |

### `CallAIUpdateImmediately()`

```csharp
public void CallAIUpdateImmediately()
```

### `Helper_CanBeCast(AbilityTrigger)`

```csharp
public bool Helper_CanBeCast(AbilityTrigger abil)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `abil` | [`AbilityTrigger`](/api/Global.AbilityTrigger) |  |

**Returns:** `bool`

### `Helper_CanBeCast<T>()`

```csharp
public bool Helper_CanBeCast<T>() where T : AbilityTrigger
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `` | `T` |  |

**Returns:** `bool`

### `Helper_CastAbility<T>(CastInfo)`

```csharp
public void Helper_CastAbility<T>(CastInfo info) where T : AbilityTrigger
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `info` | [`CastInfo`](/api/Global.CastInfo) |  |
| `` | `T` |  |

### `Helper_CastAbilityAuto(AbilityTrigger)`

Casts this ability with automatically populated CastInfo.This will select a target and then use ability trigger's prediction data.

```csharp
public bool Helper_CastAbilityAuto(AbilityTrigger abil)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `abil` | [`AbilityTrigger`](/api/Global.AbilityTrigger) |  |

**Returns:** `bool`

### `Helper_CastAbilityAuto<T>()`

Casts this ability with automatically populated CastInfo.This will select a target and then use ability trigger's prediction data.

```csharp
public void Helper_CastAbilityAuto<T>() where T : AbilityTrigger
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `` | `T` |  |

### `Helper_ChaseTarget()`

Chase targeted enemy. Note this will not interrupt ongoing chase if it's already chasing the same target.

```csharp
public void Helper_ChaseTarget()
```

### `Helper_GetAbility<T>()`

Get ability of given type. Supports normal abilities and attack trigger.

```csharp
public T Helper_GetAbility<T>() where T : AbilityTrigger
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `` | `T` |  |

**Returns:** `T`

### `Helper_IsTargetInRange(AbilityTrigger)`

```csharp
public bool Helper_IsTargetInRange(AbilityTrigger abil)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `abil` | [`AbilityTrigger`](/api/Global.AbilityTrigger) |  |

**Returns:** `bool`

### `Helper_IsTargetInRange<T>()`

```csharp
public bool Helper_IsTargetInRange<T>() where T : AbilityTrigger
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `` | `T` |  |

**Returns:** `bool`

### `Helper_IsTargetInRangeOfAttack()`

```csharp
public bool Helper_IsTargetInRangeOfAttack()
```

**Returns:** `bool`

### `Helper_TryGetCastInfoAuto(AbilityTrigger, out CastInfo)`

```csharp
public bool Helper_TryGetCastInfoAuto(AbilityTrigger abil, out CastInfo info)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `abil` | [`AbilityTrigger`](/api/Global.AbilityTrigger) |  |
| `info` | [`CastInfo`](/api/Global.CastInfo) |  |

**Returns:** `bool`

### `Helper_TryGetCastInfoAuto<T>(out CastInfo)`

```csharp
public bool Helper_TryGetCastInfoAuto<T>(out CastInfo info) where T : AbilityTrigger
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `info` | [`CastInfo`](/api/Global.CastInfo) |  |
| `` | `T` |  |

**Returns:** `bool`

### `LogicUpdate(float)`

```csharp
public override void LogicUpdate(float dt)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `dt` | `float` |  |

### `OnStartServer()`

```csharp
public override void OnStartServer()
```

### `OnStopServer()`

```csharp
public override void OnStopServer()
```
