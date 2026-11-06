# Class: AttackTrigger

- **Category:** <span class="cat-dot" style="--cat-color: #ef4444" data-cat="Combat & Abilities"></span> Combat & Abilities
- **Namespace:** `Global`
- **Assembly:** `Dew.Core.dll`
- **Inheritance / Derived:** [DewNetworkBehaviour](/api/Global.DewNetworkBehaviour) → [Actor](/api/Global.Actor) → [AbilityTrigger](/api/Global.AbilityTrigger)

```csharp
public class AttackTrigger : AbilityTrigger, ILogicUpdate, ICleanup, ICustomDestroyRoutine
```

## Fields (2)

::: details Click to expand Fields (2)

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`allowNonTargetedCast`** | `public bool allowNonTargetedCast` |  |
| **`factor`** | `public ScalingValue factor` |  |

:::

## Methods (18)

::: details `Awake()`

```csharp
protected override void Awake()
```

:::

::: details `CallAttackCompleteBeforePrepareRoutines(EventInfoCast)`

```csharp
public void CallAttackCompleteBeforePrepareRoutines(EventInfoCast cast)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `cast` | [`EventInfoCast`](/api/Global.EventInfoCast) |  |

:::

::: details `CallAttackCompleteRoutines(AbilityInstance, int, CastInfo)`

```csharp
public void CallAttackCompleteRoutines(AbilityInstance newInstance, int configIndex, CastInfo info)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `newInstance` | [`AbilityInstance`](/api/Global.AbilityInstance) |  |
| `configIndex` | `int` |  |
| `info` | [`CastInfo`](/api/Global.CastInfo) |  |

:::

::: details `GetAnimationSpeed()`

```csharp
public override float GetAnimationSpeed()
```

**Returns:** `float`

:::

::: details `GetChannelDurationMultiplier()`

```csharp
public override float GetChannelDurationMultiplier()
```

**Returns:** `float`

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

::: details `GetPostDelayDurationMultiplier()`

```csharp
public override float GetPostDelayDurationMultiplier()
```

**Returns:** `float`

:::

::: details `OnCastCancelSetCooldownTime(int, CastInfo)`

```csharp
protected override void OnCastCancelSetCooldownTime(int configIndex, CastInfo info)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `configIndex` | `int` |  |
| `info` | [`CastInfo`](/api/Global.CastInfo) |  |

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

::: details `OnCastCompleteBeforePrepare(EventInfoCast)`

```csharp
public override void OnCastCompleteBeforePrepare(EventInfoCast cast)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `cast` | [`EventInfoCast`](/api/Global.EventInfoCast) |  |

:::

::: details `OnCastCompleteSetCharge(int, CastInfo)`

```csharp
public override void OnCastCompleteSetCharge(int configIndex, CastInfo info)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `configIndex` | `int` |  |
| `info` | [`CastInfo`](/api/Global.CastInfo) |  |

:::

::: details `OnCastCompleteSetCooldownTime(int, CastInfo)`

```csharp
public override void OnCastCompleteSetCooldownTime(int configIndex, CastInfo info)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `configIndex` | `int` |  |
| `info` | [`CastInfo`](/api/Global.CastInfo) |  |

:::

::: details `OnCastCompleteSetMinimumDelay(int, CastInfo)`

```csharp
public override void OnCastCompleteSetMinimumDelay(int configIndex, CastInfo info)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `configIndex` | `int` |  |
| `info` | [`CastInfo`](/api/Global.CastInfo) |  |

:::

::: details `OnCastStart(int, CastInfo)`

```csharp
public override void OnCastStart(int configIndex, CastInfo info)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `configIndex` | `int` |  |
| `info` | [`CastInfo`](/api/Global.CastInfo) |  |

:::

::: details `OnRotateForward(int, CastInfo)`

```csharp
protected override void OnRotateForward(int configIndex, CastInfo info)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `configIndex` | `int` |  |
| `info` | [`CastInfo`](/api/Global.CastInfo) |  |

:::

::: details `OnStartChannel(int, CastInfo)`

```csharp
protected override void OnStartChannel(int configIndex, CastInfo info)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `configIndex` | `int` |  |
| `info` | [`CastInfo`](/api/Global.CastInfo) |  |

:::

::: details `ProcessRange(float)`

```csharp
public override float ProcessRange(float original)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `original` | `float` |  |

**Returns:** `float`

:::

::: details `UpdateConfigIndexForCrit()`

```csharp
public void UpdateConfigIndexForCrit()
```

:::


## Architecture & Relationships

::: details Click to expand Architecture & Relationships

### Used By (84)

*Classes and systems that invoke, reference, or depend on `AttackTrigger`:*

`At_Atk_AurenaFeather` · `At_Atk_AurenaSwipe` · `At_Atk_BismuthRock` · `At_Atk_CetusStaff` · `At_Atk_HuskSword` · `At_Atk_LacertaRifle` · `At_Atk_MistSabre` · `At_Atk_NachiaStaff` · `At_Atk_VesperMace` · `At_Atk_YubarStardust` · `At_D_BurningFist_Attack` · `At_D_ScarOfTheWind_DashAtk` · `At_Mon_DarkCave_BossSeeker_Atk` · `At_Mon_DarkCave_CaveBat_Atk` · `At_Mon_DarkCave_CaveSpider_Atk` · `At_Mon_DarkCave_DarkElemental_Atk` · `At_Mon_DarkCave_NightOlm_Atk` · `At_Mon_DarkCave_Oppressor_Atk` · `At_Mon_Despair_BossAzurak_AltAtk` · `At_Mon_Despair_BossAzurak_Atk` · `At_Mon_Despair_Displacer_Atk` · `At_Mon_Despair_DreadBug_Atk` · `At_Mon_Despair_ParalyticFly_Atk` · `At_Mon_Despair_UnstableRat_Atk` · `At_Mon_Despair_WretchedArtillery_BarrageAtk` · `At_Mon_Forest_BossDemon_Atk` · `At_Mon_Forest_Hound_Atk` · `At_Mon_Forest_Scarab_Atk` · `At_Mon_Forest_SpiderSpitter_Atk` · `At_Mon_Forest_SpiderWarrior_Atk` · `At_Mon_Forest_Treant_MeleeAtk` · `At_Mon_Ink_Archer_Atk` · `At_Mon_Ink_BossDarkMoon_AltAk` · `At_Mon_Ink_BossDarkMoon_Blade` · `At_Mon_Ink_BossDarkMoon_Hammer` · `At_Mon_Ink_BossDarkMoon_ShortDash` · `At_Mon_Ink_BossWhiteNight_AltAtk` · `At_Mon_Ink_BossWhiteNight_Atk` · `At_Mon_Ink_DivineAnimal_Atk` · `At_Mon_Ink_EgoSword_Melee` · `At_Mon_Ink_GhostBlade_Atk` · `At_Mon_Ink_GhostBlade_MeleeAtk` · `At_Mon_Ink_GhostSpear_Atk` · `At_Mon_Ink_Tiger_Atk` · `At_Mon_LavaLand_BossInfernus_AltAtk` · `At_Mon_LavaLand_BossInfernus_Atk` · `At_Mon_LavaLand_FireElemental_LaserAtk` · `At_Mon_LavaLand_InfernoSpider_Atk` · `At_Mon_LavaLand_Magmadon_Atk` · `At_Mon_LavaLand_SuperheatedWolf_Atk` · `At_Mon_MorasDomain_NightmareBlob_Atk` · `At_Mon_Primus_BossPrimusAeron_Adapt_Atk` · `At_Mon_Primus_BossPrimusAeron_Force_Atk` · `At_Mon_Primus_BossPrimusAeron_Force_DropGiantSword` · `At_Mon_Primus_BossPrimusAeron_Force_Swipe` · `At_Mon_Primus_BossPrimusAeron_Rage_Atk` · `At_Mon_Sky_Baam_Atk` · `At_Mon_Sky_BigBaam_BeamAtk` · `At_Mon_Sky_BigBaam_Melee` · `At_Mon_Sky_BigBaam_RangedAtk` · `At_Mon_Sky_BossNyx_Atk` · `At_Mon_Sky_BossNyx_LaserAtk` · `At_Mon_Sky_LittleBaam_Atk` · `At_Mon_Sky_StarSeed_Atk` · `At_Mon_Sky_StellaMatter_Atk` · `At_Mon_SnowMountain_BossSkoll_Atk` · `At_Mon_SnowMountain_IceElemental_Atk` · `At_Mon_SnowMountain_LivingShards_Atk` · `At_Mon_SnowMountain_Scavenger_Atk` · `At_Mon_SnowMountain_SnowWolf_Atk` · `At_Mon_SnowMountain_VikingWarrior_Atk` · `At_Mon_Special_BossErebos_Atk` · `At_Mon_Special_BossLightElemental_BeamAtk` · `At_Mon_Special_BossMaw_Atk` · `At_Mon_Special_BossMaw_MoonlightPact_Atk` · `At_Mon_Special_BossObliviax_Atk` · `At_Mon_Special_BossPolaris_Holy_Atk` · `At_Mon_Special_BossPolaris_Monster_Atk` · `At_Q_MoonlightPact_Fenrir_Atk` · `At_Q_SylvanCall_LeafHound_Atk` · `At_R_FrozenFists_Attack` · `At_R_SummonLittleBaam_Baam_Atk` · [EntityAbility](/api/Global.EntityAbility) · `Se_D_PrismaticEyes`

### Dependencies (12)

*Types and components that `AttackTrigger` references or depends upon:*

[AbilityInstance](/api/Global.AbilityInstance) · [AbilityTrigger](/api/Global.AbilityTrigger) · [CastInfo](/api/Global.CastInfo) · [Channel](/api/Global.Channel) · [DewPlayer](/api/Global.DewPlayer) · [Entity](/api/Global.Entity) · [EntityControl](/api/Global.EntityControl) · [EntityStatus](/api/Global.EntityStatus) · [EventInfoCast](/api/Global.EventInfoCast) · [SafeAction`1](/api/Global.SafeAction`1) · [TriggerChannelData](/api/Global.TriggerChannelData) · [TriggerConfig](/api/Global.TriggerConfig)

:::
