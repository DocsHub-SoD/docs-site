# Class: SpawnMonsterSettings

- **Namespace:** `Global`
- **Assembly:** `Dew.Core.dll`

```csharp
public class SpawnMonsterSettings
```

## Fields

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`afterSpawn`** | `public Action&lt;Entity&gt; afterSpawn` |  |
| **`beforeSpawn`** | `public Action&lt;Entity&gt; beforeSpawn` |  |
| **`earlyFinishCondition`** | `public Func&lt;bool&gt; earlyFinishCondition` | This condition is checked before every spawn.When this evaluates to true, the spawn will be finished early. |
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
| **`spawnPosGetter`** | `public Func&lt;Vector3&gt; spawnPosGetter` |  |
| **`spawnRotGetter`** | `public Func&lt;Quaternion&gt; spawnRotGetter` |  |

## Methods

### `Clone()`

```csharp
public SpawnMonsterSettings Clone()
```

**Returns:** `SpawnMonsterSettings`
