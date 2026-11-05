# Class: DewGameObserverWithProgress

- **Namespace:** `Global`
- **Assembly:** `Dew.Core.dll`
- **Inheritance / Derived:** [DewPersistentGameObserver](/api/Global.DewPersistentGameObserver) → [DewAchievementItem](/api/Global.DewAchievementItem) → [DewReverieItem](/api/Global.DewReverieItem)

```csharp
public class DewGameObserverWithProgress : DewPersistentGameObserver
```

## Properties

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`hero`** | `public Hero hero { get; }` |  |

## Methods

### `AchCompleteWhen(Func&lt;bool&gt;, float)`

```csharp
protected void AchCompleteWhen(Func<bool> condition, float checkInterval = 2)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `condition` | `System.Func&lt;TResult&gt;&lt;bool&gt;` |  |
| `checkInterval` | `float` |  |

### `Complete()`

```csharp
public void Complete()
```

### `GetCurrentProgress()`

Get current progress of this observer.

```csharp
public virtual int GetCurrentProgress()
```

**Returns:** `int`

### `GetMaxProgress()`

Get max progress of this observer. Defaults to 1. Must return consistent value.

```csharp
public virtual int GetMaxProgress()
```

**Returns:** `int`

### `OnComplete()`

```csharp
public virtual void OnComplete()
```
