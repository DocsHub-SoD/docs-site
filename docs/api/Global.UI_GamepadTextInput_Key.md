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
