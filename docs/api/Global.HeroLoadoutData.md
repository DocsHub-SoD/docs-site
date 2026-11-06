# Class: HeroLoadoutData

- **Category:** <span class="cat-dot" style="--cat-color: #22c55e" data-cat="Actors & Entities"></span> Actors & Entities
- **Namespace:** `Global`
- **Assembly:** `Dew.Core.dll`

```csharp
public class HeroLoadoutData
```

## Fields (9)

::: details Click to expand Fields (9)

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`cDestruction`** | `public List<LoadoutStarItem> cDestruction` |  |
| **`cFlexible`** | `public List<LoadoutStarItem> cFlexible` |  |
| **`cImagination`** | `public List<LoadoutStarItem> cImagination` |  |
| **`cLife`** | `public List<LoadoutStarItem> cLife` |  |
| **`HeroLoadoutCount`** | `public const int HeroLoadoutCount = 5` |  |
| **`skillMovement`** | `public int skillMovement` |  |
| **`skillQ`** | `public int skillQ` |  |
| **`skillR`** | `public int skillR` |  |
| **`skillTrait`** | `public int skillTrait` |  |

:::

## Methods (7)

::: details `ContainsStar(string)`

```csharp
public bool ContainsStar(string starName)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `starName` | `string` |  |

**Returns:** `bool`

:::

::: details `GetSkill(HeroSkillLocation)`

```csharp
public int GetSkill(HeroSkillLocation type)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `type` | [`HeroSkillLocation`](/api/Global.HeroSkillLocation) |  |

**Returns:** `int`

:::

::: details `GetStarList(StarType)`

```csharp
public List<LoadoutStarItem> GetStarList(StarType type)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `type` | [`StarType`](/api/Global.StarType) |  |

**Returns:** `System.Collections.Generic.List<T><LoadoutStarItem>`

:::

::: details `IsValidFor(string)`

```csharp
public bool IsValidFor(string heroType)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `heroType` | `string` |  |

**Returns:** `bool`

:::

::: details `PopulateLevelsByLocalSaveData()`

```csharp
public void PopulateLevelsByLocalSaveData()
```

:::

::: details `SetSkill(HeroSkillLocation, int)`

```csharp
public void SetSkill(HeroSkillLocation type, int value)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `type` | [`HeroSkillLocation`](/api/Global.HeroSkillLocation) |  |
| `value` | `int` |  |

:::

::: details `Validate_Imp(string, bool, bool, HeroStarSlotUnlockData)`

Returns false if something is invalid.If isRepair is true, the loadout data will be repaired.If not, nothing will be changed.

```csharp
public bool Validate_Imp(string heroType, bool isRepair, bool checkStarLevels, DewProfile.HeroStarSlotUnlockData unlockedSlots)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `heroType` | `string` |  |
| `isRepair` | `bool` |  |
| `checkStarLevels` | `bool` |  |
| `unlockedSlots` | [`DewProfile.HeroStarSlotUnlockData`](/api/Global.DewProfile) |  |

**Returns:** `bool`

:::


## Architecture & Relationships

::: details Click to expand Architecture & Relationships

### Used By (19)

*Classes and systems that invoke, reference, or depend on `HeroLoadoutData`:*

[DevGameManager](/api/Global.DevGameManager) · [Dew](/api/Global.Dew) · [DewPlayer](/api/Global.DewPlayer) · [DewProfile](/api/Global.DewProfile) · [Hero](/api/Global.Hero) · [PlayGameManager](/api/Global.PlayGameManager) · [StarEffect](/api/Global.StarEffect) · `UI_Lobby_Constellations` · `UI_Lobby_Constellations_HeroConstellation_StarSlot` · `UI_Lobby_Constellations_QuickLoadoutSwitch` · `UI_Lobby_Constellations_Skills_ContextMenu` · `UI_Lobby_Constellations_Skills_Slot` · `UI_Lobby_Constellations_StarCount` · `UI_Lobby_Constellations_StarItem` · `UI_Lobby_Loadout` · `UI_Lobby_Loadout_AvailableSkills` · `UI_Lobby_Loadout_ComponentBase` · `UI_Lobby_Loadout_SkillSlot` · `Mirror.GeneratedNetworkCode`

### Dependencies (2)

*Types and components that `HeroLoadoutData` references or depends upon:*

`AssetRefExtensions` · [DewResources](/api/Global.DewResources)

### Related Enums (2)

*Enumerations referenced in fields, properties, or method signatures:*

[`HeroSkillLocation`](/enums#heroskilllocation) · [`StarType`](/enums#startype)

:::
