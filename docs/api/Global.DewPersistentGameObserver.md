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
