# Struct: SyncableAssetRef

- **Category:** <span class="cat-dot" style="--cat-color: #06b6d4" data-cat="Networking"></span> Networking
- **Namespace:** `Global`
- **Assembly:** `Dew.Core.dll`

```csharp
[Serializable]
public struct SyncableAssetRef
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
| **`asset`** | `[JsonIgnore] [JsonIgnore] public Object asset { get; set; }` |  |
| **`lightAsset`** | `[JsonIgnore] [JsonIgnore] public Object lightAsset { get; }` |  |

:::

## Methods (4)

::: details `ClearCache()`

```csharp
public void ClearCache()
```

:::

::: details `Equals(SyncableAssetRef)`

```csharp
public bool Equals(SyncableAssetRef other)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `other` | [`SyncableAssetRef`](/api/Global.SyncableAssetRef) |  |

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


## Architecture & Relationships

::: details Click to expand Architecture & Relationships

### Used By (5)

*Classes and systems that invoke, reference, or depend on `SyncableAssetRef`:*

[GameManager](/api/Global.GameManager) · `LucidDream_MarshOfDestiny` · `Shrine_MarshOfDestiny_SeedOfTorment` · [ZoneManager](/api/Global.ZoneManager) · `Mirror.GeneratedNetworkCode`

### Dependencies (2)

*Types and components that `SyncableAssetRef` references or depends upon:*

`AssetRefTypeResolver` · [DewResources](/api/Global.DewResources)

:::
