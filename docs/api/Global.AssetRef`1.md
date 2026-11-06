# Struct: AssetRef&lt;T&gt;

- **Category:** <span class="cat-dot" style="--cat-color: #64748b" data-cat="Misc & Utility"></span> Misc & Utility
- **Namespace:** `Global`
- **Assembly:** `Dew.Core.dll`

```csharp
[Serializable]
public struct AssetRef<T> where T : Object
```

## Fields

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`guid`** | `public string guid` |  |
| **`isActor`** | `public bool isActor` |  |
| **`isMonoBehaviour`** | `public bool isMonoBehaviour` |  |
| **`typeAssemblyQualifiedName`** | `public string typeAssemblyQualifiedName` |  |
| **`typeName`** | `public string typeName` |  |

## Properties

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`asset`** | `[JsonIgnore] public T asset { get; set; }` |  |
| **`lightAsset`** | `[JsonIgnore] public T lightAsset { get; }` |  |

## Methods

### `ClearCache()`

```csharp
public void ClearCache()
```

### `Equals(AssetRef<T>)`

```csharp
public bool Equals(AssetRef<T> other)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `other` | `AssetRef<T>` |  |

**Returns:** `bool`

### `Equals(object)`

```csharp
public override bool Equals(object obj)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `obj` | `object` |  |

**Returns:** `bool`

### `GetHashCode()`

```csharp
public override int GetHashCode()
```

**Returns:** `int`

### `GetType()`

```csharp
[Obsolete("Using GetType() on AssetRefs is typically a mistake", true)]
public Type GetType()
```

**Returns:** `System.Type`
