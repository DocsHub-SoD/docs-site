# Class: InputManager

- **Namespace:** `Global`
- **Assembly:** `Dew.Core.dll`
- **Inheritance / Derived:** [LogicBehaviour](/api/Global.LogicBehaviour) → `ManagerBase` → [InputManager](/api/Global.InputManager)

```csharp
public class InputManager : ManagerBase<InputManager>, ILogicUpdate, ISettingsChangedCallback
```

## Methods

### `AddShakeInstance(ShakeInstance)`

```csharp
public void AddShakeInstance(ShakeInstance si)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `si` | [ShakeInstance](/api/Global.ShakeInstance) |  |

### `FrameUpdate()`

```csharp
public override void FrameUpdate()
```

### `GetMouseSensitivity()`

```csharp
public static int GetMouseSensitivity()
```

**Returns:** `int`

### `GetStickDirection(GamepadButtonEx)`

```csharp
public bool GetStickDirection(GamepadButtonEx g)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `g` | [GamepadButtonEx](/api/Global.GamepadButtonEx) |  |

**Returns:** `bool`

### `GetStickDirectionDown(GamepadButtonEx)`

```csharp
public bool GetStickDirectionDown(GamepadButtonEx g)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `g` | [GamepadButtonEx](/api/Global.GamepadButtonEx) |  |

**Returns:** `bool`

### `GetStickDirectionUp(GamepadButtonEx)`

```csharp
public bool GetStickDirectionUp(GamepadButtonEx g)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `g` | [GamepadButtonEx](/api/Global.GamepadButtonEx) |  |

**Returns:** `bool`

### `IsStickDirection(GamepadButtonEx)`

```csharp
public bool IsStickDirection(GamepadButtonEx g)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `g` | [GamepadButtonEx](/api/Global.GamepadButtonEx) |  |

**Returns:** `bool`

### `OnSettingsChanged()`

```csharp
public void OnSettingsChanged()
```

### `ResetInputDevices()`

```csharp
public void ResetInputDevices()
```

### `SetMouseSensitivity(int)`

```csharp
public static void SetMouseSensitivity(int sensitivity)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `sensitivity` | `int` |  |
