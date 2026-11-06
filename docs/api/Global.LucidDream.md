# Class: LucidDream

- **Category:** <span class="cat-dot" style="--cat-color: #22c55e" data-cat="Actors & Entities"></span> Actors & Entities
- **Namespace:** `Global`
- **Assembly:** `Dew.Core.dll`
- **Inheritance / Derived:** [DewNetworkBehaviour](/api/Global.DewNetworkBehaviour) → [Actor](/api/Global.Actor) → [GameEffect](/api/Global.GameEffect)

```csharp
public class LucidDream : GameEffect, ILogicUpdate, ICleanup, ICustomDestroyRoutine
```

## Fields (5)

::: details Click to expand Fields (5)

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`ChaoticColor`** | `public static readonly Color ChaoticColor` |  |
| **`EvilColor`** | `public static readonly Color EvilColor` |  |
| **`GoodColor`** | `public static readonly Color GoodColor` |  |
| **`icon`** | `[BoxGroup("Lucid Dream Settings", true, false, 0)] public Sprite icon` |  |
| **`type`** | `[BoxGroup("Lucid Dream Settings", true, false, 0)] public LucidDreamType type` |  |

:::

## Properties (2)

::: details Click to expand Properties (2)

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`color`** | `public Color color { get; }` |  |
| **`isDestroyedOnRoomChange`** | `public override bool isDestroyedOnRoomChange { get; }` |  |

:::

## Methods (1)

::: details `GetCustomInGameTooltip()`

```csharp
public virtual string GetCustomInGameTooltip()
```

**Returns:** `string`

:::


## Architecture & Relationships

::: details Click to expand Architecture & Relationships

### Used By (19)

*Classes and systems that invoke, reference, or depend on `LucidDream`:*

[Dew](/api/Global.Dew) · `LucidDream_BlandStarSoup` · `LucidDream_BonVoyage` · `LucidDream_EmbraceMortality` · `LucidDream_FalseLifeline` · `LucidDream_FishScales` · `LucidDream_GrievousWounds` · `LucidDream_HarmlessWhispers` · `LucidDream_KindArmadillo` · `LucidDream_MadLife` · `LucidDream_MarshOfDestiny` · `LucidDream_Overpopulation` · `LucidDream_PrudentJellyfish` · `LucidDream_SparklingDreamFlask` · `LucidDream_TheDarkestUrge` · `LucidDream_WILD` · `UI_Achievement_Icon` · `UI_LucidDreamIcon` · `UI_Tooltip_CollectableTargetName`

### Dependencies (1)

*Types and components that `LucidDream` references or depends upon:*

[GameEffect](/api/Global.GameEffect)

### Related Enums (1)

*Enumerations referenced in fields, properties, or method signatures:*

[`LucidDreamType`](/enums#luciddreamtype)

:::
