# Class: SingletonDewNetworkBehaviour&lt;T&gt;

- **Category:** <span class="cat-dot" style="--cat-color: #06b6d4" data-cat="Networking"></span> Networking
- **Namespace:** `Global`
- **Assembly:** `Dew.Core.dll`
- **Inheritance / Derived:** [DewNetworkBehaviour](/api/Global.DewNetworkBehaviour) → [Room](/api/Global.Room)

```csharp
public class SingletonDewNetworkBehaviour<T> : DewNetworkBehaviour, ILogicUpdate where T : MonoBehaviour
```

## Properties (2)

::: details Click to expand Properties (2)

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`instance`** | `public static T instance { get; }` | If you expect the instance to be null, you MUST USE softInstance in Update loops.This will call FindObjectOfType if current instance is null, which can be very expensive. |
| **`softInstance`** | `public static T softInstance { get; }` |  |

:::

## Methods (1)

::: details `Awake()`

```csharp
protected override void Awake()
```

:::


## Architecture & Relationships

::: details Click to expand Architecture & Relationships

### Used By (87)

*Classes and systems that invoke, reference, or depend on `SingletonDewNetworkBehaviour<T>`:*

`ACH_PRAYER_FOR_THE_DREAMERS` · [ActorManager](/api/Global.ActorManager) · `Ai_Mon_Special_AmbushSpawner_Projectile` · `Ai_UnstableRatSwarm_Projectile` · `DarkCaveCutSceneFogFadeOut` · `DewConsoleCommands` · [DewPersistence](/api/Global.DewPersistence) · [EntitySound](/api/Global.EntitySound) · `Forest_LoopCat_Spawner` · [GameManager](/api/Global.GameManager) · `GameMod_GoldenLizard` · [GameMod_Limbo](/api/Global.GameMod_Limbo) · [GameMod_MirageSkin](/api/Global.GameMod_MirageSkin) · `GameMod_StarlessPath` · `Ge_Shrine_PotOfGreed` · `Gem_R_Adventure` · [InGameCrashReportManager](/api/Global.InGameCrashReportManager) · `Ink_BossRoomDamageGround` · `LucidDream_FalseLifeline` · `LucidDream_MarshOfDestiny` · `Mon_Primus_BossPrimusAeron` · `Mon_Special_AmbushSpawner` · `Obliviax_Decoration_Generator` · `PlayTutorial_Tutorial_Hunt` · `PlayTutorial_Tutorial_Intro` · `PlayTutorial_Tutorial_SkillsAndEssences` · `Primus_Ending` · [Rift_RoomExit](/api/Global.Rift_RoomExit) · [Room](/api/Global.Room) · `RoomMod_Ambush` · `RoomMod_ArcticTerritory` · `RoomMod_Artifact` · `RoomMod_CallOfTheRavenous` · `RoomMod_ChallengingFight` · `RoomMod_CorruptedChaos_AuraOfPain` · `RoomMod_DistantMemories` · `RoomMod_FallenStar` · `RoomMod_FragmentOfRadiance_MysteriousPlace` · `RoomMod_FragmentOfRadiance_StartProp` · `RoomMod_GoldEverywhere` · `RoomMod_GuidingCompass_SpawnRift` · `RoomMod_HarderFightBetterReward` · `RoomMod_HeroSoul` · `RoomMod_Hunted` · `RoomMod_InkStrikeWarning` · `RoomMod_LeafPuppies` · `RoomMod_LingeringAuraOfGuidance` · `RoomMod_MeteoricLife` · `RoomMod_PureDream` · `RoomMod_RiskOfMeteors` · `RoomMod_SpawnHatred` · `RoomMod_SpawnJonasChamberRift` · `RoomMod_SpawnMawOfDoom` · `RoomMod_SpawnMiniBoss` · `RoomMod_SpawnParadox` · `RoomMod_SpawnPileOfSnow` · `RoomMod_StardustEverywhere` · `RoomMod_StrayMemory_StartProp` · [RoomModifierBase](/api/Global.RoomModifierBase) · [RoomMonsters](/api/Global.RoomMonsters) · [RoomRewards](/api/Global.RoomRewards) · [RoomRifts](/api/Global.RoomRifts) · [RoomSection](/api/Global.RoomSection) · [Room_Barrier](/api/Global.Room_Barrier) · [Room_Waypoint](/api/Global.Room_Waypoint) · `Se_LingeringAuraOfGuidance` · `Se_ObliviaxKidnap` · `Se_RoomMod_WarpingField_Unstable` · `Se_StarlessPath_PowerOfGuidance` · [Section_Monsters](/api/Global.Section_Monsters) · `Shrine_CallOfTheRavenous` · `Shrine_Despair` · `Shrine_Despair_Vestige` · `Shrine_Enlightenment` · `Shrine_FallenStar` · `Shrine_Luck` · `Shrine_Paradox` · `Shrine_PrimusEndingLightPillar` · `Shrine_Retrospection` · `Shrine_TheConsortOfNight` · `Sky_WhiteVeil` · [SpecialEntityRoomModifier](/api/Global.SpecialEntityRoomModifier) · `UI_InGame_Map` · `UI_InGame_Map_Item` · `UI_InGame_RoomModDisplay` · `WagesOfResolveBarrier` · [ZoneManager](/api/Global.ZoneManager)

### Dependencies (1)

*Types and components that `SingletonDewNetworkBehaviour<T>` references or depends upon:*

[DewNetworkBehaviour](/api/Global.DewNetworkBehaviour)

:::
