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


## Architecture & Relationships

::: details Click to expand Architecture & Relationships

### Used By (8)

*Classes and systems that invoke, reference, or depend on `IItem`:*

[EditSkillManager](/api/Global.EditSkillManager) · [Gem](/api/Global.Gem) · [HeroSkill](/api/Global.HeroSkill) · `IHoldableInHandExtension` · [InGameUIManager](/api/Global.InGameUIManager) · `ItemWorldModel` · `NetworkReaderWriterExtensions` · [SkillTrigger](/api/Global.SkillTrigger)

### Dependencies (4)

*Types and components that `IItem` references or depends upon:*

[DewPlayer](/api/Global.DewPlayer) · [Entity](/api/Global.Entity) · [Hero](/api/Global.Hero) · `ItemWorldModel`

### Related Enums (1)

*Enumerations referenced in fields, properties, or method signatures:*

<a href="/enums#rarity" class="enum-link" data-tooltip="Common=0 · Rare=1 · Epic=2 · Legendary=3 · Character=4 (+2 more)">Rarity</a>

:::
