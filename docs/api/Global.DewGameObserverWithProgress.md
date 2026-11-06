# Class: DewGameObserverWithProgress

- **Category:** <span class="cat-dot" style="--cat-color: #06b6d4" data-cat="Networking"></span> Networking
- **Namespace:** `Global`
- **Assembly:** `Dew.Core.dll`
- **Inheritance / Derived:** [DewPersistentGameObserver](/api/Global.DewPersistentGameObserver) → [DewAchievementItem](/api/Global.DewAchievementItem) → [DewReverieItem](/api/Global.DewReverieItem)

```csharp
public class DewGameObserverWithProgress : DewPersistentGameObserver
```

## Properties (1)

::: details Click to expand Properties (1)

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`hero`** | `public Hero hero { get; }` |  |

:::

## Methods (5)

::: details `AchCompleteWhen(Func&lt;bool&gt;, float)`

```csharp
protected void AchCompleteWhen(Func<bool> condition, float checkInterval = 2)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `condition` | `System.Func<TResult><bool>` |  |
| `checkInterval` | `float` |  |

:::

::: details `Complete()`

```csharp
public void Complete()
```

:::

::: details `GetCurrentProgress()`

Get current progress of this observer.

```csharp
public virtual int GetCurrentProgress()
```

**Returns:** `int`

:::

::: details `GetMaxProgress()`

Get max progress of this observer. Defaults to 1. Must return consistent value.

```csharp
public virtual int GetMaxProgress()
```

**Returns:** `int`

:::

::: details `OnComplete()`

```csharp
public virtual void OnComplete()
```

:::


## Architecture & Relationships

::: details Click to expand Architecture & Relationships

### Used By (57)

*Classes and systems that invoke, reference, or depend on `DewGameObserverWithProgress`:*

`ACH_BARE_SKIN_SUPREMACY` · `ACH_BFR_9000` · `ACH_BLACKCAT_DEJAVU` · `ACH_BURNING_LOVE` · `ACH_DOLL_OF_MANA` · `ACH_EMBRACE_MORTALITY` · `ACH_EMPRESS_OF_PAIN` · `ACH_FROM_ABYSS_TO_SUMMIT` · `ACH_FULL_MOON` · `ACH_HEAVIER_THAN_ATLAS` · `ACH_HOME_SWEET_HOME` · `ACH_ICEBERG_THE_GREAT_COMMUNICATOR` · `ACH_IN_CARNAGE_I_BLOOM` · `ACH_JUST_STAY_STILL` · `ACH_MASTER_OF_HAMMER` · `ACH_MASTER_OF_MYSTIC_ARTS` · `ACH_MIDAS_HIMSELF` · `ACH_M_M_M_MONSTER_KILL` · `ACH_NIGHT_OF_COUNTING_THE_STARS` · `ACH_NOVICE_TREASURE_HUNTER` · `ACH_ODE_TO_THE_STARS` · `ACH_ONCE_UPON_A_TIME` · `ACH_PEAK_PERFORMANCE` · `ACH_PEW_PEW_PEW` · `ACH_PRAISE_THE_SUN` · `ACH_PRAYER_FOR_THE_DREAMERS` · `ACH_PURE_IMAGINATION` · `ACH_REACTIVATED` · `ACH_REAP_WHAT_YOU_SOW` · `ACH_SHIELD_BATTERY` · `ACH_SIBLING_FIGHT` · `ACH_SNAKE_IN_THE_GRASS` · `ACH_SUPPORT_MAIN` · `ACH_SUSPICIOUSLY_WEALTHY_TRAVELER` · `ACH_TEKKAI` · `ACH_THE_CHILL_WASHES_AWAY_SINS` · `ACH_THE_CYCLE_OF_REBIRTH` · `ACH_THE_EIGHTH_TROPHY` · `ACH_THOUSAND_THUNDERS` · `ACH_THROUGH_TIME_AND_SPACE` · `ACH_WHY_YOU_BULLY_ME` · [AchievementManager](/api/Global.AchievementManager) · [DewAchievementItem](/api/Global.DewAchievementItem) · `DewConsoleCommands` · [DewProfile](/api/Global.DewProfile) · [DewReverieItem](/api/Global.DewReverieItem) · [InGameReverieManager](/api/Global.InGameReverieManager) · `Rev_AddToWishlist` · `Rev_JoinDiscord` · `Rev_PlayCoopTwice` · `Rev_PlayThreeTimes` · `Rev_PlayTwiceWithSpecificTraveler` · `Rev_PlayWithMeleeTraveler` · `Rev_PlayWithRangedTraveler` · `Rev_ReachNightSky` · `UI_DiscordBanner` · `UI_Tooltip_CollectableAchievementProgress`

### Dependencies (4)

*Types and components that `DewGameObserverWithProgress` references or depends upon:*

[DewPersistentGameObserver](/api/Global.DewPersistentGameObserver) · [DewPlayer](/api/Global.DewPlayer) · [Hero](/api/Global.Hero) · [ManagerBase`1](/api/Global.ManagerBase`1)

:::
