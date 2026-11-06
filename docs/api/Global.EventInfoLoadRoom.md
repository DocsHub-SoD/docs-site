# Struct: EventInfoLoadRoom

- **Category:** <span class="cat-dot" style="--cat-color: #3b82f6" data-cat="Managers & Systems"></span> Managers & Systems
- **Namespace:** `Global`
- **Assembly:** `Dew.Core.dll`

```csharp
public struct EventInfoLoadRoom
```

## Fields (5)

::: details Click to expand Fields (5)

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`fromIndex`** | `public int fromIndex` |  |
| **`isLoadingFromSave`** | `public bool isLoadingFromSave` |  |
| **`isSidetrackTransition`** | `public bool isSidetrackTransition` |  |
| **`isTraveling`** | `public bool isTraveling` | Is this load result of traveling through a rift? (including the start of the game)This is true if:We just started the gameWe moved through the rift to visit a new / previously visited locationWe are loading from save, which were done in the middle of traveling.This is false if:We are loading from save, which were done after clearing the room. |
| **`toIndex`** | `public int toIndex` |  |

:::


## Architecture & Relationships

::: details Click to expand Architecture & Relationships

### Used By (59)

*Classes and systems that invoke, reference, or depend on `EventInfoLoadRoom`:*

`ACH_BALANCE_FOREVER_LOST` · `ACH_FEELS_LIKE_HOME` · `ACH_GOD_PROTECTS_ME` · `ACH_HOME_SWEET_HOME` · `ACH_PRAYER_FOR_THE_DREAMERS` · `ACH_RAGE_WITHOUT_BOUNDS` · `ACH_THE_CYCLE_OF_REBIRTH` · [CurseStatusEffect](/api/Global.CurseStatusEffect) · [Dew](/api/Global.Dew) · [DewQuest](/api/Global.DewQuest) · [EffectAutoDestroy](/api/Global.EffectAutoDestroy) · `Forest_DayNightManager` · `GameMod_GoldenLizard` · [GameMod_Limbo](/api/Global.GameMod_Limbo) · [GameMod_MirageSkin](/api/Global.GameMod_MirageSkin) · `GameMod_MorasDomain` · `GameMod_Obliviax` · `GameMod_StarlessPath` · `Ge_CallOfTheRavenous` · `Ge_Shrine_PotOfGreed` · `Ge_TheConsortOfNight` · `Gem_L_ChaosApple` · `Gem_R_Adventure` · `Gem_U_GlacialCore` · `Gem_U_GuidingCompass_Charged` · [InGameCrashReportManager](/api/Global.InGameCrashReportManager) · `LucidDream_BonVoyage` · `LucidDream_FalseLifeline` · `LucidDream_MarshOfDestiny` · [Pickup_BaseGoldOrb](/api/Global.Pickup_BaseGoldOrb) · [Pickup_DreamDust](/api/Global.Pickup_DreamDust) · [PropEnt_Merchant_Base](/api/Global.PropEnt_Merchant_Base) · `Quest_HuntedByObliviax` · `Quest_LostSoul` · `Quest_TheConsortOfNight` · [RoomModifierBase](/api/Global.RoomModifierBase) · `Se_Curse_GuidingCompass_CripplingAnxiety` · `Se_D_BeautifulThreat` · `Se_D_MasterOfAssassination` · `Se_Gem_L_Culinary_Stack` · `Se_HeroKnockedOut` · `Se_HeroOneShotProtection` · `Se_Star_D_RiftFirstCastDamageUp` · `Se_Star_I_MoreShopItems` · `Se_Star_Nachia_L_AllyUnstoppable` · `Se_StarlessPath_PowerOfGuidance` · `Se_Treasure_TokenOfGuidance_Heal` · `St_D_ExplosionArtist` · `St_D_HeartOfThePack` · `TempEffect` · `Tut_Cleanse` · `Tut_ShopSell` · `Tut_World` · `Tut_WorldHunt` · `UI_InGame_Location` · `UI_InGame_Map` · `UI_InGame_RoomModDisplay` · [ZoneManager](/api/Global.ZoneManager) · `Mirror.GeneratedNetworkCode`

### Dependencies (0)

*No outgoing class dependencies recorded.*

:::
