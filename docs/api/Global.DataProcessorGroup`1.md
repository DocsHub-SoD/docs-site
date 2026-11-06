# Class: DataProcessorGroup&lt;T&gt;

- **Category:** <span class="cat-dot" style="--cat-color: #f97316" data-cat="Data & Core Math"></span> Data & Core Math
- **Namespace:** `Global`
- **Assembly:** `Dew.Core.dll`

```csharp
public class DataProcessorGroup<T> where T : struct
```

## Properties (1)

::: details Click to expand Properties (1)

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`count`** | `public int count { get; }` |  |

:::

## Methods (4)

::: details `Add(DataProcessor&lt;T&gt;, int)`

Processors with lower priority value will be executed first.

```csharp
public void Add(DataProcessor<T> processor, int priority = 0)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `processor` | `DataProcessor<T>` |  |
| `priority` | `int` |  |

:::

::: details `Clear()`

```csharp
public void Clear()
```

:::

::: details `Process(ref T)`

```csharp
public void Process(ref T data)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `data` | `T` |  |

:::

::: details `Remove(DataProcessor&lt;T&gt;)`

```csharp
public void Remove(DataProcessor<T> processor)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `processor` | `DataProcessor<T>` |  |

:::
