# Class: DewInterestManagement

- **Namespace:** `Global`
- **Assembly:** `Dew.Core.dll`

```csharp
public class DewInterestManagement : InterestManagement
```

## Methods

### `OnCheckObserver(NetworkIdentity, NetworkConnectionToClient)`

```csharp
public override bool OnCheckObserver(NetworkIdentity identity, NetworkConnectionToClient newObserver)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `identity` | `Mirror.NetworkIdentity` |  |
| `newObserver` | `Mirror.NetworkConnectionToClient` |  |

**Returns:** `bool`

### `OnRebuildObservers(NetworkIdentity, HashSet&lt;NetworkConnectionToClient&gt;)`

```csharp
public override void OnRebuildObservers(NetworkIdentity identity, HashSet<NetworkConnectionToClient> newObservers)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `identity` | `Mirror.NetworkIdentity` |  |
| `newObservers` | `System.Collections.Generic.HashSet&lt;T&gt;&lt;Mirror.NetworkConnectionToClient&gt;` |  |

### `SetHostVisibility(NetworkIdentity, bool)`

```csharp
public override void SetHostVisibility(NetworkIdentity identity, bool visible)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `identity` | `Mirror.NetworkIdentity` |  |
| `visible` | `bool` |  |
