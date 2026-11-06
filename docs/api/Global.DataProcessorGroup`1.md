# Class: DataProcessorGroup&lt;T&gt;

- **Category:** <span class="cat-dot" style="--cat-color: #f97316" data-cat="Data & Core Math"></span> Data & Core Math
- **Namespace:** `Global`
- **Assembly:** `Dew.Core.dll`

```csharp
public class DataProcessorGroup<T> where T : struct
```

## Properties

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`count`** | `public int count { get; }` |  |

## Methods

### `Add(DataProcessor<T>, int)`

Processors with lower priority value will be executed first.

```csharp
public void Add(DataProcessor<T> processor, int priority = 0)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `processor` | `DataProcessor<T>` |  |
| `priority` | `int` |  |

### `Clear()`

```csharp
public void Clear()
```

### `Process(ref T)`

```csharp
public void Process(ref T data)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `data` | `T` |  |

### `Remove(DataProcessor<T>)`

```csharp
public void Remove(DataProcessor<T> processor)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `processor` | `DataProcessor<T>` |  |
