# Interface: ICollidableWithProjectile

- **Category:** <span class="cat-dot" style="--cat-color: #ef4444" data-cat="Combat & Abilities"></span> Combat & Abilities
- **Namespace:** `Global`
- **Assembly:** `Dew.Core.dll`

```csharp
public interface ICollidableWithProjectile
```

## Methods (1)

::: details `OnProjectileCollision(CollidableHit)`

```csharp
void OnProjectileCollision(CollidableHit hit)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `hit` | [`CollidableHit`](/api/Global.CollidableHit) |  |

:::


## Architecture & Relationships

::: details Click to expand Architecture & Relationships

### Used By (3)

*Classes and systems that invoke, reference, or depend on `ICollidableWithProjectile`:*

[DewPhysics](/api/Global.DewPhysics) · [Projectile](/api/Global.Projectile) · [ProxyCollider](/api/Global.ProxyCollider)

### Dependencies (1)

*Types and components that `ICollidableWithProjectile` references or depends upon:*

[CollidableHit](/api/Global.CollidableHit)

:::
