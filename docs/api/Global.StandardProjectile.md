# Class: StandardProjectile

- **Category:** <span class="cat-dot" style="--cat-color: #ef4444" data-cat="Combat & Abilities"></span> Combat & Abilities
- **Namespace:** `Global`
- **Assembly:** `Dew.Core.dll`
- **Inheritance / Derived:** [DewNetworkBehaviour](/api/Global.DewNetworkBehaviour) → [Actor](/api/Global.Actor) → [AbilityInstance](/api/Global.AbilityInstance) → [Projectile](/api/Global.Projectile) → [AttackProjectile](/api/Global.AttackProjectile)

```csharp
public abstract class StandardProjectile : Projectile, ILogicUpdate, ICleanup, ICustomDestroyRoutine
```

## Fields (7)

::: details Click to expand Fields (7)

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`_acceleration`** | `[BoxGroup("Projectile Settings", true, false, 0)] public float _acceleration` |  |
| **`_initialSpeed`** | `[BoxGroup("Projectile Settings", true, false, 0)] public float _initialSpeed` |  |
| **`_targetSpeed`** | `[BoxGroup("Projectile Settings", true, false, 0)] public float _targetSpeed` |  |
| **`enableRandomCurve`** | `[BoxGroup("Projectile Settings", true, false, 0)] [Title("Random Curve", null, TitleAlignments.Left, true, true)] public bool enableRandomCurve` |  |
| **`ensurePositiveY`** | `[BoxGroup("Projectile Settings", true, false, 0)] [ShowIf("enableRandomCurve", true)] public bool ensurePositiveY` |  |
| **`randomCurveMagnitude`** | `[BoxGroup("Projectile Settings", true, false, 0)] [LabelText("Random Magnitude")] [ShowIf("enableRandomCurve", true)] public float randomCurveMagnitude` |  |
| **`use3DVelocity`** | `[Title("Standard Projectile", null, TitleAlignments.Left, true, true)] [LabelText("Use 3D Velocity")] [BoxGroup("Projectile Settings", true, false, 0)] public bool use3DVelocity` |  |

:::

## Properties (4)

::: details Click to expand Properties (4)

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`acceleration`** | `public float acceleration { get; set; }` |  |
| **`initialSpeed`** | `public float initialSpeed { get; set; }` |  |
| **`normalizedPosition`** | `public float normalizedPosition { get; }` | Represents progress of this projectile's trajectory. This value starts from 0 to 1 and never decreases. |
| **`targetSpeed`** | `public float targetSpeed { get; set; }` |  |

:::

## Methods (5)

::: details `ActiveFrameUpdate()`

```csharp
protected override void ActiveFrameUpdate()
```

:::

::: details `CheckForCompletion()`

```csharp
protected override bool CheckForCompletion()
```

**Returns:** `bool`

:::

::: details `OnCreate()`

```csharp
protected override void OnCreate()
```

:::

::: details `OnDisable()`

```csharp
protected override void OnDisable()
```

:::

::: details `PositionSolver(float)`

```csharp
protected override Vector3 PositionSolver(float dt)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `dt` | `float` |  |

**Returns:** `UnityEngine.Vector3`

:::
