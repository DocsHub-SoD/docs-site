# Class: QuaternionUtil

- **Namespace:** `Global`
- **Assembly:** `Dew.Core.dll`

```csharp
public static class QuaternionUtil
```

## Methods

### `AngVelToDeriv(Quaternion, Vector3)`

```csharp
public static Quaternion AngVelToDeriv(Quaternion Current, Vector3 AngVel)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `Current` | `UnityEngine.Quaternion` |  |
| `AngVel` | `UnityEngine.Vector3` |  |

**Returns:** `UnityEngine.Quaternion`

### `DerivToAngVel(Quaternion, Quaternion)`

```csharp
public static Vector3 DerivToAngVel(Quaternion Current, Quaternion Deriv)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `Current` | `UnityEngine.Quaternion` |  |
| `Deriv` | `UnityEngine.Quaternion` |  |

**Returns:** `UnityEngine.Vector3`

### `IntegrateRotation(Quaternion, Vector3, float)`

```csharp
public static Quaternion IntegrateRotation(Quaternion Rotation, Vector3 AngularVelocity, float DeltaTime)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `Rotation` | `UnityEngine.Quaternion` |  |
| `AngularVelocity` | `UnityEngine.Vector3` |  |
| `DeltaTime` | `float` |  |

**Returns:** `UnityEngine.Quaternion`

### `SmoothDamp(Quaternion, Quaternion, ref Quaternion, float)`

```csharp
public static Quaternion SmoothDamp(Quaternion rot, Quaternion target, ref Quaternion deriv, float time)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `rot` | `UnityEngine.Quaternion` |  |
| `target` | `UnityEngine.Quaternion` |  |
| `deriv` | `UnityEngine.Quaternion` |  |
| `time` | `float` |  |

**Returns:** `UnityEngine.Quaternion`
