# Class: DewInput

- **Namespace:** `Global`
- **Assembly:** `Dew.Core.dll`

```csharp
public static class DewInput
```

## Fields

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`ModifierKeys`** | `public static readonly List&lt;Key&gt; ModifierKeys` |  |
| **`NameToMouseButton`** | `public static readonly IReadOnlyDictionary&lt;string, MouseButton&gt; NameToMouseButton` |  |
| **`onCurrentModeChanged`** | `public static SafeAction&lt;InputMode, InputMode&gt; onCurrentModeChanged` |  |

## Properties

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`controllerButtonType`** | `public static ControllerButtonType controllerButtonType { get; }` |  |
| **`currentMode`** | `public static InputMode currentMode { get; }` |  |

## Methods

### `GetButton(DewBinding, bool)`

```csharp
public static bool GetButton(DewBinding b, bool checkGameAreaForMouse)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `b` | [DewBinding](/api/Global.DewBinding) |  |
| `checkGameAreaForMouse` | `bool` |  |

**Returns:** `bool`

### `GetButton(MouseButton, bool)`

```csharp
public static bool GetButton(MouseButton m, bool checkGameArea)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `m` | [MouseButton](/api/Global.MouseButton) |  |
| `checkGameArea` | `bool` |  |

**Returns:** `bool`

### `GetButton(GamepadButtonEx?)`

```csharp
public static bool GetButton(GamepadButtonEx? g)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `g` | [GamepadButtonEx?](/api/Global.GamepadButtonEx) |  |

**Returns:** `bool`

### `GetButton(Key)`

```csharp
public static bool GetButton(Key k)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `k` | `UnityEngine.InputSystem.Key` |  |

**Returns:** `bool`

### `GetButtonDown(DewBinding, bool)`

```csharp
public static bool GetButtonDown(DewBinding b, bool checkGameAreaForMouse)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `b` | [DewBinding](/api/Global.DewBinding) |  |
| `checkGameAreaForMouse` | `bool` |  |

**Returns:** `bool`

### `GetButtonDown(MouseButton, bool)`

```csharp
public static bool GetButtonDown(MouseButton m, bool checkGameArea)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `m` | [MouseButton](/api/Global.MouseButton) |  |
| `checkGameArea` | `bool` |  |

**Returns:** `bool`

### `GetButtonDown(GamepadButtonEx?)`

```csharp
public static bool GetButtonDown(GamepadButtonEx? g)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `g` | [GamepadButtonEx?](/api/Global.GamepadButtonEx) |  |

**Returns:** `bool`

### `GetButtonDown(Key)`

```csharp
public static bool GetButtonDown(Key k)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `k` | `UnityEngine.InputSystem.Key` |  |

**Returns:** `bool`

### `GetButtonDownAnyGamepad()`

```csharp
public static bool GetButtonDownAnyGamepad()
```

**Returns:** `bool`

### `GetButtonDownAnyKey()`

```csharp
public static bool GetButtonDownAnyKey()
```

**Returns:** `bool`

### `GetButtonDownAnyMouse()`

```csharp
public static bool GetButtonDownAnyMouse()
```

**Returns:** `bool`

### `GetButtonUp(DewBinding, bool)`

```csharp
public static bool GetButtonUp(DewBinding b, bool checkGameAreaForMouse)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `b` | [DewBinding](/api/Global.DewBinding) |  |
| `checkGameAreaForMouse` | `bool` |  |

**Returns:** `bool`

### `GetButtonUp(MouseButton, bool)`

```csharp
public static bool GetButtonUp(MouseButton m, bool checkGameArea)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `m` | [MouseButton](/api/Global.MouseButton) |  |
| `checkGameArea` | `bool` |  |

**Returns:** `bool`

### `GetButtonUp(GamepadButtonEx?)`

```csharp
public static bool GetButtonUp(GamepadButtonEx? g)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `g` | [GamepadButtonEx?](/api/Global.GamepadButtonEx) |  |

**Returns:** `bool`

### `GetButtonUp(Key)`

```csharp
public static bool GetButtonUp(Key k)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `k` | `UnityEngine.InputSystem.Key` |  |

**Returns:** `bool`

### `GetLeftJoystick()`

Magnitude will be full range of 0 ~ 1 regardless of dead zone settings. Returns Vector2.zero if under dead zone.

```csharp
public static Vector2 GetLeftJoystick()
```

**Returns:** `UnityEngine.Vector2`

### `GetReadableTextForCurrentMode(DewBinding, out BindingType)`

```csharp
public static string GetReadableTextForCurrentMode(DewBinding b, out BindingType type)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `b` | [DewBinding](/api/Global.DewBinding) |  |
| `type` | [BindingType](/api/Global.BindingType) |  |

**Returns:** `string`

### `GetReadableTextForCurrentMode(DewBinding)`

```csharp
public static string GetReadableTextForCurrentMode(DewBinding b)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `b` | [DewBinding](/api/Global.DewBinding) |  |

**Returns:** `string`

### `GetReadableTextOfGamepad(DewBinding, out BindingType)`

```csharp
public static string GetReadableTextOfGamepad(DewBinding b, out BindingType type)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `b` | [DewBinding](/api/Global.DewBinding) |  |
| `type` | [BindingType](/api/Global.BindingType) |  |

**Returns:** `string`

### `GetReadableTextOfGamepad(DewBinding)`

```csharp
public static string GetReadableTextOfGamepad(DewBinding b)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `b` | [DewBinding](/api/Global.DewBinding) |  |

**Returns:** `string`

### `GetReadableTextOfPC(DewBinding, out BindingType, int)`

```csharp
public static string GetReadableTextOfPC(DewBinding b, out BindingType type, int i = 0)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `b` | [DewBinding](/api/Global.DewBinding) |  |
| `type` | [BindingType](/api/Global.BindingType) |  |
| `i` | `int` |  |

**Returns:** `string`

### `GetReadableTextOfPC(DewBinding, int)`

```csharp
public static string GetReadableTextOfPC(DewBinding b, int i = 0)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `b` | [DewBinding](/api/Global.DewBinding) |  |
| `i` | `int` |  |

**Returns:** `string`

### `GetRightJoystick()`

Magnitude will be full range of 0 ~ 1 regardless of dead zone settings. Returns Vector2.zero if under dead zone.

```csharp
public static Vector2 GetRightJoystick()
```

**Returns:** `UnityEngine.Vector2`

### `IsGameRelatedMouseInputValid(MouseButton)`

```csharp
public static bool IsGameRelatedMouseInputValid(MouseButton button)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `button` | [MouseButton](/api/Global.MouseButton) |  |

**Returns:** `bool`

### `ListenAnyButtonRaw(Object, Func&lt;InputControl, bool&gt;)`

Return true in callback to stop listening.

```csharp
public static void ListenAnyButtonRaw(Object caller, Func<InputControl, bool> callback)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `caller` | `UnityEngine.Object` |  |
| `callback` | `System.Func&lt;T, TResult&gt;&lt;InputControl,bool&gt;` |  |

### `SetInputMode(InputMode)`

```csharp
public static void SetInputMode(InputMode mode)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `mode` | [InputMode](/api/Global.InputMode) |  |

### `StopListenAnyButton()`

```csharp
public static void StopListenAnyButton()
```
