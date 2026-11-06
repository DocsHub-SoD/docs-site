# Class: UIManager

- **Category:** <span class="cat-dot" style="--cat-color: #ec4899" data-cat="User Interface"></span> User Interface
- **Namespace:** `Global`
- **Assembly:** `Dew.Core.dll`
- **Inheritance / Derived:** [LogicBehaviour](/api/Global.LogicBehaviour) → `ManagerBase` → [UIManager](/api/Global.UIManager) → [InGameUIManager](/api/Global.InGameUIManager) → [LobbyUIManager](/api/Global.LobbyUIManager)

```csharp
public class UIManager : ManagerBase<UIManager>, ILogicUpdate
```

## Fields (1)

::: details Click to expand Fields (1)

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`onStateChanged`** | `public SafeAction<string, string> onStateChanged` |  |

:::

## Properties (2)

::: details Click to expand Properties (2)

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`availableStates`** | `public IReadOnlyCollection<string> availableStates { get; }` |  |
| **`state`** | `public string state { get; }` |  |

:::

## Methods (4)

::: details `IsState(string)`

```csharp
public bool IsState(string state)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `state` | `string` |  |

**Returns:** `bool`

:::

::: details `OnStateChanged(string, string)`

```csharp
protected virtual void OnStateChanged(string oldState, string newState)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `oldState` | `string` |  |
| `newState` | `string` |  |

:::

::: details `SetState(string)`

```csharp
public void SetState(string newState)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `newState` | `string` |  |

:::

::: details `ShouldDoAutoFocus()`

```csharp
public virtual bool ShouldDoAutoFocus()
```

**Returns:** `bool`

:::


## Architecture & Relationships

::: details Click to expand Architecture & Relationships

### Used By (45)

*Classes and systems that invoke, reference, or depend on `UIManager`:*

[CameraManager](/api/Global.CameraManager) · [ControlManager](/api/Global.ControlManager) · [CursorManager](/api/Global.CursorManager) · [DevGameManager](/api/Global.DevGameManager) · [DewNetworkManager](/api/Global.DewNetworkManager) · [EditSkillManager](/api/Global.EditSkillManager) · [FPSManager](/api/Global.FPSManager) · [GameResultManager](/api/Global.GameResultManager) · [GlobalUIManager](/api/Global.GlobalUIManager) · [InGameUIManager](/api/Global.InGameUIManager) · [LobbyUIManager](/api/Global.LobbyUIManager) · [ObjectHighlightManager](/api/Global.ObjectHighlightManager) · [PlayLobbyManager](/api/Global.PlayLobbyManager) · [PlayLobby_Character](/api/Global.PlayLobby_Character) · `PlayTutorialManager` · [TimescaleManager](/api/Global.TimescaleManager) · [TitleManager](/api/Global.TitleManager) · `UI_Common_MenuView` · `UI_Constellations` · `UI_CreditsView` · [UI_EmoteWheel](/api/Global.UI_EmoteWheel) · `UI_InGame_ArtifactStoryView` · `UI_InGame_CenterMessage` · `UI_InGame_InteractGroup` · `UI_Lobby_ChangeCharacterGamepadButton` · `UI_Lobby_CharacterRotator` · `UI_Lobby_CharacterView` · `UI_Lobby_Constellations` · `UI_Lobby_Constellations_HeroConstellation_StarSlot` · `UI_Lobby_Constellations_MiniHeroConstellation` · `UI_Lobby_DejavuButton` · `UI_Lobby_Emotes_Back` · `UI_Lobby_HeroList` · `UI_Lobby_Loadout_SkillSlot` · `UI_Lobby_ObliterationView` · `UI_Lobby_PlayerNametag` · `UI_Lobby_SelectedHeroInfo_TravelerStoryButton` · `UI_PlayRewardAnnouncer` · `UI_Title_EULAView` · `UI_Title_ProfileSelection_ListWindow` · `UI_Title_ProfileSelection_NewProfileWindow` · `UI_Title_ProfileSelection_RenameProfileWindow` · `UI_TooltipManager` · `UI_Tooltip_SkillStarDescriber` · [View](/api/Global.View)

### Dependencies (2)

*Types and components that `UIManager` references or depends upon:*

[ManagerBase`1](/api/Global.ManagerBase`1) · [SafeAction`2](/api/Global.SafeAction`2)

:::
