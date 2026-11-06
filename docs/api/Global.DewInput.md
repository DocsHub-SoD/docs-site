# Class: DewInput

- **Category:** <span class="cat-dot" style="--cat-color: #64748b" data-cat="Misc & Utility"></span> Misc & Utility
- **Namespace:** `Global`
- **Assembly:** `Dew.Core.dll`

```csharp
public static class DewInput
```

## Fields (3)

::: details Click to expand Fields (3)

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`ModifierKeys`** | `public static readonly List<Key> ModifierKeys` |  |
| **`NameToMouseButton`** | `public static readonly IReadOnlyDictionary<string, MouseButton> NameToMouseButton` |  |
| **`onCurrentModeChanged`** | `public static SafeAction<InputMode, InputMode> onCurrentModeChanged` |  |

:::

## Properties (2)

::: details Click to expand Properties (2)

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`controllerButtonType`** | `public static ControllerButtonType controllerButtonType { get; }` |  |
| **`currentMode`** | `public static InputMode currentMode { get; }` |  |

:::

## Methods (27)

::: details `GetButton(DewBinding, bool)`

```csharp
public static bool GetButton(DewBinding b, bool checkGameAreaForMouse)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `b` | [`DewBinding`](/api/Global.DewBinding) |  |
| `checkGameAreaForMouse` | `bool` |  |

**Returns:** `bool`

:::

::: details `GetButton(MouseButton, bool)`

```csharp
public static bool GetButton(MouseButton m, bool checkGameArea)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `m` | [`MouseButton`](/api/Global.MouseButton) |  |
| `checkGameArea` | `bool` |  |

**Returns:** `bool`

:::

::: details `GetButton(GamepadButtonEx?)`

```csharp
public static bool GetButton(GamepadButtonEx? g)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `g` | [`GamepadButtonEx?`](/api/Global.GamepadButtonEx) |  |

**Returns:** `bool`

:::

::: details `GetButton(Key)`

```csharp
public static bool GetButton(Key k)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `k` | `UnityEngine.InputSystem.Key` |  |

**Returns:** `bool`

:::

::: details `GetButtonDown(DewBinding, bool)`

```csharp
public static bool GetButtonDown(DewBinding b, bool checkGameAreaForMouse)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `b` | [`DewBinding`](/api/Global.DewBinding) |  |
| `checkGameAreaForMouse` | `bool` |  |

**Returns:** `bool`

:::

::: details `GetButtonDown(MouseButton, bool)`

```csharp
public static bool GetButtonDown(MouseButton m, bool checkGameArea)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `m` | [`MouseButton`](/api/Global.MouseButton) |  |
| `checkGameArea` | `bool` |  |

**Returns:** `bool`

:::

::: details `GetButtonDown(GamepadButtonEx?)`

```csharp
public static bool GetButtonDown(GamepadButtonEx? g)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `g` | [`GamepadButtonEx?`](/api/Global.GamepadButtonEx) |  |

**Returns:** `bool`

:::

::: details `GetButtonDown(Key)`

```csharp
public static bool GetButtonDown(Key k)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `k` | `UnityEngine.InputSystem.Key` |  |

**Returns:** `bool`

:::

::: details `GetButtonDownAnyGamepad()`

```csharp
public static bool GetButtonDownAnyGamepad()
```

**Returns:** `bool`

:::

::: details `GetButtonDownAnyKey()`

```csharp
public static bool GetButtonDownAnyKey()
```

**Returns:** `bool`

:::

::: details `GetButtonDownAnyMouse()`

```csharp
public static bool GetButtonDownAnyMouse()
```

**Returns:** `bool`

:::

::: details `GetButtonUp(DewBinding, bool)`

```csharp
public static bool GetButtonUp(DewBinding b, bool checkGameAreaForMouse)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `b` | [`DewBinding`](/api/Global.DewBinding) |  |
| `checkGameAreaForMouse` | `bool` |  |

**Returns:** `bool`

:::

::: details `GetButtonUp(MouseButton, bool)`

```csharp
public static bool GetButtonUp(MouseButton m, bool checkGameArea)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `m` | [`MouseButton`](/api/Global.MouseButton) |  |
| `checkGameArea` | `bool` |  |

**Returns:** `bool`

:::

::: details `GetButtonUp(GamepadButtonEx?)`

```csharp
public static bool GetButtonUp(GamepadButtonEx? g)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `g` | [`GamepadButtonEx?`](/api/Global.GamepadButtonEx) |  |

**Returns:** `bool`

:::

::: details `GetButtonUp(Key)`

```csharp
public static bool GetButtonUp(Key k)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `k` | `UnityEngine.InputSystem.Key` |  |

**Returns:** `bool`

:::

::: details `GetLeftJoystick()`

Magnitude will be full range of 0 ~ 1 regardless of dead zone settings. Returns Vector2.zero if under dead zone.

```csharp
public static Vector2 GetLeftJoystick()
```

**Returns:** `UnityEngine.Vector2`

:::

::: details `GetReadableTextForCurrentMode(DewBinding, out BindingType)`

```csharp
public static string GetReadableTextForCurrentMode(DewBinding b, out BindingType type)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `b` | [`DewBinding`](/api/Global.DewBinding) |  |
| `type` | [`BindingType`](/api/Global.BindingType) |  |

**Returns:** `string`

:::

::: details `GetReadableTextForCurrentMode(DewBinding)`

```csharp
public static string GetReadableTextForCurrentMode(DewBinding b)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `b` | [`DewBinding`](/api/Global.DewBinding) |  |

**Returns:** `string`

:::

::: details `GetReadableTextOfGamepad(DewBinding, out BindingType)`

```csharp
public static string GetReadableTextOfGamepad(DewBinding b, out BindingType type)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `b` | [`DewBinding`](/api/Global.DewBinding) |  |
| `type` | [`BindingType`](/api/Global.BindingType) |  |

**Returns:** `string`

:::

::: details `GetReadableTextOfGamepad(DewBinding)`

```csharp
public static string GetReadableTextOfGamepad(DewBinding b)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `b` | [`DewBinding`](/api/Global.DewBinding) |  |

**Returns:** `string`

:::

::: details `GetReadableTextOfPC(DewBinding, out BindingType, int)`

```csharp
public static string GetReadableTextOfPC(DewBinding b, out BindingType type, int i = 0)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `b` | [`DewBinding`](/api/Global.DewBinding) |  |
| `type` | [`BindingType`](/api/Global.BindingType) |  |
| `i` | `int` |  |

**Returns:** `string`

:::

::: details `GetReadableTextOfPC(DewBinding, int)`

```csharp
public static string GetReadableTextOfPC(DewBinding b, int i = 0)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `b` | [`DewBinding`](/api/Global.DewBinding) |  |
| `i` | `int` |  |

**Returns:** `string`

:::

::: details `GetRightJoystick()`

Magnitude will be full range of 0 ~ 1 regardless of dead zone settings. Returns Vector2.zero if under dead zone.

```csharp
public static Vector2 GetRightJoystick()
```

**Returns:** `UnityEngine.Vector2`

:::

::: details `IsGameRelatedMouseInputValid(MouseButton)`

```csharp
public static bool IsGameRelatedMouseInputValid(MouseButton button)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `button` | [`MouseButton`](/api/Global.MouseButton) |  |

**Returns:** `bool`

:::

::: details `ListenAnyButtonRaw(Object, Func&lt;InputControl, bool&gt;)`

Return true in callback to stop listening.

```csharp
public static void ListenAnyButtonRaw(Object caller, Func<InputControl, bool> callback)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `caller` | `UnityEngine.Object` |  |
| `callback` | `System.Func<T, TResult><InputControl,bool>` |  |

:::

::: details `SetInputMode(InputMode)`

```csharp
public static void SetInputMode(InputMode mode)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `mode` | [`InputMode`](/api/Global.InputMode) |  |

:::

::: details `StopListenAnyButton()`

```csharp
public static void StopListenAnyButton()
```

:::
