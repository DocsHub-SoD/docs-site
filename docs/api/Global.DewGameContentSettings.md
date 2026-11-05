# Class: DewGameContentSettings

- **Namespace:** `Global`
- **Assembly:** `Dew.Core.dll`

```csharp
[HideMonoScript]
[CreateAssetMenu(fileName = "New Game Content Settings", menuName = "Game Content Settings")]
public class DewGameContentSettings : ScriptableObject
```

## Fields

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`_availableAccessories`** | `[InfoBox("All accessories will be included", InfoMessageType.Info, "@_availableAccessories.Length == 0 && parent == null")]
[SerializeField]
public string[] _availableAccessories` |  |
| **`_availableArtifacts`** | `[FormerlySerializedAs("availableArtifacts")]
[InfoBox("All artifacts will be included", InfoMessageType.Info, "@_availableArtifacts.Length == 0 && parent == null")]
[SerializeField]
public string[] _availableArtifacts` |  |
| **`_availableCurses`** | `[FormerlySerializedAs("availableCurses")]
[InfoBox("All curses will be included", InfoMessageType.Info, "@_availableCurses.Length == 0 && parent == null")]
[SerializeField]
public string[] _availableCurses` |  |
| **`_availableEmotes`** | `[InfoBox("All emotes will be included", InfoMessageType.Info, "@_availableEmotes.Length == 0 && parent == null")]
[SerializeField]
public string[] _availableEmotes` |  |
| **`_availableGameModifiers`** | `[FormerlySerializedAs("availableGameModifiers")]
[InfoBox("All game modifiers will be included", InfoMessageType.Info, "@_availableGameModifiers.Length == 0 && parent == null")]
[SerializeField]
public string[] _availableGameModifiers` |  |
| **`_availableGems`** | `[FormerlySerializedAs("availableGems")]
[InfoBox("All gems will be included", InfoMessageType.Info, "@_availableGems.Length == 0 && parent == null")]
[SerializeField]
public string[] _availableGems` |  |
| **`_availableHeroes`** | `[FormerlySerializedAs("availableHeroes")]
[InfoBox("All heroes will be included", InfoMessageType.Info, "@_availableHeroes.Length == 0 && parent == null")]
[SerializeField]
public string[] _availableHeroes` |  |
| **`_availableLucidDreams`** | `[FormerlySerializedAs("availableLucidDreams")]
[InfoBox("All lucid dreams will be included", InfoMessageType.Info, "@_availableLucidDreams.Length == 0 && parent == null")]
[SerializeField]
public string[] _availableLucidDreams` |  |
| **`_availableNametags`** | `[InfoBox("All nametags will be included", InfoMessageType.Info, "@_availableNametags.Length == 0 && parent == null")]
[SerializeField]
public string[] _availableNametags` |  |
| **`_availableRoomModifiers`** | `[FormerlySerializedAs("availableRoomModifiers")]
[InfoBox("All room modifiers will be included", InfoMessageType.Info, "@_availableRoomModifiers.Length == 0 && parent == null")]
[SerializeField]
public string[] _availableRoomModifiers` |  |
| **`_availableSkills`** | `[FormerlySerializedAs("availableSkills")]
[InfoBox("All skills will be included", InfoMessageType.Info, "@_availableSkills.Length == 0 && parent == null")]
[SerializeField]
public string[] _availableSkills` |  |
| **`_availableSkins`** | `[InfoBox("All emotes will be included", InfoMessageType.Info, "@_availableEmotes.Length == 0 && parent == null")]
[SerializeField]
public string[] _availableSkins` |  |
| **`_availableStars`** | `[InfoBox("All stars will be included", InfoMessageType.Info, "@_availableStars.Length == 0 && parent == null")]
[SerializeField]
public string[] _availableStars` |  |
| **`_availableTreasures`** | `[InfoBox("All treasures will be included", InfoMessageType.Info, "@_availableTreasures.Length == 0 && parent == null")]
[SerializeField]
public string[] _availableTreasures` |  |
| **`_excludedMonsters`** | `[SerializeField]
public string[] _excludedMonsters` |  |
| **`_includedZones`** | `[FormerlySerializedAs("includedZones")]
[InfoBox("All zones will be included", InfoMessageType.Info, "@_includedZones.Length == 0 && parent == null")]
[SerializeField]
public string[] _includedZones` |  |
| **`_zoneCountByTier`** | `[FormerlySerializedAs("zoneCountByTier")]
[SerializeField]
public int[] _zoneCountByTier` |  |
| **`availableAccessories`** | `[NonSerialized]
public List&lt;string&gt; availableAccessories` |  |
| **`availableArtifacts`** | `[NonSerialized]
public List&lt;string&gt; availableArtifacts` |  |
| **`availableCurses`** | `[NonSerialized]
public List&lt;string&gt; availableCurses` |  |
| **`availableEmotes`** | `[NonSerialized]
public List&lt;string&gt; availableEmotes` |  |
| **`availableGameModifiers`** | `[NonSerialized]
public List&lt;string&gt; availableGameModifiers` |  |
| **`availableGems`** | `[NonSerialized]
public List&lt;string&gt; availableGems` |  |
| **`availableHeroes`** | `[NonSerialized]
public List&lt;string&gt; availableHeroes` |  |
| **`availableLucidDreams`** | `[NonSerialized]
public List&lt;string&gt; availableLucidDreams` |  |
| **`availableNametags`** | `[NonSerialized]
public List&lt;string&gt; availableNametags` |  |
| **`availableRoomModifiers`** | `[NonSerialized]
public List&lt;string&gt; availableRoomModifiers` |  |
| **`availableSkills`** | `[NonSerialized]
public List&lt;string&gt; availableSkills` |  |
| **`availableSkins`** | `[NonSerialized]
public List&lt;string&gt; availableSkins` |  |
| **`availableStars`** | `[NonSerialized]
public List&lt;string&gt; availableStars` |  |
| **`availableTreasures`** | `[NonSerialized]
public List&lt;string&gt; availableTreasures` |  |
| **`excludedMonsters`** | `[NonSerialized]
public List&lt;string&gt; excludedMonsters` |  |
| **`includeAllContents`** | `public bool includeAllContents` | Warning: Editor-only. Building standalone player with this is unsupported. |
| **`includedMonsters`** | `[ReadOnly]
public string[] includedMonsters` |  |
| **`includedRooms`** | `[InfoBox("Below fields are populated automatically", InfoMessageType.Info, null)]
[ReadOnly]
public string[] includedRooms` |  |
| **`includedZones`** | `[NonSerialized]
public List&lt;string&gt; includedZones` |  |
| **`parent`** | `public DewGameContentSettings parent` |  |
| **`zoneCountByTier`** | `[NonSerialized]
public List&lt;int&gt; zoneCountByTier` |  |

## Methods

### `FilterZones(string[])`

```csharp
public string[] FilterZones(string[] zones)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `zones` | `string[]` |  |

**Returns:** `string[]`

### `FilterZones(Zone[])`

```csharp
public Zone[] FilterZones(Zone[] zones)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `zones` | [Zone[]](/api/Global.Zone) |  |

**Returns:** `Zone[]`

### `Init(bool)`

```csharp
public void Init(bool skipValidation = false)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `skipValidation` | `bool` |  |

### `Validate()`

```csharp
public void Validate()
```
