# Class: LobbyServiceSteam

- **Namespace:** `Global`
- **Assembly:** `Dew.Core.dll`
- **Inheritance / Derived:** [LobbyServiceProvider](/api/Global.LobbyServiceProvider)

```csharp
public class LobbyServiceSteam : LobbyServiceProvider
```

## Fields

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`disableVersionCheck`** | `public bool disableVersionCheck` |  |
| **`lobbyMembers`** | `public List&lt;CSteamID&gt; lobbyMembers` |  |

## Properties

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`currentLobby`** | `public override LobbyInstance currentLobby { get; }` |  |

## Methods

### `ActivateGameOverlayInviteDialog()`

```csharp
public void ActivateGameOverlayInviteDialog()
```

### `CreateLobby()`

```csharp
public override UniTask CreateLobby()
```

**Returns:** `Cysharp.Threading.Tasks.UniTask`

### `GetGameServerAddress()`

```csharp
public override string GetGameServerAddress()
```

**Returns:** `string`

### `GetLobbies(Action&lt;LobbySearchResult&gt;, object)`

```csharp
public override UniTask GetLobbies(Action<LobbySearchResult> onUpdated, object continuationToken = null)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `onUpdated` | [System.Action&lt;T&gt;&lt;LobbySearchResult&gt;](/api/Global.LobbySearchResult) |  |
| `continuationToken` | `object` |  |

**Returns:** `Cysharp.Threading.Tasks.UniTask`

### `HandleUserLeavingGame(string)`

```csharp
public override UniTask HandleUserLeavingGame(string id)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `id` | `string` |  |

**Returns:** `Cysharp.Threading.Tasks.UniTask`

### `InviteToLobby(CSteamID)`

```csharp
public bool InviteToLobby(CSteamID friend)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `friend` | `Steamworks.CSteamID` |  |

**Returns:** `bool`

### `JoinGameOfCurrentLobby()`

```csharp
public override UniTask JoinGameOfCurrentLobby()
```

**Returns:** `Cysharp.Threading.Tasks.UniTask`

### `JoinLobby(object)`

```csharp
public override UniTask JoinLobby(object lobby)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `lobby` | `object` |  |

**Returns:** `Cysharp.Threading.Tasks.UniTask`

### `LeaveLobby()`

```csharp
public override UniTask LeaveLobby()
```

**Returns:** `Cysharp.Threading.Tasks.UniTask`

### `SetLobbyAttribute(string, object)`

```csharp
public override UniTask SetLobbyAttribute(string key, object value)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `key` | `string` |  |
| `value` | `object` |  |

**Returns:** `Cysharp.Threading.Tasks.UniTask`
