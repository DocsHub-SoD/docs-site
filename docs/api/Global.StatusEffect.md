# Class: StatusEffect

- **Category:** <span class="cat-dot" style="--cat-color: #ef4444" data-cat="Combat & Abilities"></span> Combat & Abilities
- **Namespace:** `Global`
- **Assembly:** `Dew.Core.dll`
- **Inheritance / Derived:** [DewNetworkBehaviour](/api/Global.DewNetworkBehaviour) → [Actor](/api/Global.Actor) → [AbilityInstance](/api/Global.AbilityInstance) → [CurseStatusEffect](/api/Global.CurseStatusEffect) → [MiniBossEffect](/api/Global.MiniBossEffect) → [MirageSkinEffect](/api/Global.MirageSkinEffect) → [PersistentStatBonusEffect](/api/Global.PersistentStatBonusEffect) → [StackedStatusEffect](/api/Global.StackedStatusEffect) → [StarEffect](/api/Global.StarEffect)

```csharp
public abstract class StatusEffect : AbilityInstance, ILogicUpdate, ICleanup, ICustomDestroyRoutine
```

## Fields (13)

::: details Click to expand Fields (13)

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`addedMaterials`** | `[BoxGroup("StatusEffect Settings", true, false, 0)] public Material[] addedMaterials` |  |
| **`bottomColor`** | `[BoxGroup("StatusEffect Settings", true, false, 0)] [ShowIf("_showIcon", true)] public Color bottomColor` |  |
| **`endEffectVictim`** | `[BoxGroup("StatusEffect Settings", true, false, 0)] [LabelText("End Effect")] public GameObject endEffectVictim` |  |
| **`HarmfulEffects`** | `public const BasicEffectMask HarmfulEffects = Slow \| Cripple \| Root \| Silence \| Stun \| Blind \| ArmorReduction \| HealReduction` |  |
| **`hideOnWorldHealthBar`** | `[BoxGroup("StatusEffect Settings", true, false, 0)] [ShowIf("_showIcon", true)] [ToggleLeft] public bool hideOnWorldHealthBar` |  |
| **`icon`** | `[BoxGroup("StatusEffect Settings", true, false, 0)] [ShowIf("_showIcon", true)] public Sprite icon` |  |
| **`iconOrder`** | `[BoxGroup("StatusEffect Settings", true, false, 0)] [ShowIf("_showIcon", true)] public int iconOrder` |  |
| **`isBeneficialBuff`** | `[FormerlySerializedAs] [FormerlySerializedAs("isBeneficial")] [BoxGroup("StatusEffect Settings", true, false, 0)] [ToggleLeft] public bool isBeneficialBuff` |  |
| **`isCleansable`** | `[BoxGroup("StatusEffect Settings", true, false, 0)] [ToggleLeft] public bool isCleansable` |  |
| **`isKilledByCrowdControlImmunity`** | `[BoxGroup("StatusEffect Settings", true, false, 0)] [ToggleLeft] public bool isKilledByCrowdControlImmunity` |  |
| **`scaleDurationByTenacity`** | `[BoxGroup("StatusEffect Settings", true, false, 0)] [ToggleLeft] public bool scaleDurationByTenacity` |  |
| **`startEffectVictim`** | `[Title("Effects On Victim", null, TitleAlignments.Left, true, true)] [BoxGroup("StatusEffect Settings", true, false, 0)] [LabelText("Start Effect")] public GameObject startEffectVictim` |  |
| **`topColor`** | `[BoxGroup("StatusEffect Settings", true, false, 0)] [ShowIf("_showIcon", true)] public Color topColor` |  |

:::

## Properties (8)

::: details Click to expand Properties (8)

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`basicEffects`** | `public IReadOnlyList<BasicEffect> basicEffects { get; }` | List of BasicEffects this status effect is applying to the victim entity. Only available on server. |
| **`isDestroyedOnRoomChange`** | `public override bool isDestroyedOnRoomChange { get; }` |  |
| **`maxDuration`** | `public float? maxDuration { get; }` |  |
| **`normalizedDuration`** | `public float? normalizedDuration { get; }` | Normalized remaining duration. Starts on 1.0f and ends on 0.0f. |
| **`numberDisplay`** | `public int? numberDisplay { get; set; }` |  |
| **`remainingDuration`** | `public float? remainingDuration { get; }` |  |
| **`showIcon`** | `public bool showIcon { get; set; }` |  |
| **`victim`** | `[SaveVar] [SaveVar(SaveVarFlags.Default)] public Entity victim { get; }` |  |

:::

## Methods (44)

::: details `ActiveLogicUpdate(float)`

```csharp
protected override void ActiveLogicUpdate(float dt)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `dt` | `float` |  |

:::

::: details `DoAbility(Func&lt;AbilityTrigger, bool&gt;, Func&lt;AbilityTrigger, Action&gt;)`

Do custom action on all matching ability and do custom cleanup. You can invoke the returned action to immediately call cleanup functions to stop the effect.

```csharp
public SafeAction DoAbility(Func<AbilityTrigger, bool> condition, Func<AbilityTrigger, Action> callback)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `condition` | [`System.Func<T, TResult><AbilityTrigger,bool>`](/api/Global.AbilityTrigger) |  |
| `callback` | [`System.Func<T, TResult><AbilityTrigger,System.Action>`](/api/Global.AbilityTrigger) |  |

**Returns:** `SafeAction`

:::

::: details `DoArmorBoost(float)`

ArmorBoost reduces all taken damage.

```csharp
public ArmorBoostEffect DoArmorBoost(float strength)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `strength` | `float` |  |

**Returns:** `ArmorBoostEffect`

:::

::: details `DoArmorReduction(float)`

ArmorReduction increases all taken damage.

```csharp
public ArmorReductionEffect DoArmorReduction(float strength)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `strength` | `float` |  |

**Returns:** `ArmorReductionEffect`

:::

::: details `DoAttackCritical(Action)`

AttackCritical makes the entity's attacks to always do a critical hit.

```csharp
public AttackCriticalEffect DoAttackCritical(Action onUse)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `onUse` | `System.Action` |  |

**Returns:** `AttackCriticalEffect`

:::

::: details `DoAttackEmpower(Action&lt;EventInfoAttackEffect, int&gt;, int, Action)`

Note this will lock the status effect until basic attack instance is destroyed.

```csharp
public AttackEmpowerEffect DoAttackEmpower(Action<EventInfoAttackEffect, int> onAttackEffect, int maxTriggerCount = 2147483647, Action onDepleted = null)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `onAttackEffect` | [`System.Action<T1, T2><EventInfoAttackEffect,int>`](/api/Global.EventInfoAttackEffect) |  |
| `maxTriggerCount` | `int` |  |
| `onDepleted` | `System.Action` |  |

**Returns:** `AttackEmpowerEffect`

:::

::: details `DoAttackOverride(AbilityTrigger, Action)`

AttackOverride replaces the entity's attack AbilityTrigger with something else.This version uses an existing ability trigger.

```csharp
public AttackOverrideEffect DoAttackOverride(AbilityTrigger trigger, Action onUse)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `trigger` | [`AbilityTrigger`](/api/Global.AbilityTrigger) |  |
| `onUse` | `System.Action` |  |

**Returns:** `AttackOverrideEffect`

:::

::: details `DoAttackOverride&lt;T&gt;(Action)`

AttackOverride replaces the entity's attack AbilityTrigger with something else.This version creates a new ability trigger of the given type and automatically disposes after use.

```csharp
public AttackOverrideEffect DoAttackOverride<T>(Action onUse) where T : AbilityTrigger
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `onUse` | `System.Action` |  |
| `` | `T` |  |

**Returns:** `AttackOverrideEffect`

:::

::: details `DoBasicEffect(BasicEffect)`

```csharp
public void DoBasicEffect(BasicEffect eff)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `eff` | [`BasicEffect`](/api/Global.BasicEffect) |  |

:::

::: details `DoBlind()`

Blind makes the entity miss its attacks.

```csharp
public BlindEffect DoBlind()
```

**Returns:** `BlindEffect`

:::

::: details `DoCripple(float)`

Cripple reduces the entity's attack speed.

```csharp
public CrippleEffect DoCripple(float strength)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `strength` | `float` |  |

**Returns:** `CrippleEffect`

:::

::: details `DoDeathInterrupt(Action&lt;EventInfoKill&gt;, int)`

Death Interrupt fires before entity's imminent death.DeathInterrupts with lower priority will be fired/checked earlier.Healing entity by any amount in an interrupt will prevent entity's death.If an interrupt prevents the death, other interrupts will not be fired.Note that interrupts can be ignored byEntity.KillNoInterrupt()

```csharp
public DeathInterruptEffect DoDeathInterrupt(Action<EventInfoKill> onInterrupt, int priority)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `onInterrupt` | [`System.Action<T><EventInfoKill>`](/api/Global.EventInfoKill) |  |
| `priority` | `int` |  |

**Returns:** `DeathInterruptEffect`

:::

::: details `DoFakeMaxHealthEffect(float)`

FakeMaxHealth increases shown max health only in health bars.

```csharp
public FakeMaxHealthEffect DoFakeMaxHealthEffect(float amount)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `amount` | `float` |  |

**Returns:** `FakeMaxHealthEffect`

:::

::: details `DoHaste(float)`

Haste increases the entity's attack speed.

```csharp
public HasteEffect DoHaste(float strength)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `strength` | `float` |  |

**Returns:** `HasteEffect`

:::

::: details `DoInvisible()`

Invisible makes the entity untargetable by targeted abilities and undetectable to enemies. Note this doesn't change the entity's graphical visibility.

```csharp
public InvisibleEffect DoInvisible()
```

**Returns:** `InvisibleEffect`

:::

::: details `DoInvulnerable(Action&lt;EventInfoDamageNegatedByImmunity&gt;)`

Invulnerable makes the entity immune to damage and crowd controls.

```csharp
public InvulnerableEffect DoInvulnerable(Action<EventInfoDamageNegatedByImmunity> onDamageNegated = null)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `onDamageNegated` | [`System.Action<T><EventInfoDamageNegatedByImmunity>`](/api/Global.EventInfoDamageNegatedByImmunity) |  |

**Returns:** `InvulnerableEffect`

:::

::: details `DoProtected(Action&lt;EventInfoDamageNegatedByImmunity&gt;)`

Protected makes the entity immune to damage.

```csharp
public ProtectedEffect DoProtected(Action<EventInfoDamageNegatedByImmunity> onDamageNegated)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `onDamageNegated` | [`System.Action<T><EventInfoDamageNegatedByImmunity>`](/api/Global.EventInfoDamageNegatedByImmunity) |  |

**Returns:** `ProtectedEffect`

:::

::: details `DoRoot()`

Root impairs the entity's movement/movement ability.

```csharp
public RootEffect DoRoot()
```

**Returns:** `RootEffect`

:::

::: details `DoShield(float, Action&lt;EventInfoDamageNegatedByShield&gt;)`

```csharp
public ShieldEffect DoShield(float amount, Action<EventInfoDamageNegatedByShield> onDamageNegated = null)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `amount` | `float` |  |
| `onDamageNegated` | [`System.Action<T><EventInfoDamageNegatedByShield>`](/api/Global.EventInfoDamageNegatedByShield) |  |

**Returns:** `ShieldEffect`

:::

::: details `DoSilence()`

Silence prevents the entity from using abilities.

```csharp
public SilenceEffect DoSilence()
```

**Returns:** `SilenceEffect`

:::

::: details `DoSkill&lt;T&gt;(Action&lt;T&gt;)`

Do custom action on all matching skill. You can invoke the returned action to immediately call cleanup functions to stop the effect.

```csharp
public SafeAction DoSkill<T>(Action<T> callback) where T : SkillTrigger
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `callback` | `System.Action<T>` |  |
| `` | `T` |  |

**Returns:** `SafeAction`

:::

::: details `DoSkill&lt;T&gt;(Func&lt;T, Action&gt;)`

Do custom action on all matching skill and do custom cleanup. You can invoke the returned action to immediately call cleanup functions to stop the effect.

```csharp
public SafeAction DoSkill<T>(Func<T, Action> callback) where T : SkillTrigger
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `callback` | `System.Func<T, TResult><T,System.Action>` |  |
| `` | `T` |  |

**Returns:** `SafeAction`

:::

::: details `DoSlow(float)`

Slow reduces the entity's movement speed.

```csharp
public SlowEffect DoSlow(float strength)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `strength` | `float` |  |

**Returns:** `SlowEffect`

:::

::: details `DoSpeed(float)`

Speed increases the entity's movement speed.

```csharp
public SpeedEffect DoSpeed(float strength)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `strength` | `float` |  |

**Returns:** `SpeedEffect`

:::

::: details `DoStatBonus()`

Do a stat bonus to victim that expires on destruction of this status effect.

```csharp
public StatBonus DoStatBonus()
```

**Returns:** `StatBonus`

:::

::: details `DoStatBonus(StatBonus)`

Do a stat bonus to victim that expires on destruction of this status effect.

```csharp
public StatBonus DoStatBonus(StatBonus bonus)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `bonus` | [`StatBonus`](/api/Global.StatBonus) |  |

**Returns:** `StatBonus`

:::

::: details `DoStun()`

Stun prevents the entity from moving/using abilities/attacking.

```csharp
public StunEffect DoStun()
```

**Returns:** `StunEffect`

:::

::: details `DoUncollidable()`

Uncollidable makes the entity uncollidable by non-targeted projectiles and abilities.

```csharp
public UncollidableEffect DoUncollidable()
```

**Returns:** `UncollidableEffect`

:::

::: details `DoUnstoppable()`

Unstoppable makes the entity immune to crowd controls.

```csharp
public UnstoppableEffect DoUnstoppable()
```

**Returns:** `UnstoppableEffect`

:::

::: details `FrameUpdate()`

```csharp
public override void FrameUpdate()
```

:::

::: details `GetActorReadableName()`

```csharp
public override string GetActorReadableName()
```

**Returns:** `string`

:::

::: details `GetCustomTooltipDescription()`

Called on the local client hovering over the status effect icon.

```csharp
public virtual string GetCustomTooltipDescription()
```

**Returns:** `string`

:::

::: details `GetCustomTooltipName()`

Called on the local client hovering over the status effect icon.

```csharp
public virtual string GetCustomTooltipName()
```

**Returns:** `string`

:::

::: details `HideOnScreenTimer()`

Hide this status effect's timer on the screen of the victim. Has no effect on non-player victim

```csharp
public void HideOnScreenTimer()
```

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

::: details `OnStartServer()`

```csharp
public override void OnStartServer()
```

:::

::: details `ResetTimer()`

Reset a timer set bySetTimerto its initial duration.

```csharp
public void ResetTimer()
```

:::

::: details `SetTimer(float, float)`

Set a timer that kills this status effect on expiration. The timer will update fillAmount automatically.

```csharp
public void SetTimer(float maxDuration, float duration)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `maxDuration` | `float` |  |
| `duration` | `float` |  |

:::

::: details `SetTimer(float)`

Set a timer that kills this status effect on expiration. The timer will update fillAmount automatically.

```csharp
public void SetTimer(float duration)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `duration` | `float` |  |

:::

::: details `ShowOnScreenTimer(string, Color, bool)`

Show this status effect's timer on the screen of the victim. Has no effect on non-player victim

```csharp
public void ShowOnScreenTimer(string customNameKey = null, Color color = default, bool invertValue = false)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `customNameKey` | `string` |  |
| `color` | `UnityEngine.Color` |  |
| `invertValue` | `bool` |  |

:::

::: details `StopAllBasicEffects()`

```csharp
protected void StopAllBasicEffects()
```

:::

::: details `StopBasicEffect(BasicEffect)`

```csharp
protected void StopBasicEffect(BasicEffect eff)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `eff` | [`BasicEffect`](/api/Global.BasicEffect) |  |

:::

::: details `StopTimer()`

```csharp
public void StopTimer()
```

:::


## Architecture & Relationships

::: details Click to expand Architecture & Relationships

### Used By (703)

*Classes and systems that invoke, reference, or depend on `StatusEffect`:*

`ACH_EMBRACE_MORTALITY` · `ACH_EMPRESS_OF_PAIN` · `ACH_PEW_PEW_PEW` · [AbilityTrigger](/api/Global.AbilityTrigger) · [Actor](/api/Global.Actor) · `Ai_ArcticTerritory` · `Ai_C_CorrosiveTrails_Gas` · `Ai_C_FlashFreeze` · `Ai_L_ButchersStrike` · `Ai_MiniBoss_BloodThorn_MainThorn` · `Ai_MiniBoss_BloodThorn_SubThorn` · `Ai_MiniBoss_IceAura_AoE` · `Ai_Mon_Despair_BossAzurak_StompProjectile_Projectile` · `Ai_Mon_Despair_ParalyticFly_Atk` · `Ai_Mon_Primus_BossPrimusAeron_Rage_MassSilence_Instance` · `Ai_Mon_Sky_BigBaam_Main_Root` · `Ai_Mon_Special_BossErebos_SpawnTormentor_Slow` · `Ai_Mon_Special_BossPolaris_Holy_Atk_Explosion` · `Ai_Mon_Special_BossPolaris_Holy_Purgatory_BurningFloor` · `Ai_Mon_Special_BossPolaris_Holy_Purgatory_Instance` · `Ai_Mon_Special_BossPolaris_Holy_RainFire_Damage` · `Ai_Mon_Special_BossPolaris_Holy_ScatterFire` · `Ai_Q_CruelSun` · `Ai_Q_EmbracingTheChill_AreaDoT` · `Ai_Q_Fleche_Dash` · `Ai_Q_SuperNova` · `Ai_R_Lava_LavaField` · `Ai_R_SanctuaryOfEl_Ground` · `Ai_R_SerpentineBlessing` · `Ai_R_StaticDischarge` · `Ai_VeilOfDark` · `At_Mon_Special_BossPolaris_Monster_PizzaLightning` · [BasicEffect](/api/Global.BasicEffect) · [CurseStatusEffect](/api/Global.CurseStatusEffect) · [Dew](/api/Global.Dew) · [EntityStatus](/api/Global.EntityStatus) · [EventInfoShield](/api/Global.EventInfoShield) · [EventInfoStatusEffect](/api/Global.EventInfoStatusEffect) · `EveryZoneStarEffect` · [FxSelectiveVisibility](/api/Global.FxSelectiveVisibility) · `Gem_C_Love` · `Gem_C_Quicksilver` · `Gem_E_Apathy` · `Gem_E_Reflex` · `Gem_R_Composure` · `Gem_R_Control` · `Gem_R_Epiphany` · `Gem_R_Hedgehog` · `Gem_R_Panic` · `Gem_R_Wound` · `Gem_U_EternalFlame` · `HealthThresholdBonusStarEffect` · `LavaLand_IcePlace` · `LucidDream_KindArmadillo` · [MiniBossEffect](/api/Global.MiniBossEffect) · [MirageSkinEffect](/api/Global.MirageSkinEffect) · [PersistentStatBonusEffect](/api/Global.PersistentStatBonusEffect) · `PropEnt_Tutorial_Obstacle` · `PropEnt_VigilanteHaven_Obstacle` · `Quest_KillToLiftCurse` · [RoomMonsters](/api/Global.RoomMonsters) · `Se_AcceleratedTime` · `Se_ArcticTerritory` · `Se_AutoDetectPresence` · `Se_BarrierPassThrough` · `Se_C_CorrosiveTrails_Poisoned` · `Se_C_CorrosiveTrails_Spawner` · `Se_C_FlashFreeze_Root` · `Se_C_Hemorrhage_Bleed` · `Se_C_Hemorrhage_EmpowerAttack` · `Se_C_IceBlock` · `Se_CallOfTheRavenous` · `Se_CorruptedChaos_BasicContainer` · `Se_Curse_AmplifiedPain` · `Se_Curse_AmplifiedPain_AtkSpdReduction` · `Se_Curse_AnchorOfMind` · `Se_Curse_BlissOfIgnorance` · `Se_Curse_BrainFog` · `Se_Curse_DarkUrge` · `Se_Curse_DreamAfflictionHallucinatory` · `Se_Curse_DreamAfflictionInductive` · `Se_Curse_DreamAfflictionParalytic` · `Se_Curse_Electrified` · `Se_Curse_EternalLoop` · `Se_Curse_FateOfGreed` · `Se_Curse_Fragility` · `Se_Curse_FragmentedBeing` · `Se_Curse_GuidingCompass_CripplingAnxiety` · `Se_Curse_IntermittentExplosion` · `Se_Curse_Lethargy` · `Se_Curse_LossOfIdentity` · `Se_Curse_SilentNight` · `Se_Curse_SilentNight_Locked` · `Se_Curse_SoftSkin` · `Se_Curse_UnstableEnergy` · `Se_Curse_VainDream` · `Se_D_AstridsMasterpieceEnGarde` · `Se_D_AstridsMasterpieceEnGarde_Exposed` · `Se_D_AstridsMasterpiecePriorite` · `Se_D_AstridsMasterpiecePriorite_Exposed` · `Se_D_BeautifulThreat` · `Se_D_BurningFist_EmpowerAttack` · `Se_D_ChargedAnguillian` · `Se_D_CircleOfLife_Summon` · `Se_D_ConvergencePoint` · `Se_D_CrystalsInOrbit` · `Se_D_DoubleTap` · `Se_D_ExoticMatter` · `Se_D_FrostTouch_EmpowerAttacks` · `Se_D_HeartOfThePack_Bond` · `Se_D_IceColdPresence` · `Se_D_IceColdPresence_PersistentBuff` · `Se_D_IcyVeins` · `Se_D_MasterOfAssassination` · `Se_D_MasterOfAssassination_DoT` · `Se_D_MasterOfAssassination_Exposed` · `Se_D_MercyOfEl` · `Se_D_ParryMaster_Buff` · `Se_D_PrismaticEyes` · `Se_D_QuartetOfDeath_Buff` · `Se_D_QuartetOfDeath_DeathMark` · `Se_D_ReactiveShockwave_Stun` · `Se_D_Resolve` · `Se_D_ScarOfTheWind_NextAtkCrit` · `Se_D_ScarOfTheWind_NextAtkDash` · `Se_D_TheKillingFlow` · `Se_D_TheKillingFlow_Crit` · `Se_D_TrueDuelist` · `Se_D_TrueDuelist_Exposed` · `Se_DarkCondensationZone` · `Se_DistantMemories` · `Se_E_Aftershock_Armor` · `Se_E_ClutchesOfMalice_Root` · `Se_E_CrimsonLance_BossDrop` · `Se_E_FinalExplosion` · `Se_E_Harvest_OnVictim` · `Se_E_LizardlyBlessing` · `Se_E_Permafrost_Shield` · `Se_E_Permafrost_Stun` · `Se_E_Rewind` · `Se_E_Rewind_Damage` · `Se_E_UmbralEdge` · `Se_E_VileStrike` · `Se_Elm_Cold` · `Se_Elm_Dark` · `Se_Elm_Fire` · `Se_Elm_Light` · `Se_EngulfedInFlame` · `Se_FallenStar_MonsterReinforcement` · `Se_FallenStar_WaveringIdentity` · `Se_FatalHitProtection_Interrupt` · `Se_FatalHitProtection_Invulnerable` · `Se_FishScales` · `Se_Gem_C_Love` · `Se_Gem_C_Nap` · `Se_Gem_C_Quicksilver` · `Se_Gem_C_Sharp_ArrowSpawner` · `Se_Gem_C_Wind` · `Se_Gem_E_Apathy_Armor` · `Se_Gem_E_Fever_LivingBomb` · `Se_Gem_E_Insensitivity_BombSpawner` · `Se_Gem_E_Insight_Buff` · `Se_Gem_E_Obsidian_EmpowerAttack` · `Se_Gem_E_Protection` · `Se_Gem_E_Reflex_ArmorBonus` · `Se_Gem_L_Culinary_Stack` · `Se_Gem_L_Infinity` · `Se_Gem_L_Liberty_Buff` · `Se_Gem_R_Control_Debuff` · `Se_Gem_R_Epiphany_ApBuff` · `Se_Gem_R_Frost_Stat` · `Se_Gem_R_Hedgehog_Aura` · `Se_Gem_R_Insatiable` · `Se_Gem_R_Panic` · `Se_Gem_R_Slippery` · `Se_Gem_R_Wound_Wounded` · `Se_Gem_Regeneration` · `Se_Gem_U_SoulPrison_DeathInterrupt` · `Se_GenericEffectContainer` · `Se_GenericHealOverTime` · `Se_GenericRevealed` · `Se_GenericShield_OneShot` · `Se_GenericShield_Stacking` · `Se_GenericStealth` · `Se_GoldEverywhere` · `Se_GravityTraining` · `Se_HarmlessWhispers` · `Se_HarmlessWhispers_GrantShield` · `Se_HealthCost` · `Se_HeroBleedingOut` · `Se_HeroDeathInterrupt` · `Se_HeroInCombatIcon` · `Se_HeroKnockedOut` · `Se_HeroOneShotProtection` · `Se_HunterBuff` · `Se_HunterBuff_ShadowWalk_Disappear` · `Se_InConversation` · `Se_L_ButchersStrike_KillTimer` · `Se_L_HerosReturn_Interrupt` · `Se_L_MentalCorruption` · `Se_L_Multishot_Buff` · `Se_L_PyranasFireball` · `Se_L_SmallMoltenCore_AttackLink` · `Se_L_SmallMoltenCore_EmpowerAtk` · `Se_LimboBossDecorator` · `Se_LingeringAuraOfGuidance` · `Se_M_Charge` · `Se_M_DreamyWaltz_Buff` · `Se_M_Endure` · `Se_M_Flicker` · `Se_M_Sprint` · `Se_MiniBoss_BloodThorn` · `Se_MiniBoss_BloodThorn_Bleeding` · `Se_MiniBoss_BloodThorn_ThornSpawner` · `Se_MiniBoss_IceAura` · `Se_MiniBoss_IceAura_Slow` · `Se_MiniBoss_OrbSpitter` · `Se_MiniBoss_SpinningArrow` · `Se_MiniBoss_UnstableExplosive` · `Se_MiniBoss_UnstableExplosive_Explosion` · `Se_MirageSkin_Delusion` · `Se_MirageSkin_Delusion_Delusional` · `Se_MirageSkin_Oblivion` · `Se_MirageSkin_Oblivion_Silenced` · `Se_MirageSkin_Oppression` · `Se_MirageSkin_Pulverization` · `Se_MirageSkin_Sanctification` · `Se_MirageSkin_Sanctification_Protected` · `Se_Mon_DarkCave_BossSeeker_Blink` · `Se_Mon_DarkCave_BossSeeker_Hallucination` · `Se_Mon_DarkCave_BossSeeker_Hallucination_Disappear` · `Se_Mon_DarkCave_BossSeeker_Substitution` · `Se_Mon_DarkCave_BossSeeker_TunnelVision` · `Se_Mon_DarkCave_BossSeeker_TunnelVision_Disappear` · `Se_Mon_DarkCave_BossSeeker_TunnelVision_PlayerLight` · `Se_Mon_DarkCave_DarkElemental_Teleport` · `Se_Mon_Despair_BossAzurak_Hide` · `Se_Mon_Despair_BossAzurak_RoarAtk_SafeZone` · `Se_Mon_Despair_BossAzurak_RoarAtk_SafeZoneSpawner` · `Se_Mon_Despair_BossAzurak_Roll_DeathInterrupt` · `Se_Mon_Despair_ParalyticFly_Atk_Instance` · `Se_Mon_Despair_ParalyticFly_Paralyze` · `Se_Mon_Forest_Treant_Rage` · `Se_Mon_Ink_BossDarkMoon_Eclipse` · `Se_Mon_Ink_BossDeathInterrupt` · `Se_Mon_Ink_BossWhiteNight_Cataclysm` · `Se_Mon_Ink_BossWhiteNight_Cataclysm_NotSafe` · `Se_Mon_Ink_BossWhiteNight_Rush` · `Se_Mon_Ink_Boss_PhaseChange` · `Se_Mon_Ink_Boss_Rage` · `Se_Mon_Ink_Tiger_Walk` · `Se_Mon_LavaLand_BossInfernus_InvulShield` · `Se_Mon_LavaLand_BossInfernus_Jump_Invul` · `Se_Mon_Polaris_Blink` · `Se_Mon_Polaris_Disappear` · `Se_Mon_Primus_BossPrimusAeron_Adapt_Doom_Initial` · `Se_Mon_Primus_BossPrimusAeron_Adapt_Doom_Ongoing` · `Se_Mon_Primus_BossPrimusAeron_Adapt_IceBlock` · `Se_Mon_Primus_BossPrimusAeron_Adaptation` · `Se_Mon_Primus_BossPrimusAeron_Force_GoldRain` · `Se_Mon_Primus_BossPrimusAeron_Force_GoldRain_Disappear` · `Se_Mon_Primus_BossPrimusAeron_PhaseSwitcher` · `Se_Mon_Primus_BossPrimusAeron_Rage_DecayingShield` · `Se_Mon_Sky_BigBaam_Main_Buff_Buffed` · `Se_Mon_Sky_BigBaam_Main_Root_Rooted` · `Se_Mon_Sky_BigBaam_Main_Root_Slowed` · `Se_Mon_Sky_BossNyx_IntrudeErebos` · `Se_Mon_Sky_BossNyx_PhaseChange` · `Se_Mon_Sky_BossNyx_StarBuff` · `Se_Mon_SnowMountain_BossSkoll_DeathFromAbove_Invulnerable` · `Se_Mon_SnowMountain_SnowWolf_SlowApproach` · `Se_Mon_SnowMountain_VikingWarrior_DmgReducer` · `Se_Mon_Special_BossErebos_PhaseChange` · `Se_Mon_Special_BossErebos_SecondPhase` · `Se_Mon_Special_BossErebos_SpawnTormentor_Slow` · `Se_Mon_Special_BossMaw_Cataclysm` · `Se_Mon_Special_BossMaw_Flee` · `Se_Mon_Special_BossMaw_ShadowOverdrive_Initial` · `Se_Mon_Special_BossMaw_ShadowWalk` · `Se_Mon_Special_BossMaw_ShieldConversion` · `Se_Mon_Special_BossPolaris_Adaptation` · `Se_Mon_Special_BossPolaris_CleansingFlame` · `Se_Mon_Special_BossPolaris_Holy_CounterSpell` · `Se_Mon_Special_BossPolaris_Holy_Dash` · `Se_Mon_Special_BossPolaris_Holy_PhaseShifter` · `Se_Mon_Special_BossPolaris_Holy_ShortInvul` · `Se_Mon_Special_BossPolaris_Monster_CursedDive` · `Se_Mon_Special_BossPolaris_Monster_PizzaLightning_Rage` · `Se_Mon_Special_BossPolaris_Monster_Scream_SkillLocked` · `Se_MonsterSprint` · `Se_MorasDomain_AppearFromGround` · `Se_MorasDomain_MonsterInvulnerability` · `Se_MorasDomain_MorasCreation` · `Se_Nor_ReptilianThirdEye` · `Se_Nor_ReptilianThirdEye_Crit` · `Se_Nor_WindowToTheSoul_SpiritualDominance` · `Se_Nor_WindowToTheSoul_WeaknessRevealed` · `Se_ObliviaxKidnap` · `Se_OntologicalShield` · `Se_Pickup_AbilityPower` · `Se_Pickup_AttackDamage` · `Se_Pickup_Protection` · `Se_Pickup_SkillHaste` · `Se_Pickup_Speed` · `Se_PlayTutorialHeroProtection` · `Se_PolarisHallucination` · `Se_PortalTransition` · `Se_Primus_Pizza_Fly` · `Se_PureDream` · `Se_PureDream_Statue` · `Se_QR_ValiantHeart_Speed` · `Se_Q_CruelSun_Armored` · `Se_Q_DeathMark_Marked` · `Se_Q_Discipline_Jump` · `Se_Q_EtherealInfluence_Root` · `Se_Q_Fleche_VictimTracker` · `Se_Q_GoldenBurst_Wither` · `Se_Q_IncendiaryRounds_EmpowerAttacks` · `Se_Q_MoonlightPact_FlyingFenrir` · `Se_Q_PerfectExecution` · `Se_Q_PerfectExecution_KillTimer` · `Se_Q_Riposte_FastFeet` · `Se_Q_SuperNova_Slow` · `Se_Q_Suppression_Old` · `Se_R_AnnihilationStance` · `Se_R_BackOff_Shielded` · `Se_R_BaptismOfSun_Buff` · `Se_R_BoneCrusher` · `Se_R_BoneCrusher_Kidnapped` · `Se_R_BoneCrusher_UnstoppableAndShield` · `Se_R_Cataclysm` · `Se_R_Composure_Buff` · `Se_R_DangerousTheory` · `Se_R_DarkGrenade_Stun` · `Se_R_Deception` · `Se_R_Frostbite_EmpowerAttacks` · `Se_R_FrozenFists` · `Se_R_Immolation` · `Se_R_Inspire_Buff` · `Se_R_Lava_Debuff` · `Se_R_LightningDance` · `Se_R_NaturesWhisper_Buff` · `Se_R_NightSky_AtkSpd` · `Se_R_Parry_End` · `Se_R_Parry_Start` · `Se_R_Rejuvenation_Timer` · `Se_R_RepulsiveShield` · `Se_R_SanctuaryOfEl_Buff` · `Se_R_SerpentineBlessing_Buff` · `Se_R_ShadowOverdrive_AtkSpd` · `Se_R_ShadowOverdrive_Initial` · `Se_R_ShadowWalk_Disappear` · `Se_R_ShadowWalk_EmpowerAttacks` · `Se_R_Somersault_CritBonus` · `Se_R_Tranquility` · `Se_R_UnbreakableDetermination` · `Se_RoomMod_BlackRain` · `Se_RoomMod_InkStrikeWarning_Slow` · `Se_RoomMod_MisticIceVein_Shield` · `Se_RoomMod_Symbiote` · `Se_RoomMod_ToxicArea_Debuff` · `Se_RoomMod_UnstableVeilOfTime_ModifyCooldowns` · `Se_RoomMod_WarpingField_Unstable` · `Se_RoomMod_WarpingField_Warp` · `Se_SantaHat` · `Se_Shrine_Chaos_StatBonus` · `Se_Shrine_Despair_Teleport` · `Se_Shrine_Polaris_Teleporter_Teleport` · `Se_Shrine_SmallSoul` · `Se_Star_Aurena_D_AbilityPower` · `Se_Star_Aurena_D_AtkSpd` · `Se_Star_Aurena_D_AttackDamage` · `Se_Star_Aurena_D_BonusStatOnLowHp` · `Se_Star_Aurena_F_CR_ChargedCast` · `Se_Star_Aurena_F_CR_EarnGold` · `Se_Star_Aurena_F_CR_GlobalHeal` · `Se_Star_Aurena_F_CR_NoHealCooldownReduction` · `Se_Star_Aurena_F_DT_LowerThresholdBiggerHeals` · `Se_Star_Aurena_F_DT_TwiceWithPenalty` · `Se_Star_Aurena_F_DT_UnstoppableAndRemoveDelusion` · `Se_Star_Aurena_F_GB_LessDamageLessSacrifice` · `Se_Star_Aurena_F_GB_NoSacrificeAfterDodge` · `Se_Star_Aurena_F_GB_NoWitherNoSacrifice` · `Se_Star_Aurena_F_RE_AtkEffect` · `Se_Star_Aurena_F_RE_CooldownButNoHeal` · `Se_Star_Aurena_F_RE_MoreProjMoreSacrifice` · `Se_Star_Aurena_I_BonusFromStones` · `Se_Star_Aurena_I_GoldOnMerchantDamage` · `Se_Star_Aurena_I_PotionGold` · `Se_Star_Aurena_L_Armor` · `Se_Star_Aurena_L_ArmorOnLowHp` · `Se_Star_Aurena_L_HealAmpWithPenalty` · `Se_Star_Aurena_L_ShareHeal` · `Se_Star_Aurena_L_SpeedOnDamage` · `Se_Star_Aurena_L_SpeedOnDamage_Speed` · `Se_Star_Bismuth_D_AtkSpd` · `Se_Star_Bismuth_D_AtkSpdFromDismantle` · `Se_Star_Bismuth_D_BonusAttackEffect` · `Se_Star_Bismuth_D_Conquerer` · `Se_Star_Bismuth_D_Conquerer_Stacks` · `Se_Star_Bismuth_D_SkillHasteAndAutoCast` · `Se_Star_Bismuth_F_DM_BonusOnFullCharge` · `Se_Star_Bismuth_F_DM_MoreShootNoMove` · `Se_Star_Bismuth_F_DM_NonFullChargeCooldown` · `Se_Star_Bismuth_F_IN_Elementals` · `Se_Star_Bismuth_F_IN_LessCooldownLessMissiles` · `Se_Star_Bismuth_F_IN_MoreProjByAtkSpd` · `Se_Star_Bismuth_F_IT_AddedDurationOnHit` · `Se_Star_Bismuth_F_IT_InnerDamage` · `Se_Star_Bismuth_F_IT_SmallerRingAddDisplacement` · `Se_Star_Bismuth_F_IT_SmallerRingMoreDamage` · `Se_Star_Bismuth_F_VH_FullCharge` · `Se_Star_Bismuth_F_VH_ResetOnDodge` · `Se_Star_Bismuth_F_VH_Shield` · `Se_Star_Bismuth_I_DismantleMemoryDreamDust` · `Se_Star_Bismuth_I_KnowledgeBook` · `Se_Star_Bismuth_I_SecretJournal` · `Se_Star_Bismuth_I_ShopDiscount` · `Se_Star_Bismuth_I_TreasureWithHealthPenalty` · `Se_Star_Bismuth_L_ContinuousSpeed` · `Se_Star_Bismuth_L_DodgeNoDashMoreCharges` · `Se_Star_Bismuth_L_SecondWindWithPenalty` · `Se_Star_Cetus_D_AdApUpByBonusHp` · `Se_Star_Cetus_D_ApUpByColdSkillCounts` · `Se_Star_Cetus_D_StackStatsOnTakenDamage` · `Se_Star_Cetus_D_StatsUpWhileShielded` · `Se_Star_Cetus_F_BA_CdReductionOnKill` · `Se_Star_Cetus_F_BA_ChargeMsNoShield` · `Se_Star_Cetus_F_BA_LightningEcho` · `Se_Star_Cetus_F_BI_FastChargeTakeDamageUp` · `Se_Star_Cetus_F_BI_MaxChargeTimePerLevel` · `Se_Star_Cetus_F_BI_SelfDamageAoeCold` · `Se_Star_Cetus_F_EM_ChaseTarget` · `Se_Star_Cetus_F_EM_DamageUpSelfDamage` · `Se_Star_Cetus_F_EM_InfiniteDuration` · `Se_Star_Cetus_F_FR_CdReductionOnTakeDamage` · `Se_Star_Cetus_F_FR_ChangeToUltHitReset` · `Se_Star_Cetus_F_FR_RecastCdrNoKnockback` · `Se_Star_Cetus_I_ColdDiscountFireSurcharge` · `Se_Star_Cetus_I_FirstColdGemQualityBoost` · `Se_Star_Cetus_I_GetDreamDustOnBossKill` · `Se_Star_Cetus_I_StartWithResources` · `Se_Star_Cetus_L_ArmorBuffOnShield` · `Se_Star_Cetus_L_ArmorBuffOnShield_Buff` · `Se_Star_Cetus_L_DodgeCdReductionOnHit` · `Se_Star_Cetus_L_FrostResistAndBuff` · `Se_Star_Cetus_L_HealOnApDamage` · `Se_Star_Cetus_L_IncreaseDealtShield` · `Se_Star_Cetus_L_MaxHpDamagePenalty` · `Se_Star_Cetus_L_ScalingHealth` · `Se_Star_D_AbilityPower` · `Se_Star_D_AttackDamage` · `Se_Star_D_AttackSpeed` · `Se_Star_D_BossDamageAmp` · `Se_Star_D_CritChance` · `Se_Star_D_CritDamage` · `Se_Star_D_CritUpHitDecay` · `Se_Star_D_DamageBonusOnAllElemental` · `Se_Star_D_DarkAmp` · `Se_Star_D_FireAmp` · `Se_Star_D_LightAmp` · `Se_Star_D_LowerADScalingAP` · `Se_Star_D_LowerAPScalingAD` · `Se_Star_D_LowerASHigherAD` · `Se_Star_D_RiftFirstCastDamageUp` · `Se_Star_D_ScalingAbilityPower` · `Se_Star_D_ScalingAttackDamage` · `Se_Star_D_ScalingAttackSpeedWithPenalty` · `Se_Star_D_ShieldDamageAmp` · `Se_Star_D_TempAbilityPower` · `Se_Star_D_TempAttackDamage` · `Se_Star_D_UltimateChargeSpeed` · `Se_Star_Husk_D_AttackDamage` · `Se_Star_Husk_D_CritAmp` · `Se_Star_Husk_D_DamageAmpOnLowHpTarget` · `Se_Star_Husk_D_DamageOverTimeCritWithPenalty` · `Se_Star_Husk_D_DamageOverTimeCritWithPenalty_DoT` · `Se_Star_Husk_D_DarkAttackWithPenalty` · `Se_Star_Husk_D_MovementSkillHaste` · `Se_Star_Husk_D_ScalingAdAndAtkSpd` · `Se_Star_Husk_F_AS_AddedDurationOnHit` · `Se_Star_Husk_F_AS_NoShockwaveFasterAttack` · `Se_Star_Husk_F_AS_NonUltimate` · `Se_Star_Husk_F_DC_EndMovespeedToBonusAttackspeed` · `Se_Star_Husk_F_DC_EndMovespeedToBonusAttackspeed_Haste` · `Se_Star_Husk_F_DC_EnhanceMaxStealthTime` · `Se_Star_Husk_F_DC_RecentDamageHoTWhileStealth` · `Se_Star_Husk_F_DE_HighAmpMissReset` · `Se_Star_Husk_F_DE_HitHealMissPenalty` · `Se_Star_Husk_F_DE_MarkHitDodgeCDR` · `Se_Star_Husk_F_LA_BlueFormOnly` · `Se_Star_Husk_F_LA_DodgeResetOnRed` · `Se_Star_Husk_F_LA_QuickBlueForm` · `Se_Star_Husk_F_LA_SingleTargetCooldown` · `Se_Star_Husk_I_BossKillPlatinumCoin` · `Se_Star_Husk_I_ShopIntimidation` · `Se_Star_Husk_L_DodgeChargesAndRangeWithPenalty` · `Se_Star_Husk_L_DodgeCooldownOnKillOrAttack` · `Se_Star_Husk_L_DodgeCooldownOnKillWithEmptyCharges` · `Se_Star_Husk_L_FatalHitProtectionWithPenalty` · `Se_Star_I_AdditionalChaosChance` · `Se_Star_I_DismantleBonus` · `Se_Star_I_DismantleDustToBonusGold` · `Se_Star_I_DismantleReroll` · `Se_Star_I_DreamDustOnKillChance` · `Se_Star_I_ExtraChaosOptionGoldOnUse` · `Se_Star_I_FirstBossGemDrop` · `Se_Star_I_FirstGemUpgrade` · `Se_Star_I_GemOnMiniBossKill` · `Se_Star_I_GoldPerCrit` · `Se_Star_I_GoldRiskAndReturn` · `Se_Star_I_KillGoldBonus` · `Se_Star_I_MawDiscountAndProtection` · `Se_Star_I_MoreShopItems` · `Se_Star_I_MoreShrineItems` · `Se_Star_I_ShopDiscount` · `Se_Star_I_StartGold` · `Se_Star_I_StartSkill` · `Se_Star_L_Armor` · `Se_Star_L_ArmorOnTravel` · `Se_Star_L_DamageReductionFromChilled` · `Se_Star_L_DodgeCooldown` · `Se_Star_L_DodgeCooldownOnLowHealth` · `Se_Star_L_ElementalResistance` · `Se_Star_L_FatalHitProtection` · `Se_Star_L_HealOnAttack` · `Se_Star_L_HealOnKill` · `Se_Star_L_IgnoreDelusion` · `Se_Star_L_IncreaseMaxHealthByGuidance` · `Se_Star_L_MaxHealth` · `Se_Star_L_MaxHealthUpHealDown` · `Se_Star_L_PeriodicScalingArmor` · `Se_Star_L_PostHitDamageImmune` · `Se_Star_L_PostHitDamageImmune_Protected` · `Se_Star_L_PotionChance` · `Se_Star_L_PotionHealAmount` · `Se_Star_L_PotionOnBuyOrSell` · `Se_Star_L_ReceivedHealingAndShieldBonus` · `Se_Star_L_ScalingMaxHealth` · `Se_Star_L_TempArmor` · `Se_Star_Lacerta_D_AbilityPower` · `Se_Star_Lacerta_D_AttackDamage` · `Se_Star_Lacerta_D_AttackRange` · `Se_Star_Lacerta_D_AttackSpeed` · `Se_Star_Lacerta_F_HC_KnockbackAndSlow` · `Se_Star_Lacerta_F_HC_NearDamage` · `Se_Star_Lacerta_F_HC_NoDelayDoubleCast` · `Se_Star_Lacerta_F_HC_ResetOnDodge` · `Se_Star_Lacerta_F_IR_AoEDamage` · `Se_Star_Lacerta_F_IR_MoreShots` · `Se_Star_Lacerta_F_IR_RechargeAmmoAmpBurnDamage` · `Se_Star_Lacerta_F_PS_ChargeSpeed` · `Se_Star_Lacerta_F_PS_CooldownReset` · `Se_Star_Lacerta_F_PS_SlowerStronger` · `Se_Star_Lacerta_F_QT_AddedCharges` · `Se_Star_Lacerta_F_QT_AttackEffect` · `Se_Star_Lacerta_F_QT_RapidFire` · `Se_Star_Lacerta_I_BonusFromStones` · `Se_Star_Lacerta_I_BossBounty` · `Se_Star_Lacerta_I_ShopDiscount` · `Se_Star_Lacerta_I_ShopMoreItemsWithPenalty` · `Se_Star_Lacerta_L_DodgeCharges` · `Se_Star_Lacerta_L_SpeedAfterDodge` · `Se_Star_Mist_D_AttackDamage` · `Se_Star_Mist_D_BonusOnDash` · `Se_Star_Mist_D_BossDamageOnHighHp` · `Se_Star_Mist_D_HunterDamage` · `Se_Star_Mist_D_ScalingAD` · `Se_Star_Mist_F_FL_DecreasedCooldownAndCharge` · `Se_Star_Mist_F_FL_Lightning` · `Se_Star_Mist_F_FL_MaxRangeExplosion` · `Se_Star_Mist_F_LG_ChainAttack` · `Se_Star_Mist_F_LG_IncreasedCooldownReduction` · `Se_Star_Mist_F_LG_RangeAndSpeed` · `Se_Star_Mist_F_LG_SingleTarget` · `Se_Star_Mist_F_PR_AllDirections` · `Se_Star_Mist_F_PR_PerfectParry` · `Se_Star_Mist_F_PR_ShieldAndCrit` · `Se_Star_Mist_F_UD_ExplosionDamage` · `Se_Star_Mist_F_UD_HealLostHealth` · `Se_Star_Mist_F_UD_NonUltimate` · `Se_Star_Mist_I_BonusOnCatPet` · `Se_Star_Mist_I_CamillasGift` · `Se_Star_Mist_I_StartGoldWithPenalty` · `Se_Star_Mist_L_AddedDodgeWithPenalty` · `Se_Star_Mist_L_ArmorWithPenalty` · `Se_Star_Mist_L_DodgeCooldownWithPenalty` · `Se_Star_Mist_L_MovSpeed` · `Se_Star_Mist_L_PotionShield` · `Se_Star_Mist_L_PotionShield_PersistentShield` · `Se_Star_Nachia_D_AbilityPower` · `Se_Star_Nachia_D_CanineLover` · `Se_Star_Nachia_D_CanineLover_Anger` · `Se_Star_Nachia_D_SkillHaste` · `Se_Star_Nachia_D_SummonAtkSpd` · `Se_Star_Nachia_F_MP_NachiaHeal` · `Se_Star_Nachia_F_MP_NoJump` · `Se_Star_Nachia_F_MP_StrongerFenrirNoCast` · `Se_Star_Nachia_F_NW_LessCooldownLessAtkSpd` · `Se_Star_Nachia_F_NW_MovSpeed` · `Se_Star_Nachia_F_NW_Teleport` · `Se_Star_Nachia_F_SB_DurationBonus` · `Se_Star_Nachia_F_SB_SecondWind` · `Se_Star_Nachia_F_SB_StrongerBuffNoSelf` · `Se_Star_Nachia_F_SC_AtkEffect` · `Se_Star_Nachia_F_SC_AtkSpd` · `Se_Star_Nachia_F_SC_MoreSummons` · `Se_Star_Nachia_F_SC_SummonDmgReduction` · `Se_Star_Nachia_I_ForestKillDreamDust` · `Se_Star_Nachia_I_ForestShopDiscount` · `Se_Star_Nachia_I_SummonKillGold` · `Se_Star_Nachia_L_AllyUnstoppable` · `Se_Star_Nachia_L_HealAndShieldAmp` · `Se_Star_Nachia_L_SelfWaltz` · `Se_Star_Nachia_L_SummonBonus` · `Se_Star_Nachia_L_WaltzArmor` · `Se_Star_Nachia_L_WaltzDurationWithPenalty` · `Se_Star_Vesper_D_ADWithNearbyBurning` · `Se_Star_Vesper_D_AtkSpd` · `Se_Star_Vesper_D_AtkSpdWithPenalty` · `Se_Star_Vesper_D_BossHunterAmpWithPenalty` · `Se_Star_Vesper_D_ConvertAPToAD` · `Se_Star_Vesper_F_BS_ADWithArmor` · `Se_Star_Vesper_F_BS_AddedDurationPerAtk` · `Se_Star_Vesper_F_BS_ExplosionOnEnd` · `Se_Star_Vesper_F_BS_MovSpd` · `Se_Star_Vesper_F_CS_ColdDamage` · `Se_Star_Vesper_F_CS_LingeringBenefits` · `Se_Star_Vesper_F_CS_UnlockMoveWithPenalty` · `Se_Star_Vesper_F_DP_FarTargetBonus` · `Se_Star_Vesper_F_DP_PointCast` · `Se_Star_Vesper_F_DP_SwitchToMelee` · `Se_Star_Vesper_F_SE_FullOffense` · `Se_Star_Vesper_F_SE_Invulnerability` · `Se_Star_Vesper_F_SE_PointCast` · `Se_Star_Vesper_I_ShopDiscount` · `Se_Star_Vesper_I_StartGold` · `Se_Star_Vesper_L_Armor` · `Se_Star_Vesper_L_ArmorOnLowHealth` · `Se_Star_Vesper_L_EmpowerDodgeShield` · `Se_Star_Vesper_L_FireResistance` · `Se_Star_Vesper_L_Health` · `Se_Star_Vesper_L_ScalingArmor` · `Se_Star_Vesper_L_ScalingHealth` · `Se_Star_Vesper_L_SlowSpeedMoreHealth` · `Se_Star_Yubar_D_ADAPWithPenalty` · `Se_Star_Yubar_D_APOnDodge` · `Se_Star_Yubar_D_APOnDodge_APBonus` · `Se_Star_Yubar_D_APPerLightSkill` · `Se_Star_Yubar_D_AbilityPower` · `Se_Star_Yubar_D_BonusDamageToLight` · `Se_Star_Yubar_D_ConvertADToAP` · `Se_Star_Yubar_D_ScalingAP` · `Se_Star_Yubar_D_SkillHaste` · `Se_Star_Yubar_F_CC_DamageOverTime` · `Se_Star_Yubar_F_CC_IncreaseAD` · `Se_Star_Yubar_F_CC_LongerDuration` · `Se_Star_Yubar_F_CC_MeteorPerLightSkill` · `Se_Star_Yubar_F_EI_AutoExplosion` · `Se_Star_Yubar_F_EI_BiggerExplosion` · `Se_Star_Yubar_F_EI_DashNoProjectile` · `Se_Star_Yubar_F_EI_NoRootMoreDamage` · `Se_Star_Yubar_F_SN_Artillery` · `Se_Star_Yubar_F_SN_AutoExplosion` · `Se_Star_Yubar_F_SN_DodgeReset` · `Se_Star_Yubar_F_SN_PullEnemy` · `Se_Star_Yubar_F_TQ_EssenceCooldown` · `Se_Star_Yubar_F_TQ_LowerCooldownNoInvul` · `Se_Star_Yubar_F_TQ_ReducedCooldownAndDuration` · `Se_Star_Yubar_I_DisintegrateDreamDust` · `Se_Star_Yubar_I_MoreDreamDustWithPenalty` · `Se_Star_Yubar_I_StarCookie` · `Se_Star_Yubar_L_DodgeChargeWithLongerCooldown` · `Se_Star_Yubar_L_DodgeCooldownWithShorterRange` · `Se_Star_Yubar_L_DodgeRange` · `Se_StarlessPath_PowerOfGuidance` · `Se_Treasure_BlueElixir_ApBoost` · `Se_Treasure_CrimsonElixir_AdBoost` · `Se_Treasure_FragmentOfDetermination_Interrupt` · `Se_Treasure_FragmentOfDetermination_Invulnerable` · `Se_U_BeamOfBalance` · `Se_U_Burrow` · `Se_U_EternalFlame_Curse` · `Se_U_HerWorld_Blackhole` · `Se_U_Hysteria` · `Se_UsingShortcut` · `Se_VeilOfDark` · `Se_WaypointTeleport` · [ShieldEffect](/api/Global.ShieldEffect) · `St_D_HeartOfThePack` · `St_D_QuartetOfDeath` · `St_D_ScarOfTheWind` · `St_U_ShoutOfOblivion` · [StackedStatusEffect](/api/Global.StackedStatusEffect) · [StarEffect](/api/Global.StarEffect) · `StatusEffectRandomPickupInstance` · [TriggerConfig](/api/Global.TriggerConfig) · `UI_InGame_CurseNotifications` · `UI_InGame_StatusEffectIcons` · `UI_InGame_StatusEffectIcons_Item` · `UI_TooltipManager` · `UI_Tooltip_StatusEffectDescription` · `UI_Tooltip_StatusEffectName`

### Dependencies (46)

*Types and components that `StatusEffect` references or depends upon:*

[AbilityInstance](/api/Global.AbilityInstance) · [AbilityTrigger](/api/Global.AbilityTrigger) · [Actor](/api/Global.Actor) · [ActorCheck](/api/Global.ActorCheck) · [ArmorBoostEffect](/api/Global.ArmorBoostEffect) · [ArmorReductionEffect](/api/Global.ArmorReductionEffect) · [AttackCriticalEffect](/api/Global.AttackCriticalEffect) · [AttackEmpowerEffect](/api/Global.AttackEmpowerEffect) · [AttackOverrideEffect](/api/Global.AttackOverrideEffect) · [BasicEffect](/api/Global.BasicEffect) · [BasicEffectWithStrength](/api/Global.BasicEffectWithStrength) · [BlindEffect](/api/Global.BlindEffect) · [ClientEventManager](/api/Global.ClientEventManager) · [CrippleEffect](/api/Global.CrippleEffect) · [DeathInterruptEffect](/api/Global.DeathInterruptEffect) · [Dew](/api/Global.Dew) · [DewLocalization](/api/Global.DewLocalization) · [DewNetworkBehaviour](/api/Global.DewNetworkBehaviour) · [DewPool](/api/Global.DewPool) · [Entity](/api/Global.Entity) · [EntityAbility](/api/Global.EntityAbility) · [EntityStatus](/api/Global.EntityStatus) · [EntityVisual](/api/Global.EntityVisual) · [FakeMaxHealthEffect](/api/Global.FakeMaxHealthEffect) · [HasteEffect](/api/Global.HasteEffect) · [InvisibleEffect](/api/Global.InvisibleEffect) · [InvulnerableEffect](/api/Global.InvulnerableEffect) · [ListReturnHandle`1](/api/Global.ListReturnHandle`1) · `NetworkReaderWriterExtensions` · [NetworkedManagerBase`1](/api/Global.NetworkedManagerBase`1) · [OnScreenTimerHandle](/api/Global.OnScreenTimerHandle) · [ProtectedEffect](/api/Global.ProtectedEffect) · `RevealEffect` · [RootEffect](/api/Global.RootEffect) · [SafeAction](/api/Global.SafeAction) · [SafeAction`1](/api/Global.SafeAction`1) · [SafeAction`2](/api/Global.SafeAction`2) · [ShieldEffect](/api/Global.ShieldEffect) · [SilenceEffect](/api/Global.SilenceEffect) · [SlowEffect](/api/Global.SlowEffect) · [SpeedEffect](/api/Global.SpeedEffect) · [StatBonus](/api/Global.StatBonus) · [StunEffect](/api/Global.StunEffect) · [UncollidableEffect](/api/Global.UncollidableEffect) · [UnstoppableEffect](/api/Global.UnstoppableEffect) · `UntargetableEffect`

### Related Enums (2)

*Enumerations referenced in fields, properties, or method signatures:*

[`BasicEffectMask`](/enums#basiceffectmask) · [`SaveVarFlags`](/enums#savevarflags)

:::
