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


## Architecture & Relationships

::: details Click to expand Architecture & Relationships

### Used By (1)

*Classes and systems that invoke, reference, or depend on `CursorManager`:*

[DewSave](/api/Global.DewSave)

### Dependencies (6)

*Types and components that `CursorManager` references or depends upon:*

`ColorExtensions` · [InGameUIManager](/api/Global.InGameUIManager) · [LogicBehaviour](/api/Global.LogicBehaviour) · [ManagerBase`1](/api/Global.ManagerBase`1) · [NetworkedManagerBase`1](/api/Global.NetworkedManagerBase`1) · [UIManager](/api/Global.UIManager)

:::
