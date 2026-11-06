# Struct: ScalingValue

- **Category:** <span class="cat-dot" style="--cat-color: #ef4444" data-cat="Combat & Abilities"></span> Combat & Abilities
- **Namespace:** `Global`
- **Assembly:** `Dew.Core.dll`

```csharp
[Serializable]
public struct ScalingValue
```

## Fields (12)

::: details Click to expand Fields (12)

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

:::

## Properties (1)

::: details Click to expand Properties (1)

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`valueString`** | `[JsonProperty] public string valueString { get; set; }` |  |

:::

## Methods (10)

::: details `EditorParse(string, ref float, ref float, ref float, ref float, ref float, ref float, ref float)`

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

:::

::: details `EditorToString(float, float, float, float, float, float, float)`

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

:::

::: details `GetAddedScalingMultiplierPerLevel()`

```csharp
public float GetAddedScalingMultiplierPerLevel()
```

**Returns:** `float`

:::

::: details `GetScalingMultiplier(int)`

```csharp
public float GetScalingMultiplier(int level)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `level` | `int` |  |

**Returns:** `float`

:::

::: details `GetValue(int, Entity)`

```csharp
public float GetValue(int level, Entity self)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `level` | `int` |  |
| `self` | [`Entity`](/api/Global.Entity) |  |

**Returns:** `float`

:::

::: details `GetValue(int, float, float, float, float, float)`

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

:::

::: details `Lerp(ScalingValue, ScalingValue, float)`

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

:::

::: details `OnAfterDeserialize()`

```csharp
public void OnAfterDeserialize()
```

:::

::: details `OnBeforeSerialize()`

```csharp
public void OnBeforeSerialize()
```

:::

::: details `ToString()`

```csharp
public override string ToString()
```

**Returns:** `string`

:::
