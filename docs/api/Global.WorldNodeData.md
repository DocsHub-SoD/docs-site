# Struct: WorldNodeData

- **Category:** <span class="cat-dot" style="--cat-color: #3b82f6" data-cat="Managers & Systems"></span> Managers & Systems
- **Namespace:** `Global`
- **Assembly:** `Dew.Core.dll`

```csharp
[Serializable]
public struct WorldNodeData
```

## Fields (8)

::: details Click to expand Fields (8)

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`modifiers`** | `public List<ModifierData> modifiers` |  |
| **`position`** | `public Vector2 position` |  |
| **`room`** | `public string room` |  |
| **`roomOverride`** | `public string roomOverride` |  |
| **`roomRotIndex`** | `public int roomRotIndex` |  |
| **`roomRotValue`** | `public float roomRotValue` |  |
| **`status`** | `public WorldNodeStatus status` |  |
| **`type`** | `public WorldNodeType type` |  |

:::

## Methods (8)

::: details `FindModifierIndex(string)`

```csharp
public int FindModifierIndex(string modName)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `modName` | `string` |  |

**Returns:** `int`

:::

::: details `FindModifierIndex&lt;T&gt;()`

```csharp
public int FindModifierIndex<T>() where T : RoomModifierBase
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `` | `T` |  |

**Returns:** `int`

:::

::: details `HasMainModifier()`

```csharp
public bool HasMainModifier()
```

**Returns:** `bool`

:::

::: details `HasModifier(int)`

```csharp
public bool HasModifier(int id)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `id` | `int` |  |

**Returns:** `bool`

:::

::: details `HasModifier(string)`

```csharp
public bool HasModifier(string modName)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `modName` | `string` |  |

**Returns:** `bool`

:::

::: details `HasModifier&lt;T&gt;()`

```csharp
public bool HasModifier<T>() where T : RoomModifierBase
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `` | `T` |  |

**Returns:** `bool`

:::

::: details `IsModifierVisible(int)`

```csharp
public bool IsModifierVisible(int index)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `index` | `int` |  |

**Returns:** `bool`

:::

::: details `IsSidetrackNode()`

```csharp
public bool IsSidetrackNode()
```

**Returns:** `bool`

:::


## Architecture & Relationships

::: details Click to expand Architecture & Relationships

### Used By (13)

*Classes and systems that invoke, reference, or depend on `WorldNodeData`:*

[DewQuest](/api/Global.DewQuest) · `GameMod_CorruptedChaos` · [GameMod_Limbo](/api/Global.GameMod_Limbo) · `Ge_CallOfTheRavenous` · `Ge_Shrine_PotOfGreed` · `Quest_TheConsortOfNight` · [RoomMonsters](/api/Global.RoomMonsters) · `Se_StarlessPath_PowerOfGuidance` · `UI_InGame_WorldMap` · `UI_InGame_World_NodeItem` · `UI_Tooltip_WorldNode_Modifiers` · [ZoneManager](/api/Global.ZoneManager) · `Mirror.GeneratedNetworkCode`

### Dependencies (1)

*Types and components that `WorldNodeData` references or depends upon:*

[DewResources](/api/Global.DewResources)

### Related Enums (2)

*Enumerations referenced in fields, properties, or method signatures:*

<a href="/enums#worldnodestatus" class="enum-link" data-tooltip="Unexplored=0 · Revealed=1 · RevealedFull=2 · HasVisited=3">WorldNodeStatus</a> · <a href="/enums#worldnodetype" class="enum-link" data-tooltip="Start=0 · Combat=1 · Event=2 · Merchant=100 · Quest=101 (+2 more)">WorldNodeType</a>

:::
