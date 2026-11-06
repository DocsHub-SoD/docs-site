# Class: SafeAction&lt;T1, T2&gt;

- **Category:** <span class="cat-dot" style="--cat-color: #22c55e" data-cat="Actors & Entities"></span> Actors & Entities
- **Namespace:** `Global`
- **Assembly:** `Dew.Core.dll`

```csharp
public class SafeAction<T1, T2>
```

## Methods (4)

::: details `Add(Action&lt;T1, T2&gt;)`

```csharp
public SafeAction<T1, T2> Add(Action<T1, T2> handler)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `handler` | `System.Action<T1, T2>` |  |

**Returns:** `SafeAction<T1, T2>`

:::

::: details `Contains(Action&lt;T1, T2&gt;)`

```csharp
public bool Contains(Action<T1, T2> handler)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `handler` | `System.Action<T1, T2>` |  |

**Returns:** `bool`

:::

::: details `Invoke(T1, T2)`

```csharp
public void Invoke(T1 a, T2 b)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `a` | `T1` |  |
| `b` | `T2` |  |

:::

::: details `Remove(Action&lt;T1, T2&gt;)`

```csharp
public SafeAction<T1, T2> Remove(Action<T1, T2> handler)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `handler` | `System.Action<T1, T2>` |  |

**Returns:** `SafeAction<T1, T2>`

:::


## Architecture & Relationships

::: details Click to expand Architecture & Relationships

### Used By (76)

*Classes and systems that invoke, reference, or depend on `SafeAction<T1, T2>`:*

`ACH_IN_CARNAGE_I_BLOOM` · `ACH_THE_EIGHTH_TROPHY` · [AbilityTrigger](/api/Global.AbilityTrigger) · [AchievementManager](/api/Global.AchievementManager) · [ActorManager](/api/Global.ActorManager) · `ButtonDisplay` · [ChatManager](/api/Global.ChatManager) · [ClientEventManager](/api/Global.ClientEventManager) · [ConversationManager](/api/Global.ConversationManager) · [DewInput](/api/Global.DewInput) · [DewPlayer](/api/Global.DewPlayer) · [EntityAbility](/api/Global.EntityAbility) · [EntityControl](/api/Global.EntityControl) · [EntityGroundMarker](/api/Global.EntityGroundMarker) · [GameManager](/api/Global.GameManager) · [GameMod_Limbo](/api/Global.GameMod_Limbo) · [GameResultManager](/api/Global.GameResultManager) · [GameSettingsManager](/api/Global.GameSettingsManager) · [Gem](/api/Global.Gem) · `GemWorldModel` · `Gem_R_Flow` · [HeroSkill](/api/Global.HeroSkill) · [InGameUIManager](/api/Global.InGameUIManager) · [PerControlVisibility](/api/Global.PerControlVisibility) · [Pickup_DreamDust](/api/Global.Pickup_DreamDust) · [PlayLobby_Character](/api/Global.PlayLobby_Character) · [PlayLobby_RotateCharacterTutorial](/api/Global.PlayLobby_RotateCharacterTutorial) · [QuestManager](/api/Global.QuestManager) · [RoomMonsters](/api/Global.RoomMonsters) · `Se_D_TheKillingFlow` · `Se_MiniBoss_SpinningArrow` · `Se_Star_Bismuth_D_AtkSpdFromDismantle` · `Se_Star_L_PotionOnBuyOrSell` · `Se_Star_Mist_D_BonusOnDash` · `Se_Star_Yubar_I_MoreDreamDustWithPenalty` · [SkillTrigger](/api/Global.SkillTrigger) · `SkillWorldModel` · `St_D_ScarOfTheWind` · [StatisticsManager](/api/Global.StatisticsManager) · [StatusEffect](/api/Global.StatusEffect) · `Tut_Cleanse` · `Tut_ShopSell` · [UIManager](/api/Global.UIManager) · `UI_Common_MenuView` · `UI_Constellations` · `UI_EmoteList` · [UI_EmoteWheel](/api/Global.UI_EmoteWheel) · `UI_EntityProvider_LocalHero` · [UI_GamepadTextInput](/api/Global.UI_GamepadTextInput) · `UI_InGame_AchievementNotifications` · `UI_InGame_AmbientLevel` · `UI_InGame_ArtifactStoryView` · `UI_InGame_Conversations_Instance` · `UI_InGame_Difficulty` · `UI_InGame_EditSkillIndicatorPositionByControl` · `UI_InGame_EmoteCanvas` · `UI_InGame_GemSlot` · `UI_InGame_HeroDetailWindow` · `UI_InGame_PartyDisplay_Item` · `UI_InGame_ScoreboardView` · `UI_InGame_SkillButton` · `UI_InGame_SkillButton_EditSkill` · `UI_InGame_WorldMap` · `UI_Lobby_Constellations` · `UI_Lobby_DifficultyItem` · `UI_Lobby_EmoteCanvas` · `UI_Lobby_LobbyNameGroup` · `UI_Lobby_PlayerNametag` · `UI_Lobby_SelectedHeroInfo_TravelerStoryButton` · `UI_Lobby_SendChatMessage` · `UI_PlayRewardAnnouncer` · `UI_PlayTutorial_TutorialCanvas` · `UI_Settings_View` · `UI_Title_PrivateDemoNotice` · `UI_TooltipManager` · [View](/api/Global.View)

### Dependencies (3)

*Types and components that `SafeAction<T1, T2>` references or depends upon:*

[DewPool](/api/Global.DewPool) · `IPoolClearable` · [ListReturnHandle`1](/api/Global.ListReturnHandle`1)

:::
