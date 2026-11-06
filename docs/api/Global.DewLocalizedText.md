# Class: DewLocalizedText

- **Category:** <span class="cat-dot" style="--cat-color: #64748b" data-cat="Misc & Utility"></span> Misc & Utility
- **Namespace:** `Global`
- **Assembly:** `Dew.Core.dll`
- **Attributes:** `[ExecuteAlways]`

```csharp
public class DewLocalizedText : MonoBehaviour, ILangaugeChangedCallback
```

## Fields (1)

::: details Click to expand Fields (1)

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`key`** | `public string key` |  |

:::

## Methods (2)

::: details `OnLanguageChanged()`

```csharp
public void OnLanguageChanged()
```

:::

::: details `UpdateText()`

```csharp
public void UpdateText()
```

:::


## Architecture & Relationships

::: details Click to expand Architecture & Relationships

### Used By (2)

*Classes and systems that invoke, reference, or depend on `DewLocalizedText`:*

`UI_Settings_Item` · `UI_TravelerStoryDetailContainer`

### Dependencies (2)

*Types and components that `DewLocalizedText` references or depends upon:*

[DewLocalization](/api/Global.DewLocalization) · [ILangaugeChangedCallback](/api/Global.ILangaugeChangedCallback)

:::
