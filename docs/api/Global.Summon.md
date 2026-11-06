# Class: Summon

- **Category:** <span class="cat-dot" style="--cat-color: #ef4444" data-cat="Combat & Abilities"></span> Combat & Abilities
- **Namespace:** `Global`
- **Assembly:** `Dew.Core.dll`
- **Inheritance / Derived:** [DewNetworkBehaviour](/api/Global.DewNetworkBehaviour) → [Actor](/api/Global.Actor) → [Entity](/api/Global.Entity)

```csharp
public class Summon : Entity, ILogicUpdate, ICleanup, ICustomDestroyRoutine
```

## Fields (5)

::: details Click to expand Fields (5)

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`armor`** | `[BoxGroup("Summon Settings", true, false, 0)] public ScalingValue armor` |  |
| **`maxDuration`** | `[BoxGroup("Summon Settings", true, false, 0)] public float maxDuration` |  |
| **`tvDefaultAllExceptSelf`** | `protected AbilityTargetValidatorWrapper tvDefaultAllExceptSelf` |  |
| **`tvDefaultHarmfulEffectTargets`** | `protected AbilityTargetValidatorWrapper tvDefaultHarmfulEffectTargets` |  |
| **`tvDefaultUsefulEffectTargets`** | `protected AbilityTargetValidatorWrapper tvDefaultUsefulEffectTargets` |  |

:::

## Properties (8)

::: details Click to expand Properties (8)

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

:::

## Methods (21)

::: details `ActiveLogicUpdate(float)`

```csharp
protected override void ActiveLogicUpdate(float dt)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `dt` | `float` |  |

:::

::: details `AddDuration(float, bool)`

```csharp
public void AddDuration(float duration, bool clampToMaxDuration = true)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `duration` | `float` |  |
| `clampToMaxDuration` | `bool` |  |

:::

::: details `AIUpdate(ref EntityAIContext)`

```csharp
protected override void AIUpdate(ref EntityAIContext context)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `context` | [`EntityAIContext`](/api/Global.EntityAIContext) |  |

:::

::: details `CanAggroTo(Entity)`

```csharp
public override bool CanAggroTo(Entity target)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `target` | [`Entity`](/api/Global.Entity) |  |

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

::: details `GetStaggerSettings()`

```csharp
protected override Entity.StaggerSettings GetStaggerSettings()
```

**Returns:** `Entity.StaggerSettings`

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

::: details `ReduceDuration(float, bool)`

```csharp
public void ReduceDuration(float duration, bool clampToMaxDuration = true)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `duration` | `float` |  |
| `clampToMaxDuration` | `bool` |  |

:::

::: details `SummonCommand_AttackTarget(Entity)`

```csharp
public void SummonCommand_AttackTarget(Entity target)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `target` | [`Entity`](/api/Global.Entity) |  |

:::

::: details `SummonCommand_MoveToDestination(Vector3)`

```csharp
public void SummonCommand_MoveToDestination(Vector3 destination)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `destination` | `UnityEngine.Vector3` |  |

:::


## Architecture & Relationships

::: details Click to expand Architecture & Relationships

### Used By (16)

*Classes and systems that invoke, reference, or depend on `Summon`:*

[AbilityInstance](/api/Global.AbilityInstance) · `Ai_R_NaturesWhisper` · [EntityAI](/api/Global.EntityAI) · [EventInfoSummon](/api/Global.EventInfoSummon) · `Primus_Ending` · `Se_Star_Nachia_F_SC_AtkSpd` · `Se_Star_Nachia_F_SC_MoreSummons` · `Se_Star_Nachia_F_SC_SummonDmgReduction` · `St_D_CircleOfLife` · `Sum_BossMaw_MoonlightPact_Fenrir` · `Sum_L_SmallMoltenCore_Dragon` · `Sum_Q_MoonlightPact_Fenrir` · `Sum_Q_SylvanCall_LeafHound` · `Sum_R_AnnoyingBanner` · `Sum_R_SummonLittleBaam_Baam` · `UI_EntitySummonDuration`

### Dependencies (32)

*Types and components that `Summon` references or depends upon:*

[AbilityInstance](/api/Global.AbilityInstance) · [AbilityTargetValidatorWrapper](/api/Global.AbilityTargetValidatorWrapper) · [AbilityTrigger](/api/Global.AbilityTrigger) · [Actor](/api/Global.Actor) · [ActorCheck](/api/Global.ActorCheck) · [BasicEffectWithStrength](/api/Global.BasicEffectWithStrength) · [CastInfo](/api/Global.CastInfo) · [CustomAIBehaviors](/api/Global.CustomAIBehaviors) · [DamageData](/api/Global.DamageData) · [Dew](/api/Global.Dew) · [DewPhysics](/api/Global.DewPhysics) · [Entity](/api/Global.Entity) · [EntityAI](/api/Global.EntityAI) · [EntityAIContext](/api/Global.EntityAIContext) · [EntityCheck](/api/Global.EntityCheck) · [EntityControl](/api/Global.EntityControl) · [EntityStatus](/api/Global.EntityStatus) · [EventInfoAttackHit](/api/Global.EventInfoAttackHit) · [GameManager](/api/Global.GameManager) · [Gem](/api/Global.Gem) · [HealData](/api/Global.HealData) · [Hero](/api/Global.Hero) · [ListReturnHandle`1](/api/Global.ListReturnHandle`1) · [NetworkedManagerBase`1](/api/Global.NetworkedManagerBase`1) · [SafeAction](/api/Global.SafeAction) · [SafeAction`1](/api/Global.SafeAction`1) · [ScalingValue](/api/Global.ScalingValue) · [SkillTrigger](/api/Global.SkillTrigger) · [StatBonus](/api/Global.StatBonus) · `VectorPlaneTransformExtension` · [ZoneManager](/api/Global.ZoneManager) · `Mirror.GeneratedNetworkCode`

:::
