# Class: LobbyInstanceSteam

- **Category:** <span class="cat-dot" style="--cat-color: #06b6d4" data-cat="Networking"></span> Networking
- **Namespace:** `Global`
- **Assembly:** `Dew.Core.dll`
- **Inheritance / Derived:** [LobbyInstance](/api/Global.LobbyInstance)

```csharp
public class LobbyInstanceSteam : LobbyInstance
```

## Methods (2)

::: details `GetCSteamId()`

```csharp
public CSteamID GetCSteamId()
```

**Returns:** `Steamworks.CSteamID`

:::

::: details `SetCSteamId(CSteamID)`

```csharp
public void SetCSteamId(CSteamID lobbyId)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `lobbyId` | `Steamworks.CSteamID` |  |

:::


## Architecture & Relationships

::: details Click to expand Architecture & Relationships

### Used By (1)

*Classes and systems that invoke, reference, or depend on `LobbyInstanceSteam`:*

[LobbyServiceSteam](/api/Global.LobbyServiceSteam)

### Dependencies (1)

*Types and components that `LobbyInstanceSteam` references or depends upon:*

[LobbyInstance](/api/Global.LobbyInstance)

:::
