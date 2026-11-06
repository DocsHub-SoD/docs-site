# Class: ObjectHighlightManager

- **Category:** <span class="cat-dot" style="--cat-color: #3b82f6" data-cat="Managers & Systems"></span> Managers & Systems
- **Namespace:** `Global`
- **Assembly:** `Dew.Core.dll`
- **Inheritance / Derived:** [LogicBehaviour](/api/Global.LogicBehaviour) → `ManagerBase` → [ObjectHighlightManager](/api/Global.ObjectHighlightManager)

```csharp
public class ObjectHighlightManager : ManagerBase<ObjectHighlightManager>, ILogicUpdate, ICinematicCameraHelperStateReceiver
```

## Fields (8)

::: details Click to expand Fields (8)

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`ally`** | `public ObjectHighlightManager.OutlineStyle ally` |  |
| **`enemy`** | `public ObjectHighlightManager.OutlineStyle enemy` |  |
| **`interactable`** | `public ObjectHighlightManager.OutlineStyle interactable` |  |
| **`isObjectHighlightDisabled`** | `[NonSerialized] public bool isObjectHighlightDisabled` |  |
| **`MouseDownStrength`** | `public const float MouseDownStrength = 0.6` |  |
| **`MouseOverStrength`** | `public const float MouseOverStrength = 0.4` |  |
| **`neutral`** | `public ObjectHighlightManager.OutlineStyle neutral` |  |
| **`own`** | `public ObjectHighlightManager.OutlineStyle own` |  |

:::

## Methods (3)

::: details `FrameUpdate()`

```csharp
public override void FrameUpdate()
```

:::

::: details `GetProfile()`

```csharp
public static HighlightProfile GetProfile()
```

**Returns:** `HighlightPlus.HighlightProfile`

:::

::: details `OnCinematicCameraHelperChanged(bool)`

```csharp
public void OnCinematicCameraHelperChanged(bool on)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `on` | `bool` |  |

:::


## Architecture & Relationships

::: details Click to expand Architecture & Relationships

### Used By (1)

*Classes and systems that invoke, reference, or depend on `ObjectHighlightManager`:*

[MeshHighlightProvider](/api/Global.MeshHighlightProvider)

### Dependencies (8)

*Types and components that `ObjectHighlightManager` references or depends upon:*

[ControlManager](/api/Global.ControlManager) · [DewInput](/api/Global.DewInput) · [HighlightProvider](/api/Global.HighlightProvider) · [ICinematicCameraHelperStateReceiver](/api/Global.ICinematicCameraHelperStateReceiver) · [InGameUIManager](/api/Global.InGameUIManager) · [LogicBehaviour](/api/Global.LogicBehaviour) · [ManagerBase`1](/api/Global.ManagerBase`1) · [UIManager](/api/Global.UIManager)

:::
