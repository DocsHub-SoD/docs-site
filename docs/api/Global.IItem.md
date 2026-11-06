# Interface: IItem

- **Category:** <span class="cat-dot" style="--cat-color: #eab308" data-cat="Items & Economy"></span> Items & Economy
- **Namespace:** `Global`
- **Assembly:** `Dew.Core.dll`

```csharp
public interface IItem
```

## Properties (7)

::: details Click to expand Properties (7)

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`handOwner`** | `Hero handOwner { get; set; }` |  |
| **`isLocked`** | `bool isLocked { get; }` |  |
| **`owner`** | `Entity owner { get; set; }` |  |
| **`rarity`** | `Rarity rarity { get; }` |  |
| **`skipStartAnimation`** | `bool skipStartAnimation { get; }` |  |
| **`tempOwner`** | `DewPlayer tempOwner { get; set; }` |  |
| **`worldModel`** | `ItemWorldModel worldModel { get; }` |  |

:::

## Methods (1)

::: details `IsLockedFor(DewPlayer)`

```csharp
bool IsLockedFor(DewPlayer player)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `player` | [`DewPlayer`](/api/Global.DewPlayer) |  |

**Returns:** `bool`

:::
