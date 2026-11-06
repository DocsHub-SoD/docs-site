# Class: PreloadInterface

- **Category:** <span class="cat-dot" style="--cat-color: #64748b" data-cat="Misc & Utility"></span> Misc & Utility
- **Namespace:** `Global`
- **Assembly:** `Dew.Core.dll`

```csharp
public class PreloadInterface
```

## Methods (5)

::: details `AddAssetRef&lt;T&gt;(AssetRef&lt;T&gt;)`

```csharp
public void AddAssetRef<T>(AssetRef<T> assetRef) where T : Object
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `assetRef` | `AssetRef<T>` |  |
| `` | `T` |  |

:::

::: details `AddFromMonsterPool(MonsterPool)`

```csharp
public void AddFromMonsterPool(MonsterPool pool)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `pool` | [`MonsterPool`](/api/Global.MonsterPool) |  |

:::

::: details `AddGuid(string)`

```csharp
public void AddGuid(string guid)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `guid` | `string` |  |

:::

::: details `AddType(string, bool)`

```csharp
public void AddType(string type, bool includeDependencies = true)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `type` | `string` |  |
| `includeDependencies` | `bool` |  |

:::

::: details `KeepEverything()`

```csharp
public void KeepEverything()
```

:::


## Architecture & Relationships

::: details Click to expand Architecture & Relationships

### Used By (1)

*Classes and systems that invoke, reference, or depend on `PreloadInterface`:*

[DewResources](/api/Global.DewResources)

### Dependencies (4)

*Types and components that `PreloadInterface` references or depends upon:*

[AssetRef`1](/api/Global.AssetRef`1) · [DewResources](/api/Global.DewResources) · [ListReturnHandle`1](/api/Global.ListReturnHandle`1) · [MonsterPool](/api/Global.MonsterPool)

:::
