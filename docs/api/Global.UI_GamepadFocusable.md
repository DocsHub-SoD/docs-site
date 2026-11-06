# Class: UI_GamepadFocusable

- **Category:** <span class="cat-dot" style="--cat-color: #ec4899" data-cat="User Interface"></span> User Interface
- **Namespace:** `Global`
- **Assembly:** `Dew.Core.dll`
- **Inheritance / Derived:** [UI_GamepadInputField](/api/Global.UI_GamepadInputField) → [UI_GamepadTextInput_Key](/api/Global.UI_GamepadTextInput_Key)

```csharp
[DisallowMultipleComponent]
public class UI_GamepadFocusable : MonoBehaviour, IGamepadFocusable, IGamepadFocusListener
```

## Fields (4)

::: details Click to expand Fields (4)

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`canHoldConfirmToRepeat`** | `public bool canHoldConfirmToRepeat` |  |
| **`display`** | `public SelectionDisplayType display` |  |
| **`focusOnEnable`** | `public bool focusOnEnable` |  |
| **`ignoreSelectableInteractivity`** | `public bool ignoreSelectableInteractivity` |  |

:::

## Properties (1)

::: details Click to expand Properties (1)

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`isFocused`** | `public bool isFocused { get; }` |  |

:::

## Methods (6)

::: details `CanBeFocused()`

```csharp
public virtual bool CanBeFocused()
```

**Returns:** `bool`

:::

::: details `CanHoldConfirmToRepeat()`

```csharp
public bool CanHoldConfirmToRepeat()
```

**Returns:** `bool`

:::

::: details `GetSelectionDisplayType()`

```csharp
public SelectionDisplayType GetSelectionDisplayType()
```

**Returns:** `SelectionDisplayType`

:::

::: details `OnDisable()`

```csharp
protected virtual void OnDisable()
```

:::

::: details `OnEnable()`

```csharp
protected virtual void OnEnable()
```

:::

::: details `OnFocusStateChanged(bool)`

```csharp
public virtual void OnFocusStateChanged(bool state)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `state` | `bool` |  |

:::
