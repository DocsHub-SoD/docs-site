# Class: ComponentCache&lt;TKey, TValue&gt;

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

### `GetOrAdd(TKey, Func&lt;TValue&gt;)`

```csharp
public TValue GetOrAdd(TKey key, Func<TValue> valueFactory)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `key` | `TKey` |  |
| `valueFactory` | `System.Func&lt;TResult&gt;&lt;TValue&gt;` |  |

**Returns:** `TValue`
