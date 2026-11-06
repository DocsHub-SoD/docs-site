# Class: SafeAction&lt;T1, T2&gt;

- **Category:** <span class="cat-dot" style="--cat-color: #22c55e" data-cat="Actors & Entities"></span> Actors & Entities
- **Namespace:** `Global`
- **Assembly:** `Dew.Core.dll`

```csharp
public class SafeAction<T1, T2>
```

## Methods (4)

::: details `Add(Action&lt;T1, T2&gt;)`

```csharp
public SafeAction<T1, T2> Add(Action<T1, T2> handler)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `handler` | `System.Action<T1, T2>` |  |

**Returns:** `SafeAction<T1, T2>`

:::

::: details `Contains(Action&lt;T1, T2&gt;)`

```csharp
public bool Contains(Action<T1, T2> handler)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `handler` | `System.Action<T1, T2>` |  |

**Returns:** `bool`

:::

::: details `Invoke(T1, T2)`

```csharp
public void Invoke(T1 a, T2 b)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `a` | `T1` |  |
| `b` | `T2` |  |

:::

::: details `Remove(Action&lt;T1, T2&gt;)`

```csharp
public SafeAction<T1, T2> Remove(Action<T1, T2> handler)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `handler` | `System.Action<T1, T2>` |  |

**Returns:** `SafeAction<T1, T2>`

:::
