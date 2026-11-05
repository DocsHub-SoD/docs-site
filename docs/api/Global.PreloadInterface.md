# Class: PreloadInterface

- **Namespace:** `Global`
- **Assembly:** `Dew.Core.dll`

```csharp
public class PreloadInterface
```

## Methods

### `AddAssetRef&lt;T&gt;(AssetRef&lt;T&gt;)`

```csharp
public void AddAssetRef<T>(AssetRef<T> assetRef) where T : Object
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `assetRef` | `AssetRef&lt;T&gt;` |  |
| `` | `T` |  |

### `AddFromMonsterPool(MonsterPool)`

```csharp
public void AddFromMonsterPool(MonsterPool pool)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `pool` | [MonsterPool](/api/Global.MonsterPool) |  |

### `AddGuid(string)`

```csharp
public void AddGuid(string guid)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `guid` | `string` |  |

### `AddType(string, bool)`

```csharp
public void AddType(string type, bool includeDependencies = true)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `type` | `string` |  |
| `includeDependencies` | `bool` |  |

### `KeepEverything()`

```csharp
public void KeepEverything()
```
