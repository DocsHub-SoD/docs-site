# Class: RoomMonsters

- **Namespace:** `Global`
- **Assembly:** `Dew.Core.dll`
- **Inheritance / Derived:** [DewNetworkBehaviour](/api/Global.DewNetworkBehaviour) → [RoomComponent](/api/Global.RoomComponent)

```csharp
[RoomComponentStartDependency(typeof(RoomModifiers))]
public class RoomMonsters : RoomComponent, ILogicUpdate
```

## Fields

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`addedHunterChance`** | `public float addedHunterChance` |  |
| **`addedMirageChance`** | `public float addedMirageChance` |  |
| **`campDensity`** | `[InfoBox("@Mathf.RoundToInt(campDensity * GetComponent&lt;RoomMap&gt;().mapData.area) + \" Camps\"", InfoMessageType.Info, null)]
[HideIf("disableEnvSpawn", true)]
public float campDensity` |  |
| **`campPopulation`** | `[HideIf("disableEnvSpawn", true)]
public Vector2 campPopulation` |  |
| **`CampWanderRange`** | `public const float CampWanderRange = 6` |  |
| **`clearRoomOnClearAllCombatAreas`** | `[ToggleLeft]
public bool clearRoomOnClearAllCombatAreas` |  |
| **`CombatAreaScoreRandomness`** | `public const float CombatAreaScoreRandomness = 0.3` |  |
| **`defaultRule`** | `public MonsterSpawnRule defaultRule` |  |
| **`destroyedSceneIds`** | `[NonSerialized]
[SaveVar(SaveVarFlags.Default)]
public List&lt;ulong&gt; destroyedSceneIds` | Available on server. Ids of objects that were in the room but has been destroyed. |
| **`disableEnvSpawn`** | `[Space(16)]
public bool disableEnvSpawn` |  |
| **`disableMiniBossRewards`** | `[NonSerialized]
public bool disableMiniBossRewards` |  |
| **`envSpawnPoolOverride`** | `[HideIf("disableEnvSpawn", true)]
public MonsterPool envSpawnPoolOverride` |  |
| **`insertedCombatAreas`** | `public int insertedCombatAreas` |  |
| **`maxPopulationMultiplier`** | `public float maxPopulationMultiplier` |  |
| **`onAfterSpawn`** | `public SafeAction&lt;Entity&gt; onAfterSpawn` | Called on server. |
| **`onBeforeSpawn`** | `public SafeAction&lt;Entity&gt; onBeforeSpawn` | Called on server. |
| **`ongoingSpawns`** | `public Dictionary&lt;SpawnMonsterSettings, Coroutine&gt; ongoingSpawns` | Available on server. |
| **`onWelcomingSpawnEnd`** | `public SafeAction onWelcomingSpawnEnd` |  |
| **`onWelcomingSpawnStart`** | `public SafeAction onWelcomingSpawnStart` |  |
| **`OverpopulationStallDelayMax`** | `public const float OverpopulationStallDelayMax = 1.5` |  |
| **`OverpopulationStallDelayMin`** | `public const float OverpopulationStallDelayMin = 0.5` |  |
| **`SpawnDelayMax`** | `public const float SpawnDelayMax = 0.5` |  |
| **`SpawnDelayMin`** | `public const float SpawnDelayMin = 0.1` |  |
| **`spawnedPopMultiplier`** | `public float spawnedPopMultiplier` |  |

## Properties

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`didSetupCombatAreas`** | `public bool didSetupCombatAreas { get; }` |  |
| **`isDoingHunterWelcomingSpawn`** | `public bool isDoingHunterWelcomingSpawn { get; }` | Available on server. |

## Methods

### `ActiveLogicUpdate(float)`

```csharp
protected override void ActiveLogicUpdate(float dt)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `dt` | `float` |  |

### `FinishAllOngoingSpawns()`

```csharp
public void FinishAllOngoingSpawns()
```

### `OnRoomStart()`

```csharp
public override void OnRoomStart()
```

### `OnRoomStartServer()`

```csharp
public override void OnRoomStartServer()
```

### `OnRoomStop()`

```csharp
public override void OnRoomStop()
```

### `OnRoomStopServer()`

```csharp
public override void OnRoomStopServer()
```

### `OverrideMonsterType(Monster)`

Make this room spawn a single type of monsters. This cannot be undone.

```csharp
public void OverrideMonsterType(Monster m)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `m` | [Monster](/api/Global.Monster) |  |

### `RemoveAllCamps()`

Remove all camps and any spawned entities.

```csharp
public void RemoveAllCamps()
```

### `SelectMiniBoss(out Entity, out MiniBossEffect, DewRandom)`

```csharp
public void SelectMiniBoss(out Entity entity, out MiniBossEffect effect, DewRandom random)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `entity` | [Entity](/api/Global.Entity) |  |
| `effect` | [MiniBossEffect](/api/Global.MiniBossEffect) |  |
| `random` | [DewRandom](/api/Global.DewRandom) |  |

### `SpawnMiniBoss(SpawnMonsterSettings, Entity, StatusEffect)`

```csharp
public void SpawnMiniBoss(SpawnMonsterSettings settings, Entity ent = null, StatusEffect se = null)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `settings` | [SpawnMonsterSettings](/api/Global.SpawnMonsterSettings) |  |
| `ent` | [Entity](/api/Global.Entity) |  |
| `se` | [StatusEffect](/api/Global.StatusEffect) |  |

### `SpawnMonsters(SpawnMonsterSettings)`

```csharp
public void SpawnMonsters(SpawnMonsterSettings settings)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `settings` | [SpawnMonsterSettings](/api/Global.SpawnMonsterSettings) |  |

### `SpawnMonstersAsync(SpawnMonsterSettings)`

```csharp
public UniTask SpawnMonstersAsync(SpawnMonsterSettings settings)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `settings` | [SpawnMonsterSettings](/api/Global.SpawnMonsterSettings) |  |

**Returns:** `Cysharp.Threading.Tasks.UniTask`
