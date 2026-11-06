# Class: EntityControl

- **Category:** <span class="cat-dot" style="--cat-color: #ef4444" data-cat="Combat & Abilities"></span> Combat & Abilities
- **Namespace:** `Global`
- **Assembly:** `Dew.Core.dll`
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
