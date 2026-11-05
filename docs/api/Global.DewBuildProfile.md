# Class: DewBuildProfile

- **Namespace:** `Global`
- **Assembly:** `Dew.Core.dll`

```csharp
[CreateAssetMenu(fileName = "New Build Profile", menuName = "Build Profile")]
public class DewBuildProfile : ScriptableObject
```

## Fields

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`bonusMemoryHaste`** | `public float bonusMemoryHaste` |  |
| **`buildType`** | `[HideLabel]
[EnumToggleButtons]
public BuildType buildType` |  |
| **`codenameSuffix`** | `public string codenameSuffix` |  |
| **`content`** | `[Title("Game", null, TitleAlignments.Left, true, true)]
public DewGameContentSettings content` |  |
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
| **`platform`** | `[HideLabel]
[EnumToggleButtons]
public PlatformType platform` |  |
| **`savePrefix`** | `[Title("System", null, TitleAlignments.Left, true, true)]
public string savePrefix` |  |
| **`stardustGainMultiplier`** | `public float stardustGainMultiplier` |  |
| **`startDreamDust`** | `public int startDreamDust` |  |
| **`startGold`** | `public int startGold` |  |
| **`useSteamLobbyAndRelay`** | `[ShowIf("@platform == PlatformType.STEAM", true)]
public bool useSteamLobbyAndRelay` |  |
| **`worldNodeCountOffset`** | `public int worldNodeCountOffset` |  |

## Properties

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`current`** | `public static DewBuildProfile current { get; }` |  |

## Methods

### `GetBundleVersion(string)`

```csharp
public string GetBundleVersion(string codename)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `codename` | `string` |  |

**Returns:** `string`

### `GetExtraScriptingDefines()`

```csharp
public string[] GetExtraScriptingDefines()
```

**Returns:** `string[]`

### `GetFolderName(string)`

```csharp
public string GetFolderName(string codename)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `codename` | `string` |  |

**Returns:** `string`

### `HasFeature(BuildFeatureTag)`

```csharp
public bool HasFeature(BuildFeatureTag tag)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `tag` | [BuildFeatureTag](/api/Global.BuildFeatureTag) |  |

**Returns:** `bool`

### `Init()`

```csharp
public void Init()
```

### `Validate()`

```csharp
public void Validate()
```
