# Class: Cells2D&lt;T&gt;

- **Namespace:** `Global`
- **Assembly:** `Dew.Core.dll`

```csharp
[Serializable]
public class Cells2D<T>
```

## Fields

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`cellSize`** | `public float cellSize` |  |
| **`center`** | `public Vector2 center` |  |
| **`data`** | `public T[] data` |  |
| **`dataHeight`** | `public int dataHeight` |  |
| **`dataWidth`** | `public int dataWidth` |  |
| **`max`** | `public Vector2 max` |  |
| **`min`** | `public Vector2 min` |  |
| **`size`** | `public Vector2 size` |  |

## Methods

### `FloodFill((int, int), Func&lt;(int, int), bool&gt;)`

```csharp
public void FloodFill((int, int) start, Func<(int, int), bool> func)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `start` | `(int,int)` |  |
| `func` | `System.Func&lt;T, TResult&gt;&lt;(int,int),bool&gt;` |  |

### `Get((int, int))`

```csharp
public T Get((int, int) indices)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `indices` | `(int,int)` |  |

**Returns:** `T`

### `GetClosestCell(Vector2)`

```csharp
public (int, int) GetClosestCell(Vector2 worldPos)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `worldPos` | `UnityEngine.Vector2` |  |

**Returns:** `(int,int)`

### `GetCropped(int, int, int, int)`

```csharp
public Cells2D<T> GetCropped(int startX, int endX, int startY, int endY)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `startX` | `int` |  |
| `endX` | `int` |  |
| `startY` | `int` |  |
| `endY` | `int` |  |

**Returns:** `Cells2D&lt;T&gt;`

### `GetNormalizedPos(Vector2)`

```csharp
public Vector2 GetNormalizedPos(Vector2 worldPos)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `worldPos` | `UnityEngine.Vector2` |  |

**Returns:** `UnityEngine.Vector2`

### `GetWorldPos((int, int))`

```csharp
public Vector2 GetWorldPos((int, int) indices)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `indices` | `(int,int)` |  |

**Returns:** `UnityEngine.Vector2`

### `IsInBounds((int, int))`

```csharp
public bool IsInBounds((int, int) indices)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `indices` | `(int,int)` |  |

**Returns:** `bool`

### `Set((int, int), T)`

```csharp
public void Set((int, int) indices, T value)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `indices` | `(int,int)` |  |
| `value` | `T` |  |
