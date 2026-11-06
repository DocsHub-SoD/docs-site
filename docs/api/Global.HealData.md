# Struct: HealData

- **Category:** <span class="cat-dot" style="--cat-color: #ef4444" data-cat="Combat & Abilities"></span> Combat & Abilities
- **Namespace:** `Global`
- **Assembly:** `Dew.Core.dll`

```csharp
public struct HealData
```

## Properties (8)

::: details Click to expand Properties (8)

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`actor`** | `public readonly Actor actor { get; }` |  |
| **`amplificationMultiplier`** | `public readonly float amplificationMultiplier { get; }` | Heal multiplier for amplications. |
| **`canMerge`** | `public readonly bool canMerge { get; }` | Can this heal number be merged into single number |
| **`currentAmount`** | `public float currentAmount { get; }` | Amount of processed damage with current modifications. |
| **`flatModifier`** | `public readonly float flatModifier { get; }` | Flat heal modifier. This value will be added to the final heal before any other multipliers. |
| **`isCrit`** | `public readonly bool isCrit { get; }` | Should this heal show a critical hit marker? |
| **`originalAmount`** | `public readonly float originalAmount { get; }` | Original amount of heal. |
| **`reductionMultiplier`** | `public readonly float reductionMultiplier { get; }` | Heal multiplier for reductions. |

:::

## Methods (16)

::: details `AddAmount(float)`

Add a flat amount to this heal.

```csharp
public HealData AddAmount(float amount)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `amount` | `float` | The amount to add. Must be a positive number or zero. |

**Returns:** `HealData`

:::

::: details `ApplyAmplification(float)`

Amplify this heal by the value specified, stacking additively.e.g. One Amplication by 0.5 will cause 50% increase in heal.Two Amplifications by 0.5 will cause 125% increase in heal.

```csharp
public HealData ApplyAmplification(float value)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `value` | `float` | Amplification value. Must be a positive number or zero. |

**Returns:** `HealData`

:::

::: details `ApplyRawMultiplier(float)`

Apply raw multiplier to this heal's original amount.

```csharp
public HealData ApplyRawMultiplier(float multiplier)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `multiplier` | `float` |  |

**Returns:** `HealData`

:::

::: details `ApplyReduction(float)`

Reduce this heal by the value specified, stacking multiplicatively.e.g. One Reduction by 0.5 will cause 50% decrease in heal.Two Reductions by 0.5 will cause 75% decrease in heal.

```csharp
public HealData ApplyReduction(float value)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `value` | `float` | Reduction value. This value will be clamped between 0 and 1. |

**Returns:** `HealData`

:::

::: details `Dispatch(Entity, ReactionChain)`

```csharp
public void Dispatch(Entity victim, ReactionChain chain = default)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `victim` | [`Entity`](/api/Global.Entity) |  |
| `chain` | [`ReactionChain`](/api/Global.ReactionChain) |  |

:::

::: details `IsAmountModifiedBy(Actor)`

```csharp
public bool IsAmountModifiedBy(Actor actor)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `actor` | [`Actor`](/api/Global.Actor) |  |

**Returns:** `bool`

:::

::: details `IsAmountModifiedBy(Type)`

```csharp
public bool IsAmountModifiedBy(Type actorType)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `actorType` | `System.Type` |  |

**Returns:** `bool`

:::

::: details `SetActor(Actor)`

```csharp
public HealData SetActor(Actor actor)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `actor` | [`Actor`](/api/Global.Actor) |  |

**Returns:** `HealData`

:::

::: details `SetAmountModifiedBy(Actor)`

```csharp
public HealData SetAmountModifiedBy(Actor actor)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `actor` | [`Actor`](/api/Global.Actor) |  |

**Returns:** `HealData`

:::

::: details `SetAmountModifiedBy(Type)`

```csharp
public HealData SetAmountModifiedBy(Type actorType)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `actorType` | `System.Type` |  |

**Returns:** `HealData`

:::

::: details `SetAmountOrigin(FinalDamageData)`

If amount of this heal originates from other damage, you can specify it here to make it inherit its flags and isCrit.

```csharp
public HealData SetAmountOrigin(FinalDamageData damage)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `damage` | [`FinalDamageData`](/api/Global.FinalDamageData) |  |

**Returns:** `HealData`

:::

::: details `SetAmountOrigin(FinalHealData)`

If amount of this heal originates from other heal, you can specify it here to make it inherit its flags and isCrit.

```csharp
public HealData SetAmountOrigin(FinalHealData heal)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `heal` | [`FinalHealData`](/api/Global.FinalHealData) |  |

**Returns:** `HealData`

:::

::: details `SetCanMerge()`

Make this heal mergeable into one damage number in UI.

```csharp
public HealData SetCanMerge()
```

**Returns:** `HealData`

:::

::: details `SetCrit()`

Make this heal show a critical hit marker.

```csharp
public HealData SetCrit()
```

**Returns:** `HealData`

:::

::: details `SetOriginalAmount(float)`

```csharp
public HealData SetOriginalAmount(float newAmount)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `newAmount` | `float` |  |

**Returns:** `HealData`

:::

::: details `SubtractAmount(float)`

Subtract a flat amount from this heal.

```csharp
public HealData SubtractAmount(float amount)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `amount` | `float` | The amount to subtract. Must be a positive number or zero. |

**Returns:** `HealData`

:::


## Architecture & Relationships

::: details Click to expand Architecture & Relationships

### Used By (76)

*Classes and systems that invoke, reference, or depend on `HealData`:*

[AbilityInstance](/api/Global.AbilityInstance) · [Actor](/api/Global.Actor) · `Ai_C_BeamOfLight` · `Ai_C_DarkSpear` · `Ai_C_Purgatory_Heal` · `Ai_C_SparklingWaterGun` · `Ai_D_BeautifulThreat_Feather` · `Ai_D_BurningFist_Attack_Instance` · `Ai_D_ScarOfTheWind_DashAtk` · `Ai_E_MassCleanse` · `Ai_E_SliceThroat` · `Ai_Gem_E_Crimson` · `Ai_Gem_R_Ricochet` · `Ai_L_BloodStrike_Meat` · `Ai_L_SmallMoltenCore_Dragon_Atk` · `Ai_Mon_Special_BossMaw_ChainReaction_Instance` · `Ai_Mon_Special_BossMaw_Purgatory_Heal` · `Ai_Mon_Special_BossPolaris_Holy_Purgatory_HealProjectile` · `Ai_Q_MoonlightPact_Land` · `Ai_Q_Reduction_Projectile` · `Ai_R_ChainReaction` · `Ai_R_OrbOfLight_BackwardHealing` · `Ai_R_SerpentineBlessing_Projectile` · `Ai_U_BeamOfBalance_Beam` · `Ai_U_BigChomp` · `Ai_U_Hysteria_Claw` · [FinalHealData](/api/Global.FinalHealData) · `Gem_C_Guidance` · `Gem_C_Vengeance` · `Gem_E_Blossom` · `Gem_E_Clemency` · `Gem_E_Overload` · `Gem_E_Umbra` · `Gem_L_DivineFaith` · `Gem_L_Embertail` · `Gem_L_SuppressedArcanum` · `Gem_R_Blood` · `Gem_R_Glass` · `Gem_R_Purity` · `Gem_R_Snow` · [Hero](/api/Global.Hero) · `LucidDream_GrievousWounds` · `LucidDream_TheDarkestUrge` · `Se_Curse_DreamAfflictionHallucinatory` · `Se_D_TheKillingFlow` · `Se_FishScales` · `Se_Gem_Regeneration` · `Se_GenericHealOverTime` · `Se_HeroBleedingOut` · `Se_LingeringAuraOfGuidance` · `Se_MirageSkin_Delusion_Delusional` · `Se_Mon_Special_BossMaw_ShieldConversion` · `Se_Mon_Special_BossPolaris_CleansingFlame` · `Se_R_SerpentineBlessing_Buff` · `Se_RoomMod_ToxicArea_Debuff` · `Se_Star_Aurena_L_HealAmpOnLowHp` · `Se_Star_Aurena_L_HealAmpWithPenalty` · `Se_Star_Aurena_L_ShareHeal` · `Se_Star_Cetus_L_HealOnApDamage` · `Se_Star_Cetus_L_IncreaseDealtShield` · `Se_Star_Husk_D_DamageOverTimeCritWithPenalty` · `Se_Star_L_HealOnAttack` · `Se_Star_L_HealOnKill` · `Se_Star_L_MaxHealthUpHealDown` · `Se_Star_L_PotionHealAmount` · `Se_Star_L_ReceivedHealingAndShieldBonus` · `Se_Star_Nachia_L_HealAndShieldAmp` · `Se_Star_Nachia_L_SummonBonus` · `Se_StarlessPath_PowerOfGuidance` · `Se_Treasure_CrimsonElixir_AdBoost` · [SkillTrigger](/api/Global.SkillTrigger) · `St_D_CircleOfLife` · `St_D_DisintegratingClaw` · `St_L_HerosReturn` · [Summon](/api/Global.Summon) · `Treasure_SparklingElixir`

### Dependencies (6)

*Types and components that `HealData` references or depends upon:*

[Actor](/api/Global.Actor) · `ActorFlags` · [Entity](/api/Global.Entity) · [FinalDamageData](/api/Global.FinalDamageData) · [FinalHealData](/api/Global.FinalHealData) · [ReactionChain](/api/Global.ReactionChain)

:::
