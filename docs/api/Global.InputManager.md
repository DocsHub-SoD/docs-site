# Class: InputManager

- **Category:** <span class="cat-dot" style="--cat-color: #3b82f6" data-cat="Managers & Systems"></span> Managers & Systems
- **Namespace:** `Global`
- **Assembly:** `Dew.Core.dll`
- **Inheritance / Derived:** [LogicBehaviour](/api/Global.LogicBehaviour) → `ManagerBase` → [InputManager](/api/Global.InputManager)

```csharp
public class InputManager : ManagerBase<InputManager>, ILogicUpdate, ISettingsChangedCallback
```

## Methods (10)

::: details `AddShakeInstance(ShakeInstance)`

```csharp
public void AddShakeInstance(ShakeInstance si)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `si` | [`ShakeInstance`](/api/Global.ShakeInstance) |  |

:::

::: details `FrameUpdate()`

```csharp
public override void FrameUpdate()
```

:::

::: details `GetMouseSensitivity()`

```csharp
public static int GetMouseSensitivity()
```

**Returns:** `int`

:::

::: details `GetStickDirection(GamepadButtonEx)`

```csharp
public bool GetStickDirection(GamepadButtonEx g)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `g` | [`GamepadButtonEx`](/api/Global.GamepadButtonEx) |  |

**Returns:** `bool`

:::

::: details `GetStickDirectionDown(GamepadButtonEx)`

```csharp
public bool GetStickDirectionDown(GamepadButtonEx g)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `g` | [`GamepadButtonEx`](/api/Global.GamepadButtonEx) |  |

**Returns:** `bool`

:::

::: details `GetStickDirectionUp(GamepadButtonEx)`

```csharp
public bool GetStickDirectionUp(GamepadButtonEx g)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `g` | [`GamepadButtonEx`](/api/Global.GamepadButtonEx) |  |

**Returns:** `bool`

:::

::: details `IsStickDirection(GamepadButtonEx)`

```csharp
public bool IsStickDirection(GamepadButtonEx g)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `g` | [`GamepadButtonEx`](/api/Global.GamepadButtonEx) |  |

**Returns:** `bool`

:::

::: details `OnSettingsChanged()`

```csharp
public void OnSettingsChanged()
```

:::

::: details `ResetInputDevices()`

```csharp
public void ResetInputDevices()
```

:::

::: details `SetMouseSensitivity(int)`

```csharp
public static void SetMouseSensitivity(int sensitivity)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `sensitivity` | `int` |  |

:::


## Architecture & Relationships

::: details Click to expand Architecture & Relationships

### Used By (10)

*Classes and systems that invoke, reference, or depend on `InputManager`:*

[ControlManager](/api/Global.ControlManager) · [DewControlSettings_User](/api/Global.DewControlSettings_User) · [DewInput](/api/Global.DewInput) · [DewInputTrigger](/api/Global.DewInputTrigger) · [DewSave](/api/Global.DewSave) · [EditSkillManager](/api/Global.EditSkillManager) · [FxCameraShake](/api/Global.FxCameraShake) · `UI_Common_SkipButton` · `UI_ControllerDisconnectedIndicator` · `UI_Lobby_Constellations_StarDetails`

### Dependencies (7)

*Types and components that `InputManager` references or depends upon:*

[DewInput](/api/Global.DewInput) · [DewInputTrigger](/api/Global.DewInputTrigger) · [ISettingsChangedCallback](/api/Global.ISettingsChangedCallback) · [LogicBehaviour](/api/Global.LogicBehaviour) · [ManagerBase`1](/api/Global.ManagerBase`1) · [SafeAction`1](/api/Global.SafeAction`1) · [ShakeInstance](/api/Global.ShakeInstance)

### Related Enums (2)

*Enumerations referenced in fields, properties, or method signatures:*

[`GamepadButtonEx`](/enums#gamepadbuttonex) · [`MouseButton`](/enums#mousebutton)

:::
