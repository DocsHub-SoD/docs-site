# Class: DewProfile

- **Category:** <span class="cat-dot" style="--cat-color: #64748b" data-cat="Misc & Utility"></span> Misc & Utility
- **Namespace:** `Global`
- **Assembly:** `Dew.Core.dll`

```csharp
public class DewProfile
```

## Fields (57)

::: details Click to expand Fields (57)

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`accessories`** | `public Dictionary<string, DewProfile.CosmeticsData> accessories` |  |
| **`achievements`** | `public Dictionary<string, DewProfile.AchievementData> achievements` |  |
| **`artifacts`** | `public Dictionary<string, DewProfile.UnlockData> artifacts` | Contains all artifacts in the game, including the ones that are excluded from the pool. |
| **`audio`** | `public DewAudioSettings_User audio` |  |
| **`completedReveries`** | `public int completedReveries` |  |
| **`controls`** | `public DewControlSettings_User controls` |  |
| **`creationDate`** | `public long creationDate` |  |
| **`CurrentSaveVersion`** | `public const int CurrentSaveVersion = 9` |  |
| **`dejavuCostReductionPeriodTimestamp`** | `public Dictionary<string, long> dejavuCostReductionPeriodTimestamp` |  |
| **`didMeetDreamTeller`** | `public bool didMeetDreamTeller` |  |
| **`didPlayTutorial`** | `public bool didPlayTutorial` |  |
| **`didReadConstellationNotice`** | `public bool didReadConstellationNotice` |  |
| **`didReadLoopNotice`** | `public bool didReadLoopNotice` |  |
| **`didReadPrivateDemoNotice`** | `public bool didReadPrivateDemoNotice` |  |
| **`didRewardMastery`** | `public bool didRewardMastery` |  |
| **`doneTutorials`** | `public List<string> doneTutorials` |  |
| **`emotes`** | `public Dictionary<string, DewProfile.CosmeticsData> emotes` |  |
| **`equippedEmotes`** | `public List<string> equippedEmotes` |  |
| **`experienceFlags`** | `public List<string> experienceFlags` |  |
| **`favoriteGameResults`** | `public List<DewGameResult> favoriteGameResults` |  |
| **`freeVersionPlayTimeMinutes`** | `public long freeVersionPlayTimeMinutes` |  |
| **`gameplay`** | `public DewGameplaySettings_User gameplay` |  |
| **`gems`** | `public Dictionary<string, DewProfile.UnlockData> gems` | Contains all gems in the game, including the ones that are excluded from the pool. |
| **`guid`** | `public string guid` | This will never change, unless this profile is from a different Steam account. |
| **`heroEquippedAccs`** | `public Dictionary<string, List<string>> heroEquippedAccs` |  |
| **`heroes`** | `public Dictionary<string, DewProfile.UnlockData> heroes` | Contains all heroes in the game. |
| **`heroLoadouts`** | `public Dictionary<string, List<HeroLoadoutData>> heroLoadouts` |  |
| **`heroSelectedSkins`** | `public Dictionary<string, string> heroSelectedSkins` |  |
| **`heroUnlockedStarSlots`** | `public Dictionary<string, DewProfile.HeroStarSlotUnlockData> heroUnlockedStarSlots` |  |
| **`language`** | `public string language` |  |
| **`lastGameResults`** | `public List<DewGameResult> lastGameResults` |  |
| **`lastReverieTypes`** | `public List<string> lastReverieTypes` |  |
| **`lastSteamId`** | `public string lastSteamId` |  |
| **`lastUnrewardedGameResult`** | `public DewGameResult lastUnrewardedGameResult` |  |
| **`lastUpsert`** | `public long lastUpsert` |  |
| **`lucidDreams`** | `public Dictionary<string, DewProfile.UnlockData> lucidDreams` | Contains all lucid dreams in the game, including the ones that are excluded from the pool. |
| **`maxObliterationSlots`** | `public int maxObliterationSlots` |  |
| **`name`** | `public string name` |  |
| **`nametags`** | `public Dictionary<string, DewProfile.CosmeticsData> nametags` |  |
| **`newStars`** | `public Dictionary<string, DewProfile.StarData> newStars` |  |
| **`nextRerollReplenishTimestamp`** | `public long nextRerollReplenishTimestamp` |  |
| **`preferredGameSettings`** | `public Dictionary<string, PreferredGameSettings> preferredGameSettings` |  |
| **`preferredNametag`** | `public string preferredNametag` |  |
| **`receivedLevelUpRewards`** | `public Dictionary<string, int> receivedLevelUpRewards` |  |
| **`recentlyConcededGames`** | `public List<DewProfile.ConcededGameData> recentlyConcededGames` |  |
| **`remainingRerolls`** | `public int remainingRerolls` |  |
| **`reverieSlots`** | `public List<DewProfile.DailyReverieData> reverieSlots` |  |
| **`saveVersion`** | `public int saveVersion` |  |
| **`seenGuides`** | `public List<string> seenGuides` |  |
| **`skills`** | `public Dictionary<string, DewProfile.UnlockData> skills` | Contains all skills in the game, including the ones that are character only or excluded from the pool. |
| **`skins`** | `public Dictionary<string, DewProfile.CosmeticsData> skins` |  |
| **`specialReverie`** | `public DewProfile.SpecialReverieData specialReverie` |  |
| **`spentStardust`** | `public int spentStardust` |  |
| **`stardust`** | `public int stardust` |  |
| **`stardustPurchases`** | `public List<DewProfile.PurchaseData> stardustPurchases` |  |
| **`stars`** | `public Dictionary<string, DewProfile.StarData> stars` | This is obsolete in non-demo builds. |
| **`totalPlayTimeMinutes`** | `public long totalPlayTimeMinutes` |  |

:::

## Methods (31)

::: details `DiscoverArtifact(string)`

```csharp
public void DiscoverArtifact(string g)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `g` | `string` |  |

:::

::: details `DiscoverGem(string)`

```csharp
public bool DiscoverGem(string g)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `g` | `string` |  |

**Returns:** `bool`

:::

::: details `DiscoverSkill(string)`

```csharp
public bool DiscoverSkill(string s)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `s` | `string` |  |

**Returns:** `bool`

:::

::: details `GetLockedGemCount()`

```csharp
public int GetLockedGemCount()
```

**Returns:** `int`

:::

::: details `GetLockedLucidDreamsCount()`

```csharp
public int GetLockedLucidDreamsCount()
```

**Returns:** `int`

:::

::: details `GetLockedSkillCount()`

```csharp
public int GetLockedSkillCount()
```

**Returns:** `int`

:::

::: details `GetPreferredGameSettings(string)`

```csharp
public PreferredGameSettings GetPreferredGameSettings(string key = null)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `key` | `string` |  |

**Returns:** `PreferredGameSettings`

:::

::: details `GetUnlockedGemCount()`

```csharp
public int GetUnlockedGemCount()
```

**Returns:** `int`

:::

::: details `GetUnlockedLucidDreamsCount()`

```csharp
public int GetUnlockedLucidDreamsCount()
```

**Returns:** `int`

:::

::: details `GetUnlockedSkillCount()`

```csharp
public int GetUnlockedSkillCount()
```

**Returns:** `int`

:::

::: details `Initialize()`

This is called on new profiles.

```csharp
public void Initialize()
```

:::

::: details `LockAccessory(string)`

```csharp
public void LockAccessory(string accName)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `accName` | `string` |  |

:::

::: details `LockEmote(string)`

```csharp
public void LockEmote(string emoteName)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `emoteName` | `string` |  |

:::

::: details `LockGem(string)`

```csharp
public void LockGem(string g)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `g` | `string` |  |

:::

::: details `LockHero(string)`

```csharp
public void LockHero(string s)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `s` | `string` |  |

:::

::: details `LockLucidDream(string)`

```csharp
public void LockLucidDream(string l)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `l` | `string` |  |

:::

::: details `LockNametag(string)`

```csharp
public void LockNametag(string ntName)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `ntName` | `string` |  |

:::

::: details `LockSkill(string)`

```csharp
public void LockSkill(string s)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `s` | `string` |  |

:::

::: details `LockSkin(string)`

```csharp
public void LockSkin(string ntName)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `ntName` | `string` |  |

:::

::: details `RefundPurchase(Func&lt;PurchaseData, bool&gt;)`

```csharp
public int RefundPurchase(Func<DewProfile.PurchaseData, bool> condition)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `condition` | [`System.Func<T, TResult><DewProfile.PurchaseData,bool>`](/api/Global.DewProfile) |  |

**Returns:** `int`

:::

::: details `UnlockAccessory(string, string)`

```csharp
public void UnlockAccessory(string accName, string ownershipKey)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `accName` | `string` |  |
| `ownershipKey` | `string` |  |

:::

::: details `UnlockEmote(string, string)`

```csharp
public void UnlockEmote(string emoteName, string ownershipKey)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `emoteName` | `string` |  |
| `ownershipKey` | `string` |  |

:::

::: details `UnlockGem(string)`

```csharp
public void UnlockGem(string g)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `g` | `string` |  |

:::

::: details `UnlockHero(string)`

```csharp
public void UnlockHero(string s)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `s` | `string` |  |

:::

::: details `UnlockLucidDream(string)`

```csharp
public void UnlockLucidDream(string l)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `l` | `string` |  |

:::

::: details `UnlockNametag(string, string)`

```csharp
public void UnlockNametag(string ntName, string ownershipKey)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `ntName` | `string` |  |
| `ownershipKey` | `string` |  |

:::

::: details `UnlockServerGeneratedItem(DecryptedItemData)`

```csharp
public void UnlockServerGeneratedItem(DecryptedItemData item)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `item` | `DecryptedItemData` |  |

:::

::: details `UnlockSkill(string)`

```csharp
public void UnlockSkill(string s)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `s` | `string` |  |

:::

::: details `UnlockSkin(string, string)`

```csharp
public void UnlockSkin(string ntName, string ownershipKey)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `ntName` | `string` |  |
| `ownershipKey` | `string` |  |

:::

::: details `Validate()`

Must be called at least once before using this profile. Does error checking and validation.

```csharp
public void Validate()
```

:::

::: details `ValidateProfileName(string)`

```csharp
public static bool ValidateProfileName(string name)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `name` | `string` |  |

**Returns:** `bool`

:::


## Architecture & Relationships

::: details Click to expand Architecture & Relationships

### Used By (19)

*Classes and systems that invoke, reference, or depend on `DewProfile`:*

[AchievementManager](/api/Global.AchievementManager) · `DewCloudSave` · `DewConsoleCommands` · [DewNetworkManager](/api/Global.DewNetworkManager) · [DewProfileItem](/api/Global.DewProfileItem) · `DewProfileMerge` · [DewProfileStats](/api/Global.DewProfileStats) · [DewSave](/api/Global.DewSave) · [GameSettingsManager](/api/Global.GameSettingsManager) · [QuestManager](/api/Global.QuestManager) · `Shrine_Ascension` · [TitleManager](/api/Global.TitleManager) · [Title_LastGameCharacters](/api/Global.Title_LastGameCharacters) · `TravelerStoryPresenter` · `UI_InGame_FloatingWindow_Shop` · `UI_Lobby_Constellations_StarList` · `UI_Title_CreateLobbyView` · `UI_Title_ProfileSelection_RenameProfileWindow` · `UI_Title_SplashView_SplashItem_Gift`

### Dependencies (20)

*Types and components that `DewProfile` references or depends upon:*

`DateTimeExtensions` · `DecryptedItemData` · [Dew](/api/Global.Dew) · [DewAudioSettings_User](/api/Global.DewAudioSettings_User) · [DewBuildProfile](/api/Global.DewBuildProfile) · [DewControlSettings_User](/api/Global.DewControlSettings_User) · [DewGameObserverWithProgress](/api/Global.DewGameObserverWithProgress) · [DewGameResult](/api/Global.DewGameResult) · [DewGameplaySettings_User](/api/Global.DewGameplaySettings_User) · `DewItem` · [DewLocalization](/api/Global.DewLocalization) · [DewResources](/api/Global.DewResources) · [DewSave](/api/Global.DewSave) · [DewSteam](/api/Global.DewSteam) · [GlobalLogicPackage](/api/Global.GlobalLogicPackage) · [HeroLoadoutData](/api/Global.HeroLoadoutData) · [HeroSkill](/api/Global.HeroSkill) · [PreferredGameSettings](/api/Global.PreferredGameSettings) · [ResourceLoadSettings](/api/Global.ResourceLoadSettings) · [Skin](/api/Global.Skin)

:::
