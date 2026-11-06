# Class: DewInterestManagement

- **Category:** <span class="cat-dot" style="--cat-color: #eab308" data-cat="Items & Economy"></span> Items & Economy
- **Namespace:** `Global`
- **Assembly:** `Dew.Core.dll`

```csharp
public class DewInterestManagement : InterestManagement
```

## Methods (3)

::: details `OnCheckObserver(NetworkIdentity, NetworkConnectionToClient)`

```csharp
public override bool OnCheckObserver(NetworkIdentity identity, NetworkConnectionToClient newObserver)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `identity` | `Mirror.NetworkIdentity` |  |
| `newObserver` | `Mirror.NetworkConnectionToClient` |  |

**Returns:** `bool`

:::

::: details `OnRebuildObservers(NetworkIdentity, HashSet&lt;NetworkConnectionToClient&gt;)`

```csharp
public override void OnRebuildObservers(NetworkIdentity identity, HashSet<NetworkConnectionToClient> newObservers)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `identity` | `Mirror.NetworkIdentity` |  |
| `newObservers` | `System.Collections.Generic.HashSet<T><Mirror.NetworkConnectionToClient>` |  |

:::

::: details `SetHostVisibility(NetworkIdentity, bool)`

```csharp
public override void SetHostVisibility(NetworkIdentity identity, bool visible)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `identity` | `Mirror.NetworkIdentity` |  |
| `visible` | `bool` |  |

:::
