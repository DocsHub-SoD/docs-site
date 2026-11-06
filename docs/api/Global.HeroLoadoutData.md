# Class: HeroLoadoutData

- **Category:** <span class="cat-dot" style="--cat-color: #22c55e" data-cat="Actors & Entities"></span> Actors & Entities
- **Namespace:** `Global`
- **Assembly:** `Dew.Core.dll`

```csharp
public class HeroLoadoutData
```

## Fields

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

## Methods

### `ContainsStar(string)`

```csharp
public bool ContainsStar(string starName)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `starName` | `string` |  |

**Returns:** `bool`

### `GetSkill(HeroSkillLocation)`

```csharp
public int GetSkill(HeroSkillLocation type)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `type` | [`HeroSkillLocation`](/api/Global.HeroSkillLocation) |  |

**Returns:** `int`

### `GetStarList(StarType)`

```csharp
public List<LoadoutStarItem> GetStarList(StarType type)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `type` | [`StarType`](/api/Global.StarType) |  |

**Returns:** `System.Collections.Generic.List<T><LoadoutStarItem>`

### `IsValidFor(string)`

```csharp
public bool IsValidFor(string heroType)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `heroType` | `string` |  |

**Returns:** `bool`

### `PopulateLevelsByLocalSaveData()`

```csharp
public void PopulateLevelsByLocalSaveData()
```

### `SetSkill(HeroSkillLocation, int)`

```csharp
public void SetSkill(HeroSkillLocation type, int value)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `type` | [`HeroSkillLocation`](/api/Global.HeroSkillLocation) |  |
| `value` | `int` |  |

### `Validate_Imp(string, bool, bool, HeroStarSlotUnlockData)`

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
