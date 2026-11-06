# Class: GameModifierBase

- **Category:** <span class="cat-dot" style="--cat-color: #22c55e" data-cat="Actors & Entities"></span> Actors & Entities
- **Namespace:** `Global`
- **Assembly:** `Dew.Core.dll`
- **Inheritance / Derived:** [DewNetworkBehaviour](/api/Global.DewNetworkBehaviour) → [Actor](/api/Global.Actor) → [GameEffect](/api/Global.GameEffect) → [GameMod_Limbo](/api/Global.GameMod_Limbo) → [GameMod_MirageSkin](/api/Global.GameMod_MirageSkin)

```csharp
public class GameModifierBase : GameEffect, ILogicUpdate, ICleanup, ICustomDestroyRoutine, IExcludeFromPool
```

## Fields (1)

::: details Click to expand Fields (1)

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`excludeFromPool`** | `public bool excludeFromPool` |  |

:::

## Methods (2)

::: details `OnStartClientLobby()`

Called in the lobby scene on the prefab asset, if this game modifier is included in current game.

```csharp
public virtual void OnStartClientLobby()
```

:::

::: details `OnStartServerLobby()`

Called in the lobby scene on the prefab asset, if this game modifier is included in current game.

```csharp
public virtual void OnStartServerLobby()
```

:::


## Architecture & Relationships

::: details Click to expand Architecture & Relationships

### Used By (10)

*Classes and systems that invoke, reference, or depend on `GameModifierBase`:*

`GameMod_CorruptedChaos` · `GameMod_DespairFixStuck` · `GameMod_GoldenLizard` · [GameMod_Limbo](/api/Global.GameMod_Limbo) · [GameMod_MirageSkin](/api/Global.GameMod_MirageSkin) · `GameMod_MorasDomain` · `GameMod_Obliviax` · `GameMod_SantaHat` · `GameMod_StarlessPath` · [GameSettingsManager](/api/Global.GameSettingsManager)

### Dependencies (2)

*Types and components that `GameModifierBase` references or depends upon:*

[GameEffect](/api/Global.GameEffect) · [IExcludeFromPool](/api/Global.IExcludeFromPool)

:::
