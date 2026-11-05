# Class: DewPhysics

- **Namespace:** `Global`
- **Assembly:** `Dew.Core.dll`

```csharp
public static class DewPhysics
```

## Methods

### `OverlapCircleAllEntities(out ListReturnHandle&lt;Entity&gt;, Vector3, float, CollisionCheckSettings)`

```csharp
public static List<Entity> OverlapCircleAllEntities(out ListReturnHandle<Entity> handle, Vector3 center, float radius, CollisionCheckSettings settings = default)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `handle` | `ListReturnHandle&lt;Entity&gt;` |  |
| `center` | `UnityEngine.Vector3` |  |
| `radius` | `float` |  |
| `settings` | [CollisionCheckSettings](/api/Global.CollisionCheckSettings) |  |

**Returns:** `System.Collections.Generic.List&lt;T&gt;&lt;Entity&gt;`

### `OverlapCircleAllEntities(out ListReturnHandle&lt;Entity&gt;, Vector3, float, IBinaryEntityValidator, Entity, CollisionCheckSettings)`

```csharp
public static List<Entity> OverlapCircleAllEntities(out ListReturnHandle<Entity> handle, Vector3 center, float radius, IBinaryEntityValidator validator, Entity self, CollisionCheckSettings settings = default)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `handle` | `ListReturnHandle&lt;Entity&gt;` |  |
| `center` | `UnityEngine.Vector3` |  |
| `radius` | `float` |  |
| `validator` | [IBinaryEntityValidator](/api/Global.IBinaryEntityValidator) |  |
| `self` | [Entity](/api/Global.Entity) |  |
| `settings` | [CollisionCheckSettings](/api/Global.CollisionCheckSettings) |  |

**Returns:** `System.Collections.Generic.List&lt;T&gt;&lt;Entity&gt;`

### `OverlapCircleAllEntities(out ListReturnHandle&lt;Entity&gt;, Vector3, float, IEntityValidator, CollisionCheckSettings)`

```csharp
public static List<Entity> OverlapCircleAllEntities(out ListReturnHandle<Entity> handle, Vector3 center, float radius, IEntityValidator validator, CollisionCheckSettings settings = default)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `handle` | `ListReturnHandle&lt;Entity&gt;` |  |
| `center` | `UnityEngine.Vector3` |  |
| `radius` | `float` |  |
| `validator` | [IEntityValidator](/api/Global.IEntityValidator) |  |
| `settings` | [CollisionCheckSettings](/api/Global.CollisionCheckSettings) |  |

**Returns:** `System.Collections.Generic.List&lt;T&gt;&lt;Entity&gt;`

### `OverlapCircleAllEntities(out ListReturnHandle&lt;Entity&gt;, Vector3, float, Func&lt;Entity, bool&gt;, CollisionCheckSettings)`

```csharp
public static List<Entity> OverlapCircleAllEntities(out ListReturnHandle<Entity> handle, Vector3 center, float radius, Func<Entity, bool> validator, CollisionCheckSettings settings = default)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `handle` | `ListReturnHandle&lt;Entity&gt;` |  |
| `center` | `UnityEngine.Vector3` |  |
| `radius` | `float` |  |
| `validator` | [System.Func&lt;T, TResult&gt;&lt;Entity,bool&gt;](/api/Global.Entity) |  |
| `settings` | [CollisionCheckSettings](/api/Global.CollisionCheckSettings) |  |

**Returns:** `System.Collections.Generic.List&lt;T&gt;&lt;Entity&gt;`

### `SphereCastAllEntities(out ListReturnHandle&lt;Entity&gt;, Vector3, float, Vector3, float, CollisionCheckSettings)`

```csharp
public static List<Entity> SphereCastAllEntities(out ListReturnHandle<Entity> handle, Vector3 origin, float radius, Vector3 direction, float maxDistance, CollisionCheckSettings settings = default)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `handle` | `ListReturnHandle&lt;Entity&gt;` |  |
| `origin` | `UnityEngine.Vector3` |  |
| `radius` | `float` |  |
| `direction` | `UnityEngine.Vector3` |  |
| `maxDistance` | `float` |  |
| `settings` | [CollisionCheckSettings](/api/Global.CollisionCheckSettings) |  |

**Returns:** `System.Collections.Generic.List&lt;T&gt;&lt;Entity&gt;`

### `SphereCastAllEntities(out ListReturnHandle&lt;Entity&gt;, Vector3, float, Vector3, float, IBinaryEntityValidator, Entity, CollisionCheckSettings)`

```csharp
public static List<Entity> SphereCastAllEntities(out ListReturnHandle<Entity> handle, Vector3 origin, float radius, Vector3 direction, float maxDistance, IBinaryEntityValidator validator, Entity self, CollisionCheckSettings settings = default)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `handle` | `ListReturnHandle&lt;Entity&gt;` |  |
| `origin` | `UnityEngine.Vector3` |  |
| `radius` | `float` |  |
| `direction` | `UnityEngine.Vector3` |  |
| `maxDistance` | `float` |  |
| `validator` | [IBinaryEntityValidator](/api/Global.IBinaryEntityValidator) |  |
| `self` | [Entity](/api/Global.Entity) |  |
| `settings` | [CollisionCheckSettings](/api/Global.CollisionCheckSettings) |  |

**Returns:** `System.Collections.Generic.List&lt;T&gt;&lt;Entity&gt;`

### `SphereCastAllEntities(out ListReturnHandle&lt;Entity&gt;, Vector3, float, Vector3, float, IEntityValidator, CollisionCheckSettings)`

```csharp
public static List<Entity> SphereCastAllEntities(out ListReturnHandle<Entity> handle, Vector3 origin, float radius, Vector3 direction, float maxDistance, IEntityValidator validator, CollisionCheckSettings settings = default)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `handle` | `ListReturnHandle&lt;Entity&gt;` |  |
| `origin` | `UnityEngine.Vector3` |  |
| `radius` | `float` |  |
| `direction` | `UnityEngine.Vector3` |  |
| `maxDistance` | `float` |  |
| `validator` | [IEntityValidator](/api/Global.IEntityValidator) |  |
| `settings` | [CollisionCheckSettings](/api/Global.CollisionCheckSettings) |  |

**Returns:** `System.Collections.Generic.List&lt;T&gt;&lt;Entity&gt;`

### `SphereCastAllEntities(out ListReturnHandle&lt;Entity&gt;, Vector3, float, Vector3, float, Func&lt;Entity, bool&gt;, CollisionCheckSettings)`

```csharp
public static List<Entity> SphereCastAllEntities(out ListReturnHandle<Entity> handle, Vector3 origin, float radius, Vector3 direction, float maxDistance, Func<Entity, bool> validator, CollisionCheckSettings settings = default)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `handle` | `ListReturnHandle&lt;Entity&gt;` |  |
| `origin` | `UnityEngine.Vector3` |  |
| `radius` | `float` |  |
| `direction` | `UnityEngine.Vector3` |  |
| `maxDistance` | `float` |  |
| `validator` | [System.Func&lt;T, TResult&gt;&lt;Entity,bool&gt;](/api/Global.Entity) |  |
| `settings` | [CollisionCheckSettings](/api/Global.CollisionCheckSettings) |  |

**Returns:** `System.Collections.Generic.List&lt;T&gt;&lt;Entity&gt;`

### `TryGetCollidableWithProjectile(Collider2D, out ICollidableWithProjectile)`

```csharp
public static bool TryGetCollidableWithProjectile(Collider2D collider, out ICollidableWithProjectile collidable)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `collider` | `UnityEngine.Collider2D` |  |
| `collidable` | [ICollidableWithProjectile](/api/Global.ICollidableWithProjectile) |  |

**Returns:** `bool`

### `TryGetEntity(Collider2D, out Entity)`

```csharp
public static bool TryGetEntity(Collider2D collider, out Entity entity)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `collider` | `UnityEngine.Collider2D` |  |
| `entity` | [Entity](/api/Global.Entity) |  |

**Returns:** `bool`

### `TryGetInteractable(Collider2D, out IInteractable)`

```csharp
public static bool TryGetInteractable(Collider2D collider, out IInteractable interactable)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `collider` | `UnityEngine.Collider2D` |  |
| `interactable` | [IInteractable](/api/Global.IInteractable) |  |

**Returns:** `bool`

### `TryGetProxy(Collider2D, out ProxyCollider)`

```csharp
public static bool TryGetProxy(Collider2D collider, out ProxyCollider proxy)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `collider` | `UnityEngine.Collider2D` |  |
| `proxy` | [ProxyCollider](/api/Global.ProxyCollider) |  |

**Returns:** `bool`
