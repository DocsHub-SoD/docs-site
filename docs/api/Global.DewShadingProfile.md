# Class: DewShadingProfile

- **Category:** <span class="cat-dot" style="--cat-color: #64748b" data-cat="Misc & Utility"></span> Misc & Utility
- **Namespace:** `Global`
- **Assembly:** `Dew.Core.dll`
- **Attributes:** `[CreateAssetMenu]`

```csharp
[CreateAssetMenu(fileName = "Shading", menuName = "Dew/Dew Shading Profile", order = 1)]
public class DewShadingProfile : ScriptableObject
```

## Fields (5)

::: details Click to expand Fields (5)

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`directionalLightRamp`** | `public Texture directionalLightRamp` |  |
| **`lightRamp`** | `public Texture lightRamp` |  |
| **`termAlpha`** | `public float termAlpha` |  |
| **`termBeta`** | `public float termBeta` |  |
| **`termGamma`** | `public float termGamma` |  |

:::


## Architecture & Relationships

::: details Click to expand Architecture & Relationships

### Used By (1)

*Classes and systems that invoke, reference, or depend on `DewShadingProfile`:*

[ShaderManager](/api/Global.ShaderManager)

### Dependencies (0)

*No outgoing class dependencies recorded.*

:::
