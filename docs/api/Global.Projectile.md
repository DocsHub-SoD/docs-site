# Class: Projectile

- **Category:** <span class="cat-dot" style="--cat-color: #ef4444" data-cat="Combat & Abilities"></span> Combat & Abilities
- **Namespace:** `Global`
- **Assembly:** `Dew.Core.dll`
- **Inheritance / Derived:** [DewNetworkBehaviour](/api/Global.DewNetworkBehaviour) → [Actor](/api/Global.Actor) → [AbilityInstance](/api/Global.AbilityInstance) → [StandardProjectile](/api/Global.StandardProjectile)

```csharp
public abstract class Projectile : AbilityInstance, ILogicUpdate, ICleanup, ICustomDestroyRoutine
```

## Fields

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`_estimatedVelocity`** | `protected Vector3 _estimatedVelocity` |  |
| **`canCollideMidFlight`** | `[BoxGroup("Projectile Settings", true, false, 0)] [LabelText("Can Collide With Entity Mid-Flight")] [ToggleLeft] public bool canCollideMidFlight` |  |
| **`collisionRadius`** | `[Title("Collisions", null, TitleAlignments.Left, true, true)] [BoxGroup("Projectile Settings", true, false, 0)] public float collisionRadius` |  |
| **`collisionTargets`** | `[ShowIf("canCollideMidFlight", true)] [BoxGroup("Projectile Settings", true, false, 0)] public AbilityTargetValidator collisionTargets` |  |
| **`customEndHeight`** | `[ShowIf("@mode != Projectile.ProjectileMode.Target && !endsWithSameHeight", true)] [BoxGroup("Projectile Settings", true, false, 0)] public float customEndHeight` |  |
| **`destroyOnComplete`** | `[FormerlySerializedAs("killOnComplete")] [BoxGroup("Projectile Settings", true, false, 0)] public bool destroyOnComplete` |  |
| **`dissipateOnTerrain`** | `[BoxGroup("Projectile Settings", true, false, 0)] [ToggleLeft] public bool dissipateOnTerrain` |  |
| **`effectOnComplete`** | `[BoxGroup("Projectile Settings", true, false, 0)] [LabelText("Complete")] public GameObject effectOnComplete` |  |
| **`effectOnDissipate`** | `[BoxGroup("Projectile Settings", true, false, 0)] [LabelText("Dissipate")] public GameObject effectOnDissipate` |  |
| **`effectOnEntity`** | `[BoxGroup("Projectile Settings", true, false, 0)] [LabelText("Entity")] public GameObject effectOnEntity` |  |
| **`effectOnFly`** | `[Title("Effects", null, TitleAlignments.Left, true, true)] [BoxGroup("Projectile Settings", true, false, 0)] [LabelText("Fly")] public GameObject effectOnFly` |  |
| **`endDistance`** | `[ShowIf("@mode == Projectile.ProjectileMode.Direction", true)] [BoxGroup("Projectile Settings", true, false, 0)] public float endDistance` |  |
| **`endsWithSameHeight`** | `[ShowIf("@mode != Projectile.ProjectileMode.Target", true)] [BoxGroup("Projectile Settings", true, false, 0)] public bool endsWithSameHeight` |  |
| **`horizontalOffsetOverTrajectory`** | `[LabelText("Horizontal Offset")] [BoxGroup("Projectile Settings", true, false, 0)] public AnimationCurve horizontalOffsetOverTrajectory` |  |
| **`killOnDissipate`** | `[BoxGroup("Projectile Settings", true, false, 0)] public bool killOnDissipate` |  |
| **`mode`** | `[Title("Flight", null, TitleAlignments.Left, true, true)] [EnumToggleButtons] [BoxGroup("Projectile Settings", true, false, 0)] public Projectile.ProjectileMode mode` |  |
| **`onEntity`** | `public SafeAction<Projectile.EntityHit> onEntity` |  |
| **`rotationType`** | `[LabelText("Rotation")] [EnumToggleButtons] [BoxGroup("Projectile Settings", true, false, 0)] public Projectile.RotationType rotationType` |  |
| **`scaleHorizontalOffsetOnLength`** | `[LabelText("Scale On Trajectory Length")] [BoxGroup("Projectile Settings", true, false, 0)] public bool scaleHorizontalOffsetOnLength` |  |
| **`scaleVerticalOffsetOnLength`** | `[LabelText("Scale On Trajectory Length")] [BoxGroup("Projectile Settings", true, false, 0)] public bool scaleVerticalOffsetOnLength` |  |
| **`start`** | `[EnumToggleButtons] [BoxGroup("Projectile Settings", true, false, 0)] public Projectile.StartPositionType start` |  |
| **`startInFrontDistance`** | `[LabelText("Front Distance")] [BoxGroup("Projectile Settings", true, false, 0)] public float startInFrontDistance` |  |
| **`verticalOffsetOverTrajectory`** | `[LabelText("Vertical Offset")] [BoxGroup("Projectile Settings", true, false, 0)] public AnimationCurve verticalOffsetOverTrajectory` |  |

## Properties

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`isCompleted`** | `public bool isCompleted { get; }` | Did this projectile complete its course? |
| **`isFlying`** | `public bool isFlying { get; }` | Is this projectile still flying over its course? |
| **`targetEntity`** | `protected Entity targetEntity { get; }` |  |
| **`targetPosition`** | `protected Vector3 targetPosition { get; set; }` | It is recommended to edit this only in OnPrepare. |

## Methods

### `AddEffect(AddEffectTarget, GameObject)`

Locally add an effect.Given effect will be instantiated and set/added to this projectile.

```csharp
public void AddEffect(Projectile.AddEffectTarget target, GameObject eff)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `target` | [`Projectile.AddEffectTarget`](/api/Global.Projectile) |  |
| `eff` | `UnityEngine.GameObject` |  |

### `CalculateOffsetOverTrajectoryInWorldSpace(float, Quaternion)`

```csharp
protected Vector3 CalculateOffsetOverTrajectoryInWorldSpace(float normalizedPosition, Quaternion rotation)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `normalizedPosition` | `float` |  |
| `rotation` | `UnityEngine.Quaternion` |  |

**Returns:** `UnityEngine.Vector3`

### `CheckForCompletion()`

```csharp
protected virtual bool CheckForCompletion()
```

**Returns:** `bool`

### `Dissipate()`

Dissipate this projectile.

```csharp
public void Dissipate()
```

### `FrameUpdate()`

```csharp
public override void FrameUpdate()
```

### `GetTargetWorldPosition()`

```csharp
protected virtual Vector3 GetTargetWorldPosition()
```

**Returns:** `UnityEngine.Vector3`

### `LogicUpdate(float)`

```csharp
public override void LogicUpdate(float dt)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `dt` | `float` |  |

### `OnComplete()`

Called on server when this Projectile fully completes its path without being despawned by itself/dissipated.Default behaviour instantiates a neweffectOnCompleteeffect using the position and rotation of this projectile on every clients, and stopseffectOnFlyeffect.It will also kill this projectile ifkillOnCompleteis set.Note: On targeted projectiles, normallyOnEntitywill be fired beforeOnComplete. It might fire differently if for example the projectile is detached or the target became an invalid target.

```csharp
protected virtual void OnComplete()
```

### `OnCreate()`

```csharp
protected override void OnCreate()
```

### `OnDestroyActor()`

```csharp
protected override void OnDestroyActor()
```

### `OnDisable()`

```csharp
protected override void OnDisable()
```

### `OnDissipate()`

Called on server when this Projectile is dissipated by an outer source. e.g. Projectile Absorbing WallDefault behaviour instantiates a neweffectOnDissipateeffect using the position and rotation of this projectile on every clients

```csharp
protected virtual void OnDissipate()
```

### `OnEntity(EntityHit)`

Called on server when this Projectile in server detects a collision with an Entity.Default behaviour instantiates a neweffectOnEntityeffect at the hit point with the rotation of this projectile attached to the entity on every clients.

```csharp
protected virtual void OnEntity(Projectile.EntityHit hit)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `hit` | [`Projectile.EntityHit`](/api/Global.Projectile) |  |

### `OnPrepare()`

```csharp
protected override void OnPrepare()
```

### `OnStartServer()`

```csharp
public override void OnStartServer()
```

### `PositionSolver(float)`

```csharp
protected abstract Vector3 PositionSolver(float dt)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `dt` | `float` |  |

**Returns:** `UnityEngine.Vector3`

### `RotationSolver(float)`

```csharp
protected virtual Quaternion RotationSolver(float dt)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `dt` | `float` |  |

**Returns:** `UnityEngine.Quaternion`

### `SetCustomStartPosition(Vector3)`

Set custom start position for projectiles with 'Custom' start position mode. Call this in OnPrepare.

```csharp
public void SetCustomStartPosition(Vector3 pos)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `pos` | `UnityEngine.Vector3` |  |

### `StopFlying()`

Stop this projectile and itseffectOnFlyeffect. This will also make this projectile instantly stop checking collisions. Note that this does not callOnCompletenorOnDissipate.

```csharp
protected void StopFlying()
```
