# Class: EntityHighlightProvider

- **Namespace:** `Global`
- **Assembly:** `Dew.Core.dll`
- **Inheritance / Derived:** [LogicBehaviour](/api/Global.LogicBehaviour) → [HighlightProvider](/api/Global.HighlightProvider) → [MeshHighlightProvider](/api/Global.MeshHighlightProvider)

```csharp
public class EntityHighlightProvider : MeshHighlightProvider, ILogicUpdate
```

## Fields

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`disableHighlight`** | `public bool disableHighlight` |  |
| **`HitEffectDuration`** | `public const float HitEffectDuration = 0.1` |  |

## Methods

### `Awake()`

```csharp
protected override void Awake()
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

### `ShowHit()`

```csharp
public void ShowHit()
```

### `Start()`

```csharp
protected override void Start()
```
