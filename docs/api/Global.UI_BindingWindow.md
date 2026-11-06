# Class: UI_BindingWindow

- **Category:** <span class="cat-dot" style="--cat-color: #ec4899" data-cat="User Interface"></span> User Interface
- **Namespace:** `Global`
- **Assembly:** `Dew.Core.dll`
- **Inheritance / Derived:** `SingletonBehaviour` → [UI_BindingWindow](/api/Global.UI_BindingWindow)

```csharp
public class UI_BindingWindow : SingletonBehaviour<UI_BindingWindow>
```

## Fields

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`keyText`** | `public TextMeshProUGUI keyText` |  |

## Methods

### `Cancel()`

```csharp
public void Cancel()
```

### `Clear()`

```csharp
public void Clear()
```

### `Confirm()`

```csharp
public void Confirm()
```

### `DoLeftClick()`

```csharp
public void DoLeftClick()
```

### `Show(DewBinding, BindingType, bool, Action, Action)`

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
