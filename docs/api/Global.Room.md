# Class: Room

- **Category:** <span class="cat-dot" style="--cat-color: #3b82f6" data-cat="Managers & Systems"></span> Managers & Systems
- **Namespace:** `Global`
- **Assembly:** `Dew.Core.dll`
- **Attributes:** `[RequireComponent] [RequireComponent] [RequireComponent] [RequireComponent] [RequireComponent] [RequireComponent] [RequireComponent]`
- **Inheritance / Derived:** [DewNetworkBehaviour](/api/Global.DewNetworkBehaviour) → `SingletonDewNetworkBehaviour` → [Room](/api/Global.Room)

```csharp
[RequireComponent(typeof(RoomMap))]
[RequireComponent(typeof(RoomMonsters))]
[RequireComponent(typeof(RoomProps))]
[RequireComponent(typeof(RoomRifts))]
[RequireComponent(typeof(RoomRewards))]
[RequireComponent(typeof(RoomModifiers))]
[RequireComponent(typeof(RoomEditorMaintenance))]
public class Room : SingletonDewNetworkBehaviour<Room>, ILogicUpdate
```

## Fields (14)

::: details Click to expand Fields (14)

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`availableCameraAngles`** | `public float[] availableCameraAngles` |  |
| **`ClientEvent_OnFootstep`** | `public SafeAction<Entity> ClientEvent_OnFootstep` | Called everywhere everytime a footstep is done on an entity. |
| **`ClientEvent_OnPrepareAsNonHostileRoom`** | `public SafeAction ClientEvent_OnPrepareAsNonHostileRoom` |  |
| **`ClientEvent_OnRoomClear`** | `public SafeAction ClientEvent_OnRoomClear` |  |
| **`ClientEvent_OnRoomStart`** | `public SafeAction ClientEvent_OnRoomStart` |  |
| **`ClientEvent_WaypointLocked`** | `public SafeAction<Room_Waypoint> ClientEvent_WaypointLocked` |  |
| **`ClientEvent_WaypointUnlocked`** | `public SafeAction<Room_Waypoint> ClientEvent_WaypointUnlocked` |  |
| **`defaultSurface`** | `public DewSurfaceData defaultSurface` |  |
| **`metadata`** | `[ReadOnly] public DewRoomMetadata metadata` |  |
| **`music`** | `public DewMusicItem music` |  |
| **`onRemoveObstacles`** | `public SafeAction onRemoveObstacles` | This is called on server when this room needs to clear any progression obstacles.e.g. Barriers, Locked Shrines of Despair |
| **`onRoomClear`** | `[FoldoutGroup("Events", 0)] public UnityEvent onRoomClear` | Called on server when all combat sections are cleared / a hero steps on clear condition section. |
| **`openRoomExitOnClear`** | `[ToggleLeft] public bool openRoomExitOnClear` |  |
| **`playerPathablePoints`** | `public readonly List<Vector3> playerPathablePoints` | Available everywhere. |

:::

## Properties (16)

::: details Click to expand Properties (16)

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`didClearRoom`** | `public bool didClearRoom { get; }` | Available on server. |
| **`didRemoveObstacles`** | `public bool didRemoveObstacles { get; set; }` | Available on server. |
| **`heroSpawnPos`** | `public Vector3 heroSpawnPos { get; }` | Available on server. |
| **`heroSpawnRot`** | `public Quaternion heroSpawnRot { get; }` | Available on server. |
| **`isActive`** | `public bool isActive { get; }` |  |
| **`isNonHostileRoom`** | `public bool isNonHostileRoom { get; set; }` | Is this room modified to be a non-hostile room? Available everywhere. |
| **`isRevisit`** | `public bool isRevisit { get; set; }` | Are we revisiting this room? Available everywhere. |
| **`map`** | `public RoomMap map { get; }` |  |
| **`modifiers`** | `public RoomModifiers modifiers { get; }` |  |
| **`monsters`** | `public RoomMonsters monsters { get; }` |  |
| **`numOfActivatedCombatAreas`** | `public int numOfActivatedCombatAreas { get; }` |  |
| **`props`** | `public RoomProps props { get; }` |  |
| **`rewards`** | `public RoomRewards rewards { get; }` |  |
| **`rifts`** | `public RoomRifts rifts { get; }` |  |
| **`sections`** | `public IList<RoomSection> sections { get; }` |  |
| **`unlockedWaypoints`** | `public IReadOnlyList<Room_Waypoint> unlockedWaypoints { get; }` |  |

:::

## Methods (20)

::: details `AddUnlockedWaypoint(Room_Waypoint)`

```csharp
public void AddUnlockedWaypoint(Room_Waypoint waypoint)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `waypoint` | [`Room_Waypoint`](/api/Global.Room_Waypoint) |  |

:::

::: details `Awake()`

```csharp
protected override void Awake()
```

:::

::: details `ClearRoom()`

```csharp
public void ClearRoom()
```

:::

::: details `GetFinalSection()`

Get a section closest to exit rift.

```csharp
public RoomSection GetFinalSection()
```

**Returns:** `RoomSection`

:::

::: details `GetHeroSpawnPosition()`

Get randomly offset spawn position.

```csharp
public Vector3 GetHeroSpawnPosition()
```

**Returns:** `UnityEngine.Vector3`

:::

::: details `GetHeroSpawnRotation()`

Get spawn rotation.

```csharp
public Quaternion GetHeroSpawnRotation()
```

**Returns:** `UnityEngine.Quaternion`

:::

::: details `GetRoomRandom(int)`

Get a random instance for this room. States for these random instances are persistent.

```csharp
public DewRandom GetRoomRandom(int offset)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `offset` | `int` |  |

**Returns:** `DewRandom`

:::

::: details `GetSectionFromWorldPos(Vector3)`

```csharp
public RoomSection GetSectionFromWorldPos(Vector3 pos)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `pos` | `UnityEngine.Vector3` |  |

**Returns:** `RoomSection`

:::

::: details `OnLateStart()`

```csharp
public override void OnLateStart()
```

:::

::: details `OnLateStartServer()`

```csharp
public override void OnLateStartServer()
```

:::

::: details `OnStartClient()`

```csharp
public override void OnStartClient()
```

:::

::: details `OnStartServer()`

```csharp
public override void OnStartServer()
```

:::

::: details `OverrideHeroSpawn(Vector3, Quaternion)`

```csharp
public void OverrideHeroSpawn(Vector3 pos, Quaternion rot)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `pos` | `UnityEngine.Vector3` |  |
| `rot` | `UnityEngine.Quaternion` |  |

:::

::: details `RemoveCombat(bool)`

Disables enemy spawns, and removes any existing enemies or camps.It is recommended to call this with Dew.CallDelayed() if you're calling it in RoomModifierBase.OnCreate().

```csharp
public void RemoveCombat(bool clearRoomOnEnteringLastSection)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `clearRoomOnEnteringLastSection` | `bool` |  |

:::

::: details `RemoveObstacles()`

Remove any kind of progression-blocking obstacles, like barriers, locked teleport shrines and such.It is recommended to call this with Dew.CallDelayed() if you're calling it in RoomModifierBase.OnCreate().

```csharp
public void RemoveObstacles()
```

:::

::: details `RemoveUnlockedWaypoint(Room_Waypoint)`

```csharp
public void RemoveUnlockedWaypoint(Room_Waypoint waypoint)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `waypoint` | [`Room_Waypoint`](/api/Global.Room_Waypoint) |  |

:::

::: details `SetCameraAngleIndex_Local(int)`

```csharp
public void SetCameraAngleIndex_Local(int index)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `index` | `int` |  |

:::

::: details `StartRoom()`

```csharp
public void StartRoom()
```

:::

::: details `StopRoom()`

```csharp
public void StopRoom()
```

:::

::: details `SyncCameraAngle()`

```csharp
public void SyncCameraAngle()
```

:::


## Architecture & Relationships

::: details Click to expand Architecture & Relationships

### Used By (77)

*Classes and systems that invoke, reference, or depend on `Room`:*

`ACH_PRAYER_FOR_THE_DREAMERS` · `Ai_Mon_Special_AmbushSpawner_Projectile` · `Ai_UnstableRatSwarm_Projectile` · [ClearSectionEventData](/api/Global.ClearSectionEventData) · `DarkCaveCutSceneFogFadeOut` · [DevGameManager](/api/Global.DevGameManager) · `DewConsoleCommands` · `Forest_LoopCat_Spawner` · [GameManager](/api/Global.GameManager) · `GameMod_GoldenLizard` · [GameMod_Limbo](/api/Global.GameMod_Limbo) · [GameMod_MirageSkin](/api/Global.GameMod_MirageSkin) · `Ge_Shrine_PotOfGreed` · `Gem_R_Adventure` · `IPreemptiveMiniBossSection` · `LucidDream_FalseLifeline` · `LucidDream_MarshOfDestiny` · `Mon_Special_AmbushSpawner` · [MonsterSpawnCondition](/api/Global.MonsterSpawnCondition) · `Obliviax_Decoration_Generator` · [PlayGameManager](/api/Global.PlayGameManager) · [Rift_RoomExit](/api/Global.Rift_RoomExit) · [RoomComponent](/api/Global.RoomComponent) · `RoomMod_Ambush` · `RoomMod_ArcticTerritory` · `RoomMod_CallOfTheRavenous` · `RoomMod_ChallengingFight` · `RoomMod_CorruptedChaos_AuraOfPain` · `RoomMod_DistantMemories` · `RoomMod_FallenStar` · `RoomMod_FragmentOfRadiance_MysteriousPlace` · `RoomMod_FragmentOfRadiance_StartProp` · `RoomMod_GoldEverywhere` · `RoomMod_GuidingCompass_SpawnRift` · `RoomMod_HarderFightBetterReward` · `RoomMod_HeroSoul` · `RoomMod_Hunted` · `RoomMod_InkStrikeWarning` · `RoomMod_LeafPuppies` · `RoomMod_LingeringAuraOfGuidance` · `RoomMod_MeteoricLife` · `RoomMod_PureDream` · `RoomMod_RiskOfMeteors` · `RoomMod_SpawnHatred` · `RoomMod_SpawnJonasChamberRift` · `RoomMod_SpawnMawOfDoom` · `RoomMod_SpawnMiniBoss` · `RoomMod_SpawnParadox` · `RoomMod_SpawnPileOfSnow` · `RoomMod_StardustEverywhere` · `RoomMod_StrayMemory_StartProp` · [RoomModifierBase](/api/Global.RoomModifierBase) · [RoomMonsters](/api/Global.RoomMonsters) · [RoomProps](/api/Global.RoomProps) · [RoomRewards](/api/Global.RoomRewards) · [RoomRifts](/api/Global.RoomRifts) · [Room_Barrier](/api/Global.Room_Barrier) · [Room_Waypoint](/api/Global.Room_Waypoint) · `Se_LingeringAuraOfGuidance` · `Se_RoomMod_WarpingField_Unstable` · `Se_StarlessPath_PowerOfGuidance` · [Section_Monsters](/api/Global.Section_Monsters) · `Shrine_CallOfTheRavenous` · `Shrine_Despair` · `Shrine_Despair_Vestige` · `Shrine_Enlightenment` · `Shrine_FallenStar` · `Shrine_Luck` · `Shrine_Paradox` · `Shrine_Retrospection` · `Shrine_TheConsortOfNight` · [SpecialEntityRoomModifier](/api/Global.SpecialEntityRoomModifier) · `UI_InGame_Map` · `UI_InGame_Map_Item` · `UI_InGame_RoomModDisplay` · `WagesOfResolveBarrier` · [ZoneManager](/api/Global.ZoneManager)

### Dependencies (35)

*Types and components that `Room` references or depends upon:*

[Actor](/api/Global.Actor) · [ActorCheck](/api/Global.ActorCheck) · [AssetRef`1](/api/Global.AssetRef`1) · [CameraManager](/api/Global.CameraManager) · [Dew](/api/Global.Dew) · [DewMusicItem](/api/Global.DewMusicItem) · [DewNetworkBehaviour](/api/Global.DewNetworkBehaviour) · [DewPlayer](/api/Global.DewPlayer) · [DewPool](/api/Global.DewPool) · [DewRandom](/api/Global.DewRandom) · [DewRoomMetadata](/api/Global.DewRoomMetadata) · [DewSurfaceData](/api/Global.DewSurfaceData) · [Entity](/api/Global.Entity) · [IPlayerPathablePoint](/api/Global.IPlayerPathablePoint) · [ListReturnHandle`1](/api/Global.ListReturnHandle`1) · [ManagerBase`1](/api/Global.ManagerBase`1) · [MusicManager](/api/Global.MusicManager) · [NetworkedManagerBase`1](/api/Global.NetworkedManagerBase`1) · [Rift](/api/Global.Rift) · [Rift_RoomExit](/api/Global.Rift_RoomExit) · [RoomComponent](/api/Global.RoomComponent) · [RoomMap](/api/Global.RoomMap) · [RoomModifiers](/api/Global.RoomModifiers) · [RoomMonsters](/api/Global.RoomMonsters) · [RoomProps](/api/Global.RoomProps) · [RoomRewards](/api/Global.RoomRewards) · [RoomRifts](/api/Global.RoomRifts) · [RoomSection](/api/Global.RoomSection) · [Room_Waypoint](/api/Global.Room_Waypoint) · [SafeAction](/api/Global.SafeAction) · [SafeAction`1](/api/Global.SafeAction`1) · [Section_Monsters](/api/Global.Section_Monsters) · [SingletonDewNetworkBehaviour`1](/api/Global.SingletonDewNetworkBehaviour`1) · `VectorPlaneTransformExtension` · [ZoneManager](/api/Global.ZoneManager)

:::
