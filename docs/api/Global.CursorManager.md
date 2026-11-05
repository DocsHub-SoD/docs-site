# Class: CursorManager

- **Namespace:** `Global`
- **Assembly:** `Dew.Core.dll`
- **Inheritance / Derived:** [LogicBehaviour](/api/Global.LogicBehaviour) → `ManagerBase` → [CursorManager](/api/Global.CursorManager)

```csharp
public class CursorManager : ManagerBase<CursorManager>, ILogicUpdate
```

## Fields

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`disableSoftwareCursor`** | `[NonSerialized]
public bool disableSoftwareCursor` |  |
| **`scaleMultiplier`** | `public float scaleMultiplier` |  |
| **`textures`** | `public Texture2D[] textures` |  |

## Methods

### `ApplyCursor(int)`

```csharp
public void ApplyCursor(int index)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `index` | `int` |  |

### `CreateScaledCopy(Texture2D, float)`

```csharp
public Texture2D CreateScaledCopy(Texture2D source, float scaleFactor)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `source` | `UnityEngine.Texture2D` |  |
| `scaleFactor` | `float` |  |

**Returns:** `UnityEngine.Texture2D`

### `FrameUpdate()`

```csharp
public override void FrameUpdate()
```

### `LogicUpdate(float)`

```csharp
public override void LogicUpdate(float dt)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `dt` | `float` |  |

### `ResizeTextures()`

```csharp
public void ResizeTextures()
```
