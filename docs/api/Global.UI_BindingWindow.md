# Class: UI_BindingWindow

- **Category:** <span class="cat-dot" style="--cat-color: #ec4899" data-cat="User Interface"></span> User Interface
- **Namespace:** `Global`
- **Assembly:** `Dew.Core.dll`
- **Inheritance / Derived:** `SingletonBehaviour` → [UI_BindingWindow](/api/Global.UI_BindingWindow)

```csharp
public class UI_BindingWindow : SingletonBehaviour<UI_BindingWindow>
```

## Fields (1)

::: details Click to expand Fields (1)

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`keyText`** | `public TextMeshProUGUI keyText` |  |

:::

## Methods (5)

::: details `Cancel()`

```csharp
public void Cancel()
```

:::

::: details `Clear()`

```csharp
public void Clear()
```

:::

::: details `Confirm()`

```csharp
public void Confirm()
```

:::

::: details `DoLeftClick()`

```csharp
public void DoLeftClick()
```

:::

::: details `Show(DewBinding, BindingType, bool, Action, Action)`

```csharp
public void Show(DewBinding newBinding, BindingType allowedTypes, bool allowModifiers, Action onFinish, Action onCancel)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `newBinding` | [`DewBinding`](/api/Global.DewBinding) |  |
| `allowedTypes` | [`BindingType`](/api/Global.BindingType) |  |
| `allowModifiers` | `bool` |  |
| `onFinish` | `System.Action` |  |
| `onCancel` | `System.Action` |  |

:::
