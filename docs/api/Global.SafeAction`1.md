# Class: SafeAction&lt;T&gt;

- **Category:** <span class="cat-dot" style="--cat-color: #22c55e" data-cat="Actors & Entities"></span> Actors & Entities
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

### `Add(Action<T>)`

```csharp
public SafeAction<T> Add(Action<T> handler)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `handler` | `System.Action<T>` |  |

**Returns:** `SafeAction<T>`

### `Contains(Action<T>)`

```csharp
public bool Contains(Action<T> handler)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `handler` | `System.Action<T>` |  |

**Returns:** `bool`

### `Invoke(T)`

```csharp
public void Invoke(T arg)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `arg` | `T` |  |

### `Remove(Action<T>)`

```csharp
public SafeAction<T> Remove(Action<T> handler)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `handler` | `System.Action<T>` |  |

**Returns:** `SafeAction<T>`
