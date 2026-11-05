# Class: DewPool

- **Namespace:** `Global`
- **Assembly:** `Dew.Core.dll`

```csharp
public static class DewPool
```

## Fields

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`_clearAction`** | `public static Dictionary&lt;Type, Action&lt;object&gt;&gt; _clearAction` |  |

## Methods

### `ClearEventsAndProcessors(Component)`

```csharp
public static void ClearEventsAndProcessors(Component obj)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `obj` | `UnityEngine.Component` |  |

### `GetArray&lt;T&gt;(out ArrayReturnHandle&lt;T&gt;, int)`

```csharp
public static T[] GetArray<T>(out ArrayReturnHandle<T> handle, int minSize = 128)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `handle` | `ArrayReturnHandle&lt;T&gt;` |  |
| `minSize` | `int` |  |
| `` | `T` |  |

**Returns:** `T[]`

### `GetDictionary&lt;TKey, TValue&gt;(out DictionaryReturnHandle&lt;TKey, TValue&gt;)`

Get an empty dictionary of TKey, TValue.You do not need to clear the dictionary before returning.

```csharp
public static Dictionary<TKey, TValue> GetDictionary<TKey, TValue>(out DictionaryReturnHandle<TKey, TValue> handle)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `handle` | `DictionaryReturnHandle&lt;TKey, TValue&gt;` |  |
| `` | `TKey` |  |
| `` | `TValue` |  |

**Returns:** `System.Collections.Generic.Dictionary&lt;TKey, TValue&gt;&lt;TKey, TValue&gt;`

### `GetList&lt;T&gt;(out ListReturnHandle&lt;T&gt;)`

Get an empty list of T.You do not need to clear the list before returning.

```csharp
public static List<T> GetList<T>(out ListReturnHandle<T> handle)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `handle` | `ListReturnHandle&lt;T&gt;` |  |
| `` | `T` |  |

**Returns:** `System.Collections.Generic.List&lt;T&gt;&lt;T&gt;`
