# Class: MeleeAttackInstance

- **Category:** <span class="cat-dot" style="--cat-color: #ef4444" data-cat="Combat & Abilities"></span> Combat & Abilities
- **Namespace:** `Global`
- **Assembly:** `Dew.Core.dll`
- **Inheritance / Derived:** [DewNetworkBehaviour](/api/Global.DewNetworkBehaviour) → [Actor](/api/Global.Actor) → [AbilityInstance](/api/Global.AbilityInstance)

```csharp
public class MeleeAttackInstance : AbilityInstance, ILogicUpdate, ICleanup, ICustomDestroyRoutine
```

## Fields (10)

::: details Click to expand Fields (10)

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`fxHitMain`** | `public GameObject fxHitMain` |  |
| **`fxHitSub`** | `public GameObject fxHitSub` |  |
| **`hitCount`** | `[NonSerialized] public int hitCount` | Available on server. |
| **`isCrit`** | `public bool isCrit` |  |
| **`mainTargetAttackEffect`** | `public float mainTargetAttackEffect` |  |
| **`mainTargetDamage`** | `public float mainTargetDamage` |  |
| **`range`** | `public DewCollider range` |  |
| **`scaleRangeWithTriggerRange`** | `public bool scaleRangeWithTriggerRange` |  |
| **`subTargetAttackEffect`** | `public float subTargetAttackEffect` |  |
| **`subTargetDamage`** | `public float subTargetDamage` |  |

:::

## Properties (1)

::: details Click to expand Properties (1)

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`didHit`** | `public bool didHit { get; }` | Available on server. |

:::

## Methods (1)

::: details `OnCreate()`

```csharp
protected override void OnCreate()
```

:::
