# Class: MonsterPool

- **Category:** <span class="cat-dot" style="--cat-color: #22c55e" data-cat="Actors & Entities"></span> Actors & Entities
- **Namespace:** `Global`
- **Assembly:** `Dew.Core.dll`
- **Attributes:** `[CreateAssetMenu]`

```csharp
[CreateAssetMenu(fileName = "New Monster Pool", menuName = "Monster Pool")]
public class MonsterPool : ScriptableObject
```

## Fields (2)

::: details Click to expand Fields (2)

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`entries`** | `[ListDrawerSettings(Expanded = true)] public List<MonsterPool.SpawnRuleEntry> entries` |  |
| **`scrambleOrder`** | `public bool scrambleOrder` |  |

:::

## Methods (2)

::: details `GetFilteredEntries()`

Get only the entries included in the build.

```csharp
public List<MonsterPool.SpawnRuleEntry> GetFilteredEntries()
```

**Returns:** `System.Collections.Generic.List<T><MonsterPool.SpawnRuleEntry>`

:::

::: details `GetMonsters(int, DewRandom)`

```csharp
public IEnumerator<Monster> GetMonsters(int sectionIndex, DewRandom random = null)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `sectionIndex` | `int` |  |
| `random` | [`DewRandom`](/api/Global.DewRandom) |  |

**Returns:** `System.Collections.Generic.IEnumerator<T><Monster>`

:::


## Architecture & Relationships

::: details Click to expand Architecture & Relationships

### Used By (8)

*Classes and systems that invoke, reference, or depend on `MonsterPool`:*

`Ai_Mon_Special_AmbushSpawner_Projectile` · [MonsterSpawnRule](/api/Global.MonsterSpawnRule) · [PreloadInterface](/api/Global.PreloadInterface) · `RoomMod_Ambush` · `RoomMod_DistantMemories` · `RoomMod_PureDream` · [RoomMonsters](/api/Global.RoomMonsters) · `Shrine_MorasDomain_HerPresence`

### Dependencies (3)

*Types and components that `MonsterPool` references or depends upon:*

[Dew](/api/Global.Dew) · [DewRandom](/api/Global.DewRandom) · [DewResources](/api/Global.DewResources)

:::
