# Class: FlatTupleListWrapper&lt;T&gt;

- **Category:** <span class="cat-dot" style="--cat-color: #64748b" data-cat="Misc & Utility"></span> Misc & Utility
- **Namespace:** `Global`
- **Assembly:** `Dew.Core.dll`
- **Attributes:** `[DefaultMember]`

```csharp
public class FlatTupleListWrapper<T>
```

## Fields (1)

::: details Click to expand Fields (1)

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`list`** | `public IList<T> list` |  |

:::

## Properties (2)

::: details Click to expand Properties (2)

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`Count`** | `public int Count { get; }` |  |
| **`this[int]`** | `public (T, T) this[int index] { get; }` |  |

:::

## Methods (1)

::: details `GetEnumerator()`

```csharp
public IEnumerator<(T, T)> GetEnumerator()
```

**Returns:** `System.Collections.Generic.IEnumerator<T><(T, T)>`

:::


## Architecture & Relationships

::: details Click to expand Architecture & Relationships

### Used By (1)

*Classes and systems that invoke, reference, or depend on `FlatTupleListWrapper<T>`:*

[MapData](/api/Global.MapData)

### Dependencies (0)

*No outgoing class dependencies recorded.*

:::
