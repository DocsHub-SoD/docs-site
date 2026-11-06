# Class: DewAnimationClip

- **Category:** <span class="cat-dot" style="--cat-color: #64748b" data-cat="Misc & Utility"></span> Misc & Utility
- **Namespace:** `Global`
- **Assembly:** `Dew.Core.dll`
- **Attributes:** `[DewResourceLink] [CreateAssetMenu]`

```csharp
[HideMonoScript]
[DewResourceLink(ResourceLinkBy.Guid)]
[CreateAssetMenu(fileName = "New Dew Animation Clip", menuName = "Dew Animation Clip")]
public class DewAnimationClip : ScriptableObject, ILinkedByGuid
```

## Fields (5)

::: details Click to expand Fields (5)

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`entries`** | `public DewAnimationEntry[] entries` |  |
| **`hideWeaponOnHeroes`** | `public bool hideWeaponOnHeroes` |  |
| **`onlyUpperBody`** | `public bool onlyUpperBody` |  |
| **`overrideWalk`** | `[InfoBox("Override Walk cannot be Full if animating only upper body!", InfoMessageType.Error, null, VisibleIf = "@onlyUpperBody && overrideWalk == DewAnimationClip.OverrideWalkBehavior.Full")] public DewAnimationClip.OverrideWalkBehavior overrideWalk` |  |
| **`overrideWalkNormalizedDuration`** | `[ShowIf("@overrideWalk != OverrideWalkBehavior.None", true)] public float overrideWalkNormalizedDuration` |  |

:::

## Properties (1)

::: details Click to expand Properties (1)

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`resourceId`** | `public string resourceId { get; set; }` |  |

:::

## Methods (6)

::: details `GetEntry()`

```csharp
public DewAnimationEntry GetEntry()
```

**Returns:** `DewAnimationEntry`

:::

::: details `GetEntry(int)`

```csharp
public DewAnimationEntry GetEntry(int index)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `index` | `int` |  |

**Returns:** `DewAnimationEntry`

:::

::: details `GetEntry(float)`

```csharp
public DewAnimationEntry GetEntry(float value)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `value` | `float` |  |

**Returns:** `DewAnimationEntry`

:::

::: details `GetEntryIndex()`

```csharp
public int GetEntryIndex()
```

**Returns:** `int`

:::

::: details `GetEntryIndex(float, int)`

```csharp
public static int GetEntryIndex(float clipSelectValue, int entriesLength)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `clipSelectValue` | `float` |  |
| `entriesLength` | `int` |  |

**Returns:** `int`

:::

::: details `GetEntryIndex(float)`

```csharp
public int GetEntryIndex(float clipSelectValue)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `clipSelectValue` | `float` |  |

**Returns:** `int`

:::


## Architecture & Relationships

::: details Click to expand Architecture & Relationships

### Used By (141)

*Classes and systems that invoke, reference, or depend on `DewAnimationClip`:*

`Ai_Atk_AurenaSwipe` · `Ai_C_BeamOfLight` · `Ai_C_Whirlwind` · `Ai_D_ParryMaster_Parry` · `Ai_D_RoaringFist` · `Ai_E_JusticeGuillotine` · `Ai_E_Permafrost` · `Ai_E_WinterDive` · `Ai_EmbraceNewIdentity` · `Ai_GenericDodge` · `Ai_L_SmallMoltenCore_Dragon_Atk` · `Ai_Mon_DarkCave_BossSeeker_Atk` · `Ai_Mon_DarkCave_BossSeeker_TunnelVision_Claw` · `Ai_Mon_DarkCave_BossSeeker_TunnelVision_SecondPoolAtk` · `Ai_Mon_DarkCave_BossSeeker_YellowDiagram_MainInstance` · `Ai_Mon_Despair_BossAzurak_DoubleStomp` · `Ai_Mon_Despair_BossAzurak_RoarAtk` · `Ai_Mon_Despair_BossAzurak_Roll` · `Ai_Mon_Forest_BossDemon_AltSkill_LineAtk_Spawner` · `Ai_Mon_Forest_BossDemon_AltSkill_Stomp` · `Ai_Mon_Forest_BossDemon_DelayedAtk` · `Ai_Mon_Forest_BossDemon_MainSkill_SpawnMissiles` · `Ai_Mon_Forest_BossDemon_SpecialAtk` · `Ai_Mon_Forest_Hound_Charge` · `Ai_Mon_Ink_BossDarkMoon_AltAtk_Spawner` · `Ai_Mon_Ink_BossDarkMoon_Blade` · `Ai_Mon_Ink_BossDarkMoon_Blade_RageInstance` · `Ai_Mon_Ink_BossDarkMoon_Eclipse` · `Ai_Mon_Ink_BossDarkMoon_Eclipse_Instance` · `Ai_Mon_Ink_BossDarkMoon_Hammer` · `Ai_Mon_Ink_BossDarkMoon_ShortDash` · `Ai_Mon_Ink_BossDarkMoon_Spear` · `Ai_Mon_Ink_BossDarkMoon_Spear_Instance` · `Ai_Mon_Ink_BossDarkMoon_TeleportAtk` · `Ai_Mon_Ink_BossDarkMoon_ThrowSpear_Spawner` · `Ai_Mon_Ink_BossWhiteNIght_BuddhasPalm_Spawner` · `Ai_Mon_Ink_BossWhiteNight_AltAtk_Ready` · `Ai_Mon_Ink_BossWhiteNight_Cataclysm` · `Ai_Mon_Ink_BossWhiteNight_Cataclysm_Instance` · `Ai_Mon_Ink_BossWhiteNight_DestructionWave` · `Ai_Mon_Ink_BossWhiteNight_DestructionWave_Wave` · `Ai_Mon_Ink_BossWhiteNight_EnergyWave_Spawner` · `Ai_Mon_Ink_BossWhiteNight_Oppression` · `Ai_Mon_Ink_BossWhiteNight_Ready` · `Ai_Mon_Ink_DivineAnimal_Bite` · `Ai_Mon_Ink_EgoSword_Atk` · `Ai_Mon_Ink_GhostBlade_SwiftStep` · `Ai_Mon_Ink_GhostBlade_SwiftStep_Atk` · `Ai_Mon_Ink_GhostSpear_Atk` · `Ai_Mon_LavaLand_BossInfernus_AltAtk` · `Ai_Mon_LavaLand_BossInfernus_Atk` · `Ai_Mon_LavaLand_BossInfernus_Dash` · `Ai_Mon_LavaLand_BossInfernus_Jump` · `Ai_Mon_LavaLand_BossInfernus_PowerBomb` · `Ai_Mon_LavaLand_BossInfernus_Roar` · `Ai_Mon_LavaLand_FireElemental_DestructSub` · `Ai_Mon_LavaLand_SuperheatedWolf_SelfDestruct` · `Ai_Mon_Sky_Baam_TeleportSequence` · `Ai_Mon_Sky_BossNyx_Blackhole` · `Ai_Mon_Sky_BossNyx_PullAtk` · `Ai_Mon_Sky_BossNyx_StellarDash` · `Ai_Mon_SnowMountain_BossSkoll_Atk` · `Ai_Mon_SnowMountain_BossSkoll_AuraBladeRain` · `Ai_Mon_SnowMountain_BossSkoll_AuraExplosion_Spawner` · `Ai_Mon_SnowMountain_BossSkoll_AuraSlice` · `Ai_Mon_SnowMountain_BossSkoll_DeathFromAbove` · `Ai_Mon_SnowMountain_BossSkoll_Whirlwind` · `Ai_Mon_SnowMountain_Scavenger_Atk` · `Ai_Mon_SnowMountain_Scavenger_Jump` · `Ai_Mon_SnowMountain_VikingWarrior_ThrowShield` · `Ai_Mon_Special_BossErebos_AntiGravity_Instance` · `Ai_Mon_Special_BossErebos_AntiGravity_Spawner` · `Ai_Mon_Special_BossErebos_Ripple` · `Ai_Mon_Special_BossErebos_SpawnBlackhole` · `Ai_Mon_Special_BossLightElemental_BeamAtk_Spawner` · `Ai_Mon_Special_BossLightElemental_BeamBarrage` · `Ai_Mon_Special_BossMaw_AnnihilationStance` · `Ai_Mon_Special_BossMaw_Cataclysm_Spawner` · `Ai_Mon_Special_BossMaw_ChainReaction` · `Ai_Mon_Special_BossMaw_Chomp_DashAtk` · `Ai_Mon_Special_BossMaw_MoonlightPact` · `Ai_Mon_Special_BossMaw_MoonlightPact_Atk` · `Ai_Mon_Special_BossMaw_PrecisionShot` · `Ai_Mon_Special_BossMaw_ScatterShot_Spawner` · `Ai_Mon_Special_BossMaw_SliceThroat` · `Ai_Mon_Special_BossMaw_SliceThroat_Atk` · `Ai_Mon_Special_BossObliviax_Artillery` · `Ai_Mon_Special_BossObliviax_Atk` · `Ai_Mon_Special_BossObliviax_BackStep` · `Ai_Mon_Special_BossObliviax_BackStep_Instance` · `Ai_Mon_Special_BossObliviax_ChargeSequence_Ready` · `Ai_Mon_Special_BossObliviax_ChargeSequence_Spawner` · `Ai_Mon_Special_BossObliviax_DashAtk_ExtraAtk` · `Ai_Mon_Special_BossObliviax_Laugh` · `Ai_Mon_Special_BossObliviax_NeedleAtk` · `Ai_Mon_Special_BossObliviax_NeedleAtk_Ready` · `Ai_Mon_Special_BossObliviax_TurretMode` · `Ai_Q_Fleche_Dash` · `Ai_Q_Laceration_Circle` · `Ai_Q_Laceration_Dash` · `Ai_Q_Lunge` · `Ai_Q_MoonlightPact` · `Ai_Q_MoonlightPact_Fenrir_Atk` · `Ai_Q_SuperNova` · `Ai_R_GreatFrostSword` · `Ai_R_StaticDischarge` · `Ai_Star_Bismuth_F_IT_SmallerRingAddDisplacement_Dash` · `Ai_U_BigChomp` · `Ai_U_Hysteria_Claw` · `Ai_U_WorldCracker` · `At_Atk_HuskSword` · [ChargingChannelData](/api/Global.ChargingChannelData) · [EntityAnimation](/api/Global.EntityAnimation) · [EntityVisual](/api/Global.EntityVisual) · [FxEntityAnimation](/api/Global.FxEntityAnimation) · `Mon_SnowMountain_BossSkoll` · `NetworkReaderWriterExtensions` · `PlayTutorial_Tutorial_Intro` · `Se_D_ExoticMatter` · `Se_FatalHitProtection_Invulnerable` · `Se_M_Charge` · `Se_M_Endure` · `Se_Mon_DarkCave_BossSeeker_Hallucination` · `Se_Mon_DarkCave_BossSeeker_Substitution` · `Se_Mon_DarkCave_BossSeeker_TunnelVision` · `Se_Mon_Ink_Boss_PhaseChange` · `Se_Mon_Sky_BossNyx_IntrudeErebos` · `Se_Mon_Sky_BossNyx_PhaseChange` · `Se_Mon_Special_BossErebos_PhaseChange` · `Se_Mon_Special_BossMaw_Flee` · `Se_Q_Discipline_Jump` · `Se_R_AnnihilationStance` · `Se_R_Parry_Start` · `Se_R_RepulsiveShield` · `Se_R_Tranquility` · `Se_Star_Aurena_F_CR_ChargedCast` · `Se_U_BeamOfBalance` · `Se_U_HerWorld_Blackhole` · `Se_WaypointTeleport` · `St_L_HerosReturn` · [TriggerConfig](/api/Global.TriggerConfig)

### Dependencies (2)

*Types and components that `DewAnimationClip` references or depends upon:*

[DewAnimationEntry](/api/Global.DewAnimationEntry) · [ILinkedByGuid](/api/Global.ILinkedByGuid)

:::
