# Class: GameEffect

- **Category:** <span class="cat-dot" style="--cat-color: #a855f7" data-cat="Buffs & Statuses"></span> Buffs & Statuses
- **Namespace:** `Global`
- **Assembly:** `Dew.Core.dll`
- **Attributes:** `[SaveActor]`
- **Inheritance / Derived:** [DewNetworkBehaviour](/api/Global.DewNetworkBehaviour) → [Actor](/api/Global.Actor) → [DewQuest](/api/Global.DewQuest) → [GameModifierBase](/api/Global.GameModifierBase) → [LucidDream](/api/Global.LucidDream)

```csharp
[SaveActor(true)]
public class GameEffect : Actor, ILogicUpdate, ICleanup, ICustomDestroyRoutine
```

## Fields (3)

::: details Click to expand Fields (3)

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`endEffect`** | `[BoxGroup("Effects", true, false, 0)] public GameObject endEffect` |  |
| **`loopEffect`** | `[BoxGroup("Effects", true, false, 0)] public GameObject loopEffect` |  |
| **`startEffect`** | `[BoxGroup("Effects", true, false, 0)] public GameObject startEffect` |  |

:::

## Properties (1)

::: details Click to expand Properties (1)

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`isDestroyedOnRoomChange`** | `public override bool isDestroyedOnRoomChange { get; }` |  |

:::

## Methods (3)

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

::: details `ShouldBeSavedWithRoom()`

```csharp
public override bool ShouldBeSavedWithRoom()
```

**Returns:** `bool`

:::


## Architecture & Relationships

::: details Click to expand Architecture & Relationships

### Used By (29)

*Classes and systems that invoke, reference, or depend on `GameEffect`:*

[DewQuest](/api/Global.DewQuest) · `GameMod_CorruptedChaos` · `GameMod_GoldenLizard` · [GameMod_Limbo](/api/Global.GameMod_Limbo) · [GameMod_MirageSkin](/api/Global.GameMod_MirageSkin) · `GameMod_Obliviax` · `GameMod_StarlessPath` · [GameModifierBase](/api/Global.GameModifierBase) · `Ge_CallOfTheRavenous` · `Ge_Obliviax_InterruptTravelAndKidnap` · `Ge_Shrine_Anitya` · `Ge_Shrine_PotOfGreed` · `Ge_TheConsortOfNight` · [LucidDream](/api/Global.LucidDream) · `LucidDream_BlandStarSoup` · `LucidDream_BonVoyage` · `LucidDream_EmbraceMortality` · `LucidDream_FalseLifeline` · `LucidDream_FishScales` · `LucidDream_GrievousWounds` · `LucidDream_HarmlessWhispers` · `LucidDream_KindArmadillo` · `LucidDream_MadLife` · `LucidDream_MarshOfDestiny` · `LucidDream_Overpopulation` · `LucidDream_PrudentJellyfish` · `LucidDream_SparklingDreamFlask` · `LucidDream_TheDarkestUrge` · `LucidDream_WILD`

### Dependencies (2)

*Types and components that `GameEffect` references or depends upon:*

[Actor](/api/Global.Actor) · [DewNetworkBehaviour](/api/Global.DewNetworkBehaviour)

:::
