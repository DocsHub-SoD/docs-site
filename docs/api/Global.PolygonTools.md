# Class: PolygonTools

- **Namespace:** `Global`
- **Assembly:** `Dew.Core.dll`

```csharp
public static class PolygonTools
```

## Fields

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`_areas`** | `public static float[] _areas` |  |

## Methods

### `GetArea(IReadOnlyList&lt;Vector2&gt;)`

```csharp
public static float GetArea(IReadOnlyList<Vector2> vertices)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `vertices` | `System.Collections.Generic.IReadOnlyList&lt;T&gt;&lt;UnityEngine.Vector2&gt;` |  |

**Returns:** `float`

### `GetRandomPositionInTriangle(Vector2[], DewRandom)`

```csharp
public static Vector2 GetRandomPositionInTriangle(Vector2[] triVerts, DewRandom random = null)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `triVerts` | `UnityEngine.Vector2[]` |  |
| `random` | [DewRandom](/api/Global.DewRandom) |  |

**Returns:** `UnityEngine.Vector2`

### `GetVerticesArray(IReadOnlyList&lt;Vector2&gt;, ref Vector2[])`

```csharp
public static void GetVerticesArray(IReadOnlyList<Vector2> points, ref Vector2[] verts)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `points` | `System.Collections.Generic.IReadOnlyList&lt;T&gt;&lt;UnityEngine.Vector2&gt;` |  |
| `verts` | `UnityEngine.Vector2[]` |  |

### `PickRandomTriangleWeightedByArea(IReadOnlyList&lt;Vector2&gt;, ref Vector2[])`

```csharp
public static int PickRandomTriangleWeightedByArea(IReadOnlyList<Vector2> vertices, ref Vector2[] triVerts)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `vertices` | `System.Collections.Generic.IReadOnlyList&lt;T&gt;&lt;UnityEngine.Vector2&gt;` |  |
| `triVerts` | `UnityEngine.Vector2[]` |  |

**Returns:** `int`
