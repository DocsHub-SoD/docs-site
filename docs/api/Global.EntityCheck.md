# Class: EntityCheck

- **Category:** <span class="cat-dot" style="--cat-color: #22c55e" data-cat="Actors & Entities"></span> Actors & Entities
- **Namespace:** `Global`
- **Assembly:** `Dew.Core.dll`
- **Attributes:** `[Extension]`

```csharp
public static class EntityCheck
```

## Methods (2)

::: details `IsAnyBoss(Entity)`

```csharp
public static bool IsAnyBoss(this Entity e)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `e` | [`Entity`](/api/Global.Entity) |  |

**Returns:** `bool`

:::

::: details `IsNullInactiveDeadOrKnockedOut(Entity)`

```csharp
public static bool IsNullInactiveDeadOrKnockedOut(this Entity e)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `e` | [`Entity`](/api/Global.Entity) |  |

**Returns:** `bool`

:::


## Architecture & Relationships

::: details Click to expand Architecture & Relationships

### Used By (226)

*Classes and systems that invoke, reference, or depend on `EntityCheck`:*

`ACH_PRAISE_THE_SUN` · `ACH_REAP_WHAT_YOU_SOW` · [AbilityTrigger](/api/Global.AbilityTrigger) · [ActionCast](/api/Global.ActionCast) · [Actor](/api/Global.Actor) · [ActorManager](/api/Global.ActorManager) · `Ai_ArcticTerritory` · `Ai_C_BeamOfLight` · `Ai_C_MassProtection` · `Ai_C_Whirlwind` · `Ai_Curse_IntermittentExplosion_Explosion` · `Ai_D_SharedPain_Instance` · `Ai_E_Aftershock_Damage` · `Ai_E_ClutchesOfMalice_ReachAndPull` · `Ai_E_FinalExplosion_Explosion` · `Ai_E_StygianRush_Rush` · `Ai_Gem_E_Crimson` · `Ai_Gem_E_Predation_Pickup` · `Ai_Gem_R_Blade` · `Ai_Gem_U_LastStarlight` · `Ai_L_BloodStrike_Meat` · `Ai_L_SmallMoltenCore_Dragon_Atk` · `Ai_M_DreamyWaltz` · `Ai_MiniBoss_BloodThorn_MainThorn` · `Ai_Mon_Despair_BossAzurak_RoarAtk` · `Ai_Mon_Despair_BossAzurak_Roll` · `Ai_Mon_Despair_DreadBug_JumpBack` · `Ai_Mon_Forest_BossDemon_AltSkill_Stomp` · `Ai_Mon_Ink_Archer_Atk` · `Ai_Mon_Ink_BossWhiteNight_Cataclysm` · `Ai_Mon_Ink_BossWhiteNight_Cataclysm_Eclipse` · `Ai_Mon_Ink_BossWhiteNight_DestructionWave_Wave` · `Ai_Mon_Ink_BossWhiteNight_Oppression` · `Ai_Mon_LavaLand_BossInfernus_BreathFire` · `Ai_Mon_LavaLand_BossInfernus_Jump` · `Ai_Mon_LavaLand_Magmadon_Charge_Projectile` · `Ai_Mon_Primus_BossPrimusAeron_Adapt_Arbalest` · `Ai_Mon_Primus_BossPrimusAeron_Adapt_Starfall_Instance` · `Ai_Mon_Primus_BossPrimusAeron_Rage_DashAttack` · `Ai_Mon_Primus_BossPrimusAeron_Rage_MassDelusion` · `Ai_Mon_Sky_Baam_TeleportSequence` · `Ai_Mon_Sky_BossNyx_Atk` · `Ai_Mon_Sky_BossNyx_Blackhole` · `Ai_Mon_Sky_BossNyx_StellarDash` · `Ai_Mon_SnowMountain_BossSkoll_AuraExplosion_Spawner` · `Ai_Mon_SnowMountain_BossSkoll_AuraSlice` · `Ai_Mon_SnowMountain_BossSkoll_DeathFromAbove` · `Ai_Mon_Special_AmbushSpawner_Projectile` · `Ai_Mon_Special_BossErebos_SpawnBlackhole_Instance` · `Ai_Mon_Special_BossMaw_ChainReaction_Instance` · `Ai_Mon_Special_BossMaw_PrecisionShot` · `Ai_Mon_Special_BossObliviax_ChargeSequence_MissileAtk` · `Ai_Mon_Special_BossPolaris_Holy_Purgatory_Spawner` · `Ai_Mon_Special_BossPolaris_Monster_Atk_SecondAtk` · `Ai_Mon_Special_BossPolaris_Monster_Atk_Spawner` · `Ai_Mon_Special_BossPolaris_Monster_PizzaLightning_Spawner` · `Ai_Mon_Special_BossPolaris_Monster_Scream` · `Ai_Q_DeathMark_Projectile` · `Ai_Q_EmbracingTheChill_AreaDoT` · `Ai_Q_Fleche_Dash` · `Ai_Q_MoonlightPact_Land` · `Ai_R_BaptismOfSun` · `Ai_R_ChainReaction` · `Ai_R_Chomp` · `Ai_R_FrozenFists_PunchDash` · `Ai_R_OrbOfLight_ForwardDamaging` · `Ai_Sky_BossIntruder_Instance` · `Ai_Star_Mist_F_LG_ChainAttack_Phantom` · `Ai_U_BigChomp` · `Ai_UnstableRatSwarm_Projectile` · `Ai_VeilOfDark` · `At_Mon_DarkCave_BossSeeker_GreenChaserOrb` · [BossMonster](/api/Global.BossMonster) · `BossSeeker_SpotLightController` · [CameraManager](/api/Global.CameraManager) · [ControlManager](/api/Global.ControlManager) · [ConversationManager](/api/Global.ConversationManager) · [CurseStatusEffect](/api/Global.CurseStatusEffect) · [DamageInstance](/api/Global.DamageInstance) · [Dew](/api/Global.Dew) · [DewCollider](/api/Global.DewCollider) · [DewEffect](/api/Global.DewEffect) · [DewHeroesTeleporter](/api/Global.DewHeroesTeleporter) · `DewLocalDitherFade` · [DewNetworkManager](/api/Global.DewNetworkManager) · [EditSkillManager](/api/Global.EditSkillManager) · [EntityAI](/api/Global.EntityAI) · [EntityControl](/api/Global.EntityControl) · [EntityGroundMarker](/api/Global.EntityGroundMarker) · [EntitySound](/api/Global.EntitySound) · [FloatingWindowManager](/api/Global.FloatingWindowManager) · [GameManager](/api/Global.GameManager) · `GameMod_DespairFixStuck` · [GameMod_Limbo](/api/Global.GameMod_Limbo) · [GameMod_MirageSkin](/api/Global.GameMod_MirageSkin) · [Gem](/api/Global.Gem) · `Gem_E_Flexibility` · `Gem_E_Omega` · `Gem_E_OurStory_Completed` · `Gem_E_OurStory_Unfinished` · `Gem_E_Predation` · `Gem_E_Reflex` · `Gem_L_Paranoia` · `Gem_L_Supersymmetry` · `Gem_R_Mortality` · `Gem_R_Wound` · `Gem_U_GuidingCompass_NotCharged` · `Hero_Bismuth_BookController` · [InGameUIManager](/api/Global.InGameUIManager) · `Ink_BossRoomDamageGround` · `LavaLand_IcePlace` · `LavaLand_Lava` · `LucidDream_MarshOfDestiny` · `LucidDream_TheDarkestUrge` · `LucidDream_WILD` · `Mon_Forest_SpiderWarrior` · `Mon_GoldenLizard_ElusiveLizard` · `Mon_Ink_BossDarkMoon` · `Mon_Ink_BossWhiteNight` · `Mon_Special_BossObliviax` · [ObjectiveArrowManager](/api/Global.ObjectiveArrowManager) · [PickupInstance](/api/Global.PickupInstance) · `PlayTutorial_Tutorial` · `PrimusCutsceneEntityVisualOff` · `Primus_Ending` · `RoomMod_Ambush` · `RoomMod_CorruptedChaos_AuraOfPain` · [RoomMonsters](/api/Global.RoomMonsters) · [RoomRewards](/api/Global.RoomRewards) · [RoomSection](/api/Global.RoomSection) · `Se_AutoDetectPresence` · `Se_Curse_AnchorOfMind` · `Se_D_BeautifulThreat` · `Se_D_PrismaticEyes` · `Se_D_TheKillingFlow` · `Se_DistantMemories` · `Se_E_Harvest_OnVictim` · `Se_Elm_Cold` · `Se_FishScales` · `Se_Gem_R_Wound_Wounded` · `Se_L_ButchersStrike_KillTimer` · `Se_LingeringAuraOfGuidance` · `Se_MiniBoss_UnstableExplosive_Explosion` · `Se_MirageSkin_Delusion_Delusional` · `Se_MirageSkin_Sanctification` · `Se_Mon_Despair_BossAzurak_RoarAtk_SafeZoneSpawner` · `Se_Mon_Despair_ParalyticFly_Atk_Instance` · `Se_Mon_Primus_BossPrimusAeron_Adapt_IceBlock` · `Se_Mon_SnowMountain_SnowWolf_SlowApproach` · `Se_Mon_SnowMountain_VikingWarrior_DmgReducer` · `Se_Mon_Special_BossMaw_ShadowOverdrive_Initial` · `Se_Mon_Special_BossPolaris_Holy_CounterSpell` · `Se_Mon_Special_BossPolaris_Holy_PhaseShifter` · `Se_Q_DeathMark_Marked` · `Se_Q_Fleche_VictimTracker` · `Se_R_AnnihilationStance` · `Se_R_Composure_Buff` · `Se_R_Deception` · `Se_R_Immolation` · `Se_R_ShadowOverdrive_Initial` · `Se_R_Tranquility` · `Se_RoomMod_BlackRain` · `Se_Shrine_SmallSoul` · `Se_Star_Aurena_I_BonusFromStones` · `Se_Star_Aurena_L_ShareHeal` · `Se_Star_Bismuth_D_SkillHasteAndAutoCast` · `Se_Star_Bismuth_I_KnowledgeBook` · `Se_Star_Cetus_I_GetDreamDustOnBossKill` · `Se_Star_D_BossDamageAmp` · `Se_Star_D_CritUpHitDecay` · `Se_Star_Husk_F_AS_NoShockwaveFasterAttack` · `Se_Star_Husk_I_BossKillPlatinumCoin` · `Se_Star_Husk_I_ShopIntimidation` · `Se_Star_Husk_L_DodgeCooldownOnKillOrAttack` · `Se_Star_I_GemOnMiniBossKill` · `Se_Star_Lacerta_I_BonusFromStones` · `Se_Star_Lacerta_I_BossBounty` · `Se_Star_Mist_D_BossDamageOnHighHp` · `Se_Star_Mist_F_LG_ChainAttack` · `Se_Star_Mist_I_BonusOnCatPet` · `Se_Star_Vesper_D_ADWithNearbyBurning` · `Se_Star_Vesper_D_BossHunterAmpWithPenalty` · `Se_Star_Yubar_I_StarCookie` · `Se_StarlessPath_PowerOfGuidance` · `Se_U_BeamOfBalance` · `Se_U_Burrow` · `Se_U_HerWorld_Blackhole` · `Se_U_Hysteria` · [Shrine](/api/Global.Shrine) · `Shrine_BossSoul` · `Shrine_CallOfTheRavenous` · `Shrine_Chaos` · `Shrine_CookingPot` · `Shrine_CorruptedChaos` · `Shrine_Guidance` · `Shrine_MarshOfDestiny_SeedOfTorment` · `Shrine_TheConsortOfNight` · [SkillTrigger](/api/Global.SkillTrigger) · `Sky_BossIntruder` · `Sky_LightFogDamager` · [SpecialEntityRoomModifier](/api/Global.SpecialEntityRoomModifier) · `St_D_DisintegratingClaw` · `St_D_QuartetOfDeath` · `St_L_SmallMoltenCore` · `St_Q_Fleche` · `St_Q_MoonlightPact` · `Sum_L_SmallMoltenCore_Dragon` · `Sum_R_AnnoyingBanner` · [Summon](/api/Global.Summon) · `UI_EntityCrowdControl` · `UI_EntityHealthBar` · `UI_EntityHealthBarGroup` · `UI_EntityHealthBarMain` · `UI_EntityProtected` · `UI_EntitySummonDuration` · `UI_EntityUnstoppable` · `UI_InGame_CurseNotifications` · `UI_InGame_FloatingWindow_Shop` · `UI_InGame_MovementSkillIndicator` · `UI_InGame_PickupNumbers` · `UI_InGame_SkillButton` · `UI_InGame_SkillNotifications` · `UI_InGame_VoteDisplay` · `UI_InGame_VoteDisplay_PlayerItem` · `UI_InGame_WorldMap` · [ZoneManager](/api/Global.ZoneManager)

### Dependencies (5)

*Types and components that `EntityCheck` references or depends upon:*

[Actor](/api/Global.Actor) · `ActorRef`1` · [Entity](/api/Global.Entity) · [EntityStatus](/api/Global.EntityStatus) · [Hero](/api/Global.Hero)

:::
