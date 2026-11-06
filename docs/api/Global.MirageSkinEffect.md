# Class: MirageSkinEffect

- **Category:** <span class="cat-dot" style="--cat-color: #ef4444" data-cat="Combat & Abilities"></span> Combat & Abilities
- **Namespace:** `Global`
- **Assembly:** `Dew.Core.dll`
- **Inheritance / Derived:** [DewNetworkBehaviour](/api/Global.DewNetworkBehaviour) → [Actor](/api/Global.Actor) → [AbilityInstance](/api/Global.AbilityInstance) → [StatusEffect](/api/Global.StatusEffect)

```csharp
public class MirageSkinEffect : StatusEffect, ILogicUpdate, ICleanup, ICustomDestroyRoutine, IOtherPlayersTonedDownDisable
```

## Fields (13)

::: details Click to expand Fields (13)

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`allowWhenChanneling`** | `[BoxGroup("Mirage Skin Settings", true, false, 0)] [ShowIf("enableSpecialAttack", true)] public bool allowWhenChanneling` |  |
| **`breakStunDuration`** | `[BoxGroup("Mirage Skin Settings", true, false, 0)] public float breakStunDuration` |  |
| **`customAmount`** | `[NonSerialized] public float? customAmount` |  |
| **`enableSpecialAttack`** | `[BoxGroup("Mirage Skin Settings", true, false, 0)] public bool enableSpecialAttack` |  |
| **`fxBreak`** | `[BoxGroup("Mirage Skin Settings", true, false, 0)] public GameObject fxBreak` |  |
| **`fxDamage`** | `[BoxGroup("Mirage Skin Settings", true, false, 0)] public GameObject fxDamage` |  |
| **`fxDamagedCooldown`** | `[BoxGroup("Mirage Skin Settings", true, false, 0)] public float fxDamagedCooldown` |  |
| **`fxDamageOverTime`** | `[BoxGroup("Mirage Skin Settings", true, false, 0)] public GameObject fxDamageOverTime` |  |
| **`maxHealthRatio`** | `[BoxGroup("Mirage Skin Settings", true, false, 0)] public float maxHealthRatio` |  |
| **`nextSpecialAttackTime`** | `[NonSerialized] public float nextSpecialAttackTime` |  |
| **`shieldMaxHealthRatio`** | `[BoxGroup("Mirage Skin Settings", true, false, 0)] public float shieldMaxHealthRatio` |  |
| **`specialAttackInterval`** | `[BoxGroup("Mirage Skin Settings", true, false, 0)] [ShowIf("enableSpecialAttack", true)] public Vector2 specialAttackInterval` |  |
| **`tier`** | `[BoxGroup("Mirage Skin Settings", true, false, 0)] public int tier` |  |

:::

## Methods (5)

::: details `ActiveLogicUpdate(float)`

```csharp
protected override void ActiveLogicUpdate(float dt)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `dt` | `float` |  |

:::

::: details `OnCreate()`

```csharp
protected override void OnCreate()
```

:::

::: details `OnDealDamage(EventInfoDamage)`

```csharp
public virtual void OnDealDamage(EventInfoDamage obj)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `obj` | [`EventInfoDamage`](/api/Global.EventInfoDamage) |  |

:::

::: details `OnDestroyActor()`

```csharp
protected override void OnDestroyActor()
```

:::

::: details `OnSpecialAttack()`

```csharp
public virtual void OnSpecialAttack()
```

:::


## Architecture & Relationships

::: details Click to expand Architecture & Relationships

### Used By (6)

*Classes and systems that invoke, reference, or depend on `MirageSkinEffect`:*

`Se_MirageSkin_Armor` · `Se_MirageSkin_Delusion` · `Se_MirageSkin_Oblivion` · `Se_MirageSkin_Oppression` · `Se_MirageSkin_Pulverization` · `Se_MirageSkin_Sanctification`

### Dependencies (9)

*Types and components that `MirageSkinEffect` references or depends upon:*

[DewMath](/api/Global.DewMath) · [Entity](/api/Global.Entity) · [EntityStatus](/api/Global.EntityStatus) · [EntityVisual](/api/Global.EntityVisual) · [EventInfoDamage](/api/Global.EventInfoDamage) · [IOtherPlayersTonedDownDisable](/api/Global.IOtherPlayersTonedDownDisable) · [SafeAction`1](/api/Global.SafeAction`1) · [StatBonus](/api/Global.StatBonus) · [StatusEffect](/api/Global.StatusEffect)

:::
