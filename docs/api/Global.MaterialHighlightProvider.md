# Class: MaterialHighlightProvider

- **Namespace:** `Global`
- **Assembly:** `Dew.Core.dll`
- **Inheritance / Derived:** [LogicBehaviour](/api/Global.LogicBehaviour) → [HighlightProvider](/api/Global.HighlightProvider)

```csharp
public class MaterialHighlightProvider : HighlightProvider, ILogicUpdate
```

## Fields

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`clickValueMax`** | `public float clickValueMax` |  |
| **`cursorValueMultiplier`** | `public float cursorValueMultiplier` |  |
| **`targetMaterial`** | `public Material targetMaterial` |  |
| **`targetProperty`** | `public string targetProperty` |  |

## Methods

### `FrameUpdate()`

```csharp
public override void FrameUpdate()
```

### `OnClickTimeUpdated()`

```csharp
protected override void OnClickTimeUpdated()
```

### `OnCursorStatusUpdated()`

```csharp
protected override void OnCursorStatusUpdated()
```
