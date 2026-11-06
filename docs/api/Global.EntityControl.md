# Class: EntityControl

- **Category:** <span class="cat-dot" style="--cat-color: #ef4444" data-cat="Combat & Abilities"></span> Combat & Abilities
- **Namespace:** `Global`
- **Assembly:** `Dew.Core.dll`
- **Attributes:** `[RequireComponent]`
- **Inheritance / Derived:** [DewNetworkBehaviour](/api/Global.DewNetworkBehaviour) → [EntityComponent](/api/Global.EntityComponent)

```csharp
[HideMonoScript]
[RequireComponent(typeof(EntityTransformSync))]
public class EntityControl : EntityComponent, ILogicUpdate, ICleanup
```

## Fields (22)

::: details Click to expand Fields (22)

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`attackTarget`** | `[NonSerialized] public Entity attackTarget` | Available on server. |
| **`baseAgentSpeed`** | `public float baseAgentSpeed` |  |
| **`ClientEvent_OnDisplacementCanceled`** | `public SafeAction<Displacement> ClientEvent_OnDisplacementCanceled` |  |
| **`ClientEvent_OnDisplacementFinished`** | `public SafeAction<Displacement> ClientEvent_OnDisplacementFinished` |  |
| **`ClientEvent_OnDisplacementStarted`** | `public SafeAction<Displacement> ClientEvent_OnDisplacementStarted` |  |
| **`ClientEvent_OnInnerRadiusChanged`** | `public SafeAction<float, float> ClientEvent_OnInnerRadiusChanged` |  |
| **`ClientEvent_OnOuterRadiusChanged`** | `public SafeAction<float, float> ClientEvent_OnOuterRadiusChanged` |  |
| **`ClientEvent_OnTeleport`** | `public SafeAction<Vector3, Vector3> ClientEvent_OnTeleport` |  |
| **`CommandStallTimeout`** | `public const float CommandStallTimeout = 0.15` |  |
| **`lastMoveTime`** | `[NonSerialized] public float lastMoveTime` | Available on server. |
| **`normalizedAcceleration`** | `public float normalizedAcceleration` |  |
| **`obstacleAvoidance`** | `public bool obstacleAvoidance` |  |
| **`ongoingChannels`** | `public List<Channel> ongoingChannels` | List of ongoingChannels on this entity.Only valid on server. |
| **`QueuedActionExpireTime`** | `public const float QueuedActionExpireTime = 0.2` |  |
| **`rotateSpeed`** | `public float rotateSpeed` |  |
| **`rotationSmoothTime`** | `public float rotationSmoothTime` |  |
| **`SyncAgentVelocityLifetime`** | `public static float SyncAgentVelocityLifetime` |  |
| **`SyncExtrapolateMaxTime`** | `public static float SyncExtrapolateMaxTime` |  |
| **`SyncExtrapolateStrength`** | `public static float SyncExtrapolateStrength` |  |
| **`SyncFixSmoothTime`** | `public static float SyncFixSmoothTime` |  |
| **`SyncFixSnapshotLifetime`** | `public static float SyncFixSnapshotLifetime` |  |
| **`SyncFixWarpDistance`** | `public static float SyncFixWarpDistance` |  |

:::

## Properties (25)

::: details Click to expand Properties (25)

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`agentPosition`** | `public Vector3 agentPosition { get; }` |  |
| **`agentVelocity`** | `public Vector3 agentVelocity { get; }` | Agent velocity of this entity. Available everywhere. |
| **`canDestroy`** | `public bool canDestroy { get; }` |  |
| **`currentMaxAgentSpeed`** | `public float currentMaxAgentSpeed { get; }` |  |
| **`desiredAngle`** | `public float desiredAngle { get; }` |  |
| **`desiredRotation`** | `public Quaternion desiredRotation { get; }` |  |
| **`forceWalking`** | `public bool forceWalking { get; }` |  |
| **`freeMovement`** | `public bool freeMovement { get; set; }` | Disables agent. |
| **`innerRadius`** | `public float innerRadius { get; set; }` |  |
| **`isAirborne`** | `public bool isAirborne { get; }` | Is this entity doing non-friendly displacement? |
| **`isClientSideMovement`** | `public bool isClientSideMovement { get; }` | Is client-side movement enabled for this entity? |
| **`isControlReversed`** | `public bool isControlReversed { get; set; }` | This only has effect on player-controlled entities. |
| **`isDashing`** | `public bool isDashing { get; }` | Is this entity doing friendly displacement? |
| **`isDisplacing`** | `public bool isDisplacing { get; }` |  |
| **`isDodging`** | `public bool isDodging { get; }` | Is this entity doing a displacement from dodge ability? e.g. Ai_GenericDodge |
| **`isDoingMoveToAction`** | `public bool isDoingMoveToAction { get; }` | Available on movement processors and server |
| **`isGamepadRotationLocked`** | `public bool isGamepadRotationLocked { get; }` | Is gamepad look rotation locked? |
| **`isLocalMovementProcessor`** | `public bool isLocalMovementProcessor { get; }` | Is local machine liable for processing movements? |
| **`isWalking`** | `public bool isWalking { get; }` | Is this entity walking? Available everywhere. |
| **`ongoingDisplacement`** | `public Displacement ongoingDisplacement { get; }` |  |
| **`outerRadius`** | `public float outerRadius { get; set; }` |  |
| **`overridenDesiredAngle`** | `public float? overridenDesiredAngle { get; }` |  |
| **`proxyCollider`** | `public ProxyCollider proxyCollider { get; }` |  |
| **`queuedActions`** | `public IReadOnlyList<ActionBase> queuedActions { get; }` |  |
| **`walkStrength`** | `public float walkStrength { get; }` | Can have values of range 0 ~ 1 depending on how fast it is walking. Available everywhere. |

:::

## Methods (53)

::: details `Attack(Entity, bool)`

```csharp
public void Attack(Entity target, bool doChase)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `target` | [`Entity`](/api/Global.Entity) |  |
| `doChase` | `bool` |  |

:::

::: details `AttackMove(Vector3, bool)`

```csharp
public void AttackMove(Vector3 destination, bool useDistanceFromDestination = false)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `destination` | `UnityEngine.Vector3` |  |
| `useDistanceFromDestination` | `bool` |  |

:::

::: details `CancelOngoingChannels()`

```csharp
public void CancelOngoingChannels()
```

:::

::: details `CancelOngoingDisplacement()`

```csharp
public void CancelOngoingDisplacement()
```

:::

::: details `Cast(AbilityTrigger, CastInfo, bool)`

```csharp
public void Cast(AbilityTrigger trigger, CastInfo info, bool allowMoveToCast = true)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `trigger` | [`AbilityTrigger`](/api/Global.AbilityTrigger) |  |
| `info` | [`CastInfo`](/api/Global.CastInfo) |  |
| `allowMoveToCast` | `bool` |  |

:::

::: details `Cast(AbilityTrigger, Entity, bool)`

```csharp
public void Cast(AbilityTrigger trigger, Entity predictTarget, bool allowMoveToCast = true)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `trigger` | [`AbilityTrigger`](/api/Global.AbilityTrigger) |  |
| `predictTarget` | [`Entity`](/api/Global.Entity) |  |
| `allowMoveToCast` | `bool` |  |

:::

::: details `Cast(AbilityTrigger, int, CastInfo, bool, bool)`

Provide -1 forconfigIndexto denote ANY config index.This will cause undefined behavior if cast method differs between configs!!

```csharp
public void Cast(AbilityTrigger trigger, int configIndex, CastInfo info, bool allowMoveToCast = true, bool skipRangeCheck = false)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `trigger` | [`AbilityTrigger`](/api/Global.AbilityTrigger) |  |
| `configIndex` | `int` |  |
| `info` | [`CastInfo`](/api/Global.CastInfo) |  |
| `allowMoveToCast` | `bool` |  |
| `skipRangeCheck` | `bool` |  |

:::

::: details `Cast(AbilityTrigger, int, Entity, bool)`

```csharp
public void Cast(AbilityTrigger trigger, int configIndex, Entity predictTarget, bool allowMoveToCast = true)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `trigger` | [`AbilityTrigger`](/api/Global.AbilityTrigger) |  |
| `configIndex` | `int` |  |
| `predictTarget` | [`Entity`](/api/Global.Entity) |  |
| `allowMoveToCast` | `bool` |  |

:::

::: details `ClearActionQueue()`

```csharp
public void ClearActionQueue()
```

:::

::: details `ClearMovement()`

```csharp
public void ClearMovement()
```

:::

::: details `CmdAttack(Entity, bool)`

Provide null to clear attack target.

```csharp
public void CmdAttack(Entity target, bool doChase)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `target` | [`Entity`](/api/Global.Entity) |  |
| `doChase` | `bool` |  |

:::

::: details `CmdAttackMove(Vector3, bool)`

```csharp
public void CmdAttackMove(Vector3 destination, bool useDistanceFromDestination)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `destination` | `UnityEngine.Vector3` |  |
| `useDistanceFromDestination` | `bool` |  |

:::

::: details `CmdCancelOngoingChannels()`

```csharp
public void CmdCancelOngoingChannels()
```

:::

::: details `CmdCast(AbilityTrigger, int, CastInfo, bool, bool)`

```csharp
public void CmdCast(AbilityTrigger trigger, int configIndex, CastInfo info, bool allowMoveToCast, bool skipRangeCheck)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `trigger` | [`AbilityTrigger`](/api/Global.AbilityTrigger) |  |
| `configIndex` | `int` |  |
| `info` | [`CastInfo`](/api/Global.CastInfo) |  |
| `allowMoveToCast` | `bool` |  |
| `skipRangeCheck` | `bool` |  |

:::

::: details `CmdClearMovement()`

```csharp
public void CmdClearMovement()
```

:::

::: details `CmdInteract(IInteractable, bool, bool)`

```csharp
public void CmdInteract(IInteractable interactable, bool isAlt, bool isMouse)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `interactable` | [`IInteractable`](/api/Global.IInteractable) |  |
| `isAlt` | `bool` |  |
| `isMouse` | `bool` |  |

:::

::: details `CmdLookInDirection(Vector3)`

```csharp
public void CmdLookInDirection(Vector3 dir)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `dir` | `UnityEngine.Vector3` |  |

:::

::: details `CmdMoveToDestination(Vector3, bool, float)`

```csharp
public void CmdMoveToDestination(Vector3 destination, bool immediately, float speedMult = 1)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `destination` | `UnityEngine.Vector3` |  |
| `immediately` | `bool` |  |
| `speedMult` | `float` |  |

:::

::: details `CmdMoveWithDirection(Vector3)`

```csharp
public void CmdMoveWithDirection(Vector3 direction)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `direction` | `UnityEngine.Vector3` |  |

:::

::: details `CmdStop()`

```csharp
public void CmdStop()
```

:::

::: details `CreateTransformABTo01(Vector2, Vector2)`

```csharp
public static Matrix4x4 CreateTransformABTo01(Vector2 a, Vector2 b)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `a` | `UnityEngine.Vector2` |  |
| `b` | `UnityEngine.Vector2` |  |

**Returns:** `UnityEngine.Matrix4x4`

:::

::: details `DecrementBlockCounters(BlockedAction, bool)`

```csharp
public void DecrementBlockCounters(Channel.BlockedAction action, bool delayOneFrame = true)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `action` | [`Channel.BlockedAction`](/api/Global.Channel) |  |
| `delayOneFrame` | `bool` |  |

:::

::: details `DisobeyBlock(BlockableAction)`

Disobey blocks for certain action, canceling related channels.

```csharp
public void DisobeyBlock(EntityControl.BlockableAction action)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `action` | [`EntityControl.BlockableAction`](/api/Global.EntityControl) |  |

:::

::: details `FrameUpdate()`

```csharp
public override void FrameUpdate()
```

:::

::: details `GetPointOnBezierCurve(Vector2, Vector2, Vector2, Vector2, float)`

```csharp
public static Vector2 GetPointOnBezierCurve(Vector2 p0, Vector2 p1, Vector2 p2, Vector2 p3, float t)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `p0` | `UnityEngine.Vector2` |  |
| `p1` | `UnityEngine.Vector2` |  |
| `p2` | `UnityEngine.Vector2` |  |
| `p3` | `UnityEngine.Vector2` |  |
| `t` | `float` |  |

**Returns:** `UnityEngine.Vector2`

:::

::: details `IncrementBlockCounters(BlockedAction)`

```csharp
public void IncrementBlockCounters(Channel.BlockedAction action)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `action` | [`Channel.BlockedAction`](/api/Global.Channel) |  |

:::

::: details `Interact(IInteractable, bool, bool)`

```csharp
public void Interact(IInteractable interactable, bool isAlt, bool isMouse)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `interactable` | [`IInteractable`](/api/Global.IInteractable) |  |
| `isAlt` | `bool` |  |
| `isMouse` | `bool` |  |

:::

::: details `IsActionBlocked(BlockableAction)`

Is the entity allowed to do a certain action? If not, the action will be postponed until the block is resolved.Available everywhere.

```csharp
public EntityControl.BlockStatus IsActionBlocked(EntityControl.BlockableAction action)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `action` | [`EntityControl.BlockableAction`](/api/Global.EntityControl) |  |

**Returns:** `EntityControl.BlockStatus`

:::

::: details `LockGamepadRotation()`

Lock gamepad look rotation of this entity. You must call UnlockLookRotation afterwards.

```csharp
public void LockGamepadRotation()
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

::: details `MoveToDestination(Vector3, bool, float)`

```csharp
public void MoveToDestination(Vector3 destination, bool immediately, float speedMult = 1)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `destination` | `UnityEngine.Vector3` |  |
| `immediately` | `bool` |  |
| `speedMult` | `float` |  |

:::

::: details `OnCleanup()`

```csharp
public void OnCleanup()
```

:::

::: details `OnStart()`

```csharp
public override void OnStart()
```

:::

::: details `OnStartClient()`

```csharp
public override void OnStartClient()
```

:::

::: details `OnStartServer()`

```csharp
public override void OnStartServer()
```

:::

::: details `OnStop()`

```csharp
public override void OnStop()
```

:::

::: details `OnStopServer()`

```csharp
public override void OnStopServer()
```

:::

::: details `Rotate(float, bool, float)`

```csharp
public void Rotate(float angle, bool immediately, float overrideDuration = -1)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `angle` | `float` |  |
| `immediately` | `bool` |  |
| `overrideDuration` | `float` |  |

:::

::: details `Rotate(Quaternion, bool, float)`

```csharp
public void Rotate(Quaternion rotation, bool immediately, float overrideDuration = -1)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `rotation` | `UnityEngine.Quaternion` |  |
| `immediately` | `bool` |  |
| `overrideDuration` | `float` |  |

:::

::: details `Rotate(Vector3, bool, float)`

```csharp
public void Rotate(Vector3 forward, bool immediately, float overrideDuration = -1)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `forward` | `UnityEngine.Vector3` |  |
| `immediately` | `bool` |  |
| `overrideDuration` | `float` |  |

:::

::: details `RotateTowards(Entity, bool, float)`

```csharp
public void RotateTowards(Entity ent, bool immediately, float overrideDuration = -1)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `ent` | [`Entity`](/api/Global.Entity) |  |
| `immediately` | `bool` |  |
| `overrideDuration` | `float` |  |

:::

::: details `RotateTowards(Vector3, bool, float)`

```csharp
public void RotateTowards(Vector3 position, bool immediately, float overrideDuration = -1)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `position` | `UnityEngine.Vector3` |  |
| `immediately` | `bool` |  |
| `overrideDuration` | `float` |  |

:::

::: details `SetAgentDestination(Vector3, bool)`

```csharp
public void SetAgentDestination(Vector3 destination, bool important)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `destination` | `UnityEngine.Vector3` |  |
| `important` | `bool` |  |

:::

::: details `SetAgentPosition(Vector3)`

Can be called on local movement processor.

```csharp
public void SetAgentPosition(Vector3 position)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `position` | `UnityEngine.Vector3` |  |

:::

::: details `StartChannel(Channel)`

```csharp
public Channel StartChannel(Channel channel)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `channel` | [`Channel`](/api/Global.Channel) |  |

**Returns:** `Channel`

:::

::: details `StartDaze(float)`

```csharp
public Channel StartDaze(float duration)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `duration` | `float` |  |

**Returns:** `Channel`

:::

::: details `StartDisplacement(Displacement)`

```csharp
public void StartDisplacement(Displacement disp)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `disp` | [`Displacement`](/api/Global.Displacement) |  |

:::

::: details `Stop()`

```csharp
public void Stop()
```

:::

::: details `StopOverrideRotation()`

Unlock override rotation.

```csharp
public void StopOverrideRotation()
```

:::

::: details `Teleport(Vector3)`

Teleport this entity to the targeted position.You should only feed in a valid position by usingDew.GetValidAgentPosition()beforehand.

```csharp
public void Teleport(Vector3 position)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `position` | `UnityEngine.Vector3` |  |

:::

::: details `TransformPoint(Vector2, Matrix4x4)`

```csharp
public static Vector2 TransformPoint(Vector2 point, Matrix4x4 transform)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `point` | `UnityEngine.Vector2` |  |
| `transform` | `UnityEngine.Matrix4x4` |  |

**Returns:** `UnityEngine.Vector2`

:::

::: details `UnlockGamepadRotation()`

Unlock gamepad look rotation of this entity.

```csharp
public void UnlockGamepadRotation()
```

:::

::: details `UpdateLastMoveTime()`

```csharp
public void UpdateLastMoveTime()
```

:::


## Architecture & Relationships

::: details Click to expand Architecture & Relationships

### Used By (244)

*Classes and systems that invoke, reference, or depend on `EntityControl`:*

[AbilitySelfValidator](/api/Global.AbilitySelfValidator) · [AbilityTrigger](/api/Global.AbilityTrigger) · [ActionAttackMove](/api/Global.ActionAttackMove) · [ActionCast](/api/Global.ActionCast) · [ActionInteract](/api/Global.ActionInteract) · [Actor](/api/Global.Actor) · [ActorManager](/api/Global.ActorManager) · `Ai_Ai_Mon_Ink_BossWhiteNight_OneInchPunch_Atk` · `Ai_ArcticTerritory` · `Ai_C_BeamOfLight` · `Ai_C_DarkSpear` · `Ai_C_MassProtection` · `Ai_C_PressurePoint` · `Ai_C_Whirlwind` · `Ai_D_BurningFist_Attack` · `Ai_D_ParryMaster_Parry` · `Ai_D_Resolve_Push` · `Ai_D_ScarOfTheWind_DashAtk` · `Ai_E_Blink_Back` · `Ai_E_FlameJet` · `Ai_E_StygianRush_Rush` · `Ai_EmbraceNewIdentity` · `Ai_Gem_U_LastStarlight` · `Ai_GenericDodge` · `Ai_MirageSkin_Pulverization_Stomp` · `Ai_Mon_Despair_BossAzurak_Roll` · `Ai_Mon_Despair_BossAzurak_StompBlock` · `Ai_Mon_Despair_Displacer_Blink` · `Ai_Mon_Despair_DreadBug_Jump` · `Ai_Mon_Despair_DreadBug_JumpBack` · `Ai_Mon_Forest_BossDemon_AltSkill_LineAtk_Spawner` · `Ai_Mon_Forest_BossDemon_AltSkill_Stomp` · `Ai_Mon_Forest_BossDemon_Blink` · `Ai_Mon_Forest_BossDemon_DelayedAtk` · `Ai_Mon_Forest_Hound_Charge` · `Ai_Mon_Forest_SpiderSpitter_Backdash` · `Ai_Mon_Forest_SpiderWarrior_Jump` · `Ai_Mon_Ink_BossDarkMoon_Blade` · `Ai_Mon_Ink_BossDarkMoon_Eclipse` · `Ai_Mon_Ink_BossDarkMoon_ShortDash` · `Ai_Mon_Ink_BossDarkMoon_ThrowSpear_TeleportAtk` · `Ai_Mon_Ink_BossWhiteNight_AltAtk_Ready` · `Ai_Mon_Ink_BossWhiteNight_Cataclysm` · `Ai_Mon_Ink_BossWhiteNight_DestructionWave_Wave` · `Ai_Mon_Ink_BossWhiteNight_Oppression` · `Ai_Mon_Ink_GhostBlade_SwiftStep` · `Ai_Mon_LavaLand_BossInfernus_BreathFire` · `Ai_Mon_LavaLand_BossInfernus_Jump` · `Ai_Mon_LavaLand_BossInfernus_PowerBomb` · `Ai_Mon_LavaLand_BossInfernus_WallStunKnockback` · `Ai_Mon_LavaLand_FireElemental_BackDash` · `Ai_Mon_LavaLand_FireElemental_Destruct` · `Ai_Mon_Primus_BossPrimusAeron_Adapt_Arbalest` · `Ai_Mon_Primus_BossPrimusAeron_Adapt_IceClaw` · `Ai_Mon_Primus_BossPrimusAeron_Adapt_SmiteStorm` · `Ai_Mon_Primus_BossPrimusAeron_Dash` · `Ai_Mon_Primus_BossPrimusAeron_Force_Grab` · `Ai_Mon_Sky_Baam_Teleport` · `Ai_Mon_Sky_BigBaam_BeamAtk` · `Ai_Mon_Sky_BossNyx_Blackhole` · `Ai_Mon_Sky_BossNyx_PullAtk_AfterAtk` · `Ai_Mon_SnowMountain_BossSkoll_Atk` · `Ai_Mon_SnowMountain_BossSkoll_AuraBladeRain` · `Ai_Mon_SnowMountain_BossSkoll_AuraExplosion_Spawner` · `Ai_Mon_SnowMountain_BossSkoll_AuraSlice` · `Ai_Mon_SnowMountain_BossSkoll_Capture` · `Ai_Mon_SnowMountain_BossSkoll_DeathFromAbove` · `Ai_Mon_SnowMountain_BossSkoll_Whirlwind` · `Ai_Mon_SnowMountain_IceElemental_IceBreaker_SubExplosion` · `Ai_Mon_SnowMountain_Scavenger_Jump` · `Ai_Mon_Special_AmbushSpawner_Projectile` · `Ai_Mon_Special_BossErebos_SpawnBlackhole_Instance` · `Ai_Mon_Special_BossErebos_StarRain_Spawner` · `Ai_Mon_Special_BossMaw_ChainReaction` · `Ai_Mon_Special_BossMaw_Chomp_Charge` · `Ai_Mon_Special_BossMaw_DarkSpear` · `Ai_Mon_Special_BossMaw_PrecisionShot` · `Ai_Mon_Special_BossMaw_ScatterShot_Spawner` · `Ai_Mon_Special_BossMaw_SliceThroat` · `Ai_Mon_Special_BossMaw_SliceThroat_Atk` · `Ai_Mon_Special_BossObliviax_BackStep` · `Ai_Mon_Special_BossObliviax_ChargeSequence_Ready` · `Ai_Mon_Special_BossObliviax_DashAtk` · `Ai_Mon_Special_BossObliviax_NeedleAtk_Ready` · `Ai_Mon_Special_BossPolaris_Monster_Atk_FirstAtk` · `Ai_Mon_Special_BossPolaris_Monster_Atk_SecondAtk` · `Ai_Mon_Special_BossPolaris_Monster_Atk_Spawner` · `Ai_Mon_Special_BossPolaris_Monster_Dash` · `Ai_Mon_Special_BossPolaris_Monster_JumpStomp` · `Ai_Mon_Special_BossPolaris_Monster_PizzaLightning_Spawner` · `Ai_Q_BigBorealChunk_Spawner` · `Ai_Q_CruelSun` · `Ai_Q_Fleche_Dash` · `Ai_Q_HandCannon` · `Ai_Q_Laceration_Circle` · `Ai_Q_Lunge` · `Ai_Q_MoonlightPact` · `Ai_Q_SuperNova` · `Ai_R_BackOff_Spawner` · `Ai_R_BaptismOfSun` · `Ai_R_Chomp` · `Ai_R_FrozenFists_PunchDash` · `Ai_R_GlacialHammer` · `Ai_R_NaturesWhisper` · `Ai_R_Parry_Projectile` · `Ai_R_RepulsiveShield_Projectile` · `Ai_R_Somersault` · `Ai_R_StaticDischarge` · `Ai_Sky_BossIntruder_Instance` · `Ai_Star_Bismuth_F_IT_SmallerRingAddDisplacement_Dash` · `Ai_U_Burrow_Emerge` · `Ai_U_ShoutOfOblivion` · `Ai_U_WorldCracker` · `Ai_UnstableRatSwarm_Projectile` · `At_Mon_Forest_BossDemon_Spawn` · `At_Mon_Primus_BossPrimusAeron_Rage_MassDelusion` · `At_Mon_Special_BossMaw_Purgatory` · `At_Mon_Special_BossObliviax_Artillery` · `At_Mon_Special_BossObliviax_NeedleAtk` · `At_Mon_Special_BossPolaris_Holy_GoldenSpear` · `At_Mon_Special_BossPolaris_Holy_SelfCleanse` · [AttackTrigger](/api/Global.AttackTrigger) · [Channel](/api/Global.Channel) · [ChargingChannel](/api/Global.ChargingChannel) · [ConsoleManager](/api/Global.ConsoleManager) · [ControlManager](/api/Global.ControlManager) · [Dash](/api/Global.Dash) · [Dew](/api/Global.Dew) · [DewCutsceneDirector](/api/Global.DewCutsceneDirector) · [DewHeroesTeleporter](/api/Global.DewHeroesTeleporter) · [DewNetworkManager](/api/Global.DewNetworkManager) · [DewPhysics](/api/Global.DewPhysics) · [EditSkillShrine](/api/Global.EditSkillShrine) · [Entity](/api/Global.Entity) · [EntityAI](/api/Global.EntityAI) · [EntityAnimation](/api/Global.EntityAnimation) · [EntityGroundMarker](/api/Global.EntityGroundMarker) · [EntitySound](/api/Global.EntitySound) · [EntityStatus](/api/Global.EntityStatus) · [EntityVisual](/api/Global.EntityVisual) · [FlavourManager](/api/Global.FlavourManager) · [FxAttachToEntity](/api/Global.FxAttachToEntity) · [FxCastTelegraph](/api/Global.FxCastTelegraph) · `GameMod_DespairFixStuck` · `Gem_C_Confidence` · `Gem_L_Paranoia` · `Gem_R_Accuracy` · [Hero](/api/Global.Hero) · `Hero_Bismuth_BookController` · [ISpawnableAsMiniBoss](/api/Global.ISpawnableAsMiniBoss) · [Knockback](/api/Global.Knockback) · `LavaLand_IcePlace` · `LavaLand_Lava` · `Mon_DarkCave_NightOlm` · `Mon_Despair_AzurakMonsterSpawner` · `Mon_Despair_DreadBug` · `Mon_Despair_UnstableRat` · [Mon_DreamTeller](/api/Global.Mon_DreamTeller) · `Mon_GoldenLizard_ElusiveLizard` · `Mon_Ink_Archer` · `Mon_Ink_BossDarkMoon` · `Mon_Ink_BossWhiteNight` · `Mon_Ink_EgoSword` · `Mon_LavaLand_FireElemental` · `Mon_Primus_BossPrimusAeron` · [Mon_RedGiant](/api/Global.Mon_RedGiant) · `Mon_Sky_Baam` · `Mon_Sky_BigBaam_Base` · `Mon_Sky_BossNyx` · `Mon_SnowMountain_LivingShards` · `Mon_Special_BossPolaris` · `Primus_Ending` · [PropEnt_Merchant_Base](/api/Global.PropEnt_Merchant_Base) · [PropEnt_Merchant_Smoothie](/api/Global.PropEnt_Merchant_Smoothie) · `PropEnt_Sky_Orca` · `RoomMod_Hunted` · `RoomMod_LeafPuppies` · `RoomMod_MeteoricLife` · [RoomMonsters](/api/Global.RoomMonsters) · `Se_AcceleratedTime` · `Se_BarrierPassThrough` · `Se_E_VileStrike` · `Se_EngulfedInFlame` · `Se_FatalHitProtection_Invulnerable` · `Se_GravityTraining` · `Se_HarmlessWhispers` · `Se_HeroKnockedOut` · `Se_HunterBuff` · `Se_InConversation` · `Se_L_PyranasFireball` · `Se_M_Charge` · `Se_MiniBoss_IceAura` · `Se_MiniBoss_SpinningArrow` · `Se_MiniBoss_UnstableExplosive_Explosion` · `Se_MirageSkin_Pulverization` · `Se_Mon_DarkCave_BossSeeker_Blink` · `Se_Mon_DarkCave_BossSeeker_Hallucination_Disappear` · `Se_Mon_DarkCave_BossSeeker_Substitution` · `Se_Mon_DarkCave_BossSeeker_TunnelVision` · `Se_Mon_DarkCave_BossSeeker_TunnelVision_Disappear` · `Se_Mon_DarkCave_DarkElemental_Teleport` · `Se_Mon_Ink_BossWhiteNight_Cataclysm` · `Se_Mon_Ink_BossWhiteNight_Rush` · `Se_Mon_LavaLand_BossInfernus_Jump_Invul` · `Se_Mon_Polaris_Blink` · `Se_Mon_Primus_BossPrimusAeron_Adapt_Doom_Initial` · `Se_Mon_Primus_BossPrimusAeron_Adapt_Doom_Ongoing` · `Se_Mon_Primus_BossPrimusAeron_Force_GoldRain` · `Se_Mon_Sky_BossNyx_StarBuff` · `Se_Mon_SnowMountain_BossSkoll_DeathFromAbove_Invulnerable` · `Se_Mon_SnowMountain_SnowWolf_SlowApproach` · `Se_Mon_Special_BossPolaris_Holy_CounterSpell` · `Se_Mon_Special_BossPolaris_Holy_Dash` · `Se_ObliviaxKidnap` · `Se_PortalTransition` · `Se_Q_Discipline_Jump` · `Se_R_BoneCrusher` · `Se_R_BoneCrusher_Kidnapped` · `Se_R_LightningDance` · `Se_R_Parry_Start` · `Se_R_RepulsiveShield` · `Se_R_SerpentineBlessing_Buff` · `Se_R_ShadowOverdrive_Initial` · `Se_R_UnbreakableDetermination` · `Se_RoomMod_WarpingField_Unstable` · `Se_RoomMod_WarpingField_Warp` · `Se_Star_Bismuth_L_ContinuousSpeed` · `Se_Star_Husk_I_ShopIntimidation` · `Se_Treasure_FragmentOfDetermination_Invulnerable` · `Se_U_BeamOfBalance` · `Se_U_HerWorld_Blackhole` · `Se_U_Hysteria` · `Se_WaypointTeleport` · `Shrine_HeroSoul` · `Sky_LightFogDamager` · [SpawnManager](/api/Global.SpawnManager) · `StarlessPath_BossPolarisManager` · `Sum_L_SmallMoltenCore_Dragon` · `Sum_R_AnnoyingBanner` · [Summon](/api/Global.Summon) · [TriggerConfig](/api/Global.TriggerConfig) · `UI_ControllerDisconnectedIndicator` · `UI_Dev_ConsoleSelectedEntityInfo` · `UI_EntityCrowdControl`

### Dependencies (39)

*Types and components that `EntityControl` references or depends upon:*

[AbilityTrigger](/api/Global.AbilityTrigger) · [ActionBase](/api/Global.ActionBase) · [Actor](/api/Global.Actor) · [ActorCheck](/api/Global.ActorCheck) · [CameraManager](/api/Global.CameraManager) · [CastInfo](/api/Global.CastInfo) · [Channel](/api/Global.Channel) · [ControlManager](/api/Global.ControlManager) · [Dew](/api/Global.Dew) · [DewNetworkBehaviour](/api/Global.DewNetworkBehaviour) · [DewPhysics](/api/Global.DewPhysics) · [DewPlayer](/api/Global.DewPlayer) · [Displacement](/api/Global.Displacement) · [EaseFunction](/api/Global.EaseFunction) · [EasingFunction](/api/Global.EasingFunction) · [Entity](/api/Global.Entity) · [EntityAbility](/api/Global.EntityAbility) · [EntityCheck](/api/Global.EntityCheck) · [EntityComponent](/api/Global.EntityComponent) · [EntityStatus](/api/Global.EntityStatus) · [EntityVisual](/api/Global.EntityVisual) · [EventInfoKill](/api/Global.EventInfoKill) · [Hero](/api/Global.Hero) · [ICleanup](/api/Global.ICleanup) · [IInteractable](/api/Global.IInteractable) · [ListReturnHandle`1](/api/Global.ListReturnHandle`1) · [ManagerBase`1](/api/Global.ManagerBase`1) · `NetworkReaderWriterExtensions` · [NetworkedManagerBase`1](/api/Global.NetworkedManagerBase`1) · [ProxyCollider](/api/Global.ProxyCollider) · [SafeAction`1](/api/Global.SafeAction`1) · [SafeAction`2](/api/Global.SafeAction`2) · [TransitionManager](/api/Global.TransitionManager) · [TriggerConfig](/api/Global.TriggerConfig) · `Vector3FlattenExtension` · `Vector3IsNanExtension` · `VectorPlaneTransformExtension` · [ZoneManager](/api/Global.ZoneManager) · `Mirror.GeneratedNetworkCode`

:::
