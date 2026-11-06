# Class: CursorManager

- **Category:** <span class="cat-dot" style="--cat-color: #ec4899" data-cat="User Interface"></span> User Interface
- **Namespace:** `Global`
- **Assembly:** `Dew.Core.dll`
- **Inheritance / Derived:** [LogicBehaviour](/api/Global.LogicBehaviour) → `ManagerBase` → [CursorManager](/api/Global.CursorManager)

```csharp
public class CursorManager : ManagerBase<CursorManager>, ILogicUpdate
```

## Fields (3)

::: details Click to expand Fields (3)

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`disableSoftwareCursor`** | `[NonSerialized] public bool disableSoftwareCursor` |  |
| **`scaleMultiplier`** | `public float scaleMultiplier` |  |
| **`textures`** | `public Texture2D[] textures` |  |

:::

## Methods (5)

::: details `ApplyCursor(int)`

```csharp
public void ApplyCursor(int index)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `index` | `int` |  |

:::

::: details `CreateScaledCopy(Texture2D, float)`

```csharp
public Texture2D CreateScaledCopy(Texture2D source, float scaleFactor)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `source` | `UnityEngine.Texture2D` |  |
| `scaleFactor` | `float` |  |

**Returns:** `UnityEngine.Texture2D`

:::

::: details `FrameUpdate()`

```csharp
public override void FrameUpdate()
```

:::

::: details `LogicUpdate(float)`

```csharp
public override void LogicUpdate(float dt)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `dt` | `float` |  |

:::

::: details `ResizeTextures()`

```csharp
public void ResizeTextures()
```

:::
