# Class: LobbyManager

- **Category:** <span class="cat-dot" style="--cat-color: #3b82f6" data-cat="Managers & Systems"></span> Managers & Systems
- **Namespace:** `Global`
- **Assembly:** `Dew.Core.dll`
- **Inheritance / Derived:** [LogicBehaviour](/api/Global.LogicBehaviour) → `ManagerBase` → [LobbyManager](/api/Global.LobbyManager)

```csharp
public class LobbyManager : ManagerBase<LobbyManager>, ILogicUpdate
```

## Fields (2)

::: details Click to expand Fields (2)

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`onCurrentLobbyChanged`** | `public Action onCurrentLobbyChanged` |  |
| **`onLobbyListUpdated`** | `public Action onLobbyListUpdated` |  |

:::

## Properties (3)

::: details Click to expand Properties (3)

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`isLobbyLeader`** | `public bool isLobbyLeader { get; }` |  |
| **`service`** | `public LobbyServiceProvider service { get; }` |  |
| **`shouldRegisterUpdates`** | `public override bool shouldRegisterUpdates { get; }` |  |

:::

## Methods (3)

::: details `GetDefaultLobbyName()`

```csharp
public static string GetDefaultLobbyName()
```

**Returns:** `string`

:::

::: details `SwitchService()`

```csharp
public void SwitchService()
```

:::

::: details `SwitchService(LobbyServiceProvider)`

```csharp
public void SwitchService(LobbyServiceProvider newProvider)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `newProvider` | [`LobbyServiceProvider`](/api/Global.LobbyServiceProvider) |  |

:::
