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
| `m` | <a href="/enums#mousebutton" class="enum-link" data-tooltip="None=0 · Left=1 · Right=2 · Middle=3 · Forward=4 (+3 more)">MouseButton</a> |  |
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
| `g` | <a href="/enums#gamepadbuttonex" class="enum-link" data-tooltip="DpadUp=0 · DpadDown=1 · DpadLeft=2 · DpadRight=3 · North=4 (+27 more)">GamepadButtonEx?</a> |  |

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
| `m` | <a href="/enums#mousebutton" class="enum-link" data-tooltip="None=0 · Left=1 · Right=2 · Middle=3 · Forward=4 (+3 more)">MouseButton</a> |  |
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
| `g` | <a href="/enums#gamepadbuttonex" class="enum-link" data-tooltip="DpadUp=0 · DpadDown=1 · DpadLeft=2 · DpadRight=3 · North=4 (+27 more)">GamepadButtonEx?</a> |  |

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
| `m` | <a href="/enums#mousebutton" class="enum-link" data-tooltip="None=0 · Left=1 · Right=2 · Middle=3 · Forward=4 (+3 more)">MouseButton</a> |  |
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
| `g` | <a href="/enums#gamepadbuttonex" class="enum-link" data-tooltip="DpadUp=0 · DpadDown=1 · DpadLeft=2 · DpadRight=3 · North=4 (+27 more)">GamepadButtonEx?</a> |  |

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
| `type` | <a href="/enums#bindingtype" class="enum-link" data-tooltip="None=0 · Keyboard=1 · Mouse=2 · Gamepad=4">BindingType</a> |  |

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
| `type` | <a href="/enums#bindingtype" class="enum-link" data-tooltip="None=0 · Keyboard=1 · Mouse=2 · Gamepad=4">BindingType</a> |  |

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
| `type` | <a href="/enums#bindingtype" class="enum-link" data-tooltip="None=0 · Keyboard=1 · Mouse=2 · Gamepad=4">BindingType</a> |  |
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
| `button` | <a href="/enums#mousebutton" class="enum-link" data-tooltip="None=0 · Left=1 · Right=2 · Middle=3 · Forward=4 (+3 more)">MouseButton</a> |  |

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
| `mode` | <a href="/enums#inputmode" class="enum-link" data-tooltip="KeyboardAndMouse=0 · Gamepad=1">InputMode</a> |  |

:::

::: details `StopListenAnyButton()`

```csharp
public static void StopListenAnyButton()
```

:::


## Architecture & Relationships

::: details Click to expand Architecture & Relationships

### Used By (84)

*Classes and systems that invoke, reference, or depend on `DewInput`:*

`ButtonDisplay` · [CameraManager](/api/Global.CameraManager) · [CollectablesManager](/api/Global.CollectablesManager) · `ContextMenu` · [ControlManager](/api/Global.ControlManager) · [DewBinding](/api/Global.DewBinding) · [DewControlSettings_User](/api/Global.DewControlSettings_User) · `DewInputReadableTextExtensions` · [DewLocalization](/api/Global.DewLocalization) · [DewPlayer](/api/Global.DewPlayer) · [DewSave](/api/Global.DewSave) · [EditSkillManager](/api/Global.EditSkillManager) · [FloatingWindowManager](/api/Global.FloatingWindowManager) · [FxCameraShake](/api/Global.FxCameraShake) · [GlobalUIManager](/api/Global.GlobalUIManager) · [InputManager](/api/Global.InputManager) · [ObjectHighlightManager](/api/Global.ObjectHighlightManager) · [PerControlVisibility](/api/Global.PerControlVisibility) · [PingManager](/api/Global.PingManager) · `Rev_AddToWishlist` · [UI_BindItem](/api/Global.UI_BindItem) · [UI_BindingWindow](/api/Global.UI_BindingWindow) · `UI_Collectables_MainView` · `UI_Collectables_ObjectDetails` · `UI_Collectables_ObjectItemProvider_Skill` · `UI_Common_ChatBox` · `UI_Common_MenuView` · `UI_Common_SkipButton` · `UI_Constellations` · `UI_Constellations_StarDetails` · `UI_ControllerDisconnectedIndicator` · `UI_CreditsView` · `UI_DemoPromotionBanner` · `UI_DiscordBanner` · `UI_DropdownControls` · `UI_EmoteList_EditEmote` · `UI_EmoteList_EditEmoteWheel_FloatingEmote` · `UI_EmoteList_EditEmoteWheel_Item` · `UI_EmoteList_Item` · [UI_EmoteWheel](/api/Global.UI_EmoteWheel) · `UI_EntityHealthBar` · `UI_EntityHealthBarMain` · [UI_GamepadBindButton](/api/Global.UI_GamepadBindButton) · [UI_GamepadInputField](/api/Global.UI_GamepadInputField) · `UI_GamepadScrollRect` · `UI_GamepadShoulderControls` · `UI_InGame_Conversations_Instance` · `UI_InGame_CooldownTimeNotification` · `UI_InGame_EditSkillIndicatorPositionByControl` · `UI_InGame_FloatingGem` · `UI_InGame_FloatingSkill` · `UI_InGame_GemSlot_EditSkill` · `UI_InGame_HeroDetailWindow` · `UI_InGame_HeroInfoBar` · `UI_InGame_InvertedControlsCursor` · `UI_InGame_MouseInputReceiver_EditSkill` · `UI_InGame_Result_HeroSkillItem` · `UI_InGame_ScoreboardView` · `UI_InGame_Scoreboard_PlayerItem_Skill` · `UI_InGame_SkillButton_EditSkill` · `UI_InGame_SkillButtons` · `UI_InGame_WorldMap` · `UI_InGame_World_NodeItem` · `UI_Lobby_CharacterRotator` · `UI_Lobby_CharacterView` · `UI_Lobby_Constellations` · `UI_Lobby_Constellations_FloatingStar` · `UI_Lobby_Constellations_HeroConstellation_StarSlot` · `UI_Lobby_Constellations_StarItem` · `UI_Lobby_Constellations_StarList` · `UI_Lobby_Emotes_Back` · `UI_Lobby_LobbyNameGroup` · `UI_Lobby_SendChatMessage` · `UI_MusicBanner` · `UI_PlayTutorial_AdvanceButton` · `UI_SelectControlPresetWindow` · `UI_Settings_View` · `UI_Title_FindLobbyView` · `UI_Title_LizardSmoothie` · `UI_Title_TitleView` · `UI_TooltipManager` · `UI_TooltipSection` · `UI_Tooltip_ObjEditSkillActions` · `UI_Tooltip_SkillExtraDetails`

### Dependencies (12)

*Types and components that `DewInput` references or depends upon:*

[ControlManager](/api/Global.ControlManager) · [Dew](/api/Global.Dew) · [DewBinding](/api/Global.DewBinding) · [DewBuildProfile](/api/Global.DewBuildProfile) · `DewInputReadableTextExtensions` · [DewLocalization](/api/Global.DewLocalization) · [InputManager](/api/Global.InputManager) · [ManagerBase`1](/api/Global.ManagerBase`1) · [MessageManager](/api/Global.MessageManager) · [NetworkedManagerBase`1](/api/Global.NetworkedManagerBase`1) · [SafeAction`2](/api/Global.SafeAction`2) · [SingletonBehaviour`1](/api/Global.SingletonBehaviour`1)

### Related Enums (5)

*Enumerations referenced in fields, properties, or method signatures:*

<a href="/enums#bindingtype" class="enum-link" data-tooltip="None=0 · Keyboard=1 · Mouse=2 · Gamepad=4">BindingType</a> · <a href="/enums#controllerbuttontype" class="enum-link" data-tooltip="Xbox=1 · PlayStation=2 · Generic=3">ControllerButtonType</a> · <a href="/enums#gamepadbuttonex" class="enum-link" data-tooltip="DpadUp=0 · DpadDown=1 · DpadLeft=2 · DpadRight=3 · North=4 (+27 more)">GamepadButtonEx</a> · <a href="/enums#inputmode" class="enum-link" data-tooltip="KeyboardAndMouse=0 · Gamepad=1">InputMode</a> · <a href="/enums#mousebutton" class="enum-link" data-tooltip="None=0 · Left=1 · Right=2 · Middle=3 · Forward=4 (+3 more)">MouseButton</a>

:::
