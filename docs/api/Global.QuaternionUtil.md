# Class: QuaternionUtil

- **Category:** <span class="cat-dot" style="--cat-color: #64748b" data-cat="Misc & Utility"></span> Misc & Utility
- **Namespace:** `Global`
- **Assembly:** `Dew.Core.dll`

```csharp
public static class QuaternionUtil
```

## Methods (4)

::: details `AngVelToDeriv(Quaternion, Vector3)`

```csharp
public static Quaternion AngVelToDeriv(Quaternion Current, Vector3 AngVel)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `Current` | `UnityEngine.Quaternion` |  |
| `AngVel` | `UnityEngine.Vector3` |  |

**Returns:** `UnityEngine.Quaternion`

:::

::: details `DerivToAngVel(Quaternion, Quaternion)`

```csharp
public static Vector3 DerivToAngVel(Quaternion Current, Quaternion Deriv)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `Current` | `UnityEngine.Quaternion` |  |
| `Deriv` | `UnityEngine.Quaternion` |  |

**Returns:** `UnityEngine.Vector3`

:::

::: details `IntegrateRotation(Quaternion, Vector3, float)`

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

:::

::: details `SmoothDamp(Quaternion, Quaternion, ref Quaternion, float)`

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

:::


## Architecture & Relationships

::: details Click to expand Architecture & Relationships

### Used By (6)

*Classes and systems that invoke, reference, or depend on `QuaternionUtil`:*

[AttachToFace](/api/Global.AttachToFace) · `Hero_Bismuth_BookController` · `UI_InGame_FollowAndFaceHero_Base` · `UI_InGame_Interact_Base` · `UI_World_FollowAndFaceCamera` · [WobblyTransform](/api/Global.WobblyTransform)

### Dependencies (0)

*No outgoing class dependencies recorded.*

:::
