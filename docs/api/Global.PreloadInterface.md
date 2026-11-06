# Class: PreloadInterface

- **Category:** <span class="cat-dot" style="--cat-color: #64748b" data-cat="Misc & Utility"></span> Misc & Utility
- **Namespace:** `Global`
- **Assembly:** `Dew.Core.dll`

```csharp
public class PreloadInterface
```

## Methods

### `AddAssetRef<T>(AssetRef<T>)`

```csharp
public void AddAssetRef<T>(AssetRef<T> assetRef) where T : Object
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `assetRef` | `AssetRef<T>` |  |
| `` | `T` |  |

### `AddFromMonsterPool(MonsterPool)`

```csharp
public void AddFromMonsterPool(MonsterPool pool)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `pool` | [`MonsterPool`](/api/Global.MonsterPool) |  |

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
