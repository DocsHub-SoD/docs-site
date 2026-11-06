# Class: DewBinding

- **Category:** <span class="cat-dot" style="--cat-color: #64748b" data-cat="Misc & Utility"></span> Misc & Utility
- **Namespace:** `Global`
- **Assembly:** `Dew.Core.dll`

```csharp
[Serializable]
public class DewBinding
```

## Fields (10)

::: details Click to expand Fields (10)

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`canAssignGamepad`** | `public bool canAssignGamepad` |  |
| **`canAssignKeyboard`** | `public bool canAssignKeyboard` |  |
| **`canAssignMouse`** | `public bool canAssignMouse` |  |
| **`gamepad`** | `[Obsolete] [Obsolete] public GamepadButtonEx? gamepad` |  |
| **`gamepadBinds`** | `public List<GamepadButtonEx> gamepadBinds` |  |
| **`keyboard`** | `[Obsolete] [Obsolete] public Key keyboard` |  |
| **`keyModifiers`** | `[Obsolete] [Obsolete] public List<Key> keyModifiers` |  |
| **`MockBinding`** | `public static readonly DewBinding MockBinding` |  |
| **`mouse`** | `[Obsolete] [Obsolete] public MouseButton mouse` |  |
| **`pcBinds`** | `public List<PCBind> pcBinds` |  |

:::

## Methods (12)

::: details `Clone()`

```csharp
public object Clone()
```

**Returns:** `object`

:::

::: details `CloneWith(GamepadButtonEx)`

```csharp
public DewBinding CloneWith(GamepadButtonEx added)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `added` | [`GamepadButtonEx`](/api/Global.GamepadButtonEx) |  |

**Returns:** `DewBinding`

:::

::: details `CloneWith(MouseButton)`

```csharp
public DewBinding CloneWith(MouseButton added)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `added` | [`MouseButton`](/api/Global.MouseButton) |  |

**Returns:** `DewBinding`

:::

::: details `CloneWith(Key)`

```csharp
public DewBinding CloneWith(Key added)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `added` | `UnityEngine.InputSystem.Key` |  |

**Returns:** `DewBinding`

:::

::: details `GamepadOnly(params object[])`

```csharp
public static DewBinding GamepadOnly(params object[] keys)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `keys` | `object[]` |  |

**Returns:** `DewBinding`

:::

::: details `GetBindingTypes()`

```csharp
public BindingType GetBindingTypes()
```

**Returns:** `BindingType`

:::

::: details `HasAssignedForCurrentMode()`

```csharp
public bool HasAssignedForCurrentMode()
```

**Returns:** `bool`

:::

::: details `HasGamepadAssigned()`

```csharp
public bool HasGamepadAssigned()
```

**Returns:** `bool`

:::

::: details `HasPCAssigned()`

```csharp
public bool HasPCAssigned()
```

**Returns:** `bool`

:::

::: details `KeyboardAndMouseOnly(params object[])`

```csharp
public static DewBinding KeyboardAndMouseOnly(params object[] keys)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `keys` | `object[]` |  |

**Returns:** `DewBinding`

:::

::: details `KeyboardOnly(params object[])`

```csharp
public static DewBinding KeyboardOnly(params object[] keys)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `keys` | `object[]` |  |

**Returns:** `DewBinding`

:::

::: details `PCAndGamepad(params object[])`

```csharp
public static DewBinding PCAndGamepad(params object[] keys)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `keys` | `object[]` |  |

**Returns:** `DewBinding`

:::


## Architecture & Relationships

::: details Click to expand Architecture & Relationships

### Used By (9)

*Classes and systems that invoke, reference, or depend on `DewBinding`:*

`ButtonDisplay` · [ControlManager](/api/Global.ControlManager) · [DewControlSettings_User](/api/Global.DewControlSettings_User) · [DewInput](/api/Global.DewInput) · [DewInputTrigger](/api/Global.DewInputTrigger) · [UI_BindItem](/api/Global.UI_BindItem) · [UI_BindingWindow](/api/Global.UI_BindingWindow) · `UI_InGame_Conversations_Instance` · `UI_Settings_Item_DewBinding`

### Dependencies (2)

*Types and components that `DewBinding` references or depends upon:*

[DewInput](/api/Global.DewInput) · [PCBind](/api/Global.PCBind)

### Related Enums (3)

*Enumerations referenced in fields, properties, or method signatures:*

[`BindingType`](/enums#bindingtype) · [`GamepadButtonEx`](/enums#gamepadbuttonex) · [`MouseButton`](/enums#mousebutton)

:::
