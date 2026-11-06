# Class: DewBuildProfile

- **Category:** <span class="cat-dot" style="--cat-color: #ec4899" data-cat="User Interface"></span> User Interface
- **Namespace:** `Global`
- **Assembly:** `Dew.Core.dll`
- **Attributes:** `[CreateAssetMenu]`

```csharp
[CreateAssetMenu(fileName = "New Build Profile", menuName = "Build Profile")]
public class DewBuildProfile : ScriptableObject
```

## Fields (24)

::: details Click to expand Fields (24)

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`bonusMemoryHaste`** | `public float bonusMemoryHaste` |  |
| **`buildType`** | `[HideLabel] [EnumToggleButtons] public BuildType buildType` |  |
| **`codenameSuffix`** | `public string codenameSuffix` |  |
| **`content`** | `[Title("Game", null, TitleAlignments.Left, true, true)] public DewGameContentSettings content` |  |
| **`CurrentBuildProfileAssetPath`** | `public static string CurrentBuildProfileAssetPath` |  |
| **`customRewardFlow`** | `public RoomRewardFlowItemType[] customRewardFlow` |  |
| **`customRewardFlowFirstTime`** | `public RoomRewardFlowItemType[] customRewardFlowFirstTime` |  |
| **`defaultStardustAmount`** | `public int defaultStardustAmount` |  |
| **`disableAnalytics`** | `public bool disableAnalytics` |  |
| **`dismantleDreamDustMultiplier`** | `public float dismantleDreamDustMultiplier` |  |
| **`EditorBuildProfileDefault`** | `public static string EditorBuildProfileDefault` |  |
| **`featureTags`** | `public BuildFeatureTag[] featureTags` |  |
| **`includeCheatCommands`** | `public bool includeCheatCommands` |  |
| **`isDevelopmentBuild`** | `public bool isDevelopmentBuild` |  |
| **`killGoldMultiplier`** | `public float killGoldMultiplier` |  |
| **`luckShrineInPoolChance`** | `public float luckShrineInPoolChance` |  |
| **`luckShrineMinZoneIndex`** | `public int luckShrineMinZoneIndex` |  |
| **`platform`** | `[HideLabel] [EnumToggleButtons] public PlatformType platform` |  |
| **`savePrefix`** | `[Title("System", null, TitleAlignments.Left, true, true)] public string savePrefix` |  |
| **`stardustGainMultiplier`** | `public float stardustGainMultiplier` |  |
| **`startDreamDust`** | `public int startDreamDust` |  |
| **`startGold`** | `public int startGold` |  |
| **`useSteamLobbyAndRelay`** | `[ShowIf("@platform == PlatformType.STEAM", true)] public bool useSteamLobbyAndRelay` |  |
| **`worldNodeCountOffset`** | `public int worldNodeCountOffset` |  |

:::

## Properties (1)

::: details Click to expand Properties (1)

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`current`** | `public static DewBuildProfile current { get; }` |  |

:::

## Methods (6)

::: details `GetBundleVersion(string)`

```csharp
public string GetBundleVersion(string codename)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `codename` | `string` |  |

**Returns:** `string`

:::

::: details `GetExtraScriptingDefines()`

```csharp
public string[] GetExtraScriptingDefines()
```

**Returns:** `string[]`

:::

::: details `GetFolderName(string)`

```csharp
public string GetFolderName(string codename)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `codename` | `string` |  |

**Returns:** `string`

:::

::: details `HasFeature(BuildFeatureTag)`

```csharp
public bool HasFeature(BuildFeatureTag tag)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `tag` | [`BuildFeatureTag`](/api/Global.BuildFeatureTag) |  |

**Returns:** `bool`

:::

::: details `Init()`

```csharp
public void Init()
```

:::

::: details `Validate()`

```csharp
public void Validate()
```

:::


## Architecture & Relationships

::: details Click to expand Architecture & Relationships

### Used By (61)

*Classes and systems that invoke, reference, or depend on `DewBuildProfile`:*

[AchievementManager](/api/Global.AchievementManager) · [Dew](/api/Global.Dew) · [DewAchievementItem](/api/Global.DewAchievementItem) · [DewBuildProfileGroup](/api/Global.DewBuildProfileGroup) · `DewConsoleCommands` · [DewDifficultySettings](/api/Global.DewDifficultySettings) · [DewInput](/api/Global.DewInput) · [DewMod](/api/Global.DewMod) · [DewNetworkManager](/api/Global.DewNetworkManager) · [DewPlayer](/api/Global.DewPlayer) · [DewProfile](/api/Global.DewProfile) · [DewProfileContinue](/api/Global.DewProfileContinue) · [DewProfileStats](/api/Global.DewProfileStats) · [DewSave](/api/Global.DewSave) · [DewSteam](/api/Global.DewSteam) · `EOSManager` · [GameManager](/api/Global.GameManager) · `GameMod_GoldenLizard` · [Gem](/api/Global.Gem) · `GlobalAnalyticsManager` · [HeroSkill](/api/Global.HeroSkill) · `InGameAnalyticsManager` · [InGameTutorialManager](/api/Global.InGameTutorialManager) · [Intro_SceneController](/api/Global.Intro_SceneController) · `Intro_VideoIntroController` · [LobbyManager](/api/Global.LobbyManager) · `LobbyServiceEOS` · [LobbyServiceSteam](/api/Global.LobbyServiceSteam) · `NextZoneOverrideTreasure` · [PerBuildVisibility](/api/Global.PerBuildVisibility) · `PerFeatureVisibility` · [PerFeatureVisibility_Booth](/api/Global.PerFeatureVisibility_Booth) · [PerPlatformVisibility](/api/Global.PerPlatformVisibility) · [PickupManager](/api/Global.PickupManager) · [Pickup_BaseGoldOrb](/api/Global.Pickup_BaseGoldOrb) · [PlayGameManager](/api/Global.PlayGameManager) · [PlayLobbyManager](/api/Global.PlayLobbyManager) · [PlayLobby_Tutorial](/api/Global.PlayLobby_Tutorial) · [Rift_RoomExit](/api/Global.Rift_RoomExit) · [RoomRewards](/api/Global.RoomRewards) · [RoomRifts](/api/Global.RoomRifts) · [SkillTrigger](/api/Global.SkillTrigger) · `Splash_SceneController` · [TitleManager](/api/Global.TitleManager) · `UI_AccList` · `UI_Constellations` · `UI_Constellations_CategoryGroup` · `UI_DemoPromotionBanner` · `UI_DiscordBanner` · `UI_EmoteList` · `UI_Lobby_Constellations_StarList` · `UI_Lobby_DejavuWindow` · `UI_Lobby_ObliterationView` · `UI_MusicBanner` · `UI_NametagList` · `UI_PlayRewardAnnouncer` · `UI_Reveries_DailySlot` · `UI_ShapeOfDreamsLogo` · `UI_Title_CoopButtonManager` · `UI_Title_PrivateDemoNotice` · [ZoneManager](/api/Global.ZoneManager)

### Dependencies (1)

*Types and components that `DewBuildProfile` references or depends upon:*

[DewGameContentSettings](/api/Global.DewGameContentSettings)

### Related Enums (5)

*Enumerations referenced in fields, properties, or method signatures:*

[`BuildFeatureTag`](/enums#buildfeaturetag) · [`BuildType`](/enums#buildtype) · [`DevelopmentBuildMode`](/enums#developmentbuildmode) · [`PlatformType`](/enums#platformtype) · [`RoomRewardFlowItemType`](/enums#roomrewardflowitemtype)

:::
