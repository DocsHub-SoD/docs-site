# Class: EntityAbility

- **Category:** <span class="cat-dot" style="--cat-color: #ef4444" data-cat="Combat & Abilities"></span> Combat & Abilities
- **Namespace:** `Global`
- **Assembly:** `Dew.Core.dll`
- **Inheritance / Derived:** [DewNetworkBehaviour](/api/Global.DewNetworkBehaviour) → [EntityComponent](/api/Global.EntityComponent)

```csharp
[HideMonoScript]
public class EntityAbility : EntityComponent, ILogicUpdate, ICleanup
```

## Fields (5)

::: details Click to expand Fields (5)

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`abilityPreset`** | `public AssetRef<AbilityTrigger>[] abilityPreset` |  |
| **`AttackAbilityIndex`** | `public const int AttackAbilityIndex = 63` |  |
| **`attackAbilityPreset`** | `public AssetRef<AttackTrigger> attackAbilityPreset` |  |
| **`ClientEvent_OnAbilityAdded`** | `public SafeAction<int, AbilityTrigger> ClientEvent_OnAbilityAdded` |  |
| **`ClientEvent_OnAbilityRemoved`** | `public SafeAction<int, AbilityTrigger> ClientEvent_OnAbilityRemoved` |  |

:::

## Properties (4)

::: details Click to expand Properties (4)

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`abilities`** | `public IReadOnlyDictionary<int, AbilityTrigger> abilities { get; }` |  |
| **`attackAbility`** | `public AbilityTrigger attackAbility { get; }` |  |
| **`originalAttackAbility`** | `public AttackTrigger originalAttackAbility { get; }` |  |
| **`overridenAttackAbility`** | `public AbilityTrigger overridenAttackAbility { get; }` |  |

:::

## Methods (17)

::: details `AddAbility(AbilityTrigger)`

Add an ability to this entity. It will be equipped on empty index between 0 and 127.

```csharp
public void AddAbility(AbilityTrigger trigger)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `trigger` | [`AbilityTrigger`](/api/Global.AbilityTrigger) |  |

:::

::: details `AddAbility&lt;T&gt;()`

Add an ability to this entity. It will be equipped on empty index between 0 and 127.

```csharp
public T AddAbility<T>() where T : AbilityTrigger
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `` | `T` |  |

**Returns:** `T`

:::

::: details `Awake()`

```csharp
protected override void Awake()
```

:::

::: details `GetAbility&lt;T&gt;()`

Get this entity's first ability of the given type. Can be null.

```csharp
public T GetAbility<T>() where T : AbilityTrigger
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `` | `T` |  |

**Returns:** `T`

:::

::: details `GetNewAbilityLockHandle(bool)`

```csharp
public AbilityLockHandle GetNewAbilityLockHandle(bool shouldShowLockIcon = false)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `shouldShowLockIcon` | `bool` |  |

**Returns:** `AbilityLockHandle`

:::

::: details `IsAbilityCastLocked(int)`

Is an ability locked by AbilityLockHandle? Available everywhere.

```csharp
public bool IsAbilityCastLocked(int index)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `index` | `int` |  |

**Returns:** `bool`

:::

::: details `IsAbilityEditLocked(int)`

```csharp
public bool IsAbilityEditLocked(int index)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `index` | `int` |  |

**Returns:** `bool`

:::

::: details `IsAttackAbilityLocked(int)`

```csharp
public bool IsAttackAbilityLocked(int index)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `index` | `int` |  |

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

::: details `RemoveAbility(int)`

```csharp
public AbilityTrigger RemoveAbility(int index)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `index` | `int` |  |

**Returns:** `AbilityTrigger`

:::

::: details `RemoveAttackAbility()`

Remove previous attack ability from this entity.

```csharp
public AbilityTrigger RemoveAttackAbility()
```

**Returns:** `AbilityTrigger`

:::

::: details `SetAbility(int, AbilityTrigger)`

Give this entity a new ability at the given index. Previously equipped ability will be unequipped.

```csharp
public void SetAbility(int index, AbilityTrigger trigger)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `index` | `int` |  |
| `trigger` | [`AbilityTrigger`](/api/Global.AbilityTrigger) |  |

:::

::: details `SetAttackAbility(AttackTrigger)`

Give a new attack ability to this entity. Previous one will be unequipped.

```csharp
public void SetAttackAbility(AttackTrigger trigger)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `trigger` | [`AttackTrigger`](/api/Global.AttackTrigger) |  |

:::

::: details `ShouldShowAbilityLockIcon(int)`

```csharp
public bool ShouldShowAbilityLockIcon(int index)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `index` | `int` |  |

**Returns:** `bool`

:::

::: details `TryGetAbility&lt;T&gt;(out T)`

```csharp
public bool TryGetAbility<T>(out T trigger) where T : AbilityTrigger
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `trigger` | `T` |  |
| `` | `T` |  |

**Returns:** `bool`

:::


## Architecture & Relationships

::: details Click to expand Architecture & Relationships

### Used By (126)

*Classes and systems that invoke, reference, or depend on `EntityAbility`:*

`ACH_THE_EIGHTH_TROPHY` · [AbilityLockHandle](/api/Global.AbilityLockHandle) · [AbilityTrigger](/api/Global.AbilityTrigger) · [ActionAttackMove](/api/Global.ActionAttackMove) · [ActionCast](/api/Global.ActionCast) · `Ai_D_ScarOfTheWind_DashAtk` · `Ai_GenericDodge` · `Ai_L_ButchersStrike` · `Ai_Mon_Ink_BossWhiteNight_Oppression` · `Ai_Mon_Primus_BossPrimusAeron_Dash` · `Ai_Mon_Primus_BossPrimusAeron_Force_Grab` · `Ai_Mon_Primus_BossPrimusAeron_Rage_DashAttack` · `Ai_Mon_Sky_BossNyx_StellarDash` · `Ai_Mon_SnowMountain_BossSkoll_DeathFromAbove` · `Ai_Mon_SnowMountain_VikingWarrior_Atk` · `Ai_Q_CruelSun` · `Ai_Q_Fleche_Dash` · `Ai_Q_Lunge` · `Ai_R_BackOff_Spawner` · `Ai_R_BaptismOfSun` · `Ai_R_Inspire_Roar` · `Ai_RandomGemUpgrade` · `At_Atk_YubarStardust` · `At_Mon_Despair_ParalyticFly_Atk` · `At_Mon_Forest_SpiderSpitter_Atk` · `At_Mon_Forest_SpiderSpitter_Melee` · `At_Mon_LavaLand_InfernoSpider_LavaAtk` · [CastIndicatorManager](/api/Global.CastIndicatorManager) · [ControlManager](/api/Global.ControlManager) · [EditSkillManager](/api/Global.EditSkillManager) · [EditSkillShrine](/api/Global.EditSkillShrine) · [Entity](/api/Global.Entity) · [EntityAI](/api/Global.EntityAI) · [EntityControl](/api/Global.EntityControl) · [GameResultManager](/api/Global.GameResultManager) · `Gem_C_Void` · `Gem_E_Obsidian` · `Gem_L_ChaosApple` · [HeroSkill](/api/Global.HeroSkill) · `Hero_Aurena` · `Hero_Bismuth` · `Hero_Bismuth_BookController` · [ISpawnableAsMiniBoss](/api/Global.ISpawnableAsMiniBoss) · `Mon_DarkCave_DarkElemental` · `Mon_DarkCave_NightOlm` · `Mon_DarkCave_Oppressor` · `Mon_Despair_Displacer` · `Mon_Despair_DreadBug` · `Mon_Despair_ParalyticFly` · `Mon_Forest_BossDemon` · `Mon_Forest_Hound` · `Mon_Forest_SpiderSpitter` · `Mon_Ink_Archer` · `Mon_Ink_BossDarkMoon` · `Mon_Ink_BossWhiteNight` · `Mon_Ink_DivineAnimal` · `Mon_LavaLand_FireElemental` · `Mon_LavaLand_InfernoSpider` · `Mon_Primus_BossPrimusAeron` · `Mon_Sky_Baam` · `Mon_Sky_BigBaam_Regular` · `Mon_Sky_BigBaam_Rooter` · `Mon_Sky_BossNyx` · `Mon_Sky_StarSeed` · `Mon_SnowMountain_IceElemental` · `Mon_SnowMountain_Scavenger` · `Mon_SnowMountain_SnowWolf` · `Mon_Special_BossErebos` · `Mon_Special_BossMaw` · `Mon_Special_BossObliviax` · `Mon_Special_BossPolaris` · [Monster](/api/Global.Monster) · `Primus_Ending` · `Se_C_Hemorrhage_EmpowerAttack` · `Se_Curse_DreamAfflictionParalytic` · `Se_Curse_SilentNight_Locked` · `Se_D_AstridsMasterpieceEnGarde` · `Se_D_AstridsMasterpiecePriorite` · `Se_D_BeautifulThreat` · `Se_D_ConvergencePoint` · `Se_D_DoubleTap` · `Se_D_ExoticMatter` · `Se_D_PrismaticEyes` · `Se_D_TheKillingFlow` · `Se_E_UmbralEdge` · `Se_FallenStar_WaveringIdentity` · `Se_GravityTraining` · `Se_HeroBleedingOut` · `Se_HunterBuff` · `Se_L_Multishot_Buff` · `Se_M_Charge` · `Se_M_Sprint` · `Se_MirageSkin_Oblivion_Silenced` · `Se_Mon_DarkCave_BossSeeker_Blink` · `Se_Mon_SnowMountain_SnowWolf_SlowApproach` · `Se_Mon_Special_BossPolaris_Monster_Scream_SkillLocked` · `Se_Q_IncendiaryRounds_EmpowerAttacks` · `Se_R_AnnihilationStance` · `Se_R_DangerousTheory` · `Se_R_Frostbite_EmpowerAttacks` · `Se_R_FrozenFists` · `Se_R_Parry_Start` · `Se_R_Tranquility` · `Se_RoomMod_UnstableVeilOfTime_ModifyCooldowns` · `Se_Star_Bismuth_F_IN_MoreProjByAtkSpd` · `Se_Star_Cetus_F_FR_CdReductionOnTakeDamage` · `Se_Star_Husk_F_AS_AddedDurationOnHit` · `Se_Star_Lacerta_D_AttackRange` · `Se_U_Burrow` · `Se_U_HerWorld_Blackhole` · `Se_U_Hysteria` · `St_D_ScarOfTheWind` · `St_L_HerosReturn` · [StarEffect](/api/Global.StarEffect) · `Star_Lacerta_AttackRange` · `Star_Lacerta_QuickTrigger` · `Star_Mist_LongerLunge` · `Star_Yubar_StrongerCataclysm` · `Star_Yubar_StrongerSuperNova` · [StatusEffect](/api/Global.StatusEffect) · `Sum_Q_SylvanCall_LeafHound` · `Sum_R_SummonLittleBaam_Baam` · `UI_Dev_ConsoleSelectedEntityInfo` · `UI_InGame_HeroDetailWindow` · `UI_InGame_HeroDetailWindow_StatItem` · `UI_InGame_SkillButton`

### Dependencies (17)

*Types and components that `EntityAbility` references or depends upon:*

[AbilityLockHandle](/api/Global.AbilityLockHandle) · [AbilityTrigger](/api/Global.AbilityTrigger) · [Actor](/api/Global.Actor) · [ActorCheck](/api/Global.ActorCheck) · [AssetRef`1](/api/Global.AssetRef`1) · [AttackTrigger](/api/Global.AttackTrigger) · [Dew](/api/Global.Dew) · [DewNetworkBehaviour](/api/Global.DewNetworkBehaviour) · [DewPlayer](/api/Global.DewPlayer) · [Entity](/api/Global.Entity) · [EntityComponent](/api/Global.EntityComponent) · [ICleanup](/api/Global.ICleanup) · `NetworkBehaviourDictionaryWrapper`2` · [NetworkedManagerBase`1](/api/Global.NetworkedManagerBase`1) · [SafeAction`1](/api/Global.SafeAction`1) · [SafeAction`2](/api/Global.SafeAction`2) · [SyncedNetworkBehaviour](/api/Global.SyncedNetworkBehaviour)

:::
