# Class: DewBuildProfileGroup

- **Category:** <span class="cat-dot" style="--cat-color: #ec4899" data-cat="User Interface"></span> User Interface
- **Namespace:** `Global`
- **Assembly:** `Dew.Core.dll`
- **Attributes:** `[CreateAssetMenu]`

```csharp
[CreateAssetMenu(fileName = "New Build Profile Group", menuName = "Build Profile Group")]
public class DewBuildProfileGroup : ScriptableObject
```

## Fields (1)

::: details Click to expand Fields (1)

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`profiles`** | `[InfoBox("Place profiles with same content settings next to each other to build faster.", InfoMessageType.Info, null)] public List<DewBuildProfile> profiles` |  |

:::

## Methods (1)

::: details `Validate()`

```csharp
public void Validate()
```

:::


## Architecture & Relationships

::: details Click to expand Architecture & Relationships

### Used By (0)

*No incoming dependencies recorded.*

### Dependencies (1)

*Types and components that `DewBuildProfileGroup` references or depends upon:*

[DewBuildProfile](/api/Global.DewBuildProfile)

:::
