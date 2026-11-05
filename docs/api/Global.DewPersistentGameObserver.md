# Class: DewPersistentGameObserver

- **Namespace:** `Global`
- **Assembly:** `Dew.Core.dll`
- **Inheritance / Derived:** [DewGameObserverWithProgress](/api/Global.DewGameObserverWithProgress)

```csharp
public class DewPersistentGameObserver
```

## Fields

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`_coroutines`** | `protected List&lt;Coroutine&gt; _coroutines` |  |

## Properties

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`name`** | `public string name { get; }` |  |

## Methods

### `AchOnDealDamage(Action&lt;EventInfoDamage&gt;)`

```csharp
protected void AchOnDealDamage(Action<EventInfoDamage> func)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `func` | [System.Action&lt;T&gt;&lt;EventInfoDamage&gt;](/api/Global.EventInfoDamage) |  |

### `AchOnDoHeal(Action&lt;EventInfoHeal&gt;)`

```csharp
protected void AchOnDoHeal(Action<EventInfoHeal> func)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `func` | [System.Action&lt;T&gt;&lt;EventInfoHeal&gt;](/api/Global.EventInfoHeal) |  |

### `AchOnGameConcluded(Action&lt;DewGameResult&gt;)`

```csharp
protected void AchOnGameConcluded(Action<DewGameResult> func)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `func` | [System.Action&lt;T&gt;&lt;DewGameResult&gt;](/api/Global.DewGameResult) |  |

### `AchOnKillLastHit(Action&lt;EventInfoKill&gt;)`

```csharp
protected void AchOnKillLastHit(Action<EventInfoKill> func)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `func` | [System.Action&lt;T&gt;&lt;EventInfoKill&gt;](/api/Global.EventInfoKill) |  |

### `AchOnKillOrAssist(Action&lt;EventInfoKill&gt;)`

```csharp
protected void AchOnKillOrAssist(Action<EventInfoKill> func)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `func` | [System.Action&lt;T&gt;&lt;EventInfoKill&gt;](/api/Global.EventInfoKill) |  |

### `AchOnTakeDamage(Action&lt;EventInfoDamage&gt;)`

```csharp
protected void AchOnTakeDamage(Action<EventInfoDamage> func)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `func` | [System.Action&lt;T&gt;&lt;EventInfoDamage&gt;](/api/Global.EventInfoDamage) |  |

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
| `obj` | [DewGameResult](/api/Global.DewGameResult) |  |

### `LoadState(Dictionary&lt;string, string&gt;)`

Load all persistent variables from the provided dictionary.

```csharp
public void LoadState(Dictionary<string, string> storage)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `storage` | `System.Collections.Generic.Dictionary&lt;TKey, TValue&gt;&lt;string,string&gt;` |  |

### `OnStartLocalClient()`

```csharp
public virtual void OnStartLocalClient()
```

### `OnStopLocalClient()`

Helper trackers are unregistered automatically, you only have to unregister custom handlers.

```csharp
public virtual void OnStopLocalClient()
```

### `SaveState(Dictionary&lt;string, string&gt;)`

Save all persistent variables to the provided dictionary.

```csharp
public void SaveState(Dictionary<string, string> storage)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `storage` | `System.Collections.Generic.Dictionary&lt;TKey, TValue&gt;&lt;string,string&gt;` |  |
