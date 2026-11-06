# Class: SafeAction

- **Category:** <span class="cat-dot" style="--cat-color: #22c55e" data-cat="Actors & Entities"></span> Actors & Entities
- **Namespace:** `Global`
- **Assembly:** `Dew.Core.dll`

```csharp
public class SafeAction
```

## Properties (1)

::: details Click to expand Properties (1)

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`Count`** | `public int Count { get; }` |  |

:::

## Methods (4)

::: details `Add(Action)`

```csharp
public SafeAction Add(Action handler)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `handler` | `System.Action` |  |

**Returns:** `SafeAction`

:::

::: details `Contains(Action)`

```csharp
public bool Contains(Action handler)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `handler` | `System.Action` |  |

**Returns:** `bool`

:::

::: details `Invoke()`

```csharp
public void Invoke()
```

:::

::: details `Remove(Action)`

```csharp
public SafeAction Remove(Action handler)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `handler` | `System.Action` |  |

**Returns:** `SafeAction`

:::


## Architecture & Relationships

::: details Click to expand Architecture & Relationships

### Used By (112)

*Classes and systems that invoke, reference, or depend on `SafeAction`:*

`ACH_REACTIVATED` · [AbilityTrigger](/api/Global.AbilityTrigger) · [AchievementManager](/api/Global.AchievementManager) · `Ai_Shrine_CallOfTheRavenous_Projectile` · `Ai_Shrine_MawOfDoom_DestroyTarget` · [ChoiceShrine](/api/Global.ChoiceShrine) · [CurseStatusEffect](/api/Global.CurseStatusEffect) · [DamageInstance](/api/Global.DamageInstance) · `DarkCaveCutSceneFogFadeOut` · `DewCloudSave` · [DewEffect](/api/Global.DewEffect) · [DewGUI](/api/Global.DewGUI) · [DewMod](/api/Global.DewMod) · [DewNetworkManager](/api/Global.DewNetworkManager) · [DewPlayer](/api/Global.DewPlayer) · [DewQuest](/api/Global.DewQuest) · [DewResources](/api/Global.DewResources) · [DewSave](/api/Global.DewSave) · [DewSteam](/api/Global.DewSteam) · [EntitySound](/api/Global.EntitySound) · [EntityStatus](/api/Global.EntityStatus) · [EntityVisual](/api/Global.EntityVisual) · [FxMeshTrail](/api/Global.FxMeshTrail) · [GameManager](/api/Global.GameManager) · `GameMod_CorruptedChaos` · [GameMod_Limbo](/api/Global.GameMod_Limbo) · [GameResultManager](/api/Global.GameResultManager) · [GameSettingsManager](/api/Global.GameSettingsManager) · `Ge_TheConsortOfNight` · [Gem](/api/Global.Gem) · `Hero_Aurena` · `Hero_Bismuth_BookController` · `InGameAnalyticsManager` · [InGameReverieManager](/api/Global.InGameReverieManager) · [InGameTutorialManager](/api/Global.InGameTutorialManager) · [InGameUIManager](/api/Global.InGameUIManager) · [LobbyManager](/api/Global.LobbyManager) · `LucidDream_WILD` · [PlayLobbyManager](/api/Global.PlayLobbyManager) · [QuestManager](/api/Global.QuestManager) · `Quest_KillToLiftCurse` · [Room](/api/Global.Room) · [RoomMonsters](/api/Global.RoomMonsters) · [Room_Barrier](/api/Global.Room_Barrier) · `Se_D_CircleOfLife_Summon` · `Se_GenericStealth` · `Se_LimboBossDecorator` · `Se_Mon_Despair_BossAzurak_Hide` · `Se_MorasDomain_AppearFromGround` · `Se_Star_Bismuth_F_IN_MoreProjByAtkSpd` · `Shrine_BrokenWoodenDoll` · `Shrine_Despair` · `Shrine_Despair_Vestige` · `St_D_IceColdPresence` · [StarEffect](/api/Global.StarEffect) · [StatusEffect](/api/Global.StatusEffect) · [Summon](/api/Global.Summon) · [TransitionManager](/api/Global.TransitionManager) · `UI_AccList` · `UI_CreditsView` · `UI_EmoteList` · `UI_EmoteList_EditEmote` · `UI_EmoteList_Item` · `UI_InGame_GemSlot` · `UI_InGame_HuntLevel` · `UI_InGame_QuestDisplay_Item` · `UI_InGame_SkillButton` · `UI_InGame_VoteDisplay` · `UI_InGame_WorldMap` · `UI_Lobby_ActiveLucidDreams` · `UI_Lobby_Constellations` · `UI_Lobby_Constellations_FloatingStar` · `UI_Lobby_Constellations_HeroConstellationBase` · `UI_Lobby_Constellations_HeroConstellation_StarSlot` · `UI_Lobby_Constellations_Skills_ContextMenu` · `UI_Lobby_Constellations_Skills_Slot` · `UI_Lobby_Constellations_StarDetails` · `UI_Lobby_Constellations_StarDetails_BuyButton` · `UI_Lobby_Constellations_StarItem` · `UI_Lobby_Constellations_StarList` · `UI_Lobby_DejavuButton` · `UI_Lobby_DejavuWindow_Item` · `UI_Lobby_HeroList_Item` · `UI_Lobby_Loadout_AvailableSkills` · `UI_Lobby_Loadout_SkillSlot` · `UI_Lobby_LucidDreamsWindow_Item` · `UI_Lobby_LucidDreams_Item` · `UI_Lobby_ObliterationView` · `UI_Lobby_ObliterationView_Item` · `UI_Lobby_Obliteration_BannedItems` · `UI_Lobby_PlayerNametag` · `UI_ModManager` · `UI_NametagList` · `UI_ProfileStatistics` · `UI_ProfileStatistics_ItemBase` · `UI_SaveIndicator` · `UI_SelectControlPresetWindow` · `UI_ShowIfTopmostView` · `UI_SkinList` · `UI_Title_MasteryRewardView` · `UI_Title_MasteryReward_HeroItem` · `UI_TooltipManager` · `UI_TravelerStory` · `UI_TravelerStory_ColorizeByHeroColor` · `UI_TravelerStory_DetailPanel` · `UI_TravelerStory_Details_Story` · `UI_TravelerStory_Details_Story_ChapterItem` · `UI_TravelerStory_IllustrationCollection` · `UI_TravelerStory_IllustrationItem` · [View](/api/Global.View) · `WagesOfResolveBarrier` · [ZoneManager](/api/Global.ZoneManager)

### Dependencies (3)

*Types and components that `SafeAction` references or depends upon:*

[DewPool](/api/Global.DewPool) · `IPoolClearable` · [ListReturnHandle`1](/api/Global.ListReturnHandle`1)

:::
