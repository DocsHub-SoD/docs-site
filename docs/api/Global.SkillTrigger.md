# Class: SkillTrigger

- **Category:** <span class="cat-dot" style="--cat-color: #ef4444" data-cat="Combat & Abilities"></span> Combat & Abilities
- **Namespace:** `Global`
- **Assembly:** `Dew.Core.dll`
- **Inheritance / Derived:** [DewNetworkBehaviour](/api/Global.DewNetworkBehaviour) → [Actor](/api/Global.Actor) → [AbilityTrigger](/api/Global.AbilityTrigger)

```csharp
public class SkillTrigger : AbilityTrigger, ILogicUpdate, ICleanup, ICustomDestroyRoutine, IInteractable, IItem, IExcludeFromPool
```

## Fields (34)

::: details Click to expand Fields (34)

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`ClientEvent_OnHandOwnerChanged`** | `public SafeAction<Hero, Hero> ClientEvent_OnHandOwnerChanged` |  |
| **`ClientEvent_OnTempOwnerChanged`** | `public SafeAction<DewPlayer, DewPlayer> ClientEvent_OnTempOwnerChanged` |  |
| **`ClientSkillEvent_OnDismantleProgressChanged`** | `public SafeAction<float, float> ClientSkillEvent_OnDismantleProgressChanged` | Called everywhere when dismantle progress changes. |
| **`ClientSkillEvent_OnLevelChange`** | `public SafeAction<int, int> ClientSkillEvent_OnLevelChange` |  |
| **`customSkillHastePerLevel`** | `[BoxGroup("Skill Settings", true, false, 0)] [LabelText("Skill Haste Per Level")] [ShowIf("useCustomSkillHastePerLevel", true)] public float customSkillHastePerLevel` |  |
| **`DisableHeroTypeCheckOnIdentityMemories`** | `public static bool DisableHeroTypeCheckOnIdentityMemories` |  |
| **`DismantleDecayStartTime`** | `public const float DismantleDecayStartTime = 1` |  |
| **`DismantleTapMinInterval`** | `public const float DismantleTapMinInterval = 0.075` |  |
| **`DismantleTapStrength`** | `public const float DismantleTapStrength = 0.4` |  |
| **`endEffect`** | `[LabelText("End Effect (Attached)")] [BoxGroup("Skill Settings", true, false, 0)] public GameObject endEffect` |  |
| **`excludeFromPool`** | `[BoxGroup("Skill Settings", true, false, 0)] public bool excludeFromPool` |  |
| **`isLevelUpEnabled`** | `[BoxGroup("Skill Settings", true, false, 0)] public bool isLevelUpEnabled` |  |
| **`rarity`** | `[BoxGroup("Skill Settings", true, false, 0)] public Rarity rarity` |  |
| **`showFillAmountOnScreen`** | `[BoxGroup("Skill Settings", true, false, 0)] public bool showFillAmountOnScreen` |  |
| **`startEffect`** | `[LabelText("Start Effect (Attached)")] [BoxGroup("Skill Settings", true, false, 0)] public GameObject startEffect` |  |
| **`statBonus`** | `[NonSerialized] public StatBonus statBonus` |  |
| **`tags`** | `[SyncVar] [BoxGroup("Skill Settings", true, false, 0)] public DescriptionTags tags` |  |
| **`type`** | `[SyncVar] [BoxGroup("Skill Settings", true, false, 0)] public SkillType type` |  |
| **`Ult_GlobalChargeMultiplier`** | `public const float Ult_GlobalChargeMultiplier = 0.85` |  |
| **`Ult_OnKillBoss`** | `public const float Ult_OnKillBoss = 42.5` |  |
| **`Ult_OnKillLesser`** | `public const float Ult_OnKillLesser = 0.12750001` |  |
| **`Ult_OnKillMiniBoss`** | `public const float Ult_OnKillMiniBoss = 12.75` |  |
| **`Ult_OnKillNormal`** | `public const float Ult_OnKillNormal = 0.63750005` |  |
| **`Ult_PerDealtAttack`** | `public const float Ult_PerDealtAttack = 0.2125` |  |
| **`Ult_PerDealtDamageBossEnemyHealthRatio`** | `public const float Ult_PerDealtDamageBossEnemyHealthRatio = 25.5` |  |
| **`Ult_PerDealtDamageLesserEnemyHealthRatio`** | `public const float Ult_PerDealtDamageLesserEnemyHealthRatio = 0.12750001` |  |
| **`Ult_PerDealtDamageMiniBossEnemyHealthRatio`** | `public const float Ult_PerDealtDamageMiniBossEnemyHealthRatio = 12.75` |  |
| **`Ult_PerDealtDamageNormalEnemyHealthRatio`** | `public const float Ult_PerDealtDamageNormalEnemyHealthRatio = 0.25500003` |  |
| **`Ult_PerDealtElementalDamage`** | `public const float Ult_PerDealtElementalDamage = 0.0425` |  |
| **`Ult_PerDealtNonElementalDamage`** | `public const float Ult_PerDealtNonElementalDamage = 0.2125` |  |
| **`Ult_PerTakenDamageMyHealthRatio`** | `public const float Ult_PerTakenDamageMyHealthRatio = 25.5` |  |
| **`Ult_PerTakenElementalDamage`** | `public const float Ult_PerTakenElementalDamage = 0.0425` |  |
| **`Ult_PerTakenNonElementalDamage`** | `public const float Ult_PerTakenNonElementalDamage = 0.2125` |  |
| **`useCustomSkillHastePerLevel`** | `[BoxGroup("Skill Settings", true, false, 0)] public bool useCustomSkillHastePerLevel` |  |

:::

## Properties (25)

::: details Click to expand Properties (25)

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`canInteractWithMouse`** | `public bool canInteractWithMouse { get; }` |  |
| **`characterSkillOwner`** | `[SaveVar] [SaveVar(SaveVarFlags.Default)] public string characterSkillOwner { get; set; }` |  |
| **`dismantleProgress`** | `public float dismantleProgress { get; }` |  |
| **`effectiveLevel`** | `public int effectiveLevel { get; }` |  |
| **`focusDistance`** | `public float focusDistance { get; }` |  |
| **`handOwner`** | `public Hero handOwner { get; set; }` |  |
| **`interactPivot`** | `public Transform interactPivot { get; }` |  |
| **`isAnimatingEmbraceNewIdentity`** | `public bool isAnimatingEmbraceNewIdentity { get; set; }` |  |
| **`isCharacterSkill`** | `public bool isCharacterSkill { get; }` |  |
| **`isLocked`** | `public bool isLocked { get; }` | Is this skill locked for local player? |
| **`level`** | `[SaveVar] [SaveVar(SaveVarFlags.Default)] public int level { get; set; }` |  |
| **`mainConfigOriginalCharge`** | `public int mainConfigOriginalCharge { get; }` |  |
| **`maxSellGold`** | `public int maxSellGold { get; set; }` |  |
| **`owner`** | `public Hero owner { get; }` |  |
| **`sbCooldownMultiplier`** | `public float sbCooldownMultiplier { get; }` |  |
| **`sbCooldownMultiplierIgnoreReceiveCooldownReductionFlag`** | `public float sbCooldownMultiplierIgnoreReceiveCooldownReductionFlag { get; }` |  |
| **`sbCooldownOffset`** | `public float sbCooldownOffset { get; }` |  |
| **`sbCooldownOffsetIgnoreReceiveCooldownReductionFlag`** | `public float sbCooldownOffsetIgnoreReceiveCooldownReductionFlag { get; }` |  |
| **`skillHastePerLevel`** | `public float skillHastePerLevel { get; }` |  |
| **`skillType`** | `public HeroSkillLocation skillType { get; }` | Location of this skill trigger if equipped. |
| **`skipStartAnimation`** | `public bool skipStartAnimation { get; set; }` |  |
| **`specialOverlayColor`** | `public Color specialOverlayColor { get; set; }` |  |
| **`statEntity`** | `public Entity statEntity { get; }` |  |
| **`tempOwner`** | `public DewPlayer tempOwner { get; set; }` |  |
| **`worldModel`** | `public ItemWorldModel worldModel { get; }` |  |

:::

## Methods (39)

::: details `AddSkillBonus(SkillBonus)`

```csharp
public SkillBonus AddSkillBonus(SkillBonus bonus)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `bonus` | [`SkillBonus`](/api/Global.SkillBonus) |  |

**Returns:** `SkillBonus`

:::

::: details `Awake()`

```csharp
protected override void Awake()
```

:::

::: details `CanInteract(Entity)`

```csharp
public bool CanInteract(Entity entity)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `entity` | [`Entity`](/api/Global.Entity) |  |

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

::: details `DismantleSkill()`

```csharp
public void DismantleSkill()
```

:::

::: details `GetActorReadableName()`

```csharp
public override string GetActorReadableName()
```

**Returns:** `string`

:::

::: details `GetBuyGold()`

```csharp
public int GetBuyGold()
```

**Returns:** `int`

:::

::: details `GetBuyGold(Rarity, int)`

```csharp
public static int GetBuyGold(Rarity rarity, int level)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `rarity` | <a href="/enums#rarity" class="enum-link" data-tooltip="Common=0 · Rare=1 · Epic=2 · Legendary=3 · Character=4 (+2 more)">Rarity</a> |  |
| `level` | `int` |  |

**Returns:** `int`

:::

::: details `GetCooldownTimeMultiplier(int)`

```csharp
public override float GetCooldownTimeMultiplier(int configIndex)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `configIndex` | `int` |  |

**Returns:** `float`

:::

::: details `GetCooldownTimeOffset(int)`

```csharp
public override float GetCooldownTimeOffset(int configIndex)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `configIndex` | `int` |  |

**Returns:** `float`

:::

::: details `GetCooldownTimeOnLevel(int)`

```csharp
public float GetCooldownTimeOnLevel(int lvl)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `lvl` | `int` |  |

**Returns:** `float`

:::

::: details `GetDismantleAmount(DewPlayer)`

```csharp
public int GetDismantleAmount(DewPlayer player)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `player` | [`DewPlayer`](/api/Global.DewPlayer) |  |

**Returns:** `int`

:::

::: details `GetFormattedSkillTitle()`

```csharp
public string GetFormattedSkillTitle()
```

**Returns:** `string`

:::

::: details `GetGoldValue(Rarity, int)`

```csharp
public static int GetGoldValue(Rarity rarity, int level)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `rarity` | <a href="/enums#rarity" class="enum-link" data-tooltip="Common=0 · Rare=1 · Epic=2 · Legendary=3 · Character=4 (+2 more)">Rarity</a> |  |
| `level` | `int` |  |

**Returns:** `int`

:::

::: details `GetLoadoutHero()`

Get a hero that contains this skill in their loadout.Returns null if this is not from a hero.Note this can be an expensive operation to be calling every frame, since it will iterate through all hero types in the game.

```csharp
public Type GetLoadoutHero()
```

**Returns:** `System.Type`

:::

::: details `GetSellGold()`

```csharp
public int GetSellGold()
```

**Returns:** `int`

:::

::: details `GetSellGold(Rarity, int)`

```csharp
public static int GetSellGold(Rarity rarity, int level)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `rarity` | <a href="/enums#rarity" class="enum-link" data-tooltip="Common=0 · Rare=1 · Epic=2 · Legendary=3 · Character=4 (+2 more)">Rarity</a> |  |
| `level` | `int` |  |

**Returns:** `int`

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

::: details `IsLockedFor(DewPlayer)`

```csharp
public bool IsLockedFor(DewPlayer player)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `player` | [`DewPlayer`](/api/Global.DewPlayer) |  |

**Returns:** `bool`

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

::: details `OnCastComplete(int, CastInfo)`

```csharp
public override AbilityInstance OnCastComplete(int configIndex, CastInfo info)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `configIndex` | `int` |  |
| `info` | [`CastInfo`](/api/Global.CastInfo) |  |

**Returns:** `AbilityInstance`

:::

::: details `OnEquip(Entity)`

```csharp
protected override void OnEquip(Entity newOwner)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `newOwner` | [`Entity`](/api/Global.Entity) |  |

:::

::: details `OnLevelChange(int, int)`

Called everywhere when this skill's level is changed.

```csharp
protected virtual void OnLevelChange(int oldLevel, int newLevel)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `oldLevel` | `int` |  |
| `newLevel` | `int` |  |

:::

::: details `OnPrepare()`

```csharp
protected override void OnPrepare()
```

:::

::: details `OnStartClient()`

```csharp
public override void OnStartClient()
```

:::

::: details `OnStartServer()`

```csharp
public override void OnStartServer()
```

:::

::: details `OnUnequip(Entity)`

```csharp
protected override void OnUnequip(Entity formerOwner)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `formerOwner` | [`Entity`](/api/Global.Entity) |  |

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

::: details `RemoveSkillBonus(SkillBonus)`

```csharp
public void RemoveSkillBonus(SkillBonus bonus)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `bonus` | [`SkillBonus`](/api/Global.SkillBonus) |  |

:::

::: details `RpcSetPositionAndRotation(Vector3, Quaternion)`

```csharp
public void RpcSetPositionAndRotation(Vector3 pos, Quaternion rot)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `pos` | `UnityEngine.Vector3` |  |
| `rot` | `UnityEngine.Quaternion` |  |

:::

::: details `ShouldBeSavedWithRoom()`

```csharp
public override bool ShouldBeSavedWithRoom()
```

**Returns:** `bool`

:::

::: details `ShouldTickCooldown(int)`

```csharp
protected override bool ShouldTickCooldown(int configIndex)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `configIndex` | `int` |  |

**Returns:** `bool`

:::

::: details `UpdateSkillBonus()`

```csharp
public void UpdateSkillBonus()
```

:::


## Architecture & Relationships

::: details Click to expand Architecture & Relationships

### Used By (305)

*Classes and systems that invoke, reference, or depend on `SkillTrigger`:*

`ACH_OMEGA_POINT` · `ACH_THE_EIGHTH_TROPHY` · [AbilityInstance](/api/Global.AbilityInstance) · [AbilityTrigger](/api/Global.AbilityTrigger) · [AchievementManager](/api/Global.AchievementManager) · [Actor](/api/Global.Actor) · `Ai_EmbraceNewIdentity` · `Ai_FirstBonusQualityUpgrader` · `Ai_Mon_Special_BossPolaris_Holy_CounterSpell_DisarmProjectile` · `Ai_RandomGemUpgrade` · `Ai_Shrine_MawOfDoom_DestroyTarget` · [ControlManager](/api/Global.ControlManager) · [Dew](/api/Global.Dew) · [DewLocalization](/api/Global.DewLocalization) · [DewPlayer](/api/Global.DewPlayer) · `DewStarItemOld` · [EditSkillManager](/api/Global.EditSkillManager) · [EditSkillShrine](/api/Global.EditSkillShrine) · [EventInfoSkillAbilityInstance](/api/Global.EventInfoSkillAbilityInstance) · [EventInfoSkillUse](/api/Global.EventInfoSkillUse) · [GameManager](/api/Global.GameManager) · `Ge_CallOfTheRavenous` · [Gem](/api/Global.Gem) · `Gem_C_Confidence` · `Gem_C_Efficiency` · `Gem_C_Guidance` · `Gem_C_Lethality` · `Gem_C_Love` · `Gem_C_Sulfur` · `Gem_C_Vengeance` · `Gem_E_Apathy` · `Gem_E_Blossom` · `Gem_E_Clemency` · `Gem_E_Direness` · `Gem_E_Inversion` · `Gem_E_Might` · `Gem_E_Omega` · `Gem_E_Pain` · `Gem_E_Predation` · `Gem_E_Umbra` · `Gem_E_Virtuousness` · `Gem_L_ChaosApple` · `Gem_L_Culinary` · `Gem_L_DivineFaith` · `Gem_L_Embertail` · `Gem_L_Paranoia` · `Gem_L_SuppressedArcanum` · `Gem_R_Abyss` · `Gem_R_Bleak` · `Gem_R_Contempt` · `Gem_R_Flow` · `Gem_R_Glass` · `Gem_R_Lightweight` · `Gem_R_NightSky` · `Gem_R_Ricochet` · `Gem_R_Rigidity` · `Gem_R_Slippery` · `Gem_R_Wealth` · `Gem_U_EternalFlame` · `Gem_U_GlacialCore` · `Gem_U_LastStarlight` · [HeroSkill](/api/Global.HeroSkill) · `InGameAnalyticsManager` · [InGameUIManager](/api/Global.InGameUIManager) · [LootManager](/api/Global.LootManager) · [PingManager](/api/Global.PingManager) · [PropEnt_Merchant_Base](/api/Global.PropEnt_Merchant_Base) · [PropEnt_Merchant_Jonas](/api/Global.PropEnt_Merchant_Jonas) · `Se_D_IceColdPresence` · `Se_E_Rewind` · `Se_Gem_L_Infinity` · `Se_Gem_R_Panic` · `Se_Mon_Special_BossPolaris_Holy_CounterSpell` · `Se_RoomMod_UnstableVeilOfTime_ModifyCooldowns` · `Se_Star_Bismuth_D_BonusAttackEffect` · `Se_Star_Bismuth_F_IN_MoreProjByAtkSpd` · `Se_Star_Cetus_D_ApUpByColdSkillCounts` · `Se_Star_Cetus_F_BA_CdReductionOnKill` · `Se_Star_Cetus_F_BI_MaxChargeTimePerLevel` · `Se_Star_D_RiftFirstCastDamageUp` · `Se_Star_Husk_D_MovementSkillHaste` · `Se_Star_I_DismantleReroll` · `Se_Star_L_DodgeCooldown` · `Se_Star_L_DodgeCooldownOnLowHealth` · `Se_Star_Lacerta_L_DodgeCharges` · `Se_Star_Mist_F_PR_PerfectParry` · `Se_Star_Mist_F_PR_ShieldAndCrit` · `Se_Star_Mist_L_AddedDodgeWithPenalty` · `Se_Star_Mist_L_DodgeCooldownWithPenalty` · `Se_Star_Yubar_D_APPerLightSkill` · `Se_Star_Yubar_L_DodgeChargeWithLongerCooldown` · `Se_Star_Yubar_L_DodgeCooldownWithShorterRange` · `Shrine_AltarOfCleansing` · `Shrine_Ascension` · `Shrine_BossSoul` · `Shrine_CallOfTheRavenous` · `Shrine_Chaos` · `Shrine_CorruptedChaos` · `Shrine_Entanglement` · `Shrine_FallenStar` · `Shrine_Luck` · `Shrine_MawOfDoom` · `Shrine_Memory` · `Shrine_ScaredMaw` · `Shrine_UpgradeWell` · [SkillBonus](/api/Global.SkillBonus) · `SkillWorldModel` · `St_C_BackStep` · `St_C_BeamOfLight` · `St_C_CorrosiveTrails` · `St_C_DarkBolt` · `St_C_DarkSpear` · `St_C_FlashFreeze` · `St_C_GlacialStomp` · `St_C_Hemorrhage` · `St_C_IceBlock` · `St_C_IceBolt` · `St_C_IceClaw` · `St_C_LuckyHammer` · `St_C_MagicSword` · `St_C_MassProtection` · `St_C_Pew` · `St_C_PressurePoint` · `St_C_Purgatory` · `St_C_ShockTrap` · `St_C_Sneeze` · `St_C_SparklingWaterGun` · `St_C_SpearThrow` · `St_C_Starfall` · `St_C_SwiftSlash` · `St_C_Whirlwind` · `St_D_AstridsMasterpieceEnGarde` · `St_D_AstridsMasterpiecePriorite` · `St_D_BeautifulThreat` · `St_D_BurningFist` · `St_D_ChargedAnguillian` · `St_D_CircleOfLife` · `St_D_ConvergencePoint` · `St_D_CrystalsInOrbit` · `St_D_DanceOfValor` · `St_D_DisintegratingClaw` · `St_D_DoubleTap` · `St_D_ExoticMatter` · `St_D_ExplosionArtist` · `St_D_FrostTouch` · `St_D_HeartOfThePack` · `St_D_IceColdPresence` · `St_D_IcyVeins` · `St_D_MasterOfAssassination` · `St_D_MercyOfEl` · `St_D_MomentumOfCombat` · `St_D_ParryMaster` · `St_D_PrismaticEyes` · `St_D_QuartetOfDeath` · `St_D_ReactiveShockwave` · `St_D_Resolve` · `St_D_RoaringFist` · `St_D_SalamanderPowder` · `St_D_ScarOfTheWind` · `St_D_SharedPain` · `St_D_TheKillingFlow` · `St_D_ThirstOfVengence` · `St_D_TrueDuelist` · `St_E_AntiGravity` · `St_E_Blink` · `St_E_ChainLightning` · `St_E_ClutchesOfMalice` · `St_E_CrimsonLance` · `St_E_DoomsdayMeteor` · `St_E_FinalExplosion` · `St_E_FlameJet` · `St_E_Harvest` · `St_E_JusticeGuillotine` · `St_E_LizardlyBlessing` · `St_E_MassCleanse` · `St_E_MysticDagger` · `St_E_Permafrost` · `St_E_Rewind` · `St_E_SearingCharge` · `St_E_ShadowVolley` · `St_E_SliceThroat` · `St_E_StygianRush` · `St_E_UmbralEdge` · `St_E_VileStrike` · `St_E_WinterDive` · `St_L_Blizzard` · `St_L_ButchersStrike` · `St_L_CoinExplosion` · `St_L_HerosReturn` · `St_L_LightExplosion` · `St_L_MentalCorruption` · `St_L_Multishot` · `St_L_PyranasFireball` · `St_L_SmallMoltenCore` · `St_L_SoulKiller` · `St_L_SpectreBullet` · `St_M_Charge` · `St_M_DreamyWaltz` · `St_M_Endure` · `St_M_FastFeet` · `St_M_FeatheryDash` · `St_M_FlashStep` · `St_M_Flicker` · `St_M_FrostyCharge` · `St_M_IceColdPresence` · `St_M_NimbleDodge` · `St_M_ParryMaster` · `St_M_Sprint` · `St_Nor_CosmicBlast` · `St_Nor_MyOwnLittleNebula` · `St_Nor_ReptilianThirdEye` · `St_Nor_WindowToTheSoul` · `St_QR_DistortedMind` · `St_QR_InfernalTales` · `St_QR_Innocence` · `St_QR_TwistedTales` · `St_QR_ValiantHeart` · `St_Q_BigBorealChunk` · `St_Q_CruelSun` · `St_Q_DeathMark` · `St_Q_Discipline` · `St_Q_EmbracingTheChill` · `St_Q_EtherealInfluence` · `St_Q_Fleche` · `St_Q_GoldenBurst` · `St_Q_HandCannon` · `St_Q_IncendiaryRounds` · `St_Q_Laceration` · `St_Q_Lunge` · `St_Q_MoonlightPact` · `St_Q_PerfectExecution` · `St_Q_Reduction` · `St_Q_Riposte` · `St_Q_SuperNova` · `St_Q_Suppression_Old` · `St_Q_SylvanCall` · `St_R_AnnihilationStance` · `St_R_AnnoyingBanner` · `St_R_BackOff` · `St_R_BaptismOfSun` · `St_R_BlackArbalest` · `St_R_BladeFan` · `St_R_BoneCrusher` · `St_R_Cataclysm` · `St_R_ChainReaction` · `St_R_Chomp` · `St_R_DancingBlades` · `St_R_DangerousTheory` · `St_R_DarkGrenade` · `St_R_Deception` · `St_R_Fireball` · `St_R_FlamingWhip` · `St_R_Frostbite` · `St_R_FrozenFists` · `St_R_GlacialHammer` · `St_R_GreatFrostSword` · `St_R_Ignite` · `St_R_Immolation` · `St_R_Inspire` · `St_R_LightningDance` · `St_R_NaturesWhisper` · `St_R_OrbOfLight` · `St_R_Parry` · `St_R_PhantomBlade` · `St_R_PhaseShift` · `St_R_PillarOfFlame` · `St_R_PrecisionShot` · `St_R_QuickTrigger` · `St_R_RepulsiveShield` · `St_R_SanctuaryOfEl` · `St_R_Scattershot` · `St_R_SerpentineBlessing` · `St_R_ShadowOverdrive` · `St_R_ShadowWalk` · `St_R_Smite` · `St_R_Somersault` · `St_R_StaticDischarge` · `St_R_SummonLittleBaam` · `St_R_Tranquility` · `St_R_UnbreakableDetermination` · `St_R_WarBoomerang` · `St_R_WrathOfEl` · `St_U_BeamOfBalance` · `St_U_BigChomp` · `St_U_Burrow` · `St_U_HerWorld` · `St_U_Hysteria` · `St_U_ShoutOfOblivion` · `St_U_WorldCracker` · [StarEffect](/api/Global.StarEffect) · [Summon](/api/Global.Summon) · `Treasure_SuspiciousHat` · `UI_InGame_Interact_Skill` · `UI_InGame_PartyDisplay_Item` · `UI_InGame_SkillButton` · `UI_InGame_SkillButton_EditSkill` · `UI_InGame_SkillNotifications` · `UI_Lobby_Constellations_Skills_ContextMenu_Item` · `UI_Lobby_Loadout_AvailableSkills_Item` · `UI_TooltipManager` · `UI_Tooltip_ObjLevel` · `UI_Tooltip_SkillCooldown` · `UI_Tooltip_SkillStarDescriber` · `UI_Tooltip_SkillTitle` · [ZoneManager](/api/Global.ZoneManager)

### Dependencies (49)

*Types and components that `SkillTrigger` references or depends upon:*

[AbilityInstance](/api/Global.AbilityInstance) · [AbilityTrigger](/api/Global.AbilityTrigger) · [Actor](/api/Global.Actor) · [ActorCheck](/api/Global.ActorCheck) · [AssetRef`1](/api/Global.AssetRef`1) · [CastInfo](/api/Global.CastInfo) · [ClientEventManager](/api/Global.ClientEventManager) · [DamageData](/api/Global.DamageData) · [DataProcessorGroup`3](/api/Global.DataProcessorGroup`3) · [Dew](/api/Global.Dew) · [DewBuildProfile](/api/Global.DewBuildProfile) · [DewLocalization](/api/Global.DewLocalization) · [DewNetworkBehaviour](/api/Global.DewNetworkBehaviour) · [DewPlayer](/api/Global.DewPlayer) · [DewResources](/api/Global.DewResources) · [Entity](/api/Global.Entity) · [EntityCheck](/api/Global.EntityCheck) · [EntityStatus](/api/Global.EntityStatus) · [EventInfoAttackHit](/api/Global.EventInfoAttackHit) · [EventInfoDamage](/api/Global.EventInfoDamage) · [EventInfoKill](/api/Global.EventInfoKill) · [EventInfoSkillUse](/api/Global.EventInfoSkillUse) · [FeedbackManager](/api/Global.FeedbackManager) · [Formula](/api/Global.Formula) · [GameManager](/api/Global.GameManager) · [HealData](/api/Global.HealData) · [Hero](/api/Global.Hero) · [HeroSkill](/api/Global.HeroSkill) · [IExcludeFromPool](/api/Global.IExcludeFromPool) · [IInteractable](/api/Global.IInteractable) · [IItem](/api/Global.IItem) · [InGameUIManager](/api/Global.InGameUIManager) · `ItemWorldModel` · [ManagerBase`1](/api/Global.ManagerBase`1) · [MessageManager](/api/Global.MessageManager) · `NetworkConnectionToClientExtension` · [NetworkedManagerBase`1](/api/Global.NetworkedManagerBase`1) · [PerRarityData`1](/api/Global.PerRarityData`1) · [PickupManager](/api/Global.PickupManager) · [ResourceLoadSettings](/api/Global.ResourceLoadSettings) · [SafeAction`1](/api/Global.SafeAction`1) · [SafeAction`2](/api/Global.SafeAction`2) · [SafeAction`3](/api/Global.SafeAction`3) · [ScalingValue](/api/Global.ScalingValue) · [SkillBonus](/api/Global.SkillBonus) · `SkillWorldModel` · [StatBonus](/api/Global.StatBonus) · [TriggerConfig](/api/Global.TriggerConfig) · `Mirror.GeneratedNetworkCode`

### Related Enums (5)

*Enumerations referenced in fields, properties, or method signatures:*

<a href="/enums#descriptiontags" class="enum-link" data-tooltip="None=0 · Fire=1 · Cold=2 · Dark=4 · Light=8 (+7 more)">DescriptionTags</a> · <a href="/enums#heroskilllocation" class="enum-link" data-tooltip="Q=0 · W=1 · E=2 · R=3 · Identity=4 (+1 more)">HeroSkillLocation</a> · <a href="/enums#rarity" class="enum-link" data-tooltip="Common=0 · Rare=1 · Epic=2 · Legendary=3 · Character=4 (+2 more)">Rarity</a> · <a href="/enums#savevarflags" class="enum-link" data-tooltip="Default=0 · ApplyAfterCreation=1 · ApplyAfterFrameDelay=2">SaveVarFlags</a> · <a href="/enums#skilltype" class="enum-link" data-tooltip="Normal=0 · Ultimate=1">SkillType</a>

:::
