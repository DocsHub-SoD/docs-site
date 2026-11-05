# Class: DataProcessorGroup&lt;TData, TFrom, TTo&gt;

- **Namespace:** `Global`
- **Assembly:** `Dew.Core.dll`

```csharp
public class DataProcessorGroup<TData, TFrom, TTo> where TData : struct
```

## Properties

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`count`** | `public int count { get; }` |  |

## Methods

### `Add(DataProcessor&lt;TData, TFrom, TTo&gt;, int)`

Processors with lower priority value will be executed first.

```csharp
public void Add(DataProcessor<TData, TFrom, TTo> processor, int priority = 0)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `processor` | `DataProcessor&lt;TData, TFrom, TTo&gt;` |  |
| `priority` | `int` |  |

### `Clear()`

```csharp
public void Clear()
```

### `Process(ref TData, TFrom, TTo)`

```csharp
public void Process(ref TData data, TFrom from, TTo to)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `data` | `TData` |  |
| `from` | `TFrom` |  |
| `to` | `TTo` |  |

### `Remove(DataProcessor&lt;TData, TFrom, TTo&gt;)`

```csharp
public void Remove(DataProcessor<TData, TFrom, TTo> processor)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `processor` | `DataProcessor&lt;TData, TFrom, TTo&gt;` |  |
