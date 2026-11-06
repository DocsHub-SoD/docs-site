# Class: RoomMonsters

- **Category:** <span class="cat-dot" style="--cat-color: #22c55e" data-cat="Actors & Entities"></span> Actors & Entities
- **Namespace:** `Global`
- **Assembly:** `Dew.Core.dll`
- **Attributes:** `[RoomComponentStartDependency]`
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
| **`destroyedSceneIds`** | `[SaveVar] [NonSerialized] [SaveVar(SaveVarFlags.Default)] public List<ulong> destroyedSceneIds` | Available on server. Ids of objects that were in the room but has been destroyed. |
| **`disableEnvSpawn`** | `[Space] [Space(16)] public bool disableEnvSpawn` |  |
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


## Architecture & Relationships

::: details Click to expand Architecture & Relationships

### Used By (8)

*Classes and systems that invoke, reference, or depend on `RoomMonsters`:*

`DewConsoleCommands` · [GameManager](/api/Global.GameManager) · [Room](/api/Global.Room) · `RoomMod_Ambush` · `RoomMod_LeafPuppies` · `RoomMod_MeteoricLife` · [Section_Monsters](/api/Global.Section_Monsters) · `Shrine_TheConsortOfNight`

### Dependencies (51)

*Types and components that `RoomMonsters` references or depends upon:*

[Actor](/api/Global.Actor) · [ActorManager](/api/Global.ActorManager) · `AdaptiveAbilityBaseline` · [AssetRef`1](/api/Global.AssetRef`1) · [CameraManager](/api/Global.CameraManager) · [Cells2D`1](/api/Global.Cells2D`1) · [Dew](/api/Global.Dew) · [DewEffect](/api/Global.DewEffect) · [DewPlayer](/api/Global.DewPlayer) · [DewRandom](/api/Global.DewRandom) · [DewResources](/api/Global.DewResources) · [Entity](/api/Global.Entity) · [EntityCheck](/api/Global.EntityCheck) · [EntityControl](/api/Global.EntityControl) · [GameManager](/api/Global.GameManager) · [GameMod_MirageSkin](/api/Global.GameMod_MirageSkin) · [Hero](/api/Global.Hero) · `IPreemptiveMiniBossSection` · `IPrewarmMiniBossContributor` · `IPrewarmMonsterContributor` · `IPrewarmPopulationMultiplier` · `IPrewarmRoomContributor` · [ISpawnableAsMiniBoss](/api/Global.ISpawnableAsMiniBoss) · [ListReturnHandle`1](/api/Global.ListReturnHandle`1) · [ManagerBase`1](/api/Global.ManagerBase`1) · [MapData](/api/Global.MapData) · [Monster](/api/Global.Monster) · `MonsterAbilityPrewarmConfig` · [MonsterPool](/api/Global.MonsterPool) · [MonsterSpawnRule](/api/Global.MonsterSpawnRule) · [NetworkedManagerBase`1](/api/Global.NetworkedManagerBase`1) · `QuaternionFlattenExtension` · [RefValue`1](/api/Global.RefValue`1) · [Room](/api/Global.Room) · [RoomComponent](/api/Global.RoomComponent) · [RoomSection](/api/Global.RoomSection) · [SafeAction](/api/Global.SafeAction) · [SafeAction`1](/api/Global.SafeAction`1) · [SafeAction`2](/api/Global.SafeAction`2) · [Section_Monsters](/api/Global.Section_Monsters) · [SingletonDewNetworkBehaviour`1](/api/Global.SingletonDewNetworkBehaviour`1) · [SpawnManager](/api/Global.SpawnManager) · [SpawnMonsterSettings](/api/Global.SpawnMonsterSettings) · [StatusEffect](/api/Global.StatusEffect) · [TransitionManager](/api/Global.TransitionManager) · [VariantDef](/api/Global.VariantDef) · `Vector3FlattenExtension` · `VectorPlaneTransformExtension` · [WorldNodeData](/api/Global.WorldNodeData) · [ZoneManager](/api/Global.ZoneManager) · `Mirror.GeneratedNetworkCode`

### Related Enums (1)

*Enumerations referenced in fields, properties, or method signatures:*

[`SaveVarFlags`](/enums#savevarflags)

:::
