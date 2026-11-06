# Class: UI_GamepadTextInput_Key

- **Category:** <span class="cat-dot" style="--cat-color: #ec4899" data-cat="User Interface"></span> User Interface
- **Namespace:** `Global`
- **Assembly:** `Dew.Core.dll`
- **Inheritance / Derived:** [UI_GamepadFocusable](/api/Global.UI_GamepadFocusable)

```csharp
public class UI_GamepadTextInput_Key : UI_GamepadFocusable, IGamepadFocusable, IGamepadFocusListener, IGamepadFocusableOverrideInput
```

## Fields (2)

::: details Click to expand Fields (2)

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`key`** | `public string key` |  |
| **`keyText`** | `public TextMeshProUGUI keyText` |  |

:::

## Methods (5)

::: details `OnGamepadDpadDown()`

```csharp
public bool OnGamepadDpadDown()
```

**Returns:** `bool`

:::

::: details `OnGamepadDpadLeft()`

```csharp
public bool OnGamepadDpadLeft()
```

**Returns:** `bool`

:::

::: details `OnGamepadDpadRight()`

```csharp
public bool OnGamepadDpadRight()
```

**Returns:** `bool`

:::

::: details `OnGamepadDpadUp()`

```csharp
public bool OnGamepadDpadUp()
```

**Returns:** `bool`

:::

::: details `OnPointerClick(PointerEventData)`

```csharp
public void OnPointerClick(PointerEventData eventData)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `eventData` | `UnityEngine.EventSystems.PointerEventData` |  |

:::


## Architecture & Relationships

::: details Click to expand Architecture & Relationships

### Used By (1)

*Classes and systems that invoke, reference, or depend on `UI_GamepadTextInput_Key`:*

[UI_GamepadTextInput](/api/Global.UI_GamepadTextInput)

### Dependencies (5)

*Types and components that `UI_GamepadTextInput_Key` references or depends upon:*

[GlobalUIManager](/api/Global.GlobalUIManager) · [IGamepadFocusableOverrideInput](/api/Global.IGamepadFocusableOverrideInput) · [ManagerBase`1](/api/Global.ManagerBase`1) · [UI_GamepadFocusable](/api/Global.UI_GamepadFocusable) · [UI_GamepadTextInput](/api/Global.UI_GamepadTextInput)

:::
