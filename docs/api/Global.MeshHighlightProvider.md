# Class: MeshHighlightProvider

- **Category:** <span class="cat-dot" style="--cat-color: #64748b" data-cat="Misc & Utility"></span> Misc & Utility
- **Namespace:** `Global`
- **Assembly:** `Dew.Core.dll`
- **Inheritance / Derived:** [LogicBehaviour](/api/Global.LogicBehaviour) → [HighlightProvider](/api/Global.HighlightProvider) → [EntityHighlightProvider](/api/Global.EntityHighlightProvider) → [InteractableMeshHighlightProvider](/api/Global.InteractableMeshHighlightProvider)

```csharp
public class MeshHighlightProvider : HighlightProvider, ILogicUpdate
```

## Properties

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`meshHighlight`** | `public HighlightEffect meshHighlight { get; }` |  |

## Methods

### `Awake()`

```csharp
protected virtual void Awake()
```

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

### `OnDestroy()`

```csharp
protected void OnDestroy()
```

### `Start()`

```csharp
protected virtual void Start()
```
