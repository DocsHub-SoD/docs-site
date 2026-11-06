# Class: UI_Toggle

- **Category:** <span class="cat-dot" style="--cat-color: #ec4899" data-cat="User Interface"></span> User Interface
- **Namespace:** `Global`
- **Assembly:** `Dew.Core.dll`

```csharp
public class UI_Toggle : MonoBehaviour
```

## Fields (6)

::: details Click to expand Fields (6)

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`doNotToggleOnClick`** | `public bool doNotToggleOnClick` |  |
| **`index`** | `public int index` |  |
| **`offObject`** | `public GameObject offObject` |  |
| **`onClick`** | `public UnityEvent onClick` |  |
| **`onIsCheckedChanged`** | `public UnityEvent<bool> onIsCheckedChanged` |  |
| **`onObject`** | `public GameObject onObject` |  |

:::

## Properties (2)

::: details Click to expand Properties (2)

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`interactable`** | `public bool interactable { get; set; }` |  |
| **`isChecked`** | `public bool isChecked { get; set; }` |  |

:::


## Architecture & Relationships

::: details Click to expand Architecture & Relationships

### Used By (25)

*Classes and systems that invoke, reference, or depend on `UI_Toggle`:*

[DewGUI](/api/Global.DewGUI) · `UI_AccList_Item` · `UI_Collectables_ObjectItem` · `UI_EmoteList_Item` · `UI_EmoteList_Item_GamepadFocusable` · `UI_InGame_HeroDetailWindow` · `UI_InGame_ResultView` · `UI_InGame_Scoreboard_PlayerItem` · `UI_Lobby_AccList` · `UI_Lobby_AllowDejavu` · `UI_Lobby_Constellations` · `UI_Lobby_Constellations_QuickLoadoutSwitch` · `UI_Lobby_Constellations_StarItem` · `UI_Lobby_DejavuWindow_Item` · `UI_Lobby_EnableVotes` · `UI_Lobby_NametagList` · `UI_Lobby_ObliterationView_Item` · `UI_Lobby_PlayerListItem` · `UI_Lobby_StartButtonController` · `UI_ModManager` · `UI_NametagList_Item` · `UI_Settings_Item` · `UI_Settings_Item_ResetTutorial` · `UI_SkinList_Item` · [UI_ToggleGroup](/api/Global.UI_ToggleGroup)

### Dependencies (1)

*Types and components that `UI_Toggle` references or depends upon:*

[UI_ToggleGroup](/api/Global.UI_ToggleGroup)

:::
