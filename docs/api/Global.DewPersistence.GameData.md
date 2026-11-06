# Class: DewPersistence.GameData

- **Category:** <span class="cat-dot" style="--cat-color: #f97316" data-cat="Data & Core Math"></span> Data & Core Math
- **Namespace:** `Global`
- **Assembly:** `Dew.Core.dll`

```csharp
public class DewPersistence.GameData
```

## Fields

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

## Methods

### `GetElapsedGameTimeSeconds()`

```csharp
public int GetElapsedGameTimeSeconds()
```

**Returns:** `int`

### `GetReadableDescription()`

```csharp
public string GetReadableDescription()
```

**Returns:** `string`

### `GetReadableGameType()`

```csharp
public string GetReadableGameType()
```

**Returns:** `string`

### `Validate()`

```csharp
public bool Validate()
```

**Returns:** `bool`
