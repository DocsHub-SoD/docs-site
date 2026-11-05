# Class: UI_GamepadTextInput_Key

- **Namespace:** `Global`
- **Assembly:** `Dew.Core.dll`
- **Inheritance / Derived:** [UI_GamepadFocusable](/api/Global.UI_GamepadFocusable)

```csharp
public class UI_GamepadTextInput_Key : UI_GamepadFocusable, IGamepadFocusable, IGamepadFocusListener, IGamepadFocusableOverrideInput
```

## Fields

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`key`** | `public string key` |  |
| **`keyText`** | `public TextMeshProUGUI keyText` |  |

## Methods

### `OnGamepadDpadDown()`

```csharp
public bool OnGamepadDpadDown()
```

**Returns:** `bool`

### `OnGamepadDpadLeft()`

```csharp
public bool OnGamepadDpadLeft()
```

**Returns:** `bool`

### `OnGamepadDpadRight()`

```csharp
public bool OnGamepadDpadRight()
```

**Returns:** `bool`

### `OnGamepadDpadUp()`

```csharp
public bool OnGamepadDpadUp()
```

**Returns:** `bool`

### `OnPointerClick(PointerEventData)`

```csharp
public void OnPointerClick(PointerEventData eventData)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `eventData` | `UnityEngine.EventSystems.PointerEventData` |  |
