# Class: DewProfile

- **Category:** <span class="cat-dot" style="--cat-color: #64748b" data-cat="Misc & Utility"></span> Misc & Utility
- **Namespace:** `Global`
- **Assembly:** `Dew.Core.dll`

```csharp
public class DewProfile
```

## Fields

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

## Methods

### `DiscoverArtifact(string)`

```csharp
public void DiscoverArtifact(string g)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `g` | `string` |  |

### `DiscoverGem(string)`

```csharp
public bool DiscoverGem(string g)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `g` | `string` |  |

**Returns:** `bool`

### `DiscoverSkill(string)`

```csharp
public bool DiscoverSkill(string s)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `s` | `string` |  |

**Returns:** `bool`

### `GetLockedGemCount()`

```csharp
public int GetLockedGemCount()
```

**Returns:** `int`

### `GetLockedLucidDreamsCount()`

```csharp
public int GetLockedLucidDreamsCount()
```

**Returns:** `int`

### `GetLockedSkillCount()`

```csharp
public int GetLockedSkillCount()
```

**Returns:** `int`

### `GetPreferredGameSettings(string)`

```csharp
public PreferredGameSettings GetPreferredGameSettings(string key = null)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `key` | `string` |  |

**Returns:** `PreferredGameSettings`

### `GetUnlockedGemCount()`

```csharp
public int GetUnlockedGemCount()
```

**Returns:** `int`

### `GetUnlockedLucidDreamsCount()`

```csharp
public int GetUnlockedLucidDreamsCount()
```

**Returns:** `int`

### `GetUnlockedSkillCount()`

```csharp
public int GetUnlockedSkillCount()
```

**Returns:** `int`

### `Initialize()`

This is called on new profiles.

```csharp
public void Initialize()
```

### `LockAccessory(string)`

```csharp
public void LockAccessory(string accName)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `accName` | `string` |  |

### `LockEmote(string)`

```csharp
public void LockEmote(string emoteName)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `emoteName` | `string` |  |

### `LockGem(string)`

```csharp
public void LockGem(string g)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `g` | `string` |  |

### `LockHero(string)`

```csharp
public void LockHero(string s)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `s` | `string` |  |

### `LockLucidDream(string)`

```csharp
public void LockLucidDream(string l)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `l` | `string` |  |

### `LockNametag(string)`

```csharp
public void LockNametag(string ntName)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `ntName` | `string` |  |

### `LockSkill(string)`

```csharp
public void LockSkill(string s)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `s` | `string` |  |

### `LockSkin(string)`

```csharp
public void LockSkin(string ntName)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `ntName` | `string` |  |

### `RefundPurchase(Func<PurchaseData, bool>)`

```csharp
public int RefundPurchase(Func<DewProfile.PurchaseData, bool> condition)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `condition` | [`System.Func<T, TResult><DewProfile.PurchaseData,bool>`](/api/Global.DewProfile) |  |

**Returns:** `int`

### `UnlockAccessory(string, string)`

```csharp
public void UnlockAccessory(string accName, string ownershipKey)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `accName` | `string` |  |
| `ownershipKey` | `string` |  |

### `UnlockEmote(string, string)`

```csharp
public void UnlockEmote(string emoteName, string ownershipKey)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `emoteName` | `string` |  |
| `ownershipKey` | `string` |  |

### `UnlockGem(string)`

```csharp
public void UnlockGem(string g)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `g` | `string` |  |

### `UnlockHero(string)`

```csharp
public void UnlockHero(string s)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `s` | `string` |  |

### `UnlockLucidDream(string)`

```csharp
public void UnlockLucidDream(string l)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `l` | `string` |  |

### `UnlockNametag(string, string)`

```csharp
public void UnlockNametag(string ntName, string ownershipKey)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `ntName` | `string` |  |
| `ownershipKey` | `string` |  |

### `UnlockServerGeneratedItem(DecryptedItemData)`

```csharp
public void UnlockServerGeneratedItem(DecryptedItemData item)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `item` | `DecryptedItemData` |  |

### `UnlockSkill(string)`

```csharp
public void UnlockSkill(string s)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `s` | `string` |  |

### `UnlockSkin(string, string)`

```csharp
public void UnlockSkin(string ntName, string ownershipKey)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `ntName` | `string` |  |
| `ownershipKey` | `string` |  |

### `Validate()`

Must be called at least once before using this profile. Does error checking and validation.

```csharp
public void Validate()
```

### `ValidateProfileName(string)`

```csharp
public static bool ValidateProfileName(string name)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `name` | `string` |  |

**Returns:** `bool`
