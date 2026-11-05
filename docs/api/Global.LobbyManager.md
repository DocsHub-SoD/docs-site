# Class: LobbyManager

- **Namespace:** `Global`
- **Assembly:** `Dew.Core.dll`
- **Inheritance / Derived:** [LogicBehaviour](/api/Global.LogicBehaviour) → `ManagerBase` → [LobbyManager](/api/Global.LobbyManager)

```csharp
public class LobbyManager : ManagerBase<LobbyManager>, ILogicUpdate
```

## Fields

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`onCurrentLobbyChanged`** | `public Action onCurrentLobbyChanged` |  |
| **`onLobbyListUpdated`** | `public Action onLobbyListUpdated` |  |

## Properties

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`isLobbyLeader`** | `public bool isLobbyLeader { get; }` |  |
| **`service`** | `public LobbyServiceProvider service { get; }` |  |
| **`shouldRegisterUpdates`** | `public override bool shouldRegisterUpdates { get; }` |  |

## Methods

### `GetDefaultLobbyName()`

```csharp
public static string GetDefaultLobbyName()
```

**Returns:** `string`

### `SwitchService()`

```csharp
public void SwitchService()
```

### `SwitchService(LobbyServiceProvider)`

```csharp
public void SwitchService(LobbyServiceProvider newProvider)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `newProvider` | [LobbyServiceProvider](/api/Global.LobbyServiceProvider) |  |
