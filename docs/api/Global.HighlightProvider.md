# Class: HighlightProvider

- **Namespace:** `Global`
- **Assembly:** `Dew.Core.dll`
- **Inheritance / Derived:** [LogicBehaviour](/api/Global.LogicBehaviour) → [MaterialHighlightProvider](/api/Global.MaterialHighlightProvider) → [MeshHighlightProvider](/api/Global.MeshHighlightProvider)

```csharp
[LogicUpdatePriority(500)]
public class HighlightProvider : LogicBehaviour, ILogicUpdate
```

## Properties

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`cursorStatus`** | `public HighlightProvider.CursorStatus cursorStatus { get; set; }` |  |
| **`elapsedClickTime`** | `public float elapsedClickTime { get; }` |  |

## Methods

### `OnClickTimeUpdated()`

```csharp
protected virtual void OnClickTimeUpdated()
```

### `OnCursorStatusUpdated()`

```csharp
protected virtual void OnCursorStatusUpdated()
```

### `ShowClick()`

```csharp
public void ShowClick()
```
