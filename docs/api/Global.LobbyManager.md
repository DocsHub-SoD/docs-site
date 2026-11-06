# Class: LobbyManager

- **Category:** <span class="cat-dot" style="--cat-color: #3b82f6" data-cat="Managers & Systems"></span> Managers & Systems
- **Namespace:** `Global`
- **Assembly:** `Dew.Core.dll`
- **Inheritance / Derived:** [LogicBehaviour](/api/Global.LogicBehaviour) → `ManagerBase` → [LobbyManager](/api/Global.LobbyManager)

```csharp
public class LobbyManager : ManagerBase<LobbyManager>, ILogicUpdate
```

## Fields (2)

::: details Click to expand Fields (2)

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`onCurrentLobbyChanged`** | `public Action onCurrentLobbyChanged` |  |
| **`onLobbyListUpdated`** | `public Action onLobbyListUpdated` |  |

:::

## Properties (3)

::: details Click to expand Properties (3)

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`isLobbyLeader`** | `public bool isLobbyLeader { get; }` |  |
| **`service`** | `public LobbyServiceProvider service { get; }` |  |
| **`shouldRegisterUpdates`** | `public override bool shouldRegisterUpdates { get; }` |  |

:::

## Methods (3)

::: details `GetDefaultLobbyName()`

```csharp
public static string GetDefaultLobbyName()
```

**Returns:** `string`

:::

::: details `SwitchService()`

```csharp
public void SwitchService()
```

:::

::: details `SwitchService(LobbyServiceProvider)`

```csharp
public void SwitchService(LobbyServiceProvider newProvider)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `newProvider` | [`LobbyServiceProvider`](/api/Global.LobbyServiceProvider) |  |

:::


## Architecture & Relationships

::: details Click to expand Architecture & Relationships

### Used By (17)

*Classes and systems that invoke, reference, or depend on `LobbyManager`:*

`DewConsoleCommands` · [DewMod](/api/Global.DewMod) · [DewNetworkAuthenticator](/api/Global.DewNetworkAuthenticator) · [DewNetworkManager](/api/Global.DewNetworkManager) · [DewPlayer](/api/Global.DewPlayer) · [DewSave](/api/Global.DewSave) · [GameManager](/api/Global.GameManager) · [GameMod_Limbo](/api/Global.GameMod_Limbo) · [GameSettingsManager](/api/Global.GameSettingsManager) · `LobbyServiceEOS` · `UI_Lobby_InviteButtonController` · `UI_Lobby_LobbyID` · `UI_Lobby_LobbyNameGroup` · `UI_Lobby_LobbyType` · `UI_Lobby_PlayerListItem` · `UI_Title_CreateLobbyView` · `UI_Title_FindLobbyView`

### Dependencies (7)

*Types and components that `LobbyManager` references or depends upon:*

[DewBuildProfile](/api/Global.DewBuildProfile) · [DewLocalization](/api/Global.DewLocalization) · `LobbyServiceEOS` · [LobbyServiceProvider](/api/Global.LobbyServiceProvider) · [ManagerBase`1](/api/Global.ManagerBase`1) · [MessageManager](/api/Global.MessageManager) · [SafeAction](/api/Global.SafeAction)

:::
