# Class: GameSettingsManager

- **Namespace:** `Global`
- **Assembly:** `Dew.Core.dll`
- **Inheritance / Derived:** [DewNetworkBehaviour](/api/Global.DewNetworkBehaviour) → `NetworkedManagerBase` → [GameSettingsManager](/api/Global.GameSettingsManager)

```csharp
public class GameSettingsManager : NetworkedManagerBase<GameSettingsManager>, ILogicUpdate
```

## Fields

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`activeLucidDreams`** | `[SaveVar(SaveVarFlags.Default)]
public readonly SyncList&lt;string&gt; activeLucidDreams` |  |
| **`addedGameMods`** | `[SaveVar(SaveVarFlags.Default)]
public readonly SyncList&lt;string&gt; addedGameMods` | This should not be changed after starting the server. |
| **`availableLucidDreams`** | `[SaveVar(SaveVarFlags.Default)]
public readonly SyncList&lt;string&gt; availableLucidDreams` |  |
| **`bannedGameItems`** | `[SaveVar(SaveVarFlags.Default)]
public readonly SyncList&lt;string&gt; bannedGameItems` |  |
| **`ClientEvent_OnActiveLucidDreamsChanged`** | `public SafeAction ClientEvent_OnActiveLucidDreamsChanged` |  |
| **`ClientEvent_OnAvailableLucidDreamsChanged`** | `public SafeAction ClientEvent_OnAvailableLucidDreamsChanged` |  |
| **`ClientEvent_OnBannedItemsChanged`** | `public SafeAction ClientEvent_OnBannedItemsChanged` |  |
| **`ClientEvent_OnCustomDataChanged`** | `public SafeAction&lt;string&gt; ClientEvent_OnCustomDataChanged` |  |
| **`ClientEvent_OnDifficultyChanged`** | `public SafeAction&lt;string, string&gt; ClientEvent_OnDifficultyChanged` |  |
| **`ClientEvent_OnLobbyTagsChanged`** | `public SafeAction ClientEvent_OnLobbyTagsChanged` |  |
| **`ClientEvent_OnStateChanged`** | `public SafeAction ClientEvent_OnStateChanged` |  |
| **`ClientEvent_OnUnlockedGameItemsChanged`** | `public SafeAction ClientEvent_OnUnlockedGameItemsChanged` |  |
| **`customData`** | `[SaveVar(SaveVarFlags.Default)]
public readonly SyncDictionary&lt;string, string&gt; customData` |  |
| **`lobbyTags`** | `[SaveVar(SaveVarFlags.Default)]
public readonly SyncList&lt;string&gt; lobbyTags` |  |
| **`localPlayerDejavuCost`** | `public int localPlayerDejavuCost` |  |
| **`unlockedGameItems`** | `[SaveVar(SaveVarFlags.Default)]
public readonly SyncList&lt;string&gt; unlockedGameItems` |  |

## Properties

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`allowDejavu`** | `[SaveVar(SaveVarFlags.Default)]
public bool allowDejavu { get; set; }` |  |
| **`allowMidJoins`** | `[SaveVar(SaveVarFlags.Default)]
public AllowMidJoinType allowMidJoins { get; set; }` |  |
| **`difficulty`** | `[SaveVar(SaveVarFlags.Default)]
public string difficulty { get; set; }` |  |
| **`enableVotes`** | `[SaveVar(SaveVarFlags.Default)]
public bool enableVotes { get; set; }` |  |
| **`gameSettingsSaveKey`** | `[SaveVar(SaveVarFlags.Default)]
public string gameSettingsSaveKey { get; set; }` |  |
| **`lobbyDescription`** | `[SaveVar(SaveVarFlags.Default)]
public string lobbyDescription { get; set; }` |  |
| **`lobbyName`** | `[SaveVar(SaveVarFlags.Default)]
public string lobbyName { get; set; }` |  |
| **`maxPlayers`** | `[SaveVar(SaveVarFlags.Default)]
public int maxPlayers { get; set; }` |  |
| **`midJoinBanType`** | `[SaveVar(SaveVarFlags.Default)]
public MidJoinBanType midJoinBanType { get; set; }` | This is irreversible by design. |
| **`midJoinWaitType`** | `public MidJoinWaitType midJoinWaitType { get; set; }` | This should be set and unset accordingly mid-run. |
| **`state`** | `public GameState state { get; set; }` |  |

## Methods

### `AddLucidDream(string)`

```csharp
public void AddLucidDream(string type)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `type` | `string` |  |

### `Awake()`

```csharp
protected override void Awake()
```

### `ClearLucidDreams()`

```csharp
public void ClearLucidDreams()
```

### `DisconnectByMidJoinBan()`

```csharp
public void DisconnectByMidJoinBan()
```

### `DisconnectByMidJoinWaitBlock()`

```csharp
public void DisconnectByMidJoinWaitBlock()
```

### `GetLocalPreferredGameSettings()`

```csharp
public PreferredGameSettings GetLocalPreferredGameSettings()
```

**Returns:** `PreferredGameSettings`

### `Lobby_UpdateAttribute(string)`

```csharp
public UniTask Lobby_UpdateAttribute(string key)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `key` | `string` |  |

**Returns:** `Cysharp.Threading.Tasks.UniTask`

### `Lobby_UpdateCanJoinAndGameStarted(bool?)`

```csharp
public UniTask Lobby_UpdateCanJoinAndGameStarted(bool? hasGameStartedOverride = null)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `hasGameStartedOverride` | `bool?` |  |

**Returns:** `Cysharp.Threading.Tasks.UniTask`

### `Lobby_UpdateGameAttributes()`

```csharp
public UniTask Lobby_UpdateGameAttributes()
```

**Returns:** `Cysharp.Threading.Tasks.UniTask`

### `Lobby_UpdateGameStartTimestamp()`

```csharp
public UniTask Lobby_UpdateGameStartTimestamp()
```

**Returns:** `Cysharp.Threading.Tasks.UniTask`

### `LogicUpdate(float)`

```csharp
public override void LogicUpdate(float dt)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `dt` | `float` |  |

### `OnStartClient()`

```csharp
public override void OnStartClient()
```

### `OnStartServer()`

```csharp
public override void OnStartServer()
```

### `OnStopServer()`

```csharp
public override void OnStopServer()
```

### `RemoveLucidDream(string)`

```csharp
public void RemoveLucidDream(string type)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `type` | `string` |  |

### `SetEnableVotes(bool)`

```csharp
public void SetEnableVotes(bool value)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `value` | `bool` |  |

### `UpdateAvailableLucidDreams()`

```csharp
public void UpdateAvailableLucidDreams()
```

### `ValidateBannedItems(bool)`

```csharp
public void ValidateBannedItems(bool printMessage)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `printMessage` | `bool` |  |
