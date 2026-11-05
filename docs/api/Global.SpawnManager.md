# Class: SpawnManager

- **Namespace:** `Global`
- **Assembly:** `Dew.Core.dll`
- **Inheritance / Derived:** [LogicBehaviour](/api/Global.LogicBehaviour) → `ManagerBase` → [SpawnManager](/api/Global.SpawnManager)

```csharp
public class SpawnManager : ManagerBase<SpawnManager>, ILogicUpdate
```

## Fields

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`activeInstanceToPool`** | `public Dictionary&lt;GameObject, ObjectPoolItem&gt; activeInstanceToPool` |  |
| **`pool`** | `public Dictionary&lt;GameObject, ObjectPoolItem&gt; pool` |  |
| **`showPoolInfo`** | `[NonSerialized]
public bool showPoolInfo` |  |
| **`usePooling`** | `[NonSerialized]
public bool usePooling` |  |

## Methods

### `Awake()`

```csharp
protected override void Awake()
```

### `Create&lt;T&gt;(T, Vector3, Quaternion, Transform)`

```csharp
public static T Create<T>(T prefab, Vector3 position, Quaternion rotation, Transform parent) where T : Object
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `prefab` | `T` |  |
| `position` | `UnityEngine.Vector3` |  |
| `rotation` | `UnityEngine.Quaternion` |  |
| `parent` | `UnityEngine.Transform` |  |
| `` | `T` |  |

**Returns:** `T`

### `Create&lt;T&gt;(T, Vector3, Quaternion)`

```csharp
public static T Create<T>(T prefab, Vector3 position, Quaternion rotation) where T : Object
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `prefab` | `T` |  |
| `position` | `UnityEngine.Vector3` |  |
| `rotation` | `UnityEngine.Quaternion` |  |
| `` | `T` |  |

**Returns:** `T`

### `Destroy(GameObject)`

```csharp
public static void Destroy(GameObject gobj)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `gobj` | `UnityEngine.GameObject` |  |

### `InvalidateInstance(Component)`

Invalidate an instance from pool, preventing it from being reused.

```csharp
public static void InvalidateInstance(Component activeInstance)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `activeInstance` | `UnityEngine.Component` |  |

### `InvalidateInstance(GameObject)`

Invalidate an instance from pool, preventing it from being reused.

```csharp
public static void InvalidateInstance(GameObject activeInstance)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `activeInstance` | `UnityEngine.GameObject` |  |
