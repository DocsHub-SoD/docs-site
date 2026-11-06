# Class: BasicEffectWithStrength

- **Category:** <span class="cat-dot" style="--cat-color: #a855f7" data-cat="Buffs & Statuses"></span> Buffs & Statuses
- **Namespace:** `Global`
- **Assembly:** `Dew.Core.dll`
- **Inheritance / Derived:** [BasicEffect](/api/Global.BasicEffect) → [ArmorBoostEffect](/api/Global.ArmorBoostEffect) → [ArmorReductionEffect](/api/Global.ArmorReductionEffect) → [CrippleEffect](/api/Global.CrippleEffect) → [FakeMaxHealthEffect](/api/Global.FakeMaxHealthEffect) → [HasteEffect](/api/Global.HasteEffect) → [SlowEffect](/api/Global.SlowEffect) → [SpeedEffect](/api/Global.SpeedEffect)

```csharp
public abstract class BasicEffectWithStrength : BasicEffect
```

## Properties (2)

::: details Click to expand Properties (2)

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`decay`** | `public bool decay { get; set; }` | If true, strength will be scaled to remaining duration of the status effect.Works only if the status effect has a timer active. |
| **`strength`** | `public float strength { get; set; }` |  |

:::


## Architecture & Relationships

::: details Click to expand Architecture & Relationships

### Used By (69)

*Classes and systems that invoke, reference, or depend on `BasicEffectWithStrength`:*

`Ai_C_BeamOfLight` · `Ai_Curse_AnchorOfMind_Anchor` · `Ai_Curse_IntermittentExplosion_Explosion` · `Ai_E_FinalExplosion_Explosion` · `Ai_HunterArtillery_Small` · `Ai_L_ButchersStrike` · `Ai_Mon_DarkCave_Oppressor_Hypnotize` · `Ai_Mon_Ink_BossDarkMoon_ThrowSpear_TeleportAtk` · `Ai_Mon_LavaLand_FireElemental_Explosion` · `Ai_Mon_LavaLand_FireElemental_ExplosionSub` · `Ai_Mon_LavaLand_FireElemental_LaserAtk` · `Ai_Mon_Primus_BossPrimusAeron_Force_Grab` · `Ai_Mon_Sky_BossNyx_StellarDash` · `Ai_Mon_SnowMountain_BossSkoll_Whirlwind` · `Ai_Mon_Special_BossObliviax_NeedleAtk_Ready` · `Ai_Mon_Special_BossPolaris_Monster_Scream` · `Ai_QR_Innocence_Explosion` · `Ai_Q_BigBorealChunk_Spawner` · `Ai_Q_Fleche_Dash` · `Ai_Q_Laceration_Circle` · `Ai_Q_SuperNova` · `Ai_R_FlamingWhip` · `Ai_R_Somersault` · `Ai_R_StaticDischarge` · [ArmorBoostEffect](/api/Global.ArmorBoostEffect) · [ArmorReductionEffect](/api/Global.ArmorReductionEffect) · [ChargingChannel](/api/Global.ChargingChannel) · [CrippleEffect](/api/Global.CrippleEffect) · [EntityStatus](/api/Global.EntityStatus) · [FakeMaxHealthEffect](/api/Global.FakeMaxHealthEffect) · `Gem_L_Supersymmetry` · `Gem_R_NightSky` · [HasteEffect](/api/Global.HasteEffect) · `Mon_Special_BossPolaris` · `Primus_Ending` · `Se_D_AstridsMasterpiecePriorite` · `Se_D_BeautifulThreat` · `Se_D_MercyOfEl` · `Se_E_Harvest_OnVictim` · `Se_E_UmbralEdge` · `Se_Elm_Cold` · `Se_FishScales` · `Se_Gem_C_Quicksilver` · `Se_M_Sprint` · `Se_MiniBoss_BloodThorn_ThornSpawner` · `Se_MiniBoss_UnstableExplosive_Explosion` · `Se_Mon_Ink_BossWhiteNight_Rush` · `Se_Mon_SnowMountain_SnowWolf_SlowApproach` · `Se_MonsterSprint` · `Se_Q_IncendiaryRounds_EmpowerAttacks` · `Se_R_BoneCrusher` · `Se_R_NightSky_AtkSpd` · `Se_R_UnbreakableDetermination` · `Se_Star_Bismuth_L_ContinuousSpeed` · `Se_Star_Cetus_F_BA_ChargeMsNoShield` · `Se_Star_Lacerta_L_SpeedAfterDodge` · `Se_Star_Nachia_D_SummonAtkSpd` · `Se_Star_Nachia_F_MP_StrongerFenrirNoCast` · `Se_Star_Nachia_F_SC_AtkSpd` · `Se_Star_Nachia_I_ForestKillDreamDust` · `Se_Star_Nachia_L_SummonBonus` · `Se_U_HerWorld_Blackhole` · [SlowEffect](/api/Global.SlowEffect) · [SpeedEffect](/api/Global.SpeedEffect) · `Star_Global_Armor` · `Star_Lacerta_HandCannon` · `Star_Vesper_Armor` · [StatusEffect](/api/Global.StatusEffect) · [Summon](/api/Global.Summon)

### Dependencies (3)

*Types and components that `BasicEffectWithStrength` references or depends upon:*

[BasicEffect](/api/Global.BasicEffect) · [Entity](/api/Global.Entity) · [EntityStatus](/api/Global.EntityStatus)

:::
