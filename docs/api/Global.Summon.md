# Class: Summon

- **Namespace:** `Global`
- **Assembly:** `Dew.Core.dll`
- **Inheritance / Derived:** [DewNetworkBehaviour](/api/Global.DewNetworkBehaviour) → [Actor](/api/Global.Actor) → [Entity](/api/Global.Entity)

```csharp
public class Summon : Entity, ILogicUpdate, ICleanup, ICustomDestroyRoutine
```

## Fields

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`armor`** | `[BoxGroup("Summon Settings", true, false, 0)]
public ScalingValue armor` |  |
| **`maxDuration`** | `[BoxGroup("Summon Settings", true, false, 0)]
public float maxDuration` |  |
| **`tvDefaultAllExceptSelf`** | `protected AbilityTargetValidatorWrapper tvDefaultAllExceptSelf` |  |
| **`tvDefaultHarmfulEffectTargets`** | `protected AbilityTargetValidatorWrapper tvDefaultHarmfulEffectTargets` |  |
| **`tvDefaultUsefulEffectTargets`** | `protected AbilityTargetValidatorWrapper tvDefaultUsefulEffectTargets` |  |

## Properties

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`effectiveLevel`** | `public int effectiveLevel { get; }` |  |
| **`hero`** | `public Hero hero { get; }` |  |
| **`info`** | `public CastInfo info { get; set; }` |  |
| **`isDestroyedOnRoomChange`** | `public override bool isDestroyedOnRoomChange { get; }` |  |
| **`normalizedRemainingDuration`** | `public float normalizedRemainingDuration { get; }` |  |
| **`skillLevel`** | `public int skillLevel { get; set; }` | Level of its origin skill trigger at the time this instance was cast. Defaults to -1 or that of parent's level.Parent type can either be SkillTrigger, AbilityInstance, or Gem.You can override level by setting this field when the instance is preparing. |
| **`statEntity`** | `public Entity statEntity { get; }` |  |
| **`summonHealth`** | `public float summonHealth { get; }` |  |

## Methods

### `ActiveLogicUpdate(float)`

```csharp
protected override void ActiveLogicUpdate(float dt)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `dt` | `float` |  |

### `AddDuration(float, bool)`

```csharp
public void AddDuration(float duration, bool clampToMaxDuration = true)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `duration` | `float` |  |
| `clampToMaxDuration` | `bool` |  |

### `AIUpdate(ref EntityAIContext)`

```csharp
protected override void AIUpdate(ref EntityAIContext context)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `context` | [EntityAIContext](/api/Global.EntityAIContext) |  |

### `CanAggroTo(Entity)`

```csharp
public override bool CanAggroTo(Entity target)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `target` | [Entity](/api/Global.Entity) |  |

**Returns:** `bool`

### `CreateDamage(SourceType, ScalingValue, float)`

```csharp
public DamageData CreateDamage(DamageData.SourceType type, ScalingValue value, float procCoefficient = 1)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `type` | [DamageData.SourceType](/api/Global.DamageData) |  |
| `value` | [ScalingValue](/api/Global.ScalingValue) |  |
| `procCoefficient` | `float` |  |

**Returns:** `DamageData`

### `Damage(ScalingValue, float)`

```csharp
public DamageData Damage(ScalingValue value, float procCoefficient = 1)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `value` | [ScalingValue](/api/Global.ScalingValue) |  |
| `procCoefficient` | `float` |  |

**Returns:** `DamageData`

### `DefaultDamage(ScalingValue, float)`

```csharp
public DamageData DefaultDamage(ScalingValue value, float procCoefficient = 1)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `value` | [ScalingValue](/api/Global.ScalingValue) |  |
| `procCoefficient` | `float` |  |

**Returns:** `DamageData`

### `GetStaggerSettings()`

```csharp
protected override Entity.StaggerSettings GetStaggerSettings()
```

**Returns:** `Entity.StaggerSettings`

### `GetValue(ScalingValue)`

```csharp
public float GetValue(ScalingValue val)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `val` | [ScalingValue](/api/Global.ScalingValue) |  |

**Returns:** `float`

### `Heal(ScalingValue)`

```csharp
public HealData Heal(ScalingValue amount)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `amount` | [ScalingValue](/api/Global.ScalingValue) |  |

**Returns:** `HealData`

### `MagicDamage(ScalingValue, float)`

```csharp
public DamageData MagicDamage(ScalingValue value, float procCoefficient = 1)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `value` | [ScalingValue](/api/Global.ScalingValue) |  |
| `procCoefficient` | `float` |  |

**Returns:** `DamageData`

### `OnCreate()`

```csharp
protected override void OnCreate()
```

### `OnDestroyActor()`

```csharp
protected override void OnDestroyActor()
```

### `OnPrepare()`

Called on server right before this instance to be spawned.Configure this instance's initial state here.By default this sets skillLevel to parent's level.Parent type can either be SkillTrigger, AbilityInstance, or Gem.

```csharp
protected override void OnPrepare()
```

### `OnStart()`

```csharp
public override void OnStart()
```

### `PhysicalDamage(ScalingValue, float)`

```csharp
public DamageData PhysicalDamage(ScalingValue value, float procCoefficient = 1)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `value` | [ScalingValue](/api/Global.ScalingValue) |  |
| `procCoefficient` | `float` |  |

**Returns:** `DamageData`

### `PhysicalMagicDamage(ScalingValue, float)`

```csharp
public DamageData PhysicalMagicDamage(ScalingValue value, float procCoefficient = 1)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `value` | [ScalingValue](/api/Global.ScalingValue) |  |
| `procCoefficient` | `float` |  |

**Returns:** `DamageData`

### `PureDamage(ScalingValue, float)`

```csharp
public DamageData PureDamage(ScalingValue value, float procCoefficient = 1)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `value` | [ScalingValue](/api/Global.ScalingValue) |  |
| `procCoefficient` | `float` |  |

**Returns:** `DamageData`

### `ReduceDuration(float, bool)`

```csharp
public void ReduceDuration(float duration, bool clampToMaxDuration = true)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `duration` | `float` |  |
| `clampToMaxDuration` | `bool` |  |

### `SummonCommand_AttackTarget(Entity)`

```csharp
public void SummonCommand_AttackTarget(Entity target)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `target` | [Entity](/api/Global.Entity) |  |

### `SummonCommand_MoveToDestination(Vector3)`

```csharp
public void SummonCommand_MoveToDestination(Vector3 destination)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `destination` | `UnityEngine.Vector3` |  |
