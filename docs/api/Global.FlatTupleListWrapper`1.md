# Class: FlatTupleListWrapper&lt;T&gt;

- **Category:** <span class="cat-dot" style="--cat-color: #64748b" data-cat="Misc & Utility"></span> Misc & Utility
- **Namespace:** `Global`
- **Assembly:** `Dew.Core.dll`

```csharp
public class FlatTupleListWrapper<T>
```

## Fields

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`list`** | `public IList<T> list` |  |

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

**Returns:** `System.Collections.Generic.IEnumerator<T><(T, T)>`
