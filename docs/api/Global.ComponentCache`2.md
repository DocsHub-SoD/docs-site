# Class: ComponentCache&lt;TKey, TValue&gt;

- **Category:** <span class="cat-dot" style="--cat-color: #f97316" data-cat="Data & Core Math"></span> Data & Core Math
- **Namespace:** `Global`
- **Assembly:** `Dew.Core.dll`

```csharp
public class ComponentCache<TKey, TValue> where TKey : Object where TValue : class
```

## Methods (2)

::: details `Clear()`

```csharp
public void Clear()
```

:::

::: details `GetOrAdd(TKey, Func&lt;TValue&gt;)`

```csharp
public TValue GetOrAdd(TKey key, Func<TValue> valueFactory)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `key` | `TKey` |  |
| `valueFactory` | `System.Func<TResult><TValue>` |  |

**Returns:** `TValue`

:::


## Architecture & Relationships

::: details Click to expand Architecture & Relationships

### Used By (2)

*Classes and systems that invoke, reference, or depend on `ComponentCache<TKey, TValue>`:*

[CameraManager](/api/Global.CameraManager) · [ControlManager](/api/Global.ControlManager)

### Dependencies (0)

*No outgoing class dependencies recorded.*

:::
