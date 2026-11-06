# Class: SafeAction&lt;T1, T2, T3&gt;

- **Category:** <span class="cat-dot" style="--cat-color: #22c55e" data-cat="Actors & Entities"></span> Actors & Entities
- **Namespace:** `Global`
- **Assembly:** `Dew.Core.dll`

```csharp
public class SafeAction<T1, T2, T3>
```

## Methods

### `Add(Action<T1, T2, T3>)`

```csharp
public SafeAction<T1, T2, T3> Add(Action<T1, T2, T3> handler)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `handler` | `System.Action<T1, T2, T3>` |  |

**Returns:** `SafeAction<T1, T2, T3>`

### `Contains(Action<T1, T2, T3>)`

```csharp
public bool Contains(Action<T1, T2, T3> handler)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `handler` | `System.Action<T1, T2, T3>` |  |

**Returns:** `bool`

### `Invoke(T1, T2, T3)`

```csharp
public void Invoke(T1 a, T2 b, T3 c)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `a` | `T1` |  |
| `b` | `T2` |  |
| `c` | `T3` |  |

### `Remove(Action<T1, T2, T3>)`

```csharp
public SafeAction<T1, T2, T3> Remove(Action<T1, T2, T3> handler)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `handler` | `System.Action<T1, T2, T3>` |  |

**Returns:** `SafeAction<T1, T2, T3>`
