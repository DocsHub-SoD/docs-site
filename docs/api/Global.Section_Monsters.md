# Class: Section_Monsters

- **Namespace:** `Global`
- **Assembly:** `Dew.Core.dll`
- **Inheritance / Derived:** [LogicBehaviour](/api/Global.LogicBehaviour) → [RoomSectionComponent](/api/Global.RoomSectionComponent)

```csharp
public class Section_Monsters : RoomSectionComponent, ILogicUpdate
```

## Fields

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`activateCondition`** | `[ShowIf("@combatAreaSettings != SectionCombatAreaType.No", true)]
public CombatAreaActivateCondition activateCondition` |  |
| **`addedInitDelay`** | `[ShowIf("@combatAreaSettings != SectionCombatAreaType.No", true)]
public Vector2 addedInitDelay` |  |
| **`combatAreaSettings`** | `public SectionCombatAreaType combatAreaSettings` |  |
| **`miniBossCount`** | `[ShowIf("@combatAreaSettings != SectionCombatAreaType.No", true)]
public int miniBossCount` |  |
| **`onClearCombatArea`** | `[FoldoutGroup("Events", 0)]
public UnityEvent onClearCombatArea` |  |
| **`onStartCombatArea`** | `[FoldoutGroup("Events", 0)]
public UnityEvent onStartCombatArea` |  |
| **`ruleOverride`** | `[ShowIf("@combatAreaSettings != SectionCombatAreaType.No", true)]
public MonsterSpawnRule ruleOverride` |  |
| **`spawnMiniBossInstead`** | `[ShowIf("@combatAreaSettings != SectionCombatAreaType.No", true)]
public bool spawnMiniBossInstead` |  |
| **`spawnPosOverride`** | `[ShowIf("@combatAreaSettings != SectionCombatAreaType.No", true)]
public Transform spawnPosOverride` |  |

## Properties

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`didClearCombatArea`** | `public bool didClearCombatArea { get; set; }` | Available on server. |
| **`isCombatActive`** | `public bool isCombatActive { get; }` | Available on server. |
| **`isMarkedAsCombatArea`** | `public bool isMarkedAsCombatArea { get; set; }` | Available on server. |
| **`isOverPopulation`** | `public bool isOverPopulation { get; }` | Available on server. |
| **`maxPopulation`** | `public float maxPopulation { get; }` |  |
| **`population`** | `public float population { get; }` | Available on server. |

## Methods

### `Awake()`

```csharp
protected override void Awake()
```

### `GetSpawnPositionInSection(Func&lt;Vector3, bool&gt;, DewRandom)`

Evaluator will be provided raw position without NavMesh, ground or any checks.Position got passed by evaluator might not be returned as result of this function.

```csharp
public Vector3 GetSpawnPositionInSection(Func<Vector3, bool> evaluator = null, DewRandom random = null)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `evaluator` | `System.Func&lt;T, TResult&gt;&lt;UnityEngine.Vector3,bool&gt;` |  |
| `random` | [DewRandom](/api/Global.DewRandom) |  |

**Returns:** `UnityEngine.Vector3`

### `GetSpawnPositionInSection(float, float, DewRandom)`

```csharp
public Vector3 GetSpawnPositionInSection(float minDist, float maxDist, DewRandom random = null)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `minDist` | `float` |  |
| `maxDist` | `float` |  |
| `random` | [DewRandom](/api/Global.DewRandom) |  |

**Returns:** `UnityEngine.Vector3`
