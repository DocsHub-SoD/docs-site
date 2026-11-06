# Struct: EntityAIContext

- **Category:** <span class="cat-dot" style="--cat-color: #22c55e" data-cat="Actors & Entities"></span> Actors & Entities
- **Namespace:** `Global`
- **Assembly:** `Dew.Core.dll`

```csharp
public struct EntityAIContext
```

## Fields (1)

::: details Click to expand Fields (1)

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`targetEnemyLastKnownPosition`** | `public Vector3? targetEnemyLastKnownPosition` |  |

:::

## Properties (3)

::: details Click to expand Properties (3)

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`deltaTime`** | `public readonly float deltaTime { get; }` | Usually similar to aiInterval of this entity, but this can get longer if AI congestion control is active. |
| **`targetEnemy`** | `public readonly Entity targetEnemy { get; }` | Get this entity's primary target enemy. |
| **`targetEnemyElapsedTime`** | `public float targetEnemyElapsedTime { get; }` | Get elapsed time since this entity chose its primary target enemy. |

:::


## Architecture & Relationships

::: details Click to expand Architecture & Relationships

### Used By (62)

*Classes and systems that invoke, reference, or depend on `EntityAIContext`:*

`Ai_Mon_Primus_BossPrimusAeron_Dash` · [Entity](/api/Global.Entity) · [EntityAI](/api/Global.EntityAI) · [Hero](/api/Global.Hero) · `Mon_DarkCave_BossSeeker` · `Mon_DarkCave_CaveBat` · `Mon_DarkCave_DarkElemental` · `Mon_DarkCave_NightOlm` · `Mon_DarkCave_Oppressor` · `Mon_DarkCave_SeekerHallucination` · `Mon_Despair_BossAzurak` · `Mon_Despair_Displacer` · `Mon_Despair_DreadBug` · `Mon_Despair_ParalyticFly` · `Mon_Despair_UnstableRat` · `Mon_Despair_WretchedArtillery` · `Mon_Forest_BossDemon` · `Mon_Forest_Hound` · `Mon_Forest_Scarab` · `Mon_Forest_SpiderSpitter` · `Mon_Forest_SpiderWarrior` · `Mon_Forest_Treant` · `Mon_Ink_Archer` · `Mon_Ink_BossDarkMoon` · `Mon_Ink_BossWhiteNight` · `Mon_Ink_DivineAnimal` · `Mon_Ink_EgoSword` · `Mon_Ink_GhostBlade` · `Mon_Ink_GhostSpear` · `Mon_LavaLand_BossInfernus` · `Mon_LavaLand_FireElemental` · `Mon_LavaLand_InfernoSpider` · `Mon_LavaLand_Magmadon` · `Mon_LavaLand_SuperheatedWolf` · `Mon_Primus_BossPrimusAeron` · [Mon_RedGiant](/api/Global.Mon_RedGiant) · `Mon_Sky_Baam` · `Mon_Sky_BigBaam_Base` · `Mon_Sky_BigBaam_Rooter` · `Mon_Sky_BossNyx` · `Mon_Sky_LittleBaam` · `Mon_Sky_StarSeed` · `Mon_SnowMountain_BossSkoll` · `Mon_SnowMountain_IceElemental` · `Mon_SnowMountain_LivingShards` · `Mon_SnowMountain_Scavenger` · `Mon_SnowMountain_SnowWolf` · `Mon_SnowMountain_VikingWarrior` · `Mon_Special_BossErebos` · `Mon_Special_BossLightElemental` · `Mon_Special_BossMaw` · `Mon_Special_BossObliviax` · `Mon_Special_BossPolaris` · `Mon_Special_ObliviaxHallucination` · [Monster](/api/Global.Monster) · `PropEnt_Sky_Orca` · `Se_AutoDetectPresence` · `Se_Mon_SnowMountain_SnowWolf_SlowApproach` · `Se_MonsterSprint` · `Sum_R_AnnoyingBanner` · `Sum_R_SummonLittleBaam_Baam` · [Summon](/api/Global.Summon)

### Dependencies (1)

*Types and components that `EntityAIContext` references or depends upon:*

[Entity](/api/Global.Entity)

:::
