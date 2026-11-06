# Class: DewNetworkStartSettings

- **Category:** <span class="cat-dot" style="--cat-color: #06b6d4" data-cat="Networking"></span> Networking
- **Namespace:** `Global`
- **Assembly:** `Dew.Core.dll`

```csharp
public class DewNetworkStartSettings
```

## Fields (9)

::: details Click to expand Fields (9)

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`addedGameMods`** | `public List<string> addedGameMods` |  |
| **`address`** | `public string address` |  |
| **`continueData`** | `public DewPersistence.GameData continueData` |  |
| **`customGameSettingsSaveKey`** | `public string customGameSettingsSaveKey` |  |
| **`lanMode`** | `public bool lanMode` |  |
| **`lobbyName`** | `public string lobbyName` |  |
| **`lobbyType`** | `public DewLobbyType lobbyType` |  |
| **`maxPlayers`** | `public int maxPlayers` |  |
| **`networkMode`** | `public DewNetworkMode networkMode` |  |

:::


## Architecture & Relationships

::: details Click to expand Architecture & Relationships

### Used By (5)

*Classes and systems that invoke, reference, or depend on `DewNetworkStartSettings`:*

[DewNetworkManager](/api/Global.DewNetworkManager) · [GameSettingsManager](/api/Global.GameSettingsManager) · `LobbyServiceEOS` · [TransitionManager](/api/Global.TransitionManager) · `UI_Title_CreateLobbyView`

### Dependencies (0)

*No outgoing class dependencies recorded.*

### Related Enums (2)

*Enumerations referenced in fields, properties, or method signatures:*

<a href="/enums#dewlobbytype" class="enum-link" data-tooltip="Public=0 · InviteOnly=1">DewLobbyType</a> · <a href="/enums#dewnetworkmode" class="enum-link" data-tooltip="Singleplayer=0 · MultiplayerHost=1 · MultiplayerJoinLobby=2 · MultiplayerHostRestart=3 · MultiplayerJoinRestart=4">DewNetworkMode</a>

:::
