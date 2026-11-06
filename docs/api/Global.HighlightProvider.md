# Class: HighlightProvider

- **Category:** <span class="cat-dot" style="--cat-color: #64748b" data-cat="Misc & Utility"></span> Misc & Utility
- **Namespace:** `Global`
- **Assembly:** `Dew.Core.dll`
- **Attributes:** `[LogicUpdatePriority]`
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


## Architecture & Relationships

::: details Click to expand Architecture & Relationships

### Used By (5)

*Classes and systems that invoke, reference, or depend on `HighlightProvider`:*

[ControlManager](/api/Global.ControlManager) · [EntityHighlightProvider](/api/Global.EntityHighlightProvider) · [MaterialHighlightProvider](/api/Global.MaterialHighlightProvider) · [MeshHighlightProvider](/api/Global.MeshHighlightProvider) · [ObjectHighlightManager](/api/Global.ObjectHighlightManager)

### Dependencies (2)

*Types and components that `HighlightProvider` references or depends upon:*

[LogicBehaviour](/api/Global.LogicBehaviour) · [ManagerBase`1](/api/Global.ManagerBase`1)

:::
