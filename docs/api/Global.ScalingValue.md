# Struct: ScalingValue

- **Category:** <span class="cat-dot" style="--cat-color: #ef4444" data-cat="Combat & Abilities"></span> Combat & Abilities
- **Namespace:** `Global`
- **Assembly:** `Dew.Core.dll`

```csharp
[Serializable]
public struct ScalingValue
```

## Fields

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`addedHpFactor`** | `public float addedHpFactor` |  |
| **`adFactor`** | `public float adFactor` |  |
| **`apFactor`** | `public float apFactor` |  |
| **`armorFactor`** | `public float armorFactor` |  |
| **`baseValue`** | `public float baseValue` |  |
| **`critPercentageFactor`** | `public float critPercentageFactor` |  |
| **`GemDefaultPerLevelMultiplier`** | `public const float GemDefaultPerLevelMultiplier = 1.01` |  |
| **`leveling`** | `public LevelScaling leveling` |  |
| **`levelOverride`** | `public static int? levelOverride` |  |
| **`lvlFactor`** | `public float lvlFactor` |  |
| **`scalingMultiplier`** | `public float scalingMultiplier` |  |
| **`SkillDefaultPerLevelMultiplier`** | `public const float SkillDefaultPerLevelMultiplier = 1.25` |  |

## Properties

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`valueString`** | `[JsonProperty] public string valueString { get; set; }` |  |

## Methods

### `EditorParse(string, ref float, ref float, ref float, ref float, ref float, ref float, ref float)`

```csharp
public static void EditorParse(string input, ref float baseVal, ref float ad, ref float ap, ref float lvl, ref float arm, ref float ahp, ref float critp)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `input` | `string` |  |
| `baseVal` | `float` |  |
| `ad` | `float` |  |
| `ap` | `float` |  |
| `lvl` | `float` |  |
| `arm` | `float` |  |
| `ahp` | `float` |  |
| `critp` | `float` |  |

### `EditorToString(float, float, float, float, float, float, float)`

```csharp
public static string EditorToString(float baseVal, float ad, float ap, float lvl, float arm, float ahp, float critp)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `baseVal` | `float` |  |
| `ad` | `float` |  |
| `ap` | `float` |  |
| `lvl` | `float` |  |
| `arm` | `float` |  |
| `ahp` | `float` |  |
| `critp` | `float` |  |

**Returns:** `string`

### `GetAddedScalingMultiplierPerLevel()`

```csharp
public float GetAddedScalingMultiplierPerLevel()
```

**Returns:** `float`

### `GetScalingMultiplier(int)`

```csharp
public float GetScalingMultiplier(int level)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `level` | `int` |  |

**Returns:** `float`

### `GetValue(int, Entity)`

```csharp
public float GetValue(int level, Entity self)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `level` | `int` |  |
| `self` | [`Entity`](/api/Global.Entity) |  |

**Returns:** `float`

### `GetValue(int, float, float, float, float, float)`

```csharp
public float GetValue(int level, float attackDamage, float abilityPower, float armor, float addedHp, float critChance)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `level` | `int` |  |
| `attackDamage` | `float` |  |
| `abilityPower` | `float` |  |
| `armor` | `float` |  |
| `addedHp` | `float` |  |
| `critChance` | `float` |  |

**Returns:** `float`

### `Lerp(ScalingValue, ScalingValue, float)`

```csharp
public static ScalingValue Lerp(ScalingValue a, ScalingValue b, float t)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `a` | [`ScalingValue`](/api/Global.ScalingValue) |  |
| `b` | [`ScalingValue`](/api/Global.ScalingValue) |  |
| `t` | `float` |  |

**Returns:** `ScalingValue`

### `OnAfterDeserialize()`

```csharp
public void OnAfterDeserialize()
```

### `OnBeforeSerialize()`

```csharp
public void OnBeforeSerialize()
```

### `ToString()`

```csharp
public override string ToString()
```

**Returns:** `string`
