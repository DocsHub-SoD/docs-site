# Struct: SyncedNetworkBehaviour

- **Category:** <span class="cat-dot" style="--cat-color: #06b6d4" data-cat="Networking"></span> Networking
- **Namespace:** `Global`
- **Assembly:** `Dew.Core.dll`

```csharp
public struct SyncedNetworkBehaviour
```

## Fields

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`componentIndex`** | `public byte componentIndex` |  |
| **`netId`** | `public uint netId` |  |

## Methods

### `Equals(SyncedNetworkBehaviour)`

```csharp
public bool Equals(SyncedNetworkBehaviour other)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `other` | [`SyncedNetworkBehaviour`](/api/Global.SyncedNetworkBehaviour) |  |

**Returns:** `bool`

### `Equals(uint, int)`

```csharp
public bool Equals(uint netId, int componentIndex)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `netId` | `uint` |  |
| `componentIndex` | `int` |  |

**Returns:** `bool`

### `ToString()`

```csharp
public override string ToString()
```

**Returns:** `string`
