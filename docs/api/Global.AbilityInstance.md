# Class: AbilityInstance

- **Category:** <span class="cat-dot" style="--cat-color: #ef4444" data-cat="Combat & Abilities"></span> Combat & Abilities
- **Namespace:** `Global`
- **Assembly:** `Dew.Core.dll`
- **Attributes:** `[LogicUpdatePriority]`
- **Inheritance / Derived:** [DewNetworkBehaviour](/api/Global.DewNetworkBehaviour) → [Actor](/api/Global.Actor) → [DamageInstance](/api/Global.DamageInstance) → [MeleeAttackInstance](/api/Global.MeleeAttackInstance) → [MockAbilityInstance](/api/Global.MockAbilityInstance) → [PickupInstance](/api/Global.PickupInstance) → [Projectile](/api/Global.Projectile) → [PunishmentInstance](/api/Global.PunishmentInstance) → [StatusEffect](/api/Global.StatusEffect)

```csharp
[LogicUpdatePriority(-200)]
public abstract class AbilityInstance : Actor, ILogicUpdate, ICleanup, ICustomDestroyRoutine
```

## Fields (12)

::: details Click to expand Fields (12)

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`budgetCost`** | `[BoxGroup("Ability Instance Settings", true, false, 0)] public int budgetCost` |  |
| **`chain`** | `[NonSerialized] public ReactionChain chain` | If this instance is part of reaction, you can provide ReactionChain in this variable. Available only on server. |
| **`currentCostSum`** | `public static int currentCostSum` |  |
| **`currentCostSumPerPlayer`** | `public static Dictionary<DewPlayer, int> currentCostSumPerPlayer` |  |
| **`endEffect`** | `[BoxGroup("Ability Instance Settings", true, false, 0)] [LabelText("End Effect (Attached To Caster)")] public GameObject endEffect` |  |
| **`maxBudget`** | `public static int maxBudget` |  |
| **`startEffect`** | `[BoxGroup("Ability Instance Settings", true, false, 0)] [LabelText("Loop Effect (Attached To Caster)")] public GameObject startEffect` |  |
| **`startEffectNoStop`** | `[BoxGroup("Ability Instance Settings", true, false, 0)] [LabelText("Start Effect (Attached To Caster)")] public GameObject startEffectNoStop` |  |
| **`tvDefaultAllExceptSelf`** | `protected AbilityTargetValidatorWrapper tvDefaultAllExceptSelf` |  |
| **`tvDefaultHarmfulEffectTargets`** | `protected AbilityTargetValidatorWrapper tvDefaultHarmfulEffectTargets` |  |
| **`tvDefaultUsefulEffectTargets`** | `protected AbilityTargetValidatorWrapper tvDefaultUsefulEffectTargets` |  |
| **`useBudgetSystem`** | `public static bool useBudgetSystem` |  |

:::

## Properties (7)

::: details Click to expand Properties (7)

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`budgetPressure`** | `public BudgetPressure budgetPressure { get; }` | Returns current budget pressure. Costly ability instances must adjust their resource spending according to this value.Requires budgetCost to be set to non-zero value. |
| **`effectiveLevel`** | `public int effectiveLevel { get; }` |  |
| **`gem`** | `public Gem gem { get; set; }` | If this instance is from a gem, you can access the gem from here. |
| **`hasOngoingSequences`** | `public bool hasOngoingSequences { get; }` |  |
| **`info`** | `[SaveVar] [SaveVar(SaveVarFlags.Default)] public CastInfo info { get; set; }` |  |
| **`skillLevel`** | `[SaveVar] [SaveVar(SaveVarFlags.Default)] public int skillLevel { get; set; }` | Level of its origin skill trigger at the time this instance was cast. Defaults to -1 or that of parent's level.Parent type can either be SkillTrigger, AbilityInstance, or Gem.You can override level by setting this field when the instance is preparing. |
| **`statEntity`** | `public Entity statEntity { get; }` |  |

:::

## Methods (29)

::: details `Budget_ShouldDoFullCalculations()`

Should this instance skip calculations? Based on current budget pressure.Use this as a default suggested behavior.

```csharp
public bool Budget_ShouldDoFullCalculations()
```

**Returns:** `bool`

:::

::: details `Budget_ShouldPlayEffects()`

Should this instance play effects? Based on current budget pressure.Use this as a default suggested behavior.

```csharp
public bool Budget_ShouldPlayEffects()
```

**Returns:** `bool`

:::

::: details `CreateDamage(SourceType, ScalingValue, float)`

```csharp
public DamageData CreateDamage(DamageData.SourceType type, ScalingValue value, float procCoefficient = 1)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `type` | [`DamageData.SourceType`](/api/Global.DamageData) |  |
| `value` | [`ScalingValue`](/api/Global.ScalingValue) |  |
| `procCoefficient` | `float` |  |

**Returns:** `DamageData`

:::

::: details `CreateStatusEffect&lt;T&gt;(T, Entity, Action&lt;T&gt;)`

Create a new status effect and attach it to an entity.This can return null if the creation fails:e.g. Trying to apply a status effect with isKilledByUnstoppable flag to an unstoppable/invulnerable entity.

```csharp
public T CreateStatusEffect<T>(T prefab, Entity victim, Action<T> beforePrepare = null) where T : StatusEffect
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `prefab` | `T` |  |
| `victim` | [`Entity`](/api/Global.Entity) |  |
| `beforePrepare` | `System.Action<T>` |  |
| `` | `T` |  |

**Returns:** `T`

:::

::: details `CreateStatusEffect&lt;T&gt;(Entity, Action&lt;T&gt;)`

Create a new status effect and attach it to an entity.This can return null if the creation fails:e.g. Trying to apply a status effect with isKilledByUnstoppable flag to an unstoppable/invulnerable entity.

```csharp
public T CreateStatusEffect<T>(Entity victim, Action<T> beforePrepare = null) where T : StatusEffect
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `victim` | [`Entity`](/api/Global.Entity) |  |
| `beforePrepare` | `System.Action<T>` |  |
| `` | `T` |  |

**Returns:** `T`

:::

::: details `Damage(ScalingValue, float)`

```csharp
public DamageData Damage(ScalingValue value, float procCoefficient = 1)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `value` | [`ScalingValue`](/api/Global.ScalingValue) |  |
| `procCoefficient` | `float` |  |

**Returns:** `DamageData`

:::

::: details `DefaultDamage(ScalingValue, float)`

```csharp
public DamageData DefaultDamage(ScalingValue value, float procCoefficient = 1)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `value` | [`ScalingValue`](/api/Global.ScalingValue) |  |
| `procCoefficient` | `float` |  |

**Returns:** `DamageData`

:::

::: details `DestroyOnCondition(Func&lt;bool&gt;)`

Kill this instance when condition is met.

```csharp
public AbilityInstance.WatchedCondition DestroyOnCondition(Func<bool> condition)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `condition` | `System.Func<TResult><bool>` |  |

**Returns:** `AbilityInstance.WatchedCondition`

:::

::: details `DestroyOnDeath(Entity, bool)`

Kill this instance when the specified entity dies/gets destroyed.

```csharp
public void DestroyOnDeath(Entity entity, bool includeKnockOuts = false)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `entity` | [`Entity`](/api/Global.Entity) |  |
| `includeKnockOuts` | `bool` |  |

:::

::: details `DestroyOnDestroy(Actor)`

Remove this instance when the specified actor gets destroyed.

```csharp
public void DestroyOnDestroy(Actor actor)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `actor` | [`Actor`](/api/Global.Actor) |  |

:::

::: details `GetActorReadableName()`

```csharp
public override string GetActorReadableName()
```

**Returns:** `string`

:::

::: details `GetValue(ScalingValue)`

```csharp
public float GetValue(ScalingValue val)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `val` | [`ScalingValue`](/api/Global.ScalingValue) |  |

**Returns:** `float`

:::

::: details `GetValue(StarScalingValue)`

```csharp
public float GetValue(StarScalingValue value)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `value` | [`StarScalingValue`](/api/Global.StarScalingValue) |  |

**Returns:** `float`

:::

::: details `GetValue&lt;T&gt;(T[])`

```csharp
public T GetValue<T>(T[] val)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `val` | `T[]` |  |
| `` | `T` |  |

**Returns:** `T`

:::

::: details `GetValueInt(StarScalingValue)`

```csharp
public int GetValueInt(StarScalingValue value)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `value` | [`StarScalingValue`](/api/Global.StarScalingValue) |  |

**Returns:** `int`

:::

::: details `Heal(ScalingValue)`

```csharp
public HealData Heal(ScalingValue amount)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `amount` | [`ScalingValue`](/api/Global.ScalingValue) |  |

**Returns:** `HealData`

:::

::: details `LogicUpdate(float)`

```csharp
public override void LogicUpdate(float dt)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `dt` | `float` |  |

:::

::: details `MagicDamage(ScalingValue, float)`

```csharp
public DamageData MagicDamage(ScalingValue value, float procCoefficient = 1)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `value` | [`ScalingValue`](/api/Global.ScalingValue) |  |
| `procCoefficient` | `float` |  |

**Returns:** `DamageData`

:::

::: details `OnCreate()`

```csharp
protected override void OnCreate()
```

:::

::: details `OnCreateSequenced()`

Started everywhere when this ability instance is created, running on LogicUpdates.This will stop running when this instance gets killed.Return SequenceInstructions (e.g.new SI.WaitForSeconds()) to yield this sequence.Returning null has same effect ofnew SI.WaitForNextLogicUpdate().

```csharp
protected virtual IEnumerator OnCreateSequenced()
```

**Returns:** `System.Collections.IEnumerator`

:::

::: details `OnDestroyActor()`

```csharp
protected override void OnDestroyActor()
```

:::

::: details `OnPrepare()`

Called on server right before this instance to be spawned.Configure this instance's initial state here.By default this sets skillLevel to parent's level.Parent type can either be SkillTrigger, AbilityInstance, or Gem.

```csharp
protected override void OnPrepare()
```

:::

::: details `OnStart()`

```csharp
public override void OnStart()
```

:::

::: details `PhysicalDamage(ScalingValue, float)`

```csharp
public DamageData PhysicalDamage(ScalingValue value, float procCoefficient = 1)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `value` | [`ScalingValue`](/api/Global.ScalingValue) |  |
| `procCoefficient` | `float` |  |

**Returns:** `DamageData`

:::

::: details `PhysicalMagicDamage(ScalingValue, float)`

```csharp
public DamageData PhysicalMagicDamage(ScalingValue value, float procCoefficient = 1)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `value` | [`ScalingValue`](/api/Global.ScalingValue) |  |
| `procCoefficient` | `float` |  |

**Returns:** `DamageData`

:::

::: details `PureDamage(ScalingValue, float)`

```csharp
public DamageData PureDamage(ScalingValue value, float procCoefficient = 1)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `value` | [`ScalingValue`](/api/Global.ScalingValue) |  |
| `procCoefficient` | `float` |  |

**Returns:** `DamageData`

:::

::: details `ResetBudget()`

```csharp
public static void ResetBudget()
```

:::

::: details `StartChargingChannel(ChargingChannel)`

```csharp
public void StartChargingChannel(ChargingChannel channel)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `channel` | [`ChargingChannel`](/api/Global.ChargingChannel) |  |

:::

::: details `StartSequence(IEnumerator)`

Start a sequence that will run while this instance is alive on LogicUpdates.

```csharp
protected void StartSequence(IEnumerator sequence)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `sequence` | `System.Collections.IEnumerator` |  |

:::


## Architecture & Relationships

::: details Click to expand Architecture & Relationships

### Used By (937)

*Classes and systems that invoke, reference, or depend on `AbilityInstance`:*

[AbilityTrigger](/api/Global.AbilityTrigger) · [Actor](/api/Global.Actor) · `Ai_Ai_Mon_Ink_BossWhiteNight_OneInchPunch_Atk` · `Ai_ArcticTerritory` · `Ai_Atk_AurenaSwipe` · `Ai_Atk_LacertaRifle` · `Ai_Atk_LacertaRifle_Crit` · `Ai_Atk_YubarStardust` · `Ai_AutoDetectPresence_DetectWave` · `Ai_C_BackStep` · `Ai_C_BackStep_Bomb` · `Ai_C_BeamOfLight` · `Ai_C_CorrosiveTrails_Gas` · `Ai_C_DarkBolt` · `Ai_C_DarkSpear` · `Ai_C_FlashFreeze` · `Ai_C_GlacialStomp` · `Ai_C_IceClaw` · `Ai_C_MagicSword` · `Ai_C_MassProtection` · `Ai_C_Pew` · `Ai_C_Pew_Projectile` · `Ai_C_PressurePoint` · `Ai_C_Purgatory` · `Ai_C_Purgatory_Heal` · `Ai_C_ShockTrap_Mine` · `Ai_C_Sneeze` · `Ai_C_SparklingWaterGun` · `Ai_C_Starfall` · `Ai_C_Starfall_Projectile` · `Ai_C_SwiftSlash` · `Ai_C_Whirlwind` · `Ai_Culinary_Pickup` · `Ai_Curse_AnchorOfMind_Anchor` · `Ai_Curse_DreamAfflictionInductive_Smite` · `Ai_Curse_IntermittentExplosion_Explosion` · `Ai_D_BeautifulThreat_Feather` · `Ai_D_BurningFist_Attack` · `Ai_D_BurningFist_Attack_Instance` · `Ai_D_ChargedAnguillian_Lightning` · `Ai_D_ExoticMatter_Projectile` · `Ai_D_IceColdPresence_AOE` · `Ai_D_IcyVeins_Damage` · `Ai_D_ParryMaster_Parry` · `Ai_D_PrismaticEyes_Attack` · `Ai_D_QuartetOfDeath_Explosion` · `Ai_D_Resolve_Push` · `Ai_D_SalamanderPowder_Projectile` · `Ai_D_ScarOfTheWind_DashAtk` · `Ai_D_SharedPain_Instance` · `Ai_E_Aftershock_Damage` · `Ai_E_AntiGravity` · `Ai_E_Blink` · `Ai_E_Blink_Back` · `Ai_E_ChainLightning` · `Ai_E_ClutchesOfMalice` · `Ai_E_ClutchesOfMalice_ReachAndPull` · `Ai_E_CrimsonLance` · `Ai_E_DoomsdayMeteor` · `Ai_E_DoomsdayMeteor_SubProjectile` · `Ai_E_FinalExplosion_Explosion` · `Ai_E_FlameJet` · `Ai_E_FlameJet_Projectile` · `Ai_E_Harvest` · `Ai_E_JusticeGuillotine` · `Ai_E_MassCleanse` · `Ai_E_MysticDagger` · `Ai_E_Permafrost` · `Ai_E_SearingCharge` · `Ai_E_ShadowVolley` · `Ai_E_ShadowVolley_Projectile` · `Ai_E_SliceThroat` · `Ai_E_StygianRush` · `Ai_E_StygianRush_Rush` · `Ai_E_WinterDive` · `Ai_EmbraceNewIdentity` · `Ai_FirstBonusQualityUpgrader` · `Ai_Gem_C_Charcoal_Projectile` · `Ai_Gem_C_Sharp_Arrow` · `Ai_Gem_C_Vengence_Projectile` · `Ai_Gem_C_Void_Explosion` · `Ai_Gem_E_Crimson` · `Ai_Gem_E_Domination_CritGainEffect` · `Ai_Gem_E_Fangs_Projectile` · `Ai_Gem_E_Insight_Damage` · `Ai_Gem_E_Predation_Pickup` · `Ai_Gem_E_Thunder` · `Ai_Gem_L_Embertail_Projectile` · `Ai_Gem_L_PureWhite_Projectile` · `Ai_Gem_L_SolarEye` · `Ai_Gem_L_SuppressedArcanum` · `Ai_Gem_R_Accuracy_Projectile` · `Ai_Gem_R_Blade` · `Ai_Gem_R_Celestial` · `Ai_Gem_R_Dusk_Projectile` · `Ai_Gem_R_Glaciate` · `Ai_Gem_R_Ricochet` · `Ai_Gem_R_Shock_Lightning` · `Ai_Gem_R_Snow_Projectile` · `Ai_Gem_R_Spiral_Fireball` · `Ai_Gem_R_Stillness` · `Ai_Gem_U_GlacialCore_Projectile` · `Ai_Gem_U_LastStarlight` · `Ai_GenericDodge` · `Ai_GlacialBarrier_Spawn` · `Ai_Hatred_Curse` · `Ai_Hatred_InkMapCurse` · `Ai_HunterArtillery_Big` · `Ai_HunterArtillery_Small` · `Ai_HunterBuff_ShadowWalk` · `Ai_L_Blizzard` · `Ai_L_Blizzard_Instance` · `Ai_L_BloodStrike_Meat` · `Ai_L_ButchersStrike` · `Ai_L_CoinExplosion_Coin` · `Ai_L_LightExplosion` · `Ai_L_MentalCorruption_Projectile` · `Ai_L_Multishot_Arrow` · `Ai_L_SmallMoltenCore_Dragon_Atk` · `Ai_L_SoulKiller` · `Ai_L_SoulKiller_Soul` · `Ai_L_SpectreBullet` · `Ai_M_DreamyWaltz` · `Ai_M_DreamyWaltz_BuffExplosion` · `Ai_M_FeatheryDash` · `Ai_M_FrostyCharge` · `Ai_M_Sprint` · `Ai_MiniBoss_BloodThorn_MainThorn` · `Ai_MiniBoss_BloodThorn_Projectile` · `Ai_MiniBoss_BloodThorn_SubThorn` · `Ai_MiniBoss_IceAura_AoE` · `Ai_MiniBoss_OrbSpitter_Orb` · `Ai_MiniBoss_SpinningArrow_Arrow` · `Ai_MirageSkin_Delusion_Missile` · `Ai_MirageSkin_Oppression_Explode` · `Ai_MirageSkin_Pulverization_Stomp` · `Ai_Mon_DarkCave_BossSeeker_Atk` · `Ai_Mon_DarkCave_BossSeeker_Atk_Projectile` · `Ai_Mon_DarkCave_BossSeeker_BlinkBarrage` · `Ai_Mon_DarkCave_BossSeeker_GreenChaserOrb` · `Ai_Mon_DarkCave_BossSeeker_PurpleOrb` · `Ai_Mon_DarkCave_BossSeeker_PurpleOrb_Instance` · `Ai_Mon_DarkCave_BossSeeker_RedFissure` · `Ai_Mon_DarkCave_BossSeeker_TunnelVision_Claw` · `Ai_Mon_DarkCave_BossSeeker_TunnelVision_SecondPoolAtk` · `Ai_Mon_DarkCave_BossSeeker_YellowDiagram_MainInstance` · `Ai_Mon_DarkCave_BossSeeker_YellowDiagram_Spawner` · `Ai_Mon_DarkCave_CaveBat_Dash` · `Ai_Mon_DarkCave_DarkElemental_Atk_Projectile` · `Ai_Mon_DarkCave_DarkElemental_Atk_Spawner` · `Ai_Mon_DarkCave_DarkElemental_Barrage_Arrow` · `Ai_Mon_DarkCave_DarkElemental_Barrage_Spawner` · `Ai_Mon_DarkCave_NightOlm_Atk` · `Ai_Mon_DarkCave_NightOlm_Atk_Projectile` · `Ai_Mon_DarkCave_Oppressor_Hypnotize` · `Ai_Mon_Despair_BossAzurak_AltAtk` · `Ai_Mon_Despair_BossAzurak_Atk_InitDamage` · `Ai_Mon_Despair_BossAzurak_Atk_SubSpawner` · `Ai_Mon_Despair_BossAzurak_DoubleStomp` · `Ai_Mon_Despair_BossAzurak_DoubleStomp_Instance` · `Ai_Mon_Despair_BossAzurak_RoarAtk` · `Ai_Mon_Despair_BossAzurak_Roll` · `Ai_Mon_Despair_BossAzurak_SpawnMonsters` · `Ai_Mon_Despair_BossAzurak_StompBlock` · `Ai_Mon_Despair_BossAzurak_StompBlock_Artillery` · `Ai_Mon_Despair_BossAzurak_StompGlobal` · `Ai_Mon_Despair_BossAzurak_StompProjectile` · `Ai_Mon_Despair_BossAzurak_StompProjectile_FirstAtk` · `Ai_Mon_Despair_BossAzurak_StompProjectile_Projectile` · `Ai_Mon_Despair_BossAzurak_StompProjectile_Spawner` · `Ai_Mon_Despair_BossAzurak_StompTargetArea` · `Ai_Mon_Despair_BossAzurak_SummonDisplacers` · `Ai_Mon_Despair_Displacer_Blink` · `Ai_Mon_Despair_Displacer_SpawnEgg` · `Ai_Mon_Despair_DreadBug_Jump` · `Ai_Mon_Despair_DreadBug_JumpBack` · `Ai_Mon_Despair_ParalyticFly_Atk` · `Ai_Mon_Despair_ParalyticFly_Paralyze` · `Ai_Mon_Despair_UnstableRat_Explosion` · `Ai_Mon_Despair_WretchedArtillery_BarrageAtk` · `Ai_Mon_Despair_WretchedArtillery_BarrageAtk_AoE` · `Ai_Mon_Despair_WretchedArtillery_BarrageAtk_Missile` · `Ai_Mon_Forest_BossDemon_AltSkill_LineAtk` · `Ai_Mon_Forest_BossDemon_AltSkill_LineAtk_Spawner` · `Ai_Mon_Forest_BossDemon_AltSkill_Stomp` · `Ai_Mon_Forest_BossDemon_AltSkill_Stomp_Tree` · `Ai_Mon_Forest_BossDemon_Blink` · `Ai_Mon_Forest_BossDemon_DelayedAtk` · `Ai_Mon_Forest_BossDemon_MainSkill_SpawnMissiles` · `Ai_Mon_Forest_BossDemon_MainSkill_SpawnMissiles_Missile` · `Ai_Mon_Forest_BossDemon_MainSkill_Stomp` · `Ai_Mon_Forest_BossDemon_Spawn` · `Ai_Mon_Forest_BossDemon_SpecialAtk` · `Ai_Mon_Forest_Hound_Charge` · `Ai_Mon_Forest_SpiderSpitter_Atk` · `Ai_Mon_Forest_SpiderSpitter_Backdash` · `Ai_Mon_Forest_SpiderWarrior_Jump` · `Ai_Mon_Forest_SpiderWarrior_SpawnScarabs` · `Ai_Mon_Forest_Treant_PowerBomb` · `Ai_Mon_Ink_Archer_Atk` · `Ai_Mon_Ink_Archer_Dodge` · `Ai_Mon_Ink_BossDarkMoon_AltAtk_HorizontalAtk` · `Ai_Mon_Ink_BossDarkMoon_AltAtk_Spawner` · `Ai_Mon_Ink_BossDarkMoon_Blade` · `Ai_Mon_Ink_BossDarkMoon_Blade_Instance` · `Ai_Mon_Ink_BossDarkMoon_Blade_RageInstance` · `Ai_Mon_Ink_BossDarkMoon_Eclipse` · `Ai_Mon_Ink_BossDarkMoon_Eclipse_Instance` · `Ai_Mon_Ink_BossDarkMoon_Hammer` · `Ai_Mon_Ink_BossDarkMoon_ShortDash` · `Ai_Mon_Ink_BossDarkMoon_ShortDash_Atk` · `Ai_Mon_Ink_BossDarkMoon_SpawnEgoSword` · `Ai_Mon_Ink_BossDarkMoon_SpawnEgoSword_Controller` · `Ai_Mon_Ink_BossDarkMoon_SpawnEgoSword_Projectile` · `Ai_Mon_Ink_BossDarkMoon_SpawnEgoSword_Spawner` · `Ai_Mon_Ink_BossDarkMoon_Spear` · `Ai_Mon_Ink_BossDarkMoon_Spear_Instance` · `Ai_Mon_Ink_BossDarkMoon_TeleportAtk` · `Ai_Mon_Ink_BossDarkMoon_TeleportDash` · `Ai_Mon_Ink_BossDarkMoon_ThrowSpear_AoE` · `Ai_Mon_Ink_BossDarkMoon_ThrowSpear_Projectile` · `Ai_Mon_Ink_BossDarkMoon_ThrowSpear_Spawner` · `Ai_Mon_Ink_BossDarkMoon_ThrowSpear_TeleportAtk` · `Ai_Mon_Ink_BossDarkMoon_ThrowSpear_TeleportAtk_AfterAtk` · `Ai_Mon_Ink_BossWhiteNIght_BuddhasPalm_Spawner` · `Ai_Mon_Ink_BossWhiteNight_AltAtk` · `Ai_Mon_Ink_BossWhiteNight_AltAtk_Ready` · `Ai_Mon_Ink_BossWhiteNight_BuddhasPalm_Instance` · `Ai_Mon_Ink_BossWhiteNight_Cataclysm` · `Ai_Mon_Ink_BossWhiteNight_Cataclysm_Eclipse` · `Ai_Mon_Ink_BossWhiteNight_Cataclysm_Instance` · `Ai_Mon_Ink_BossWhiteNight_Cataclysm_SafeZone` · `Ai_Mon_Ink_BossWhiteNight_DestructionWave` · `Ai_Mon_Ink_BossWhiteNight_DestructionWave_Wave` · `Ai_Mon_Ink_BossWhiteNight_EnergyWave_Instance` · `Ai_Mon_Ink_BossWhiteNight_EnergyWave_Spawner` · `Ai_Mon_Ink_BossWhiteNight_OneInchPunch_Pull` · `Ai_Mon_Ink_BossWhiteNight_Oppression` · `Ai_Mon_Ink_BossWhiteNight_RageInstance` · `Ai_Mon_Ink_BossWhiteNight_RageInstance_Rock` · `Ai_Mon_Ink_BossWhiteNight_RageInstance_RockSpawner` · `Ai_Mon_Ink_BossWhiteNight_Ready` · `Ai_Mon_Ink_Boss_OnDeath` · `Ai_Mon_Ink_DivineAnimal_Bite` · `Ai_Mon_Ink_DivineAnimal_Missile` · `Ai_Mon_Ink_DivineAnimal_Missile_Sub` · `Ai_Mon_Ink_DivineAnimal_Stomp` · `Ai_Mon_Ink_EgoSword_Atk` · `Ai_Mon_Ink_GhostBlade_AtkSpawner` · `Ai_Mon_Ink_GhostBlade_DemolitionMan` · `Ai_Mon_Ink_GhostBlade_MeleeAtk` · `Ai_Mon_Ink_GhostBlade_SwiftStep` · `Ai_Mon_Ink_GhostBlade_SwiftStep_Atk` · `Ai_Mon_Ink_GhostBlade_SwiftStep_Projectile` · `Ai_Mon_Ink_GhostSpear_Atk` · `Ai_Mon_Ink_GhostSpear_Dash` · `Ai_Mon_Ink_Tiger_DashAtk` · `Ai_Mon_Ink_Tiger_ShadowWalk` · `Ai_Mon_LavaLand_BossInfernus_AltAtk_Instance` · `Ai_Mon_LavaLand_BossInfernus_Atk` · `Ai_Mon_LavaLand_BossInfernus_BreathFire` · `Ai_Mon_LavaLand_BossInfernus_BreathFire_Projectile` · `Ai_Mon_LavaLand_BossInfernus_Dash` · `Ai_Mon_LavaLand_BossInfernus_Jump` · `Ai_Mon_LavaLand_BossInfernus_MeteorSpawner` · `Ai_Mon_LavaLand_BossInfernus_PowerBomb` · `Ai_Mon_LavaLand_BossInfernus_PowerBomb_FlamePillar` · `Ai_Mon_LavaLand_BossInfernus_Roar` · `Ai_Mon_LavaLand_BossInfernus_Roar_Projectile` · `Ai_Mon_LavaLand_BossInfernus_Swipe` · `Ai_Mon_LavaLand_BossInfernus_WallStunKnockback` · `Ai_Mon_LavaLand_FireElemental_BackDash` · `Ai_Mon_LavaLand_FireElemental_Destruct` · `Ai_Mon_LavaLand_FireElemental_DestructSub` · `Ai_Mon_LavaLand_FireElemental_Explosion` · `Ai_Mon_LavaLand_FireElemental_ExplosionSub` · `Ai_Mon_LavaLand_FireElemental_LaserAtk` · `Ai_Mon_LavaLand_InfernoSpider_LavaAtk` · `Ai_Mon_LavaLand_Magmadon_AtkSpawner` · `Ai_Mon_LavaLand_Magmadon_Charge` · `Ai_Mon_LavaLand_Magmadon_Charge_Projectile` · `Ai_Mon_LavaLand_SuperheatedWolf_SelfDestruct` · `Ai_Mon_Polaris_Smite` · `Ai_Mon_Primus_BossPrimusAeron_Adapt_Arbalest` · `Ai_Mon_Primus_BossPrimusAeron_Adapt_Arbalest_Projectile` · `Ai_Mon_Primus_BossPrimusAeron_Adapt_Atk` · `Ai_Mon_Primus_BossPrimusAeron_Adapt_Doom_Meteor` · `Ai_Mon_Primus_BossPrimusAeron_Adapt_Doom_Meteor_SubFireball` · `Ai_Mon_Primus_BossPrimusAeron_Adapt_Doom_PyranasFireball` · `Ai_Mon_Primus_BossPrimusAeron_Adapt_IceClaw` · `Ai_Mon_Primus_BossPrimusAeron_Adapt_IceClaw_Frost` · `Ai_Mon_Primus_BossPrimusAeron_Adapt_SmiteStorm` · `Ai_Mon_Primus_BossPrimusAeron_Adapt_SmiteStorm_Smite` · `Ai_Mon_Primus_BossPrimusAeron_Adapt_Starfall` · `Ai_Mon_Primus_BossPrimusAeron_Adapt_Starfall_Instance` · `Ai_Mon_Primus_BossPrimusAeron_Adaptation_Orb` · `Ai_Mon_Primus_BossPrimusAeron_Dash` · `Ai_Mon_Primus_BossPrimusAeron_Force_DropGiantSword` · `Ai_Mon_Primus_BossPrimusAeron_Force_GoldRain_Attack_SubInstance` · `Ai_Mon_Primus_BossPrimusAeron_Force_Grab` · `Ai_Mon_Primus_BossPrimusAeron_Force_JumpAttack` · `Ai_Mon_Primus_BossPrimusAeron_Rage_Atk` · `Ai_Mon_Primus_BossPrimusAeron_Rage_DashAttack` · `Ai_Mon_Primus_BossPrimusAeron_Rage_MassDelusion` · `Ai_Mon_Primus_BossPrimusAeron_Rage_MassSilence_Instance` · `Ai_Mon_Primus_BossPrimusAeron_Rage_MassSilence_Spawner` · `Ai_Mon_Primus_BossPrimusAeron_Rage_Whirlwind` · `Ai_Mon_Primus_SpawnAttack` · `Ai_Mon_Sky_Baam_Teleport` · `Ai_Mon_Sky_Baam_TeleportSequence` · `Ai_Mon_Sky_BigBaam_BeamAtk` · `Ai_Mon_Sky_BigBaam_Main_Root` · `Ai_Mon_Sky_BossNyx_AltTeleport` · `Ai_Mon_Sky_BossNyx_Atk` · `Ai_Mon_Sky_BossNyx_Blackhole` · `Ai_Mon_Sky_BossNyx_CreateSeeds` · `Ai_Mon_Sky_BossNyx_LaserAtk` · `Ai_Mon_Sky_BossNyx_LineAtk` · `Ai_Mon_Sky_BossNyx_LineAtk_Displacement` · `Ai_Mon_Sky_BossNyx_PillarOfStars` · `Ai_Mon_Sky_BossNyx_PullAtk` · `Ai_Mon_Sky_BossNyx_PullAtk_AfterAtk` · `Ai_Mon_Sky_BossNyx_Starfall` · `Ai_Mon_Sky_BossNyx_StellarDash` · `Ai_Mon_Sky_BossNyx_Swipe` · `Ai_Mon_Sky_BossNyx_Teleport` · `Ai_Mon_Sky_LittleBaam_Atk` · `Ai_Mon_Sky_LittleBaam_Reposition` · `Ai_Mon_Sky_StarSeed_SelfDestruct` · `Ai_Mon_Sky_StarSeed_SelfDestruct_Projectile` · `Ai_Mon_Sky_StellaMatter_Atk` · `Ai_Mon_Sky_StellaMatter_AtkSub` · `Ai_Mon_Sky_StellaMatter_Dash` · `Ai_Mon_Sky_StellaMatter_ThrowMagazine` · `Ai_Mon_Sky_StellaMatter_ThrowSub` · `Ai_Mon_SnowMountain_BossSkoll_Atk` · `Ai_Mon_SnowMountain_BossSkoll_AuraBlade` · `Ai_Mon_SnowMountain_BossSkoll_AuraBladeRain` · `Ai_Mon_SnowMountain_BossSkoll_AuraBladeRain_Instance` · `Ai_Mon_SnowMountain_BossSkoll_AuraBladeSpawner` · `Ai_Mon_SnowMountain_BossSkoll_AuraExplosion_Spawner` · `Ai_Mon_SnowMountain_BossSkoll_AuraSlice` · `Ai_Mon_SnowMountain_BossSkoll_Capture` · `Ai_Mon_SnowMountain_BossSkoll_DeathFromAbove` · `Ai_Mon_SnowMountain_BossSkoll_SummonArrow_Instance` · `Ai_Mon_SnowMountain_BossSkoll_SummonArrow_Spawner` · `Ai_Mon_SnowMountain_BossSkoll_Sword` · `Ai_Mon_SnowMountain_BossSkoll_Whirlwind` · `Ai_Mon_SnowMountain_IceElemental_DoubleSwipe` · `Ai_Mon_SnowMountain_IceElemental_MiniBossAtkFlavour` · `Ai_Mon_SnowMountain_LivingShards_Atk` · `Ai_Mon_SnowMountain_Scavenger_Atk` · `Ai_Mon_SnowMountain_Scavenger_Jump` · `Ai_Mon_SnowMountain_Scavenger_Throw` · `Ai_Mon_SnowMountain_VikingWarrior_Atk` · `Ai_Mon_SnowMountain_VikingWarrior_SpawnSword` · `Ai_Mon_SnowMountain_VikingWarrior_Sword` · `Ai_Mon_SnowMountain_VikingWarrior_ThrowShield` · `Ai_Mon_Special_AmbushSpawner_Projectile` · `Ai_Mon_Special_AmbushSpawner_Spawn` · `Ai_Mon_Special_BossErebos_AntiGravity_Instance` · `Ai_Mon_Special_BossErebos_AntiGravity_Spawner` · `Ai_Mon_Special_BossErebos_AtkInstance` · `Ai_Mon_Special_BossErebos_AtkSpawner` · `Ai_Mon_Special_BossErebos_Gaze_Instance` · `Ai_Mon_Special_BossErebos_Gaze_Spawner` · `Ai_Mon_Special_BossErebos_Meteor` · `Ai_Mon_Special_BossErebos_Ripple` · `Ai_Mon_Special_BossErebos_SpawnBlackhole` · `Ai_Mon_Special_BossErebos_SpawnBlackhole_Instance` · `Ai_Mon_Special_BossErebos_SpawnTormentor_Attacker` · `Ai_Mon_Special_BossErebos_SpawnTormentor_Attacker_Instance` · `Ai_Mon_Special_BossErebos_SpawnTormentor_Slow` · `Ai_Mon_Special_BossErebos_SpawnTormentor_Spawner` · `Ai_Mon_Special_BossErebos_StarRain_Instance` · `Ai_Mon_Special_BossErebos_StarRain_Spawner` · `Ai_Mon_Special_BossErebos_Teleport` · `Ai_Mon_Special_BossErebos_Teleport_Instance` · `Ai_Mon_Special_BossLightElemental_Beam` · `Ai_Mon_Special_BossLightElemental_BeamAtk_Spawner` · `Ai_Mon_Special_BossLightElemental_BeamBarrage` · `Ai_Mon_Special_BossLightElemental_Lightning_Spawner` · `Ai_Mon_Special_BossLightElemental_Summon` · `Ai_Mon_Special_BossMaw_AnnihilationStance` · `Ai_Mon_Special_BossMaw_AnnihilationStance_Instance` · `Ai_Mon_Special_BossMaw_Atk` · `Ai_Mon_Special_BossMaw_Cataclysm_Meteor` · `Ai_Mon_Special_BossMaw_Cataclysm_Spawner` · `Ai_Mon_Special_BossMaw_ChainReaction` · `Ai_Mon_Special_BossMaw_ChainReaction_Instance` · `Ai_Mon_Special_BossMaw_Chomp_Charge` · `Ai_Mon_Special_BossMaw_Chomp_DashAtk` · `Ai_Mon_Special_BossMaw_DarkSpear` · `Ai_Mon_Special_BossMaw_MoonlightPact` · `Ai_Mon_Special_BossMaw_MoonlightPact_Atk` · `Ai_Mon_Special_BossMaw_PillarOfFlame_Projectile` · `Ai_Mon_Special_BossMaw_PillarOfFlame_Spawner` · `Ai_Mon_Special_BossMaw_PrecisionShot` · `Ai_Mon_Special_BossMaw_PrecisionShot_Projectile` · `Ai_Mon_Special_BossMaw_Purgatory_Heal` · `Ai_Mon_Special_BossMaw_Purgatory_Instance` · `Ai_Mon_Special_BossMaw_Purgatory_Spawner` · `Ai_Mon_Special_BossMaw_Purgatory_Trap` · `Ai_Mon_Special_BossMaw_ScatterShot_ShortProjectile` · `Ai_Mon_Special_BossMaw_ScatterShot_Spawner` · `Ai_Mon_Special_BossMaw_ShadowOverdrive_Projectile` · `Ai_Mon_Special_BossMaw_ShadowWalk` · `Ai_Mon_Special_BossMaw_ShadowWalk_Projectile` · `Ai_Mon_Special_BossMaw_SliceThroat` · `Ai_Mon_Special_BossMaw_SliceThroat_Atk` · `Ai_Mon_Special_BossObliviax_Artillery` · `Ai_Mon_Special_BossObliviax_Artillery_Instance` · `Ai_Mon_Special_BossObliviax_Atk` · `Ai_Mon_Special_BossObliviax_BackStep` · `Ai_Mon_Special_BossObliviax_BackStep_Instance` · `Ai_Mon_Special_BossObliviax_ChainAtk` · `Ai_Mon_Special_BossObliviax_ChargeSequence_GroundExplosion` · `Ai_Mon_Special_BossObliviax_ChargeSequence_MissileAtk` · `Ai_Mon_Special_BossObliviax_ChargeSequence_Ready` · `Ai_Mon_Special_BossObliviax_ChargeSequence_Spawner` · `Ai_Mon_Special_BossObliviax_DashAtk` · `Ai_Mon_Special_BossObliviax_DashAtk_ExtraAtk` · `Ai_Mon_Special_BossObliviax_DashAtk_Spawner` · `Ai_Mon_Special_BossObliviax_Laugh` · `Ai_Mon_Special_BossObliviax_NeedleAtk` · `Ai_Mon_Special_BossObliviax_NeedleAtk_AtkInstance` · `Ai_Mon_Special_BossObliviax_NeedleAtk_Ready` · `Ai_Mon_Special_BossObliviax_ShadowWalk` · `Ai_Mon_Special_BossObliviax_TurnAtk` · `Ai_Mon_Special_BossObliviax_TurnAtk_DelayedAtk` · `Ai_Mon_Special_BossObliviax_TurnAtk_Projectile` · `Ai_Mon_Special_BossObliviax_TurretMode` · `Ai_Mon_Special_BossObliviax_TurretMode_Projectile` · `Ai_Mon_Special_BossPolaris_Holy_Atk_Explosion` · `Ai_Mon_Special_BossPolaris_Holy_Atk_Projectile` · `Ai_Mon_Special_BossPolaris_Holy_Atk_Spawner` · `Ai_Mon_Special_BossPolaris_Holy_Beam_GravityPull` · `Ai_Mon_Special_BossPolaris_Holy_CounterSpell_DisarmProjectile` · `Ai_Mon_Special_BossPolaris_Holy_GoldenSpear_Projectile` · `Ai_Mon_Special_BossPolaris_Holy_GoldenSpear_Spawner` · `Ai_Mon_Special_BossPolaris_Holy_Purgatory_BurningFloor` · `Ai_Mon_Special_BossPolaris_Holy_Purgatory_Instance` · `Ai_Mon_Special_BossPolaris_Holy_Purgatory_Spawner` · `Ai_Mon_Special_BossPolaris_Holy_RainFire` · `Ai_Mon_Special_BossPolaris_Holy_RainFire_Damage` · `Ai_Mon_Special_BossPolaris_Holy_ScatterFire` · `Ai_Mon_Special_BossPolaris_Holy_SelfCleanse` · `Ai_Mon_Special_BossPolaris_Holy_Summon` · `Ai_Mon_Special_BossPolaris_Monster_Atk_FirstAtk` · `Ai_Mon_Special_BossPolaris_Monster_Atk_SecondAtk` · `Ai_Mon_Special_BossPolaris_Monster_Atk_Spawner` · `Ai_Mon_Special_BossPolaris_Monster_Dash` · `Ai_Mon_Special_BossPolaris_Monster_JumpStomp` · `Ai_Mon_Special_BossPolaris_Monster_JumpStomp_Explosion` · `Ai_Mon_Special_BossPolaris_Monster_PizzaLightning_Instance` · `Ai_Mon_Special_BossPolaris_Monster_PizzaLightning_Spawner` · `Ai_Mon_Special_BossPolaris_Monster_Scream` · `Ai_Mon_Special_BossPolaris_Monster_SlashDash` · `Ai_Mon_Special_BossPolaris_Monster_Smite_Instance` · `Ai_Mon_Special_BossPolaris_Monster_Smite_Spawner` · `Ai_MorasDomain_MorasCreation_Boss_Move` · `Ai_MorasDomain_MorasCreation_Boss_SpawnSwarm` · `Ai_Prop_Merchant_Flee` · `Ai_QR_DistortedMind_Spawner` · `Ai_QR_InfernalTales` · `Ai_QR_Innocence_Projectile` · `Ai_QR_Innocence_Spawner` · `Ai_QR_TwistedTales_Spawner` · `Ai_QR_ValiantHeart` · `Ai_Q_BigBorealChunk_Explosion` · `Ai_Q_BigBorealChunk_Projectile` · `Ai_Q_BigBorealChunk_Spawner` · `Ai_Q_CruelSun` · `Ai_Q_CruelSun_Shockwave` · `Ai_Q_DeathMark_Projectile` · `Ai_Q_Discipline_Stomp` · `Ai_Q_EmbracingTheChill_AreaDoT` · `Ai_Q_EmbracingTheChill_Explosion` · `Ai_Q_EtherealInfluence` · `Ai_Q_EtherealInfluence_Projectile_Base` · `Ai_Q_EtherealInfluence_Projectile_Forward` · `Ai_Q_Fleche_Dash` · `Ai_Q_GoldenBurst` · `Ai_Q_HandCannon` · `Ai_Q_IncendiaryRounds_Attack` · `Ai_Q_Laceration_Circle` · `Ai_Q_Laceration_Dash` · `Ai_Q_Lunge` · `Ai_Q_MoonlightPact` · `Ai_Q_MoonlightPact_Fenrir_Atk` · `Ai_Q_MoonlightPact_Land` · `Ai_Q_Reduction_Projectile` · `Ai_Q_Reduction_Spawner` · `Ai_Q_Riposte` · `Ai_Q_SuperNova` · `Ai_Q_SuperNova_Activate` · `Ai_Q_SylvanCall` · `Ai_Q_SylvanCall_LeafHound_Atk` · `Ai_R_AnnihilationStance_Projectile` · `Ai_R_BackOff_Damage` · `Ai_R_BackOff_Spawner` · `Ai_R_BaptismOfSun` · `Ai_R_BlackArbalest` · `Ai_R_BladeFan` · `Ai_R_Cataclysm_Activate` · `Ai_R_Cataclysm_Meteor` · `Ai_R_ChainReaction` · `Ai_R_Chomp` · `Ai_R_DancingBlades` · `Ai_R_DarkGrenade_Shard` · `Ai_R_DarkGrenade_ShardSpawner` · `Ai_R_Frostbite_Freeze` · `Ai_R_FrozenFists_Attack` · `Ai_R_FrozenFists_PunchDash` · `Ai_R_GlacialHammer` · `Ai_R_GreatFrostSword` · `Ai_R_Ignite` · `Ai_R_Immolation_Damage` · `Ai_R_Inspire_Roar` · `Ai_R_Lava_LavaField` · `Ai_R_NaturesWhisper` · `Ai_R_OrbOfLight_BackwardHealing` · `Ai_R_OrbOfLight_ForwardDamaging` · `Ai_R_Parry_Projectile` · `Ai_R_PhantomBlade` · `Ai_R_PhaseShift` · `Ai_R_PillarOfFlame` · `Ai_R_PrecisionShot` · `Ai_R_PrecisionShot_Projectile` · `Ai_R_QuickTrigger` · `Ai_R_QuickTrigger_Projectile` · `Ai_R_RepulsiveShield_Projectile` · `Ai_R_SanctuaryOfEl_Ground` · `Ai_R_Scattershot_Projectile` · `Ai_R_Scattershot_Spawner` · `Ai_R_SerpentineBlessing` · `Ai_R_SerpentineBlessing_Projectile` · `Ai_R_ShadowOverdrive_Projectile` · `Ai_R_ShadowWalk` · `Ai_R_ShadowWalk_Projectile` · `Ai_R_Smite` · `Ai_R_Somersault` · `Ai_R_StaticDischarge` · `Ai_R_SummonLittleBaam` · `Ai_R_SummonLittleBaam_Baam_Atk` · `Ai_R_UnbreakableDetermination_SubExplosion` · `Ai_RegenOrb_Projectile` · `Ai_ReviveHero` · `Ai_RoomMod_InkStrikeWarning_Artillery` · `Ai_RoomMod_MeteoricLife_Explosion` · `Ai_Shrine_MawOfDoom_DestroyTarget` · `Ai_Shrine_SmallSoul_Attack` · `Ai_Sky_BossIntruder_Instance` · `Ai_Star_Aurena_F_CR_ChargedCast_InstanceCharger` · `Ai_Star_Bismuth_D_BonusAttackEffect_Arrow` · `Ai_Star_Bismuth_F_IT_SmallerRingAddDisplacement_Dash` · `Ai_Star_Cetus_F_BA_LightningEcho_Lightning` · `Ai_Star_Cetus_F_BI_SelfDamageAoeCold_AOE` · `Ai_Star_Mist_F_LG_ChainAttack_Phantom` · `Ai_Star_Yubar_F_EI_DashNoProjectile_Dash` · `Ai_Star_Yubar_F_SN_Pull` · `Ai_U_BeamOfBalance_Beam` · `Ai_U_BigChomp` · `Ai_U_Burrow_Emerge` · `Ai_U_Hysteria_Claw` · `Ai_U_ShoutOfOblivion` · `Ai_U_WorldCracker` · `Ai_UnstableRatSwarm_Projectile` · `Ai_VeilOfDark` · `At_Atk_HuskSword` · `At_Atk_LacertaRifle` · `At_Atk_YubarStardust` · `At_Mon_DarkCave_BossSeeker_GreenChaserOrb` · `At_Mon_DarkCave_DarkElemental_Atk` · `At_Mon_Despair_ParalyticFly_Atk` · `At_Mon_Forest_BossDemon_AltSkill` · `At_Mon_Forest_BossDemon_MainSkill` · `At_Mon_Forest_SpiderSpitter_Atk` · `At_Mon_Forest_SpiderSpitter_Melee` · `At_Mon_LavaLand_InfernoSpider_LavaAtk` · `At_Mon_Sky_BigBaam_BeamAtk` · `At_Mon_Sky_StarSeed_SelfDestruct` · `At_Mon_Special_BossPolaris_Monster_PizzaLightning` · [AttackProjectile](/api/Global.AttackProjectile) · [AttackTrigger](/api/Global.AttackTrigger) · [CurseStatusEffect](/api/Global.CurseStatusEffect) · [DamageInstance](/api/Global.DamageInstance) · [DashAttackInstance](/api/Global.DashAttackInstance) · [Dew](/api/Global.Dew) · [EventInfoAbilityInstance](/api/Global.EventInfoAbilityInstance) · [EventInfoAttackFired](/api/Global.EventInfoAttackFired) · [EventInfoCast](/api/Global.EventInfoCast) · [EventInfoSkillAbilityInstance](/api/Global.EventInfoSkillAbilityInstance) · [FxSelectiveVisibility](/api/Global.FxSelectiveVisibility) · `GameMod_StarlessPath` · `Gem_E_Fangs` · `Gem_R_Celestial` · `Gem_R_Scorched` · [MeleeAttackInstance](/api/Global.MeleeAttackInstance) · [MockAbilityInstance](/api/Global.MockAbilityInstance) · [PickupInstance](/api/Global.PickupInstance) · [Projectile](/api/Global.Projectile) · [PunishmentInstance](/api/Global.PunishmentInstance) · `Se_C_CorrosiveTrails_Poisoned` · `Se_C_CorrosiveTrails_Spawner` · `Se_C_Hemorrhage_EmpowerAttack` · `Se_C_IceBlock` · `Se_Curse_AmplifiedPain` · `Se_Curse_AmplifiedPain_AtkSpdReduction` · `Se_Curse_EternalLoop` · `Se_Curse_SilentNight` · `Se_D_AstridsMasterpieceEnGarde` · `Se_D_AstridsMasterpieceEnGarde_Exposed` · `Se_D_AstridsMasterpiecePriorite` · `Se_D_AstridsMasterpiecePriorite_Exposed` · `Se_D_BeautifulThreat` · `Se_D_ChargedAnguillian` · `Se_D_CircleOfLife_Summon` · `Se_D_ConvergencePoint` · `Se_D_DoubleTap` · `Se_D_ExoticMatter` · `Se_D_IcyVeins` · `Se_D_MercyOfEl` · `Se_D_ParryMaster_Buff` · `Se_D_PrismaticEyes` · `Se_D_QuartetOfDeath_DeathMark` · `Se_D_Resolve` · `Se_D_TheKillingFlow` · `Se_E_Aftershock_Armor` · `Se_E_CrimsonLance_BossDrop` · `Se_E_FinalExplosion` · `Se_E_Harvest_OnVictim` · `Se_E_LizardlyBlessing` · `Se_E_Permafrost_Shield` · `Se_E_Rewind` · `Se_E_Rewind_Damage` · `Se_E_UmbralEdge` · `Se_E_VileStrike` · `Se_Elm_Cold` · `Se_EngulfedInFlame` · `Se_Gem_C_Love` · `Se_Gem_C_Quicksilver` · `Se_Gem_C_Wind` · `Se_Gem_E_Apathy_Armor` · `Se_Gem_E_Fever_LivingBomb` · `Se_Gem_E_Insight_Buff` · `Se_Gem_E_Protection` · `Se_Gem_E_Reflex_ArmorBonus` · `Se_Gem_L_Liberty_Buff` · `Se_Gem_R_Control_Debuff` · `Se_Gem_R_Epiphany_ApBuff` · `Se_Gem_R_Hedgehog_Aura` · `Se_Gem_R_Insatiable` · `Se_Gem_R_Panic` · `Se_Gem_R_Wound_Wounded` · `Se_Gem_Regeneration` · `Se_GenericRevealed` · `Se_GenericStealth` · `Se_HarmlessWhispers` · `Se_HunterBuff_ShadowWalk_Disappear` · `Se_L_ButchersStrike_KillTimer` · `Se_L_MentalCorruption` · `Se_L_Multishot_Buff` · `Se_L_PyranasFireball` · `Se_L_SmallMoltenCore_EmpowerAtk` · `Se_LimboBossDecorator` · `Se_M_Charge` · `Se_M_Flicker` · `Se_M_Sprint` · `Se_MiniBoss_BloodThorn_Bleeding` · `Se_MiniBoss_IceAura` · `Se_MiniBoss_OrbSpitter` · `Se_MiniBoss_UnstableExplosive_Explosion` · `Se_MirageSkin_Sanctification_Protected` · `Se_Mon_DarkCave_BossSeeker_Blink` · `Se_Mon_DarkCave_BossSeeker_Substitution` · `Se_Mon_DarkCave_BossSeeker_TunnelVision` · `Se_Mon_DarkCave_BossSeeker_TunnelVision_PlayerLight` · `Se_Mon_DarkCave_DarkElemental_Teleport` · `Se_Mon_Despair_BossAzurak_RoarAtk_SafeZone` · `Se_Mon_Despair_BossAzurak_RoarAtk_SafeZoneSpawner` · `Se_Mon_Despair_ParalyticFly_Atk_Instance` · `Se_Mon_Forest_Treant_Rage` · `Se_Mon_Ink_BossWhiteNight_Cataclysm` · `Se_Mon_Ink_BossWhiteNight_Rush` · `Se_Mon_LavaLand_BossInfernus_InvulShield` · `Se_Mon_Polaris_Blink` · `Se_Mon_Primus_BossPrimusAeron_Adapt_Doom_Initial` · `Se_Mon_Primus_BossPrimusAeron_Adapt_Doom_Ongoing` · `Se_Mon_Primus_BossPrimusAeron_Force_GoldRain` · `Se_Mon_Primus_BossPrimusAeron_Force_GoldRain_Disappear` · `Se_Mon_Sky_BossNyx_StarBuff` · `Se_Mon_SnowMountain_BossSkoll_DeathFromAbove_Invulnerable` · `Se_Mon_SnowMountain_SnowWolf_SlowApproach` · `Se_Mon_SnowMountain_VikingWarrior_DmgReducer` · `Se_Mon_Special_BossMaw_Cataclysm` · `Se_Mon_Special_BossPolaris_Holy_CounterSpell` · `Se_Mon_Special_BossPolaris_Holy_Dash` · `Se_QR_ValiantHeart_Speed` · `Se_Q_CruelSun_Armored` · `Se_Q_DeathMark_Marked` · `Se_Q_Discipline_Jump` · `Se_Q_Fleche_VictimTracker` · `Se_Q_IncendiaryRounds_EmpowerAttacks` · `Se_Q_SuperNova_Slow` · `Se_R_AnnihilationStance` · `Se_R_BackOff_Shielded` · `Se_R_BaptismOfSun_Buff` · `Se_R_BoneCrusher` · `Se_R_BoneCrusher_Kidnapped` · `Se_R_BoneCrusher_UnstoppableAndShield` · `Se_R_Cataclysm` · `Se_R_Composure_Buff` · `Se_R_DangerousTheory` · `Se_R_Deception` · `Se_R_FrozenFists` · `Se_R_Immolation` · `Se_R_Inspire_Buff` · `Se_R_Lava_Debuff` · `Se_R_NaturesWhisper_Buff` · `Se_R_Parry_Start` · `Se_R_RepulsiveShield` · `Se_R_SanctuaryOfEl_Buff` · `Se_R_SerpentineBlessing_Buff` · `Se_R_ShadowOverdrive_AtkSpd` · `Se_R_ShadowOverdrive_Initial` · `Se_R_ShadowWalk_Disappear` · `Se_R_Somersault_CritBonus` · `Se_R_Tranquility` · `Se_R_UnbreakableDetermination` · `Se_RoomMod_InkStrikeWarning_Slow` · `Se_RoomMod_WarpingField_Warp` · `Se_Shrine_Chaos_StatBonus` · `Se_Shrine_SmallSoul` · `Se_Star_Aurena_D_AbilityPower` · `Se_Star_Aurena_D_AtkSpd` · `Se_Star_Aurena_D_AttackDamage` · `Se_Star_Aurena_D_BonusStatOnLowHp` · `Se_Star_Aurena_I_BonusFromStones` · `Se_Star_Aurena_I_GoldEveryZone` · `Se_Star_Aurena_I_GoldOnMerchantDamage` · `Se_Star_Aurena_I_PotionGold` · `Se_Star_Aurena_L_Armor` · `Se_Star_Aurena_L_ArmorOnLowHp` · `Se_Star_Aurena_L_HealAmpOnLowHp` · `Se_Star_Aurena_L_HealAmpWithPenalty` · `Se_Star_Aurena_L_ShareHeal` · `Se_Star_Aurena_L_SpeedOnDamage` · `Se_Star_Bismuth_D_AtkSpd` · `Se_Star_Bismuth_D_AtkSpdFromDismantle` · `Se_Star_Bismuth_D_BonusAttackEffect` · `Se_Star_Bismuth_D_SkillHasteAndAutoCast` · `Se_Star_Bismuth_I_DismantleMemoryDreamDust` · `Se_Star_Bismuth_I_ShopDiscount` · `Se_Star_Bismuth_L_ContinuousSpeed` · `Se_Star_Bismuth_L_DodgeNoDashMoreCharges` · `Se_Star_Cetus_D_AdApUpByBonusHp` · `Se_Star_Cetus_D_ApUpByColdSkillCounts` · `Se_Star_Cetus_D_StackStatsOnTakenDamage` · `Se_Star_Cetus_D_StatsUpWhileShielded` · `Se_Star_Cetus_F_BA_ChargeMsNoShield` · `Se_Star_Cetus_F_BA_LightningEcho` · `Se_Star_Cetus_F_FR_ChangeToUltHitReset` · `Se_Star_Cetus_I_ColdDiscountFireSurcharge` · `Se_Star_Cetus_I_FirstColdGemQualityBoost` · `Se_Star_Cetus_I_GetDreamDustOnBossKill` · `Se_Star_Cetus_L_DodgeCdReductionOnHit` · `Se_Star_Cetus_L_FrostResistAndBuff` · `Se_Star_Cetus_L_HealOnApDamage` · `Se_Star_Cetus_L_IncreaseDealtShield` · `Se_Star_Cetus_L_MaxHpDamagePenalty` · `Se_Star_Cetus_L_ScalingHealth` · `Se_Star_D_AbilityPower` · `Se_Star_D_AttackDamage` · `Se_Star_D_AttackSpeed` · `Se_Star_D_BossDamageAmp` · `Se_Star_D_CritChance` · `Se_Star_D_CritDamage` · `Se_Star_D_CritUpHitDecay` · `Se_Star_D_DamageBonusOnAllElemental` · `Se_Star_D_DarkAmp` · `Se_Star_D_FireAmp` · `Se_Star_D_LightAmp` · `Se_Star_D_LowerADScalingAP` · `Se_Star_D_LowerAPScalingAD` · `Se_Star_D_LowerASHigherAD` · `Se_Star_D_RiftFirstCastDamageUp` · `Se_Star_D_ScalingAbilityPower` · `Se_Star_D_ScalingAttackDamage` · `Se_Star_D_ScalingAttackSpeedWithPenalty` · `Se_Star_D_ShieldDamageAmp` · `Se_Star_D_TempAbilityPower` · `Se_Star_D_TempAttackDamage` · `Se_Star_Husk_D_AttackDamage` · `Se_Star_Husk_D_CritAmp` · `Se_Star_Husk_D_DamageAmpOnLowHpTarget` · `Se_Star_Husk_D_DamageOverTimeCritWithPenalty` · `Se_Star_Husk_D_DarkAttackWithPenalty` · `Se_Star_Husk_D_MovementSkillHaste` · `Se_Star_Husk_D_ScalingAdAndAtkSpd` · `Se_Star_Husk_F_DC_EnhanceMaxStealthTime` · `Se_Star_Husk_F_DC_RecentDamageHoTWhileStealth` · `Se_Star_Husk_F_LA_SingleTargetCooldown` · `Se_Star_Husk_I_BossKillPlatinumCoin` · `Se_Star_Husk_I_ShopIntimidation` · `Se_Star_Husk_L_DodgeChargesAndRangeWithPenalty` · `Se_Star_Husk_L_DodgeCooldownOnKillOrAttack` · `Se_Star_Husk_L_DodgeCooldownOnKillWithEmptyCharges` · `Se_Star_I_AdditionalChaosChance` · `Se_Star_I_DismantleBonus` · `Se_Star_I_DismantleDustToBonusGold` · `Se_Star_I_DismantleReroll` · `Se_Star_I_DreamDustOnKillChance` · `Se_Star_I_ExtraChaosOptionGoldOnUse` · `Se_Star_I_FirstBossGemDrop` · `Se_Star_I_FirstGemUpgrade` · `Se_Star_I_GemOnMiniBossKill` · `Se_Star_I_GoldPerCrit` · `Se_Star_I_GoldRiskAndReturn` · `Se_Star_I_KillGoldBonus` · `Se_Star_I_MawDiscountAndProtection` · `Se_Star_I_MoreShopItems` · `Se_Star_I_MoreShrineItems` · `Se_Star_I_ShopDiscount` · `Se_Star_I_StartGold` · `Se_Star_L_Armor` · `Se_Star_L_ArmorOnTravel` · `Se_Star_L_DamageReductionFromChilled` · `Se_Star_L_DodgeCooldown` · `Se_Star_L_DodgeCooldownOnLowHealth` · `Se_Star_L_ElementalResistance` · `Se_Star_L_HealOnAttack` · `Se_Star_L_HealOnKill` · `Se_Star_L_IgnoreDelusion` · `Se_Star_L_MaxHealth` · `Se_Star_L_MaxHealthUpHealDown` · `Se_Star_L_PeriodicScalingArmor` · `Se_Star_L_PostHitDamageImmune` · `Se_Star_L_PotionChance` · `Se_Star_L_PotionHealAmount` · `Se_Star_L_PotionOnBuyOrSell` · `Se_Star_L_ReceivedHealingAndShieldBonus` · `Se_Star_L_ScalingMaxHealth` · `Se_Star_L_TempArmor` · `Se_Star_Lacerta_D_AbilityPower` · `Se_Star_Lacerta_D_AttackDamage` · `Se_Star_Lacerta_D_AttackRange` · `Se_Star_Lacerta_D_AttackSpeed` · `Se_Star_Lacerta_F_IR_RechargeAmmoAmpBurnDamage` · `Se_Star_Lacerta_I_BonusFromStones` · `Se_Star_Lacerta_I_BossBounty` · `Se_Star_Lacerta_I_ShopDiscount` · `Se_Star_Lacerta_I_ShopMoreItemsWithPenalty` · `Se_Star_Lacerta_L_DodgeCharges` · `Se_Star_Lacerta_L_SpeedAfterDodge` · `Se_Star_Mist_D_AttackDamage` · `Se_Star_Mist_D_BossDamageOnHighHp` · `Se_Star_Mist_D_HunterDamage` · `Se_Star_Mist_D_ScalingAD` · `Se_Star_Mist_I_BonusOnCatPet` · `Se_Star_Mist_I_StartGoldWithPenalty` · `Se_Star_Mist_L_AddedDodgeWithPenalty` · `Se_Star_Mist_L_ArmorWithPenalty` · `Se_Star_Mist_L_DodgeCooldownWithPenalty` · `Se_Star_Mist_L_MovSpeed` · `Se_Star_Mist_L_PotionShield` · `Se_Star_Nachia_D_AbilityPower` · `Se_Star_Nachia_D_CanineLover` · `Se_Star_Nachia_D_SkillHaste` · `Se_Star_Nachia_D_SummonAtkSpd` · `Se_Star_Nachia_F_NW_MovSpeed` · `Se_Star_Nachia_I_ForestKillDreamDust` · `Se_Star_Nachia_I_ForestShopDiscount` · `Se_Star_Nachia_I_SummonKillGold` · `Se_Star_Nachia_L_AllyUnstoppable` · `Se_Star_Nachia_L_HealAndShieldAmp` · `Se_Star_Nachia_L_SelfWaltz` · `Se_Star_Nachia_L_SummonBonus` · `Se_Star_Nachia_L_WaltzArmor` · `Se_Star_Nachia_L_WaltzDurationWithPenalty` · `Se_Star_Vesper_D_ADWithNearbyBurning` · `Se_Star_Vesper_D_AtkSpd` · `Se_Star_Vesper_D_AtkSpdWithPenalty` · `Se_Star_Vesper_D_BossHunterAmpWithPenalty` · `Se_Star_Vesper_D_ConvertAPToAD` · `Se_Star_Vesper_F_BS_ADWithArmor` · `Se_Star_Vesper_F_BS_MovSpd` · `Se_Star_Vesper_F_DP_FarTargetBonus` · `Se_Star_Vesper_I_ShopDiscount` · `Se_Star_Vesper_I_StartGold` · `Se_Star_Vesper_L_Armor` · `Se_Star_Vesper_L_ArmorOnLowHealth` · `Se_Star_Vesper_L_EmpowerDodgeShield` · `Se_Star_Vesper_L_FireResistance` · `Se_Star_Vesper_L_Health` · `Se_Star_Vesper_L_ScalingArmor` · `Se_Star_Vesper_L_ScalingHealth` · `Se_Star_Vesper_L_SlowSpeedMoreHealth` · `Se_Star_Yubar_D_ADAPWithPenalty` · `Se_Star_Yubar_D_APOnDodge` · `Se_Star_Yubar_D_APOnDodge_APBonus` · `Se_Star_Yubar_D_APPerLightSkill` · `Se_Star_Yubar_D_AbilityPower` · `Se_Star_Yubar_D_BonusDamageToLight` · `Se_Star_Yubar_D_ConvertADToAP` · `Se_Star_Yubar_D_ScalingAP` · `Se_Star_Yubar_D_SkillHaste` · `Se_Star_Yubar_F_CC_IncreaseAD` · `Se_Star_Yubar_F_EI_DashNoProjectile` · `Se_Star_Yubar_F_SN_PullEnemy` · `Se_Star_Yubar_I_DisintegrateDreamDust` · `Se_Star_Yubar_I_StarCookie` · `Se_Star_Yubar_L_DodgeChargeWithLongerCooldown` · `Se_Star_Yubar_L_DodgeCooldownWithShorterRange` · `Se_Star_Yubar_L_DodgeRange` · `Se_U_BeamOfBalance` · `Se_U_Burrow` · `Se_U_EternalFlame_Curse` · `Se_U_HerWorld_Blackhole` · `Se_U_Hysteria` · `Se_WaypointTeleport` · `Shrine_Guidance` · [SkillTrigger](/api/Global.SkillTrigger) · `St_C_Whirlwind` · `St_D_ExplosionArtist` · `St_L_HerosReturn` · `St_L_SmallMoltenCore` · `St_QR_InfernalTales` · `St_R_AnnoyingBanner` · `St_U_ShoutOfOblivion` · [StandardProjectile](/api/Global.StandardProjectile) · [StarEffect](/api/Global.StarEffect) · [StatusEffect](/api/Global.StatusEffect) · [Summon](/api/Global.Summon) · [TriggerConfig](/api/Global.TriggerConfig) · `UI_Tooltip_SkillStarDescriber` · `UI_Tooltip_StatusEffectDescription`

### Dependencies (25)

*Types and components that `AbilityInstance` references or depends upon:*

[AbilityTargetValidatorWrapper](/api/Global.AbilityTargetValidatorWrapper) · [AbilityTrigger](/api/Global.AbilityTrigger) · [Actor](/api/Global.Actor) · [ActorCheck](/api/Global.ActorCheck) · `ArrayGetClampedExtensions` · [CastInfo](/api/Global.CastInfo) · [ChargingChannel](/api/Global.ChargingChannel) · [DamageData](/api/Global.DamageData) · [DewNetworkBehaviour](/api/Global.DewNetworkBehaviour) · [Entity](/api/Global.Entity) · [EventInfoKill](/api/Global.EventInfoKill) · [Gem](/api/Global.Gem) · `GraphicsManager` · [HealData](/api/Global.HealData) · [Hero](/api/Global.Hero) · [ManagerBase`1](/api/Global.ManagerBase`1) · [ReactionChain](/api/Global.ReactionChain) · [SafeAction`1](/api/Global.SafeAction`1) · [ScalingValue](/api/Global.ScalingValue) · [SkillTrigger](/api/Global.SkillTrigger) · [StarEffect](/api/Global.StarEffect) · [StarScalingValue](/api/Global.StarScalingValue) · [Summon](/api/Global.Summon) · `TransformGetScenePathExtension` · `Mirror.GeneratedNetworkCode`

### Related Enums (1)

*Enumerations referenced in fields, properties, or method signatures:*

<a href="/enums#savevarflags" class="enum-link" data-tooltip="Default=0 · ApplyAfterCreation=1 · ApplyAfterFrameDelay=2">SaveVarFlags</a>

:::
