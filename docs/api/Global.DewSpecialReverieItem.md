# Class: DewSpecialReverieItem

- **Category:** <span class="cat-dot" style="--cat-color: #eab308" data-cat="Items & Economy"></span> Items & Economy
- **Namespace:** `Global`
- **Assembly:** `Dew.Core.dll`
- **Inheritance / Derived:** [DewPersistentGameObserver](/api/Global.DewPersistentGameObserver) → [DewGameObserverWithProgress](/api/Global.DewGameObserverWithProgress) → [DewReverieItem](/api/Global.DewReverieItem)

```csharp
public abstract class DewSpecialReverieItem : DewReverieItem, IExcludeFromPool
```

## Properties (1)

::: details Click to expand Properties (1)

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`nextReverie`** | `public virtual Type nextReverie { get; }` |  |

:::

## Methods (2)

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


## Architecture & Relationships

::: details Click to expand Architecture & Relationships

### Used By (7)

*Classes and systems that invoke, reference, or depend on `DewSpecialReverieItem`:*

[DewReverie](/api/Global.DewReverie) · `Rev_Special_2025WinterSale` · `Rev_Special_Founders` · `Rev_Special_NextFest_Mission0` · `Rev_Special_NextFest_Mission1` · `Rev_Special_NextFest_Mission2` · `Rev_Special_T1Emote`

### Dependencies (2)

*Types and components that `DewSpecialReverieItem` references or depends upon:*

[DewPersistentGameObserver](/api/Global.DewPersistentGameObserver) · [DewReverieItem](/api/Global.DewReverieItem)

:::
