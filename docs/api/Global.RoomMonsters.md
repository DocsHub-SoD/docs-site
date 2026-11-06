# Class: RoomMonsters

- **Category:** <span class="cat-dot" style="--cat-color: #22c55e" data-cat="Actors & Entities"></span> Actors & Entities
- **Namespace:** `Global`
- **Assembly:** `Dew.Core.dll`
- **Inheritance / Derived:** [DewNetworkBehaviour](/api/Global.DewNetworkBehaviour) → [RoomComponent](/api/Global.RoomComponent)

```csharp
[RoomComponentStartDependency(typeof(RoomModifiers))]
public class RoomMonsters : RoomComponent, ILogicUpdate
```

## Fields (24)

::: details Click to expand Fields (24)

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`addedHunterChance`** | `public float addedHunterChance` |  |
| **`addedMirageChance`** | `public float addedMirageChance` |  |
| **`campDensity`** | `[InfoBox("@Mathf.RoundToInt(campDensity * GetComponent<RoomMap>().mapData.area) + \" Camps\"", InfoMessageType.Info, null)] [HideIf("disableEnvSpawn", true)] public float campDensity` |  |
| **`campPopulation`** | `[HideIf("disableEnvSpawn", true)] public Vector2 campPopulation` |  |
| **`CampWanderRange`** | `public const float CampWanderRange = 6` |  |
| **`clearRoomOnClearAllCombatAreas`** | `[ToggleLeft] public bool clearRoomOnClearAllCombatAreas` |  |
| **`CombatAreaScoreRandomness`** | `public const float CombatAreaScoreRandomness = 0.3` |  |
| **`defaultRule`** | `public MonsterSpawnRule defaultRule` |  |
| **`destroyedSceneIds`** | `[NonSerialized] [SaveVar(SaveVarFlags.Default)] public List<ulong> destroyedSceneIds` | Available on server. Ids of objects that were in the room but has been destroyed. |
| **`disableEnvSpawn`** | `[Space(16)] public bool disableEnvSpawn` |  |
| **`disableMiniBossRewards`** | `[NonSerialized] public bool disableMiniBossRewards` |  |
| **`envSpawnPoolOverride`** | `[HideIf("disableEnvSpawn", true)] public MonsterPool envSpawnPoolOverride` |  |
| **`insertedCombatAreas`** | `public int insertedCombatAreas` |  |
| **`maxPopulationMultiplier`** | `public float maxPopulationMultiplier` |  |
| **`onAfterSpawn`** | `public SafeAction<Entity> onAfterSpawn` | Called on server. |
| **`onBeforeSpawn`** | `public SafeAction<Entity> onBeforeSpawn` | Called on server. |
| **`ongoingSpawns`** | `public Dictionary<SpawnMonsterSettings, Coroutine> ongoingSpawns` | Available on server. |
| **`onWelcomingSpawnEnd`** | `public SafeAction onWelcomingSpawnEnd` |  |
| **`onWelcomingSpawnStart`** | `public SafeAction onWelcomingSpawnStart` |  |
| **`OverpopulationStallDelayMax`** | `public const float OverpopulationStallDelayMax = 1.5` |  |
| **`OverpopulationStallDelayMin`** | `public const float OverpopulationStallDelayMin = 0.5` |  |
| **`SpawnDelayMax`** | `public const float SpawnDelayMax = 0.5` |  |
| **`SpawnDelayMin`** | `public const float SpawnDelayMin = 0.1` |  |
| **`spawnedPopMultiplier`** | `public float spawnedPopMultiplier` |  |

:::

## Properties (2)

::: details Click to expand Properties (2)

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`didSetupCombatAreas`** | `public bool didSetupCombatAreas { get; }` |  |
| **`isDoingHunterWelcomingSpawn`** | `public bool isDoingHunterWelcomingSpawn { get; }` | Available on server. |

:::

## Methods (12)

::: details `ActiveLogicUpdate(float)`

```csharp
protected override void ActiveLogicUpdate(float dt)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `dt` | `float` |  |

:::

::: details `FinishAllOngoingSpawns()`

```csharp
public void FinishAllOngoingSpawns()
```

:::

::: details `OnRoomStart()`

```csharp
public override void OnRoomStart()
```

:::

::: details `OnRoomStartServer()`

```csharp
public override void OnRoomStartServer()
```

:::

::: details `OnRoomStop()`

```csharp
public override void OnRoomStop()
```

:::

::: details `OnRoomStopServer()`

```csharp
public override void OnRoomStopServer()
```

:::

::: details `OverrideMonsterType(Monster)`

Make this room spawn a single type of monsters. This cannot be undone.

```csharp
public void OverrideMonsterType(Monster m)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `m` | [`Monster`](/api/Global.Monster) |  |

:::

::: details `RemoveAllCamps()`

Remove all camps and any spawned entities.

```csharp
public void RemoveAllCamps()
```

:::

::: details `SelectMiniBoss(out Entity, out MiniBossEffect, DewRandom)`

```csharp
public void SelectMiniBoss(out Entity entity, out MiniBossEffect effect, DewRandom random)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `entity` | [`Entity`](/api/Global.Entity) |  |
| `effect` | [`MiniBossEffect`](/api/Global.MiniBossEffect) |  |
| `random` | [`DewRandom`](/api/Global.DewRandom) |  |

:::

::: details `SpawnMiniBoss(SpawnMonsterSettings, Entity, StatusEffect)`

```csharp
public void SpawnMiniBoss(SpawnMonsterSettings settings, Entity ent = null, StatusEffect se = null)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `settings` | [`SpawnMonsterSettings`](/api/Global.SpawnMonsterSettings) |  |
| `ent` | [`Entity`](/api/Global.Entity) |  |
| `se` | [`StatusEffect`](/api/Global.StatusEffect) |  |

:::

::: details `SpawnMonsters(SpawnMonsterSettings)`

```csharp
public void SpawnMonsters(SpawnMonsterSettings settings)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `settings` | [`SpawnMonsterSettings`](/api/Global.SpawnMonsterSettings) |  |

:::

::: details `SpawnMonstersAsync(SpawnMonsterSettings)`

```csharp
public UniTask SpawnMonstersAsync(SpawnMonsterSettings settings)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `settings` | [`SpawnMonsterSettings`](/api/Global.SpawnMonsterSettings) |  |

**Returns:** `Cysharp.Threading.Tasks.UniTask`

:::
