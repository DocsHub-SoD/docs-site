# Class: PlayGameManager

- **Category:** <span class="cat-dot" style="--cat-color: #3b82f6" data-cat="Managers & Systems"></span> Managers & Systems
- **Namespace:** `Global`
- **Assembly:** `Dew.Core.dll`
- **Inheritance / Derived:** [DewNetworkBehaviour](/api/Global.DewNetworkBehaviour) → `NetworkedManagerBase` → [GameManager](/api/Global.GameManager) → [GameManager](/api/Global.GameManager)

```csharp
[DewResourceLink(ResourceLinkBy.Type)]
public class PlayGameManager : GameManager, ILogicUpdate
```

## Properties

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`instance`** | `public static PlayGameManager instance { get; }` |  |

## Methods

### `DoDejavuSpawn(DewPlayer)`

```csharp
public void DoDejavuSpawn(DewPlayer h)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `h` | [`DewPlayer`](/api/Global.DewPlayer) |  |

### `GetDifficulty()`

```csharp
protected override DewDifficultySettings GetDifficulty()
```

**Returns:** `DewDifficultySettings`

### `IsContinueSaveSupported()`

```csharp
public override bool IsContinueSaveSupported()
```

**Returns:** `bool`

### `LoadNextZone()`

```csharp
public override void LoadNextZone()
```

### `OnLateStartServer()`

```csharp
public override void OnLateStartServer()
```

### `OnStartClient()`

```csharp
public override void OnStartClient()
```

### `SpawnHero(DewPlayer, Hero, HeroLoadoutData, string, List<string>)`

```csharp
public void SpawnHero(DewPlayer player, Hero hero, HeroLoadoutData loadout, string skin, List<string> accs)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `player` | [`DewPlayer`](/api/Global.DewPlayer) |  |
| `hero` | [`Hero`](/api/Global.Hero) |  |
| `loadout` | [`HeroLoadoutData`](/api/Global.HeroLoadoutData) |  |
| `skin` | `string` |  |
| `accs` | `System.Collections.Generic.List<T><string>` |  |
