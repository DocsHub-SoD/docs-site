# Class: PreferredGameSettings

- **Category:** <span class="cat-dot" style="--cat-color: #f97316" data-cat="Data & Core Math"></span> Data & Core Math
- **Namespace:** `Global`
- **Assembly:** `Dew.Core.dll`

```csharp
public class PreferredGameSettings
```

## Fields (13)

::: details Click to expand Fields (13)

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`allowDejavu`** | `public bool allowDejavu` |  |
| **`allowMidJoins`** | `public AllowMidJoinType allowMidJoins` |  |
| **`bannedGameItems`** | `public List<string> bannedGameItems` |  |
| **`customData`** | `public Dictionary<string, string> customData` |  |
| **`dejavuItem`** | `public string dejavuItem` |  |
| **`difficulty`** | `public string difficulty` |  |
| **`enableVotes`** | `public bool enableVotes` |  |
| **`hero`** | `public string hero` |  |
| **`heroSelectedLoadoutIndex`** | `public Dictionary<string, int> heroSelectedLoadoutIndex` |  |
| **`lobbyDescription`** | `public string lobbyDescription` |  |
| **`lobbyName`** | `public string lobbyName` |  |
| **`lucidDreams`** | `public List<string> lucidDreams` |  |
| **`tags`** | `public List<string> tags` |  |

:::

## Methods (2)

::: details `ApplyToGame()`

```csharp
public void ApplyToGame()
```

:::

::: details `Validate()`

```csharp
public void Validate()
```

:::


## Architecture & Relationships

::: details Click to expand Architecture & Relationships

### Used By (3)

*Classes and systems that invoke, reference, or depend on `PreferredGameSettings`:*

[DewProfile](/api/Global.DewProfile) · [GameSettingsManager](/api/Global.GameSettingsManager) · [TitleManager](/api/Global.TitleManager)

### Dependencies (3)

*Types and components that `PreferredGameSettings` references or depends upon:*

[Dew](/api/Global.Dew) · [GameSettingsManager](/api/Global.GameSettingsManager) · [NetworkedManagerBase`1](/api/Global.NetworkedManagerBase`1)

### Related Enums (1)

*Enumerations referenced in fields, properties, or method signatures:*

<a href="/enums#allowmidjointype" class="enum-link" data-tooltip="AllowAll=0 · RejoinOnly=1 · Disallow=2">AllowMidJoinType</a>

:::
