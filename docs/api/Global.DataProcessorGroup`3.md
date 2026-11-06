# Class: DataProcessorGroup&lt;TData, TFrom, TTo&gt;

- **Category:** <span class="cat-dot" style="--cat-color: #f97316" data-cat="Data & Core Math"></span> Data & Core Math
- **Namespace:** `Global`
- **Assembly:** `Dew.Core.dll`

```csharp
public class DataProcessorGroup<TData, TFrom, TTo> where TData : struct
```

## Properties (1)

::: details Click to expand Properties (1)

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`count`** | `public int count { get; }` |  |

:::

## Methods (4)

::: details `Add(DataProcessor&lt;TData, TFrom, TTo&gt;, int)`

Processors with lower priority value will be executed first.

```csharp
public void Add(DataProcessor<TData, TFrom, TTo> processor, int priority = 0)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `processor` | `DataProcessor<TData, TFrom, TTo>` |  |
| `priority` | `int` |  |

:::

::: details `Clear()`

```csharp
public void Clear()
```

:::

::: details `Process(ref TData, TFrom, TTo)`

```csharp
public void Process(ref TData data, TFrom from, TTo to)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `data` | `TData` |  |
| `from` | `TFrom` |  |
| `to` | `TTo` |  |

:::

::: details `Remove(DataProcessor&lt;TData, TFrom, TTo&gt;)`

```csharp
public void Remove(DataProcessor<TData, TFrom, TTo> processor)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `processor` | `DataProcessor<TData, TFrom, TTo>` |  |

:::


## Architecture & Relationships

::: details Click to expand Architecture & Relationships

### Used By (115)

*Classes and systems that invoke, reference, or depend on `DataProcessorGroup<TData, TFrom, TTo>`:*

[AbilityTrigger](/api/Global.AbilityTrigger) · [Actor](/api/Global.Actor) · `Ai_Mon_Despair_BossAzurak_StompBlock` · [DewDifficultySettings](/api/Global.DewDifficultySettings) · [Entity](/api/Global.Entity) · [GameMod_Limbo](/api/Global.GameMod_Limbo) · [Gem](/api/Global.Gem) · `Gem_C_Confidence` · `Gem_C_Guidance` · `Gem_C_Lethality` · `Gem_C_Shatter` · `Gem_C_Sulfur` · `Gem_C_Talc` · `Gem_C_Vengeance` · `Gem_E_Apathy` · `Gem_E_Blossom` · `Gem_E_Flexibility` · `Gem_E_Inversion` · `Gem_E_Might` · `Gem_E_Omega` · `Gem_E_Overload` · `Gem_E_Predation` · `Gem_E_Twilight` · `Gem_E_Umbra` · `Gem_L_DivineFaith` · `Gem_L_Embertail` · `Gem_L_HeartOfGold` · `Gem_L_SuppressedArcanum` · `Gem_R_Abyss` · `Gem_R_Bleak` · `Gem_R_Contempt` · `Gem_R_Crucible` · `Gem_R_Glass` · `Gem_R_Lightweight` · `Gem_R_Slippery` · `Gem_R_Snow` · `Gem_U_EternalFlame` · [Hero](/api/Global.Hero) · `LucidDream_BlandStarSoup` · `LucidDream_EmbraceMortality` · `LucidDream_GrievousWounds` · `LucidDream_PrudentJellyfish` · `Mon_GoldenLizard_ElusiveLizard` · `Mon_Special_BossPolaris` · `Se_Curse_DarkUrge` · `Se_Curse_DreamAfflictionHallucinatory` · `Se_Curse_Fragility` · `Se_Curse_FragmentedBeing` · `Se_Curse_Lethargy` · `Se_Curse_SoftSkin` · `Se_DistantMemories` · `Se_E_LizardlyBlessing` · `Se_Elm_Dark` · `Se_Elm_Light` · `Se_EngulfedInFlame` · `Se_FishScales` · `Se_HeroBleedingOut` · `Se_L_PyranasFireball` · `Se_MirageSkin_Delusion_Delusional` · `Se_Mon_Ink_Boss_Rage` · `Se_Mon_Primus_BossPrimusAeron_Adaptation` · `Se_Mon_SnowMountain_VikingWarrior_DmgReducer` · `Se_Mon_Special_BossMaw_ShieldConversion` · `Se_Mon_Special_BossPolaris_Adaptation` · `Se_Mon_Special_BossPolaris_CleansingFlame` · `Se_PlayTutorialHeroProtection` · `Se_PolarisHallucination` · `Se_R_Lava_Debuff` · `Se_R_Parry_Start` · `Se_R_RepulsiveShield` · `Se_R_UnbreakableDetermination` · `Se_RoomMod_BlackRain` · `Se_RoomMod_ToxicArea_Debuff` · `Se_Star_Aurena_F_RE_AtkEffect` · `Se_Star_Aurena_L_HealAmpOnLowHp` · `Se_Star_Aurena_L_HealAmpWithPenalty` · `Se_Star_Bismuth_F_IT_SmallerRingAddDisplacement` · `Se_Star_Cetus_F_BI_FastChargeTakeDamageUp` · `Se_Star_Cetus_L_ArmorBuffOnShield` · `Se_Star_Cetus_L_FrostResistAndBuff` · `Se_Star_Cetus_L_IncreaseDealtShield` · `Se_Star_Cetus_L_MaxHpDamagePenalty` · `Se_Star_D_BossDamageAmp` · `Se_Star_D_DamageBonusOnAllElemental` · `Se_Star_D_RiftFirstCastDamageUp` · `Se_Star_D_ShieldDamageAmp` · `Se_Star_Husk_D_DamageAmpOnLowHpTarget` · `Se_Star_Husk_D_DamageOverTimeCritWithPenalty` · `Se_Star_Husk_D_DarkAttackWithPenalty` · `Se_Star_Husk_F_DE_MarkHitDodgeCDR` · `Se_Star_I_DismantleReroll` · `Se_Star_L_DamageReductionFromChilled` · `Se_Star_L_ElementalResistance` · `Se_Star_L_MaxHealthUpHealDown` · `Se_Star_L_PotionHealAmount` · `Se_Star_L_ReceivedHealingAndShieldBonus` · `Se_Star_Lacerta_F_IR_RechargeAmmoAmpBurnDamage` · `Se_Star_Mist_D_BossDamageOnHighHp` · `Se_Star_Mist_D_HunterDamage` · `Se_Star_Mist_F_LG_IncreasedCooldownReduction` · `Se_Star_Mist_F_LG_SingleTarget` · `Se_Star_Mist_L_AddedDodgeWithPenalty` · `Se_Star_Nachia_D_CanineLover` · `Se_Star_Nachia_L_HealAndShieldAmp` · `Se_Star_Nachia_L_SummonBonus` · `Se_Star_Vesper_D_BossHunterAmpWithPenalty` · `Se_Star_Vesper_L_FireResistance` · `Se_Star_Yubar_D_BonusDamageToLight` · `Se_Star_Yubar_F_EI_AutoExplosion` · `Se_StarlessPath_PowerOfGuidance` · [SkillTrigger](/api/Global.SkillTrigger) · `St_Q_GoldenBurst` · `Star_Global_DecreaseDamageFromChilled` · `Star_Global_ElementResistance` · `Star_Lacerta_HandCannon`

### Dependencies (2)

*Types and components that `DataProcessorGroup<TData, TFrom, TTo>` references or depends upon:*

[DataProcessor`3](/api/Global.DataProcessor`3) · `IPoolClearable`

:::
