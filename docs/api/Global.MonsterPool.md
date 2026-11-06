# Class: MonsterPool

- **Category:** <span class="cat-dot" style="--cat-color: #22c55e" data-cat="Actors & Entities"></span> Actors & Entities
- **Namespace:** `Global`
- **Assembly:** `Dew.Core.dll`

```csharp
[CreateAssetMenu(fileName = "New Monster Pool", menuName = "Monster Pool")]
public class MonsterPool : ScriptableObject
```

## Fields

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`entries`** | `[ListDrawerSettings(Expanded = true)] public List<MonsterPool.SpawnRuleEntry> entries` |  |
| **`scrambleOrder`** | `public bool scrambleOrder` |  |

## Methods

### `GetFilteredEntries()`

Get only the entries included in the build.

```csharp
public List<MonsterPool.SpawnRuleEntry> GetFilteredEntries()
```

**Returns:** `System.Collections.Generic.List<T><MonsterPool.SpawnRuleEntry>`

### `GetMonsters(int, DewRandom)`

```csharp
public IEnumerator<Monster> GetMonsters(int sectionIndex, DewRandom random = null)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `sectionIndex` | `int` |  |
| `random` | [`DewRandom`](/api/Global.DewRandom) |  |

**Returns:** `System.Collections.Generic.IEnumerator<T><Monster>`
