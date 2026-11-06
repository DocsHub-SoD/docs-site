# Class: LobbyUIManager

- **Category:** <span class="cat-dot" style="--cat-color: #ec4899" data-cat="User Interface"></span> User Interface
- **Namespace:** `Global`
- **Assembly:** `Dew.Core.dll`
- **Inheritance / Derived:** [LogicBehaviour](/api/Global.LogicBehaviour) → `ManagerBase` → [UIManager](/api/Global.UIManager) → [UIManager](/api/Global.UIManager)

```csharp
public class LobbyUIManager : UIManager, ILogicUpdate
```

## Fields (1)

::: details Click to expand Fields (1)

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`lobbyEffect`** | `public GameObject lobbyEffect` |  |

:::

## Properties (2)

::: details Click to expand Properties (2)

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`instance`** | `public static LobbyUIManager instance { get; }` | If you expect the instance to be null, you MUST USE softInstance in Update loops.This will call FindObjectOfType if current instance is null, which can be very expensive. |
| **`softInstance`** | `public static LobbyUIManager softInstance { get; }` |  |

:::

## Methods (3)

::: details `LogicUpdate(float)`

```csharp
public override void LogicUpdate(float dt)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `dt` | `float` |  |

:::

::: details `OnStateChanged(string, string)`

```csharp
protected override void OnStateChanged(string oldState, string newState)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `oldState` | `string` |  |
| `newState` | `string` |  |

:::

::: details `OpenCharacterSelection()`

```csharp
public void OpenCharacterSelection()
```

:::


## Architecture & Relationships

::: details Click to expand Architecture & Relationships

### Used By (20)

*Classes and systems that invoke, reference, or depend on `LobbyUIManager`:*

[PlayLobbyManager](/api/Global.PlayLobbyManager) · [PlayLobby_Character](/api/Global.PlayLobby_Character) · [PlayLobby_RotateCharacterTutorial](/api/Global.PlayLobby_RotateCharacterTutorial) · `UI_Constellations` · [UI_EmoteWheel](/api/Global.UI_EmoteWheel) · `UI_Lobby_ChangeCharacterGamepadButton` · `UI_Lobby_CharacterRotator` · `UI_Lobby_CharacterView` · `UI_Lobby_Constellations` · `UI_Lobby_Constellations_HeroConstellation_StarSlot` · `UI_Lobby_Constellations_MiniHeroConstellation` · `UI_Lobby_DejavuButton` · `UI_Lobby_Emotes_Back` · `UI_Lobby_HeroList` · `UI_Lobby_Loadout_SkillSlot` · `UI_Lobby_PlayerNametag` · `UI_Lobby_SelectedHeroInfo_TravelerStoryButton` · `UI_Lobby_SendChatMessage` · `UI_PlayRewardAnnouncer` · `UI_Tooltip_SkillStarDescriber`

### Dependencies (6)

*Types and components that `LobbyUIManager` references or depends upon:*

[DewEffect](/api/Global.DewEffect) · [DewPlayer](/api/Global.DewPlayer) · [GlobalUIManager](/api/Global.GlobalUIManager) · [LogicBehaviour](/api/Global.LogicBehaviour) · [ManagerBase`1](/api/Global.ManagerBase`1) · [UIManager](/api/Global.UIManager)

:::
