# Class: DewReverieItem

- **Category:** <span class="cat-dot" style="--cat-color: #eab308" data-cat="Items & Economy"></span> Items & Economy
- **Namespace:** `Global`
- **Assembly:** `Dew.Core.dll`
- **Inheritance / Derived:** [DewPersistentGameObserver](/api/Global.DewPersistentGameObserver) → [DewGameObserverWithProgress](/api/Global.DewGameObserverWithProgress) → [DewSpecialReverieItem](/api/Global.DewSpecialReverieItem)

```csharp
public abstract class DewReverieItem : DewGameObserverWithProgress, IExcludeFromPool
```

## Fields (2)

::: details Click to expand Fields (2)

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`index`** | `public int index` |  |
| **`ReverieSlotCount`** | `public const int ReverieSlotCount = 3` |  |

:::

## Properties (4)

::: details Click to expand Properties (4)

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`excludeFromPool`** | `public virtual bool excludeFromPool { get; }` |  |
| **`grantedItems`** | `public virtual string[] grantedItems { get; }` |  |
| **`grantedStardust`** | `public abstract int grantedStardust { get; }` |  |
| **`reverieListButtonText`** | `public virtual string reverieListButtonText { get; }` |  |

:::

## Methods (6)

::: details `OnComplete()`

```csharp
public override void OnComplete()
```

:::

::: details `OnReverieListButtonClick()`

```csharp
public virtual void OnReverieListButtonClick()
```

:::

::: details `OnSetupReverie()`

Called on a reverie item when the entry gets created for the very first time. You must set persistent variables needed for this reverie to function properly.

```csharp
public virtual void OnSetupReverie()
```

:::

::: details `OnStartLocalClient()`

```csharp
public override void OnStartLocalClient()
```

:::

::: details `OnStopLocalClient()`

```csharp
public override void OnStopLocalClient()
```

:::

::: details `SaveReverieStateToData(ReverieDataBase)`

```csharp
public void SaveReverieStateToData(DewProfile.ReverieDataBase data)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `data` | [`DewProfile.ReverieDataBase`](/api/Global.DewProfile) |  |

:::


## Architecture & Relationships

::: details Click to expand Architecture & Relationships

### Used By (18)

*Classes and systems that invoke, reference, or depend on `DewReverieItem`:*

[DewReverie](/api/Global.DewReverie) · [DewSpecialReverieItem](/api/Global.DewSpecialReverieItem) · [InGameReverieManager](/api/Global.InGameReverieManager) · `Rev_AddToWishlist` · `Rev_DealElementalDamage` · `Rev_EnterPureWhiteDream` · `Rev_JoinDiscord` · `Rev_KillHeroicBosses` · `Rev_KillHeroicBossesInCoop` · `Rev_KillHunters` · `Rev_KillSpecificMonster` · `Rev_PlayCoopTwice` · `Rev_PlayThreeTimes` · `Rev_PlayTwiceWithSpecificTraveler` · `Rev_PlayWithMeleeTraveler` · `Rev_PlayWithRangedTraveler` · `Rev_ReachNightSky` · `UI_Reveries_SlotBase`

### Dependencies (6)

*Types and components that `DewReverieItem` references or depends upon:*

[DewGameObserverWithProgress](/api/Global.DewGameObserverWithProgress) · [DewPersistentGameObserver](/api/Global.DewPersistentGameObserver) · [DewSave](/api/Global.DewSave) · [IExcludeFromPool](/api/Global.IExcludeFromPool) · [InGameReverieManager](/api/Global.InGameReverieManager) · [ManagerBase`1](/api/Global.ManagerBase`1)

:::
