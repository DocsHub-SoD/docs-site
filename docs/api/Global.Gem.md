# Class: Gem

- **Category:** <span class="cat-dot" style="--cat-color: #ef4444" data-cat="Combat & Abilities"></span> Combat & Abilities
- **Namespace:** `Global`
- **Assembly:** `Dew.Core.dll`
- **Inheritance / Derived:** [DewNetworkBehaviour](/api/Global.DewNetworkBehaviour) → [Actor](/api/Global.Actor)

```csharp
public class Gem : Actor, ILogicUpdate, ICleanup, ICustomDestroyRoutine, IInteractable, IItem, IExcludeFromPool
```

## Fields (26)

::: details Click to expand Fields (26)

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`ClientEvent_OnHandOwnerChanged`** | `public SafeAction<Hero, Hero> ClientEvent_OnHandOwnerChanged` |  |
| **`ClientEvent_OnOwnerChanged`** | `public SafeAction<Hero, Hero> ClientEvent_OnOwnerChanged` |  |
| **`ClientEvent_OnTempOwnerChanged`** | `public SafeAction<DewPlayer, DewPlayer> ClientEvent_OnTempOwnerChanged` |  |
| **`ClientGemEvent_OnCooldownReady`** | `public SafeAction ClientGemEvent_OnCooldownReady` |  |
| **`ClientGemEvent_OnCooldownReduced`** | `public SafeAction<float> ClientGemEvent_OnCooldownReduced` |  |
| **`ClientGemEvent_OnCooldownReducedByRatio`** | `public SafeAction<float> ClientGemEvent_OnCooldownReducedByRatio` |  |
| **`ClientGemEvent_OnCooldownStarted`** | `public SafeAction ClientGemEvent_OnCooldownStarted` |  |
| **`ClientGemEvent_OnFlash`** | `public SafeAction ClientGemEvent_OnFlash` |  |
| **`ClientGemEvent_OnQualityChanged`** | `public SafeAction<int, int> ClientGemEvent_OnQualityChanged` |  |
| **`cooldownTime`** | `[BoxGroup("Gem Settings", true, false, 0)] [ShowIf("isCooldownEnabled", true)] public ScalingValue cooldownTime` |  |
| **`enableStatBonus`** | `[BoxGroup("Gem Settings", true, false, 0)] public bool enableStatBonus` |  |
| **`excludeFromPool`** | `[BoxGroup("Gem Settings", true, false, 0)] public bool excludeFromPool` |  |
| **`GemMergeExponent`** | `public const float GemMergeExponent = 1` |  |
| **`icon`** | `[BoxGroup("Gem Settings", true, false, 0)] public Sprite icon` |  |
| **`isCooldownEnabled`** | `[BoxGroup("Gem Settings", true, false, 0)] public bool isCooldownEnabled` |  |
| **`isRateLimited`** | `[BoxGroup("Gem Settings", true, false, 0)] public bool isRateLimited` |  |
| **`rarity`** | `[BoxGroup("Gem Settings", true, false, 0)] public Rarity rarity` |  |
| **`rateLimitCount`** | `[BoxGroup("Gem Settings", true, false, 0)] [ShowIf("isRateLimited", true)] public ScalingValue rateLimitCount` |  |
| **`rateLimitTime`** | `[BoxGroup("Gem Settings", true, false, 0)] [ShowIf("isRateLimited", true)] public ScalingValue rateLimitTime` |  |
| **`readyEffect`** | `[BoxGroup("Gem Settings", true, false, 0)] [ShowIf("isCooldownEnabled", true)] public GameObject readyEffect` |  |
| **`setNumberDisplay`** | `[BoxGroup("Gem Settings", true, false, 0)] [ShowIf("isRateLimited", true)] public bool setNumberDisplay` |  |
| **`statBonus`** | `[BoxGroup("Gem Settings", true, false, 0)] [ShowIf("enableStatBonus", true)] public StatBonus statBonus` |  |
| **`tags`** | `[BoxGroup("Gem Settings", true, false, 0)] public DescriptionTags tags` |  |
| **`tvDefaultAllExceptSelf`** | `protected AbilityTargetValidatorWrapper tvDefaultAllExceptSelf` |  |
| **`tvDefaultHarmfulEffectTargets`** | `protected AbilityTargetValidatorWrapper tvDefaultHarmfulEffectTargets` |  |
| **`tvDefaultUsefulEffectTargets`** | `protected AbilityTargetValidatorWrapper tvDefaultUsefulEffectTargets` |  |

:::

## Properties (25)

::: details Click to expand Properties (25)

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`canInteractWithMouse`** | `public bool canInteractWithMouse { get; }` |  |
| **`currentCooldown`** | `public float currentCooldown { get; }` |  |
| **`dismantleDreamDustOverride`** | `public int? dismantleDreamDustOverride { get; set; }` |  |
| **`dismantleProgress`** | `public float dismantleProgress { get; }` |  |
| **`effectiveLevel`** | `public int effectiveLevel { get; }` |  |
| **`fillAmount`** | `public float fillAmount { get; set; }` |  |
| **`focusDistance`** | `public float focusDistance { get; }` |  |
| **`handOwner`** | `public Hero handOwner { get; set; }` |  |
| **`interactPivot`** | `public Transform interactPivot { get; }` |  |
| **`isDestroyedOnRoomChange`** | `public override bool isDestroyedOnRoomChange { get; }` |  |
| **`isLocked`** | `public bool isLocked { get; }` | Is this gem locked for local player? |
| **`isNotReadyByRateLimit`** | `public bool isNotReadyByRateLimit { get; }` | Is this gem not ready because of rate limit? |
| **`isValid`** | `public bool isValid { get; }` | Returns true if gem is not destroyed, is active, and has owner. |
| **`location`** | `public GemLocation location { get; set; }` | Location of this gem if equipped to a hero. |
| **`maxCooldown`** | `public float maxCooldown { get; }` |  |
| **`maxSellGold`** | `public int maxSellGold { get; set; }` |  |
| **`numberDisplay`** | `public int? numberDisplay { get; set; }` |  |
| **`owner`** | `public Hero owner { get; set; }` |  |
| **`quality`** | `[SaveVar] [SaveVar(SaveVarFlags.Default)] public int quality { get; set; }` |  |
| **`qualityType`** | `public Gem.QualityType qualityType { get; }` |  |
| **`sellGoldOverride`** | `public int? sellGoldOverride { get; set; }` |  |
| **`skill`** | `public SkillTrigger skill { get; set; }` |  |
| **`skipStartAnimation`** | `public bool skipStartAnimation { get; set; }` |  |
| **`tempOwner`** | `public DewPlayer tempOwner { get; set; }` |  |
| **`worldModel`** | `public ItemWorldModel worldModel { get; }` |  |

:::

## Methods (36)

::: details `ApplyCooldownReduction(float)`

```csharp
public void ApplyCooldownReduction(float amount)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `amount` | `float` |  |

:::

::: details `ApplyCooldownReductionByRatio(float)`

```csharp
public void ApplyCooldownReductionByRatio(float ratio)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `ratio` | `float` |  |

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

::: details `CreateAbilityInstanceWithSource&lt;T&gt;(Actor, Vector3, Quaternion?, CastInfo, Action&lt;T&gt;)`

Create an ability instance on behalf of source actor, but make it inherit this gem's quality. You MUST ensure source will not be destroyed before calling this. Call this right after instance spawn or use Actor.LockDestroy().

```csharp
public T CreateAbilityInstanceWithSource<T>(Actor source, Vector3 position, Quaternion? rotation, CastInfo info, Action<T> beforePrepare = null) where T : AbilityInstance
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `source` | [`Actor`](/api/Global.Actor) |  |
| `position` | `UnityEngine.Vector3` |  |
| `rotation` | `UnityEngine.Quaternion?` |  |
| `info` | [`CastInfo`](/api/Global.CastInfo) |  |
| `beforePrepare` | `System.Action<T>` |  |
| `` | `T` |  |

**Returns:** `T`

:::

::: details `CreateBasicEffectWithSource(Actor, Entity, BasicEffect, float, string, DuplicateEffectBehavior)`

Create a basic effect container on behalf of source actor. You MUST ensure source will not be destroyed before calling this. Call this right after instance spawn or use Actor.LockDestroy().

```csharp
public Se_GenericEffectContainer CreateBasicEffectWithSource(Actor source, Entity victim, BasicEffect eff, float duration, string id, DuplicateEffectBehavior onDuplicate = DuplicateEffectBehavior.ReplacePrevious)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `source` | [`Actor`](/api/Global.Actor) |  |
| `victim` | [`Entity`](/api/Global.Entity) |  |
| `eff` | [`BasicEffect`](/api/Global.BasicEffect) |  |
| `duration` | `float` |  |
| `id` | `string` |  |
| `onDuplicate` | <a href="/enums#duplicateeffectbehavior" class="enum-link" data-tooltip="UsePrevious=0 · ReplacePrevious=1 · DoNothing=2">DuplicateEffectBehavior</a> |  |

**Returns:** `Se_GenericEffectContainer`

:::

::: details `CreateStatusEffectWithSource&lt;T&gt;(Actor, Entity, CastInfo, Action&lt;T&gt;)`

Create a status effect on behalf of source actor, but make it inherit this gem's quality. You MUST ensure source will not be destroyed before calling this. Call this right after instance spawn or use Actor.LockDestroy().

```csharp
public T CreateStatusEffectWithSource<T>(Actor source, Entity victim, CastInfo info, Action<T> beforePrepare = null) where T : StatusEffect
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `source` | [`Actor`](/api/Global.Actor) |  |
| `victim` | [`Entity`](/api/Global.Entity) |  |
| `info` | [`CastInfo`](/api/Global.CastInfo) |  |
| `beforePrepare` | `System.Action<T>` |  |
| `` | `T` |  |

**Returns:** `T`

:::

::: details `DismantleGem()`

```csharp
public void DismantleGem()
```

:::

::: details `GetBuyGold()`

```csharp
public int GetBuyGold()
```

**Returns:** `int`

:::

::: details `GetBuyGold(Rarity, int)`

```csharp
public static int GetBuyGold(Rarity rarity, int quality)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `rarity` | <a href="/enums#rarity" class="enum-link" data-tooltip="Common=0 · Rare=1 · Epic=2 · Legendary=3 · Character=4 (+2 more)">Rarity</a> |  |
| `quality` | `int` |  |

**Returns:** `int`

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

::: details `GetGoldValue(Rarity, int)`

```csharp
public static int GetGoldValue(Rarity rarity, int quality)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `rarity` | <a href="/enums#rarity" class="enum-link" data-tooltip="Common=0 · Rare=1 · Epic=2 · Legendary=3 · Character=4 (+2 more)">Rarity</a> |  |
| `quality` | `int` |  |

**Returns:** `int`

:::

::: details `GetMergedQuality(int, int)`

```csharp
public static int GetMergedQuality(int a, int b)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `a` | `int` |  |
| `b` | `int` |  |

**Returns:** `int`

:::

::: details `GetQualityType(float)`

```csharp
public static Gem.QualityType GetQualityType(float quality)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `quality` | `float` |  |

**Returns:** `Gem.QualityType`

:::

::: details `GetSellGold()`

```csharp
public int GetSellGold()
```

**Returns:** `int`

:::

::: details `GetSellGold(Rarity, int)`

```csharp
public static int GetSellGold(Rarity rarity, int quality)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `rarity` | <a href="/enums#rarity" class="enum-link" data-tooltip="Common=0 · Rare=1 · Epic=2 · Legendary=3 · Character=4 (+2 more)">Rarity</a> |  |
| `quality` | `int` |  |

**Returns:** `int`

:::

::: details `GetValue(ScalingValue)`

Gets value of the given scaling value using this gem's level and caster.

```csharp
public float GetValue(ScalingValue val)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `val` | [`ScalingValue`](/api/Global.ScalingValue) |  |

**Returns:** `float`

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

::: details `IsReady()`

Is this gem ready? By default this checks if the gem is cooled down and has at least 1 use left (rate-limit).This must return the same value everywhere(server/clients) for consistent behavior.

```csharp
public virtual bool IsReady()
```

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

::: details `NotifyUse()`

Flash this gem in UI for highlighting or giving attention to player.If this gem is rate-limited, it will decrement remaining use.

```csharp
public void NotifyUse()
```

:::

::: details `OnCastComplete(EventInfoCast)`

Called on server when equipped skill completes casting.

```csharp
protected virtual void OnCastComplete(EventInfoCast info)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `info` | [`EventInfoCast`](/api/Global.EventInfoCast) |  |

:::

::: details `OnCastCompleteBeforePrepare(EventInfoCast)`

Called on server when equipped skill creates ability instance before it is spawned and prepared.

```csharp
protected virtual void OnCastCompleteBeforePrepare(EventInfoCast info)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `info` | [`EventInfoCast`](/api/Global.EventInfoCast) |  |

:::

::: details `OnDealDamage(EventInfoDamage)`

Called on server when equipped skill deals damage.

```csharp
protected virtual void OnDealDamage(EventInfoDamage info)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `info` | [`EventInfoDamage`](/api/Global.EventInfoDamage) |  |

:::

::: details `OnDoHeal(EventInfoHeal)`

Called on server when equipped skill does heal.

```csharp
protected virtual void OnDoHeal(EventInfoHeal obj)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `obj` | [`EventInfoHeal`](/api/Global.EventInfoHeal) |  |

:::

::: details `OnEquipGem(Hero)`

Called everywhere when this gem is picked up by hero.

```csharp
public virtual void OnEquipGem(Hero newOwner)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `newOwner` | [`Hero`](/api/Global.Hero) |  |

:::

::: details `OnEquipSkill(SkillTrigger)`

Called everywhere when this gem starts taking effect on skill.

```csharp
public virtual void OnEquipSkill(SkillTrigger newSkill)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `newSkill` | [`SkillTrigger`](/api/Global.SkillTrigger) |  |

:::

::: details `OnPrepare()`

```csharp
protected override void OnPrepare()
```

:::

::: details `OnQualityChange(int, int)`

Called everywhere when this gem's quality is changed.

```csharp
protected virtual void OnQualityChange(int oldQuality, int newQuality)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `oldQuality` | `int` |  |
| `newQuality` | `int` |  |

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

::: details `OnUnequipGem(Hero)`

Called everywhere when this gem is dropped by hero.

```csharp
public virtual void OnUnequipGem(Hero oldOwner)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `oldOwner` | [`Hero`](/api/Global.Hero) |  |

:::

::: details `OnUnequipSkill(SkillTrigger)`

Called everywhere when this gem stops taking effect on skill.

```csharp
public virtual void OnUnequipSkill(SkillTrigger oldSkill)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `oldSkill` | [`SkillTrigger`](/api/Global.SkillTrigger) |  |

:::

::: details `ResetCooldown()`

```csharp
public void ResetCooldown()
```

:::

::: details `ShouldBeSavedWithRoom()`

```csharp
public override bool ShouldBeSavedWithRoom()
```

**Returns:** `bool`

:::

::: details `StartCooldown()`

```csharp
public void StartCooldown()
```

:::


## Architecture & Relationships

::: details Click to expand Architecture & Relationships

### Used By (164)

*Classes and systems that invoke, reference, or depend on `Gem`:*

`ACH_THE_EIGHTH_TROPHY` · [AbilityInstance](/api/Global.AbilityInstance) · [AchievementManager](/api/Global.AchievementManager) · `Ai_FirstBonusQualityUpgrader` · `Ai_Gem_U_GuidingCompass_PowerGainProjectile` · `Ai_Gem_U_LastStarlight` · `Ai_RandomGemUpgrade` · `Ai_Shrine_MawOfDoom_DestroyTarget` · [AnalyticsEquipmentData](/api/Global.AnalyticsEquipmentData) · [ChatManager](/api/Global.ChatManager) · [ClientEventManager](/api/Global.ClientEventManager) · [Dew](/api/Global.Dew) · [DewLocalization](/api/Global.DewLocalization) · [DewPlayer](/api/Global.DewPlayer) · [EditSkillManager](/api/Global.EditSkillManager) · [EditSkillShrine](/api/Global.EditSkillShrine) · [GameManager](/api/Global.GameManager) · `GemWorldModel` · `Gem_C_CamillasGiftRuined` · `Gem_C_Charcoal` · `Gem_C_Confidence` · `Gem_C_Efficiency` · `Gem_C_Guidance` · `Gem_C_Lethality` · `Gem_C_Love` · `Gem_C_Nap` · `Gem_C_Quicksilver` · `Gem_C_Regeneration` · `Gem_C_Responsibility` · `Gem_C_Sharp` · `Gem_C_Shatter` · `Gem_C_Sulfur` · `Gem_C_Talc` · `Gem_C_Vengeance` · `Gem_C_Void` · `Gem_C_Wind` · `Gem_E_Aftershock` · `Gem_E_Apathy` · `Gem_E_Blossom` · `Gem_E_Clemency` · `Gem_E_Crimson` · `Gem_E_Direness` · `Gem_E_Domination` · `Gem_E_Fangs` · `Gem_E_Fever` · `Gem_E_Flexibility` · `Gem_E_Insensitivity` · `Gem_E_Insight` · `Gem_E_Inversion` · `Gem_E_Metal` · `Gem_E_Might` · `Gem_E_Obsidian` · `Gem_E_Omega` · `Gem_E_Opportunity` · `Gem_E_OurStory_Completed` · `Gem_E_OurStory_Unfinished` · `Gem_E_Overload` · `Gem_E_Pain` · `Gem_E_Predation` · `Gem_E_Protection` · `Gem_E_Reflex` · `Gem_E_Thunder` · `Gem_E_Twilight` · `Gem_E_Umbra` · `Gem_E_Virtuousness` · `Gem_L_CamillasGift` · `Gem_L_ChaosApple` · `Gem_L_Culinary` · `Gem_L_DivineFaith` · `Gem_L_Embertail` · `Gem_L_HeartOfGold` · `Gem_L_Infinity` · `Gem_L_Liberty` · `Gem_L_MetalCrystal` · `Gem_L_Paranoia` · `Gem_L_Perfect` · `Gem_L_PureWhite` · `Gem_L_SolarEye` · `Gem_L_Supersymmetry` · `Gem_L_SuppressedArcanum` · `Gem_R_Abyss` · `Gem_R_Accuracy` · `Gem_R_Adventure` · `Gem_R_Blade` · `Gem_R_Bleak` · `Gem_R_Blood` · `Gem_R_Celestial` · `Gem_R_Composure` · `Gem_R_Contempt` · `Gem_R_Control` · `Gem_R_Crucible` · `Gem_R_Dusk` · `Gem_R_Epiphany` · `Gem_R_Flow` · `Gem_R_Frost` · `Gem_R_Glaciate` · `Gem_R_Glass` · `Gem_R_Hedgehog` · `Gem_R_Insatiable` · `Gem_R_Lava` · `Gem_R_Lightweight` · `Gem_R_Momentum` · `Gem_R_Mortality` · `Gem_R_NightSky` · `Gem_R_Panic` · `Gem_R_Purity` · `Gem_R_Rejuvenation` · `Gem_R_Ricochet` · `Gem_R_Rigidity` · `Gem_R_Scorched` · `Gem_R_Shock` · `Gem_R_Slippery` · `Gem_R_Snow` · `Gem_R_Spiral` · `Gem_R_Stillness` · `Gem_R_Wealth` · `Gem_R_Wound` · `Gem_U_EternalFlame` · `Gem_U_GlacialCore` · `Gem_U_GuidingCompass_Charged` · `Gem_U_GuidingCompass_NotCharged` · `Gem_U_LastStarlight` · `Gem_U_SoulPrison` · [HeroSkill](/api/Global.HeroSkill) · `InGameAnalyticsManager` · [InGameUIManager](/api/Global.InGameUIManager) · [PingManager](/api/Global.PingManager) · [PropEnt_Merchant_Base](/api/Global.PropEnt_Merchant_Base) · [PropEnt_Merchant_Jonas](/api/Global.PropEnt_Merchant_Jonas) · `Se_E_Aftershock_Armor` · `Se_Gem_E_Fever_LivingBomb` · `Se_Gem_L_Liberty_Buff` · `Se_Gem_R_Insatiable` · `Se_R_Tranquility` · `Se_Star_Cetus_I_FirstColdGemQualityBoost` · `Se_Star_I_DismantleReroll` · `Se_Star_I_FirstGemUpgrade` · `Shrine_AltarOfCleansing` · `Shrine_Ascension` · `Shrine_BossSoul` · `Shrine_Chaos` · `Shrine_Concept` · `Shrine_Destiny` · `Shrine_Entanglement` · `Shrine_Guidance` · `Shrine_Luck` · `Shrine_MawOfDoom` · `Shrine_ScaredMaw` · `Shrine_UpgradeWell` · `Star_Global_FirstGemUpgrade` · [Summon](/api/Global.Summon) · `Treasure_SuspiciousHat` · `UI_InGame_GemSlot` · `UI_InGame_GemSlot_EditSkill` · `UI_InGame_Interact_Gem` · `UI_InGame_PartyDisplay_Item` · `UI_InGame_SkillButton_EditSkill` · `UI_InGame_SkillNotifications` · `UI_TooltipManager` · `UI_Tooltip_EquippedGemDescriber_Item` · `UI_Tooltip_GemQuality` · `UI_Tooltip_GemTitle` · `UI_Tooltip_ObjLevel` · [ZoneManager](/api/Global.ZoneManager)

### Dependencies (40)

*Types and components that `Gem` references or depends upon:*

[AbilityTargetValidatorWrapper](/api/Global.AbilityTargetValidatorWrapper) · [Actor](/api/Global.Actor) · [BasicEffect](/api/Global.BasicEffect) · [CastInfo](/api/Global.CastInfo) · [ClientEventManager](/api/Global.ClientEventManager) · [DataProcessorGroup`3](/api/Global.DataProcessorGroup`3) · [DewBuildProfile](/api/Global.DewBuildProfile) · [DewPlayer](/api/Global.DewPlayer) · [Entity](/api/Global.Entity) · [EntityCheck](/api/Global.EntityCheck) · [EntityStatus](/api/Global.EntityStatus) · [EventInfoCast](/api/Global.EventInfoCast) · [EventInfoDamage](/api/Global.EventInfoDamage) · [EventInfoHeal](/api/Global.EventInfoHeal) · [Formula](/api/Global.Formula) · [GameManager](/api/Global.GameManager) · [GemLocation](/api/Global.GemLocation) · `GemWorldModel` · [Hero](/api/Global.Hero) · [HeroSkill](/api/Global.HeroSkill) · [IExcludeFromPool](/api/Global.IExcludeFromPool) · [IInteractable](/api/Global.IInteractable) · [IItem](/api/Global.IItem) · [InGameUIManager](/api/Global.InGameUIManager) · `ItemWorldModel` · [LootManager](/api/Global.LootManager) · [ManagerBase`1](/api/Global.ManagerBase`1) · `NetworkConnectionToClientExtension` · [NetworkedManagerBase`1](/api/Global.NetworkedManagerBase`1) · [PerRarityData`1](/api/Global.PerRarityData`1) · [PickupManager](/api/Global.PickupManager) · [SafeAction](/api/Global.SafeAction) · [SafeAction`1](/api/Global.SafeAction`1) · [SafeAction`2](/api/Global.SafeAction`2) · [SafeAction`3](/api/Global.SafeAction`3) · [ScalingValue](/api/Global.ScalingValue) · `Se_GenericEffectContainer` · [SkillTrigger](/api/Global.SkillTrigger) · [StatBonus](/api/Global.StatBonus) · `Mirror.GeneratedNetworkCode`

### Related Enums (4)

*Enumerations referenced in fields, properties, or method signatures:*

<a href="/enums#descriptiontags" class="enum-link" data-tooltip="None=0 · Fire=1 · Cold=2 · Dark=4 · Light=8 (+7 more)">DescriptionTags</a> · <a href="/enums#duplicateeffectbehavior" class="enum-link" data-tooltip="UsePrevious=0 · ReplacePrevious=1 · DoNothing=2">DuplicateEffectBehavior</a> · <a href="/enums#rarity" class="enum-link" data-tooltip="Common=0 · Rare=1 · Epic=2 · Legendary=3 · Character=4 (+2 more)">Rarity</a> · <a href="/enums#savevarflags" class="enum-link" data-tooltip="Default=0 · ApplyAfterCreation=1 · ApplyAfterFrameDelay=2">SaveVarFlags</a>

:::
