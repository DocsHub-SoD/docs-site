# Class: UI_GamepadInputField

- **Category:** <span class="cat-dot" style="--cat-color: #ec4899" data-cat="User Interface"></span> User Interface
- **Namespace:** `Global`
- **Assembly:** `Dew.Core.dll`
- **Inheritance / Derived:** [UI_GamepadFocusable](/api/Global.UI_GamepadFocusable)

```csharp
public class UI_GamepadInputField : UI_GamepadFocusable, IGamepadFocusable, IGamepadFocusListener
```

## Methods (4)

::: details `CanBeFocused()`

```csharp
public override bool CanBeFocused()
```

**Returns:** `bool`

:::

::: details `OnEnable()`

```csharp
protected override void OnEnable()
```

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

::: details `StartInput(Action&lt;string&gt;, Action)`

```csharp
public void StartInput(Action<string> onConfirm = null, Action onCancel = null)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `onConfirm` | `System.Action<T><string>` |  |
| `onCancel` | `System.Action` |  |

:::


## Architecture & Relationships

::: details Click to expand Architecture & Relationships

### Used By (1)

*Classes and systems that invoke, reference, or depend on `UI_GamepadInputField`:*

`UI_Lobby_LobbyNameGroup`

### Dependencies (8)

*Types and components that `UI_GamepadInputField` references or depends upon:*

[DewInput](/api/Global.DewInput) · [GlobalUIManager](/api/Global.GlobalUIManager) · [IGamepadFocusListener](/api/Global.IGamepadFocusListener) · [IGamepadFocusable](/api/Global.IGamepadFocusable) · [ManagerBase`1](/api/Global.ManagerBase`1) · [SingletonBehaviour`1](/api/Global.SingletonBehaviour`1) · [UI_GamepadFocusable](/api/Global.UI_GamepadFocusable) · [UI_GamepadTextInput](/api/Global.UI_GamepadTextInput)

:::
