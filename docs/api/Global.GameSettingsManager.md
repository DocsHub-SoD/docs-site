# Class: GameSettingsManager

- **Category:** <span class="cat-dot" style="--cat-color: #3b82f6" data-cat="Managers & Systems"></span> Managers & Systems
- **Namespace:** `Global`
- **Assembly:** `Dew.Core.dll`
- **Inheritance / Derived:** [DewNetworkBehaviour](/api/Global.DewNetworkBehaviour) → `NetworkedManagerBase` → [GameSettingsManager](/api/Global.GameSettingsManager)

```csharp
public class GameSettingsManager : NetworkedManagerBase<GameSettingsManager>, ILogicUpdate
```

## Fields (16)

::: details Click to expand Fields (16)

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`activeLucidDreams`** | `[SaveVar] [SaveVar(SaveVarFlags.Default)] public readonly SyncList<string> activeLucidDreams` |  |
| **`addedGameMods`** | `[SaveVar] [SaveVar(SaveVarFlags.Default)] public readonly SyncList<string> addedGameMods` | This should not be changed after starting the server. |
| **`availableLucidDreams`** | `[SaveVar] [SaveVar(SaveVarFlags.Default)] public readonly SyncList<string> availableLucidDreams` |  |
| **`bannedGameItems`** | `[SaveVar] [SaveVar(SaveVarFlags.Default)] public readonly SyncList<string> bannedGameItems` |  |
| **`ClientEvent_OnActiveLucidDreamsChanged`** | `public SafeAction ClientEvent_OnActiveLucidDreamsChanged` |  |
| **`ClientEvent_OnAvailableLucidDreamsChanged`** | `public SafeAction ClientEvent_OnAvailableLucidDreamsChanged` |  |
| **`ClientEvent_OnBannedItemsChanged`** | `public SafeAction ClientEvent_OnBannedItemsChanged` |  |
| **`ClientEvent_OnCustomDataChanged`** | `public SafeAction<string> ClientEvent_OnCustomDataChanged` |  |
| **`ClientEvent_OnDifficultyChanged`** | `public SafeAction<string, string> ClientEvent_OnDifficultyChanged` |  |
| **`ClientEvent_OnLobbyTagsChanged`** | `public SafeAction ClientEvent_OnLobbyTagsChanged` |  |
| **`ClientEvent_OnStateChanged`** | `public SafeAction ClientEvent_OnStateChanged` |  |
| **`ClientEvent_OnUnlockedGameItemsChanged`** | `public SafeAction ClientEvent_OnUnlockedGameItemsChanged` |  |
| **`customData`** | `[SaveVar] [SaveVar(SaveVarFlags.Default)] public readonly SyncDictionary<string, string> customData` |  |
| **`lobbyTags`** | `[SaveVar] [SaveVar(SaveVarFlags.Default)] public readonly SyncList<string> lobbyTags` |  |
| **`localPlayerDejavuCost`** | `public int localPlayerDejavuCost` |  |
| **`unlockedGameItems`** | `[SaveVar] [SaveVar(SaveVarFlags.Default)] public readonly SyncList<string> unlockedGameItems` |  |

:::

## Properties (11)

::: details Click to expand Properties (11)

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`allowDejavu`** | `[SaveVar] [SaveVar(SaveVarFlags.Default)] public bool allowDejavu { get; set; }` |  |
| **`allowMidJoins`** | `[SaveVar] [SaveVar(SaveVarFlags.Default)] public AllowMidJoinType allowMidJoins { get; set; }` |  |
| **`difficulty`** | `[SaveVar] [SaveVar(SaveVarFlags.Default)] public string difficulty { get; set; }` |  |
| **`enableVotes`** | `[SaveVar] [SaveVar(SaveVarFlags.Default)] public bool enableVotes { get; set; }` |  |
| **`gameSettingsSaveKey`** | `[SaveVar] [SaveVar(SaveVarFlags.Default)] public string gameSettingsSaveKey { get; set; }` |  |
| **`lobbyDescription`** | `[SaveVar] [SaveVar(SaveVarFlags.Default)] public string lobbyDescription { get; set; }` |  |
| **`lobbyName`** | `[SaveVar] [SaveVar(SaveVarFlags.Default)] public string lobbyName { get; set; }` |  |
| **`maxPlayers`** | `[SaveVar] [SaveVar(SaveVarFlags.Default)] public int maxPlayers { get; set; }` |  |
| **`midJoinBanType`** | `[SaveVar] [SaveVar(SaveVarFlags.Default)] public MidJoinBanType midJoinBanType { get; set; }` | This is irreversible by design. |
| **`midJoinWaitType`** | `public MidJoinWaitType midJoinWaitType { get; set; }` | This should be set and unset accordingly mid-run. |
| **`state`** | `public GameState state { get; set; }` |  |

:::

## Methods (18)

::: details `AddLucidDream(string)`

```csharp
public void AddLucidDream(string type)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `type` | `string` |  |

:::

::: details `Awake()`

```csharp
protected override void Awake()
```

:::

::: details `ClearLucidDreams()`

```csharp
public void ClearLucidDreams()
```

:::

::: details `DisconnectByMidJoinBan()`

```csharp
public void DisconnectByMidJoinBan()
```

:::

::: details `DisconnectByMidJoinWaitBlock()`

```csharp
public void DisconnectByMidJoinWaitBlock()
```

:::

::: details `GetLocalPreferredGameSettings()`

```csharp
public PreferredGameSettings GetLocalPreferredGameSettings()
```

**Returns:** `PreferredGameSettings`

:::

::: details `Lobby_UpdateAttribute(string)`

```csharp
public UniTask Lobby_UpdateAttribute(string key)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `key` | `string` |  |

**Returns:** `Cysharp.Threading.Tasks.UniTask`

:::

::: details `Lobby_UpdateCanJoinAndGameStarted(bool?)`

```csharp
public UniTask Lobby_UpdateCanJoinAndGameStarted(bool? hasGameStartedOverride = null)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `hasGameStartedOverride` | `bool?` |  |

**Returns:** `Cysharp.Threading.Tasks.UniTask`

:::

::: details `Lobby_UpdateGameAttributes()`

```csharp
public UniTask Lobby_UpdateGameAttributes()
```

**Returns:** `Cysharp.Threading.Tasks.UniTask`

:::

::: details `Lobby_UpdateGameStartTimestamp()`

```csharp
public UniTask Lobby_UpdateGameStartTimestamp()
```

**Returns:** `Cysharp.Threading.Tasks.UniTask`

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

::: details `OnStartClient()`

```csharp
public override void OnStartClient()
```

:::

::: details `OnStartServer()`

```csharp
public override void OnStartServer()
```

:::

::: details `OnStopServer()`

```csharp
public override void OnStopServer()
```

:::

::: details `RemoveLucidDream(string)`

```csharp
public void RemoveLucidDream(string type)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `type` | `string` |  |

:::

::: details `SetEnableVotes(bool)`

```csharp
public void SetEnableVotes(bool value)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `value` | `bool` |  |

:::

::: details `UpdateAvailableLucidDreams()`

```csharp
public void UpdateAvailableLucidDreams()
```

:::

::: details `ValidateBannedItems(bool)`

```csharp
public void ValidateBannedItems(bool printMessage)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `printMessage` | `bool` |  |

:::


## Architecture & Relationships

::: details Click to expand Architecture & Relationships

### Used By (30)

*Classes and systems that invoke, reference, or depend on `GameSettingsManager`:*

[BossMonster](/api/Global.BossMonster) · [DewEffect](/api/Global.DewEffect) · [DewMod](/api/Global.DewMod) · [DewNetworkAuthenticator](/api/Global.DewNetworkAuthenticator) · [DewNetworkManager](/api/Global.DewNetworkManager) · [DewPlayer](/api/Global.DewPlayer) · [GameManager](/api/Global.GameManager) · [GameMod_Limbo](/api/Global.GameMod_Limbo) · [InGameUIManager](/api/Global.InGameUIManager) · `LobbyServiceEOS` · [PlayGameManager](/api/Global.PlayGameManager) · [PlayLobbyManager](/api/Global.PlayLobbyManager) · [PreferredGameSettings](/api/Global.PreferredGameSettings) · `StarlessPath_BossPolarisManager` · `UI_Lobby_AllowDejavu` · `UI_Lobby_AllowMidJoins` · `UI_Lobby_Constellations` · `UI_Lobby_Constellations_QuickLoadoutSwitch` · `UI_Lobby_DejavuButton_ActivationManager` · `UI_Lobby_DifficultyItem` · `UI_Lobby_EnableVotes` · `UI_Lobby_Loadout_AvailableSkills` · `UI_Lobby_LobbyNameGroup` · `UI_Lobby_LucidDreamsWindow_Item` · `UI_Lobby_LucidDreams_Item` · `UI_Lobby_MidJoinWaitObject` · `UI_Lobby_ReadyStatusText` · `UI_Lobby_StartButtonController` · `UI_Lobby_WaitingForContinueMidJoin_Loading` · [ZoneManager](/api/Global.ZoneManager)

### Dependencies (20)

*Types and components that `GameSettingsManager` references or depends upon:*

[Dew](/api/Global.Dew) · [DewLocalization](/api/Global.DewLocalization) · [DewNetworkBehaviour](/api/Global.DewNetworkBehaviour) · [DewNetworkManager](/api/Global.DewNetworkManager) · [DewNetworkStartSettings](/api/Global.DewNetworkStartSettings) · [DewPlayer](/api/Global.DewPlayer) · [DewProfile](/api/Global.DewProfile) · [DewResources](/api/Global.DewResources) · [DewSessionError](/api/Global.DewSessionError) · [GameModifierBase](/api/Global.GameModifierBase) · [LobbyManager](/api/Global.LobbyManager) · [ManagerBase`1](/api/Global.ManagerBase`1) · [MessageManager](/api/Global.MessageManager) · [NetworkedManagerBase`1](/api/Global.NetworkedManagerBase`1) · [PreferredGameSettings](/api/Global.PreferredGameSettings) · [ResourceLoadSettings](/api/Global.ResourceLoadSettings) · [SafeAction](/api/Global.SafeAction) · [SafeAction`1](/api/Global.SafeAction`1) · [SafeAction`2](/api/Global.SafeAction`2) · `Mirror.GeneratedNetworkCode`

### Related Enums (5)

*Enumerations referenced in fields, properties, or method signatures:*

[`AllowMidJoinType`](/enums#allowmidjointype) · [`GameState`](/enums#gamestate) · [`MidJoinBanType`](/enums#midjoinbantype) · [`MidJoinWaitType`](/enums#midjoinwaittype) · [`SaveVarFlags`](/enums#savevarflags)

:::
