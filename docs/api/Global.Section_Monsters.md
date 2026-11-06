# Class: Section_Monsters

- **Category:** <span class="cat-dot" style="--cat-color: #22c55e" data-cat="Actors & Entities"></span> Actors & Entities
- **Namespace:** `Global`
- **Assembly:** `Dew.Core.dll`
- **Inheritance / Derived:** [LogicBehaviour](/api/Global.LogicBehaviour) → [RoomSectionComponent](/api/Global.RoomSectionComponent)

```csharp
public class Section_Monsters : RoomSectionComponent, ILogicUpdate
```

## Fields (9)

::: details Click to expand Fields (9)

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`activateCondition`** | `[ShowIf("@combatAreaSettings != SectionCombatAreaType.No", true)] public CombatAreaActivateCondition activateCondition` |  |
| **`addedInitDelay`** | `[ShowIf("@combatAreaSettings != SectionCombatAreaType.No", true)] public Vector2 addedInitDelay` |  |
| **`combatAreaSettings`** | `public SectionCombatAreaType combatAreaSettings` |  |
| **`miniBossCount`** | `[ShowIf("@combatAreaSettings != SectionCombatAreaType.No", true)] public int miniBossCount` |  |
| **`onClearCombatArea`** | `[FoldoutGroup("Events", 0)] public UnityEvent onClearCombatArea` |  |
| **`onStartCombatArea`** | `[FoldoutGroup("Events", 0)] public UnityEvent onStartCombatArea` |  |
| **`ruleOverride`** | `[ShowIf("@combatAreaSettings != SectionCombatAreaType.No", true)] public MonsterSpawnRule ruleOverride` |  |
| **`spawnMiniBossInstead`** | `[ShowIf("@combatAreaSettings != SectionCombatAreaType.No", true)] public bool spawnMiniBossInstead` |  |
| **`spawnPosOverride`** | `[ShowIf("@combatAreaSettings != SectionCombatAreaType.No", true)] public Transform spawnPosOverride` |  |

:::

## Properties (6)

::: details Click to expand Properties (6)

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`didClearCombatArea`** | `public bool didClearCombatArea { get; set; }` | Available on server. |
| **`isCombatActive`** | `public bool isCombatActive { get; }` | Available on server. |
| **`isMarkedAsCombatArea`** | `public bool isMarkedAsCombatArea { get; set; }` | Available on server. |
| **`isOverPopulation`** | `public bool isOverPopulation { get; }` | Available on server. |
| **`maxPopulation`** | `public float maxPopulation { get; }` |  |
| **`population`** | `public float population { get; }` | Available on server. |

:::

## Methods (3)

::: details `Awake()`

```csharp
protected override void Awake()
```

:::

::: details `GetSpawnPositionInSection(Func&lt;Vector3, bool&gt;, DewRandom)`

Evaluator will be provided raw position without NavMesh, ground or any checks.Position got passed by evaluator might not be returned as result of this function.

```csharp
public Vector3 GetSpawnPositionInSection(Func<Vector3, bool> evaluator = null, DewRandom random = null)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `evaluator` | `System.Func<T, TResult><UnityEngine.Vector3,bool>` |  |
| `random` | [`DewRandom`](/api/Global.DewRandom) |  |

**Returns:** `UnityEngine.Vector3`

:::

::: details `GetSpawnPositionInSection(float, float, DewRandom)`

```csharp
public Vector3 GetSpawnPositionInSection(float minDist, float maxDist, DewRandom random = null)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `minDist` | `float` |  |
| `maxDist` | `float` |  |
| `random` | [`DewRandom`](/api/Global.DewRandom) |  |

**Returns:** `UnityEngine.Vector3`

:::
