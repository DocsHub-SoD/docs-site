# Class: Cells2D&lt;T&gt;

- **Category:** <span class="cat-dot" style="--cat-color: #f97316" data-cat="Data & Core Math"></span> Data & Core Math
- **Namespace:** `Global`
- **Assembly:** `Dew.Core.dll`

```csharp
[Serializable]
public class Cells2D<T>
```

## Fields (8)

::: details Click to expand Fields (8)

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

:::

## Methods (8)

::: details `FloodFill((int, int), Func&lt;(int, int), bool&gt;)`

```csharp
public void FloodFill((int, int) start, Func<(int, int), bool> func)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `start` | `(int,int)` |  |
| `func` | `System.Func<T, TResult><(int,int),bool>` |  |

:::

::: details `Get((int, int))`

```csharp
public T Get((int, int) indices)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `indices` | `(int,int)` |  |

**Returns:** `T`

:::

::: details `GetClosestCell(Vector2)`

```csharp
public (int, int) GetClosestCell(Vector2 worldPos)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `worldPos` | `UnityEngine.Vector2` |  |

**Returns:** `(int,int)`

:::

::: details `GetCropped(int, int, int, int)`

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

**Returns:** `Cells2D<T>`

:::

::: details `GetNormalizedPos(Vector2)`

```csharp
public Vector2 GetNormalizedPos(Vector2 worldPos)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `worldPos` | `UnityEngine.Vector2` |  |

**Returns:** `UnityEngine.Vector2`

:::

::: details `GetWorldPos((int, int))`

```csharp
public Vector2 GetWorldPos((int, int) indices)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `indices` | `(int,int)` |  |

**Returns:** `UnityEngine.Vector2`

:::

::: details `IsInBounds((int, int))`

```csharp
public bool IsInBounds((int, int) indices)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `indices` | `(int,int)` |  |

**Returns:** `bool`

:::

::: details `Set((int, int), T)`

```csharp
public void Set((int, int) indices, T value)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `indices` | `(int,int)` |  |
| `value` | `T` |  |

:::


## Architecture & Relationships

::: details Click to expand Architecture & Relationships

### Used By (10)

*Classes and systems that invoke, reference, or depend on `Cells2D<T>`:*

[MapData](/api/Global.MapData) · [RoomMap](/api/Global.RoomMap) · `RoomMod_ArcticTerritory` · `RoomMod_GoldEverywhere` · `RoomMod_PureDream` · [RoomModifierBase](/api/Global.RoomModifierBase) · [RoomMonsters](/api/Global.RoomMonsters) · `Sky_WhiteVeil` · `UI_InGame_Map` · `UI_InGame_Map_Item`

### Dependencies (0)

*No outgoing class dependencies recorded.*

:::
