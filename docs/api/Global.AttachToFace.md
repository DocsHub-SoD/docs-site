# Class: AttachToFace

- **Category:** <span class="cat-dot" style="--cat-color: #64748b" data-cat="Misc & Utility"></span> Misc & Utility
- **Namespace:** `Global`
- **Assembly:** `Dew.Core.dll`
- **Attributes:** `[ExecuteAlways]`

```csharp
[ExecuteAlways]
public class AttachToFace : MonoBehaviour
```

## Fields (9)

::: details Click to expand Fields (9)

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`globalCache`** | `public static Dictionary<Renderer, AttachToFace.CacheItem> globalCache` |  |
| **`lastSetupPosition`** | `public Vector3 lastSetupPosition` |  |
| **`lastSetupRotation`** | `public Quaternion lastSetupRotation` |  |
| **`relPosition`** | `public Vector3 relPosition` |  |
| **`relRotation`** | `public Quaternion relRotation` |  |
| **`targetRenderer`** | `public SkinnedMeshRenderer targetRenderer` |  |
| **`vertexIndex0`** | `public int vertexIndex0` |  |
| **`vertexIndex1`** | `public int vertexIndex1` |  |
| **`vertexIndex2`** | `public int vertexIndex2` |  |

:::


## Architecture & Relationships

::: details Click to expand Architecture & Relationships

### Used By (0)

*No incoming dependencies recorded.*

### Dependencies (4)

*Types and components that `AttachToFace` references or depends upon:*

[Dew](/api/Global.Dew) · [DewPool](/api/Global.DewPool) · [ListReturnHandle`1](/api/Global.ListReturnHandle`1) · [QuaternionUtil](/api/Global.QuaternionUtil)

:::
