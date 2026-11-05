# Class: DewProfile

- **Namespace:** `Global`
- **Assembly:** `Dew.Core.dll`

```csharp
public class DewProfile
```

## Fields

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`accessories`** | `public Dictionary&lt;string, DewProfile.CosmeticsData&gt; accessories` |  |
| **`achievements`** | `public Dictionary&lt;string, DewProfile.AchievementData&gt; achievements` |  |
| **`artifacts`** | `public Dictionary&lt;string, DewProfile.UnlockData&gt; artifacts` | Contains all artifacts in the game, including the ones that are excluded from the pool. |
| **`audio`** | `public DewAudioSettings_User audio` |  |
| **`completedReveries`** | `public int completedReveries` |  |
| **`controls`** | `public DewControlSettings_User controls` |  |
| **`creationDate`** | `public long creationDate` |  |
| **`CurrentSaveVersion`** | `public const int CurrentSaveVersion = 9` |  |
| **`dejavuCostReductionPeriodTimestamp`** | `public Dictionary&lt;string, long&gt; dejavuCostReductionPeriodTimestamp` |  |
| **`didMeetDreamTeller`** | `public bool didMeetDreamTeller` |  |
| **`didPlayTutorial`** | `public bool didPlayTutorial` |  |
| **`didReadConstellationNotice`** | `public bool didReadConstellationNotice` |  |
| **`didReadLoopNotice`** | `public bool didReadLoopNotice` |  |
| **`didReadPrivateDemoNotice`** | `public bool didReadPrivateDemoNotice` |  |
| **`didRewardMastery`** | `public bool didRewardMastery` |  |
| **`doneTutorials`** | `public List&lt;string&gt; doneTutorials` |  |
| **`emotes`** | `public Dictionary&lt;string, DewProfile.CosmeticsData&gt; emotes` |  |
| **`equippedEmotes`** | `public List&lt;string&gt; equippedEmotes` |  |
| **`experienceFlags`** | `public List&lt;string&gt; experienceFlags` |  |
| **`favoriteGameResults`** | `public List&lt;DewGameResult&gt; favoriteGameResults` |  |
| **`freeVersionPlayTimeMinutes`** | `public long freeVersionPlayTimeMinutes` |  |
| **`gameplay`** | `public DewGameplaySettings_User gameplay` |  |
| **`gems`** | `public Dictionary&lt;string, DewProfile.UnlockData&gt; gems` | Contains all gems in the game, including the ones that are excluded from the pool. |
| **`guid`** | `public string guid` | This will never change, unless this profile is from a different Steam account. |
| **`heroEquippedAccs`** | `public Dictionary&lt;string, List&lt;string&gt;&gt; heroEquippedAccs` |  |
| **`heroes`** | `public Dictionary&lt;string, DewProfile.UnlockData&gt; heroes` | Contains all heroes in the game. |
| **`heroLoadouts`** | `public Dictionary&lt;string, List&lt;HeroLoadoutData&gt;&gt; heroLoadouts` |  |
| **`heroSelectedSkins`** | `public Dictionary&lt;string, string&gt; heroSelectedSkins` |  |
| **`heroUnlockedStarSlots`** | `public Dictionary&lt;string, DewProfile.HeroStarSlotUnlockData&gt; heroUnlockedStarSlots` |  |
| **`language`** | `public string language` |  |
| **`lastGameResults`** | `public List&lt;DewGameResult&gt; lastGameResults` |  |
| **`lastReverieTypes`** | `public List&lt;string&gt; lastReverieTypes` |  |
| **`lastSteamId`** | `public string lastSteamId` |  |
| **`lastUnrewardedGameResult`** | `public DewGameResult lastUnrewardedGameResult` |  |
| **`lastUpsert`** | `public long lastUpsert` |  |
| **`lucidDreams`** | `public Dictionary&lt;string, DewProfile.UnlockData&gt; lucidDreams` | Contains all lucid dreams in the game, including the ones that are excluded from the pool. |
| **`maxObliterationSlots`** | `public int maxObliterationSlots` |  |
| **`name`** | `public string name` |  |
| **`nametags`** | `public Dictionary&lt;string, DewProfile.CosmeticsData&gt; nametags` |  |
| **`newStars`** | `public Dictionary&lt;string, DewProfile.StarData&gt; newStars` |  |
| **`nextRerollReplenishTimestamp`** | `public long nextRerollReplenishTimestamp` |  |
| **`preferredGameSettings`** | `public Dictionary&lt;string, PreferredGameSettings&gt; preferredGameSettings` |  |
| **`preferredNametag`** | `public string preferredNametag` |  |
| **`receivedLevelUpRewards`** | `public Dictionary&lt;string, int&gt; receivedLevelUpRewards` |  |
| **`recentlyConcededGames`** | `public List&lt;DewProfile.ConcededGameData&gt; recentlyConcededGames` |  |
| **`remainingRerolls`** | `public int remainingRerolls` |  |
| **`reverieSlots`** | `public List&lt;DewProfile.DailyReverieData&gt; reverieSlots` |  |
| **`saveVersion`** | `public int saveVersion` |  |
| **`seenGuides`** | `public List&lt;string&gt; seenGuides` |  |
| **`skills`** | `public Dictionary&lt;string, DewProfile.UnlockData&gt; skills` | Contains all skills in the game, including the ones that are character only or excluded from the pool. |
| **`skins`** | `public Dictionary&lt;string, DewProfile.CosmeticsData&gt; skins` |  |
| **`specialReverie`** | `public DewProfile.SpecialReverieData specialReverie` |  |
| **`spentStardust`** | `public int spentStardust` |  |
| **`stardust`** | `public int stardust` |  |
| **`stardustPurchases`** | `public List&lt;DewProfile.PurchaseData&gt; stardustPurchases` |  |
| **`stars`** | `public Dictionary&lt;string, DewProfile.StarData&gt; stars` | This is obsolete in non-demo builds. |
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

### `RefundPurchase(Func&lt;PurchaseData, bool&gt;)`

```csharp
public int RefundPurchase(Func<DewProfile.PurchaseData, bool> condition)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `condition` | [System.Func&lt;T, TResult&gt;&lt;DewProfile.PurchaseData,bool&gt;](/api/Global.DewProfile) |  |

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
