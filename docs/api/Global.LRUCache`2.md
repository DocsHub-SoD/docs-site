# Class: LRUCache&lt;TKey, TValue&gt;

- **Category:** <span class="cat-dot" style="--cat-color: #f97316" data-cat="Data & Core Math"></span> Data & Core Math
- **Namespace:** `Global`
- **Assembly:** `Dew.Core.dll`

```csharp
public class LRUCache<TKey, TValue>
```

## Properties (1)

::: details Click to expand Properties (1)

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`Count`** | `public int Count { get; }` |  |

:::

## Methods (3)

::: details `Clear()`

```csharp
public void Clear()
```

:::

::: details `Set(TKey, TValue)`

Adds or updates a key/value pair. If added, it becomes the most recently used.
If the cache is at capacity, the least recently used item is removed.

```csharp
public void Set(TKey key, TValue value)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `key` | `TKey` |  |
| `value` | `TValue` |  |

:::

::: details `TryGet(TKey, out TValue)`

Tries to get a value from the cache. If found, it's marked as most recently used.

```csharp
public bool TryGet(TKey key, out TValue value)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `key` | `TKey` |  |
| `value` | `TValue` |  |

**Returns:** `bool`

:::


## Architecture & Relationships

::: details Click to expand Architecture & Relationships

### Used By (0)

*No incoming dependencies recorded.*

### Dependencies (0)

*No outgoing class dependencies recorded.*

:::
