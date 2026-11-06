# Class: DewBinding

- **Category:** <span class="cat-dot" style="--cat-color: #64748b" data-cat="Misc & Utility"></span> Misc & Utility
- **Namespace:** `Global`
- **Assembly:** `Dew.Core.dll`

```csharp
[Serializable]
public class DewBinding
```

## Fields

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`canAssignGamepad`** | `public bool canAssignGamepad` |  |
| **`canAssignKeyboard`** | `public bool canAssignKeyboard` |  |
| **`canAssignMouse`** | `public bool canAssignMouse` |  |
| **`gamepad`** | `[Obsolete] public GamepadButtonEx? gamepad` |  |
| **`gamepadBinds`** | `public List<GamepadButtonEx> gamepadBinds` |  |
| **`keyboard`** | `[Obsolete] public Key keyboard` |  |
| **`keyModifiers`** | `[Obsolete] public List<Key> keyModifiers` |  |
| **`MockBinding`** | `public static readonly DewBinding MockBinding` |  |
| **`mouse`** | `[Obsolete] public MouseButton mouse` |  |
| **`pcBinds`** | `public List<PCBind> pcBinds` |  |

## Methods

### `Clone()`

```csharp
public object Clone()
```

**Returns:** `object`

### `CloneWith(GamepadButtonEx)`

```csharp
public DewBinding CloneWith(GamepadButtonEx added)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `added` | [`GamepadButtonEx`](/api/Global.GamepadButtonEx) |  |

**Returns:** `DewBinding`

### `CloneWith(MouseButton)`

```csharp
public DewBinding CloneWith(MouseButton added)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `added` | [`MouseButton`](/api/Global.MouseButton) |  |

**Returns:** `DewBinding`

### `CloneWith(Key)`

```csharp
public DewBinding CloneWith(Key added)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `added` | `UnityEngine.InputSystem.Key` |  |

**Returns:** `DewBinding`

### `GamepadOnly(params object[])`

```csharp
public static DewBinding GamepadOnly(params object[] keys)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `keys` | `object[]` |  |

**Returns:** `DewBinding`

### `GetBindingTypes()`

```csharp
public BindingType GetBindingTypes()
```

**Returns:** `BindingType`

### `HasAssignedForCurrentMode()`

```csharp
public bool HasAssignedForCurrentMode()
```

**Returns:** `bool`

### `HasGamepadAssigned()`

```csharp
public bool HasGamepadAssigned()
```

**Returns:** `bool`

### `HasPCAssigned()`

```csharp
public bool HasPCAssigned()
```

**Returns:** `bool`

### `KeyboardAndMouseOnly(params object[])`

```csharp
public static DewBinding KeyboardAndMouseOnly(params object[] keys)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `keys` | `object[]` |  |

**Returns:** `DewBinding`

### `KeyboardOnly(params object[])`

```csharp
public static DewBinding KeyboardOnly(params object[] keys)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `keys` | `object[]` |  |

**Returns:** `DewBinding`

### `PCAndGamepad(params object[])`

```csharp
public static DewBinding PCAndGamepad(params object[] keys)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `keys` | `object[]` |  |

**Returns:** `DewBinding`
