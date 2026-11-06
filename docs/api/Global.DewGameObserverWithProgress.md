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
