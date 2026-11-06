# Class: AutoColumnGridLayout

- **Category:** <span class="cat-dot" style="--cat-color: #ec4899" data-cat="User Interface"></span> User Interface
- **Namespace:** `Global`
- **Assembly:** `Dew.Core.dll`
- **Attributes:** `[AddComponentMenu] [ExecuteAlways]`

```csharp
[AddComponentMenu("Layout/Auto Column Grid Layout")]
[ExecuteAlways]
public class AutoColumnGridLayout : GridLayoutGroup
```

## Properties (3)

::: details Click to expand Properties (3)

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`AutoAdjustColumns`** | `public bool AutoAdjustColumns { get; set; }` |  |
| **`MaxColumns`** | `public int MaxColumns { get; set; }` |  |
| **`MinColumns`** | `public int MinColumns { get; set; }` |  |

:::

## Methods (5)

::: details `OnDidApplyAnimationProperties()`

```csharp
protected override void OnDidApplyAnimationProperties()
```

:::

::: details `OnEnable()`

```csharp
protected override void OnEnable()
```

:::

::: details `OnRectTransformDimensionsChange()`

```csharp
protected override void OnRectTransformDimensionsChange()
```

:::

::: details `OnTransformParentChanged()`

```csharp
protected override void OnTransformParentChanged()
```

:::

::: details `UpdateColumnCount()`

Updates the column count based on the available parent width and cell size.

```csharp
public void UpdateColumnCount()
```

:::


## Architecture & Relationships

::: details Click to expand Architecture & Relationships

### Used By (0)

*No incoming dependencies recorded.*

### Dependencies (0)

*No outgoing class dependencies recorded.*

:::
