# Class: DewLocalization

- **Category:** <span class="cat-dot" style="--cat-color: #64748b" data-cat="Misc & Utility"></span> Misc & Utility
- **Namespace:** `Global`
- **Assembly:** `Dew.Core.dll`

```csharp
public static class DewLocalization
```

## Properties (2)

::: details Click to expand Properties (2)

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`buildData`** | `public static DewLocalizationBuildData buildData { get; }` |  |
| **`data`** | `public static PerLanguageLocalizationData data { get; }` |  |

:::

## Methods (55)

::: details `CaptureDescriptionExpressions(IReadOnlyList&lt;LocaleNode&gt;, Dictionary&lt;string, string&gt;, DescriptionSettings)`

```csharp
public static void CaptureDescriptionExpressions(IReadOnlyList<LocaleNode> nodes, Dictionary<string, string> data, DewLocalization.DescriptionSettings settings)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `nodes` | `System.Collections.Generic.IReadOnlyList<T><LocaleNode>` |  |
| `data` | `System.Collections.Generic.Dictionary<TKey, TValue><string,string>` |  |
| `settings` | [`DewLocalization.DescriptionSettings`](/api/Global.DewLocalization) |  |

:::

::: details `ConvertDescriptionNodesToText(IReadOnlyList&lt;LocaleNode&gt;, DescriptionSettings)`

```csharp
public static string ConvertDescriptionNodesToText(IReadOnlyList<LocaleNode> nodes, DewLocalization.DescriptionSettings settings)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `nodes` | `System.Collections.Generic.IReadOnlyList<T><LocaleNode>` |  |
| `settings` | [`DewLocalization.DescriptionSettings`](/api/Global.DewLocalization) |  |

**Returns:** `string`

:::

::: details `EvaluateAndRenderExpression(ExpressionData, DescriptionSettings, bool)`

```csharp
public static string EvaluateAndRenderExpression(ExpressionData exp, DewLocalization.DescriptionSettings settings, bool shouldShowDetail)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `exp` | `DewInternal.ExpressionData` |  |
| `settings` | [`DewLocalization.DescriptionSettings`](/api/Global.DewLocalization) |  |
| `shouldShowDetail` | `bool` |  |

**Returns:** `string`

:::

::: details `GetAchievementDescription(string)`

```csharp
public static string GetAchievementDescription(string key)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `key` | `string` |  |

**Returns:** `string`

:::

::: details `GetAchievementName(string)`

```csharp
public static string GetAchievementName(string key)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `key` | `string` |  |

**Returns:** `string`

:::

::: details `GetArtifactKey(string)`

```csharp
public static string GetArtifactKey(string artifactType)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `artifactType` | `string` |  |

**Returns:** `string`

:::

::: details `GetArtifactKey(Type)`

```csharp
public static string GetArtifactKey(Type artifactType)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `artifactType` | `System.Type` |  |

**Returns:** `string`

:::

::: details `GetArtifactName(string)`

```csharp
public static string GetArtifactName(string key)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `key` | `string` |  |

**Returns:** `string`

:::

::: details `GetArtifactShortStory(string)`

```csharp
public static string[] GetArtifactShortStory(string key)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `key` | `string` |  |

**Returns:** `string[]`

:::

::: details `GetArtifactStory(string)`

```csharp
public static string GetArtifactStory(string key)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `key` | `string` |  |

**Returns:** `string`

:::

::: details `GetConversationData(string)`

```csharp
public static ConversationData GetConversationData(string key)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `key` | `string` |  |

**Returns:** `DewInternal.ConversationData`

:::

::: details `GetCurseDescription(string)`

```csharp
public static List<LocaleNode> GetCurseDescription(string key)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `key` | `string` |  |

**Returns:** `System.Collections.Generic.List<T><LocaleNode>`

:::

::: details `GetCurseKey(string)`

```csharp
public static string GetCurseKey(string name)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `name` | `string` |  |

**Returns:** `string`

:::

::: details `GetCurseName(string)`

```csharp
public static string GetCurseName(string key)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `key` | `string` |  |

**Returns:** `string`

:::

::: details `GetCurseShortDescription(string)`

```csharp
public static List<LocaleNode> GetCurseShortDescription(string key)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `key` | `string` |  |

**Returns:** `System.Collections.Generic.List<T><LocaleNode>`

:::

::: details `GetFormat(string, string)`

```csharp
public static string GetFormat(string formatString, string lang = null)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `formatString` | `string` |  |
| `lang` | `string` |  |

**Returns:** `string`

:::

::: details `GetGemDescription(string)`

```csharp
public static IReadOnlyList<LocaleNode> GetGemDescription(string key)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `key` | `string` |  |

**Returns:** `System.Collections.Generic.IReadOnlyList<T><LocaleNode>`

:::

::: details `GetGemDescriptionKey(Gem)`

```csharp
public static string GetGemDescriptionKey(Gem gem)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `gem` | [`Gem`](/api/Global.Gem) |  |

**Returns:** `string`

:::

::: details `GetGemKey(string)`

```csharp
public static string GetGemKey(string gemType)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `gemType` | `string` |  |

**Returns:** `string`

:::

::: details `GetGemKey(Type)`

```csharp
public static string GetGemKey(Type gemType)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `gemType` | `System.Type` |  |

**Returns:** `string`

:::

::: details `GetGemMemory(string)`

```csharp
public static string GetGemMemory(string key)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `key` | `string` |  |

**Returns:** `string`

:::

::: details `GetGemName(Gem)`

```csharp
public static string GetGemName(Gem gem)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `gem` | [`Gem`](/api/Global.Gem) |  |

**Returns:** `string`

:::

::: details `GetGemName(string)`

```csharp
public static string GetGemName(string key)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `key` | `string` |  |

**Returns:** `string`

:::

::: details `GetGemNameKey(Gem)`

```csharp
public static string GetGemNameKey(Gem gem)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `gem` | [`Gem`](/api/Global.Gem) |  |

**Returns:** `string`

:::

::: details `GetGemShortDescription(string)`

```csharp
public static string GetGemShortDescription(string key)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `key` | `string` |  |

**Returns:** `string`

:::

::: details `GetGemTemplate(string)`

```csharp
public static string GetGemTemplate(string key)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `key` | `string` |  |

**Returns:** `string`

:::

::: details `GetRecommendedSupportedLanguage()`

```csharp
public static string GetRecommendedSupportedLanguage()
```

**Returns:** `string`

:::

::: details `GetSkillDescription(string, int)`

```csharp
public static List<LocaleNode> GetSkillDescription(string key, int configIndex)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `key` | `string` |  |
| `configIndex` | `int` |  |

**Returns:** `System.Collections.Generic.List<T><LocaleNode>`

:::

::: details `GetSkillDescriptionKey(SkillTrigger, int)`

```csharp
public static string GetSkillDescriptionKey(SkillTrigger skill, int configIndex)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `skill` | [`SkillTrigger`](/api/Global.SkillTrigger) |  |
| `configIndex` | `int` |  |

**Returns:** `string`

:::

::: details `GetSkillKey(string)`

```csharp
public static string GetSkillKey(string skillType)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `skillType` | `string` |  |

**Returns:** `string`

:::

::: details `GetSkillKey(Type)`

```csharp
public static string GetSkillKey(Type skillType)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `skillType` | `System.Type` |  |

**Returns:** `string`

:::

::: details `GetSkillLevelKey(int)`

```csharp
public static string GetSkillLevelKey(int level)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `level` | `int` |  |

**Returns:** `string`

:::

::: details `GetSkillLevelSuffix(int)`

```csharp
public static string GetSkillLevelSuffix(int level)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `level` | `int` |  |

**Returns:** `string`

:::

::: details `GetSkillLevelTemplate(int, int?)`

```csharp
public static string GetSkillLevelTemplate(int level, int? toLevel = null)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `level` | `int` |  |
| `toLevel` | `int?` |  |

**Returns:** `string`

:::

::: details `GetSkillMemory(string)`

```csharp
public static string GetSkillMemory(string key)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `key` | `string` |  |

**Returns:** `string`

:::

::: details `GetSkillName(SkillTrigger, int)`

```csharp
public static string GetSkillName(SkillTrigger skill, int configIndex)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `skill` | [`SkillTrigger`](/api/Global.SkillTrigger) |  |
| `configIndex` | `int` |  |

**Returns:** `string`

:::

::: details `GetSkillName(string, int)`

```csharp
public static string GetSkillName(string key, int configIndex)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `key` | `string` |  |
| `configIndex` | `int` |  |

**Returns:** `string`

:::

::: details `GetSkillNameKey(SkillTrigger, int)`

```csharp
public static string GetSkillNameKey(SkillTrigger skill, int configIndex)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `skill` | [`SkillTrigger`](/api/Global.SkillTrigger) |  |
| `configIndex` | `int` |  |

**Returns:** `string`

:::

::: details `GetSkillShortDesc(string, int)`

```csharp
public static string GetSkillShortDesc(string key, int configIndex)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `key` | `string` |  |
| `configIndex` | `int` |  |

**Returns:** `string`

:::

::: details `GetStarDescription(string)`

```csharp
public static List<LocaleNode> GetStarDescription(string key)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `key` | `string` |  |

**Returns:** `System.Collections.Generic.List<T><LocaleNode>`

:::

::: details `GetStarDescription(Type)`

```csharp
public static List<LocaleNode> GetStarDescription(Type type)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `type` | `System.Type` |  |

**Returns:** `System.Collections.Generic.List<T><LocaleNode>`

:::

::: details `GetStarLore(string)`

```csharp
public static string GetStarLore(string key)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `key` | `string` |  |

**Returns:** `string`

:::

::: details `GetStarName(string)`

```csharp
public static string GetStarName(string key)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `key` | `string` |  |

**Returns:** `string`

:::

::: details `GetStarName(Type)`

```csharp
public static string GetStarName(Type type)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `type` | `System.Type` |  |

**Returns:** `string`

:::

::: details `GetTreasureDescription(string)`

```csharp
public static IReadOnlyList<LocaleNode> GetTreasureDescription(string key)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `key` | `string` |  |

**Returns:** `System.Collections.Generic.IReadOnlyList<T><LocaleNode>`

:::

::: details `GetTreasureKey(string)`

```csharp
public static string GetTreasureKey(string treasureType)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `treasureType` | `string` |  |

**Returns:** `string`

:::

::: details `GetTreasureLore(string)`

```csharp
public static string GetTreasureLore(string key)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `key` | `string` |  |

**Returns:** `string`

:::

::: details `GetTreasureName(string)`

```csharp
public static string GetTreasureName(string key)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `key` | `string` |  |

**Returns:** `string`

:::

::: details `GetUIValue(string)`

```csharp
public static string GetUIValue(string key)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `key` | `string` |  |

**Returns:** `string`

:::

::: details `HighlightKeywords(string)`

```csharp
public static string HighlightKeywords(string input)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `input` | `string` |  |

**Returns:** `string`

:::

::: details `Initialize()`

```csharp
public static void Initialize()
```

:::

::: details `ProcessGenericBacktickedString(string, object, string)`

refObject can be any object including System.Type.Supported Field Types: Field/const value in refObject, Field/const value in refType instance of DewResources Database.

```csharp
public static string ProcessGenericBacktickedString(string text, object refObject, string lang = null)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `text` | `string` |  |
| `refObject` | `object` |  |
| `lang` | `string` |  |

**Returns:** `string`

:::

::: details `RenderChangedValue(string, string)`

```csharp
public static string RenderChangedValue(string prev, string after)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `prev` | `string` |  |
| `after` | `string` |  |

**Returns:** `string`

:::

::: details `RenderWeakenedValue(string, string)`

```csharp
public static string RenderWeakenedValue(string prev, string after)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `prev` | `string` |  |
| `after` | `string` |  |

**Returns:** `string`

:::

::: details `TryGetUIValue(string, out string)`

```csharp
public static bool TryGetUIValue(string key, out string value)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `key` | `string` |  |
| `value` | `string` |  |

**Returns:** `bool`

:::


## Architecture & Relationships

::: details Click to expand Architecture & Relationships

### Used By (264)

*Classes and systems that invoke, reference, or depend on `DewLocalization`:*

[Actor](/api/Global.Actor) · [Artifact](/api/Global.Artifact) · [ChargingChannel](/api/Global.ChargingChannel) · [ChatManager](/api/Global.ChatManager) · [CollectablesManager](/api/Global.CollectablesManager) · [ConversationManager](/api/Global.ConversationManager) · `ConversationShrineBase` · [Cost](/api/Global.Cost) · `CostDisplay` · [CurseStatusEffect](/api/Global.CurseStatusEffect) · [DevCanvas](/api/Global.DevCanvas) · [Dew](/api/Global.Dew) · [DewAdvText](/api/Global.DewAdvText) · `DewConsoleCommands` · [DewControlSettings_User](/api/Global.DewControlSettings_User) · [DewGUI](/api/Global.DewGUI) · [DewInput](/api/Global.DewInput) · `DewInputReadableTextExtensions` · `DewItem` · [DewLocalizedText](/api/Global.DewLocalizedText) · [DewMod](/api/Global.DewMod) · [DewPlayer](/api/Global.DewPlayer) · [DewProfile](/api/Global.DewProfile) · [DewQuest](/api/Global.DewQuest) · [DewSessionError](/api/Global.DewSessionError) · `EOSManager` · [EditSkillManager](/api/Global.EditSkillManager) · [EditSkillShrine](/api/Global.EditSkillShrine) · [GameMod_Limbo](/api/Global.GameMod_Limbo) · [GameSettingsManager](/api/Global.GameSettingsManager) · [GlobalUIManager](/api/Global.GlobalUIManager) · [Hero](/api/Global.Hero) · [InGameUIManager](/api/Global.InGameUIManager) · [LobbyManager](/api/Global.LobbyManager) · `LucidDream_MarshOfDestiny` · [MessageManager](/api/Global.MessageManager) · `Mon_GoldenLizard_ElusiveLizard` · `NextZoneOverrideTreasure` · `NodeListExtensions` · [PingManager](/api/Global.PingManager) · [PlayLobbyManager](/api/Global.PlayLobbyManager) · [QuestManager](/api/Global.QuestManager) · `Quest_HuntedByObliviax` · `Quest_KillToLiftCurse` · `Quest_LostSoul` · `Quest_TheConsortOfNight` · `Rev_AddToWishlist` · `Rev_DealElementalDamage` · `Rev_JoinDiscord` · `Rev_KillSpecificMonster` · `Rev_PlayTwiceWithSpecificTraveler` · [Rift_RoomExit](/api/Global.Rift_RoomExit) · [Rift_Sidetrack](/api/Global.Rift_Sidetrack) · `Rift_Sidetrack_TheDream` · [Room_Shortcut](/api/Global.Room_Shortcut) · `Se_GenericStealth` · `Se_MirageSkin_Delusion_Delusional` · `Se_Mon_Special_BossPolaris_Holy_ShortInvul` · `Se_OntologicalShield` · `Se_Shrine_Chaos_StatBonus` · `Se_Star_Husk_I_ShopIntimidation` · `Se_VeilOfDark` · `Shrine_AltarOfCleansing` · `Shrine_AncientRemnants` · `Shrine_Anitya` · `Shrine_ArtifactGiver` · `Shrine_Ascension` · `Shrine_BossSoul` · `Shrine_CallOfTheRavenous` · `Shrine_Chaos` · `Shrine_CookingPot` · `Shrine_CorruptedChaos` · `Shrine_Destiny` · `Shrine_DreamdustBit` · `Shrine_DreamdustBox` · `Shrine_Entanglement` · `Shrine_GoldBit` · `Shrine_GoldBox` · `Shrine_Guidance` · `Shrine_HeroSoul` · `Shrine_LoopCat` · `Shrine_Luck` · `Shrine_MarshOfDestiny_SeedOfTorment` · `Shrine_MawOfDoom` · `Shrine_Merchant_Backpack` · `Shrine_MirrorOfRemorse` · `Shrine_PileOfSnow` · `Shrine_Polaris_Teleporter` · `Shrine_PrimusDoor` · `Shrine_ScaredMaw` · `Shrine_StarCookie` · `Shrine_Stardust` · `Shrine_StarlessPath_EndingRift` · `Shrine_TheConsortOfNight` · `Shrine_TheConsortOfNight_Rift` · `Shrine_UpgradeWell` · [SkillTrigger](/api/Global.SkillTrigger) · `StarlessPath_BossPolarisManager` · [StatusEffect](/api/Global.StatusEffect) · [TitleManager](/api/Global.TitleManager) · [TransitionManager](/api/Global.TransitionManager) · `TravelerStoryPresenter` · `TutorialArrow` · `UI_AccList_Item` · `UI_AccList_PreviewWindow` · `UI_Achievement_AddedToCollectablesText` · `UI_Collectables_ObjectDetails` · `UI_Common_ChatBox_Item` · `UI_Common_MenuView` · `UI_Constellations` · `UI_Constellations_CategoryGroup` · `UI_Constellations_StarDetails` · `UI_CreditsView_NameSpawner` · `UI_DamageNumberGroup` · `UI_DamageNumberText` · `UI_DemoPromotionBanner` · `UI_DifficultyIcon` · `UI_DiscordBanner` · `UI_EmoteList_PreviewWindow` · `UI_EndingBlackScreenText` · `UI_EntityManaBar` · `UI_EntityName` · [UI_GamepadTextInput](/api/Global.UI_GamepadTextInput) · `UI_Guide_Content` · `UI_Guide_ListItem` · `UI_Guide_View` · `UI_InGame_AchievementNotifications` · `UI_InGame_AmbientLevel` · `UI_InGame_BossBars_Item` · `UI_InGame_Conversations_Instance` · `UI_InGame_CurrentArtifact` · `UI_InGame_CurseNotifications` · `UI_InGame_FloatingWindow_Chaos_Item` · `UI_InGame_FloatingWindow_ChoiceShrine` · `UI_InGame_FloatingWindow_CorruptedChaos_Item` · `UI_InGame_FloatingWindow_Hatred_Item` · `UI_InGame_FloatingWindow_Shop_Item` · `UI_InGame_GiveCurrencyView` · `UI_InGame_HeroDetailWindow_StatItem` · `UI_InGame_Interact_Custom` · `UI_InGame_Interact_Gem` · `UI_InGame_Interact_GenericButton` · `UI_InGame_Interact_Merchant` · `UI_InGame_Interact_Rift` · `UI_InGame_Interact_Shrine` · `UI_InGame_Interact_Skill` · `UI_InGame_Location` · `UI_InGame_MouseInputReceiver` · `UI_InGame_PartyDisplay_Item` · `UI_InGame_PickupNumbers_Number` · `UI_InGame_ResultView` · `UI_InGame_Result_GameStatsItem` · `UI_InGame_Result_PlayerName` · `UI_InGame_Result_PlayerStatsItem` · `UI_InGame_RoomModDisplay` · `UI_InGame_Scoreboard_PlayerItem` · `UI_InGame_SkillButton_EditSkill` · `UI_InGame_SkillNotifications` · `UI_InGame_SpectateIndicator` · `UI_InGame_VoteDisplay` · `UI_InGame_WorldMap` · `UI_LimboDepthIcon` · `UI_LobbyTag` · `UI_Lobby_AllowMidJoins` · `UI_Lobby_Constellations` · `UI_Lobby_Constellations_AlphaStar` · `UI_Lobby_Constellations_HeroConstellation_StarSlot` · `UI_Lobby_Constellations_StarDetails` · `UI_Lobby_Constellations_StarList` · `UI_Lobby_Constellations_TitleAndEmblem` · `UI_Lobby_DejavuButton` · `UI_Lobby_DejavuWindow` · `UI_Lobby_Emotes_Back` · `UI_Lobby_LobbyType` · `UI_Lobby_ObliterationView` · `UI_Lobby_PlayerListItem` · `UI_Lobby_PlayerNametag` · `UI_Lobby_ReadyStatusText` · `UI_Lobby_SelectedHeroInfo_ClassType` · `UI_Lobby_SelectedHeroInfo_Description` · `UI_Lobby_SelectedHeroInfo_Difficulty` · `UI_Lobby_SelectedHeroInfo_HeroName` · `UI_Lobby_SelectedHeroInfo_LevelUpReward` · `UI_Lobby_SelectedHeroInfo_LimboProgress` · `UI_Lobby_SelectedHeroInfo_Mastery` · `UI_Lobby_SelectedHeroInfo_Story` · `UI_Lobby_SelectedHeroInfo_Subtitle` · `UI_Lobby_SendChatMessage` · `UI_Lobby_StartButtonController` · `UI_Lobby_WaitingForContinueMidJoin_Loading` · `UI_ModManager` · `UI_ModManager_Item` · `UI_MusicBanner` · `UI_NametagList_PreviewWindow` · `UI_ProfileStatistics_Item_FavouriteItem` · `UI_ProfileStatistics_Item_FavouriteTraveler` · `UI_ProfileStatistics_Item_HeroField` · `UI_ProfileStatistics_Item_HeroSelector` · `UI_ProfileStatistics_Item_Nemesis` · `UI_Reveries_DailySlot` · `UI_Reveries_SlotBase` · `UI_Reveries_SpecialSlot` · `UI_SelectControlPresetWindow` · `UI_Settings_Item` · `UI_Settings_Item_FPSDropdown` · `UI_Settings_Item_FullScreenModeDropdown` · `UI_Settings_View` · `UI_SkinList` · `UI_SkinList_PreviewWindow` · `UI_TitleDescTooltip` · `UI_Title_ContinueDreaming` · `UI_Title_CreateLobbyView` · `UI_Title_EULAView` · `UI_Title_FindLobbyView` · `UI_Title_FindLobby_LobbyItem` · `UI_Title_LanguageSelectionView` · `UI_Title_MasteryRewardView` · `UI_Title_MasteryReward_HeroItem` · `UI_Title_PrivateDemoNotice` · `UI_Title_ProfileSelection_DeleteProfileWindow` · `UI_Title_ProfileSelection_LinkEnterCodeWindow` · `UI_Title_ProfileSelection_LinkShowCodeWindow` · `UI_Title_ProfileSelection_ListWindow` · `UI_Title_TitleView` · `UI_TooltipManager` · `UI_Tooltip_ArtifactName` · `UI_Tooltip_CollectableAchievementDescription` · `UI_Tooltip_CollectableTargetName` · `UI_Tooltip_CosmeticsName` · `UI_Tooltip_DejavuDescription` · `UI_Tooltip_EquipSwapActionIndicator` · `UI_Tooltip_EquippedGemDescriber_Item` · `UI_Tooltip_GemDescription` · `UI_Tooltip_GemQuality` · `UI_Tooltip_GemTitle` · `UI_Tooltip_LocalizationText` · `UI_Tooltip_ObjMemory` · `UI_Tooltip_ObjRarityText` · `UI_Tooltip_QuestProgress` · `UI_Tooltip_SkillCooldown` · `UI_Tooltip_SkillDescription` · `UI_Tooltip_SkillExtraDetails` · `UI_Tooltip_SkillMaxCharges` · `UI_Tooltip_SkillStarDescriber_Item` · `UI_Tooltip_SkillTitle` · `UI_Tooltip_SouvenirDesc` · `UI_Tooltip_SouvenirName` · `UI_Tooltip_StatusEffectDescription` · `UI_Tooltip_StatusEffectName` · `UI_Tooltip_TreasureDescription` · `UI_Tooltip_TreasureLore` · `UI_Tooltip_TreasureName` · `UI_Tooltip_WorldNode_Description` · `UI_Tooltip_WorldNode_HunterStatus` · `UI_Tooltip_WorldNode_Modifiers` · `UI_TravelerHeroTitle` · `UI_TravelerStory` · `UI_TravelerStory_DetailPanel` · `UI_TravelerStory_Details_Accessory` · `UI_TravelerStory_Details_Emote` · `UI_TravelerStory_Details_ShortStory` · `UI_TravelerStory_Details_Story` · `UI_TravelerStory_StoryViewer` · [ZoneManager](/api/Global.ZoneManager)

### Dependencies (10)

*Types and components that `DewLocalization` references or depends upon:*

`DewInternal.ConversationData` · `DewInternal.DewLocalizationBuildData` · `DewInternal.DewLocalizationNodeParser` · `DewInternal.ExpressionData` · `DewInternal.PerLanguageLocalizationData` · [Dew](/api/Global.Dew) · [DewInput](/api/Global.DewInput) · [Gem](/api/Global.Gem) · [NetworkedManagerBase`1](/api/Global.NetworkedManagerBase`1) · [SkillTrigger](/api/Global.SkillTrigger)

:::
