# Class: ComponentCache&lt;TKey, TValue&gt;

- **Category:** <span class="cat-dot" style="--cat-color: #f97316" data-cat="Data & Core Math"></span> Data & Core Math
- **Namespace:** `Global`
- **Assembly:** `Dew.Core.dll`

```csharp
public class ComponentCache<TKey, TValue> where TKey : Object where TValue : class
```

## Methods

### `Clear()`

```csharp
public void Clear()
```

### `GetOrAdd(TKey, Func<TValue>)`

```csharp
public TValue GetOrAdd(TKey key, Func<TValue> valueFactory)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `key` | `TKey` |  |
| `valueFactory` | `System.Func<TResult><TValue>` |  |

**Returns:** `TValue`
