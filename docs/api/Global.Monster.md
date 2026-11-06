# Class: Monster

- **Category:** <span class="cat-dot" style="--cat-color: #22c55e" data-cat="Actors & Entities"></span> Actors & Entities
- **Namespace:** `Global`
- **Assembly:** `Dew.Core.dll`
- **Inheritance / Derived:** [DewNetworkBehaviour](/api/Global.DewNetworkBehaviour) → [Actor](/api/Global.Actor) → [Entity](/api/Global.Entity) → [BossMonster](/api/Global.BossMonster) → [Mon_DreamTeller](/api/Global.Mon_DreamTeller) → [Mon_RedGiant](/api/Global.Mon_RedGiant) → [Mon_RedMan](/api/Global.Mon_RedMan)

```csharp
public class Monster : Entity, ILogicUpdate, ICleanup, ICustomDestroyRoutine
```

## Fields (4)

::: details Click to expand Fields (4)

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`chasePredictiveness`** | `[BoxGroup("Monster Settings", true, false, 0)] public float chasePredictiveness` |  |
| **`chaseRandomness`** | `[BoxGroup("Monster Settings", true, false, 0)] public float chaseRandomness` |  |
| **`disableLoot`** | `[NonSerialized] public bool disableLoot` |  |
| **`type`** | `[SyncVar] [BoxGroup("Monster Settings", true, false, 0)] public Monster.MonsterType type` |  |

:::

## Properties (6)

::: details Click to expand Properties (6)

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`campPosition`** | `[SaveVar] [SaveVar(SaveVarFlags.Default)] public Vector3? campPosition { get; }` | Available on server. |
| **`defaultOwner`** | `protected override DewPlayer defaultOwner { get; }` |  |
| **`isHunter`** | `public bool isHunter { get; set; }` |  |
| **`populationCost`** | `public float populationCost { get; set; }` |  |
| **`spawnPosOverride`** | `public virtual Vector3? spawnPosOverride { get; }` | Override spawn position for this monster. This has higher priority than all other spawn pos overrides. |
| **`spawnRotOverride`** | `public virtual Quaternion? spawnRotOverride { get; }` | Override spawn rotation for this monster. This has higher priority than all other spawn rot overrides. |

:::

## Methods (5)

::: details `AIUpdate(ref EntityAIContext)`

```csharp
protected override void AIUpdate(ref EntityAIContext context)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `context` | [`EntityAIContext`](/api/Global.EntityAIContext) |  |

:::

::: details `GetStaggerSettings()`

```csharp
protected override Entity.StaggerSettings GetStaggerSettings()
```

**Returns:** `Entity.StaggerSettings`

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

::: details `OnStartServer()`

```csharp
public override void OnStartServer()
```

:::


## Architecture & Relationships

::: details Click to expand Architecture & Relationships

### Used By (82)

*Classes and systems that invoke, reference, or depend on `Monster`:*

[AbilityTrigger](/api/Global.AbilityTrigger) · `Ai_Mon_Forest_SpiderWarrior_SpawnScarabs` · `Ai_Mon_Special_AmbushSpawner_Projectile` · `At_Mon_Special_BossLightElemental_Summon` · [BossMonster](/api/Global.BossMonster) · [EntityAI](/api/Global.EntityAI) · [FlavourManager](/api/Global.FlavourManager) · [GameManager](/api/Global.GameManager) · [GameMod_Limbo](/api/Global.GameMod_Limbo) · `Gem_E_Predation` · `Mon_DarkCave_BossSeeker` · `Mon_DarkCave_CaveBat` · `Mon_DarkCave_CaveSpider` · `Mon_DarkCave_DarkElemental` · `Mon_DarkCave_NightOlm` · `Mon_DarkCave_Oppressor` · `Mon_DarkCave_SeekerHallucination` · `Mon_Despair_AzurakMonsterSpawner` · `Mon_Despair_AzurakRoarPillar` · `Mon_Despair_AzurakRollPillar` · `Mon_Despair_BossAzurak` · `Mon_Despair_Displacer` · `Mon_Despair_DreadBug` · `Mon_Despair_ParalyticFly` · `Mon_Despair_UnstableRat` · `Mon_Despair_WretchedArtillery` · [Mon_DreamTeller](/api/Global.Mon_DreamTeller) · `Mon_Forest_BossDemon` · `Mon_Forest_Hound` · `Mon_Forest_Scarab` · `Mon_Forest_SpiderSpitter` · `Mon_Forest_SpiderWarrior` · `Mon_Forest_Treant` · `Mon_GoldenLizard_ElusiveLizard` · `Mon_Ink_Archer` · `Mon_Ink_BossDarkMoon` · `Mon_Ink_BossDarkMoonHallucination` · `Mon_Ink_BossWhiteNight` · `Mon_Ink_BossWhiteNightHallucination` · `Mon_Ink_DivineAnimal` · `Mon_Ink_EgoSword` · `Mon_Ink_GhostBlade` · `Mon_Ink_GhostSpear` · `Mon_Ink_Tiger` · `Mon_LavaLand_BossInfernus` · `Mon_LavaLand_FireElemental` · `Mon_LavaLand_InfernoSpider` · `Mon_LavaLand_InfernusPillar` · `Mon_LavaLand_Magmadon` · `Mon_LavaLand_SuperheatedWolf` · `Mon_MorasDomain_NightmareBlob` · `Mon_Polaris` · `Mon_Primus_BossPrimusAeron` · [Mon_RedGiant](/api/Global.Mon_RedGiant) · [Mon_RedMan](/api/Global.Mon_RedMan) · `Mon_Sky_Baam` · `Mon_Sky_BigBaam_Base` · `Mon_Sky_BossNyx` · `Mon_Sky_LittleBaam` · `Mon_Sky_StarSeed` · `Mon_Sky_StellaMatter` · `Mon_SnowMountain_BossSkoll` · `Mon_SnowMountain_IceElemental` · `Mon_SnowMountain_LivingShards` · `Mon_SnowMountain_Scavenger` · `Mon_SnowMountain_SnowWolf` · `Mon_SnowMountain_VikingWarrior` · `Mon_Special_AmbushSpawner` · `Mon_Special_BossErebos` · `Mon_Special_BossLightElemental` · `Mon_Special_BossMaw` · `Mon_Special_BossObliviax` · `Mon_Special_BossPolaris` · `Mon_Special_BossPolaris_Monster_CursedDive_Stone` · `Mon_Special_ObliviaxHallucination` · `MonsterAbilityPrewarmConfig` · `RoomMod_EngulfedInFlame` · [RoomMonsters](/api/Global.RoomMonsters) · `Se_HunterBuff` · `Se_Mon_DarkCave_BossSeeker_TunnelVision` · `Se_Star_Mist_D_HunterDamage` · `Se_Star_Vesper_D_BossHunterAmpWithPenalty`

### Dependencies (15)

*Types and components that `Monster` references or depends upon:*

[Actor](/api/Global.Actor) · `ArrayGetOrDefaultExtensions` · [AssetRef`1](/api/Global.AssetRef`1) · [Dew](/api/Global.Dew) · [DewPlayer](/api/Global.DewPlayer) · [Entity](/api/Global.Entity) · [EntityAI](/api/Global.EntityAI) · [EntityAIContext](/api/Global.EntityAIContext) · [EntityAbility](/api/Global.EntityAbility) · [EntityStatus](/api/Global.EntityStatus) · [GameManager](/api/Global.GameManager) · [NetworkedManagerBase`1](/api/Global.NetworkedManagerBase`1) · [StatBonus](/api/Global.StatBonus) · [ZoneManager](/api/Global.ZoneManager) · `Mirror.GeneratedNetworkCode`

### Related Enums (1)

*Enumerations referenced in fields, properties, or method signatures:*

<a href="/enums#savevarflags" class="enum-link" data-tooltip="Default=0 · ApplyAfterCreation=1 · ApplyAfterFrameDelay=2">SaveVarFlags</a>

:::
