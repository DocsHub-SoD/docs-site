# Class: PerDeveloperModeVisibility

- **Category:** <span class="cat-dot" style="--cat-color: #64748b" data-cat="Misc & Utility"></span> Misc & Utility
- **Namespace:** `Global`
- **Assembly:** `Dew.Core.dll`
- **Attributes:** `[RequireComponent]`

```csharp
public class PerDeveloperModeVisibility : MonoBehaviour, ISettingsChangedCallback
```

## Fields (2)

::: details Click to expand Fields (2)

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`showIfDeveloper`** | `public bool showIfDeveloper` |  |
| **`showIfNotDeveloper`** | `public bool showIfNotDeveloper` |  |

:::

## Methods (1)

::: details `OnSettingsChanged()`

```csharp
public void OnSettingsChanged()
```

:::


## Architecture & Relationships

::: details Click to expand Architecture & Relationships

### Used By (0)

*No incoming dependencies recorded.*

### Dependencies (3)

*Types and components that `PerDeveloperModeVisibility` references or depends upon:*

[ISettingsChangedCallback](/api/Global.ISettingsChangedCallback) · `IVisibilityComponent` · `VisibilityController`

:::
