# Class: DewCollider

- **Category:** <span class="cat-dot" style="--cat-color: #64748b" data-cat="Misc & Utility"></span> Misc & Utility
- **Namespace:** `Global`
- **Assembly:** `Dew.Core.dll`

```csharp
public class DewCollider : MonoBehaviour
```

## Fields

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`invokeEventsOnClients`** | `[ShowIf("receiveEntityCallbacks", true)] public bool invokeEventsOnClients` |  |
| **`maxDecimals`** | `[ShowIf("@shape == DewCollider.ColliderShape.Polygon", true)] public int maxDecimals` |  |
| **`offset`** | `[ShowIf("@shape == DewCollider.ColliderShape.Box \|\| shape == DewCollider.ColliderShape.Circle", true)] public Vector2 offset` |  |
| **`onEntityEnter`** | `[ShowIf("receiveEntityCallbacks", true)] public UnityEvent<Entity> onEntityEnter` |  |
| **`onEntityExit`** | `[ShowIf("receiveEntityCallbacks", true)] public UnityEvent<Entity> onEntityExit` |  |
| **`points`** | `[ShowIf("@shape == DewCollider.ColliderShape.Polygon", true)] public Vector2[] points` |  |
| **`radius`** | `[ShowIf("@shape == DewCollider.ColliderShape.Circle", true)] public float radius` |  |
| **`receiveEntityCallbacks`** | `public bool receiveEntityCallbacks` |  |
| **`shape`** | `[EnumToggleButtons] public DewCollider.ColliderShape shape` |  |
| **`size`** | `[ShowIf("@shape == DewCollider.ColliderShape.Box", true)] public Vector2 size` |  |

## Methods

### `GeneratePointsInCircle(int, float, float, Vector2[])`

```csharp
public static void GeneratePointsInCircle(int count, float radius, float angle, Vector2[] points)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `count` | `int` |  |
| `radius` | `float` |  |
| `angle` | `float` |  |
| `points` | `UnityEngine.Vector2[]` |  |

### `GeneratePointsInCircle(int, float, float)`

```csharp
public static Vector2[] GeneratePointsInCircle(int count, float radius, float angle)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `count` | `int` |  |
| `radius` | `float` |  |
| `angle` | `float` |  |

**Returns:** `UnityEngine.Vector2[]`

### `GeneratePolygonPoints_Arc(float, float, int)`

```csharp
public void GeneratePolygonPoints_Arc(float arcRadius, float arcAngle, int accuracy = 20)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `arcRadius` | `float` |  |
| `arcAngle` | `float` |  |
| `accuracy` | `int` |  |

### `GeneratePolygonPoints_ArcDonut(float, float, float, int)`

```csharp
public void GeneratePolygonPoints_ArcDonut(float innerRadius, float outerRadius, float arcAngle = 360, int accuracy = 20)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `innerRadius` | `float` |  |
| `outerRadius` | `float` |  |
| `arcAngle` | `float` |  |
| `accuracy` | `int` |  |

### `GeneratePolygonPoints_Circle(float, int)`

```csharp
public void GeneratePolygonPoints_Circle(float circleRadius, int accuracy = 20)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `circleRadius` | `float` |  |
| `accuracy` | `int` |  |

### `GeneratePolygonPoints_Donut(float, float, int)`

```csharp
public void GeneratePolygonPoints_Donut(float innerRadius, float outerRadius, int accuracy = 20)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `innerRadius` | `float` |  |
| `outerRadius` | `float` |  |
| `accuracy` | `int` |  |

### `GetEntities(out ListReturnHandle<Entity>, CollisionCheckSettings)`

```csharp
public List<Entity> GetEntities(out ListReturnHandle<Entity> handle, CollisionCheckSettings settings = default)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `handle` | `ListReturnHandle<Entity>` |  |
| `settings` | [`CollisionCheckSettings`](/api/Global.CollisionCheckSettings) |  |

**Returns:** `System.Collections.Generic.List<T><Entity>`

### `GetEntities(out ListReturnHandle<Entity>, IBinaryEntityValidator, Entity, CollisionCheckSettings)`

```csharp
public List<Entity> GetEntities(out ListReturnHandle<Entity> handle, IBinaryEntityValidator validator, Entity self, CollisionCheckSettings settings = default)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `handle` | `ListReturnHandle<Entity>` |  |
| `validator` | [`IBinaryEntityValidator`](/api/Global.IBinaryEntityValidator) |  |
| `self` | [`Entity`](/api/Global.Entity) |  |
| `settings` | [`CollisionCheckSettings`](/api/Global.CollisionCheckSettings) |  |

**Returns:** `System.Collections.Generic.List<T><Entity>`

### `GetEntities(out ListReturnHandle<Entity>, IEntityValidator, CollisionCheckSettings)`

```csharp
public List<Entity> GetEntities(out ListReturnHandle<Entity> handle, IEntityValidator validator, CollisionCheckSettings settings = default)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `handle` | `ListReturnHandle<Entity>` |  |
| `validator` | [`IEntityValidator`](/api/Global.IEntityValidator) |  |
| `settings` | [`CollisionCheckSettings`](/api/Global.CollisionCheckSettings) |  |

**Returns:** `System.Collections.Generic.List<T><Entity>`

### `GetEntities(out ListReturnHandle<Entity>, Func<Entity, bool>, CollisionCheckSettings)`

```csharp
public List<Entity> GetEntities(out ListReturnHandle<Entity> handle, Func<Entity, bool> validator, CollisionCheckSettings settings = default)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `handle` | `ListReturnHandle<Entity>` |  |
| `validator` | [`System.Func<T, TResult><Entity,bool>`](/api/Global.Entity) |  |
| `settings` | [`CollisionCheckSettings`](/api/Global.CollisionCheckSettings) |  |

**Returns:** `System.Collections.Generic.List<T><Entity>`

### `OverlapPoint(Vector2)`

```csharp
public bool OverlapPoint(Vector2 point)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `point` | `UnityEngine.Vector2` |  |

**Returns:** `bool`

### `SweepEntitiesFromOrigin(int, IBinaryEntityValidator, Entity, bool)`

```csharp
public IEnumerable<List<Entity>> SweepEntitiesFromOrigin(int iterations, IBinaryEntityValidator validator, Entity self, bool includeUncollidable = false)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `iterations` | `int` |  |
| `validator` | [`IBinaryEntityValidator`](/api/Global.IBinaryEntityValidator) |  |
| `self` | [`Entity`](/api/Global.Entity) |  |
| `includeUncollidable` | `bool` |  |

**Returns:** `System.Collections.Generic.IEnumerable<T><System.Collections.Generic.List<T><Entity>>`

### `SweepEntitiesFromOrigin(int, IEntityValidator, bool)`

```csharp
public IEnumerable<List<Entity>> SweepEntitiesFromOrigin(int iterations, IEntityValidator validator, bool includeUncollidable = false)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `iterations` | `int` |  |
| `validator` | [`IEntityValidator`](/api/Global.IEntityValidator) |  |
| `includeUncollidable` | `bool` |  |

**Returns:** `System.Collections.Generic.IEnumerable<T><System.Collections.Generic.List<T><Entity>>`

### `SweepEntitiesFromOrigin(int, bool)`

```csharp
public IEnumerable<List<Entity>> SweepEntitiesFromOrigin(int iterations, bool includeUncollidable = false)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `iterations` | `int` |  |
| `includeUncollidable` | `bool` |  |

**Returns:** `System.Collections.Generic.IEnumerable<T><System.Collections.Generic.List<T><Entity>>`

### `SweepEntitiesFromOrigin(int, Func<Entity, bool>, bool)`

```csharp
public IEnumerable<List<Entity>> SweepEntitiesFromOrigin(int iterations, Func<Entity, bool> validator, bool includeUncollidable = false)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `iterations` | `int` |  |
| `validator` | [`System.Func<T, TResult><Entity,bool>`](/api/Global.Entity) |  |
| `includeUncollidable` | `bool` |  |

**Returns:** `System.Collections.Generic.IEnumerable<T><System.Collections.Generic.List<T><Entity>>`

### `UpdateProxyCollider()`

```csharp
public void UpdateProxyCollider()
```
