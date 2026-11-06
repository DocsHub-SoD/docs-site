# Struct: DamageData

- **Category:** <span class="cat-dot" style="--cat-color: #ef4444" data-cat="Combat & Abilities"></span> Combat & Abilities
- **Namespace:** `Global`
- **Assembly:** `Dew.Core.dll`

```csharp
public struct DamageData
```

## Fields (2)

::: details Click to expand Fields (2)

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`elemental`** | `public ElementalType? elemental` |  |
| **`source`** | `public DamageData.SourceType source` | Source type of this damage. |

:::

## Properties (15)

::: details Click to expand Properties (15)

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`actor`** | `public readonly Actor actor { get; }` |  |
| **`amplificationMultiplier`** | `public readonly float amplificationMultiplier { get; }` | Damage multiplier for amplications. Amplications are multiplicatively combined. This value will be multiplied to the damage after flatModifier. |
| **`attackEffectStrength`** | `public readonly float attackEffectStrength { get; }` | Attack effect strength (0~1). If this value is above 0, this damage will trigger attack effects. |
| **`attackEffectType`** | `public readonly AttackEffectType attackEffectType { get; }` |  |
| **`attributes`** | `public readonly DamageAttribute attributes { get; }` |  |
| **`currentAmount`** | `public float currentAmount { get; }` | Amount of processed damage with current modifications. |
| **`damageToShieldMultiplier`** | `public readonly float damageToShieldMultiplier { get; }` |  |
| **`direction`** | `public readonly Vector3? direction { get; }` | Direction of this damage. |
| **`flatModifier`** | `public readonly float flatModifier { get; }` | Flat damage modifier. This value will be added to the final damage before any other multipliers. |
| **`isBlockedByImmunity`** | `public readonly bool isBlockedByImmunity { get; }` | Is this damage currently blocked by immunity? |
| **`originalAmount`** | `public readonly float originalAmount { get; }` | Original amount of damage. |
| **`originPosition`** | `public readonly Vector3? originPosition { get; }` | Origin position of this damage. |
| **`overrideElementalStacks`** | `public readonly int? overrideElementalStacks { get; }` |  |
| **`procCoefficient`** | `public readonly float procCoefficient { get; }` | Proc coefficient of damage. |
| **`reductionMultiplier`** | `public readonly float reductionMultiplier { get; }` | Damage multiplier for reductions. Reductions are multiplicatively combined. This value will be multiplied to the damage after flatModifier. |

:::

## Methods (25)

::: details `AddFlatAmount(float)`

Add a flat amount to this damage.

```csharp
public DamageData AddFlatAmount(float amount)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `amount` | `float` | The amount to add. Must be a positive number or zero. |

**Returns:** `DamageData`

:::

::: details `ApplyAmplification(float)`

Amplify this damage by the value specified, stacking multiplicatively.e.g. One Amplication by 0.5 will cause 50% increase in damage.Two Amplifications by 0.5 will cause 125% increase in damage.

```csharp
public DamageData ApplyAmplification(float value)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `value` | `float` | Amplification value. Must be a positive number or zero. |

**Returns:** `DamageData`

:::

::: details `ApplyDamageToShieldMultiplier(float)`

```csharp
public DamageData ApplyDamageToShieldMultiplier(float multiplier)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `multiplier` | `float` |  |

**Returns:** `DamageData`

:::

::: details `ApplyRawMultiplier(float)`

Apply raw multiplier to this damage's original amount.

```csharp
public DamageData ApplyRawMultiplier(float multiplier)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `multiplier` | `float` |  |

**Returns:** `DamageData`

:::

::: details `ApplyReduction(float)`

Reduce this damage by the value specified, stacking multiplicatively.e.g. One Reduction by 0.5 will cause 50% decrease in damage.Two Reductions by 0.5 will cause 75% decrease in damage.

```csharp
public DamageData ApplyReduction(float value)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `value` | `float` | Reduction value. This value will be clamped between 0 and 1. |

**Returns:** `DamageData`

:::

::: details `ApplyStrength(float)`

Apply the given multiplier to the damage and the proc coefficient.

```csharp
public DamageData ApplyStrength(float multiplier)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `multiplier` | `float` |  |

**Returns:** `DamageData`

:::

::: details `BlockWithImmunity()`

Block this damage with damage immunity. Note this will be ignored ifIgnoreDamageImmunityis set to true.

```csharp
public DamageData BlockWithImmunity()
```

**Returns:** `DamageData`

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

::: details `DoAttackEffect(AttackEffectType, float)`

```csharp
public DamageData DoAttackEffect(AttackEffectType type, float strength = 1)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `type` | [`AttackEffectType`](/api/Global.AttackEffectType) |  |
| `strength` | `float` |  |

**Returns:** `DamageData`

:::

::: details `HasAttr(DamageAttribute)`

Does this damage has specific attribute?

```csharp
public bool HasAttr(DamageAttribute attr)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `attr` | [`DamageAttribute`](/api/Global.DamageAttribute) |  |

**Returns:** `bool`

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
public DamageData SetActor(Actor actor)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `actor` | [`Actor`](/api/Global.Actor) |  |

**Returns:** `DamageData`

:::

::: details `SetAmountModifiedBy(Actor)`

```csharp
public DamageData SetAmountModifiedBy(Actor actor)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `actor` | [`Actor`](/api/Global.Actor) |  |

**Returns:** `DamageData`

:::

::: details `SetAmountModifiedBy(Type)`

```csharp
public DamageData SetAmountModifiedBy(Type actorType)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `actorType` | `System.Type` |  |

**Returns:** `DamageData`

:::

::: details `SetAmountOrigin(FinalDamageData)`

If amount of this damage originates from other damage, you can specify it here to make it inherit its modifier flags and attributes.

```csharp
public DamageData SetAmountOrigin(FinalDamageData damage)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `damage` | [`FinalDamageData`](/api/Global.FinalDamageData) |  |

**Returns:** `DamageData`

:::

::: details `SetAmountOrigin(FinalHealData)`

If amount of this damage originates from other heal, you can specify it here to make it inherit its modifier flags and isCrit.

```csharp
public DamageData SetAmountOrigin(FinalHealData heal)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `heal` | [`FinalHealData`](/api/Global.FinalHealData) |  |

**Returns:** `DamageData`

:::

::: details `SetAttr(DamageAttribute)`

Add special attribute for this damage.

```csharp
public DamageData SetAttr(DamageAttribute attr)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `attr` | [`DamageAttribute`](/api/Global.DamageAttribute) |  |

**Returns:** `DamageData`

:::

::: details `SetDirection(Quaternion)`

```csharp
public DamageData SetDirection(Quaternion rot)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `rot` | `UnityEngine.Quaternion` |  |

**Returns:** `DamageData`

:::

::: details `SetDirection(Vector3)`

```csharp
public DamageData SetDirection(Vector3 dir)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `dir` | `UnityEngine.Vector3` |  |

**Returns:** `DamageData`

:::

::: details `SetElemental(ElementalType?)`

```csharp
public DamageData SetElemental(ElementalType? type)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `type` | [`ElementalType?`](/api/Global.ElementalType) |  |

**Returns:** `DamageData`

:::

::: details `SetOriginPosition(Vector3)`

```csharp
public DamageData SetOriginPosition(Vector3 pos)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `pos` | `UnityEngine.Vector3` |  |

**Returns:** `DamageData`

:::

::: details `SetOverrideElementalStacks(int)`

Set this to override number of elemental stacks this damage applies.

```csharp
public DamageData SetOverrideElementalStacks(int stacks)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `stacks` | `int` |  |

**Returns:** `DamageData`

:::

::: details `SetSourceType(SourceType)`

```csharp
public DamageData SetSourceType(DamageData.SourceType type)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `type` | [`DamageData.SourceType`](/api/Global.DamageData) |  |

**Returns:** `DamageData`

:::

::: details `SubtractFlatAmount(float)`

Subtract a flat amount from this damage.

```csharp
public DamageData SubtractFlatAmount(float amount)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `amount` | `float` | The amount to subtract. Must be a positive number or zero. |

**Returns:** `DamageData`

:::


## Architecture & Relationships

::: details Click to expand Architecture & Relationships

### Used By (268)

*Classes and systems that invoke, reference, or depend on `DamageData`:*

[AbilityInstance](/api/Global.AbilityInstance) · [Actor](/api/Global.Actor) · [ActorManager](/api/Global.ActorManager) · `Ai_C_BackStep_Bomb` · `Ai_C_BeamOfLight` · `Ai_C_DarkBolt` · `Ai_C_DarkSpear` · `Ai_C_FlashFreeze` · `Ai_C_GlacialStomp` · `Ai_C_MagicSword` · `Ai_C_Pew_Projectile` · `Ai_C_PressurePoint` · `Ai_C_SparklingWaterGun` · `Ai_C_Starfall_Projectile` · `Ai_Curse_AnchorOfMind_Anchor` · `Ai_Curse_DreamAfflictionInductive_Smite` · `Ai_D_BeautifulThreat_Feather` · `Ai_D_BurningFist_Attack` · `Ai_D_ChargedAnguillian_Lightning` · `Ai_D_ExoticMatter_Projectile` · `Ai_D_IcyVeins_Damage` · `Ai_D_PrismaticEyes_Attack` · `Ai_D_QuartetOfDeath_Explosion` · `Ai_D_SalamanderPowder_Projectile` · `Ai_D_ScarOfTheWind_DashAtk` · `Ai_E_CrimsonLance` · `Ai_E_DoomsdayMeteor_SubProjectile` · `Ai_E_FinalExplosion_Explosion` · `Ai_E_FlameJet_Projectile` · `Ai_E_JusticeGuillotine` · `Ai_E_MysticDagger` · `Ai_E_SearingCharge` · `Ai_E_ShadowVolley_Projectile` · `Ai_E_SliceThroat` · `Ai_E_VileStrike_Damage` · `Ai_Gem_C_Charcoal_Projectile` · `Ai_Gem_C_Sharp_Arrow` · `Ai_Gem_C_Vengence_Projectile` · `Ai_Gem_C_Void_Explosion` · `Ai_Gem_E_Fangs_Projectile` · `Ai_Gem_E_Fever_Explosion` · `Ai_Gem_L_Embertail_Projectile` · `Ai_Gem_L_PureWhite_Projectile` · `Ai_Gem_L_SuppressedArcanum` · `Ai_Gem_R_Accuracy_Projectile` · `Ai_Gem_R_Blade` · `Ai_Gem_R_Dusk_Projectile` · `Ai_Gem_R_Ricochet` · `Ai_Gem_R_Snow_Projectile` · `Ai_Gem_R_Spiral_Fireball` · `Ai_Gem_U_GlacialCore_Projectile` · `Ai_Gem_U_LastStarlight` · `Ai_L_CoinExplosion_Explosion` · `Ai_L_MentalCorruption_Projectile` · `Ai_L_Multishot_Arrow` · `Ai_L_SmallMoltenCore_Dragon_Atk` · `Ai_L_SpectreBullet` · `Ai_M_FrostyCharge` · `Ai_MiniBoss_IceAura_AoE` · `Ai_MiniBoss_OrbSpitter_Orb` · `Ai_MiniBoss_SpinningArrow_Arrow` · `Ai_MirageSkin_Oblivion_Orb` · `Ai_Mon_DarkCave_CaveBat_Dash` · `Ai_Mon_DarkCave_DarkElemental_Atk_Projectile` · `Ai_Mon_DarkCave_DarkElemental_Barrage_Arrow` · `Ai_Mon_DarkCave_NightOlm_Atk_Projectile` · `Ai_Mon_Despair_BossAzurak_DoubleStomp_Instance` · `Ai_Mon_Despair_BossAzurak_Roll` · `Ai_Mon_Despair_BossAzurak_StompBlock` · `Ai_Mon_Despair_BossAzurak_StompProjectile_Projectile` · `Ai_Mon_Despair_ParalyticFly_Paralyze` · `Ai_Mon_Despair_WretchedArtillery_BarrageAtk_Missile` · `Ai_Mon_Forest_BossDemon_MainSkill_SpawnMissiles_Missile` · `Ai_Mon_Forest_Hound_Charge` · `Ai_Mon_Forest_SpiderSpitter_Atk` · `Ai_Mon_Ink_Archer_Atk` · `Ai_Mon_Ink_BossDarkMoon_SpawnEgoSword_Projectile` · `Ai_Mon_Ink_BossDarkMoon_ThrowSpear_Projectile` · `Ai_Mon_Ink_BossDarkMoon_ThrowSpear_TeleportAtk_AfterAtk` · `Ai_Mon_Ink_BossWhiteNight_AltAtk` · `Ai_Mon_Ink_BossWhiteNight_Cataclysm_Eclipse` · `Ai_Mon_Ink_BossWhiteNight_DestructionWave_Wave` · `Ai_Mon_Ink_DivineAnimal_Bite` · `Ai_Mon_Ink_GhostBlade_SwiftStep_Projectile` · `Ai_Mon_LavaLand_BossInfernus_BreathFire_Projectile` · `Ai_Mon_LavaLand_BossInfernus_Roar_Projectile` · `Ai_Mon_LavaLand_FireElemental_ExplosionSub` · `Ai_Mon_LavaLand_FireElemental_LaserAtk` · `Ai_Mon_LavaLand_InfernoSpider_LavaAtk` · `Ai_Mon_LavaLand_Magmadon_Charge_Projectile` · `Ai_Mon_Polaris_Smite` · `Ai_Mon_Primus_BossPrimusAeron_Adapt_Arbalest_Projectile` · `Ai_Mon_Primus_BossPrimusAeron_Adapt_Doom_Meteor_SubFireball` · `Ai_Mon_Sky_Baam_Teleport` · `Ai_Mon_Sky_BigBaam_BeamAtk` · `Ai_Mon_Sky_BossNyx_Blackhole` · `Ai_Mon_Sky_BossNyx_StellarDash` · `Ai_Mon_Sky_LittleBaam_Atk` · `Ai_Mon_Sky_StarSeed_SelfDestruct_Projectile` · `Ai_Mon_SnowMountain_BossSkoll_Capture` · `Ai_Mon_SnowMountain_BossSkoll_SummonArrow_Instance` · `Ai_Mon_SnowMountain_Scavenger_Throw` · `Ai_Mon_Special_BossErebos_Gaze_Instance` · `Ai_Mon_Special_BossErebos_SpawnBlackhole_Instance` · `Ai_Mon_Special_BossErebos_SpawnTormentor_Attacker_Instance` · `Ai_Mon_Special_BossErebos_StarRain_Instance` · `Ai_Mon_Special_BossLightElemental_Beam` · `Ai_Mon_Special_BossMaw_AnnihilationStance_Instance` · `Ai_Mon_Special_BossMaw_PrecisionShot_Projectile` · `Ai_Mon_Special_BossMaw_ScatterShot_ShortProjectile` · `Ai_Mon_Special_BossMaw_ShadowOverdrive_Projectile` · `Ai_Mon_Special_BossObliviax_ChargeSequence_MissileAtk` · `Ai_Mon_Special_BossPolaris_Holy_GoldenSpear_Projectile` · `Ai_Mon_Special_BossPolaris_Holy_SelfCleanse` · `Ai_Q_BigBorealChunk_Explosion` · `Ai_Q_CruelSun_Shockwave` · `Ai_Q_DeathMark_Projectile` · `Ai_Q_Discipline_Stomp` · `Ai_Q_EmbracingTheChill_AreaDoT` · `Ai_Q_EmbracingTheChill_Explosion` · `Ai_Q_EtherealInfluence` · `Ai_Q_EtherealInfluence_Projectile_Base` · `Ai_Q_Fleche_Dash` · `Ai_Q_HandCannon` · `Ai_Q_IncendiaryRounds_Attack` · `Ai_Q_Laceration_Circle` · `Ai_Q_Lunge` · `Ai_Q_Reduction_Projectile` · `Ai_Q_SuperNova` · `Ai_R_AnnihilationStance_Projectile` · `Ai_R_BackOff_Damage` · `Ai_R_BlackArbalest` · `Ai_R_ChainReaction` · `Ai_R_Chomp` · `Ai_R_DarkGrenade_Shard` · `Ai_R_FrozenFists_PunchDash` · `Ai_R_GlacialHammer` · `Ai_R_Ignite` · `Ai_R_OrbOfLight_ForwardDamaging` · `Ai_R_Parry_Projectile` · `Ai_R_PrecisionShot_Projectile` · `Ai_R_QuickTrigger_Projectile` · `Ai_R_RepulsiveShield_Projectile` · `Ai_R_Scattershot_Projectile` · `Ai_R_SerpentineBlessing_Projectile` · `Ai_R_ShadowOverdrive_Projectile` · `Ai_R_ShadowWalk_Projectile` · `Ai_R_StaticDischarge` · `Ai_Shrine_SmallSoul_Attack` · `Ai_Star_Cetus_F_BA_LightningEcho_Lightning` · `Ai_Star_Cetus_F_BI_SelfDamageAoeCold_AOE` · `Ai_Star_Yubar_F_EI_DashNoProjectile_Dash` · `Ai_U_BeamOfBalance_Beam` · `Ai_U_BigChomp` · `Ai_U_Hysteria_Claw` · `Ai_U_ShoutOfOblivion` · `Ai_U_WorldCracker` · `Ai_UnstableRatSwarm_Projectile` · [DamageInstance](/api/Global.DamageInstance) · [DashAttackInstance](/api/Global.DashAttackInstance) · [FinalDamageData](/api/Global.FinalDamageData) · `Forest_Fireplace` · `Gem_C_Confidence` · `Gem_C_Lethality` · `Gem_C_Shatter` · `Gem_C_Sulfur` · `Gem_C_Talc` · `Gem_C_Vengeance` · `Gem_E_Apathy` · `Gem_E_Blossom` · `Gem_E_Flexibility` · `Gem_E_Inversion` · `Gem_E_Might` · `Gem_E_OurStory_Completed` · `Gem_E_OurStory_Unfinished` · `Gem_E_Overload` · `Gem_E_Pain` · `Gem_E_Predation` · `Gem_E_Umbra` · `Gem_L_DivineFaith` · `Gem_L_Embertail` · `Gem_L_Supersymmetry` · `Gem_R_Abyss` · `Gem_R_Bleak` · `Gem_R_Contempt` · `Gem_R_Lightweight` · `Gem_R_Slippery` · `Gem_U_EternalFlame` · `Ink_BossRoomDamageGround` · `LavaLand_Lava` · `LucidDream_BlandStarSoup` · `LucidDream_EmbraceMortality` · `Mon_Special_BossPolaris` · `RoomMod_CorruptedChaos_AuraOfPain` · `RoomMod_InversionSigil` · `Se_C_CorrosiveTrails_Poisoned` · `Se_C_IceBlock` · `Se_Curse_DarkUrge` · `Se_Curse_Fragility` · `Se_Curse_FragmentedBeing` · `Se_Curse_Lethargy` · `Se_Curse_SoftSkin` · `Se_Curse_UnstableEnergy` · `Se_D_AstridsMasterpieceEnGarde` · `Se_D_AstridsMasterpiecePriorite` · `Se_DistantMemories` · `Se_E_Harvest_OnVictim` · `Se_E_LizardlyBlessing` · `Se_E_Rewind_Damage` · `Se_Elm_Dark` · `Se_Elm_Fire` · `Se_Elm_Light` · `Se_EngulfedInFlame` · `Se_Gem_R_Hedgehog_Aura` · `Se_Gem_R_Wound_Wounded` · `Se_L_MentalCorruption` · `Se_L_PyranasFireball` · `Se_M_Charge` · `Se_MiniBoss_BloodThorn_Bleeding` · `Se_MiniBoss_UnstableExplosive_Explosion` · `Se_MirageSkin_Pulverization` · `Se_Mon_Despair_ParalyticFly_Atk_Instance` · `Se_Mon_Ink_Boss_Rage` · `Se_Mon_Primus_BossPrimusAeron_Adaptation` · `Se_Mon_SnowMountain_VikingWarrior_DmgReducer` · `Se_Mon_Special_BossPolaris_Adaptation` · `Se_Mon_Special_BossPolaris_CleansingFlame` · `Se_PlayTutorialHeroProtection` · `Se_PolarisHallucination` · `Se_R_BoneCrusher` · `Se_R_Immolation` · `Se_R_Lava_Debuff` · `Se_R_Parry_Start` · `Se_R_RepulsiveShield` · `Se_R_UnbreakableDetermination` · `Se_RoomMod_BlackRain` · `Se_Star_Aurena_L_HealAmpWithPenalty` · `Se_Star_Bismuth_F_IT_SmallerRingAddDisplacement` · `Se_Star_Cetus_L_ArmorBuffOnShield` · `Se_Star_Cetus_L_FrostResistAndBuff` · `Se_Star_Cetus_L_MaxHpDamagePenalty` · `Se_Star_D_BossDamageAmp` · `Se_Star_D_DamageBonusOnAllElemental` · `Se_Star_D_RiftFirstCastDamageUp` · `Se_Star_D_ShieldDamageAmp` · `Se_Star_Husk_D_DamageAmpOnLowHpTarget` · `Se_Star_Husk_D_DarkAttackWithPenalty` · `Se_Star_Husk_F_DE_MarkHitDodgeCDR` · `Se_Star_L_DamageReductionFromChilled` · `Se_Star_L_ElementalResistance` · `Se_Star_Lacerta_F_HC_NoDelayDoubleCast` · `Se_Star_Mist_D_BossDamageOnHighHp` · `Se_Star_Mist_D_HunterDamage` · `Se_Star_Mist_L_AddedDodgeWithPenalty` · `Se_Star_Nachia_D_CanineLover` · `Se_Star_Vesper_D_BossHunterAmpWithPenalty` · `Se_Star_Vesper_L_FireResistance` · `Se_Star_Yubar_D_BonusDamageToLight` · `Se_U_HerWorld_Blackhole` · [SkillTrigger](/api/Global.SkillTrigger) · `Sky_LightFogDamager` · `St_D_DisintegratingClaw` · `Star_Global_DecreaseDamageFromChilled` · `Star_Global_ElementResistance` · `Star_Lacerta_HandCannon` · `Sum_R_AnnoyingBanner` · [Summon](/api/Global.Summon) · `Trap_FlameJet`

### Dependencies (7)

*Types and components that `DamageData` references or depends upon:*

[Actor](/api/Global.Actor) · `ActorFlags` · [Entity](/api/Global.Entity) · [FinalDamageData](/api/Global.FinalDamageData) · [FinalHealData](/api/Global.FinalHealData) · [ReactionChain](/api/Global.ReactionChain) · [ScalingValue](/api/Global.ScalingValue)

### Related Enums (3)

*Enumerations referenced in fields, properties, or method signatures:*

[`AttackEffectType`](/enums#attackeffecttype) · [`DamageAttribute`](/enums#damageattribute) · [`ElementalType`](/enums#elementaltype)

:::
