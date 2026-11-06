# Struct: WorldNodeData

- **Category:** <span class="cat-dot" style="--cat-color: #3b82f6" data-cat="Managers & Systems"></span> Managers & Systems
- **Namespace:** `Global`
- **Assembly:** `Dew.Core.dll`

```csharp
[Serializable]
public struct WorldNodeData
```

## Fields

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

## Methods

### `FindModifierIndex(string)`

```csharp
public int FindModifierIndex(string modName)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `modName` | `string` |  |

**Returns:** `int`

### `FindModifierIndex<T>()`

```csharp
public int FindModifierIndex<T>() where T : RoomModifierBase
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `` | `T` |  |

**Returns:** `int`

### `HasMainModifier()`

```csharp
public bool HasMainModifier()
```

**Returns:** `bool`

### `HasModifier(int)`

```csharp
public bool HasModifier(int id)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `id` | `int` |  |

**Returns:** `bool`

### `HasModifier(string)`

```csharp
public bool HasModifier(string modName)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `modName` | `string` |  |

**Returns:** `bool`

### `HasModifier<T>()`

```csharp
public bool HasModifier<T>() where T : RoomModifierBase
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `` | `T` |  |

**Returns:** `bool`

### `IsModifierVisible(int)`

```csharp
public bool IsModifierVisible(int index)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `index` | `int` |  |

**Returns:** `bool`

### `IsSidetrackNode()`

```csharp
public bool IsSidetrackNode()
```

**Returns:** `bool`
