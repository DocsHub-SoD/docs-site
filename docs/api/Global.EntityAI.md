# Class: EntityAI

- **Category:** <span class="cat-dot" style="--cat-color: #ef4444" data-cat="Combat & Abilities"></span> Combat & Abilities
- **Namespace:** `Global`
- **Assembly:** `Dew.Core.dll`
- **Attributes:** `[LogicUpdatePriority]`
- **Inheritance / Derived:** [DewNetworkBehaviour](/api/Global.DewNetworkBehaviour) → [EntityComponent](/api/Global.EntityComponent)

```csharp
[HideMonoScript]
[LogicUpdatePriority(-301)]
public class EntityAI : EntityComponent, ILogicUpdate
```

## Fields (24)

::: details Click to expand Fields (24)

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

:::

## Properties (5)

::: details Click to expand Properties (5)

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`context`** | `public EntityAIContext context { get; }` |  |
| **`detectionRange`** | `public float detectionRange { get; }` |  |
| **`estimatedVelocity`** | `public Vector3 estimatedVelocity { get; }` | Available only on server. |
| **`estimatedVelocityUnclamped`** | `public Vector3 estimatedVelocityUnclamped { get; }` | Available only on server. |
| **`isAITicking`** | `public bool isAITicking { get; set; }` |  |

:::

## Methods (17)

::: details `Aggro(Entity, bool)`

```csharp
public void Aggro(Entity target, bool doPropagation = false)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `target` | [`Entity`](/api/Global.Entity) |  |
| `doPropagation` | `bool` |  |

:::

::: details `CallAIUpdateImmediately()`

```csharp
public void CallAIUpdateImmediately()
```

:::

::: details `Helper_CanBeCast(AbilityTrigger)`

```csharp
public bool Helper_CanBeCast(AbilityTrigger abil)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `abil` | [`AbilityTrigger`](/api/Global.AbilityTrigger) |  |

**Returns:** `bool`

:::

::: details `Helper_CanBeCast&lt;T&gt;()`

```csharp
public bool Helper_CanBeCast<T>() where T : AbilityTrigger
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `` | `T` |  |

**Returns:** `bool`

:::

::: details `Helper_CastAbility&lt;T&gt;(CastInfo)`

```csharp
public void Helper_CastAbility<T>(CastInfo info) where T : AbilityTrigger
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `info` | [`CastInfo`](/api/Global.CastInfo) |  |
| `` | `T` |  |

:::

::: details `Helper_CastAbilityAuto(AbilityTrigger)`

Casts this ability with automatically populated CastInfo.This will select a target and then use ability trigger's prediction data.

```csharp
public bool Helper_CastAbilityAuto(AbilityTrigger abil)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `abil` | [`AbilityTrigger`](/api/Global.AbilityTrigger) |  |

**Returns:** `bool`

:::

::: details `Helper_CastAbilityAuto&lt;T&gt;()`

Casts this ability with automatically populated CastInfo.This will select a target and then use ability trigger's prediction data.

```csharp
public void Helper_CastAbilityAuto<T>() where T : AbilityTrigger
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `` | `T` |  |

:::

::: details `Helper_ChaseTarget()`

Chase targeted enemy. Note this will not interrupt ongoing chase if it's already chasing the same target.

```csharp
public void Helper_ChaseTarget()
```

:::

::: details `Helper_GetAbility&lt;T&gt;()`

Get ability of given type. Supports normal abilities and attack trigger.

```csharp
public T Helper_GetAbility<T>() where T : AbilityTrigger
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `` | `T` |  |

**Returns:** `T`

:::

::: details `Helper_IsTargetInRange(AbilityTrigger)`

```csharp
public bool Helper_IsTargetInRange(AbilityTrigger abil)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `abil` | [`AbilityTrigger`](/api/Global.AbilityTrigger) |  |

**Returns:** `bool`

:::

::: details `Helper_IsTargetInRange&lt;T&gt;()`

```csharp
public bool Helper_IsTargetInRange<T>() where T : AbilityTrigger
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `` | `T` |  |

**Returns:** `bool`

:::

::: details `Helper_IsTargetInRangeOfAttack()`

```csharp
public bool Helper_IsTargetInRangeOfAttack()
```

**Returns:** `bool`

:::

::: details `Helper_TryGetCastInfoAuto(AbilityTrigger, out CastInfo)`

```csharp
public bool Helper_TryGetCastInfoAuto(AbilityTrigger abil, out CastInfo info)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `abil` | [`AbilityTrigger`](/api/Global.AbilityTrigger) |  |
| `info` | [`CastInfo`](/api/Global.CastInfo) |  |

**Returns:** `bool`

:::

::: details `Helper_TryGetCastInfoAuto&lt;T&gt;(out CastInfo)`

```csharp
public bool Helper_TryGetCastInfoAuto<T>(out CastInfo info) where T : AbilityTrigger
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `info` | [`CastInfo`](/api/Global.CastInfo) |  |
| `` | `T` |  |

**Returns:** `bool`

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


## Architecture & Relationships

::: details Click to expand Architecture & Relationships

### Used By (69)

*Classes and systems that invoke, reference, or depend on `EntityAI`:*

[AbilityTrigger](/api/Global.AbilityTrigger) · [ActionCast](/api/Global.ActionCast) · `Ai_Mon_Ink_BossWhiteNight_Oppression` · `Ai_Mon_Primus_BossPrimusAeron_Dash` · `Ai_Mon_Special_AmbushSpawner_Projectile` · `Ai_R_BaptismOfSun` · [Entity](/api/Global.Entity) · [EntityVisual](/api/Global.EntityVisual) · [Hero](/api/Global.Hero) · `Mon_DarkCave_BossSeeker` · `Mon_DarkCave_CaveBat` · `Mon_DarkCave_DarkElemental` · `Mon_DarkCave_NightOlm` · `Mon_DarkCave_Oppressor` · `Mon_DarkCave_SeekerHallucination` · `Mon_Despair_AzurakMonsterSpawner` · `Mon_Despair_BossAzurak` · `Mon_Despair_Displacer` · `Mon_Despair_DreadBug` · `Mon_Despair_ParalyticFly` · `Mon_Despair_UnstableRat` · `Mon_Despair_WretchedArtillery` · `Mon_Forest_BossDemon` · `Mon_Forest_Hound` · `Mon_Forest_Scarab` · `Mon_Forest_SpiderSpitter` · `Mon_Forest_SpiderWarrior` · `Mon_Forest_Treant` · `Mon_Ink_Archer` · `Mon_Ink_BossDarkMoon` · `Mon_Ink_BossWhiteNight` · `Mon_Ink_DivineAnimal` · `Mon_Ink_EgoSword` · `Mon_Ink_GhostBlade` · `Mon_Ink_GhostSpear` · `Mon_LavaLand_BossInfernus` · `Mon_LavaLand_FireElemental` · `Mon_LavaLand_InfernoSpider` · `Mon_LavaLand_Magmadon` · `Mon_LavaLand_SuperheatedWolf` · `Mon_Primus_BossPrimusAeron` · `Mon_Sky_Baam` · `Mon_Sky_BigBaam_Base` · `Mon_Sky_BigBaam_Rooter` · `Mon_Sky_BossNyx` · `Mon_Sky_LittleBaam` · `Mon_Sky_StarSeed` · `Mon_SnowMountain_BossSkoll` · `Mon_SnowMountain_IceElemental` · `Mon_SnowMountain_LivingShards` · `Mon_SnowMountain_Scavenger` · `Mon_SnowMountain_SnowWolf` · `Mon_SnowMountain_VikingWarrior` · `Mon_Special_AmbushSpawner` · `Mon_Special_BossErebos` · `Mon_Special_BossLightElemental` · `Mon_Special_BossMaw` · `Mon_Special_BossObliviax` · `Mon_Special_BossPolaris` · [Monster](/api/Global.Monster) · [PropEnt_Merchant_Jonas](/api/Global.PropEnt_Merchant_Jonas) · `Se_AutoDetectPresence` · `Se_HeroKnockedOut` · `Se_Mon_DarkCave_BossSeeker_Blink` · `Se_Mon_SnowMountain_SnowWolf_SlowApproach` · `Se_MonsterSprint` · `Sum_R_AnnoyingBanner` · `Sum_R_SummonLittleBaam_Baam` · [Summon](/api/Global.Summon)

### Dependencies (28)

*Types and components that `EntityAI` references or depends upon:*

[AbilityTargetValidator](/api/Global.AbilityTargetValidator) · [AbilityTrigger](/api/Global.AbilityTrigger) · [Actor](/api/Global.Actor) · [ActorCheck](/api/Global.ActorCheck) · `ActorRef`1` · [CastInfo](/api/Global.CastInfo) · [CustomAIBehaviors](/api/Global.CustomAIBehaviors) · [Dew](/api/Global.Dew) · [DewNetworkBehaviour](/api/Global.DewNetworkBehaviour) · [DewPhysics](/api/Global.DewPhysics) · [DewPlayer](/api/Global.DewPlayer) · [Entity](/api/Global.Entity) · [EntityAIContext](/api/Global.EntityAIContext) · [EntityAbility](/api/Global.EntityAbility) · [EntityCheck](/api/Global.EntityCheck) · [EntityComponent](/api/Global.EntityComponent) · [EntityControl](/api/Global.EntityControl) · [EntityStatus](/api/Global.EntityStatus) · [EntityVisual](/api/Global.EntityVisual) · [Hero](/api/Global.Hero) · [IEnableWandering](/api/Global.IEnableWandering) · [ListReturnHandle`1](/api/Global.ListReturnHandle`1) · [Monster](/api/Global.Monster) · [RoomSection](/api/Global.RoomSection) · [SafeAction`1](/api/Global.SafeAction`1) · [Summon](/api/Global.Summon) · [TriggerConfig](/api/Global.TriggerConfig) · `VectorPlaneTransformExtension`

:::
