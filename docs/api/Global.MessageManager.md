# Class: MessageManager

- **Category:** <span class="cat-dot" style="--cat-color: #eab308" data-cat="Items & Economy"></span> Items & Economy
- **Namespace:** `Global`
- **Assembly:** `Dew.Core.dll`
- **Inheritance / Derived:** [LogicBehaviour](/api/Global.LogicBehaviour) → `ManagerBase` → [MessageManager](/api/Global.MessageManager)

```csharp
public class MessageManager : ManagerBase<MessageManager>, ILogicUpdate
```

## Fields (3)

::: details Click to expand Fields (3)

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`buttons`** | `public List<GameObject> buttons` |  |
| **`canvasGroup`** | `public CanvasGroup canvasGroup` |  |
| **`contentText`** | `public TextMeshProUGUI contentText` |  |

:::

## Properties (1)

::: details Click to expand Properties (1)

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`isShowingMessage`** | `public bool isShowingMessage { get; }` |  |

:::

## Methods (9)

::: details `CloseMessage(ButtonType)`

```csharp
public void CloseMessage(DewMessageSettings.ButtonType button)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `button` | [`DewMessageSettings.ButtonType`](/api/Global.DewMessageSettings) |  |

:::

::: details `CloseMessageCancel()`

```csharp
public void CloseMessageCancel()
```

:::

::: details `CloseMessageNo()`

```csharp
public void CloseMessageNo()
```

:::

::: details `CloseMessageOk()`

```csharp
public void CloseMessageOk()
```

:::

::: details `CloseMessageYes()`

```csharp
public void CloseMessageYes()
```

:::

::: details `FrameUpdate()`

```csharp
public override void FrameUpdate()
```

:::

::: details `LogicUpdate(float)`

```csharp
public override void LogicUpdate(float dt)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `dt` | `float` |  |

:::

::: details `ShowMessage(DewMessageSettings)`

```csharp
public void ShowMessage(DewMessageSettings msg)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `msg` | [`DewMessageSettings`](/api/Global.DewMessageSettings) |  |

:::

::: details `ShowMessageLocalized(string)`

```csharp
public void ShowMessageLocalized(string id)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `id` | `string` |  |

:::


## Architecture & Relationships

::: details Click to expand Architecture & Relationships

### Used By (59)

*Classes and systems that invoke, reference, or depend on `MessageManager`:*

[CollectablesManager](/api/Global.CollectablesManager) · [ControlManager](/api/Global.ControlManager) · [Dew](/api/Global.Dew) · `DewConsoleCommands` · [DewInput](/api/Global.DewInput) · [DewPlayer](/api/Global.DewPlayer) · [GameMod_Limbo](/api/Global.GameMod_Limbo) · [GameSettingsManager](/api/Global.GameSettingsManager) · [GlobalUIManager](/api/Global.GlobalUIManager) · [InGameUIManager](/api/Global.InGameUIManager) · [LobbyManager](/api/Global.LobbyManager) · [LobbyServiceSteam](/api/Global.LobbyServiceSteam) · [PlayLobbyManager](/api/Global.PlayLobbyManager) · `Rev_AddToWishlist` · [Rift_RoomExit](/api/Global.Rift_RoomExit) · [Rift_Sidetrack](/api/Global.Rift_Sidetrack) · `Shrine_CookingPot` · `Shrine_Entanglement` · `Shrine_MirrorOfRemorse` · `Shrine_StarlessPath_EndingRift` · `Shrine_TheConsortOfNight_Rift` · [SkillTrigger](/api/Global.SkillTrigger) · [TitleManager](/api/Global.TitleManager) · `UI_Common_MenuView` · `UI_Constellations` · `UI_DemoPromotionBanner` · `UI_DiscordBanner` · [UI_GamepadTextInput](/api/Global.UI_GamepadTextInput) · `UI_InGame_Scoreboard_PlayerItem` · `UI_InGame_WorldMap` · `UI_InGame_World_NodeItem` · `UI_Lobby_CharacterView` · `UI_Lobby_Constellations` · `UI_Lobby_Constellations_HeroConstellation_StarSlot` · `UI_Lobby_Constellations_StarDetails` · `UI_Lobby_Constellations_StarList` · `UI_Lobby_DejavuButton` · `UI_Lobby_Emotes_Back` · `UI_Lobby_ObliterationView` · `UI_Lobby_PlayerListItem` · `UI_ModManager` · `UI_MusicBanner` · `UI_Reveries_DailySlot` · `UI_SelectControlPresetWindow` · `UI_Settings_Item_ResolutionDropdown` · `UI_Settings_View` · `UI_Title_CoopButtonManager` · `UI_Title_EULAView` · `UI_Title_FindLobbyView` · `UI_Title_MasteryRewardView` · `UI_Title_PrivateDemoNotice` · `UI_Title_ProfileSelection_DeleteProfileWindow` · `UI_Title_ProfileSelection_LinkEnterCodeWindow` · `UI_Title_ProfileSelection_LinkShowCodeWindow` · `UI_Title_ProfileSelection_ListWindow` · `UI_TooltipManager` · `UI_TravelerStory` · `UI_TravelerStory_Details_Story` · [ZoneManager](/api/Global.ZoneManager)

### Dependencies (9)

*Types and components that `MessageManager` references or depends upon:*

[BackHandler](/api/Global.BackHandler) · [Dew](/api/Global.Dew) · [DewInputTrigger](/api/Global.DewInputTrigger) · [DewLocalization](/api/Global.DewLocalization) · [DewMessageSettings](/api/Global.DewMessageSettings) · [GlobalUIManager](/api/Global.GlobalUIManager) · [LogicBehaviour](/api/Global.LogicBehaviour) · [ManagerBase`1](/api/Global.ManagerBase`1) · `UnityEngine.UI.DewContentSizeFitter`

:::
