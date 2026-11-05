# Class: DewReverieItem

- **Namespace:** `Global`
- **Assembly:** `Dew.Core.dll`
- **Inheritance / Derived:** [DewPersistentGameObserver](/api/Global.DewPersistentGameObserver) → [DewGameObserverWithProgress](/api/Global.DewGameObserverWithProgress) → [DewSpecialReverieItem](/api/Global.DewSpecialReverieItem)

```csharp
public abstract class DewReverieItem : DewGameObserverWithProgress, IExcludeFromPool
```

## Fields

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`index`** | `public int index` |  |
| **`ReverieSlotCount`** | `public const int ReverieSlotCount = 3` |  |

## Properties

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`excludeFromPool`** | `public virtual bool excludeFromPool { get; }` |  |
| **`grantedItems`** | `public virtual string[] grantedItems { get; }` |  |
| **`grantedStardust`** | `public abstract int grantedStardust { get; }` |  |
| **`reverieListButtonText`** | `public virtual string reverieListButtonText { get; }` |  |

## Methods

### `OnComplete()`

```csharp
public override void OnComplete()
```

### `OnReverieListButtonClick()`

```csharp
public virtual void OnReverieListButtonClick()
```

### `OnSetupReverie()`

Called on a reverie item when the entry gets created for the very first time. You must set persistent variables needed for this reverie to function properly.

```csharp
public virtual void OnSetupReverie()
```

### `OnStartLocalClient()`

```csharp
public override void OnStartLocalClient()
```

### `OnStopLocalClient()`

```csharp
public override void OnStopLocalClient()
```

### `SaveReverieStateToData(ReverieDataBase)`

```csharp
public void SaveReverieStateToData(DewProfile.ReverieDataBase data)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `data` | [DewProfile.ReverieDataBase](/api/Global.DewProfile) |  |
