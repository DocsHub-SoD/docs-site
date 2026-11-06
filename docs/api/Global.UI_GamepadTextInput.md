# Class: UI_GamepadTextInput

- **Category:** <span class="cat-dot" style="--cat-color: #ec4899" data-cat="User Interface"></span> User Interface
- **Namespace:** `Global`
- **Assembly:** `Dew.Core.dll`
- **Inheritance / Derived:** `SingletonBehaviour` → [UI_GamepadTextInput](/api/Global.UI_GamepadTextInput)

```csharp
public class UI_GamepadTextInput : SingletonBehaviour<UI_GamepadTextInput>
```

## Fields (14)

::: details Click to expand Fields (14)

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`azertyLayout`** | `[Multiline] [Multiline] public string azertyLayout` |  |
| **`azertyShiftAlpha`** | `public string azertyShiftAlpha` |  |
| **`backspacePrefab`** | `public UI_GamepadTextInput_Key backspacePrefab` |  |
| **`cancelButton`** | `public Button cancelButton` |  |
| **`clearButton`** | `public Button clearButton` |  |
| **`confirmButton`** | `public Button confirmButton` |  |
| **`inputField`** | `public TMP_InputField inputField` |  |
| **`leftShiftPrefab`** | `public UI_GamepadTextInput_Key leftShiftPrefab` |  |
| **`onIsShiftPressedChanged`** | `public Action onIsShiftPressedChanged` |  |
| **`qwertyLayout`** | `[Multiline] [Multiline] public string qwertyLayout` |  |
| **`qwertyShiftAlpha`** | `public string qwertyShiftAlpha` |  |
| **`regularKeyPrefab`** | `public UI_GamepadTextInput_Key regularKeyPrefab` |  |
| **`rightShiftPrefab`** | `public UI_GamepadTextInput_Key rightShiftPrefab` |  |
| **`rowTransforms`** | `public Transform[] rowTransforms` |  |

:::

## Properties (2)

::: details Click to expand Properties (2)

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`isAzerty`** | `public bool isAzerty { get; }` |  |
| **`isShiftPressed`** | `public bool isShiftPressed { get; }` |  |

:::

## Methods (11)

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

::: details `EraseOne()`

```csharp
public void EraseOne()
```

:::

::: details `GetShiftSubstitute(string)`

```csharp
public string GetShiftSubstitute(string key)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `key` | `string` |  |

**Returns:** `string`

:::

::: details `PressCharacter(string)`

```csharp
public void PressCharacter(string key)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `key` | `string` |  |

:::

::: details `SetAzertyMode(bool)`

```csharp
public void SetAzertyMode(bool value)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `value` | `bool` |  |

:::

::: details `SetShift(bool)`

```csharp
public void SetShift(bool value)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `value` | `bool` |  |

:::

::: details `StartInput(string, string, bool, bool, int, Action&lt;string&gt;, Action)`

```csharp
public void StartInput(string previousText, string placeholderText, bool isMultiline, bool isPassword, int maxCharacters, Action<string> onConfirm, Action onCancel)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `previousText` | `string` |  |
| `placeholderText` | `string` |  |
| `isMultiline` | `bool` |  |
| `isPassword` | `bool` |  |
| `maxCharacters` | `int` |  |
| `onConfirm` | `System.Action<T><string>` |  |
| `onCancel` | `System.Action` |  |

:::

::: details `StartInput(TMP_InputField, Action&lt;string&gt;, Action)`

```csharp
public void StartInput(TMP_InputField target, Action<string> onConfirm = null, Action onCancel = null)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `target` | `TMPro.TMP_InputField` |  |
| `onConfirm` | `System.Action<T><string>` |  |
| `onCancel` | `System.Action` |  |

:::

::: details `ToggleShift()`

```csharp
public void ToggleShift()
```

:::


## Architecture & Relationships

::: details Click to expand Architecture & Relationships

### Used By (5)

*Classes and systems that invoke, reference, or depend on `UI_GamepadTextInput`:*

`UI_Common_MenuView` · [UI_GamepadInputField](/api/Global.UI_GamepadInputField) · [UI_GamepadTextInput_Key](/api/Global.UI_GamepadTextInput_Key) · `UI_Lobby_SendChatMessage` · `UI_Title_ProfileSelection_LinkEnterCodeWindow`

### Dependencies (10)

*Types and components that `UI_GamepadTextInput` references or depends upon:*

[DewInputTrigger](/api/Global.DewInputTrigger) · [DewLocalization](/api/Global.DewLocalization) · [DewSteam](/api/Global.DewSteam) · [GlobalUIManager](/api/Global.GlobalUIManager) · [ManagerBase`1](/api/Global.ManagerBase`1) · [MessageManager](/api/Global.MessageManager) · [SafeAction`2](/api/Global.SafeAction`2) · [SingletonBehaviour`1](/api/Global.SingletonBehaviour`1) · [TransitionManager](/api/Global.TransitionManager) · [UI_GamepadTextInput_Key](/api/Global.UI_GamepadTextInput_Key)

### Related Enums (1)

*Enumerations referenced in fields, properties, or method signatures:*

[`InputMode`](/enums#inputmode)

:::
