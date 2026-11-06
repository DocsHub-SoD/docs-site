# Class: DewPersistentGameObserver

- **Category:** <span class="cat-dot" style="--cat-color: #ef4444" data-cat="Combat & Abilities"></span> Combat & Abilities
- **Namespace:** `Global`
- **Assembly:** `Dew.Core.dll`
- **Inheritance / Derived:** [DewGameObserverWithProgress](/api/Global.DewGameObserverWithProgress)

```csharp
public class DewPersistentGameObserver
```

## Fields (1)

::: details Click to expand Fields (1)

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`_coroutines`** | `protected List<Coroutine> _coroutines` |  |

:::

## Properties (1)

::: details Click to expand Properties (1)

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`name`** | `public string name { get; }` |  |

:::

## Methods (14)

::: details `AchOnDealDamage(Action&lt;EventInfoDamage&gt;)`

```csharp
protected void AchOnDealDamage(Action<EventInfoDamage> func)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `func` | [`System.Action<T><EventInfoDamage>`](/api/Global.EventInfoDamage) |  |

:::

::: details `AchOnDoHeal(Action&lt;EventInfoHeal&gt;)`

```csharp
protected void AchOnDoHeal(Action<EventInfoHeal> func)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `func` | [`System.Action<T><EventInfoHeal>`](/api/Global.EventInfoHeal) |  |

:::

::: details `AchOnGameConcluded(Action&lt;DewGameResult&gt;)`

```csharp
protected void AchOnGameConcluded(Action<DewGameResult> func)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `func` | [`System.Action<T><DewGameResult>`](/api/Global.DewGameResult) |  |

:::

::: details `AchOnKillLastHit(Action&lt;EventInfoKill&gt;)`

```csharp
protected void AchOnKillLastHit(Action<EventInfoKill> func)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `func` | [`System.Action<T><EventInfoKill>`](/api/Global.EventInfoKill) |  |

:::

::: details `AchOnKillOrAssist(Action&lt;EventInfoKill&gt;)`

```csharp
protected void AchOnKillOrAssist(Action<EventInfoKill> func)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `func` | [`System.Action<T><EventInfoKill>`](/api/Global.EventInfoKill) |  |

:::

::: details `AchOnTakeDamage(Action&lt;EventInfoDamage&gt;)`

```csharp
protected void AchOnTakeDamage(Action<EventInfoDamage> func)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `func` | [`System.Action<T><EventInfoDamage>`](/api/Global.EventInfoDamage) |  |

:::

::: details `AchSetInterval(Action, float)`

```csharp
protected void AchSetInterval(Action func, float interval)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `func` | `System.Action` |  |
| `interval` | `float` |  |

:::

::: details `AchStartCoroutine(IEnumerator)`

```csharp
protected void AchStartCoroutine(IEnumerator routine)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `routine` | `System.Collections.IEnumerator` |  |

:::

::: details `AchStopAllCoroutines()`

```csharp
protected void AchStopAllCoroutines()
```

:::

::: details `FeedGameResult(DewGameResult)`

This needs to be called when the game ends by appropriate observer managers, e.g. AchievementManager, InGameReverieManager

```csharp
public void FeedGameResult(DewGameResult obj)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `obj` | [`DewGameResult`](/api/Global.DewGameResult) |  |

:::

::: details `LoadState(Dictionary&lt;string, string&gt;)`

Load all persistent variables from the provided dictionary.

```csharp
public void LoadState(Dictionary<string, string> storage)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `storage` | `System.Collections.Generic.Dictionary<TKey, TValue><string,string>` |  |

:::

::: details `OnStartLocalClient()`

```csharp
public virtual void OnStartLocalClient()
```

:::

::: details `OnStopLocalClient()`

Helper trackers are unregistered automatically, you only have to unregister custom handlers.

```csharp
public virtual void OnStopLocalClient()
```

:::

::: details `SaveState(Dictionary&lt;string, string&gt;)`

Save all persistent variables to the provided dictionary.

```csharp
public void SaveState(Dictionary<string, string> storage)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `storage` | `System.Collections.Generic.Dictionary<TKey, TValue><string,string>` |  |

:::


## Architecture & Relationships

::: details Click to expand Architecture & Relationships

### Used By (75)

*Classes and systems that invoke, reference, or depend on `DewPersistentGameObserver`:*

`ACH_ANGER_MANAGEMENT_PROFESSIONAL` · `ACH_BALANCE_FOREVER_LOST` · `ACH_BARE_SKIN_SUPREMACY` · `ACH_CLEAR_MIND` · `ACH_DECEIVING_LOOKS` · `ACH_DESPERATE_HERO` · `ACH_DOUBLE_VISION` · `ACH_ELECTRIC_TYPE` · `ACH_ELEMENTALS_101` · `ACH_EMPTY_CANVAS` · `ACH_ETERNAL_REST` · `ACH_EVERYONE_LETS_NOT_PANIC` · `ACH_FIGHTING_COLD_WITH_COLD` · `ACH_FLEXIBLE_DIET` · `ACH_FOUR_OF_A_KIND` · `ACH_FROM_ABYSS_TO_SUMMIT` · `ACH_FULL_MOON` · `ACH_GO_WITH_THE_FLOW` · `ACH_HOME_SWEET_HOME` · `ACH_HORNS_FEATHERS_AND_GOLD` · `ACH_HOTTER_FIRE_WINS` · `ACH_HUNTERS_WHAT_HUNTERS` · `ACH_IMMORTALITY_ACHIEVED` · `ACH_I_AM_SHELL` · `ACH_JUST_LIKE_THE_OLD_DAYS` · `ACH_KING_OF_THE_ELEMENTALS` · `ACH_KYAAAAAA` · `ACH_LIKE_A_BREEZE` · `ACH_LOOK_RAINBOW` · `ACH_MASTER_OF_EVASION` · `ACH_ME_LOVE_GLOWY_STUFF` · `ACH_MINE_AND_CRAFT` · `ACH_M_M_M_MONSTER_KILL` · `ACH_NOT_EVEN_A_SCRATCH` · `ACH_NO_NEED_FOR_YOUR_HELP` · `ACH_OMEGA_POINT` · `ACH_OVERFLOWING_HEALS` · `ACH_PEACE_AMID_THE_STORM` · `ACH_PYROMANIA` · `ACH_RUN_ME_LIKE_A_RACE_HORSE` · `ACH_SHOOT_FOR_THE_MOON` · `ACH_SIBLING_FIGHT` · `ACH_TASTE_OF_THEIR_OWN_MEDICINE` · `ACH_THEYRE_JUST_BIG_CATS` · `ACH_THE_CHILL_WASHES_AWAY_SINS` · `ACH_THE_CYCLE_OF_REBIRTH` · `ACH_THE_ROAD_NOT_TAKEN` · `ACH_THE_TRUE_FOREST_SOVEREIGN` · `ACH_TRUE_SUPPORT` · `ACH_ULTRA_RAPID_FIRE` · `ACH_UNTOUCHABLE` · `ACH_VINE_IN_CREVICES` · `ACH_VIVID_DREAM` · `ACH_WHOS_THE_PREY_NOW` · `ACH_WRIST_FRIENDLY_BUILD` · [AchievementManager](/api/Global.AchievementManager) · [DewAchievementItem](/api/Global.DewAchievementItem) · `DewConsoleCommands` · [DewGameObserverWithProgress](/api/Global.DewGameObserverWithProgress) · [DewReverieItem](/api/Global.DewReverieItem) · [DewSpecialReverieItem](/api/Global.DewSpecialReverieItem) · [InGameReverieManager](/api/Global.InGameReverieManager) · `Rev_DealElementalDamage` · `Rev_EnterPureWhiteDream` · `Rev_KillHeroicBosses` · `Rev_KillHeroicBossesInCoop` · `Rev_KillHunters` · `Rev_KillSpecificMonster` · `Rev_Special_2025WinterSale` · `Rev_Special_Founders` · `Rev_Special_NextFest_Mission0` · `Rev_Special_NextFest_Mission1` · `Rev_Special_NextFest_Mission2` · `Rev_Special_T1Emote` · `UI_Reveries_SlotBase`

### Dependencies (6)

*Types and components that `DewPersistentGameObserver` references or depends upon:*

[DewGameResult](/api/Global.DewGameResult) · [DewPlayer](/api/Global.DewPlayer) · `JsonUtilityEx` · [ManagerBase`1](/api/Global.ManagerBase`1) · [NetworkedManagerBase`1](/api/Global.NetworkedManagerBase`1) · [SafeAction`1](/api/Global.SafeAction`1)

:::
