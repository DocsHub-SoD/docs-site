# Class: SafeAction&lt;T&gt;

- **Category:** <span class="cat-dot" style="--cat-color: #22c55e" data-cat="Actors & Entities"></span> Actors & Entities
- **Namespace:** `Global`
- **Assembly:** `Dew.Core.dll`

```csharp
public class SafeAction<T>
```

## Properties (1)

::: details Click to expand Properties (1)

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`Count`** | `public int Count { get; }` |  |

:::

## Methods (4)

::: details `Add(Action&lt;T&gt;)`

```csharp
public SafeAction<T> Add(Action<T> handler)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `handler` | `System.Action<T>` |  |

**Returns:** `SafeAction<T>`

:::

::: details `Contains(Action&lt;T&gt;)`

```csharp
public bool Contains(Action<T> handler)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `handler` | `System.Action<T>` |  |

**Returns:** `bool`

:::

::: details `Invoke(T)`

```csharp
public void Invoke(T arg)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `arg` | `T` |  |

:::

::: details `Remove(Action&lt;T&gt;)`

```csharp
public SafeAction<T> Remove(Action<T> handler)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `handler` | `System.Action<T>` |  |

**Returns:** `SafeAction<T>`

:::
