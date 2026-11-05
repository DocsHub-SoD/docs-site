# Class: SafeAction&lt;T1, T2&gt;

- **Namespace:** `Global`
- **Assembly:** `Dew.Core.dll`

```csharp
public class SafeAction<T1, T2>
```

## Methods

### `Add(Action&lt;T1, T2&gt;)`

```csharp
public SafeAction<T1, T2> Add(Action<T1, T2> handler)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `handler` | `System.Action&lt;T1, T2&gt;&lt;T1, T2&gt;` |  |

**Returns:** `SafeAction&lt;T1, T2&gt;`

### `Contains(Action&lt;T1, T2&gt;)`

```csharp
public bool Contains(Action<T1, T2> handler)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `handler` | `System.Action&lt;T1, T2&gt;&lt;T1, T2&gt;` |  |

**Returns:** `bool`

### `Invoke(T1, T2)`

```csharp
public void Invoke(T1 a, T2 b)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `a` | `T1` |  |
| `b` | `T2` |  |

### `Remove(Action&lt;T1, T2&gt;)`

```csharp
public SafeAction<T1, T2> Remove(Action<T1, T2> handler)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `handler` | `System.Action&lt;T1, T2&gt;&lt;T1, T2&gt;` |  |

**Returns:** `SafeAction&lt;T1, T2&gt;`
