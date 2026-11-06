# Class: Knockback

- **Category:** <span class="cat-dot" style="--cat-color: #64748b" data-cat="Misc & Utility"></span> Misc & Utility
- **Namespace:** `Global`
- **Assembly:** `Dew.Core.dll`

```csharp
[Serializable]
public class Knockback
```

## Fields (3)

::: details Click to expand Fields (3)

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`distance`** | `public float distance` |  |
| **`duration`** | `public float duration` |  |
| **`ignoreTenacity`** | `public bool ignoreTenacity` |  |

:::

## Methods (3)

::: details `ApplyWithDirection(Quaternion, Entity)`

```csharp
public void ApplyWithDirection(Quaternion rot, Entity to)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `rot` | `UnityEngine.Quaternion` |  |
| `to` | [`Entity`](/api/Global.Entity) |  |

:::

::: details `ApplyWithDirection(Vector3, Entity)`

```csharp
public void ApplyWithDirection(Vector3 dir, Entity to)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `dir` | `UnityEngine.Vector3` |  |
| `to` | [`Entity`](/api/Global.Entity) |  |

:::

::: details `ApplyWithOrigin(Vector3, Entity)`

```csharp
public void ApplyWithOrigin(Vector3 origin, Entity to)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `origin` | `UnityEngine.Vector3` |  |
| `to` | [`Entity`](/api/Global.Entity) |  |

:::


## Architecture & Relationships

::: details Click to expand Architecture & Relationships

### Used By (107)

*Classes and systems that invoke, reference, or depend on `Knockback`:*

`Ai_C_BackStep_Bomb` · `Ai_C_IceClaw` · `Ai_C_Pew_Projectile` · `Ai_D_BurningFist_Attack` · `Ai_D_Resolve_Push` · `Ai_E_JusticeGuillotine` · `Ai_E_SearingCharge` · `Ai_E_StygianRush_Rush` · `Ai_GlacialBarrier_Spawn` · `Ai_Hatred_Explosion` · `Ai_L_SoulKiller` · `Ai_L_SoulKiller_Soul` · `Ai_Mon_DarkCave_BossSeeker_PurpleOrb` · `Ai_Mon_DarkCave_NightOlm_Atk_Projectile` · `Ai_Mon_Despair_BossAzurak_AltAtk` · `Ai_Mon_Despair_BossAzurak_DoubleStomp_Instance` · `Ai_Mon_Despair_BossAzurak_RoarAtk` · `Ai_Mon_Despair_BossAzurak_Roll` · `Ai_Mon_Despair_BossAzurak_StompProjectile` · `Ai_Mon_Despair_BossAzurak_StompProjectile_Projectile` · `Ai_Mon_Despair_Displacer_SpawnEgg` · `Ai_Mon_Despair_ParalyticFly_Paralyze` · `Ai_Mon_Forest_BossDemon_MainSkill_Stomp` · `Ai_Mon_Forest_BossDemon_MainSkill_Stomp_Tree` · `Ai_Mon_Forest_Hound_Charge` · `Ai_Mon_Forest_Treant_PowerBomb` · `Ai_Mon_Ink_Archer_Dodge` · `Ai_Mon_Ink_BossDarkMoon_Blade_Instance` · `Ai_Mon_Ink_BossDarkMoon_Blade_RageInstance` · `Ai_Mon_Ink_BossDarkMoon_Eclipse_Instance` · `Ai_Mon_Ink_BossDarkMoon_ShortDash_Atk` · `Ai_Mon_Ink_BossDarkMoon_SpawnEgoSword_Projectile` · `Ai_Mon_Ink_BossDarkMoon_ThrowSpear_Projectile` · `Ai_Mon_Ink_BossDarkMoon_ThrowSpear_TeleportAtk_AfterAtk` · `Ai_Mon_Ink_BossWhiteNight_AltAtk` · `Ai_Mon_Ink_BossWhiteNight_Cataclysm_Instance` · `Ai_Mon_Ink_BossWhiteNight_DestructionWave_Wave` · `Ai_Mon_Ink_BossWhiteNight_RageInstance_Rock` · `Ai_Mon_Ink_DivineAnimal_Stomp` · `Ai_Mon_Ink_EgoSword_Atk` · `Ai_Mon_Ink_GhostBlade_DemolitionMan` · `Ai_Mon_Ink_GhostBlade_SwiftStep_Atk` · `Ai_Mon_Ink_GhostBlade_SwiftStep_Projectile` · `Ai_Mon_Ink_GhostSpear_Atk` · `Ai_Mon_LavaLand_BossInfernus_Roar_Projectile` · `Ai_Mon_LavaLand_FireElemental_DestructSub` · `Ai_Mon_LavaLand_FireElemental_LaserAtk` · `Ai_Mon_LavaLand_Magmadon_Charge` · `Ai_Mon_LavaLand_Magmadon_Charge_Projectile` · `Ai_Mon_LavaLand_SuperheatedWolf_SelfDestruct` · `Ai_Mon_Primus_BossPrimusAeron_Adapt_Arbalest_Projectile` · `Ai_Mon_Primus_BossPrimusAeron_Adapt_IceClaw` · `Ai_Mon_Primus_BossPrimusAeron_Rage_MassDelusion` · `Ai_Mon_Primus_SpawnAttack` · `Ai_Mon_Sky_Baam_Teleport` · `Ai_Mon_Sky_BossNyx_LineAtk_Displacement` · `Ai_Mon_Sky_BossNyx_StarBuff_Projectile` · `Ai_Mon_Sky_StellaMatter_AtkSub` · `Ai_Mon_SnowMountain_BossSkoll_AuraSlice` · `Ai_Mon_SnowMountain_BossSkoll_SummonArrow_Instance` · `Ai_Mon_Special_BossErebos_AtkInstance` · `Ai_Mon_Special_BossErebos_Gaze_Instance` · `Ai_Mon_Special_BossErebos_Ripple` · `Ai_Mon_Special_BossErebos_StarRain_Instance` · `Ai_Mon_Special_BossErebos_Teleport_Instance` · `Ai_Mon_Special_BossMaw_Chomp_Charge` · `Ai_Mon_Special_BossMaw_Chomp_DashAtk` · `Ai_Mon_Special_BossMaw_PrecisionShot_Projectile` · `Ai_Mon_Special_BossMaw_ScatterShot_ShortProjectile` · `Ai_Mon_Special_BossMaw_ShadowOverdrive_Projectile` · `Ai_Mon_Special_BossMaw_ShadowWalk_Projectile` · `Ai_Mon_Special_BossMaw_SliceThroat_Atk` · `Ai_Mon_Special_BossObliviax_Artillery_Instance` · `Ai_Mon_Special_BossObliviax_BackStep_Instance` · `Ai_Mon_Special_BossObliviax_DashAtk` · `Ai_Mon_Special_BossObliviax_NeedleAtk_AtkInstance` · `Ai_Mon_Special_BossObliviax_NeedleAtk_Instance` · `Ai_Mon_Special_BossObliviax_TurnAtk` · `Ai_Mon_Special_BossObliviax_TurnAtk_DelayedAtk` · `Ai_Mon_Special_BossObliviax_TurretMode_Projectile` · `Ai_QR_ValiantHeart` · `Ai_Q_HandCannon` · `Ai_R_BlackArbalest` · `Ai_R_Fireball` · `Ai_R_GreatFrostSword` · `Ai_R_Parry_Projectile` · `Ai_R_PhantomBlade` · `Ai_R_PrecisionShot_Projectile` · `Ai_R_RepulsiveShield_Projectile` · `Ai_R_StaticDischarge` · `Ai_Sky_BossIntruder_Instance` · `Ai_Trap_ArrowShooter_Arrow` · `Ai_UnstableRatSwarm_Projectile` · [DamageInstance](/api/Global.DamageInstance) · `Se_C_IceBlock` · `Se_FatalHitProtection_Invulnerable` · `Se_M_Charge` · `Se_MiniBoss_UnstableExplosive_Explosion` · `Se_MirageSkin_Pulverization` · `Se_Mon_Ink_BossWhiteNight_Rush` · `Se_Mon_Primus_BossPrimusAeron_PhaseSwitcher` · `Se_Mon_Sky_BossNyx_PhaseChange` · `Se_R_DangerousTheory` · `Se_Star_Mist_F_LG_SingleTarget` · `Se_Treasure_FragmentOfDetermination_Invulnerable` · `Shrine_PrimusDoor` · `SpawnGemStarProp`

### Dependencies (6)

*Types and components that `Knockback` references or depends upon:*

[Actor](/api/Global.Actor) · [ClientEventManager](/api/Global.ClientEventManager) · [Entity](/api/Global.Entity) · [EntityControl](/api/Global.EntityControl) · [EntityStatus](/api/Global.EntityStatus) · [NetworkedManagerBase`1](/api/Global.NetworkedManagerBase`1)

:::
