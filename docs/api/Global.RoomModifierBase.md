# Class: RoomModifierBase

- **Category:** <span class="cat-dot" style="--cat-color: #22c55e" data-cat="Actors & Entities"></span> Actors & Entities
- **Namespace:** `Global`
- **Assembly:** `Dew.Core.dll`
- **Inheritance / Derived:** [DewNetworkBehaviour](/api/Global.DewNetworkBehaviour) → [Actor](/api/Global.Actor) → [SpecialEntityRoomModifier](/api/Global.SpecialEntityRoomModifier)

```csharp
public class RoomModifierBase : Actor, ILogicUpdate, ICleanup, ICustomDestroyRoutine, IExcludeFromPool
```

## Fields (24)

::: details Click to expand Fields (24)

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`allowedZones`** | `[ShowIf("@chance > 0.000001f", true)] [InfoBox("All zones will be allowed to have this modifier", InfoMessageType.Info, "@allowedZones == null \|\| allowedZones.Length == 0")] [InfoBox("@GetZoneValidationMessage(allowedZones)", InfoMessageType.Error, "@GetZoneValidationMessage(allowedZones) != null")] public string[] allowedZones` |  |
| **`chance`** | `[LabelText("@spawnType.ToString()")] public float chance` |  |
| **`difficultyScaling`** | `[ShowIf("@chance > 0.000001f", true)] public ScaleWithDifficultyMode difficultyScaling` |  |
| **`disableOtherEnvParticles`** | `[ToggleLeft] public bool disableOtherEnvParticles` |  |
| **`disallowOtherModifiers`** | `[ShowIf("@chance > 0.000001f", true)] [ToggleLeft] public bool disallowOtherModifiers` |  |
| **`enableInnerDecorations`** | `[Title("Decorations", null, TitleAlignments.Left, true, true)] [ToggleLeft] public bool enableInnerDecorations` |  |
| **`enableOuterDecorations`** | `[ToggleLeft] public bool enableOuterDecorations` |  |
| **`excludeFromPool`** | `public bool excludeFromPool` |  |
| **`fxLoop`** | `[Title("Effects", null, TitleAlignments.Left, true, true)] public GameObject fxLoop` |  |
| **`hiddenOnVisitedNode`** | `[ShowIf("@isMain \|\| visibilityOnWorld != NodeModifierVisibility.Hidden", true)] public bool hiddenOnVisitedNode` |  |
| **`innerDecorations`** | `[BoxGroup("Inner Decorations", true, false, 0)] [InlineProperty] [HideLabel] [ShowIf("enableInnerDecorations", true)] public DecorationSettings innerDecorations` |  |
| **`isMain`** | `[FormerlySerializedAs] [Title("General", null, TitleAlignments.Left, true, true)] [FormerlySerializedAs("showOnTopRight")] public bool isMain` | Main modifiers will print notification when user enters the node.A node can only have a single main modifier. |
| **`mainColor`** | `[ShowIf("@isMain \|\| visibilityOnWorld != NodeModifierVisibility.Hidden", true)] public Color mainColor` |  |
| **`mapSprite`** | `[ShowIf("@isMain \|\| visibilityOnWorld != NodeModifierVisibility.Hidden", true)] public Sprite mapSprite` |  |
| **`mapSpriteScale`** | `[ShowIf("@isMain \|\| visibilityOnWorld != NodeModifierVisibility.Hidden", true)] public float mapSpriteScale` |  |
| **`modifiesRewards`** | `[ShowIf("@chance > 0.000001f", true)] [ToggleLeft] public bool modifiesRewards` |  |
| **`outerDecorations`** | `[BoxGroup("Outer Decorations", true, false, 0)] [InlineProperty] [HideLabel] [ShowIf("enableOuterDecorations", true)] public DecorationSettings outerDecorations` |  |
| **`removeModifierWhenOverrideOverwritten`** | `[ToggleLeft] [ShowIf("@!string.IsNullOrEmpty(roomOverride)", true)] public bool removeModifierWhenOverrideOverwritten` |  |
| **`roomOverride`** | `public string roomOverride` |  |
| **`spawnedDecorations`** | `public readonly List<GameObject> spawnedDecorations` |  |
| **`spawnOncePerLoop`** | `[ShowIf("@chance > 0.000001f", true)] [ToggleLeft] public bool spawnOncePerLoop` |  |
| **`spawnType`** | `[Title("Natural Spawn Settings", null, TitleAlignments.Left, true, true)] public ModifierSpawnType spawnType` |  |
| **`visibilityOnWorld`** | `public NodeModifierVisibility visibilityOnWorld` |  |
| **`zoneIndexRange`** | `[ShowIf("@chance > 0.000001f", true)] public Vector2Int zoneIndexRange` |  |

:::

## Properties (3)

::: details Click to expand Properties (3)

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`id`** | `[SaveVar] [SaveVar(SaveVarFlags.Default)] public int id { get; }` | Modifier id of this modifier instance. |
| **`isDestroyedOnRoomChange`** | `public override bool isDestroyedOnRoomChange { get; }` |  |
| **`modData`** | `public ModifierData modData { get; }` |  |

:::

## Methods (11)

::: details `CanSpawnAtNode(int)`

Checked on server, on the modifier prefab, when generating the world.It will be called in the middle of generating the world, but essential things like basic node positions and distances will be provided.

```csharp
public virtual bool CanSpawnAtNode(int nodeIndex)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `nodeIndex` | `int` |  |

**Returns:** `bool`

:::

::: details `GetScaledChance()`

```csharp
public float GetScaledChance()
```

**Returns:** `float`

:::

::: details `IsAvailableInGame()`

Is this modifier available in game? If false, this modifier will not be applied to nodes.Checked on server everytime when generating world.NOTE that in-game constellation registration happens AFTER first world generation!!!!

```csharp
public virtual bool IsAvailableInGame()
```

**Returns:** `bool`

:::

::: details `ModifyEntities(Action&lt;Entity&gt;, Action&lt;Entity&gt;)`

Modify all entities.onStart is called on all existing entities and entities spawned in the future.onStop is called on all existing entities when modifier stops.

```csharp
public void ModifyEntities(Action<Entity> onStart, Action<Entity> onStop)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `onStart` | [`System.Action<T><Entity>`](/api/Global.Entity) |  |
| `onStop` | [`System.Action<T><Entity>`](/api/Global.Entity) |  |

:::

::: details `OnCreate()`

```csharp
protected override void OnCreate()
```

:::

::: details `OnDestroyActor()`

```csharp
protected override void OnDestroyActor()
```

:::

::: details `OnStart()`

```csharp
public override void OnStart()
```

:::

::: details `PlaceDecorations(DecorationSettings, IReadOnlyList&lt;(int, int)&gt;)`

```csharp
public static List<GameObject> PlaceDecorations(DecorationSettings s, IReadOnlyList<(int, int)> indices)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `s` | [`DecorationSettings`](/api/Global.DecorationSettings) |  |
| `indices` | `System.Collections.Generic.IReadOnlyList<T><(int,int)>` |  |

**Returns:** `System.Collections.Generic.List<T><UnityEngine.GameObject>`

:::

::: details `PlaceShrine&lt;T&gt;(PlaceShrineSettings)`

Places a shrine on random position.This function properly handles revisits.Warning: does not support multiple shrines of same type

```csharp
public void PlaceShrine<T>(PlaceShrineSettings settings) where T : Shrine
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `settings` | [`PlaceShrineSettings`](/api/Global.PlaceShrineSettings) |  |
| `` | `T` |  |

:::

::: details `RemoveModifier()`

Remove and destroy this modifier.

```csharp
public void RemoveModifier()
```

:::

::: details `ShouldBeSavedWithRoom()`

```csharp
public override bool ShouldBeSavedWithRoom()
```

**Returns:** `bool`

:::


## Architecture & Relationships

::: details Click to expand Architecture & Relationships

### Used By (73)

*Classes and systems that invoke, reference, or depend on `RoomModifierBase`:*

`Obliviax_Decoration_Generator` · `RoomMod_AcceleratedTime` · `RoomMod_Ambush` · `RoomMod_Anitya` · `RoomMod_ArcticTerritory` · `RoomMod_Artifact` · `RoomMod_BlackRain` · `RoomMod_CallOfTheRavenous` · `RoomMod_ChallengingFight` · `RoomMod_CorruptedChaos_AuraOfPain` · `RoomMod_DarkCondensationZone` · `RoomMod_DistantMemories` · `RoomMod_EngulfedInFlame` · `RoomMod_FallenStar` · `RoomMod_FireDevil` · `RoomMod_FragmentOfRadiance_MysteriousPlace` · `RoomMod_FragmentOfRadiance_StartProp` · `RoomMod_GazeOfErebos` · `RoomMod_GlacialBarrier` · `RoomMod_GoldEverywhere` · `RoomMod_GravityTraining` · `RoomMod_GuidingCompass_SpawnRift` · `RoomMod_HarderFightBetterReward` · `RoomMod_HeroSoul` · `RoomMod_Hunted` · `RoomMod_InkStrikeWarning` · `RoomMod_InversionSigil` · `RoomMod_LeafPuppies` · `RoomMod_Limbo_Decorator` · `RoomMod_LingeringAuraOfGuidance` · `RoomMod_MerchantBackpack` · `RoomMod_MeteoricLife` · `RoomMod_MisticIceVein` · `RoomMod_NoMerchant` · `RoomMod_PureDream` · `RoomMod_RiskOfMeteors` · `RoomMod_SmallSoul` · `RoomMod_SpawnAltarOfCleansing` · `RoomMod_SpawnAscension` · `RoomMod_SpawnBlessedGuidance` · `RoomMod_SpawnDestiny` · `RoomMod_SpawnDisintegration` · `RoomMod_SpawnEntanglement` · `RoomMod_SpawnGuidance` · `RoomMod_SpawnHatred` · `RoomMod_SpawnHiddenStash` · `RoomMod_SpawnJonasChamberRift` · `RoomMod_SpawnMawOfDoom` · `RoomMod_SpawnMiniBoss` · `RoomMod_SpawnMirrorOfRemorse` · `RoomMod_SpawnParadox` · `RoomMod_SpawnPileOfSnow` · `RoomMod_SpawnPotOfGreed` · `RoomMod_SpawnWell` · `RoomMod_StarCookie` · `RoomMod_StardustEverywhere` · `RoomMod_StrangePlace` · `RoomMod_StrayMemory_StartProp` · `RoomMod_SuspiciousTreasureLocation` · `RoomMod_SymbioteHabitat` · `RoomMod_TheConsortOfNight_Raven` · `RoomMod_TheConsortOfNight_Raven_Marker` · `RoomMod_ToxicArea` · `RoomMod_Tutorial_Voice` · `RoomMod_UnstableRatSwarm` · `RoomMod_UnstableVeilOfTime` · `RoomMod_VeilOfDark` · `RoomMod_WagesOfResolve` · `RoomMod_WarpingField` · `Shrine_TheConsortOfNight` · [SpecialEntityRoomModifier](/api/Global.SpecialEntityRoomModifier) · `UI_InGame_RoomModDisplay` · [ZoneManager](/api/Global.ZoneManager)

### Dependencies (25)

*Types and components that `RoomModifierBase` references or depends upon:*

[Actor](/api/Global.Actor) · [ArrayReturnHandle`1](/api/Global.ArrayReturnHandle`1) · [Cells2D`1](/api/Global.Cells2D`1) · [DecorationSettings](/api/Global.DecorationSettings) · [Dew](/api/Global.Dew) · [DewNetworkBehaviour](/api/Global.DewNetworkBehaviour) · [DewPersistence](/api/Global.DewPersistence) · [DewPool](/api/Global.DewPool) · [DewResources](/api/Global.DewResources) · [Entity](/api/Global.Entity) · [EventInfoLoadRoom](/api/Global.EventInfoLoadRoom) · [GameManager](/api/Global.GameManager) · [IExcludeFromPool](/api/Global.IExcludeFromPool) · [MapData](/api/Global.MapData) · [ModifierData](/api/Global.ModifierData) · [NetworkedManagerBase`1](/api/Global.NetworkedManagerBase`1) · [PlaceShrineSettings](/api/Global.PlaceShrineSettings) · [Room](/api/Global.Room) · [RoomProps](/api/Global.RoomProps) · [RoomSection](/api/Global.RoomSection) · [SafeAction`1](/api/Global.SafeAction`1) · [Shrine](/api/Global.Shrine) · [SingletonDewNetworkBehaviour`1](/api/Global.SingletonDewNetworkBehaviour`1) · `VectorPlaneTransformExtension` · [ZoneManager](/api/Global.ZoneManager)

### Related Enums (4)

*Enumerations referenced in fields, properties, or method signatures:*

[`ModifierSpawnType`](/enums#modifierspawntype) · [`NodeModifierVisibility`](/enums#nodemodifiervisibility) · [`SaveVarFlags`](/enums#savevarflags) · [`ScaleWithDifficultyMode`](/enums#scalewithdifficultymode)

:::
