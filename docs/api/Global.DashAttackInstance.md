# Class: DashAttackInstance

- **Category:** <span class="cat-dot" style="--cat-color: #ef4444" data-cat="Combat & Abilities"></span> Combat & Abilities
- **Namespace:** `Global`
- **Assembly:** `Dew.Core.dll`
- **Inheritance / Derived:** [DewNetworkBehaviour](/api/Global.DewNetworkBehaviour) → [Actor](/api/Global.Actor) → [AbilityInstance](/api/Global.AbilityInstance) → [DamageInstance](/api/Global.DamageInstance)

```csharp
public class DashAttackInstance : DamageInstance, ILogicUpdate, ICleanup, ICustomDestroyRoutine
```

## Fields (3)

::: details Click to expand Fields (3)

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`damageGracePeriod`** | `[Title("Dash Attack Instance", null, TitleAlignments.Left, true, true)] public float damageGracePeriod` |  |
| **`dash`** | `[InlineProperty] [HideLabel] public Dash dash` |  |
| **`isDirectionMode`** | `public bool isDirectionMode` |  |

:::

## Methods (5)

::: details `ActiveFrameUpdate()`

```csharp
protected override void ActiveFrameUpdate()
```

:::

::: details `ActiveLogicUpdate(float)`

```csharp
protected override void ActiveLogicUpdate(float dt)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `dt` | `float` |  |

:::

::: details `OnBeforeDispatchDamage(ref DamageData, Entity)`

```csharp
protected override void OnBeforeDispatchDamage(ref DamageData dmg, Entity target)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `dmg` | [`DamageData`](/api/Global.DamageData) |  |
| `target` | [`Entity`](/api/Global.Entity) |  |

:::

::: details `OnCreate()`

```csharp
protected override void OnCreate()
```

:::

::: details `OnSetupDash(DispByDestination)`

```csharp
protected virtual void OnSetupDash(DispByDestination disp)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `disp` | [`DispByDestination`](/api/Global.DispByDestination) |  |

:::


## Architecture & Relationships

::: details Click to expand Architecture & Relationships

### Used By (18)

*Classes and systems that invoke, reference, or depend on `DashAttackInstance`:*

`Ai_C_SwiftSlash` · `Ai_Mon_Despair_Displacer_Dash` · `Ai_Mon_Despair_DreadBug_Atk` · `Ai_Mon_Despair_UnstableRat_Atk` · `Ai_Mon_Forest_BossDemon_Atk` · `Ai_Mon_Forest_SpiderWarrior_Atk` · `Ai_Mon_Ink_BossDarkMoon_AltAtk_FirstAtk` · `Ai_Mon_Ink_EgoSword_Melee` · `Ai_Mon_LavaLand_InfernoSpider_Atk` · `Ai_Mon_SnowMountain_SnowWolf_Pounce` · `Ai_Mon_Special_BossMaw_Atk_First` · `Ai_Mon_Special_BossMaw_Atk_Second` · `Ai_Mon_Special_BossMaw_DarkSpear` · `Ai_Mon_Special_BossObliviax_Atk` · `Ai_Mon_Special_BossPolaris_Monster_SlashDash` · `Ai_Q_Laceration_Dash` · `Ai_R_FrozenFists_PunchDash` · `Ai_Star_Yubar_F_EI_DashNoProjectile_Dash`

### Dependencies (10)

*Types and components that `DashAttackInstance` references or depends upon:*

[AbilityInstance](/api/Global.AbilityInstance) · [Actor](/api/Global.Actor) · [CastInfo](/api/Global.CastInfo) · [DamageData](/api/Global.DamageData) · [DamageInstance](/api/Global.DamageInstance) · [Dash](/api/Global.Dash) · [DispByDestination](/api/Global.DispByDestination) · [Entity](/api/Global.Entity) · [EntityStatus](/api/Global.EntityStatus) · `QuaternionFlattenExtension`

:::
