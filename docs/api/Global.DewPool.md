# Class: DewPool

- **Category:** <span class="cat-dot" style="--cat-color: #f97316" data-cat="Data & Core Math"></span> Data & Core Math
- **Namespace:** `Global`
- **Assembly:** `Dew.Core.dll`

```csharp
public static class DewPool
```

## Fields (1)

::: details Click to expand Fields (1)

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`_clearAction`** | `public static Dictionary<Type, Action<object>> _clearAction` |  |

:::

## Methods (4)

::: details `ClearEventsAndProcessors(Component)`

```csharp
public static void ClearEventsAndProcessors(Component obj)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `obj` | `UnityEngine.Component` |  |

:::

::: details `GetArray&lt;T&gt;(out ArrayReturnHandle&lt;T&gt;, int)`

```csharp
public static T[] GetArray<T>(out ArrayReturnHandle<T> handle, int minSize = 128)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `handle` | `ArrayReturnHandle<T>` |  |
| `minSize` | `int` |  |
| `` | `T` |  |

**Returns:** `T[]`

:::

::: details `GetDictionary&lt;TKey, TValue&gt;(out DictionaryReturnHandle&lt;TKey, TValue&gt;)`

Get an empty dictionary of TKey, TValue.You do not need to clear the dictionary before returning.

```csharp
public static Dictionary<TKey, TValue> GetDictionary<TKey, TValue>(out DictionaryReturnHandle<TKey, TValue> handle)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `handle` | `DictionaryReturnHandle<TKey, TValue>` |  |
| `` | `TKey` |  |
| `` | `TValue` |  |

**Returns:** `System.Collections.Generic.Dictionary<TKey, TValue>`

:::

::: details `GetList&lt;T&gt;(out ListReturnHandle&lt;T&gt;)`

Get an empty list of T.You do not need to clear the list before returning.

```csharp
public static List<T> GetList<T>(out ListReturnHandle<T> handle)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `handle` | `ListReturnHandle<T>` |  |
| `` | `T` |  |

**Returns:** `System.Collections.Generic.List<T>`

:::
