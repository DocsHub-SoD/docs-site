# Class: InstantDamageInstance

- **Category:** <span class="cat-dot" style="--cat-color: #ef4444" data-cat="Combat & Abilities"></span> Combat & Abilities
- **Namespace:** `Global`
- **Assembly:** `Dew.Core.dll`
- **Inheritance / Derived:** [DewNetworkBehaviour](/api/Global.DewNetworkBehaviour) → [Actor](/api/Global.Actor) → [AbilityInstance](/api/Global.AbilityInstance) → [DamageInstance](/api/Global.DamageInstance)

```csharp
public class InstantDamageInstance : DamageInstance, ILogicUpdate, ICleanup, ICustomDestroyRoutine
```

## Fields (2)

::: details Click to expand Fields (2)

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`damageDelay`** | `[Title("Instant Damage Instance", null, TitleAlignments.Left, true, true)] [LabelText("Delay")] public float damageDelay` |  |
| **`mainEffectAfterDelay`** | `[LabelText("Main Effect (After Delay)")] public GameObject mainEffectAfterDelay` |  |

:::

## Methods (2)

::: details `OnAfterDelay()`

Called after instant damage instance's delay on server.

```csharp
protected virtual void OnAfterDelay()
```

:::

::: details `OnCreateSequenced()`

```csharp
protected override IEnumerator OnCreateSequenced()
```

**Returns:** `System.Collections.IEnumerator`

:::


## Architecture & Relationships

::: details Click to expand Architecture & Relationships

### Used By (185)

*Classes and systems that invoke, reference, or depend on `InstantDamageInstance`:*

`Ai_Ai_Mon_Ink_BossWhiteNight_OneInchPunch_Atk` · `Ai_C_DarkSpear` · `Ai_C_FlashFreeze` · `Ai_C_GlacialStomp` · `Ai_C_IceClaw` · `Ai_C_MagicSword` · `Ai_C_ShockTrap_Explosion` · `Ai_Curse_DreamAfflictionInductive_Smite` · `Ai_Curse_IntermittentExplosion_Explosion` · `Ai_D_BurningFist_Attack_Instance` · `Ai_D_ExplosionArtist_DodgeExplosion` · `Ai_D_ExplosionArtist_LargeExplosion` · `Ai_D_HeartOfThePack_Explosion` · `Ai_D_IceColdPresence_AOE` · `Ai_D_IcyVeins_Damage` · `Ai_D_MercyOfEl_Swipe` · `Ai_D_ReactiveShockwave_Shockwave` · `Ai_D_RoaringFist` · `Ai_E_Aftershock_Damage` · `Ai_E_DoomsdayMeteor` · `Ai_E_FinalExplosion_Explosion` · `Ai_E_MassCleanse` · `Ai_E_VileStrike_Damage` · `Ai_Gem_E_Crimson` · `Ai_Gem_E_Fever_Explosion` · `Ai_Gem_E_Insensitivity_Bomb` · `Ai_Gem_E_Reflex_IceJet` · `Ai_Gem_R_Scorched_Meteor` · `Ai_HunterArtillery_Big` · `Ai_HunterArtillery_Small` · `Ai_L_Blizzard_Instance` · `Ai_L_ButchersStrike` · `Ai_L_CoinExplosion_Explosion` · `Ai_L_LightExplosion_Instance` · `Ai_M_Endure_Shout` · `Ai_MiniBoss_BloodThorn_MainThorn` · `Ai_MiniBoss_BloodThorn_SubThorn` · `Ai_MirageSkin_Delusion_Missile_Explode` · `Ai_MirageSkin_Oppression_Explode` · `Ai_MirageSkin_Pulverization_Stomp` · `Ai_Mon_DarkCave_BossSeeker_Atk_DelayedExplosion` · `Ai_Mon_DarkCave_BossSeeker_GreenChaserOrb_Explode` · `Ai_Mon_DarkCave_BossSeeker_PurpleOrb_Instance` · `Ai_Mon_DarkCave_BossSeeker_RedFissure` · `Ai_Mon_DarkCave_BossSeeker_TunnelVision_Claw` · `Ai_Mon_DarkCave_BossSeeker_TunnelVision_SecondPoolAtk` · `Ai_Mon_DarkCave_BossSeeker_YellowDiagram_MainInstance` · `Ai_Mon_DarkCave_BossSeeker_YellowDiagram_SubInstance` · `Ai_Mon_DarkCave_CaveBat_Atk` · `Ai_Mon_DarkCave_NightOlm_Atk_DelayedAtk` · `Ai_Mon_DarkCave_Oppressor_Atk` · `Ai_Mon_DarkCave_Oppressor_Hypnotize` · `Ai_Mon_Despair_BossAzurak_AltAtk_Instance` · `Ai_Mon_Despair_BossAzurak_Atk_InitDamage` · `Ai_Mon_Despair_BossAzurak_Atk_SubDamage` · `Ai_Mon_Despair_BossAzurak_StompBlock_Artillery_Damage` · `Ai_Mon_Despair_BossAzurak_StompProjectile_FirstAtk` · `Ai_Mon_Despair_BossAzurak_StompTargetArea` · `Ai_Mon_Despair_Displacer_Atk` · `Ai_Mon_Despair_ParalyticFly_Melee` · `Ai_Mon_Despair_UnstableRat_Explosion` · `Ai_Mon_Despair_WretchedArtillery_Melee` · `Ai_Mon_Forest_BossDemon_AltSkill_LineAtk` · `Ai_Mon_Forest_BossDemon_AltSkill_Stomp_Tree` · `Ai_Mon_Forest_BossDemon_MainSkill_Stomp_Tree` · `Ai_Mon_Forest_BossDemon_SpecialAtk_Instance` · `Ai_Mon_Forest_Hound_Atk` · `Ai_Mon_Forest_Scarab_Atk` · `Ai_Mon_Forest_SpiderSpitter_Melee` · `Ai_Mon_Forest_Treant_MeleeAtk` · `Ai_Mon_Forest_Treant_PowerBomb` · `Ai_Mon_Ink_BossDarkMoon_AltAtk_HorizontalAtk` · `Ai_Mon_Ink_BossDarkMoon_AltAtk_JumpAtk` · `Ai_Mon_Ink_BossDarkMoon_AltAtk_StingAtk` · `Ai_Mon_Ink_BossDarkMoon_Hammer_RageInstance` · `Ai_Mon_Ink_BossDarkMoon_TeleportAtk_Instance` · `Ai_Mon_Ink_BossDarkMoon_ThrowSpear_TeleportAtk` · `Ai_Mon_Ink_BossWhiteNight_AtkInstance` · `Ai_Mon_Ink_BosswhiteNight_DestructionWave_Instance` · `Ai_Mon_Ink_DivineAnimal_Atk` · `Ai_Mon_Ink_Tiger_Atk` · `Ai_Mon_LavaLand_BossInfernus_AltAtk` · `Ai_Mon_LavaLand_BossInfernus_AltAtk_AfterAtk` · `Ai_Mon_LavaLand_BossInfernus_AltAtk_Instance` · `Ai_Mon_LavaLand_BossInfernus_Atk` · `Ai_Mon_LavaLand_BossInfernus_Jump_Land` · `Ai_Mon_LavaLand_BossInfernus_Meteor` · `Ai_Mon_LavaLand_BossInfernus_PowerBomb` · `Ai_Mon_LavaLand_BossInfernus_Stomp` · `Ai_Mon_LavaLand_BossInfernus_Stomp_Eruption` · `Ai_Mon_LavaLand_BossInfernus_Swipe` · `Ai_Mon_LavaLand_FireElemental_Explosion` · `Ai_Mon_LavaLand_Magmadon_Atk` · `Ai_Mon_LavaLand_SuperheatedWolf_Atk` · `Ai_Mon_MorasDomain_NightmareBlob_Atk` · `Ai_Mon_Primus_BossPrimusAeron_Adapt_Doom_Meteor` · `Ai_Mon_Primus_BossPrimusAeron_Adapt_IceBlock_Damage` · `Ai_Mon_Primus_BossPrimusAeron_Adapt_SmiteStorm_Smite` · `Ai_Mon_Primus_BossPrimusAeron_Adapt_Starfall_Instance` · `Ai_Mon_Primus_BossPrimusAeron_Force_Atk` · `Ai_Mon_Primus_BossPrimusAeron_Force_DropGiantSword` · `Ai_Mon_Primus_BossPrimusAeron_Force_GoldRain_Attack` · `Ai_Mon_Primus_BossPrimusAeron_Force_GoldRain_Attack_SubInstance` · `Ai_Mon_Primus_BossPrimusAeron_Force_GoldRain_RainInstance` · `Ai_Mon_Primus_BossPrimusAeron_Force_JumpAttack_CircleInstance` · `Ai_Mon_Primus_BossPrimusAeron_Force_JumpAttack_ConeInstance` · `Ai_Mon_Primus_BossPrimusAeron_Force_Swipe` · `Ai_Mon_Primus_BossPrimusAeron_Rage_Atk_FirstSwipe` · `Ai_Mon_Primus_BossPrimusAeron_Rage_Atk_SecondSwipe` · `Ai_Mon_Primus_BossPrimusAeron_Rage_DashAttack` · `Ai_Mon_Primus_BossPrimusAeron_Rage_MassSilence_Instance` · `Ai_Mon_Sky_Baam_Atk` · `Ai_Mon_Sky_BigBaam_Melee` · `Ai_Mon_Sky_BossNyx_LaserAtk_Instance` · `Ai_Mon_Sky_BossNyx_LineAtk` · `Ai_Mon_Sky_BossNyx_PullAtk_AfterAtk` · `Ai_Mon_Sky_BossNyx_StarBuff_Instance` · `Ai_Mon_Sky_BossNyx_Starfall_Instance` · `Ai_Mon_Sky_BossNyx_Swipe` · `Ai_Mon_Sky_StarSeed_Atk` · `Ai_Mon_Sky_StellaMatter_Melee` · `Ai_Mon_SnowMountain_BossSkoll_Atk_Damage` · `Ai_Mon_SnowMountain_BossSkoll_AuraBladeRain_Instance` · `Ai_Mon_SnowMountain_BossSkoll_AuraExplosion_AfterAtk` · `Ai_Mon_SnowMountain_BossSkoll_AuraExplosion_Spawner` · `Ai_Mon_SnowMountain_BossSkoll_Capture` · `Ai_Mon_SnowMountain_BossSkoll_DeathFromAbove_Land` · `Ai_Mon_SnowMountain_BossSkoll_Swipe` · `Ai_Mon_SnowMountain_BossSkoll_Sword` · `Ai_Mon_SnowMountain_IceElemental_Atk` · `Ai_Mon_SnowMountain_IceElemental_IceBreaker` · `Ai_Mon_SnowMountain_IceElemental_IceBreaker_SubExplosion` · `Ai_Mon_SnowMountain_Scavenger_Atk` · `Ai_Mon_SnowMountain_SnowWolf_Atk` · `Ai_Mon_SnowMountain_VikingWarrior_Atk` · `Ai_Mon_SnowMountain_VikingWarrior_Sword` · `Ai_Mon_Special_BossLightElemental_Lightning` · `Ai_Mon_Special_BossMaw_Cataclysm_Meteor` · `Ai_Mon_Special_BossMaw_MoonlightPact_Atk` · `Ai_Mon_Special_BossMaw_PillarOfFlame_Instance` · `Ai_Mon_Special_BossObliviax_ChargeSequence_LinearAtk` · `Ai_Mon_Special_BossPolaris_Holy_Atk_Explosion` · `Ai_Mon_Special_BossPolaris_Holy_Purgatory_Instance` · `Ai_Mon_Special_BossPolaris_Holy_RainFire_Damage` · `Ai_Mon_Special_BossPolaris_Holy_ScatterFire` · `Ai_Mon_Special_BossPolaris_Monster_Atk_FirstAtk` · `Ai_Mon_Special_BossPolaris_Monster_Atk_SecondAtk` · `Ai_Mon_Special_BossPolaris_Monster_CircularSwipe` · `Ai_Mon_Special_BossPolaris_Monster_CursedDive_SpawnStone` · `Ai_Mon_Special_BossPolaris_Monster_CursedDive_Stomp` · `Ai_Mon_Special_BossPolaris_Monster_JumpStomp_Explosion` · `Ai_Mon_Special_BossPolaris_Monster_JumpStomp_LargerExplosion` · `Ai_Mon_Special_BossPolaris_Monster_JumpStomp_StarfallInstance` · `Ai_Mon_Special_BossPolaris_Monster_PizzaLightning_Instance` · `Ai_Mon_Special_BossPolaris_Monster_Scream_SkillLocker` · `Ai_Mon_Special_BossPolaris_Monster_Smite_Instance` · `Ai_QR_DistortedMind_Damage` · `Ai_QR_Innocence_Explosion` · `Ai_Q_BigBorealChunk_Explosion` · `Ai_Q_CruelSun_Shockwave` · `Ai_Q_Discipline_Stomp` · `Ai_Q_EmbracingTheChill_Explosion` · `Ai_Q_MoonlightPact_Fenrir_Atk` · `Ai_Q_MoonlightPact_Land` · `Ai_Q_SylvanCall` · `Ai_Q_SylvanCall_LeafHound_Atk` · `Ai_R_BackOff_Damage` · `Ai_R_BaptismOfSun` · `Ai_R_BoneCrusher_Explosion` · `Ai_R_Cataclysm_Meteor` · `Ai_R_Deception_EndExplosion` · `Ai_R_FlamingWhip` · `Ai_R_GlacialHammer` · `Ai_R_UnbreakableDetermination_SubExplosion` · `Ai_R_WrathOfEl` · `Ai_RoomMod_MeteoricLife_Explosion` · `Ai_RoomMod_RiskOfMeteors_Meteor` · `Ai_RoomMod_StardustEverywhere_Starfall` · `Ai_Trap_Lightning` · `Ai_Trap_UnstableMushroom` · `Ai_U_BigChomp` · `Ai_U_Burrow_Emerge` · `Ai_U_HerWorld_Explosion` · `Ai_U_Hysteria_Claw` · `Ai_U_ShoutOfOblivion`

### Dependencies (1)

*Types and components that `InstantDamageInstance` references or depends upon:*

[DamageInstance](/api/Global.DamageInstance)

:::
