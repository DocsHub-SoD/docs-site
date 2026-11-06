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


## Architecture & Relationships

::: details Click to expand Architecture & Relationships

### Used By (1)

*Classes and systems that invoke, reference, or depend on `PingManager`:*

[ControlManager](/api/Global.ControlManager)

### Dependencies (24)

*Types and components that `PingManager` references or depends upon:*

[AbilityTrigger](/api/Global.AbilityTrigger) · [Actor](/api/Global.Actor) · [ChatManager](/api/Global.ChatManager) · [Dew](/api/Global.Dew) · [DewInput](/api/Global.DewInput) · [DewLocalization](/api/Global.DewLocalization) · [DewNetworkBehaviour](/api/Global.DewNetworkBehaviour) · [DewPlayer](/api/Global.DewPlayer) · [DewResources](/api/Global.DewResources) · [Entity](/api/Global.Entity) · [EntityStatus](/api/Global.EntityStatus) · [Gem](/api/Global.Gem) · [Hero](/api/Global.Hero) · [HeroSkill](/api/Global.HeroSkill) · [ICustomInteractable](/api/Global.ICustomInteractable) · [IInteractable](/api/Global.IInteractable) · [IShrineCustomName](/api/Global.IShrineCustomName) · `NetworkConnectionToClientExtension` · [NetworkedManagerBase`1](/api/Global.NetworkedManagerBase`1) · [Rift](/api/Global.Rift) · [Shrine](/api/Global.Shrine) · [SkillTrigger](/api/Global.SkillTrigger) · [TriggerConfig](/api/Global.TriggerConfig) · `Mirror.GeneratedNetworkCode`

:::
