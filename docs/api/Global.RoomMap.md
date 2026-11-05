# Class: RoomMap

- **Namespace:** `Global`
- **Assembly:** `Dew.Core.dll`
- **Inheritance / Derived:** [DewNetworkBehaviour](/api/Global.DewNetworkBehaviour) → [RoomComponent](/api/Global.RoomComponent)

```csharp
public class RoomMap : RoomComponent, ILogicUpdate
```

## Fields

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`density`** | `public float density` |  |
| **`mapData`** | `[HideInInspector]
public MapData mapData` |  |
| **`mapTexture`** | `public Texture2D mapTexture` |  |

## Properties

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`fowTexture`** | `public Texture2D fowTexture { get; }` |  |

## Methods

### `ActiveLogicUpdate(float)`

```csharp
protected override void ActiveLogicUpdate(float dt)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `dt` | `float` |  |

### `IsWorldPosVisible(Vector3)`

```csharp
public bool IsWorldPosVisible(Vector3 worldPos)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `worldPos` | `UnityEngine.Vector3` |  |

**Returns:** `bool`

### `IsWorldPosVisited(Vector3)`

```csharp
public bool IsWorldPosVisited(Vector3 worldPos)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `worldPos` | `UnityEngine.Vector3` |  |

**Returns:** `bool`

### `OnDestroy()`

```csharp
protected override void OnDestroy()
```

### `OnRoomStart()`

```csharp
public override void OnRoomStart()
```
