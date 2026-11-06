# Class: SpecialEntityRoomModifier

- **Category:** <span class="cat-dot" style="--cat-color: #22c55e" data-cat="Actors & Entities"></span> Actors & Entities
- **Namespace:** `Global`
- **Assembly:** `Dew.Core.dll`
- **Inheritance / Derived:** [DewNetworkBehaviour](/api/Global.DewNetworkBehaviour) → [Actor](/api/Global.Actor) → [RoomModifierBase](/api/Global.RoomModifierBase)

```csharp
public abstract class SpecialEntityRoomModifier : RoomModifierBase, ILogicUpdate, ICleanup, ICustomDestroyRoutine, IExcludeFromPool
```

## Fields

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`dontSpawnIfHunted`** | `public bool dontSpawnIfHunted` |  |
| **`spawnedDreamDust`** | `public Vector2Int spawnedDreamDust` |  |
| **`spawnedGold`** | `public Vector2Int spawnedGold` |  |
| **`spawnedStardust`** | `public Vector2Int spawnedStardust` |  |

## Methods

### `GetEntityType()`

```csharp
protected abstract Type GetEntityType()
```

**Returns:** `System.Type`

### `OnCreate()`

```csharp
protected override void OnCreate()
```

### `OnDestroyActor()`

```csharp
protected override void OnDestroyActor()
```

### `SpawnNpc(Vector3)`

```csharp
protected virtual Entity SpawnNpc(Vector3 pos)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `pos` | `UnityEngine.Vector3` |  |

**Returns:** `Entity`
