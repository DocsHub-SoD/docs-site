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
| `allowedTypes` | <a href="/enums#bindingtype" class="enum-link" data-tooltip="None=0 · Keyboard=1 · Mouse=2 · Gamepad=4">BindingType</a> |  |
| `allowModifiers` | `bool` |  |
| `onFinish` | `System.Action` |  |
| `onCancel` | `System.Action` |  |

:::


## Architecture & Relationships

::: details Click to expand Architecture & Relationships

### Used By (2)

*Classes and systems that invoke, reference, or depend on `UI_BindingWindow`:*

[UI_BindItem](/api/Global.UI_BindItem) · [UI_BindingWindow_ClickReceiver](/api/Global.UI_BindingWindow_ClickReceiver)

### Dependencies (4)

*Types and components that `UI_BindingWindow` references or depends upon:*

[DewBinding](/api/Global.DewBinding) · [DewInput](/api/Global.DewInput) · [ManagerBase`1](/api/Global.ManagerBase`1) · [SingletonBehaviour`1](/api/Global.SingletonBehaviour`1)

### Related Enums (1)

*Enumerations referenced in fields, properties, or method signatures:*

<a href="/enums#bindingtype" class="enum-link" data-tooltip="None=0 · Keyboard=1 · Mouse=2 · Gamepad=4">BindingType</a>

:::
