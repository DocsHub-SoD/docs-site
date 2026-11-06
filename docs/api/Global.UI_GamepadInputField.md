# Class: UI_GamepadInputField

- **Category:** <span class="cat-dot" style="--cat-color: #ec4899" data-cat="User Interface"></span> User Interface
- **Namespace:** `Global`
- **Assembly:** `Dew.Core.dll`
- **Inheritance / Derived:** [UI_GamepadFocusable](/api/Global.UI_GamepadFocusable)

```csharp
public class UI_GamepadInputField : UI_GamepadFocusable, IGamepadFocusable, IGamepadFocusListener
```

## Methods

### `CanBeFocused()`

```csharp
public override bool CanBeFocused()
```

**Returns:** `bool`

### `OnEnable()`

```csharp
protected override void OnEnable()
```

### `OnPointerClick(PointerEventData)`

```csharp
public void OnPointerClick(PointerEventData eventData)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `eventData` | `UnityEngine.EventSystems.PointerEventData` |  |

### `StartInput(Action<string>, Action)`

```csharp
public void StartInput(Action<string> onConfirm = null, Action onCancel = null)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `onConfirm` | `System.Action<T><string>` |  |
| `onCancel` | `System.Action` |  |
