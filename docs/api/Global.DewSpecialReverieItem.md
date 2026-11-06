# Class: DewSpecialReverieItem

- **Category:** <span class="cat-dot" style="--cat-color: #eab308" data-cat="Items & Economy"></span> Items & Economy
- **Namespace:** `Global`
- **Assembly:** `Dew.Core.dll`
- **Inheritance / Derived:** [DewPersistentGameObserver](/api/Global.DewPersistentGameObserver) → [DewGameObserverWithProgress](/api/Global.DewGameObserverWithProgress) → [DewReverieItem](/api/Global.DewReverieItem)

```csharp
public abstract class DewSpecialReverieItem : DewReverieItem, IExcludeFromPool
```

## Properties

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`nextReverie`** | `public virtual Type nextReverie { get; }` |  |

## Methods

### `OnStartLocalClient()`

```csharp
public override void OnStartLocalClient()
```

### `OnStopLocalClient()`

```csharp
public override void OnStopLocalClient()
```
