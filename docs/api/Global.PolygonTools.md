# Class: PolygonTools

- **Category:** <span class="cat-dot" style="--cat-color: #64748b" data-cat="Misc & Utility"></span> Misc & Utility
- **Namespace:** `Global`
- **Assembly:** `Dew.Core.dll`

```csharp
public static class PolygonTools
```

## Fields (1)

::: details Click to expand Fields (1)

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`_areas`** | `public static float[] _areas` |  |

:::

## Methods (4)

::: details `GetArea(IReadOnlyList&lt;Vector2&gt;)`

```csharp
public static float GetArea(IReadOnlyList<Vector2> vertices)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `vertices` | `System.Collections.Generic.IReadOnlyList<T><UnityEngine.Vector2>` |  |

**Returns:** `float`

:::

::: details `GetRandomPositionInTriangle(Vector2[], DewRandom)`

```csharp
public static Vector2 GetRandomPositionInTriangle(Vector2[] triVerts, DewRandom random = null)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `triVerts` | `UnityEngine.Vector2[]` |  |
| `random` | [`DewRandom`](/api/Global.DewRandom) |  |

**Returns:** `UnityEngine.Vector2`

:::

::: details `GetVerticesArray(IReadOnlyList&lt;Vector2&gt;, ref Vector2[])`

```csharp
public static void GetVerticesArray(IReadOnlyList<Vector2> points, ref Vector2[] verts)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `points` | `System.Collections.Generic.IReadOnlyList<T><UnityEngine.Vector2>` |  |
| `verts` | `UnityEngine.Vector2[]` |  |

:::

::: details `PickRandomTriangleWeightedByArea(IReadOnlyList&lt;Vector2&gt;, ref Vector2[])`

```csharp
public static int PickRandomTriangleWeightedByArea(IReadOnlyList<Vector2> vertices, ref Vector2[] triVerts)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `vertices` | `System.Collections.Generic.IReadOnlyList<T><UnityEngine.Vector2>` |  |
| `triVerts` | `UnityEngine.Vector2[]` |  |

**Returns:** `int`

:::
