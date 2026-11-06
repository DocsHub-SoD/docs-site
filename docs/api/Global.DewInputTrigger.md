# Class: DewInputTrigger

- **Category:** <span class="cat-dot" style="--cat-color: #64748b" data-cat="Misc & Utility"></span> Misc & Utility
- **Namespace:** `Global`
- **Assembly:** `Dew.Core.dll`

```csharp
public class DewInputTrigger
```

## Fields (8)

::: details Click to expand Fields (8)

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`binding`** | `public Func<DewBinding> binding` |  |
| **`canConsume`** | `public bool canConsume` |  |
| **`checkGameAreaForMouse`** | `public bool checkGameAreaForMouse` |  |
| **`ignoreConsumeCheck`** | `public bool ignoreConsumeCheck` |  |
| **`isValidCheck`** | `public Func<bool> isValidCheck` |  |
| **`MockTrigger`** | `public static DewInputTrigger MockTrigger` |  |
| **`owner`** | `public Object owner` |  |
| **`priority`** | `public int priority` | Lower will be checked first. |

:::

## Properties (3)

::: details Click to expand Properties (3)

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`down`** | `public bool down { get; }` |  |
| **`downRepeated`** | `public bool downRepeated { get; }` |  |
| **`up`** | `public bool up { get; }` |  |

:::


## Architecture & Relationships

::: details Click to expand Architecture & Relationships

### Used By (20)

*Classes and systems that invoke, reference, or depend on `DewInputTrigger`:*

[CameraManager](/api/Global.CameraManager) · [ControlManager](/api/Global.ControlManager) · [EditSkillManager](/api/Global.EditSkillManager) · [GlobalUIManager](/api/Global.GlobalUIManager) · [InGameUIManager](/api/Global.InGameUIManager) · [InputManager](/api/Global.InputManager) · [MessageManager](/api/Global.MessageManager) · [SampleCastInfoContext](/api/Global.SampleCastInfoContext) · [UI_BackButtonHandler](/api/Global.UI_BackButtonHandler) · `UI_Common_ChatBox` · `UI_Common_SkipButton` · [UI_EmoteWheel](/api/Global.UI_EmoteWheel) · [UI_GamepadBindButton](/api/Global.UI_GamepadBindButton) · `UI_GamepadShoulderControls` · [UI_GamepadTextInput](/api/Global.UI_GamepadTextInput) · `UI_InGame_Conversations_Instance` · `UI_InGame_HeroDetailWindow` · `UI_InGame_HeroInfoBar` · `UI_Lobby_Constellations` · `UI_Lobby_Constellations_StarDetails`

### Dependencies (3)

*Types and components that `DewInputTrigger` references or depends upon:*

[DewBinding](/api/Global.DewBinding) · [InputManager](/api/Global.InputManager) · [ManagerBase`1](/api/Global.ManagerBase`1)

:::
