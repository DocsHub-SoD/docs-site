# Struct: GemLocation

- **Category:** <span class="cat-dot" style="--cat-color: #eab308" data-cat="Items & Economy"></span> Items & Economy
- **Namespace:** `Global`
- **Assembly:** `Dew.Core.dll`

```csharp
public struct GemLocation
```

## Fields (2)

::: details Click to expand Fields (2)

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`index`** | `public int index` |  |
| **`skill`** | `public HeroSkillLocation skill` |  |

:::

## Methods (3)

::: details `Equals(GemLocation)`

```csharp
public bool Equals(GemLocation other)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `other` | [`GemLocation`](/api/Global.GemLocation) |  |

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

### Used By (19)

*Classes and systems that invoke, reference, or depend on `GemLocation`:*

[AnalyticsEquipmentData](/api/Global.AnalyticsEquipmentData) · [EditSkillManager](/api/Global.EditSkillManager) · [EditSkillShrine](/api/Global.EditSkillShrine) · [Gem](/api/Global.Gem) · [HeroSkill](/api/Global.HeroSkill) · [IEditSkillDropTargetGemSlot](/api/Global.IEditSkillDropTargetGemSlot) · `Shrine_AltarOfCleansing` · `Shrine_Ascension` · `Shrine_BossSoul` · `Shrine_Chaos` · `Shrine_Destiny` · `Shrine_Entanglement` · `Shrine_MawOfDoom` · `Shrine_ScaredMaw` · `Shrine_UpgradeWell` · `UI_InGame_GemSlot` · `UI_InGame_GemSlot_EditSkill` · `UI_TooltipManager` · `Mirror.GeneratedNetworkCode`

### Dependencies (0)

*No outgoing class dependencies recorded.*

### Related Enums (1)

*Enumerations referenced in fields, properties, or method signatures:*

<a href="/enums#heroskilllocation" class="enum-link" data-tooltip="Q=0 · W=1 · E=2 · R=3 · Identity=4 (+1 more)">HeroSkillLocation</a>

:::
