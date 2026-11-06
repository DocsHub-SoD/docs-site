# Class: PingManager

- **Category:** <span class="cat-dot" style="--cat-color: #3b82f6" data-cat="Managers & Systems"></span> Managers & Systems
- **Namespace:** `Global`
- **Assembly:** `Dew.Core.dll`
- **Inheritance / Derived:** [DewNetworkBehaviour](/api/Global.DewNetworkBehaviour) → `NetworkedManagerBase` → [PingManager](/api/Global.PingManager)

```csharp
public class PingManager : NetworkedManagerBase<PingManager>, ILogicUpdate
```

## Fields (6)

::: details Click to expand Fields (6)

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`enemy`** | `public PingManager.PingPrefabBindings enemy` |  |
| **`interest`** | `public PingManager.PingPrefabBindings interest` |  |
| **`move`** | `public PingManager.PingPrefabBindings move` |  |
| **`pingIndicatorAlwaysOnTopParent`** | `public Transform pingIndicatorAlwaysOnTopParent` |  |
| **`pingIndicatorParent`** | `public Transform pingIndicatorParent` |  |
| **`worldNode`** | `public PingManager.PingPrefabBindings worldNode` |  |

:::

## Methods (4)

::: details `BroadcastPing(Ping)`

```csharp
public void BroadcastPing(PingManager.Ping ping)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `ping` | [`PingManager.Ping`](/api/Global.PingManager) |  |

:::

::: details `CmdSendPing(Ping, NetworkConnectionToClient)`

```csharp
public void CmdSendPing(PingManager.Ping ping, NetworkConnectionToClient sender = null)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `ping` | [`PingManager.Ping`](/api/Global.PingManager) |  |
| `sender` | `Mirror.NetworkConnectionToClient` |  |

:::

::: details `GetPingUIValue(string, string)`

```csharp
public static string GetPingUIValue(string key, string accentColor = "#63e3ff")
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `key` | `string` |  |
| `accentColor` | `string` |  |

**Returns:** `string`

:::

::: details `OnStart()`

```csharp
public override void OnStart()
```

:::
