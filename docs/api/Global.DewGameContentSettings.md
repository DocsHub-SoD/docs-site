# Class: DewGameContentSettings

- **Category:** <span class="cat-dot" style="--cat-color: #f97316" data-cat="Data & Core Math"></span> Data & Core Math
- **Namespace:** `Global`
- **Assembly:** `Dew.Core.dll`
- **Attributes:** `[CreateAssetMenu]`

```csharp
[HideMonoScript]
[CreateAssetMenu(fileName = "New Game Content Settings", menuName = "Game Content Settings")]
public class DewGameContentSettings : ScriptableObject
```

## Fields (38)

::: details Click to expand Fields (38)

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`_availableAccessories`** | `[SerializeField] [InfoBox("All accessories will be included", InfoMessageType.Info, "@_availableAccessories.Length == 0 && parent == null")] [SerializeField] public string[] _availableAccessories` |  |
| **`_availableArtifacts`** | `[FormerlySerializedAs] [SerializeField] [FormerlySerializedAs("availableArtifacts")] [InfoBox("All artifacts will be included", InfoMessageType.Info, "@_availableArtifacts.Length == 0 && parent == null")] [SerializeField] public string[] _availableArtifacts` |  |
| **`_availableCurses`** | `[FormerlySerializedAs] [SerializeField] [FormerlySerializedAs("availableCurses")] [InfoBox("All curses will be included", InfoMessageType.Info, "@_availableCurses.Length == 0 && parent == null")] [SerializeField] public string[] _availableCurses` |  |
| **`_availableEmotes`** | `[SerializeField] [InfoBox("All emotes will be included", InfoMessageType.Info, "@_availableEmotes.Length == 0 && parent == null")] [SerializeField] public string[] _availableEmotes` |  |
| **`_availableGameModifiers`** | `[FormerlySerializedAs] [SerializeField] [FormerlySerializedAs("availableGameModifiers")] [InfoBox("All game modifiers will be included", InfoMessageType.Info, "@_availableGameModifiers.Length == 0 && parent == null")] [SerializeField] public string[] _availableGameModifiers` |  |
| **`_availableGems`** | `[FormerlySerializedAs] [SerializeField] [FormerlySerializedAs("availableGems")] [InfoBox("All gems will be included", InfoMessageType.Info, "@_availableGems.Length == 0 && parent == null")] [SerializeField] public string[] _availableGems` |  |
| **`_availableHeroes`** | `[FormerlySerializedAs] [SerializeField] [FormerlySerializedAs("availableHeroes")] [InfoBox("All heroes will be included", InfoMessageType.Info, "@_availableHeroes.Length == 0 && parent == null")] [SerializeField] public string[] _availableHeroes` |  |
| **`_availableLucidDreams`** | `[FormerlySerializedAs] [SerializeField] [FormerlySerializedAs("availableLucidDreams")] [InfoBox("All lucid dreams will be included", InfoMessageType.Info, "@_availableLucidDreams.Length == 0 && parent == null")] [SerializeField] public string[] _availableLucidDreams` |  |
| **`_availableNametags`** | `[SerializeField] [InfoBox("All nametags will be included", InfoMessageType.Info, "@_availableNametags.Length == 0 && parent == null")] [SerializeField] public string[] _availableNametags` |  |
| **`_availableRoomModifiers`** | `[FormerlySerializedAs] [SerializeField] [FormerlySerializedAs("availableRoomModifiers")] [InfoBox("All room modifiers will be included", InfoMessageType.Info, "@_availableRoomModifiers.Length == 0 && parent == null")] [SerializeField] public string[] _availableRoomModifiers` |  |
| **`_availableSkills`** | `[FormerlySerializedAs] [SerializeField] [FormerlySerializedAs("availableSkills")] [InfoBox("All skills will be included", InfoMessageType.Info, "@_availableSkills.Length == 0 && parent == null")] [SerializeField] public string[] _availableSkills` |  |
| **`_availableSkins`** | `[SerializeField] [InfoBox("All emotes will be included", InfoMessageType.Info, "@_availableEmotes.Length == 0 && parent == null")] [SerializeField] public string[] _availableSkins` |  |
| **`_availableStars`** | `[SerializeField] [InfoBox("All stars will be included", InfoMessageType.Info, "@_availableStars.Length == 0 && parent == null")] [SerializeField] public string[] _availableStars` |  |
| **`_availableTreasures`** | `[SerializeField] [InfoBox("All treasures will be included", InfoMessageType.Info, "@_availableTreasures.Length == 0 && parent == null")] [SerializeField] public string[] _availableTreasures` |  |
| **`_excludedMonsters`** | `[SerializeField] [SerializeField] public string[] _excludedMonsters` |  |
| **`_includedZones`** | `[FormerlySerializedAs] [SerializeField] [FormerlySerializedAs("includedZones")] [InfoBox("All zones will be included", InfoMessageType.Info, "@_includedZones.Length == 0 && parent == null")] [SerializeField] public string[] _includedZones` |  |
| **`_zoneCountByTier`** | `[FormerlySerializedAs] [SerializeField] [FormerlySerializedAs("zoneCountByTier")] [SerializeField] public int[] _zoneCountByTier` |  |
| **`availableAccessories`** | `[NonSerialized] public List<string> availableAccessories` |  |
| **`availableArtifacts`** | `[NonSerialized] public List<string> availableArtifacts` |  |
| **`availableCurses`** | `[NonSerialized] public List<string> availableCurses` |  |
| **`availableEmotes`** | `[NonSerialized] public List<string> availableEmotes` |  |
| **`availableGameModifiers`** | `[NonSerialized] public List<string> availableGameModifiers` |  |
| **`availableGems`** | `[NonSerialized] public List<string> availableGems` |  |
| **`availableHeroes`** | `[NonSerialized] public List<string> availableHeroes` |  |
| **`availableLucidDreams`** | `[NonSerialized] public List<string> availableLucidDreams` |  |
| **`availableNametags`** | `[NonSerialized] public List<string> availableNametags` |  |
| **`availableRoomModifiers`** | `[NonSerialized] public List<string> availableRoomModifiers` |  |
| **`availableSkills`** | `[NonSerialized] public List<string> availableSkills` |  |
| **`availableSkins`** | `[NonSerialized] public List<string> availableSkins` |  |
| **`availableStars`** | `[NonSerialized] public List<string> availableStars` |  |
| **`availableTreasures`** | `[NonSerialized] public List<string> availableTreasures` |  |
| **`excludedMonsters`** | `[NonSerialized] public List<string> excludedMonsters` |  |
| **`includeAllContents`** | `public bool includeAllContents` | Warning: Editor-only. Building standalone player with this is unsupported. |
| **`includedMonsters`** | `[ReadOnly] public string[] includedMonsters` |  |
| **`includedRooms`** | `[InfoBox("Below fields are populated automatically", InfoMessageType.Info, null)] [ReadOnly] public string[] includedRooms` |  |
| **`includedZones`** | `[NonSerialized] public List<string> includedZones` |  |
| **`parent`** | `public DewGameContentSettings parent` |  |
| **`zoneCountByTier`** | `[NonSerialized] public List<int> zoneCountByTier` |  |

:::

## Methods (4)

::: details `FilterZones(string[])`

```csharp
public string[] FilterZones(string[] zones)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `zones` | `string[]` |  |

**Returns:** `string[]`

:::

::: details `FilterZones(Zone[])`

```csharp
public Zone[] FilterZones(Zone[] zones)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `zones` | [`Zone[]`](/api/Global.Zone) |  |

**Returns:** `Zone[]`

:::

::: details `Init(bool)`

```csharp
public void Init(bool skipValidation = false)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `skipValidation` | `bool` |  |

:::

::: details `Validate()`

```csharp
public void Validate()
```

:::


## Architecture & Relationships

::: details Click to expand Architecture & Relationships

### Used By (4)

*Classes and systems that invoke, reference, or depend on `DewGameContentSettings`:*

[Dew](/api/Global.Dew) · [DewBuildProfile](/api/Global.DewBuildProfile) · [HeroSkill](/api/Global.HeroSkill) · [ZoneManager](/api/Global.ZoneManager)

### Dependencies (0)

*No outgoing class dependencies recorded.*

:::
