# Class: DewPersistence.GameData

- **Category:** <span class="cat-dot" style="--cat-color: #f97316" data-cat="Data & Core Math"></span> Data & Core Math
- **Namespace:** `Global`
- **Assembly:** `Dew.Core.dll`

```csharp
public class DewPersistence.GameData
```

## Fields (10)

::: details Click to expand Fields (10)

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`actors`** | `public List<DewPersistence.GeneralData> actors` |  |
| **`CurrentSaveVersion`** | `public const int CurrentSaveVersion = 1` |  |
| **`isMultiplayer`** | `public bool isMultiplayer` |  |
| **`loadNodeSettings`** | `public LoadNodeSettings loadNodeSettings` |  |
| **`lobbyType`** | `public DewLobbyType lobbyType` |  |
| **`managerPersistentData`** | `public Dictionary<string, Dictionary<string, string>> managerPersistentData` |  |
| **`players`** | `public List<DewPersistence.PlayerData> players` |  |
| **`saveVersion`** | `public int saveVersion` |  |
| **`serverActorData`** | `public Dictionary<string, string> serverActorData` |  |
| **`shouldShowVersionWarning`** | `public bool shouldShowVersionWarning` |  |

:::

## Methods (4)

::: details `GetElapsedGameTimeSeconds()`

```csharp
public int GetElapsedGameTimeSeconds()
```

**Returns:** `int`

:::

::: details `GetReadableDescription()`

```csharp
public string GetReadableDescription()
```

**Returns:** `string`

:::

::: details `GetReadableGameType()`

```csharp
public string GetReadableGameType()
```

**Returns:** `string`

:::

::: details `Validate()`

```csharp
public bool Validate()
```

**Returns:** `bool`

:::


## Architecture & Relationships

::: details Click to expand Architecture & Relationships

### Used By (0)

*No incoming dependencies recorded.*

### Dependencies (0)

*No outgoing class dependencies recorded.*

### Related Enums (1)

*Enumerations referenced in fields, properties, or method signatures:*

<a href="/enums#dewlobbytype" class="enum-link" data-tooltip="Public=0 · InviteOnly=1">DewLobbyType</a>

:::
