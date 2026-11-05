# Interface: IItem

- **Namespace:** `Global`
- **Assembly:** `Dew.Core.dll`

```csharp
public interface IItem
```

## Properties

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`handOwner`** | `Hero handOwner { get; set; }` |  |
| **`isLocked`** | `bool isLocked { get; }` |  |
| **`owner`** | `Entity owner { get; set; }` |  |
| **`rarity`** | `Rarity rarity { get; }` |  |
| **`skipStartAnimation`** | `bool skipStartAnimation { get; }` |  |
| **`tempOwner`** | `DewPlayer tempOwner { get; set; }` |  |
| **`worldModel`** | `ItemWorldModel worldModel { get; }` |  |

## Methods

### `IsLockedFor(DewPlayer)`

```csharp
bool IsLockedFor(DewPlayer player)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `player` | [DewPlayer](/api/Global.DewPlayer) |  |

**Returns:** `bool`
