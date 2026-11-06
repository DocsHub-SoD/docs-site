# Class: MonsterSpawnRule

- **Category:** <span class="cat-dot" style="--cat-color: #22c55e" data-cat="Actors & Entities"></span> Actors & Entities
- **Namespace:** `Global`
- **Assembly:** `Dew.Core.dll`
- **Attributes:** `[CreateAssetMenu]`

```csharp
[CreateAssetMenu(fileName = "New Monster Spawn Rule", menuName = "Monster Spawn Rule")]
public class MonsterSpawnRule : ScriptableObject
```

## Fields (13)

::: details Click to expand Fields (13)

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`initialDelay`** | `public Vector2 initialDelay` |  |
| **`isBossSpawn`** | `public bool isBossSpawn` |  |
| **`nextWavePopulationThreshold`** | `[HideIf("isBossSpawn", true)] public Vector2 nextWavePopulationThreshold` |  |
| **`onOverPopulation`** | `[HideIf("isBossSpawn", true)] public OverpopulationBehavior onOverPopulation` |  |
| **`pool`** | `public MonsterPool pool` |  |
| **`populationPerWave`** | `[HideIf("isBossSpawn", true)] public Vector2 populationPerWave` |  |
| **`spawnMaxDistance`** | `public float spawnMaxDistance` |  |
| **`spawnMinDistance`** | `public float spawnMinDistance` |  |
| **`stallCancelTimeout`** | `[ShowIf("@onOverPopulation == OverpopulationBehavior.Stall", true)] [HideIf("isBossSpawn", true)] public float stallCancelTimeout` |  |
| **`wavesMax`** | `[HideIf("isBossSpawn", true)] [HorizontalGroup("Waves Min, Max/A", 0, 0, 0, 0)] [HideLabel] public int wavesMax` |  |
| **`wavesMin`** | `[TitleGroup("Waves Min, Max", null, TitleAlignments.Left, true, true, false, 0, HorizontalLine = false, BoldTitle = false)] [HorizontalGroup("Waves Min, Max/A", 0, 0, 0, 0)] [HideLabel] [HideIf("isBossSpawn", true)] public int wavesMin` |  |
| **`waveTimeoutMax`** | `[HorizontalGroup("Wave Timeout Min, Max/A", 0, 0, 0, 0)] [HideLabel] [HideIf("isBossSpawn", true)] public float waveTimeoutMax` |  |
| **`waveTimeoutMin`** | `[TitleGroup("Wave Timeout Min, Max", null, TitleAlignments.Left, true, true, false, 0, HorizontalLine = false, BoldTitle = false)] [HorizontalGroup("Wave Timeout Min, Max/A", 0, 0, 0, 0)] [HideLabel] [HideIf("isBossSpawn", true)] public float waveTimeoutMin` |  |

:::


## Architecture & Relationships

::: details Click to expand Architecture & Relationships

### Used By (6)

*Classes and systems that invoke, reference, or depend on `MonsterSpawnRule`:*

`Ink_BossSelector` · [RoomMonsters](/api/Global.RoomMonsters) · [Section_Monsters](/api/Global.Section_Monsters) · `Shrine_MorasDomain_HerPresence` · [SpawnMonsterSettings](/api/Global.SpawnMonsterSettings) · [Zone](/api/Global.Zone)

### Dependencies (1)

*Types and components that `MonsterSpawnRule` references or depends upon:*

[MonsterPool](/api/Global.MonsterPool)

### Related Enums (1)

*Enumerations referenced in fields, properties, or method signatures:*

[`OverpopulationBehavior`](/enums#overpopulationbehavior)

:::
