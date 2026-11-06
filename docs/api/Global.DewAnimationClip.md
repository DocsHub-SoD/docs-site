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

## Fields (5)

::: details Click to expand Fields (5)

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`entries`** | `public DewAnimationEntry[] entries` |  |
| **`hideWeaponOnHeroes`** | `public bool hideWeaponOnHeroes` |  |
| **`onlyUpperBody`** | `public bool onlyUpperBody` |  |
| **`overrideWalk`** | `[InfoBox("Override Walk cannot be Full if animating only upper body!", InfoMessageType.Error, null, VisibleIf = "@onlyUpperBody && overrideWalk == DewAnimationClip.OverrideWalkBehavior.Full")] public DewAnimationClip.OverrideWalkBehavior overrideWalk` |  |
| **`overrideWalkNormalizedDuration`** | `[ShowIf("@overrideWalk != OverrideWalkBehavior.None", true)] public float overrideWalkNormalizedDuration` |  |

:::

## Properties (1)

::: details Click to expand Properties (1)

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`resourceId`** | `public string resourceId { get; set; }` |  |

:::

## Methods (6)

::: details `GetEntry()`

```csharp
public DewAnimationEntry GetEntry()
```

**Returns:** `DewAnimationEntry`

:::

::: details `GetEntry(int)`

```csharp
public DewAnimationEntry GetEntry(int index)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `index` | `int` |  |

**Returns:** `DewAnimationEntry`

:::

::: details `GetEntry(float)`

```csharp
public DewAnimationEntry GetEntry(float value)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `value` | `float` |  |

**Returns:** `DewAnimationEntry`

:::

::: details `GetEntryIndex()`

```csharp
public int GetEntryIndex()
```

**Returns:** `int`

:::

::: details `GetEntryIndex(float, int)`

```csharp
public static int GetEntryIndex(float clipSelectValue, int entriesLength)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `clipSelectValue` | `float` |  |
| `entriesLength` | `int` |  |

**Returns:** `int`

:::

::: details `GetEntryIndex(float)`

```csharp
public int GetEntryIndex(float clipSelectValue)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `clipSelectValue` | `float` |  |

**Returns:** `int`

:::
