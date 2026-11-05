# Class: DewPersistence.GameData

- **Namespace:** `Global`
- **Assembly:** `Dew.Core.dll`

```csharp
public class DewPersistence.GameData
```

## Fields

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`actors`** | `public List&lt;DewPersistence.GeneralData&gt; actors` |  |
| **`CurrentSaveVersion`** | `public const int CurrentSaveVersion = 1` |  |
| **`isMultiplayer`** | `public bool isMultiplayer` |  |
| **`loadNodeSettings`** | `public LoadNodeSettings loadNodeSettings` |  |
| **`lobbyType`** | `public DewLobbyType lobbyType` |  |
| **`managerPersistentData`** | `public Dictionary&lt;string, Dictionary&lt;string, string&gt;&gt; managerPersistentData` |  |
| **`players`** | `public List&lt;DewPersistence.PlayerData&gt; players` |  |
| **`saveVersion`** | `public int saveVersion` |  |
| **`serverActorData`** | `public Dictionary&lt;string, string&gt; serverActorData` |  |
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
