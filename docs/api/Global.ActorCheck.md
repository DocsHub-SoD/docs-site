# Class: ActorCheck

- **Category:** <span class="cat-dot" style="--cat-color: #22c55e" data-cat="Actors & Entities"></span> Actors & Entities
- **Namespace:** `Global`
- **Assembly:** `Dew.Core.dll`
- **Attributes:** `[Extension]`

```csharp
public static class ActorCheck
```

## Methods (1)

::: details `IsNullOrInactive(Actor)`

```csharp
public static bool IsNullOrInactive(this Actor a)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `a` | [`Actor`](/api/Global.Actor) |  |

**Returns:** `bool`

:::


## Architecture & Relationships

::: details Click to expand Architecture & Relationships

### Used By (192)

*Classes and systems that invoke, reference, or depend on `ActorCheck`:*

[AbilityInstance](/api/Global.AbilityInstance) · [AbilityTrigger](/api/Global.AbilityTrigger) · [ActionCast](/api/Global.ActionCast) · [Actor](/api/Global.Actor) · `Ai_C_BeamOfLight` · `Ai_E_FlameJet` · `Ai_E_MassCleanse` · `Ai_E_StygianRush` · `Ai_EmbraceNewIdentity` · `Ai_Gem_U_GuidingCompass_PowerGainProjectile` · `Ai_Gem_U_LastStarlight` · `Ai_GenericDodge` · `Ai_L_LightExplosion` · `Ai_L_SmallMoltenCore_Dragon_Atk` · `Ai_Mon_DarkCave_BossSeeker_TunnelVision_Claw` · `Ai_Mon_DarkCave_BossSeeker_TunnelVision_SecondPoolAtk` · `Ai_Mon_Forest_Hound_Charge` · `Ai_Mon_Ink_BossDarkMoon_Eclipse` · `Ai_Mon_Ink_BossDarkMoon_Hammer` · `Ai_Mon_Ink_BossWhiteNight_Oppression` · `Ai_Mon_Ink_GhostBlade_SwiftStep` · `Ai_Mon_LavaLand_BossInfernus_PowerBomb` · `Ai_Mon_Primus_BossPrimusAeron_Force_DropGiantSword` · `Ai_Mon_SnowMountain_BossSkoll_AuraBladeRain` · `Ai_Mon_SnowMountain_BossSkoll_Whirlwind` · `Ai_Mon_Special_BossPolaris_Holy_CounterSpell_DisarmProjectile` · `Ai_Q_Fleche_Dash` · `Ai_Q_Laceration_Circle` · `Ai_Q_Lunge` · `Ai_Q_SuperNova` · `Ai_R_BackOff_Spawner` · `Ai_R_Inspire_Roar` · `Ai_R_PrecisionShot` · `Ai_R_SanctuaryOfEl_Ground` · `Ai_R_Somersault` · `Ai_R_StaticDischarge` · `Ai_RandomGemUpgrade` · `Ai_Shrine_MawOfDoom_DestroyTarget` · `Ai_Star_Cetus_F_BI_SelfDamageAoeCold_AOE` · `Ai_Star_Yubar_F_EI_DashNoProjectile_Dash` · `At_Mon_Sky_StarSeed_SelfDestruct` · `At_Mon_Special_BossPolaris_Monster_PizzaLightning` · [AttachToHero](/api/Global.AttachToHero) · [CameraManager](/api/Global.CameraManager) · [ChargingChannel](/api/Global.ChargingChannel) · [ControlManager](/api/Global.ControlManager) · `ConversationShrineBase` · [CurseStatusEffect](/api/Global.CurseStatusEffect) · [Dew](/api/Global.Dew) · [DewNetworkManager](/api/Global.DewNetworkManager) · [EditSkillManager](/api/Global.EditSkillManager) · [EditSkillShrine](/api/Global.EditSkillShrine) · [EntityAI](/api/Global.EntityAI) · [EntityAbility](/api/Global.EntityAbility) · [EntityControl](/api/Global.EntityControl) · [EntityGroundMarker](/api/Global.EntityGroundMarker) · [EntityVisual](/api/Global.EntityVisual) · [FloatingWindowManager](/api/Global.FloatingWindowManager) · [FxEntityAnimation](/api/Global.FxEntityAnimation) · [FxEntityDisableRenderer](/api/Global.FxEntityDisableRenderer) · `FxEntityInvoke` · [FxRepeatedEffect](/api/Global.FxRepeatedEffect) · [GameMod_Limbo](/api/Global.GameMod_Limbo) · [GameResultManager](/api/Global.GameResultManager) · `Ge_Obliviax_InterruptTravelAndKidnap` · `Gem_C_Guidance` · `Gem_E_Apathy` · `Gem_E_Fangs` · `Gem_E_Reflex` · `Gem_L_ChaosApple` · `Gem_L_Supersymmetry` · `Gem_R_Abyss` · `Gem_R_Composure` · `Gem_R_Glass` · `Gem_R_NightSky` · `Gem_R_Purity` · `Gem_R_Rigidity` · `Gem_R_Snow` · `Gem_U_GuidingCompass_Charged` · `Gem_U_GuidingCompass_NotCharged` · `Gem_U_LastStarlight` · [HeroSkill](/api/Global.HeroSkill) · `Hero_Husk` · `InGameAnalyticsManager` · `LucidDream_MarshOfDestiny` · `Mon_Ink_BossDarkMoon` · `Mon_Ink_BossWhiteNight` · `Mon_LavaLand_InfernusPillar` · `Mon_Primus_BossPrimusAeron` · `Mon_Special_AmbushSpawner` · `Mon_Special_BossPolaris` · [PickupManager](/api/Global.PickupManager) · [Pickup_BaseGoldOrb](/api/Global.Pickup_BaseGoldOrb) · [Pickup_DreamDust](/api/Global.Pickup_DreamDust) · `Primus_Ending` · `Primus_Pizza0` · `Quest_KillToLiftCurse` · `Quest_LostSoul` · [Room](/api/Global.Room) · `RoomMod_HeroSoul` · [RoomModifiers](/api/Global.RoomModifiers) · [RoomRifts](/api/Global.RoomRifts) · [RoomSection](/api/Global.RoomSection) · `Se_Curse_AnchorOfMind` · `Se_Curse_EternalLoop` · `Se_Curse_LossOfIdentity` · `Se_D_AstridsMasterpiecePriorite` · `Se_D_BurningFist_EmpowerAttack` · `Se_D_ConvergencePoint` · `Se_D_IceColdPresence` · `Se_E_LizardlyBlessing` · `Se_FallenStar_WaveringIdentity` · `Se_FishScales` · `Se_Gem_E_Fever_LivingBomb` · `Se_Gem_L_Culinary_Stack` · `Se_L_SmallMoltenCore_EmpowerAtk` · `Se_M_Charge` · `Se_Mon_DarkCave_BossSeeker_TunnelVision_Disappear` · `Se_Mon_Special_BossMaw_ShieldConversion` · `Se_Mon_Special_BossPolaris_Holy_PhaseShifter` · `Se_Mon_Special_BossPolaris_Monster_Scream_SkillLocked` · `Se_Q_GoldenBurst_Wither` · `Se_R_BoneCrusher` · `Se_Shrine_Chaos_StatBonus` · `Se_Star_Aurena_I_GoldEveryZone` · `Se_Star_Bismuth_D_Conquerer` · `Se_Star_Cetus_D_StackStatsOnTakenDamage` · `Se_Star_Cetus_F_BA_CdReductionOnKill` · `Se_Star_Cetus_F_BI_SelfDamageAoeCold` · `Se_Star_Cetus_F_EM_InfiniteDuration` · `Se_Star_Cetus_L_ArmorBuffOnShield` · `Se_Star_D_LowerADScalingAP` · `Se_Star_D_LowerAPScalingAD` · `Se_Star_D_ShieldDamageAmp` · `Se_Star_Husk_F_DC_RecentDamageHoTWhileStealth` · `Se_Star_L_DodgeCooldown` · `Se_Star_L_DodgeCooldownOnLowHealth` · `Se_Star_L_IgnoreDelusion` · `Se_Star_L_PostHitDamageImmune` · `Se_Star_Lacerta_F_QT_RapidFire` · `Se_Star_Lacerta_L_SpeedAfterDodge` · `Se_Star_Mist_I_BonusOnCatPet` · `Se_Star_Nachia_D_CanineLover` · `Se_Star_Nachia_F_SC_SummonDmgReduction` · `Se_Star_Nachia_I_ForestKillDreamDust` · `Se_Star_Vesper_D_ADWithNearbyBurning` · `Se_StarlessPath_PowerOfGuidance` · `Se_U_BeamOfBalance` · `Shrine_Anitya` · `Shrine_ArtifactGiver` · `Shrine_BossSoul` · `Shrine_Destiny` · `Shrine_FallenStar` · `Shrine_HeroSoul` · `Shrine_MarshOfDestiny_SeedOfTorment` · `Shrine_StarlessPath_EndingRift` · [SkillTrigger](/api/Global.SkillTrigger) · `St_D_ParryMaster` · `St_D_QuartetOfDeath` · `St_L_HerosReturn` · `St_QR_InfernalTales` · `St_U_ShoutOfOblivion` · `StarlessPath_BossPolarisManager` · [StatusEffect](/api/Global.StatusEffect) · `Sum_L_SmallMoltenCore_Dragon` · [Summon](/api/Global.Summon) · `UI_ControllerDisconnectedIndicator` · `UI_DamageNumberGroup` · `UI_Dev_ConsoleSelectedEntityInfo` · `UI_EndingBlackScreenText` · `UI_InGame_BossBars_Item` · `UI_InGame_Difficulty` · `UI_InGame_EditSkillShrineText` · `UI_InGame_FloatingWindow_Chaos` · `UI_InGame_FloatingWindow_ChoiceShrine` · `UI_InGame_FloatingWindow_CorruptedChaos` · `UI_InGame_FloatingWindow_Hatred` · `UI_InGame_FloatingWindow_SeedOfTorment` · `UI_InGame_FloatingWindow_Shop` · `UI_InGame_GemSlot` · `UI_InGame_Map_Item_Actor` · `UI_InGame_OffscreenIndicator_Item_Entity` · `UI_InGame_QuestDisplay_Item` · `UI_InGame_ScoreboardView` · `UI_InGame_Scoreboard_PlayerItem` · `UI_InGame_SkillButton` · `UI_InGame_StatusEffectIcons_Item` · `UI_InGame_WorldMap` · `UI_LucidDreamIcon` · `UI_Tooltip_EditSkillShrineTooltip` · `UI_Tooltip_ObjEditSkillActions` · [ZoneManager](/api/Global.ZoneManager)

### Dependencies (2)

*Types and components that `ActorCheck` references or depends upon:*

[Actor](/api/Global.Actor) · `ActorRef`1`

:::
