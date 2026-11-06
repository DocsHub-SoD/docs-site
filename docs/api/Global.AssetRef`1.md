# Struct: AssetRef&lt;T&gt;

- **Category:** <span class="cat-dot" style="--cat-color: #64748b" data-cat="Misc & Utility"></span> Misc & Utility
- **Namespace:** `Global`
- **Assembly:** `Dew.Core.dll`

```csharp
[Serializable]
public struct AssetRef<T> where T : Object
```

## Fields (5)

::: details Click to expand Fields (5)

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`guid`** | `public string guid` |  |
| **`isActor`** | `public bool isActor` |  |
| **`isMonoBehaviour`** | `public bool isMonoBehaviour` |  |
| **`typeAssemblyQualifiedName`** | `public string typeAssemblyQualifiedName` |  |
| **`typeName`** | `public string typeName` |  |

:::

## Properties (2)

::: details Click to expand Properties (2)

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`asset`** | `[JsonIgnore] public T asset { get; set; }` |  |
| **`lightAsset`** | `[JsonIgnore] public T lightAsset { get; }` |  |

:::

## Methods (5)

::: details `ClearCache()`

```csharp
public void ClearCache()
```

:::

::: details `Equals(AssetRef&lt;T&gt;)`

```csharp
public bool Equals(AssetRef<T> other)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `other` | `AssetRef<T>` |  |

**Returns:** `bool`

:::

::: details `Equals(object)`

```csharp
public override bool Equals(object obj)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `obj` | `object` |  |

**Returns:** `bool`

:::

::: details `GetHashCode()`

```csharp
public override int GetHashCode()
```

**Returns:** `int`

:::

::: details `GetType()`

```csharp
[Obsolete("Using GetType() on AssetRefs is typically a mistake", true)]
public Type GetType()
```

**Returns:** `System.Type`

:::
