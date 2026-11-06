# Class: DewNetworkAuthenticator

- **Category:** <span class="cat-dot" style="--cat-color: #06b6d4" data-cat="Networking"></span> Networking
- **Namespace:** `Global`
- **Assembly:** `Dew.Core.dll`

```csharp
public class DewNetworkAuthenticator : NetworkAuthenticator
```

## Methods (7)

::: details `OnAuthRequestMessage(NetworkConnectionToClient, DewAuthRequestMessage)`

```csharp
public void OnAuthRequestMessage(NetworkConnectionToClient conn, DewAuthRequestMessage msg)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `conn` | `Mirror.NetworkConnectionToClient` |  |
| `msg` | [`DewAuthRequestMessage`](/api/Global.DewAuthRequestMessage) |  |

:::

::: details `OnAuthResponseMessage(DewAuthResponseMessage)`

```csharp
public void OnAuthResponseMessage(DewAuthResponseMessage msg)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `msg` | [`DewAuthResponseMessage`](/api/Global.DewAuthResponseMessage) |  |

:::

::: details `OnClientAuthenticate()`

```csharp
public override void OnClientAuthenticate()
```

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

::: details `OnStopClient()`

```csharp
public override void OnStopClient()
```

:::

::: details `OnStopServer()`

```csharp
public override void OnStopServer()
```

:::


## Architecture & Relationships

::: details Click to expand Architecture & Relationships

### Used By (0)

*No incoming dependencies recorded.*

### Dependencies (9)

*Types and components that `DewNetworkAuthenticator` references or depends upon:*

[DewAuthRequestMessage](/api/Global.DewAuthRequestMessage) · [DewAuthResponseMessage](/api/Global.DewAuthResponseMessage) · [DewNetworkManager](/api/Global.DewNetworkManager) · [DewSessionError](/api/Global.DewSessionError) · [DewSteam](/api/Global.DewSteam) · [GameSettingsManager](/api/Global.GameSettingsManager) · [LobbyManager](/api/Global.LobbyManager) · [ManagerBase`1](/api/Global.ManagerBase`1) · [NetworkedManagerBase`1](/api/Global.NetworkedManagerBase`1)

:::
