# Class: StackedStatusEffect

- **Category:** <span class="cat-dot" style="--cat-color: #ef4444" data-cat="Combat & Abilities"></span> Combat & Abilities
- **Namespace:** `Global`
- **Assembly:** `Dew.Core.dll`
- **Inheritance / Derived:** [DewNetworkBehaviour](/api/Global.DewNetworkBehaviour) → [Actor](/api/Global.Actor) → [AbilityInstance](/api/Global.AbilityInstance) → [StatusEffect](/api/Global.StatusEffect) → [ElementalStatusEffect](/api/Global.ElementalStatusEffect)

```csharp
public abstract class StackedStatusEffect : StatusEffect, ILogicUpdate, ICleanup, ICustomDestroyRoutine
```

## Fields (7)

::: details Click to expand Fields (7)

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`autoDecay`** | `[BoxGroup("Stack Settings", true, false, 0)] [ToggleGroup("Stack Settings/autoDecay", "Auto Decay")] public bool autoDecay` |  |
| **`decayAllAtOnce`** | `[BoxGroup("Stack Settings", true, false, 0)] [ToggleGroup("Stack Settings/autoDecay", "Auto Decay")] [ToggleLeft] public bool decayAllAtOnce` |  |
| **`decayCount`** | `[BoxGroup("Stack Settings", true, false, 0)] [HideIf("decayAllAtOnce", true)] [ToggleGroup("Stack Settings/autoDecay", "Auto Decay")] public int decayCount` |  |
| **`decayTime`** | `[BoxGroup("Stack Settings", true, false, 0)] [ToggleGroup("Stack Settings/autoDecay", "Auto Decay")] public float decayTime` |  |
| **`killOnZeroStack`** | `[BoxGroup("Stack Settings", true, false, 0)] public bool killOnZeroStack` |  |
| **`maxStack`** | `[BoxGroup("Stack Settings", true, false, 0)] public int maxStack` |  |
| **`resetTimerOnStackChange`** | `[BoxGroup("Stack Settings", true, false, 0)] [ToggleGroup("Stack Settings/autoDecay", "Auto Decay")] [ToggleLeft] public bool resetTimerOnStackChange` |  |

:::

## Properties (2)

::: details Click to expand Properties (2)

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`remainingDecayTime`** | `public float remainingDecayTime { get; }` |  |
| **`stack`** | `public int stack { get; }` |  |

:::

## Methods (8)

::: details `ActiveLogicUpdate(float)`

```csharp
protected override void ActiveLogicUpdate(float dt)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `dt` | `float` |  |

:::

::: details `AddStack(int)`

```csharp
public void AddStack(int value = 1)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `value` | `int` |  |

:::

::: details `OnCreate()`

```csharp
protected override void OnCreate()
```

:::

::: details `OnDestroyActor()`

```csharp
protected override void OnDestroyActor()
```

:::

::: details `OnStackChange(int, int)`

Called everywhere when stack count changes.

```csharp
protected virtual void OnStackChange(int oldStack, int newStack)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `oldStack` | `int` |  |
| `newStack` | `int` |  |

:::

::: details `RemoveStack(int)`

```csharp
public void RemoveStack(int value = 1)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `value` | `int` |  |

:::

::: details `ResetDecayTimer()`

```csharp
public void ResetDecayTimer()
```

:::

::: details `SetStack(int)`

```csharp
public void SetStack(int stack)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `stack` | `int` |  |

:::


## Architecture & Relationships

::: details Click to expand Architecture & Relationships

### Used By (35)

*Classes and systems that invoke, reference, or depend on `StackedStatusEffect`:*

[Actor](/api/Global.Actor) · `Ai_Culinary_Pickup` · `Ai_L_MentalCorruption_Projectile` · `Ai_Q_GoldenBurst` · [ElementalStatusEffect](/api/Global.ElementalStatusEffect) · `Se_Curse_EternalLoop` · `Se_D_BeautifulThreat` · `Se_D_ChargedAnguillian` · `Se_D_DoubleTap` · `Se_D_ExoticMatter` · `Se_D_IcyVeins` · `Se_D_MercyOfEl` · `Se_Elm_Cold` · `Se_Elm_Dark` · `Se_Elm_Fire` · `Se_Elm_Light` · `Se_FatalHitProtection_Interrupt` · `Se_Gem_L_Culinary_Stack` · `Se_L_MentalCorruption` · `Se_MirageSkin_Delusion` · `Se_MirageSkin_Delusion_Delusional` · `Se_Nor_MyOwnLittleNebula` · `Se_Q_Fleche` · `Se_Q_GoldenBurst_Wither` · `Se_Shrine_SmallSoul` · `Se_Star_Bismuth_D_Conquerer_Stacks` · `Se_StarlessPath_PowerOfGuidance` · `Shrine_BrokenWoodenDoll` · `Shrine_CookingPot` · `Shrine_Guidance` · `Shrine_SmallSoul` · `St_D_IcyVeins` · `St_Q_GoldenBurst` · `TempEffect` · `UI_InGame_StatusEffectIcons_Item`

### Dependencies (2)

*Types and components that `StackedStatusEffect` references or depends upon:*

[Actor](/api/Global.Actor) · [StatusEffect](/api/Global.StatusEffect)

:::
