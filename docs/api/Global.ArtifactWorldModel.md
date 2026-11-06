# Class: ArtifactWorldModel

- **Category:** <span class="cat-dot" style="--cat-color: #eab308" data-cat="Items & Economy"></span> Items & Economy
- **Namespace:** `Global`
- **Assembly:** `Dew.Core.dll`

```csharp
public class ArtifactWorldModel : MonoBehaviour
```

## Fields (7)

::: details Click to expand Fields (7)

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`fire`** | `public ParticleSystemRenderer fire` |  |
| **`fxAppear`** | `public GameObject fxAppear` |  |
| **`fxLoop`** | `public GameObject fxLoop` |  |
| **`fxPickUp`** | `public GameObject fxPickUp` |  |
| **`icon`** | `public MeshRenderer icon` |  |
| **`interactPivot`** | `public Transform interactPivot` |  |
| **`tinted`** | `public GameObject[] tinted` |  |

:::

## Methods (1)

::: details `Setup(Artifact)`

```csharp
public void Setup(Artifact a)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `a` | [`Artifact`](/api/Global.Artifact) |  |

:::


## Architecture & Relationships

::: details Click to expand Architecture & Relationships

### Used By (1)

*Classes and systems that invoke, reference, or depend on `ArtifactWorldModel`:*

[Artifact](/api/Global.Artifact)

### Dependencies (2)

*Types and components that `ArtifactWorldModel` references or depends upon:*

[Artifact](/api/Global.Artifact) · [DewEffect](/api/Global.DewEffect)

:::
