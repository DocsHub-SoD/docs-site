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
