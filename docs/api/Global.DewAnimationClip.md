# Class: DewAnimationClip

- **Category:** <span class="cat-dot" style="--cat-color: #64748b" data-cat="Misc & Utility"></span> Misc & Utility
- **Namespace:** `Global`
- **Assembly:** `Dew.Core.dll`

```csharp
[HideMonoScript]
[DewResourceLink(ResourceLinkBy.Guid)]
[CreateAssetMenu(fileName = "New Dew Animation Clip", menuName = "Dew Animation Clip")]
public class DewAnimationClip : ScriptableObject, ILinkedByGuid
```

## Fields

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`entries`** | `public DewAnimationEntry[] entries` |  |
| **`hideWeaponOnHeroes`** | `public bool hideWeaponOnHeroes` |  |
| **`onlyUpperBody`** | `public bool onlyUpperBody` |  |
| **`overrideWalk`** | `[InfoBox("Override Walk cannot be Full if animating only upper body!", InfoMessageType.Error, null, VisibleIf = "@onlyUpperBody && overrideWalk == DewAnimationClip.OverrideWalkBehavior.Full")] public DewAnimationClip.OverrideWalkBehavior overrideWalk` |  |
| **`overrideWalkNormalizedDuration`** | `[ShowIf("@overrideWalk != OverrideWalkBehavior.None", true)] public float overrideWalkNormalizedDuration` |  |

## Properties

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`resourceId`** | `public string resourceId { get; set; }` |  |

## Methods

### `GetEntry()`

```csharp
public DewAnimationEntry GetEntry()
```

**Returns:** `DewAnimationEntry`

### `GetEntry(int)`

```csharp
public DewAnimationEntry GetEntry(int index)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `index` | `int` |  |

**Returns:** `DewAnimationEntry`

### `GetEntry(float)`

```csharp
public DewAnimationEntry GetEntry(float value)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `value` | `float` |  |

**Returns:** `DewAnimationEntry`

### `GetEntryIndex()`

```csharp
public int GetEntryIndex()
```

**Returns:** `int`

### `GetEntryIndex(float, int)`

```csharp
public static int GetEntryIndex(float clipSelectValue, int entriesLength)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `clipSelectValue` | `float` |  |
| `entriesLength` | `int` |  |

**Returns:** `int`

### `GetEntryIndex(float)`

```csharp
public int GetEntryIndex(float clipSelectValue)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `clipSelectValue` | `float` |  |

**Returns:** `int`
