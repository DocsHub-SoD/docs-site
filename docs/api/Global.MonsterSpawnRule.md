# Class: MonsterSpawnRule

- **Category:** <span class="cat-dot" style="--cat-color: #22c55e" data-cat="Actors & Entities"></span> Actors & Entities
- **Namespace:** `Global`
- **Assembly:** `Dew.Core.dll`

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
