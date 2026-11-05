# Class: DataProcessorGroup&lt;T&gt;

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

### `Add(DataProcessor&lt;T&gt;, int)`

Processors with lower priority value will be executed first.

```csharp
public void Add(DataProcessor<T> processor, int priority = 0)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `processor` | `DataProcessor&lt;T&gt;` |  |
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

### `Remove(DataProcessor&lt;T&gt;)`

```csharp
public void Remove(DataProcessor<T> processor)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `processor` | `DataProcessor&lt;T&gt;` |  |
