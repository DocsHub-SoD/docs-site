# Class: RoomMap

- **Category:** <span class="cat-dot" style="--cat-color: #3b82f6" data-cat="Managers & Systems"></span> Managers & Systems
- **Namespace:** `Global`
- **Assembly:** `Dew.Core.dll`
- **Inheritance / Derived:** [DewNetworkBehaviour](/api/Global.DewNetworkBehaviour) → [RoomComponent](/api/Global.RoomComponent)

```csharp
public class RoomMap : RoomComponent, ILogicUpdate
```

## Fields (3)

::: details Click to expand Fields (3)

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`density`** | `public float density` |  |
| **`mapData`** | `[HideInInspector] public MapData mapData` |  |
| **`mapTexture`** | `public Texture2D mapTexture` |  |

:::

## Properties (1)

::: details Click to expand Properties (1)

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`fowTexture`** | `public Texture2D fowTexture { get; }` |  |

:::

## Methods (5)

::: details `ActiveLogicUpdate(float)`

```csharp
protected override void ActiveLogicUpdate(float dt)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `dt` | `float` |  |

:::

::: details `IsWorldPosVisible(Vector3)`

```csharp
public bool IsWorldPosVisible(Vector3 worldPos)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `worldPos` | `UnityEngine.Vector3` |  |

**Returns:** `bool`

:::

::: details `IsWorldPosVisited(Vector3)`

```csharp
public bool IsWorldPosVisited(Vector3 worldPos)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `worldPos` | `UnityEngine.Vector3` |  |

**Returns:** `bool`

:::

::: details `OnDestroy()`

```csharp
protected override void OnDestroy()
```

:::

::: details `OnRoomStart()`

```csharp
public override void OnRoomStart()
```

:::
