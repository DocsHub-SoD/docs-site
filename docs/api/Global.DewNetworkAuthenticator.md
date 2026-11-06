# Class: DewNetworkAuthenticator

- **Category:** <span class="cat-dot" style="--cat-color: #06b6d4" data-cat="Networking"></span> Networking
- **Namespace:** `Global`
- **Assembly:** `Dew.Core.dll`

```csharp
public class DewNetworkAuthenticator : NetworkAuthenticator
```

## Methods

### `OnAuthRequestMessage(NetworkConnectionToClient, DewAuthRequestMessage)`

```csharp
public void OnAuthRequestMessage(NetworkConnectionToClient conn, DewAuthRequestMessage msg)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `conn` | `Mirror.NetworkConnectionToClient` |  |
| `msg` | [`DewAuthRequestMessage`](/api/Global.DewAuthRequestMessage) |  |

### `OnAuthResponseMessage(DewAuthResponseMessage)`

```csharp
public void OnAuthResponseMessage(DewAuthResponseMessage msg)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `msg` | [`DewAuthResponseMessage`](/api/Global.DewAuthResponseMessage) |  |

### `OnClientAuthenticate()`

```csharp
public override void OnClientAuthenticate()
```

### `OnStartClient()`

```csharp
public override void OnStartClient()
```

### `OnStartServer()`

```csharp
public override void OnStartServer()
```

### `OnStopClient()`

```csharp
public override void OnStopClient()
```

### `OnStopServer()`

```csharp
public override void OnStopServer()
```
