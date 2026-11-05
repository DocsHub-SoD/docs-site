# Class: MonsterPool

- **Namespace:** `Global`
- **Assembly:** `Dew.Core.dll`

```csharp
[CreateAssetMenu(fileName = "New Monster Pool", menuName = "Monster Pool")]
public class MonsterPool : ScriptableObject
```

## Fields

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`entries`** | `[ListDrawerSettings(Expanded = true)]
public List&lt;MonsterPool.SpawnRuleEntry&gt; entries` |  |
| **`scrambleOrder`** | `public bool scrambleOrder` |  |

## Methods

### `GetFilteredEntries()`

Get only the entries included in the build.

```csharp
public List<MonsterPool.SpawnRuleEntry> GetFilteredEntries()
```

**Returns:** `System.Collections.Generic.List&lt;T&gt;&lt;MonsterPool.SpawnRuleEntry&gt;`

### `GetMonsters(int, DewRandom)`

```csharp
public IEnumerator<Monster> GetMonsters(int sectionIndex, DewRandom random = null)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `sectionIndex` | `int` |  |
| `random` | [DewRandom](/api/Global.DewRandom) |  |

**Returns:** `System.Collections.Generic.IEnumerator&lt;T&gt;&lt;Monster&gt;`
