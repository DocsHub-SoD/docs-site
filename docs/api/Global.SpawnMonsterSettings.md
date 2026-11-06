# Class: SpawnMonsterSettings

- **Category:** <span class="cat-dot" style="--cat-color: #22c55e" data-cat="Actors & Entities"></span> Actors & Entities
- **Namespace:** `Global`
- **Assembly:** `Dew.Core.dll`

```csharp
public class SpawnMonsterSettings
```

## Fields (16)

::: details Click to expand Fields (16)

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`afterSpawn`** | `public Action<Entity> afterSpawn` |  |
| **`beforeSpawn`** | `public Action<Entity> beforeSpawn` |  |
| **`earlyFinishCondition`** | `public Func<bool> earlyFinishCondition` | This condition is checked before every spawn.When this evaluates to true, the spawn will be finished early. |
| **`hero`** | `public Hero hero` |  |
| **`ignoreCoopPopMultiplier`** | `public bool ignoreCoopPopMultiplier` |  |
| **`ignoreTurnPopMultiplier`** | `public bool ignoreTurnPopMultiplier` |  |
| **`initDelayFlat`** | `public float initDelayFlat` |  |
| **`initDelayMultiplier`** | `public float initDelayMultiplier` |  |
| **`monsterSpawnData`** | `public RoomMonsters.MonsterSpawnData monsterSpawnData` |  |
| **`onFinish`** | `public Action onFinish` |  |
| **`random`** | `public DewRandom random` |  |
| **`rule`** | `public MonsterSpawnRule rule` |  |
| **`section`** | `public RoomSection section` |  |
| **`spawnPopulationMultiplier`** | `public float spawnPopulationMultiplier` |  |
| **`spawnPosGetter`** | `public Func<Vector3> spawnPosGetter` |  |
| **`spawnRotGetter`** | `public Func<Quaternion> spawnRotGetter` |  |

:::

## Methods (1)

::: details `Clone()`

```csharp
public SpawnMonsterSettings Clone()
```

**Returns:** `SpawnMonsterSettings`

:::


## Architecture & Relationships

::: details Click to expand Architecture & Relationships

### Used By (1)

*Classes and systems that invoke, reference, or depend on `SpawnMonsterSettings`:*

[RoomMonsters](/api/Global.RoomMonsters)

### Dependencies (4)

*Types and components that `SpawnMonsterSettings` references or depends upon:*

[DewRandom](/api/Global.DewRandom) · [Hero](/api/Global.Hero) · [MonsterSpawnRule](/api/Global.MonsterSpawnRule) · [RoomSection](/api/Global.RoomSection)

:::
