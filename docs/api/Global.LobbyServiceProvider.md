# Class: LobbyServiceProvider

- **Category:** <span class="cat-dot" style="--cat-color: #06b6d4" data-cat="Networking"></span> Networking
- **Namespace:** `Global`
- **Assembly:** `Dew.Core.dll`
- **Inheritance / Derived:** [LobbyServiceSteam](/api/Global.LobbyServiceSteam)

```csharp
public abstract class LobbyServiceProvider : MonoBehaviour
```

## Properties

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`currentLobby`** | `public abstract LobbyInstance currentLobby { get; }` |  |
| **`foundLobbies`** | `public LobbySearchResult foundLobbies { get; set; }` |  |
| **`isRefreshingLobby`** | `public bool isRefreshingLobby { get; }` |  |

## Methods

### `CreateLobby()`

Create a new lobby. You can use this to either create a new lobby or replace old faulty/deleted lobby mid-session.

```csharp
public abstract UniTask CreateLobby()
```

**Returns:** `Cysharp.Threading.Tasks.UniTask`

### `GenerateRandomShortCode()`

```csharp
public string GenerateRandomShortCode()
```

**Returns:** `string`

### `GetGameServerAddress()`

```csharp
public abstract string GetGameServerAddress()
```

**Returns:** `string`

### `GetLobbies(Action<LobbySearchResult>, object)`

Get list of lobbies we can join.

```csharp
public abstract UniTask GetLobbies(Action<LobbySearchResult> onUpdated, object continuationToken = null)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `onUpdated` | [`System.Action<T><LobbySearchResult>`](/api/Global.LobbySearchResult) |  |
| `continuationToken` | `object` |  |

**Returns:** `Cysharp.Threading.Tasks.UniTask`

### `HandleUserLeavingGame(string)`

Handle user leaving the game server. The user must be removed from the lobby if possible.

```csharp
public abstract UniTask HandleUserLeavingGame(string id)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `id` | `string` |  |

**Returns:** `Cysharp.Threading.Tasks.UniTask`

### `InvokeOnCurrentLobbyChanged()`

You must call this when currentLobby's value changes or its property(s) changes.

```csharp
protected void InvokeOnCurrentLobbyChanged()
```

### `JoinGameOfCurrentLobby()`

```csharp
public virtual UniTask JoinGameOfCurrentLobby()
```

**Returns:** `Cysharp.Threading.Tasks.UniTask`

### `JoinLobby(object)`

Join a lobby. If you want to join the game of the lobby, you need to call respective function as well.

```csharp
public abstract UniTask JoinLobby(object lobby)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `lobby` | `object` |  |

**Returns:** `Cysharp.Threading.Tasks.UniTask`

### `LeaveLobby()`

Leave current lobby. This can be called anytime even when you are not in a lobby, to make sure you don't have any leftover lobbies.

```csharp
public abstract UniTask LeaveLobby()
```

**Returns:** `Cysharp.Threading.Tasks.UniTask`

### `RefreshLobbies(object)`

Refresh foundLobbies result.

```csharp
public UniTaskVoid RefreshLobbies(object continuationToken = null)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `continuationToken` | `object` |  |

**Returns:** `Cysharp.Threading.Tasks.UniTaskVoid`

### `SetBasicAttributes()`

```csharp
public UniTask SetBasicAttributes()
```

**Returns:** `Cysharp.Threading.Tasks.UniTask`

### `SetLobbyAttribute(string, object)`

```csharp
public abstract UniTask SetLobbyAttribute(string key, object value)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `key` | `string` |  |
| `value` | `object` |  |

**Returns:** `Cysharp.Threading.Tasks.UniTask`
