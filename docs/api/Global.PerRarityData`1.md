# Struct: PerRarityData&lt;T&gt;

- **Category:** <span class="cat-dot" style="--cat-color: #f97316" data-cat="Data & Core Math"></span> Data & Core Math
- **Namespace:** `Global`
- **Assembly:** `Dew.Core.dll`

```csharp
[Serializable]
public struct PerRarityData<T>
```

## Fields

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`character`** | `public T character` |  |
| **`common`** | `public T common` |  |
| **`epic`** | `public T epic` |  |
| **`identity`** | `public T identity` |  |
| **`legendary`** | `public T legendary` |  |
| **`rare`** | `public T rare` |  |
| **`unique`** | `public T unique` |  |

## Methods

### `Get(Rarity)`

```csharp
public T Get(Rarity rarity)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `rarity` | [`Rarity`](/api/Global.Rarity) |  |

**Returns:** `T`

### `Set(Rarity, T)`

```csharp
public void Set(Rarity rarity, T value)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `rarity` | [`Rarity`](/api/Global.Rarity) |  |
| `value` | `T` |  |
