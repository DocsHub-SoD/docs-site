# Class: DewPersistentGameObserver

- **Category:** <span class="cat-dot" style="--cat-color: #ef4444" data-cat="Combat & Abilities"></span> Combat & Abilities
- **Namespace:** `Global`
- **Assembly:** `Dew.Core.dll`
- **Inheritance / Derived:** [DewGameObserverWithProgress](/api/Global.DewGameObserverWithProgress)

```csharp
public class DewPersistentGameObserver
```

## Fields

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`_coroutines`** | `protected List<Coroutine> _coroutines` |  |

## Properties

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`name`** | `public string name { get; }` |  |

## Methods

### `AchOnDealDamage(Action<EventInfoDamage>)`

```csharp
protected void AchOnDealDamage(Action<EventInfoDamage> func)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `func` | [`System.Action<T><EventInfoDamage>`](/api/Global.EventInfoDamage) |  |

### `AchOnDoHeal(Action<EventInfoHeal>)`

```csharp
protected void AchOnDoHeal(Action<EventInfoHeal> func)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `func` | [`System.Action<T><EventInfoHeal>`](/api/Global.EventInfoHeal) |  |

### `AchOnGameConcluded(Action<DewGameResult>)`

```csharp
protected void AchOnGameConcluded(Action<DewGameResult> func)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `func` | [`System.Action<T><DewGameResult>`](/api/Global.DewGameResult) |  |

### `AchOnKillLastHit(Action<EventInfoKill>)`

```csharp
protected void AchOnKillLastHit(Action<EventInfoKill> func)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `func` | [`System.Action<T><EventInfoKill>`](/api/Global.EventInfoKill) |  |

### `AchOnKillOrAssist(Action<EventInfoKill>)`

```csharp
protected void AchOnKillOrAssist(Action<EventInfoKill> func)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `func` | [`System.Action<T><EventInfoKill>`](/api/Global.EventInfoKill) |  |

### `AchOnTakeDamage(Action<EventInfoDamage>)`

```csharp
protected void AchOnTakeDamage(Action<EventInfoDamage> func)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `func` | [`System.Action<T><EventInfoDamage>`](/api/Global.EventInfoDamage) |  |

### `AchSetInterval(Action, float)`

```csharp
protected void AchSetInterval(Action func, float interval)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `func` | `System.Action` |  |
| `interval` | `float` |  |

### `AchStartCoroutine(IEnumerator)`

```csharp
protected void AchStartCoroutine(IEnumerator routine)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `routine` | `System.Collections.IEnumerator` |  |

### `AchStopAllCoroutines()`

```csharp
protected void AchStopAllCoroutines()
```

### `FeedGameResult(DewGameResult)`

This needs to be called when the game ends by appropriate observer managers, e.g. AchievementManager, InGameReverieManager

```csharp
public void FeedGameResult(DewGameResult obj)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `obj` | [`DewGameResult`](/api/Global.DewGameResult) |  |

### `LoadState(Dictionary<string, string>)`

Load all persistent variables from the provided dictionary.

```csharp
public void LoadState(Dictionary<string, string> storage)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `storage` | `System.Collections.Generic.Dictionary<TKey, TValue><string,string>` |  |

### `OnStartLocalClient()`

```csharp
public virtual void OnStartLocalClient()
```

### `OnStopLocalClient()`

Helper trackers are unregistered automatically, you only have to unregister custom handlers.

```csharp
public virtual void OnStopLocalClient()
```

### `SaveState(Dictionary<string, string>)`

Save all persistent variables to the provided dictionary.

```csharp
public void SaveState(Dictionary<string, string> storage)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `storage` | `System.Collections.Generic.Dictionary<TKey, TValue><string,string>` |  |
