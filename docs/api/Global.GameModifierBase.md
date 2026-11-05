# Class: GameModifierBase

- **Namespace:** `Global`
- **Assembly:** `Dew.Core.dll`
- **Inheritance / Derived:** [DewNetworkBehaviour](/api/Global.DewNetworkBehaviour) → [Actor](/api/Global.Actor) → [GameEffect](/api/Global.GameEffect) → [GameMod_Limbo](/api/Global.GameMod_Limbo) → [GameMod_MirageSkin](/api/Global.GameMod_MirageSkin)

```csharp
public class GameModifierBase : GameEffect, ILogicUpdate, ICleanup, ICustomDestroyRoutine, IExcludeFromPool
```

## Fields

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`excludeFromPool`** | `public bool excludeFromPool` |  |

## Methods

### `OnStartClientLobby()`

Called in the lobby scene on the prefab asset, if this game modifier is included in current game.

```csharp
public virtual void OnStartClientLobby()
```

### `OnStartServerLobby()`

Called in the lobby scene on the prefab asset, if this game modifier is included in current game.

```csharp
public virtual void OnStartServerLobby()
```
