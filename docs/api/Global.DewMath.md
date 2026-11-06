# Class: DewMath

- **Category:** <span class="cat-dot" style="--cat-color: #f97316" data-cat="Data & Core Math"></span> Data & Core Math
- **Namespace:** `Global`
- **Assembly:** `Dew.Core.dll`
- **Attributes:** `[Extension]`

```csharp
public static class DewMath
```

## Methods (4)

::: details `Lerp(Vector2, float)`

```csharp
public static float Lerp(this Vector2 vec, float t)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `vec` | `UnityEngine.Vector2` |  |
| `t` | `float` |  |

**Returns:** `float`

:::

::: details `MultiplyPercentageBonuses(float, float)`

Multiply percentage bonuses.This(50, 50) = 125. (1.5 * 1.5 = 2.25)This(100, 100) = 300. (2 * 2 = 4)This(-50, 50) = -25. (0.5 * 1.5 = 0.75)

```csharp
public static float MultiplyPercentageBonuses(float a, float b)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `a` | `float` |  |
| `b` | `float` |  |

**Returns:** `float`

:::

::: details `RandomRange(Vector2)`

```csharp
public static float RandomRange(this Vector2 vec)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `vec` | `UnityEngine.Vector2` |  |

**Returns:** `float`

:::

::: details `RandomRoundToInt(float, DewRandom)`

```csharp
public static int RandomRoundToInt(float value, DewRandom random = null)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `value` | `float` |  |
| `random` | [`DewRandom`](/api/Global.DewRandom) |  |

**Returns:** `int`

:::


## Architecture & Relationships

::: details Click to expand Architecture & Relationships

### Used By (28)

*Classes and systems that invoke, reference, or depend on `DewMath`:*

[Actor](/api/Global.Actor) · `Ai_L_CoinExplosion_Coin` · `Ai_MirageSkin_Oblivion_Orb` · `Ai_Mon_Special_BossPolaris_Monster_PizzaLightning_Instance` · [BonusStats](/api/Global.BonusStats) · `FxCanvasGroup` · [GameManager](/api/Global.GameManager) · `Gem_L_HeartOfGold` · [MirageSkinEffect](/api/Global.MirageSkinEffect) · `Mon_GoldenLizard_ElusiveLizard` · [PickupManager](/api/Global.PickupManager) · [Pickup_BaseExpOrb](/api/Global.Pickup_BaseExpOrb) · [Pickup_BaseGoldOrb](/api/Global.Pickup_BaseGoldOrb) · [Pickup_DreamDust](/api/Global.Pickup_DreamDust) · [PropEnt_Stone_DreamDust](/api/Global.PropEnt_Stone_DreamDust) · [PropEnt_Stone_Gold](/api/Global.PropEnt_Stone_Gold) · `Se_E_LizardlyBlessing` · `Se_GoldEverywhere` · `Se_PureDream` · `Se_Star_Aurena_F_CR_EarnGold` · `Se_Star_Aurena_I_BonusFromStones` · `Se_Star_I_DismantleDustToBonusGold` · `Se_Star_I_GoldPerCrit` · `Se_Star_Nachia_I_ForestKillDreamDust` · `Shrine_Disintegration` · `Shrine_DreamdustBox` · `Shrine_GoldBox` · [ZoneManager](/api/Global.ZoneManager)

### Dependencies (1)

*Types and components that `DewMath` references or depends upon:*

[DewRandom](/api/Global.DewRandom)

:::
