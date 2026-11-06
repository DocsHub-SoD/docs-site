# Struct: CastInfo

- **Category:** <span class="cat-dot" style="--cat-color: #ef4444" data-cat="Combat & Abilities"></span> Combat & Abilities
- **Namespace:** `Global`
- **Assembly:** `Dew.Core.dll`

```csharp
public struct CastInfo
```

## Fields

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`angle`** | `public float angle` |  |
| **`animSelectValue`** | `public float animSelectValue` | This is populated on AbilityTrigger.OnCastStart. |
| **`caster`** | `public Entity caster` |  |
| **`point`** | `public Vector3 point` |  |
| **`target`** | `public Entity target` |  |

## Properties

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`forward`** | `public Vector3 forward { get; }` |  |
| **`rotation`** | `public Quaternion rotation { get; }` |  |

## Methods

### `GetAngle(Quaternion)`

```csharp
public static float GetAngle(Quaternion rotation)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `rotation` | `UnityEngine.Quaternion` |  |

**Returns:** `float`

### `GetAngle(Vector3)`

```csharp
public static float GetAngle(Vector3 forward)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `forward` | `UnityEngine.Vector3` |  |

**Returns:** `float`
