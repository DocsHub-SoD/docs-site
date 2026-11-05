# Struct: SyncableAssetRef

- **Namespace:** `Global`
- **Assembly:** `Dew.Core.dll`

```csharp
[Serializable]
public struct SyncableAssetRef
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
| **`asset`** | `[JsonIgnore]
public Object asset { get; set; }` |  |
| **`lightAsset`** | `[JsonIgnore]
public Object lightAsset { get; }` |  |

## Methods

### `ClearCache()`

```csharp
public void ClearCache()
```

### `Equals(SyncableAssetRef)`

```csharp
public bool Equals(SyncableAssetRef other)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `other` | [SyncableAssetRef](/api/Global.SyncableAssetRef) |  |

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
