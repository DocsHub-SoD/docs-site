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
