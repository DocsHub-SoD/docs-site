# Class: HighlightProvider

- **Category:** <span class="cat-dot" style="--cat-color: #64748b" data-cat="Misc & Utility"></span> Misc & Utility
- **Namespace:** `Global`
- **Assembly:** `Dew.Core.dll`
- **Inheritance / Derived:** [LogicBehaviour](/api/Global.LogicBehaviour) → [MaterialHighlightProvider](/api/Global.MaterialHighlightProvider) → [MeshHighlightProvider](/api/Global.MeshHighlightProvider)

```csharp
[LogicUpdatePriority(500)]
public class HighlightProvider : LogicBehaviour, ILogicUpdate
```

## Properties (2)

::: details Click to expand Properties (2)

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`cursorStatus`** | `public HighlightProvider.CursorStatus cursorStatus { get; set; }` |  |
| **`elapsedClickTime`** | `public float elapsedClickTime { get; }` |  |

:::

## Methods (3)

::: details `OnClickTimeUpdated()`

```csharp
protected virtual void OnClickTimeUpdated()
```

:::

::: details `OnCursorStatusUpdated()`

```csharp
protected virtual void OnCursorStatusUpdated()
```

:::

::: details `ShowClick()`

```csharp
public void ShowClick()
```

:::
