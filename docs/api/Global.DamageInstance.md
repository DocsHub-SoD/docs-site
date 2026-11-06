# Class: DamageInstance

- **Category:** <span class="cat-dot" style="--cat-color: #ef4444" data-cat="Combat & Abilities"></span> Combat & Abilities
- **Namespace:** `Global`
- **Assembly:** `Dew.Core.dll`
- **Inheritance / Derived:** [DewNetworkBehaviour](/api/Global.DewNetworkBehaviour) → [Actor](/api/Global.Actor) → [AbilityInstance](/api/Global.AbilityInstance) → [DashAttackInstance](/api/Global.DashAttackInstance) → [InstantDamageInstance](/api/Global.InstantDamageInstance) → [TickDamageInstance](/api/Global.TickDamageInstance)

```csharp
public abstract class DamageInstance : AbilityInstance, ILogicUpdate, ICleanup, ICustomDestroyRoutine
```

## Fields (30)

::: details Click to expand Fields (30)

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`applyElemental`** | `public bool applyElemental` |  |
| **`attackEffect`** | `public float attackEffect` |  |
| **`attackEffectType`** | `[ShowIf("@attackEffect > 0.001f", true)] public AttackEffectType attackEffectType` |  |
| **`cancelIfCasterDead`** | `public bool cancelIfCasterDead` |  |
| **`closeEnemyDistanceThreshold`** | `public float closeEnemyDistanceThreshold` |  |
| **`closeEnemyMultiplier`** | `public float closeEnemyMultiplier` |  |
| **`cooldownTime`** | `[ShowIf("_isCooldownCheck", true)] public float cooldownTime` |  |
| **`destroyWhenDone`** | `public bool destroyWhenDone` |  |
| **`dmgFactor`** | `public ScalingValue dmgFactor` |  |
| **`doKnockback`** | `public bool doKnockback` |  |
| **`duplicateCheck`** | `public DamageInstance.DuplicateCheckType duplicateCheck` |  |
| **`elemental`** | `[ShowIf("applyElemental", true)] public ElementalType elemental` |  |
| **`elementalChance`** | `[ShowIf("applyElemental", true)] public float elementalChance` |  |
| **`forceMergeNumbers`** | `public bool forceMergeNumbers` |  |
| **`heroDamageMultiplier`** | `public float heroDamageMultiplier` |  |
| **`hitEffect`** | `[Title("Effects", null, TitleAlignments.Left, true, true)] public GameObject hitEffect` |  |
| **`hittable`** | `public AbilityTargetValidator hittable` |  |
| **`isDamageOverTime`** | `public bool isDamageOverTime` |  |
| **`knockbackSettings`** | `[ShowIf("doKnockback", true)] [InlineProperty] [HideLabel] public Knockback knockbackSettings` |  |
| **`knockupAmount`** | `[Title("Extras", null, TitleAlignments.Left, true, true)] public float knockupAmount` |  |
| **`mainEffect`** | `[LabelText("Main Effect (Obsolete, Use Start Effect)")] [HideIf("@mainEffect == null", true)] public GameObject mainEffect` |  |
| **`monsterDamageMultiplier`** | `public float monsterDamageMultiplier` |  |
| **`multiplyDamageByMaxHp`** | `public bool multiplyDamageByMaxHp` |  |
| **`onHit`** | `public SafeAction<Entity> onHit` |  |
| **`origin`** | `public DamageInstance.OriginType origin` |  |
| **`procCoefficient`** | `public float procCoefficient` |  |
| **`range`** | `[Title("General", null, TitleAlignments.Left, true, true)] public DewCollider range` |  |
| **`strengthMultiplier`** | `[SyncVar] public float strengthMultiplier` | Affects damage amount, knockup amount and proc coefficient. |
| **`type`** | `[Title("Damage", null, TitleAlignments.Left, true, true)] public DamageData.SourceType type` |  |
| **`useDirectionOfCast`** | `[ShowIf("doKnockback", true)] public bool useDirectionOfCast` |  |

:::

## Methods (11)

::: details `AddToDuplicateTracker(Entity)`

```csharp
protected void AddToDuplicateTracker(Entity ent)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `ent` | [`Entity`](/api/Global.Entity) |  |

:::

::: details `CheckShouldBeDestroyed()`

```csharp
protected bool CheckShouldBeDestroyed()
```

**Returns:** `bool`

:::

::: details `DoCollisionChecks()`

Can be called multiple times. Duplicates will be excluded.

```csharp
protected void DoCollisionChecks()
```

:::

::: details `IsDuplicate(Entity)`

```csharp
protected bool IsDuplicate(Entity ent)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `ent` | [`Entity`](/api/Global.Entity) |  |

**Returns:** `bool`

:::

::: details `OnBeforeDispatchDamage(ref DamageData, Entity)`

Called on server to process damage before applying it.

```csharp
protected virtual void OnBeforeDispatchDamage(ref DamageData dmg, Entity target)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `dmg` | [`DamageData`](/api/Global.DamageData) |  |
| `target` | [`Entity`](/api/Global.Entity) |  |

:::

::: details `OnCollisionCheck()`

```csharp
protected virtual void OnCollisionCheck()
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

::: details `OnHit(Entity)`

Called on server when this instance hits an entity.

```csharp
protected virtual void OnHit(Entity entity)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `entity` | [`Entity`](/api/Global.Entity) |  |

:::

::: details `OnValidateTarget(Entity)`

Called on server to validate hits on entity. Return false here to ignore certain hit on an entity.

```csharp
protected virtual bool OnValidateTarget(Entity entity)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `entity` | [`Entity`](/api/Global.Entity) |  |

**Returns:** `bool`

:::

::: details `ShouldUseDefaultAbilityTargetValidator()`

```csharp
protected virtual bool ShouldUseDefaultAbilityTargetValidator()
```

**Returns:** `bool`

:::


## Architecture & Relationships

::: details Click to expand Architecture & Relationships

### Used By (130)

*Classes and systems that invoke, reference, or depend on `DamageInstance`:*

`Ai_Ai_Mon_Ink_BossWhiteNight_OneInchPunch_Atk` · `Ai_C_DarkSpear` · `Ai_C_FlashFreeze` · `Ai_C_GlacialStomp` · `Ai_C_IceClaw` · `Ai_C_MagicSword` · `Ai_C_Whirlwind` · `Ai_Curse_DreamAfflictionInductive_Smite` · `Ai_Curse_IntermittentExplosion_Explosion` · `Ai_D_ExplosionArtist_DodgeExplosion` · `Ai_D_ExplosionArtist_LargeExplosion` · `Ai_D_IceColdPresence_AOE` · `Ai_D_IcyVeins_Damage` · `Ai_E_Aftershock_Damage` · `Ai_E_DoomsdayMeteor` · `Ai_E_FinalExplosion_Explosion` · `Ai_E_MassCleanse` · `Ai_E_VileStrike_Damage` · `Ai_Gem_E_Crimson` · `Ai_Gem_E_Fever_Explosion` · `Ai_Gem_R_Scorched_Meteor` · `Ai_HunterArtillery_Big` · `Ai_HunterArtillery_Small` · `Ai_L_ButchersStrike` · `Ai_L_CoinExplosion_Explosion` · `Ai_L_LightExplosion_Instance` · `Ai_MiniBoss_BloodThorn_MainThorn` · `Ai_MiniBoss_BloodThorn_SubThorn` · `Ai_MirageSkin_Oppression_Explode` · `Ai_MirageSkin_Pulverization_Stomp` · `Ai_Mon_DarkCave_BossSeeker_GreenChaserOrb_Explode` · `Ai_Mon_DarkCave_BossSeeker_PurpleOrb_Instance` · `Ai_Mon_DarkCave_BossSeeker_RedFissure` · `Ai_Mon_DarkCave_BossSeeker_TunnelVision_Claw` · `Ai_Mon_DarkCave_BossSeeker_TunnelVision_SecondPoolAtk` · `Ai_Mon_DarkCave_BossSeeker_YellowDiagram_SubInstance` · `Ai_Mon_DarkCave_Oppressor_Hypnotize` · `Ai_Mon_Despair_BossAzurak_Atk_InitDamage` · `Ai_Mon_Despair_BossAzurak_Atk_SubDamage` · `Ai_Mon_Despair_BossAzurak_StompProjectile_FirstAtk` · `Ai_Mon_Despair_BossAzurak_StompTargetArea` · `Ai_Mon_Despair_UnstableRat_Explosion` · `Ai_Mon_Forest_BossDemon_AltSkill_LineAtk` · `Ai_Mon_Forest_BossDemon_AltSkill_Stomp_Tree` · `Ai_Mon_Forest_BossDemon_MainSkill_Stomp_Tree` · `Ai_Mon_Forest_Treant_PowerBomb` · `Ai_Mon_Ink_BossDarkMoon_AltAtk_JumpAtk` · `Ai_Mon_Ink_BossDarkMoon_ThrowSpear_TeleportAtk` · `Ai_Mon_Ink_BossWhiteNight_EnergyWave_Instance` · `Ai_Mon_LavaLand_BossInfernus_AltAtk_Instance` · `Ai_Mon_LavaLand_BossInfernus_Atk` · `Ai_Mon_LavaLand_BossInfernus_Jump_Land` · `Ai_Mon_LavaLand_BossInfernus_PowerBomb` · `Ai_Mon_LavaLand_BossInfernus_Stomp` · `Ai_Mon_LavaLand_BossInfernus_Swipe` · `Ai_Mon_LavaLand_FireElemental_Explosion` · `Ai_Mon_Primus_BossPrimusAeron_Adapt_Doom_Meteor` · `Ai_Mon_Primus_BossPrimusAeron_Adapt_SmiteStorm_Smite` · `Ai_Mon_Primus_BossPrimusAeron_Force_DropGiantSword` · `Ai_Mon_Primus_BossPrimusAeron_Force_GoldRain_Attack` · `Ai_Mon_Primus_BossPrimusAeron_Force_GoldRain_Attack_SubInstance` · `Ai_Mon_Primus_BossPrimusAeron_Force_JumpAttack_ConeInstance` · `Ai_Mon_Primus_BossPrimusAeron_Rage_DashAttack` · `Ai_Mon_Primus_BossPrimusAeron_Rage_MassSilence_Instance` · `Ai_Mon_Sky_BossNyx_LaserAtk_Instance` · `Ai_Mon_Sky_BossNyx_LineAtk` · `Ai_Mon_Sky_BossNyx_Swipe` · `Ai_Mon_Sky_StarSeed_Atk` · `Ai_Mon_SnowMountain_BossSkoll_AuraBladeRain_Instance` · `Ai_Mon_SnowMountain_BossSkoll_AuraExplosion_Spawner` · `Ai_Mon_SnowMountain_BossSkoll_Capture` · `Ai_Mon_SnowMountain_BossSkoll_DeathFromAbove_Land` · `Ai_Mon_SnowMountain_BossSkoll_Sword` · `Ai_Mon_SnowMountain_BossSkoll_Whirlwind` · `Ai_Mon_SnowMountain_IceElemental_IceBreaker` · `Ai_Mon_SnowMountain_IceElemental_IceBreaker_SubExplosion` · `Ai_Mon_SnowMountain_Scavenger_Atk` · `Ai_Mon_SnowMountain_VikingWarrior_Atk` · `Ai_Mon_SnowMountain_VikingWarrior_Sword` · `Ai_Mon_Special_BossMaw_Cataclysm_Meteor` · `Ai_Mon_Special_BossMaw_ChainReaction_Instance` · `Ai_Mon_Special_BossMaw_DarkSpear` · `Ai_Mon_Special_BossMaw_MoonlightPact_Atk` · `Ai_Mon_Special_BossObliviax_Atk` · `Ai_Mon_Special_BossPolaris_Holy_Atk_Explosion` · `Ai_Mon_Special_BossPolaris_Holy_Purgatory_BurningFloor` · `Ai_Mon_Special_BossPolaris_Holy_Purgatory_Instance` · `Ai_Mon_Special_BossPolaris_Holy_RainFire_Damage` · `Ai_Mon_Special_BossPolaris_Holy_ScatterFire` · `Ai_Mon_Special_BossPolaris_Monster_Atk_FirstAtk` · `Ai_Mon_Special_BossPolaris_Monster_Atk_SecondAtk` · `Ai_Mon_Special_BossPolaris_Monster_JumpStomp_LargerExplosion` · `Ai_Mon_Special_BossPolaris_Monster_PizzaLightning_Instance` · `Ai_Mon_Special_BossPolaris_Monster_SlashDash` · `Ai_Mon_Special_BossPolaris_Monster_Smite_Instance` · `Ai_QR_DistortedMind_Damage` · `Ai_QR_InfernalTales` · `Ai_QR_Innocence_Explosion` · `Ai_Q_BigBorealChunk_Explosion` · `Ai_Q_CruelSun_Shockwave` · `Ai_Q_Discipline_Stomp` · `Ai_Q_EmbracingTheChill_AreaDoT` · `Ai_Q_EmbracingTheChill_Explosion` · `Ai_Q_Laceration_Dash` · `Ai_Q_MoonlightPact_Fenrir_Atk` · `Ai_Q_MoonlightPact_Land` · `Ai_Q_SylvanCall` · `Ai_Q_SylvanCall_LeafHound_Atk` · `Ai_R_BackOff_Damage` · `Ai_R_BaptismOfSun` · `Ai_R_BoneCrusher_Explosion` · `Ai_R_Cataclysm_Meteor` · `Ai_R_ChainReaction` · `Ai_R_DancingBlades` · `Ai_R_FlamingWhip` · `Ai_R_FrozenFists_PunchDash` · `Ai_R_GlacialHammer` · `Ai_R_Immolation_Damage` · `Ai_R_Lava_LavaField` · `Ai_RoomMod_FireDevil_Tornado` · `Ai_RoomMod_MeteoricLife_Explosion` · `Ai_Star_Cetus_F_BI_SelfDamageAoeCold_AOE` · `Ai_U_BigChomp` · `Ai_U_Burrow_Emerge` · `Ai_U_HerWorld_Explosion` · `Ai_U_Hysteria_Claw` · `Ai_U_ShoutOfOblivion` · [DashAttackInstance](/api/Global.DashAttackInstance) · [InstantDamageInstance](/api/Global.InstantDamageInstance) · [TickDamageInstance](/api/Global.TickDamageInstance)

### Dependencies (19)

*Types and components that `DamageInstance` references or depends upon:*

[AbilityInstance](/api/Global.AbilityInstance) · [AbilityTargetValidator](/api/Global.AbilityTargetValidator) · [Actor](/api/Global.Actor) · [CastInfo](/api/Global.CastInfo) · [Channel](/api/Global.Channel) · [ChannelData](/api/Global.ChannelData) · [DamageData](/api/Global.DamageData) · [DewCollider](/api/Global.DewCollider) · [DewEffect](/api/Global.DewEffect) · [DewNetworkBehaviour](/api/Global.DewNetworkBehaviour) · [Entity](/api/Global.Entity) · [EntityCheck](/api/Global.EntityCheck) · [EntityStatus](/api/Global.EntityStatus) · [EntityVisual](/api/Global.EntityVisual) · [Knockback](/api/Global.Knockback) · [ListReturnHandle`1](/api/Global.ListReturnHandle`1) · [SafeAction](/api/Global.SafeAction) · [SafeAction`1](/api/Global.SafeAction`1) · [ScalingValue](/api/Global.ScalingValue)

### Related Enums (2)

*Enumerations referenced in fields, properties, or method signatures:*

[`AttackEffectType`](/enums#attackeffecttype) · [`ElementalType`](/enums#elementaltype)

:::
