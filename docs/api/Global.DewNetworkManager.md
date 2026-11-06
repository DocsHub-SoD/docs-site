# Class: DewNetworkManager

- **Category:** <span class="cat-dot" style="--cat-color: #3b82f6" data-cat="Managers & Systems"></span> Managers & Systems
- **Namespace:** `Global`
- **Assembly:** `Dew.Core.dll`

```csharp
public class DewNetworkManager : NetworkManager
```

## Fields (5)

::: details Click to expand Fields (5)

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`ClientEvent_OnDewNetworkBehaviourStart`** | `public SafeAction<DewNetworkBehaviour> ClientEvent_OnDewNetworkBehaviourStart` |  |
| **`ClientEvent_OnDewNetworkBehaviourStop`** | `public SafeAction<DewNetworkBehaviour> ClientEvent_OnDewNetworkBehaviourStop` |  |
| **`ClientEvent_OnLoadingStatusChanged`** | `public SafeAction<bool> ClientEvent_OnLoadingStatusChanged` |  |
| **`ClientEvent_OnSessionEnd`** | `public SafeAction ClientEvent_OnSessionEnd` | Called when current session is terminated, regardless of cause. (Kick, concluded game, restart, etc.) |
| **`startSettings`** | `public static DewNetworkStartSettings startSettings` |  |

:::

## Properties (6)

::: details Click to expand Properties (6)

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`didRegisterError`** | `public bool didRegisterError { get; set; }` |  |
| **`hasSessionEnded`** | `public bool hasSessionEnded { get; }` |  |
| **`instance`** | `public static DewNetworkManager instance { get; }` | If you expect the instance to be null, you MUST USE softInstance in Update loops.This will call FindObjectOfType if current instance is null, which can be very expensive. |
| **`isBeingKicked`** | `public bool isBeingKicked { get; }` |  |
| **`isEndingSession`** | `public bool isEndingSession { get; }` | Available on server. |
| **`softInstance`** | `public static DewNetworkManager softInstance { get; }` |  |

:::

## Methods (17)

::: details `Awake()`

```csharp
public override void Awake()
```

:::

::: details `EndSession()`

End this session. When called on server this ends everyone's game completely. When on client, it locally exits out of the game.You can use this to exit out of game/lobby or whatever scenario where network is involved.When ending a game on server, it is recommended to register game results beforehand.

```csharp
public void EndSession()
```

:::

::: details `LoadSceneAsync(string, List&lt;DewPlayer&gt;, Action)`

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

:::

::: details `OnClientConnect()`

```csharp
public override void OnClientConnect()
```

:::

::: details `OnClientDisconnect()`

```csharp
public override void OnClientDisconnect()
```

:::

::: details `OnDestroy()`

```csharp
public override void OnDestroy()
```

:::

::: details `OnServerAddPlayer(NetworkConnectionToClient)`

```csharp
public override void OnServerAddPlayer(NetworkConnectionToClient conn)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `conn` | `Mirror.NetworkConnectionToClient` |  |

:::

::: details `OnServerConnect(NetworkConnectionToClient)`

```csharp
public override void OnServerConnect(NetworkConnectionToClient conn)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `conn` | `Mirror.NetworkConnectionToClient` |  |

:::

::: details `OnServerDisconnect(NetworkConnectionToClient)`

```csharp
public override void OnServerDisconnect(NetworkConnectionToClient conn)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `conn` | `Mirror.NetworkConnectionToClient` |  |

:::

::: details `OnStartClient()`

```csharp
public override void OnStartClient()
```

:::

::: details `OnStartHost()`

```csharp
public override void OnStartHost()
```

:::

::: details `RestartSession()`

Restart this session. This can only be called on server.All players in the session will restart the game and be placed in the same lobby they were in.All game related states are started from scratch and only lobbies are reused.

```csharp
public void RestartSession()
```

:::

::: details `SetLoadingStatus(bool, List&lt;DewPlayer&gt;)`

```csharp
public void SetLoadingStatus(bool isLoading, List<DewPlayer> players = null)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `isLoading` | `bool` |  |
| `players` | [`System.Collections.Generic.List<T><DewPlayer>`](/api/Global.DewPlayer) |  |

:::

::: details `SetWhiteLoadingStatus(bool, List&lt;DewPlayer&gt;)`

```csharp
public void SetWhiteLoadingStatus(bool isLoading, List<DewPlayer> players = null)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `isLoading` | `bool` |  |
| `players` | [`System.Collections.Generic.List<T><DewPlayer>`](/api/Global.DewPlayer) |  |

:::

::: details `SpawnPlayerObject(NetworkConnectionToClient)`

```csharp
public void SpawnPlayerObject(NetworkConnectionToClient conn)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `conn` | `Mirror.NetworkConnectionToClient` |  |

:::

::: details `Start()`

```csharp
public override void Start()
```

:::

::: details `StartSession()`

```csharp
protected virtual UniTaskVoid StartSession()
```

**Returns:** `Cysharp.Threading.Tasks.UniTaskVoid`

:::


## Architecture & Relationships

::: details Click to expand Architecture & Relationships

### Used By (17)

*Classes and systems that invoke, reference, or depend on `DewNetworkManager`:*

[AchievementManager](/api/Global.AchievementManager) · [CameraManager](/api/Global.CameraManager) · [DewMod](/api/Global.DewMod) · [DewNetworkAuthenticator](/api/Global.DewNetworkAuthenticator) · [DewNetworkBehaviour](/api/Global.DewNetworkBehaviour) · [DewPlayer](/api/Global.DewPlayer) · [GameManager](/api/Global.GameManager) · [GameMod_Limbo](/api/Global.GameMod_Limbo) · [GameSettingsManager](/api/Global.GameSettingsManager) · `InGameAnalyticsManager` · [InGameReverieManager](/api/Global.InGameReverieManager) · `LobbyServiceEOS` · [PlayLobbyManager](/api/Global.PlayLobbyManager) · [TimescaleManager](/api/Global.TimescaleManager) · `TutorialNetworkManager` · `UI_InGame_Map` · `UI_SelectControlPresetWindow`

### Dependencies (35)

*Types and components that `DewNetworkManager` references or depends upon:*

[Actor](/api/Global.Actor) · [ActorCheck](/api/Global.ActorCheck) · [ActorManager](/api/Global.ActorManager) · [ChatManager](/api/Global.ChatManager) · [ConsoleManager](/api/Global.ConsoleManager) · [Dew](/api/Global.Dew) · [DewBuildProfile](/api/Global.DewBuildProfile) · [DewEffect](/api/Global.DewEffect) · [DewNetworkStartSettings](/api/Global.DewNetworkStartSettings) · [DewPlayer](/api/Global.DewPlayer) · [DewProfile](/api/Global.DewProfile) · [DewResources](/api/Global.DewResources) · [DewSessionError](/api/Global.DewSessionError) · [DewSteam](/api/Global.DewSteam) · [Entity](/api/Global.Entity) · [EntityCheck](/api/Global.EntityCheck) · [EntityControl](/api/Global.EntityControl) · [GameManager](/api/Global.GameManager) · [GameResultManager](/api/Global.GameResultManager) · [GameSettingsManager](/api/Global.GameSettingsManager) · [Hero](/api/Global.Hero) · [HeroSkill](/api/Global.HeroSkill) · `InGameAnalyticsManager` · [InGameUIManager](/api/Global.InGameUIManager) · [LobbyInstance](/api/Global.LobbyInstance) · [LobbyManager](/api/Global.LobbyManager) · `LobbyServiceEOS` · [LobbyServiceProvider](/api/Global.LobbyServiceProvider) · [ManagerBase`1](/api/Global.ManagerBase`1) · `NetworkConnectionToClientExtension` · [NetworkedManagerBase`1](/api/Global.NetworkedManagerBase`1) · [SafeAction](/api/Global.SafeAction) · [SafeAction`1](/api/Global.SafeAction`1) · [TransitionManager](/api/Global.TransitionManager) · [UIManager](/api/Global.UIManager)

### Related Enums (3)

*Enumerations referenced in fields, properties, or method signatures:*

<a href="/enums#clienttransportchoice" class="enum-link" data-tooltip="Eos=0 · Steam=1">ClientTransportChoice</a> · <a href="/enums#dewtransportpreference" class="enum-link" data-tooltip="Auto=0 · ForceEOS=1 · ForceSteam=2">DewTransportPreference</a> · <a href="/enums#loadingstatus" class="enum-link" data-tooltip="Empty=0 · WaitingForService=1 · CheckingLobbyStatus=2 · CleaningUpPreviousLobby=3 · LeavingPreviousLobby=4 (+11 more)">LoadingStatus</a>

:::
