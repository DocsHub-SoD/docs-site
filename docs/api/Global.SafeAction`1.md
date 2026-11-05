# Class: SafeAction&lt;T&gt;

- **Namespace:** `Global`
- **Assembly:** `Dew.Core.dll`

```csharp
public class SafeAction<T>
```

## Properties

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`Count`** | `public int Count { get; }` |  |

## Methods

### `Add(Action&lt;T&gt;)`

```csharp
public SafeAction<T> Add(Action<T> handler)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `handler` | `System.Action&lt;T&gt;&lt;T&gt;` |  |

**Returns:** `SafeAction&lt;T&gt;`

### `Contains(Action&lt;T&gt;)`

```csharp
public bool Contains(Action<T> handler)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `handler` | `System.Action&lt;T&gt;&lt;T&gt;` |  |

**Returns:** `bool`

### `Invoke(T)`

```csharp
public void Invoke(T arg)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `arg` | `T` |  |

### `Remove(Action&lt;T&gt;)`

```csharp
public SafeAction<T> Remove(Action<T> handler)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `handler` | `System.Action&lt;T&gt;&lt;T&gt;` |  |

**Returns:** `SafeAction&lt;T&gt;`
