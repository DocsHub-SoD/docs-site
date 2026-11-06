# Struct: ListReturnHandle&lt;T&gt;

- **Category:** <span class="cat-dot" style="--cat-color: #f97316" data-cat="Data & Core Math"></span> Data & Core Math
- **Namespace:** `Global`
- **Assembly:** `Dew.Core.dll`

```csharp
public struct ListReturnHandle<T>
```

## Properties (1)

::: details Click to expand Properties (1)

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`needToReturn`** | `public bool needToReturn { get; }` |  |

:::

## Methods (1)

::: details `Return()`

Clear and return the borrowed list.

```csharp
public void Return()
```

:::


## Architecture & Relationships

::: details Click to expand Architecture & Relationships

### Used By (216)

*Classes and systems that invoke, reference, or depend on `ListReturnHandle<T>`:*

`ACH_M_M_M_MONSTER_KILL` · `AccessoryPreviewRenderer` · `Accessory_AttachPoint` · [ActionAttackMove](/api/Global.ActionAttackMove) · [ActionInteract](/api/Global.ActionInteract) · [Actor](/api/Global.Actor) · `Ai_ArcticTerritory` · `Ai_C_BackStep_Bomb` · `Ai_C_BeamOfLight` · `Ai_C_CorrosiveTrails_Gas` · `Ai_C_FlashFreeze` · `Ai_C_MassProtection` · `Ai_C_PressurePoint` · `Ai_D_ExoticMatter_Projectile` · `Ai_D_Resolve_Push` · `Ai_D_SharedPain_Instance` · `Ai_E_MassCleanse` · `Ai_E_SearingCharge` · `Ai_E_SliceThroat` · `Ai_E_StygianRush_Rush` · `Ai_Gem_C_Void_Explosion` · `Ai_Gem_L_SuppressedArcanum` · `Ai_Gem_U_LastStarlight` · `Ai_L_Blizzard_Instance` · `Ai_L_MentalCorruption_Projectile` · `Ai_L_SmallMoltenCore_Dragon_Atk` · `Ai_M_DreamyWaltz_BuffExplosion` · `Ai_M_FrostyCharge` · `Ai_MiniBoss_IceAura_AoE` · `Ai_MiniBoss_OrbSpitter_Orb` · `Ai_Mon_DarkCave_CaveBat_Dash` · `Ai_Mon_DarkCave_DarkElemental_Barrage_Arrow` · `Ai_Mon_Despair_BossAzurak_DoubleStomp_Instance` · `Ai_Mon_Despair_BossAzurak_Roll` · `Ai_Mon_Despair_BossAzurak_StompBlock` · `Ai_Mon_Despair_BossAzurak_StompGlobal` · `Ai_Mon_Despair_WretchedArtillery_BarrageAtk_Missile` · `Ai_Mon_Forest_Hound_Charge` · `Ai_Mon_Ink_Archer_Atk` · `Ai_Mon_Ink_BossDarkMoon_SpawnEgoSword_Projectile` · `Ai_Mon_Ink_BossDarkMoon_ThrowSpear_Projectile` · `Ai_Mon_Ink_BossDarkMoon_ThrowSpear_TeleportAtk_AfterAtk` · `Ai_Mon_Ink_BossWhiteNight_Cataclysm_Eclipse` · `Ai_Mon_Ink_BossWhiteNight_Cataclysm_SafeZone` · `Ai_Mon_Ink_BossWhiteNight_DestructionWave_Wave` · `Ai_Mon_LavaLand_BossInfernus_Roar_Projectile` · `Ai_Mon_LavaLand_FireElemental_ExplosionSub` · `Ai_Mon_LavaLand_Magmadon_Charge_Projectile` · `Ai_Mon_Primus_BossPrimusAeron_Adapt_Atk` · `Ai_Mon_Primus_BossPrimusAeron_Adapt_SmiteStorm_Smite` · `Ai_Mon_Primus_BossPrimusAeron_Force_Grab` · `Ai_Mon_Sky_Baam_Teleport` · `Ai_Mon_Sky_BigBaam_BeamAtk` · `Ai_Mon_Sky_BigBaam_Main_Root` · `Ai_Mon_Sky_BossNyx_Blackhole` · `Ai_Mon_Sky_BossNyx_LineAtk` · `Ai_Mon_Sky_BossNyx_StellarDash` · `Ai_Mon_Sky_LittleBaam_Atk` · `Ai_Mon_Sky_StarSeed_Atk` · `Ai_Mon_SnowMountain_BossSkoll_SummonArrow_Instance` · `Ai_Mon_Special_BossErebos_Gaze_Instance` · `Ai_Mon_Special_BossErebos_SpawnBlackhole_Instance` · `Ai_Mon_Special_BossErebos_SpawnTormentor_Attacker` · `Ai_Mon_Special_BossErebos_SpawnTormentor_Attacker_Instance` · `Ai_Mon_Special_BossErebos_SpawnTormentor_Slow` · `Ai_Mon_Special_BossErebos_StarRain_Instance` · `Ai_Mon_Special_BossErebos_Teleport` · `Ai_Mon_Special_BossLightElemental_Beam` · `Ai_Mon_Special_BossMaw_ChainReaction_Instance` · `Ai_Mon_Special_BossMaw_Chomp_Charge` · `Ai_Mon_Special_BossMaw_Purgatory_Trap` · `Ai_Mon_Special_BossMaw_ShadowOverdrive_Projectile` · `Ai_Mon_Special_BossObliviax_ChargeSequence_MissileAtk` · `Ai_Mon_Special_BossPolaris_Holy_Purgatory_Spawner` · `Ai_QR_ValiantHeart` · `Ai_Q_EmbracingTheChill_AreaDoT` · `Ai_Q_EtherealInfluence` · `Ai_Q_Fleche_Dash` · `Ai_Q_HandCannon` · `Ai_Q_IncendiaryRounds_Attack` · `Ai_Q_Laceration_Circle` · `Ai_Q_Lunge` · `Ai_Q_MoonlightPact` · `Ai_Q_SuperNova` · `Ai_R_BackOff_Spawner` · `Ai_R_ChainReaction` · `Ai_R_DancingBlades` · `Ai_R_Ignite` · `Ai_R_Inspire_Roar` · `Ai_R_NaturesWhisper` · `Ai_R_OrbOfLight_BackwardHealing` · `Ai_R_SanctuaryOfEl_Ground` · `Ai_R_StaticDischarge` · `Ai_Sky_BossIntruder_Instance` · `Ai_Star_Mist_F_LG_ChainAttack_Phantom` · `Ai_U_BeamOfBalance_Beam` · `Ai_U_Hysteria_Claw` · `Ai_U_WorldCracker` · `Ai_UnstableRatSwarm_Projectile` · `Ai_VeilOfDark` · `At_Mon_Sky_StarSeed_Atk` · [AttachToFace](/api/Global.AttachToFace) · [CameraManager](/api/Global.CameraManager) · [ControlManager](/api/Global.ControlManager) · [DamageInstance](/api/Global.DamageInstance) · [Dew](/api/Global.Dew) · [DewCollider](/api/Global.DewCollider) · [DewEffect](/api/Global.DewEffect) · [DewPersistence](/api/Global.DewPersistence) · [DewPhysics](/api/Global.DewPhysics) · [DewQuest](/api/Global.DewQuest) · [DewResources](/api/Global.DewResources) · [Entity](/api/Global.Entity) · [EntityAI](/api/Global.EntityAI) · [EntityControl](/api/Global.EntityControl) · [EntityModel](/api/Global.EntityModel) · [EntityStatus](/api/Global.EntityStatus) · [EntityVisual](/api/Global.EntityVisual) · `Forest_Fireplace` · [FxCastTelegraph](/api/Global.FxCastTelegraph) · [FxFindEntity](/api/Global.FxFindEntity) · [FxMeshTrail](/api/Global.FxMeshTrail) · `Gem_C_Responsibility` · `Gem_C_Vengeance` · `Gem_E_Blossom` · `Gem_E_Insight` · `Gem_E_Pain` · `Gem_E_Reflex` · `Gem_L_Embertail` · `Gem_L_Paranoia` · `Gem_R_Ricochet` · `Gem_R_Snow` · `Gem_R_Spiral` · `Gem_U_GlacialCore` · `Gem_U_LastStarlight` · [GlobalUIManager](/api/Global.GlobalUIManager) · [Hero](/api/Global.Hero) · `Hero_Bismuth` · `Hero_Bismuth_BookController` · `Hero_Yubar_ScrollTexture` · `Ink_BossRoomDamageGround` · `Ink_ScrollingInkAnimation` · `LavaLand_IcePlace` · `LucidDream_MarshOfDestiny` · [MeleeAttackInstance](/api/Global.MeleeAttackInstance) · `Mon_GoldenLizard_ElusiveLizard` · `Mon_Special_BossMaw` · `Mon_Special_BossPolaris` · [Pickup_RegenOrb](/api/Global.Pickup_RegenOrb) · [PlayLobby_Character](/api/Global.PlayLobby_Character) · [PreloadInterface](/api/Global.PreloadInterface) · `Primus_Pizza0` · [Room](/api/Global.Room) · [RoomMonsters](/api/Global.RoomMonsters) · [Room_Barrier](/api/Global.Room_Barrier) · [SafeAction](/api/Global.SafeAction) · [SafeAction`1](/api/Global.SafeAction`1) · [SafeAction`2](/api/Global.SafeAction`2) · [SafeAction`3](/api/Global.SafeAction`3) · [SafeAction`4](/api/Global.SafeAction`4) · `Se_C_IceBlock` · `Se_D_AstridsMasterpieceEnGarde` · `Se_D_AstridsMasterpiecePriorite` · `Se_D_ChargedAnguillian` · `Se_D_ConvergencePoint` · `Se_D_ExoticMatter` · `Se_D_PrismaticEyes` · `Se_EngulfedInFlame` · `Se_FatalHitProtection_Invulnerable` · `Se_Gem_R_Hedgehog_Aura` · `Se_Gem_R_Wound_Wounded` · `Se_GenericStealth` · `Se_L_PyranasFireball` · `Se_M_Charge` · `Se_MiniBoss_IceAura` · `Se_MiniBoss_OrbSpitter` · `Se_MiniBoss_UnstableExplosive_Explosion` · `Se_MirageSkin_Delusion` · `Se_MirageSkin_Oblivion` · `Se_MirageSkin_Pulverization` · `Se_MirageSkin_Sanctification` · `Se_Mon_DarkCave_BossSeeker_Blink` · `Se_Mon_Despair_BossAzurak_RoarAtk_SafeZoneSpawner` · `Se_Mon_Ink_BossWhiteNight_Rush` · `Se_R_BaptismOfSun_Buff` · `Se_R_BoneCrusher` · `Se_R_Parry_Start` · `Se_R_RepulsiveShield` · `Se_RoomMod_UnstableVeilOfTime_ModifyCooldowns` · `Se_Star_Aurena_L_ShareHeal` · `Se_Star_Husk_I_ShopIntimidation` · `Se_Star_Mist_F_LG_ChainAttack` · `Se_Star_Nachia_L_SummonBonus` · `Se_Star_Vesper_D_ADWithNearbyBurning` · `Se_Treasure_FragmentOfDetermination_Invulnerable` · `Se_U_HerWorld_Blackhole` · [Shrine](/api/Global.Shrine) · `Shrine_Chaos` · `Shrine_CorruptedChaos` · `Shrine_FallenStar` · [SpawnManager](/api/Global.SpawnManager) · `St_C_Starfall` · [StatusEffect](/api/Global.StatusEffect) · `Sum_R_AnnoyingBanner` · `Sum_R_SummonLittleBaam_Baam` · [Summon](/api/Global.Summon) · `Trap_FlameJet` · `UI_Constellations_CategoryGroup` · `UI_EmoteList` · `UI_EmoteList_EditEmoteWheel_FloatingEmote` · [UI_GamepadFocusableGroup](/api/Global.UI_GamepadFocusableGroup) · `UI_GamepadShoulderControls` · `UI_InGame_TimerDisplay_Item` · `UI_Lobby_CharacterView` · `UI_Lobby_Constellations_StarList` · `UI_TravelerStory_HeroConstellation`

### Dependencies (0)

*No outgoing class dependencies recorded.*

:::
