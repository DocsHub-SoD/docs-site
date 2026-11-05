# Class: FlatTupleListWrapper&lt;T&gt;

- **Namespace:** `Global`
- **Assembly:** `Dew.Core.dll`

```csharp
public class FlatTupleListWrapper<T>
```

## Fields

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`list`** | `public IList&lt;T&gt; list` |  |

## Properties

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`Count`** | `public int Count { get; }` |  |
| **`this[int]`** | `public (T, T) this[int index] { get; }` |  |

## Methods

### `GetEnumerator()`

```csharp
public IEnumerator<(T, T)> GetEnumerator()
```

**Returns:** `System.Collections.Generic.IEnumerator&lt;T&gt;&lt;(T, T)&gt;`
