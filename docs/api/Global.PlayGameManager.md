# Class: PlayGameManager

- **Category:** <span class="cat-dot" style="--cat-color: #3b82f6" data-cat="Managers & Systems"></span> Managers & Systems
- **Namespace:** `Global`
- **Assembly:** `Dew.Core.dll`
- **Attributes:** `[DewResourceLink]`
- **Inheritance / Derived:** [DewNetworkBehaviour](/api/Global.DewNetworkBehaviour) → `NetworkedManagerBase` → [GameManager](/api/Global.GameManager) → [GameManager](/api/Global.GameManager)

```csharp
[DewResourceLink(ResourceLinkBy.Type)]
public class PlayGameManager : GameManager, ILogicUpdate
```

## Properties (1)

::: details Click to expand Properties (1)

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`instance`** | `public static PlayGameManager instance { get; }` |  |

:::

## Methods (7)

::: details `DoDejavuSpawn(DewPlayer)`

```csharp
public void DoDejavuSpawn(DewPlayer h)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `h` | [`DewPlayer`](/api/Global.DewPlayer) |  |

:::

::: details `GetDifficulty()`

```csharp
protected override DewDifficultySettings GetDifficulty()
```

**Returns:** `DewDifficultySettings`

:::

::: details `IsContinueSaveSupported()`

```csharp
public override bool IsContinueSaveSupported()
```

**Returns:** `bool`

:::

::: details `LoadNextZone()`

```csharp
public override void LoadNextZone()
```

:::

::: details `OnLateStartServer()`

```csharp
public override void OnLateStartServer()
```

:::

::: details `OnStartClient()`

```csharp
public override void OnStartClient()
```

:::

::: details `SpawnHero(DewPlayer, Hero, HeroLoadoutData, string, List&lt;string&gt;)`

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

:::


## Architecture & Relationships

::: details Click to expand Architecture & Relationships

### Used By (0)

*No incoming dependencies recorded.*

### Dependencies (16)

*Types and components that `PlayGameManager` references or depends upon:*

[Dew](/api/Global.Dew) · [DewBuildProfile](/api/Global.DewBuildProfile) · [DewDifficultySettings](/api/Global.DewDifficultySettings) · [DewNetworkBehaviour](/api/Global.DewNetworkBehaviour) · [DewPlayer](/api/Global.DewPlayer) · [DewResources](/api/Global.DewResources) · [Entity](/api/Global.Entity) · [EntityStatus](/api/Global.EntityStatus) · [GameManager](/api/Global.GameManager) · [GameSettingsManager](/api/Global.GameSettingsManager) · [Hero](/api/Global.Hero) · [HeroLoadoutData](/api/Global.HeroLoadoutData) · [NetworkedManagerBase`1](/api/Global.NetworkedManagerBase`1) · [Room](/api/Global.Room) · [StatBonus](/api/Global.StatBonus) · [ZoneManager](/api/Global.ZoneManager)

:::
