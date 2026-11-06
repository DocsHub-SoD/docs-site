# Class: CastMethodDataSerialization

- **Category:** <span class="cat-dot" style="--cat-color: #ef4444" data-cat="Combat & Abilities"></span> Combat & Abilities
- **Namespace:** `Global`
- **Assembly:** `Dew.Core.dll`

```csharp
public static class CastMethodDataSerialization
```

## Methods

### `ReadWriteCastMethodData(NetworkReader)`

```csharp
public static CastMethodData ReadWriteCastMethodData(this NetworkReader reader)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `reader` | `Mirror.NetworkReader` |  |

**Returns:** `CastMethodData`

### `WriteCastMethodData(NetworkWriter, CastMethodData)`

```csharp
public static void WriteCastMethodData(this NetworkWriter writer, CastMethodData value)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `writer` | `Mirror.NetworkWriter` |  |
| `value` | [`CastMethodData`](/api/Global.CastMethodData) |  |
