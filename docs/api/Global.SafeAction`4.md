# Class: SafeAction&lt;T1, T2, T3, T4&gt;

- **Namespace:** `Global`
- **Assembly:** `Dew.Core.dll`

```csharp
public class SafeAction<T1, T2, T3, T4>
```

## Methods

### `Add(Action&lt;T1, T2, T3, T4&gt;)`

```csharp
public SafeAction<T1, T2, T3, T4> Add(Action<T1, T2, T3, T4> handler)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `handler` | `System.Action&lt;T1, T2, T3, T4&gt;&lt;T1, T2, T3, T4&gt;` |  |

**Returns:** `SafeAction&lt;T1, T2, T3, T4&gt;`

### `Contains(Action&lt;T1, T2, T3, T4&gt;)`

```csharp
public bool Contains(Action<T1, T2, T3, T4> handler)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `handler` | `System.Action&lt;T1, T2, T3, T4&gt;&lt;T1, T2, T3, T4&gt;` |  |

**Returns:** `bool`

### `Invoke(T1, T2, T3, T4)`

```csharp
public void Invoke(T1 a, T2 b, T3 c, T4 d)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `a` | `T1` |  |
| `b` | `T2` |  |
| `c` | `T3` |  |
| `d` | `T4` |  |

### `Remove(Action&lt;T1, T2, T3, T4&gt;)`

```csharp
public SafeAction<T1, T2, T3, T4> Remove(Action<T1, T2, T3, T4> handler)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `handler` | `System.Action&lt;T1, T2, T3, T4&gt;&lt;T1, T2, T3, T4&gt;` |  |

**Returns:** `SafeAction&lt;T1, T2, T3, T4&gt;`
