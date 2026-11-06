# Class: AutoColumnGridLayout

- **Category:** <span class="cat-dot" style="--cat-color: #ec4899" data-cat="User Interface"></span> User Interface
- **Namespace:** `Global`
- **Assembly:** `Dew.Core.dll`

```csharp
[AddComponentMenu("Layout/Auto Column Grid Layout")]
[ExecuteAlways]
public class AutoColumnGridLayout : GridLayoutGroup
```

## Properties

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`AutoAdjustColumns`** | `public bool AutoAdjustColumns { get; set; }` |  |
| **`MaxColumns`** | `public int MaxColumns { get; set; }` |  |
| **`MinColumns`** | `public int MinColumns { get; set; }` |  |

## Methods

### `OnDidApplyAnimationProperties()`

```csharp
protected override void OnDidApplyAnimationProperties()
```

### `OnEnable()`

```csharp
protected override void OnEnable()
```

### `OnRectTransformDimensionsChange()`

```csharp
protected override void OnRectTransformDimensionsChange()
```

### `OnTransformParentChanged()`

```csharp
protected override void OnTransformParentChanged()
```

### `UpdateColumnCount()`

Updates the column count based on the available parent width and cell size.

```csharp
public void UpdateColumnCount()
```
