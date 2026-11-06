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
