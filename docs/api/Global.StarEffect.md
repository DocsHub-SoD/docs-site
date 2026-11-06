# Class: StarEffect

- **Category:** <span class="cat-dot" style="--cat-color: #ef4444" data-cat="Combat & Abilities"></span> Combat & Abilities
- **Namespace:** `Global`
- **Assembly:** `Dew.Core.dll`
- **Inheritance / Derived:** [DewNetworkBehaviour](/api/Global.DewNetworkBehaviour) → [Actor](/api/Global.Actor) → [AbilityInstance](/api/Global.AbilityInstance) → [StatusEffect](/api/Global.StatusEffect)

```csharp
[SaveActor(true)]
public class StarEffect : StatusEffect, ILogicUpdate, ICleanup, ICustomDestroyRoutine
```

## Fields (5)

::: details Click to expand Fields (5)

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`maxStarLevel`** | `[BoxGroup("Star Settings", true, false, 0)] public int maxStarLevel` |  |
| **`price`** | `[BoxGroup("Star Settings", true, false, 0)] public int[] price` |  |
| **`requiredLevel`** | `[BoxGroup("Star Settings", true, false, 0)] [LabelText("Req. Mastery Level")] public int requiredLevel` |  |
| **`starIcon`** | `[BoxGroup("Star Settings", true, false, 0)] public Sprite starIcon` |  |
| **`type`** | `[BoxGroup("Star Settings", true, false, 0)] public StarType type` |  |

:::

## Properties (8)

::: details Click to expand Properties (8)

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`hero`** | `public Hero hero { get; }` |  |
| **`heroType`** | `public virtual Type heroType { get; }` |  |
| **`isMovementSkillType`** | `public virtual bool isMovementSkillType { get; }` |  |
| **`player`** | `public DewPlayer player { get; }` |  |
| **`skill`** | `public SkillTrigger skill { get; }` |  |
| **`skills`** | `public SkillTrigger[] skills { get; }` | This never returns null. |
| **`skillType`** | `public virtual Type skillType { get; }` |  |
| **`strength`** | `[SaveVar(SaveVarFlags.Default)] public float strength { get; set; }` | Strength of this star effect. Usually 1.0f, but can be lower if non-flexible star is slotted in different category slot. |

:::

## Methods (6)

::: details `DoSkill(Action&lt;SkillTrigger&gt;)`

Do custom action on all matching skill. You can invoke the returned action to immediately call cleanup functions to stop the effect.

```csharp
public SafeAction DoSkill(Action<SkillTrigger> callback)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `callback` | [`System.Action<T><SkillTrigger>`](/api/Global.SkillTrigger) |  |

**Returns:** `SafeAction`

:::

::: details `DoSkill(Func&lt;SkillTrigger, Action&gt;)`

Do custom action on all matching skill and do custom cleanup. You can invoke the returned action to immediately call cleanup functions to stop the effect.

```csharp
public SafeAction DoSkill(Func<SkillTrigger, Action> callback)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `callback` | [`System.Func<T, TResult><SkillTrigger,System.Action>`](/api/Global.SkillTrigger) |  |

**Returns:** `SafeAction`

:::

::: details `DoSkillBonusAll(SkillBonus)`

Note the given bonus will be cloned. You can invoke the returned action to immediately call cleanup functions to stop the effect.

```csharp
public SafeAction DoSkillBonusAll(SkillBonus bonus)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `bonus` | [`SkillBonus`](/api/Global.SkillBonus) |  |

**Returns:** `SafeAction`

:::

::: details `IsIncompatibleWith(Hero, HeroLoadoutData)`

```csharp
public bool IsIncompatibleWith(Hero h, HeroLoadoutData l)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `h` | [`Hero`](/api/Global.Hero) |  |
| `l` | [`HeroLoadoutData`](/api/Global.HeroLoadoutData) |  |

**Returns:** `bool`

:::

::: details `IsSkillRelated(SkillTrigger)`

```csharp
public bool IsSkillRelated(SkillTrigger s)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `s` | [`SkillTrigger`](/api/Global.SkillTrigger) |  |

**Returns:** `bool`

:::

::: details `IsSkillRelated(string)`

```csharp
public bool IsSkillRelated(string s)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `s` | `string` |  |

**Returns:** `bool`

:::
