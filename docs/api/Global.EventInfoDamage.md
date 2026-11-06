# Struct: EventInfoDamage

- **Category:** <span class="cat-dot" style="--cat-color: #ef4444" data-cat="Combat & Abilities"></span> Combat & Abilities
- **Namespace:** `Global`
- **Assembly:** `Dew.Core.dll`

```csharp
public struct EventInfoDamage
```

## Fields (5)

::: details Click to expand Fields (5)

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`actor`** | `public Actor actor` | The actor who invoked this event in an actor chain. |
| **`chain`** | `[NonSerialized] public ReactionChain chain` |  |
| **`damage`** | `public FinalDamageData damage` |  |
| **`negatedAmountByShield`** | `public float negatedAmountByShield` |  |
| **`victim`** | `public Entity victim` |  |

:::


## Architecture & Relationships

::: details Click to expand Architecture & Relationships

### Used By (116)

*Classes and systems that invoke, reference, or depend on `EventInfoDamage`:*

`ACH_ANGER_MANAGEMENT_PROFESSIONAL` · `ACH_SIBLING_FIGHT` · [Actor](/api/Global.Actor) · `Ai_Mon_Special_BossObliviax_NeedleAtk_Ready` · [CameraManager](/api/Global.CameraManager) · [ClientEventManager](/api/Global.ClientEventManager) · [Entity](/api/Global.Entity) · [EntityVisual](/api/Global.EntityVisual) · [FlavourManager](/api/Global.FlavourManager) · [Gem](/api/Global.Gem) · `Gem_C_Charcoal` · `Gem_C_Nap` · `Gem_C_Quicksilver` · `Gem_C_Vengeance` · `Gem_E_Apathy` · `Gem_E_Blossom` · `Gem_E_Clemency` · `Gem_E_Fever` · `Gem_E_Insight` · `Gem_E_Pain` · `Gem_E_Reflex` · `Gem_E_Twilight` · `Gem_E_Umbra` · `Gem_L_CamillasGift` · `Gem_L_Paranoia` · `Gem_L_Supersymmetry` · `Gem_R_Abyss` · `Gem_R_Accuracy` · `Gem_R_Blade` · `Gem_R_Blood` · `Gem_R_Control` · `Gem_R_Flow` · `Gem_R_Frost` · `Gem_R_Hedgehog` · `Gem_R_Mortality` · `Gem_R_NightSky` · `Gem_R_Panic` · `Gem_R_Ricochet` · `Gem_R_Rigidity` · `Gem_R_Snow` · `Gem_R_Wound` · `Gem_U_EternalFlame` · `Gem_U_GlacialCore` · `HealthThresholdBonusStarEffect` · `Ink_SecondCutscenePlay` · [KillTracker](/api/Global.KillTracker) · [MirageSkinEffect](/api/Global.MirageSkinEffect) · `Mon_DarkCave_CaveSpider` · `Mon_DarkCave_DarkElemental` · `Mon_DarkCave_NightOlm` · `Mon_Ink_BossDarkMoon` · `Mon_Ink_BossWhiteNight` · `Mon_Ink_Tiger` · `Mon_Sky_BossNyx` · `Mon_Special_BossErebos` · `Mon_Special_BossPolaris` · [PropEntity](/api/Global.PropEntity) · `Se_Curse_AmplifiedPain` · `Se_Curse_Electrified` · `Se_Curse_FateOfGreed` · `Se_Curse_VainDream` · `Se_D_ChargedAnguillian` · `Se_E_LizardlyBlessing` · `Se_FallenStar_MonsterReinforcement` · `Se_FishScales` · `Se_GenericStealth` · `Se_HeroOneShotProtection` · `Se_MirageSkin_Delusion` · `Se_MirageSkin_Oblivion` · `Se_MirageSkin_Oppression` · `Se_MirageSkin_Pulverization` · `Se_MirageSkin_Sanctification_Protected` · `Se_Mon_DarkCave_BossSeeker_Substitution` · `Se_Mon_Ink_Tiger_Walk` · `Se_Mon_Primus_BossPrimusAeron_Adaptation` · `Se_Mon_SnowMountain_SnowWolf_SlowApproach` · `Se_Mon_Special_BossMaw_ShieldConversion` · `Se_Mon_Special_BossPolaris_Adaptation` · `Se_Mon_Special_BossPolaris_Holy_CounterSpell` · `Se_Mon_Special_BossPolaris_Holy_ShortInvul` · `Se_MorasDomain_MorasCreation` · `Se_MorasDomain_MorasCreation_Boss` · `Se_R_Composure_Buff` · `Se_R_UnbreakableDetermination` · `Se_Shrine_Chaos_StatBonus` · `Se_Star_Aurena_F_CR_EarnGold` · `Se_Star_Aurena_I_GoldOnMerchantDamage` · `Se_Star_Aurena_L_SpeedOnDamage` · `Se_Star_Bismuth_D_Conquerer_Stacks` · `Se_Star_Bismuth_F_VH_Shield` · `Se_Star_Cetus_D_StackStatsOnTakenDamage` · `Se_Star_Cetus_F_BA_CdReductionOnKill` · `Se_Star_Cetus_F_FR_CdReductionOnTakeDamage` · `Se_Star_Cetus_F_FR_ChangeToUltHitReset` · `Se_Star_Cetus_L_DodgeCdReductionOnHit` · `Se_Star_Cetus_L_HealOnApDamage` · `Se_Star_D_CritUpHitDecay` · `Se_Star_Husk_D_DamageOverTimeCritWithPenalty` · `Se_Star_Husk_F_AS_AddedDurationOnHit` · `Se_Star_Husk_F_DC_RecentDamageHoTWhileStealth` · `Se_Star_I_GoldRiskAndReturn` · `Se_Star_L_PostHitDamageImmune` · `Se_Star_Mist_L_ArmorWithPenalty` · `Se_Star_Yubar_F_EI_BiggerExplosion` · `Se_Star_Yubar_F_SN_DodgeReset` · `Se_U_EternalFlame_Curse` · `Se_WaypointTeleport` · [SkillTrigger](/api/Global.SkillTrigger) · `Sky_BossIntruder` · `St_D_IcyVeins` · `Star_Yubar_EtherealInfluenceCooldownReduction` · `Star_Yubar_StrongerSuperNova` · `UI_DamageNumberGroup` · `UI_DamageNumberText` · `UI_EntityFollow` · `Mirror.GeneratedNetworkCode`

### Dependencies (4)

*Types and components that `EventInfoDamage` references or depends upon:*

[Actor](/api/Global.Actor) · [Entity](/api/Global.Entity) · [FinalDamageData](/api/Global.FinalDamageData) · [ReactionChain](/api/Global.ReactionChain)

:::
