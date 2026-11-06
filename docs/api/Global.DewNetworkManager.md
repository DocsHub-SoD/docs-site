# Class: DewNetworkManager

- **Category:** <span class="cat-dot" style="--cat-color: #3b82f6" data-cat="Managers & Systems"></span> Managers & Systems
- **Namespace:** `Global`
- **Assembly:** `Dew.Core.dll`

```csharp
public class DewNetworkManager : NetworkManager
```

## Fields

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`ClientEvent_OnDewNetworkBehaviourStart`** | `public SafeAction<DewNetworkBehaviour> ClientEvent_OnDewNetworkBehaviourStart` |  |
| **`ClientEvent_OnDewNetworkBehaviourStop`** | `public SafeAction<DewNetworkBehaviour> ClientEvent_OnDewNetworkBehaviourStop` |  |
| **`ClientEvent_OnLoadingStatusChanged`** | `public SafeAction<bool> ClientEvent_OnLoadingStatusChanged` |  |
| **`ClientEvent_OnSessionEnd`** | `public SafeAction ClientEvent_OnSessionEnd` | Called when current session is terminated, regardless of cause. (Kick, concluded game, restart, etc.) |
| **`startSettings`** | `public static DewNetworkStartSettings startSettings` |  |

## Properties

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`didRegisterError`** | `public bool didRegisterError { get; set; }` |  |
| **`hasSessionEnded`** | `public bool hasSessionEnded { get; }` |  |
| **`instance`** | `public static DewNetworkManager instance { get; }` | If you expect the instance to be null, you MUST USE softInstance in Update loops.This will call FindObjectOfType if current instance is null, which can be very expensive. |
| **`isBeingKicked`** | `public bool isBeingKicked { get; }` |  |
| **`isEndingSession`** | `public bool isEndingSession { get; }` | Available on server. |
| **`softInstance`** | `public static DewNetworkManager softInstance { get; }` |  |

## Methods

### `Awake()`

```csharp
public override void Awake()
```

### `EndSession()`

End this session. When called on server this ends everyone's game completely. When on client, it locally exits out of the game.You can use this to exit out of game/lobby or whatever scenario where network is involved.When ending a game on server, it is recommended to register game results beforehand.

```csharp
public void EndSession()
```

### `LoadSceneAsync(string, List<DewPlayer>, Action)`

```csharp
public IEnumerator LoadSceneAsync(string sceneName, List<DewPlayer> players = null, Action onBeforeSpawnObjects = null)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `sceneName` | `string` |  |
| `players` | [`System.Collections.Generic.List<T><DewPlayer>`](/api/Global.DewPlayer) |  |
| `onBeforeSpawnObjects` | `System.Action` |  |

**Returns:** `System.Collections.IEnumerator`

### `OnClientConnect()`

```csharp
public override void OnClientConnect()
```

### `OnClientDisconnect()`

```csharp
public override void OnClientDisconnect()
```

### `OnDestroy()`

```csharp
public override void OnDestroy()
```

### `OnServerAddPlayer(NetworkConnectionToClient)`

```csharp
public override void OnServerAddPlayer(NetworkConnectionToClient conn)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `conn` | `Mirror.NetworkConnectionToClient` |  |

### `OnServerConnect(NetworkConnectionToClient)`

```csharp
public override void OnServerConnect(NetworkConnectionToClient conn)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `conn` | `Mirror.NetworkConnectionToClient` |  |

### `OnServerDisconnect(NetworkConnectionToClient)`

```csharp
public override void OnServerDisconnect(NetworkConnectionToClient conn)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `conn` | `Mirror.NetworkConnectionToClient` |  |

### `OnStartClient()`

```csharp
public override void OnStartClient()
```

### `OnStartHost()`

```csharp
public override void OnStartHost()
```

### `RestartSession()`

Restart this session. This can only be called on server.All players in the session will restart the game and be placed in the same lobby they were in.All game related states are started from scratch and only lobbies are reused.

```csharp
public void RestartSession()
```

### `SetLoadingStatus(bool, List<DewPlayer>)`

```csharp
public void SetLoadingStatus(bool isLoading, List<DewPlayer> players = null)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `isLoading` | `bool` |  |
| `players` | [`System.Collections.Generic.List<T><DewPlayer>`](/api/Global.DewPlayer) |  |

### `SetWhiteLoadingStatus(bool, List<DewPlayer>)`

```csharp
public void SetWhiteLoadingStatus(bool isLoading, List<DewPlayer> players = null)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `isLoading` | `bool` |  |
| `players` | [`System.Collections.Generic.List<T><DewPlayer>`](/api/Global.DewPlayer) |  |

### `SpawnPlayerObject(NetworkConnectionToClient)`

```csharp
public void SpawnPlayerObject(NetworkConnectionToClient conn)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `conn` | `Mirror.NetworkConnectionToClient` |  |

### `Start()`

```csharp
public override void Start()
```

### `StartSession()`

```csharp
protected virtual UniTaskVoid StartSession()
```

**Returns:** `Cysharp.Threading.Tasks.UniTaskVoid`
