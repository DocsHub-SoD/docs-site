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
