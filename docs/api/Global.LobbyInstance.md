# Class: LobbyInstance

- **Category:** <span class="cat-dot" style="--cat-color: #06b6d4" data-cat="Networking"></span> Networking
- **Namespace:** `Global`
- **Assembly:** `Dew.Core.dll`
- **Inheritance / Derived:** [LobbyInstanceSteam](/api/Global.LobbyInstanceSteam)

```csharp
public class LobbyInstance
```

## Fields (23)

::: details Click to expand Fields (23)

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`activeLucidDreams`** | `public List<string> activeLucidDreams` |  |
| **`allowDejavu`** | `public bool allowDejavu` |  |
| **`allowJoin`** | `public bool allowJoin` |  |
| **`allowMidJoins`** | `public AllowMidJoinType allowMidJoins` |  |
| **`bannedGameItems`** | `public List<string> bannedGameItems` |  |
| **`connectionQuality`** | `public LobbyConnectionQuality connectionQuality` |  |
| **`currentPlayers`** | `public int currentPlayers` |  |
| **`customData`** | `public Dictionary<string, string> customData` |  |
| **`difficulty`** | `public string difficulty` |  |
| **`gameServerAddress`** | `public string gameServerAddress` |  |
| **`gameStartTimestamp`** | `public long gameStartTimestamp` |  |
| **`hasGameStarted`** | `public bool hasGameStarted` |  |
| **`id`** | `public string id` |  |
| **`isInviteOnly`** | `public bool isInviteOnly` |  |
| **`isLobbyLeader`** | `public bool isLobbyLeader` |  |
| **`isModded`** | `public bool isModded` |  |
| **`lobbyDescription`** | `public string lobbyDescription` |  |
| **`lobbyName`** | `public string lobbyName` |  |
| **`lobbyTags`** | `public List<string> lobbyTags` |  |
| **`maxPlayers`** | `public int maxPlayers` |  |
| **`savedPlayers`** | `public List<string> savedPlayers` |  |
| **`shortCode`** | `public string shortCode` |  |
| **`version`** | `public string version` |  |

:::

## Methods (1)

::: details `ToString()`

```csharp
public override string ToString()
```

**Returns:** `string`

:::


## Architecture & Relationships

::: details Click to expand Architecture & Relationships

### Used By (8)

*Classes and systems that invoke, reference, or depend on `LobbyInstance`:*

[DewNetworkManager](/api/Global.DewNetworkManager) · [GameMod_Limbo](/api/Global.GameMod_Limbo) · `LobbyInstanceEpic` · [LobbyInstanceSteam](/api/Global.LobbyInstanceSteam) · `LobbyServiceEOS` · [LobbyServiceProvider](/api/Global.LobbyServiceProvider) · [LobbyServiceSteam](/api/Global.LobbyServiceSteam) · `UI_Title_FindLobby_LobbyItem`

### Dependencies (0)

*No outgoing class dependencies recorded.*

### Related Enums (2)

*Enumerations referenced in fields, properties, or method signatures:*

[`AllowMidJoinType`](/enums#allowmidjointype) · [`LobbyConnectionQuality`](/enums#lobbyconnectionquality)

:::
