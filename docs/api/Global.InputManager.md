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
