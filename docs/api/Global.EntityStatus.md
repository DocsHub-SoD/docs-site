# Class: EntityStatus

- **Category:** <span class="cat-dot" style="--cat-color: #ef4444" data-cat="Combat & Abilities"></span> Combat & Abilities
- **Namespace:** `Global`
- **Assembly:** `Dew.Core.dll`
- **Inheritance / Derived:** [DewNetworkBehaviour](/api/Global.DewNetworkBehaviour) → [EntityComponent](/api/Global.EntityComponent)

```csharp
[HideMonoScript]
public class EntityStatus : EntityComponent, ILogicUpdate, ICleanup
```

## Fields (10)

::: details Click to expand Fields (10)

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`baseStats`** | `[SyncVar] [BoxGroup("Stat Settings", true, false, 0)] public BaseStats baseStats` |  |
| **`bonusStats`** | `[SyncVar] [BoxGroup("Stat Settings", true, false, 0)] [NonSerialized] [ShowInInspector] [ReadOnly] [HideIn(PrefabKind.PrefabInstance\|PrefabKind.PrefabAsset)] public BonusStats bonusStats` |  |
| **`ClientEvent_OnOnFinalStatsUpdated`** | `public SafeAction ClientEvent_OnOnFinalStatsUpdated` |  |
| **`finalStats`** | `public FinalStats finalStats` | Base stats + scaling stats + bonus stats + basic effect stats |
| **`finalStatsProcessors`** | `public DataProcessorGroup<FinalStats> finalStatsProcessors` |  |
| **`manaTypeKey`** | `public string manaTypeKey` |  |
| **`MaximumArmorValue`** | `public const float MaximumArmorValue = 100000` |  |
| **`MinimumArmorValue`** | `public const float MinimumArmorValue = -300` |  |
| **`scalingStats`** | `[SyncVar] [BoxGroup("Stat Settings", true, false, 0)] public BonusStats scalingStats` |  |
| **`statusEffects`** | `public readonly List<StatusEffect> statusEffects` | List of status effects this entity has. |

:::

## Properties (66)

::: details Click to expand Properties (66)

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`abilityHaste`** | `public float abilityHaste { get; }` |  |
| **`abilityPower`** | `public float abilityPower { get; }` |  |
| **`armor`** | `public float armor { get; }` |  |
| **`attackDamage`** | `public float attackDamage { get; }` |  |
| **`attackSpeedMultiplier`** | `public float attackSpeedMultiplier { get; }` |  |
| **`basicEffectMask`** | `public BasicEffectMask basicEffectMask { get; }` |  |
| **`coldEffectAmp`** | `public float coldEffectAmp { get; }` |  |
| **`critAmp`** | `public float critAmp { get; }` |  |
| **`critChance`** | `public float critChance { get; }` |  |
| **`currentHealth`** | `[SaveVar] [SaveVar(SaveVarFlags.ApplyAfterFrameDelay)] public float currentHealth { get; }` |  |
| **`currentMana`** | `[SaveVar] [SaveVar(SaveVarFlags.ApplyAfterFrameDelay)] public float currentMana { get; }` |  |
| **`currentShield`** | `public float currentShield { get; }` |  |
| **`darkEffectAmp`** | `public float darkEffectAmp { get; }` |  |
| **`darkStack`** | `public int darkStack { get; }` |  |
| **`fireEffectAmp`** | `public float fireEffectAmp { get; }` |  |
| **`fireStack`** | `public int fireStack { get; }` |  |
| **`hasArmorBoost`** | `public bool hasArmorBoost { get; }` |  |
| **`hasArmorReduction`** | `public bool hasArmorReduction { get; }` |  |
| **`hasAttackCritical`** | `public bool hasAttackCritical { get; }` |  |
| **`hasAttackOverride`** | `public bool hasAttackOverride { get; }` |  |
| **`hasBlind`** | `public bool hasBlind { get; }` |  |
| **`hasCold`** | `public bool hasCold { get; }` |  |
| **`hasCripple`** | `public bool hasCripple { get; }` |  |
| **`hasCrowdControlImmunity`** | `public bool hasCrowdControlImmunity { get; }` |  |
| **`hasDamageImmunity`** | `public bool hasDamageImmunity { get; }` |  |
| **`hasDeathInterrupt`** | `public bool hasDeathInterrupt { get; }` |  |
| **`hasHaste`** | `public bool hasHaste { get; }` |  |
| **`hasImmobility`** | `public bool hasImmobility { get; }` |  |
| **`hasInvisible`** | `public bool hasInvisible { get; }` |  |
| **`hasInvulnerable`** | `public bool hasInvulnerable { get; }` |  |
| **`hasMirageSkin`** | `public bool hasMirageSkin { get; }` |  |
| **`hasProtected`** | `public bool hasProtected { get; }` |  |
| **`hasRoot`** | `public bool hasRoot { get; }` |  |
| **`hasSilence`** | `public bool hasSilence { get; }` |  |
| **`hasSlow`** | `public bool hasSlow { get; }` |  |
| **`hasSpeed`** | `public bool hasSpeed { get; }` |  |
| **`hasStun`** | `public bool hasStun { get; }` |  |
| **`hasUncollidable`** | `public bool hasUncollidable { get; }` |  |
| **`hasUnstoppable`** | `public bool hasUnstoppable { get; }` |  |
| **`healthRegen`** | `public float healthRegen { get; }` |  |
| **`isAlive`** | `public bool isAlive { get; }` |  |
| **`isDead`** | `public bool isDead { get; }` |  |
| **`isHealthHidden`** | `public bool isHealthHidden { get; }` |  |
| **`isInConversation`** | `public bool isInConversation { get; }` |  |
| **`isSectionTriggeringDisabled`** | `public CounterBool isSectionTriggeringDisabled { get; }` |  |
| **`level`** | `[SaveVar] [SaveVar(SaveVarFlags.Default)] public int level { get; set; }` |  |
| **`lightEffectAmp`** | `public float lightEffectAmp { get; }` |  |
| **`lightStack`** | `public int lightStack { get; }` |  |
| **`manaRegen`** | `public float manaRegen { get; }` |  |
| **`maxHealth`** | `public float maxHealth { get; }` |  |
| **`maxMana`** | `public float maxMana { get; }` |  |
| **`mirageSkinInitAmount`** | `public float mirageSkinInitAmount { get; }` |  |
| **`missingHealth`** | `public float missingHealth { get; }` |  |
| **`missingMana`** | `public float missingMana { get; }` |  |
| **`movementSpeedMultiplier`** | `public float movementSpeedMultiplier { get; }` |  |
| **`normalizedHealth`** | `public float normalizedHealth { get; }` |  |
| **`normalizedMana`** | `public float normalizedMana { get; }` |  |
| **`overridenAttack`** | `public AbilityTrigger overridenAttack { get; }` |  |
| **`specialFill`** | `public Vector2 specialFill { get; set; }` |  |
| **`tenacity`** | `public float tenacity { get; }` |  |
| **`totalArmorFromStatusEffects`** | `public float totalArmorFromStatusEffects { get; }` |  |
| **`totalCripple`** | `public float totalCripple { get; }` |  |
| **`totalFakeMaxHealth`** | `public float totalFakeMaxHealth { get; }` |  |
| **`totalHaste`** | `public float totalHaste { get; }` |  |
| **`totalSlow`** | `public float totalSlow { get; }` |  |
| **`totalSpeed`** | `public float totalSpeed { get; }` |  |

:::

## Methods (28)

::: details `AddStatBonus(StatBonus)`

Add the given bonus stats to this entity.

```csharp
public StatBonus AddStatBonus(StatBonus bonus)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `bonus` | [`StatBonus`](/api/Global.StatBonus) |  |

**Returns:** `StatBonus`

:::

::: details `CalculateTotalBonusStat(float, float, float)`

```csharp
public float CalculateTotalBonusStat(float current, float bonusFlat, float bonusPercentage)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `current` | `float` |  |
| `bonusFlat` | `float` |  |
| `bonusPercentage` | `float` |  |

**Returns:** `float`

:::

::: details `DisableSectionTriggering()`

This entity will not trigger section colliders. Note EnableSectionTriggering() must be done after calling this function.

```csharp
public void DisableSectionTriggering()
```

:::

::: details `EnableSectionTriggering()`

This entity will trigger section colliders. Note this has to be done AFTER calling DisableSectionTriggering().

```csharp
public void EnableSectionTriggering()
```

:::

::: details `FindStatusEffect(Type, Func&lt;StatusEffect, bool&gt;)`

Find a status effect of given type with predicate.

```csharp
public StatusEffect FindStatusEffect(Type type, Func<StatusEffect, bool> predicate)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `type` | `System.Type` |  |
| `predicate` | [`System.Func<T, TResult><StatusEffect,bool>`](/api/Global.StatusEffect) |  |

**Returns:** `StatusEffect`

:::

::: details `FindStatusEffect&lt;T&gt;(Func&lt;T, bool&gt;)`

Find a status effect of given type with predicate.

```csharp
public T FindStatusEffect<T>(Func<T, bool> predicate) where T : StatusEffect
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `predicate` | `System.Func<T, TResult><T,bool>` |  |
| `` | `T` |  |

**Returns:** `T`

:::

::: details `GetBonusAbilityPower()`

```csharp
public float GetBonusAbilityPower()
```

**Returns:** `float`

:::

::: details `GetBonusArmor()`

```csharp
public float GetBonusArmor()
```

**Returns:** `float`

:::

::: details `GetBonusAttackDamage()`

```csharp
public float GetBonusAttackDamage()
```

**Returns:** `float`

:::

::: details `GetBonusHealth()`

```csharp
public float GetBonusHealth()
```

**Returns:** `float`

:::

::: details `GetElementalAmp(ElementalType)`

```csharp
public float GetElementalAmp(ElementalType type)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `type` | <a href="/enums#elementaltype" class="enum-link" data-tooltip="Fire=0 · Cold=1 · Light=2 · Dark=3">ElementalType</a> |  |

**Returns:** `float`

:::

::: details `GetElementalStack(ElementalType)`

```csharp
public int GetElementalStack(ElementalType type)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `type` | <a href="/enums#elementaltype" class="enum-link" data-tooltip="Fire=0 · Cold=1 · Light=2 · Dark=3">ElementalType</a> |  |

**Returns:** `int`

:::

::: details `GetStatusEffect(Type)`

Get a status effect of given type.

```csharp
public StatusEffect GetStatusEffect(Type type)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `type` | `System.Type` |  |

**Returns:** `StatusEffect`

:::

::: details `GetStatusEffect&lt;T&gt;()`

Get a status effect of given type.

```csharp
public T GetStatusEffect<T>() where T : StatusEffect
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `` | `T` |  |

**Returns:** `T`

:::

::: details `GetStatusEffects(Type)`

Enumerate all status effects of given type.

```csharp
public IEnumerable<StatusEffect> GetStatusEffects(Type type)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `type` | `System.Type` |  |

**Returns:** `System.Collections.Generic.IEnumerable<T><StatusEffect>`

:::

::: details `GetStatusEffects&lt;T&gt;()`

Enumerate all status effects of given type.

```csharp
public IEnumerable<T> GetStatusEffects<T>() where T : StatusEffect
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `` | `T` |  |

**Returns:** `System.Collections.Generic.IEnumerable<T>`

:::

::: details `HasElemental(ElementalType)`

```csharp
public bool HasElemental(ElementalType type)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `type` | <a href="/enums#elementaltype" class="enum-link" data-tooltip="Fire=0 · Cold=1 · Light=2 · Dark=3">ElementalType</a> |  |

**Returns:** `bool`

:::

::: details `HasStatusEffect(Type)`

Does this entity has a status effect of a certain type?

```csharp
public bool HasStatusEffect(Type statusEffectType)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `statusEffectType` | `System.Type` |  |

**Returns:** `bool`

:::

::: details `HasStatusEffect&lt;T&gt;()`

Does this entity has a status effect of a certain type?

```csharp
public bool HasStatusEffect<T>() where T : StatusEffect
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `` | `T` |  |

**Returns:** `bool`

:::

::: details `HideHealth()`

```csharp
public void HideHealth()
```

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

::: details `RemoveStatBonus(StatBonus)`

Remove the given bonus stats from this entity. Throws if the provided bonus did not exist on this entity.

```csharp
public void RemoveStatBonus(StatBonus bonus)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `bonus` | [`StatBonus`](/api/Global.StatBonus) |  |

:::

::: details `SetHealth(float)`

```csharp
public void SetHealth(float amount)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `amount` | `float` |  |

:::

::: details `SetMana(float)`

```csharp
public void SetMana(float amount)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `amount` | `float` |  |

:::

::: details `ShowHealth()`

```csharp
public void ShowHealth()
```

:::

::: details `TryGetStatusEffect(Type, out StatusEffect)`

Try to get an existing status effect instance on this entity.

```csharp
public bool TryGetStatusEffect(Type type, out StatusEffect effect)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `type` | `System.Type` |  |
| `effect` | [`StatusEffect`](/api/Global.StatusEffect) |  |

**Returns:** `bool`

:::

::: details `TryGetStatusEffect&lt;T&gt;(out T)`

Try to get an existing status effect instance on this entity.

```csharp
public bool TryGetStatusEffect<T>(out T effect) where T : StatusEffect
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `effect` | `T` |  |
| `` | `T` |  |

**Returns:** `bool`

:::

::: details `UpdateStats()`

Recalculate entity stats + stat processors + basic effects + bonus stats immediately.

```csharp
public void UpdateStats()
```

:::


## Architecture & Relationships

::: details Click to expand Architecture & Relationships

### Used By (381)

*Classes and systems that invoke, reference, or depend on `EntityStatus`:*

`ACH_THOUSAND_THUNDERS` · [AbilitySelfValidator](/api/Global.AbilitySelfValidator) · [AbilityTrigger](/api/Global.AbilityTrigger) · [ActionAttackMove](/api/Global.ActionAttackMove) · [ActionCast](/api/Global.ActionCast) · [ActionInteract](/api/Global.ActionInteract) · [Actor](/api/Global.Actor) · `Ai_ArcticTerritory` · `Ai_C_CorrosiveTrails_Gas` · `Ai_C_DarkSpear` · `Ai_C_FlashFreeze` · `Ai_C_PressurePoint` · `Ai_C_SparklingWaterGun` · `Ai_C_Whirlwind` · `Ai_Culinary_Pickup` · `Ai_Curse_AnchorOfMind_Anchor` · `Ai_D_BurningFist_Attack` · `Ai_D_IceColdPresence_AOE` · `Ai_D_SalamanderPowder_Projectile` · `Ai_D_ScarOfTheWind_DashAtk` · `Ai_E_Aftershock_Damage` · `Ai_E_ClutchesOfMalice_ReachAndPull` · `Ai_E_SliceThroat` · `Ai_Gem_C_Charcoal_Projectile` · `Ai_Gem_E_Crimson` · `Ai_Gem_E_Predation_Pickup` · `Ai_Gem_U_LastStarlight` · `Ai_Hatred_Curse` · `Ai_Hatred_InkMapCurse` · `Ai_L_ButchersStrike` · `Ai_L_MentalCorruption_Projectile` · `Ai_M_DreamyWaltz_BuffExplosion` · `Ai_M_Sprint` · `Ai_MiniBoss_BloodThorn_MainThorn` · `Ai_MiniBoss_BloodThorn_SubThorn` · `Ai_MiniBoss_IceAura_AoE` · `Ai_Mon_DarkCave_Oppressor_Hypnotize` · `Ai_Mon_Despair_BossAzurak_Roll` · `Ai_Mon_Despair_BossAzurak_StompProjectile_Projectile` · `Ai_Mon_Despair_ParalyticFly_Atk` · `Ai_Mon_Ink_BossDarkMoon_Blade` · `Ai_Mon_Ink_BossWhiteNight_AltAtk_Ready` · `Ai_Mon_Ink_BossWhiteNight_Cataclysm` · `Ai_Mon_Ink_BossWhiteNight_Cataclysm_Instance` · `Ai_Mon_Ink_BossWhiteNight_Cataclysm_SafeZone` · `Ai_Mon_Ink_BossWhiteNight_DestructionWave_Wave` · `Ai_Mon_LavaLand_FireElemental_Destruct` · `Ai_Mon_LavaLand_FireElemental_Explosion` · `Ai_Mon_Primus_BossPrimusAeron_Rage_MassDelusion` · `Ai_Mon_Primus_BossPrimusAeron_Rage_MassSilence_Instance` · `Ai_Mon_Sky_Baam_TeleportSequence` · `Ai_Mon_Sky_BigBaam_BeamAtk` · `Ai_Mon_Sky_BigBaam_Main_Root` · `Ai_Mon_Sky_BossNyx_Blackhole` · `Ai_Mon_SnowMountain_BossSkoll_Atk` · `Ai_Mon_Special_AmbushSpawner_Projectile` · `Ai_Mon_Special_BossErebos_Gaze_Instance` · `Ai_Mon_Special_BossErebos_SpawnBlackhole_Instance` · `Ai_Mon_Special_BossErebos_SpawnTormentor_Slow` · `Ai_Mon_Special_BossMaw_ChainReaction_Instance` · `Ai_Mon_Special_BossMaw_DarkSpear` · `Ai_Mon_Special_BossMaw_Purgatory_Heal` · `Ai_Mon_Special_BossPolaris_Holy_Atk_Explosion` · `Ai_Mon_Special_BossPolaris_Holy_Purgatory_BurningFloor` · `Ai_Mon_Special_BossPolaris_Holy_Purgatory_HealProjectile` · `Ai_Mon_Special_BossPolaris_Holy_Purgatory_Instance` · `Ai_Mon_Special_BossPolaris_Holy_RainFire_Damage` · `Ai_Mon_Special_BossPolaris_Holy_ScatterFire` · `Ai_Mon_Special_BossPolaris_Monster_Atk_FirstAtk` · `Ai_Mon_Special_BossPolaris_Monster_Atk_SecondAtk` · `Ai_Mon_Special_BossPolaris_Monster_Atk_Spawner` · `Ai_Mon_Special_BossPolaris_Monster_Scream` · `Ai_Q_CruelSun` · `Ai_Q_DeathMark_Projectile` · `Ai_Q_EmbracingTheChill_AreaDoT` · `Ai_Q_EtherealInfluence` · `Ai_Q_Fleche_Dash` · `Ai_Q_GoldenBurst` · `Ai_Q_SuperNova` · `Ai_R_BackOff_Spawner` · `Ai_R_ChainReaction` · `Ai_R_DarkGrenade_Shard` · `Ai_R_FrozenFists_PunchDash` · `Ai_R_Ignite` · `Ai_R_NaturesWhisper` · `Ai_R_SanctuaryOfEl_Ground` · `Ai_R_Somersault` · `Ai_ReviveHero` · `Ai_U_BigChomp` · `Ai_UnstableRatSwarm_Projectile` · `Ai_VeilOfDark` · [AttackOverrideEffect](/api/Global.AttackOverrideEffect) · [AttackTrigger](/api/Global.AttackTrigger) · [BasicEffectWithStrength](/api/Global.BasicEffectWithStrength) · [BossMonster](/api/Global.BossMonster) · `BossSeeker_SpotLightController` · [CameraManager](/api/Global.CameraManager) · [ControlManager](/api/Global.ControlManager) · [ConversationManager](/api/Global.ConversationManager) · `ConversationShrineBase` · [DamageInstance](/api/Global.DamageInstance) · [DashAttackInstance](/api/Global.DashAttackInstance) · `Despair_FogPositionController` · [Dew](/api/Global.Dew) · [DewCollider](/api/Global.DewCollider) · [DewDifficultySettings](/api/Global.DewDifficultySettings) · [DewPhysics](/api/Global.DewPhysics) · `DewStarItemOld` · [Entity](/api/Global.Entity) · [EntityAI](/api/Global.EntityAI) · [EntityAnimation](/api/Global.EntityAnimation) · [EntityCheck](/api/Global.EntityCheck) · [EntityControl](/api/Global.EntityControl) · [EntitySound](/api/Global.EntitySound) · [EntityVisual](/api/Global.EntityVisual) · [FinalDamageData](/api/Global.FinalDamageData) · [FlavourManager](/api/Global.FlavourManager) · `GameMod_DespairFixStuck` · [GameMod_Limbo](/api/Global.GameMod_Limbo) · [GameMod_MirageSkin](/api/Global.GameMod_MirageSkin) · [GameResultManager](/api/Global.GameResultManager) · [Gem](/api/Global.Gem) · `Gem_C_Lethality` · `Gem_C_Love` · `Gem_C_Quicksilver` · `Gem_C_Regeneration` · `Gem_C_Sulfur` · `Gem_C_Wind` · `Gem_E_Aftershock` · `Gem_E_Apathy` · `Gem_E_Domination` · `Gem_E_Fever` · `Gem_E_Flexibility` · `Gem_E_Insensitivity` · `Gem_E_Insight` · `Gem_E_Obsidian` · `Gem_E_OurStory_Completed` · `Gem_E_Predation` · `Gem_E_Protection` · `Gem_E_Reflex` · `Gem_E_Umbra` · `Gem_L_DivineFaith` · `Gem_L_Embertail` · `Gem_L_Liberty` · `Gem_L_MetalCrystal` · `Gem_L_Supersymmetry` · `Gem_R_Abyss` · `Gem_R_Bleak` · `Gem_R_Composure` · `Gem_R_Control` · `Gem_R_Epiphany` · `Gem_R_Frost` · `Gem_R_Hedgehog` · `Gem_R_Insatiable` · `Gem_R_Mortality` · `Gem_R_Panic` · `Gem_R_Shock` · `Gem_R_Slippery` · `Gem_R_Snow` · `Gem_R_Spiral` · `Gem_R_Wound` · `Gem_U_EternalFlame` · `Gem_U_SoulPrison` · [Hero](/api/Global.Hero) · `Hero_Bismuth` · [ISpawnableAsMiniBoss](/api/Global.ISpawnableAsMiniBoss) · `Ink_BossRoomDamageGround` · [InvisibleEffect](/api/Global.InvisibleEffect) · [KillTracker](/api/Global.KillTracker) · [Knockback](/api/Global.Knockback) · `LavaLand_IcePlace` · `LavaLand_Lava` · `LucidDream_FishScales` · `LucidDream_KindArmadillo` · `LucidDream_MarshOfDestiny` · `LucidDream_TheDarkestUrge` · `LucidDream_WILD` · [MirageSkinEffect](/api/Global.MirageSkinEffect) · `Mon_DarkCave_BossSeeker` · `Mon_DarkCave_CaveSpider` · `Mon_Despair_Displacer` · `Mon_Despair_DreadBug` · `Mon_Despair_WretchedArtillery` · [Mon_DreamTeller](/api/Global.Mon_DreamTeller) · `Mon_Forest_SpiderSpitter` · `Mon_Ink_Archer` · `Mon_Ink_BossDarkMoon` · `Mon_Ink_BossWhiteNight` · `Mon_Ink_DivineAnimal` · `Mon_Ink_GhostBlade` · `Mon_Ink_GhostSpear` · `Mon_LavaLand_FireElemental` · `Mon_LavaLand_InfernoSpider` · `Mon_LavaLand_Magmadon` · `Mon_LavaLand_SuperheatedWolf` · `Mon_Polaris` · `Mon_Primus_BossPrimusAeron` · `Mon_Sky_BossNyx` · `Mon_Sky_LittleBaam` · `Mon_Sky_StarSeed` · `Mon_SnowMountain_SnowWolf` · `Mon_Special_BossErebos` · `Mon_Special_BossPolaris` · [Monster](/api/Global.Monster) · [PickupManager](/api/Global.PickupManager) · [PingManager](/api/Global.PingManager) · [PlayGameManager](/api/Global.PlayGameManager) · `PlayTutorial_Tutorial_Hunt` · `PlayTutorial_Tutorial_SkillsAndEssences` · `Primus_Ending` · [Projectile](/api/Global.Projectile) · [PropEnt_Merchant_Base](/api/Global.PropEnt_Merchant_Base) · [PropEnt_Merchant_Jonas](/api/Global.PropEnt_Merchant_Jonas) · `Quest_LostSoul` · `RoomMod_CorruptedChaos_AuraOfPain` · `RoomMod_EngulfedInFlame` · `RoomMod_Hunted` · `RoomMod_LeafPuppies` · `RoomMod_MeteoricLife` · [RoomSection](/api/Global.RoomSection) · [Room_Shortcut](/api/Global.Room_Shortcut) · [ScalingValue](/api/Global.ScalingValue) · `Se_AutoDetectPresence` · `Se_Curse_AmplifiedPain` · `Se_Curse_BlissOfIgnorance` · `Se_Curse_Fragility` · `Se_Curse_FragmentedBeing` · `Se_Curse_GuidingCompass_CripplingAnxiety` · `Se_Curse_SilentNight` · `Se_Curse_SoftSkin` · `Se_D_AstridsMasterpieceEnGarde` · `Se_D_AstridsMasterpiecePriorite` · `Se_D_CircleOfLife_Summon` · `Se_D_ConvergencePoint` · `Se_D_DoubleTap` · `Se_D_MercyOfEl` · `Se_D_QuartetOfDeath_Buff` · `Se_D_TheKillingFlow` · `Se_E_Permafrost_Shield` · `Se_Elm_Cold` · `Se_Elm_Dark` · `Se_Elm_Fire` · `Se_Elm_Light` · `Se_EngulfedInFlame` · `Se_FallenStar_MonsterReinforcement` · `Se_FishScales` · `Se_Gem_E_Fever_LivingBomb` · `Se_Gem_R_Insatiable` · `Se_GenericEffectContainer` · `Se_GenericHealOverTime` · `Se_GenericRevealed` · `Se_GenericStealth` · `Se_HarmlessWhispers` · `Se_HeroKnockedOut` · `Se_HeroOneShotProtection` · `Se_HunterBuff` · `Se_InConversation` · `Se_L_PyranasFireball` · `Se_LingeringAuraOfGuidance` · `Se_MiniBoss_BloodThorn_Bleeding` · `Se_MiniBoss_IceAura` · `Se_MirageSkin_Delusion` · `Se_MirageSkin_Oblivion` · `Se_MirageSkin_Pulverization` · `Se_MirageSkin_Sanctification` · `Se_Mon_DarkCave_BossSeeker_Substitution` · `Se_Mon_DarkCave_BossSeeker_TunnelVision` · `Se_Mon_Despair_BossAzurak_RoarAtk_SafeZoneSpawner` · `Se_Mon_Ink_Boss_Rage` · `Se_Mon_Primus_BossPrimusAeron_Adaptation` · `Se_Mon_Primus_BossPrimusAeron_Rage_DecayingShield` · `Se_Mon_SnowMountain_SnowWolf_SlowApproach` · `Se_Mon_Special_BossMaw_Cataclysm` · `Se_Mon_Special_BossMaw_ShieldConversion` · `Se_Mon_Special_BossPolaris_Adaptation` · `Se_Mon_Special_BossPolaris_CleansingFlame` · `Se_PortalTransition` · `Se_R_AnnihilationStance` · `Se_R_BoneCrusher` · `Se_R_BoneCrusher_Kidnapped` · `Se_R_Cataclysm` · `Se_R_FrozenFists` · `Se_R_Parry_Start` · `Se_R_UnbreakableDetermination` · `Se_RoomMod_Symbiote` · `Se_RoomMod_WarpingField_Unstable` · `Se_Shrine_Chaos_StatBonus` · `Se_Shrine_Despair_Teleport` · `Se_Star_Aurena_F_DT_UnstoppableAndRemoveDelusion` · `Se_Star_Aurena_L_SpeedOnDamage` · `Se_Star_Bismuth_F_IN_MoreProjByAtkSpd` · `Se_Star_Cetus_D_StatsUpWhileShielded` · `Se_Star_Cetus_F_BA_CdReductionOnKill` · `Se_Star_Cetus_F_FR_ChangeToUltHitReset` · `Se_Star_Cetus_L_ArmorBuffOnShield` · `Se_Star_D_DamageBonusOnAllElemental` · `Se_Star_D_ShieldDamageAmp` · `Se_Star_Husk_F_AS_AddedDurationOnHit` · `Se_Star_Husk_F_DE_MarkHitDodgeCDR` · `Se_Star_I_GoldPerCrit` · `Se_Star_L_DamageReductionFromChilled` · `Se_Star_L_HealOnAttack` · `Se_Star_Mist_F_PR_ShieldAndCrit` · `Se_Star_Mist_L_PotionShield` · `Se_Star_Nachia_D_CanineLover` · `Se_Star_Nachia_F_SC_SummonDmgReduction` · `Se_Star_Vesper_D_ADWithNearbyBurning` · `Se_Star_Vesper_D_ConvertAPToAD` · `Se_Star_Yubar_D_APOnDodge` · `Se_Star_Yubar_D_BonusDamageToLight` · `Se_Star_Yubar_D_ConvertADToAP` · `Se_U_HerWorld_Blackhole` · `Se_U_Hysteria` · [ShieldEffect](/api/Global.ShieldEffect) · `Shrine_ArtifactGiver` · `Shrine_BlessedGuidance` · `Shrine_BrokenWoodenDoll` · `Shrine_Chaos` · `Shrine_CookingPot` · `Shrine_Despair` · `Shrine_Despair_Vestige` · `Shrine_Guidance` · `Shrine_Polaris_Teleporter` · `Shrine_Se_Star_Bismuth_I_KnowledgeBook_Book` · `Shrine_SmallSoul` · [SkillTrigger](/api/Global.SkillTrigger) · `Sky_BossIntruder` · `Sky_LightFogDamager` · `St_D_BurningFist` · `St_D_CircleOfLife` · `St_D_HeartOfThePack` · `St_D_IceColdPresence` · `St_D_IcyVeins` · `St_D_QuartetOfDeath` · `St_D_SalamanderPowder` · `St_D_ScarOfTheWind` · `St_E_Harvest` · `St_E_Rewind` · `St_L_HerosReturn` · `St_L_SmallMoltenCore` · `St_Q_GoldenBurst` · `St_Q_Reduction` · `Star_Global_AbilityPower` · `Star_Global_AttackDamage` · `Star_Global_AttackSpeed` · `Star_Global_DarkAmp` · `Star_Global_DecreaseDamageFromChilled` · `Star_Global_FireAmp` · `Star_Global_LightAmp` · `Star_Global_MaxHealth` · `Star_Global_SkillHaste` · `Star_Global_Tenacity` · `Star_Lacerta_AttackSpeed` · `Star_Lacerta_FireAmp` · `Star_Mist_AddAttackDamage` · `Star_Mist_MovementSpeed` · `Star_Vesper_MaxHealth` · `Star_Yubar_AbilityPower` · `Star_Yubar_SkillHaste` · [StatusEffect](/api/Global.StatusEffect) · `StatusEffectRandomPickupInstance` · [Summon](/api/Global.Summon) · `UI_DamageNumberGroup` · `UI_Dev_ConsoleSelectedEntityInfo` · `UI_EntityCrowdControl` · `UI_EntityCursed` · `UI_EntityDestroyOnDeath` · `UI_EntityElementals` · `UI_EntityFollow` · `UI_EntityHealthBar` · `UI_EntityHealthBarGroup` · `UI_EntityHealthBarMain` · `UI_EntityPrimaryStats` · `UI_EntityProtected` · `UI_EntityUnstoppable` · `UI_HealthBar_Simple` · `UI_InGame_BossBars_Item` · `UI_InGame_HeroDetailWindow` · `UI_InGame_HeroDetailWindow_StatItem` · `UI_InGame_HeroInfoBar` · [ZoneManager](/api/Global.ZoneManager)

### Dependencies (26)

*Types and components that `EntityStatus` references or depends upon:*

[AbilityTrigger](/api/Global.AbilityTrigger) · [Actor](/api/Global.Actor) · [AttackOverrideEffect](/api/Global.AttackOverrideEffect) · [BaseStats](/api/Global.BaseStats) · [BasicEffect](/api/Global.BasicEffect) · [BasicEffectWithStrength](/api/Global.BasicEffectWithStrength) · [BonusStats](/api/Global.BonusStats) · [CounterBool](/api/Global.CounterBool) · [DataProcessorGroup`1](/api/Global.DataProcessorGroup`1) · [Dew](/api/Global.Dew) · [DewNetworkBehaviour](/api/Global.DewNetworkBehaviour) · [DewPool](/api/Global.DewPool) · [Entity](/api/Global.Entity) · [EntityComponent](/api/Global.EntityComponent) · [EntityControl](/api/Global.EntityControl) · [FinalStats](/api/Global.FinalStats) · [ICleanup](/api/Global.ICleanup) · [InvisibleEffect](/api/Global.InvisibleEffect) · [ListReturnHandle`1](/api/Global.ListReturnHandle`1) · `NetworkReaderWriterExtensions` · [SafeAction](/api/Global.SafeAction) · [SafeAction`1](/api/Global.SafeAction`1) · [ShieldEffect](/api/Global.ShieldEffect) · [StatBonus](/api/Global.StatBonus) · [StatusEffect](/api/Global.StatusEffect) · `Mirror.GeneratedNetworkCode`

### Related Enums (3)

*Enumerations referenced in fields, properties, or method signatures:*

<a href="/enums#basiceffectmask" class="enum-link" data-tooltip="Slow=1 · Speed=2 · Haste=4 · Cripple=8 · Root=16 (+19 more)">BasicEffectMask</a> · <a href="/enums#elementaltype" class="enum-link" data-tooltip="Fire=0 · Cold=1 · Light=2 · Dark=3">ElementalType</a> · <a href="/enums#savevarflags" class="enum-link" data-tooltip="Default=0 · ApplyAfterCreation=1 · ApplyAfterFrameDelay=2">SaveVarFlags</a>

:::
