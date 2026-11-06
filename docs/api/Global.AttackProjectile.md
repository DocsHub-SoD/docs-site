# Class: AttackProjectile

- **Category:** <span class="cat-dot" style="--cat-color: #ef4444" data-cat="Combat & Abilities"></span> Combat & Abilities
- **Namespace:** `Global`
- **Assembly:** `Dew.Core.dll`
- **Inheritance / Derived:** [DewNetworkBehaviour](/api/Global.DewNetworkBehaviour) → [Actor](/api/Global.Actor) → [AbilityInstance](/api/Global.AbilityInstance) → [Projectile](/api/Global.Projectile) → [StandardProjectile](/api/Global.StandardProjectile)

```csharp
public class AttackProjectile : StandardProjectile, ILogicUpdate, ICleanup, ICustomDestroyRoutine
```

## Fields

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`isCrit`** | `public bool isCrit` |  |
| **`isMain`** | `[NonSerialized] public bool isMain` |  |
| **`strength`** | `public float strength` |  |

## Methods

### `OnCreate()`

```csharp
protected override void OnCreate()
```

### `OnEntity(EntityHit)`

```csharp
protected override void OnEntity(Projectile.EntityHit hit)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `hit` | [`Projectile.EntityHit`](/api/Global.Projectile) |  |

### `OnPrepare()`

```csharp
protected override void OnPrepare()
```
