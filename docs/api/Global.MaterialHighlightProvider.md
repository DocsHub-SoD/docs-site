# Class: MaterialHighlightProvider

- **Category:** <span class="cat-dot" style="--cat-color: #64748b" data-cat="Misc & Utility"></span> Misc & Utility
- **Namespace:** `Global`
- **Assembly:** `Dew.Core.dll`
- **Inheritance / Derived:** [LogicBehaviour](/api/Global.LogicBehaviour) → [HighlightProvider](/api/Global.HighlightProvider)

```csharp
public class MaterialHighlightProvider : HighlightProvider, ILogicUpdate
```

## Fields (4)

::: details Click to expand Fields (4)

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`clickValueMax`** | `public float clickValueMax` |  |
| **`cursorValueMultiplier`** | `public float cursorValueMultiplier` |  |
| **`targetMaterial`** | `public Material targetMaterial` |  |
| **`targetProperty`** | `public string targetProperty` |  |

:::

## Methods (3)

::: details `FrameUpdate()`

```csharp
public override void FrameUpdate()
```

:::

::: details `OnClickTimeUpdated()`

```csharp
protected override void OnClickTimeUpdated()
```

:::

::: details `OnCursorStatusUpdated()`

```csharp
protected override void OnCursorStatusUpdated()
```

:::


## Architecture & Relationships

::: details Click to expand Architecture & Relationships

### Used By (0)

*No incoming dependencies recorded.*

### Dependencies (2)

*Types and components that `MaterialHighlightProvider` references or depends upon:*

[HighlightProvider](/api/Global.HighlightProvider) · [LogicBehaviour](/api/Global.LogicBehaviour)

:::
