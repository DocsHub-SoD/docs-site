# Class: LobbyServiceSteam

- **Category:** <span class="cat-dot" style="--cat-color: #06b6d4" data-cat="Networking"></span> Networking
- **Namespace:** `Global`
- **Assembly:** `Dew.Core.dll`
- **Inheritance / Derived:** [LobbyServiceProvider](/api/Global.LobbyServiceProvider)

```csharp
public class LobbyServiceSteam : LobbyServiceProvider
```

## Fields (2)

::: details Click to expand Fields (2)

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`disableVersionCheck`** | `public bool disableVersionCheck` |  |
| **`lobbyMembers`** | `public List<CSteamID> lobbyMembers` |  |

:::

## Properties (1)

::: details Click to expand Properties (1)

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`currentLobby`** | `public override LobbyInstance currentLobby { get; }` |  |

:::

## Methods (10)

::: details `ActivateGameOverlayInviteDialog()`

```csharp
public void ActivateGameOverlayInviteDialog()
```

:::

::: details `CreateLobby()`

```csharp
public override UniTask CreateLobby()
```

**Returns:** `Cysharp.Threading.Tasks.UniTask`

:::

::: details `GetGameServerAddress()`

```csharp
public override string GetGameServerAddress()
```

**Returns:** `string`

:::

::: details `GetLobbies(Action&lt;LobbySearchResult&gt;, object)`

```csharp
public override UniTask GetLobbies(Action<LobbySearchResult> onUpdated, object continuationToken = null)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `onUpdated` | [`System.Action<T><LobbySearchResult>`](/api/Global.LobbySearchResult) |  |
| `continuationToken` | `object` |  |

**Returns:** `Cysharp.Threading.Tasks.UniTask`

:::

::: details `HandleUserLeavingGame(string)`

```csharp
public override UniTask HandleUserLeavingGame(string id)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `id` | `string` |  |

**Returns:** `Cysharp.Threading.Tasks.UniTask`

:::

::: details `InviteToLobby(CSteamID)`

```csharp
public bool InviteToLobby(CSteamID friend)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `friend` | `Steamworks.CSteamID` |  |

**Returns:** `bool`

:::

::: details `JoinGameOfCurrentLobby()`

```csharp
public override UniTask JoinGameOfCurrentLobby()
```

**Returns:** `Cysharp.Threading.Tasks.UniTask`

:::

::: details `JoinLobby(object)`

```csharp
public override UniTask JoinLobby(object lobby)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `lobby` | `object` |  |

**Returns:** `Cysharp.Threading.Tasks.UniTask`

:::

::: details `LeaveLobby()`

```csharp
public override UniTask LeaveLobby()
```

**Returns:** `Cysharp.Threading.Tasks.UniTask`

:::

::: details `SetLobbyAttribute(string, object)`

```csharp
public override UniTask SetLobbyAttribute(string key, object value)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `key` | `string` |  |
| `value` | `object` |  |

**Returns:** `Cysharp.Threading.Tasks.UniTask`

:::
