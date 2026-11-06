# Class: NextGoalSettings

- **Category:** <span class="cat-dot" style="--cat-color: #f97316" data-cat="Data & Core Math"></span> Data & Core Math
- **Namespace:** `Global`
- **Assembly:** `Dew.Core.dll`

```csharp
public class NextGoalSettings
```

## Fields (10)

::: details Click to expand Fields (10)

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`addedModifiers`** | `public AddedModifierData[] addedModifiers` |  |
| **`dontChangeDescription`** | `public bool dontChangeDescription` |  |
| **`dontChangeTitle`** | `public bool dontChangeTitle` |  |
| **`ignoreSuboptimalSituation`** | `public bool ignoreSuboptimalSituation` |  |
| **`localizedDescriptionKey`** | `public string localizedDescriptionKey` |  |
| **`localizedTitleKey`** | `public string localizedTitleKey` |  |
| **`nodeIndexSettings`** | `public GetNodeIndexSettings nodeIndexSettings` |  |
| **`onFail`** | `[NonSerialized] public Action<FailReason> onFail` | Called when players fails to reach the goal node. This can be due to skipping the goal node and moving to the next world, the applied modifier being removed by hunters, room override being overriden by other quest, etc. |
| **`onReachDestination`** | `[NonSerialized] public Action onReachDestination` | Called when players reach the goal node. |
| **`roomOverride`** | `public string roomOverride` |  |

:::


## Architecture & Relationships

::: details Click to expand Architecture & Relationships

### Used By (1)

*Classes and systems that invoke, reference, or depend on `NextGoalSettings`:*

[DewQuest](/api/Global.DewQuest)

### Dependencies (1)

*Types and components that `NextGoalSettings` references or depends upon:*

[GetNodeIndexSettings](/api/Global.GetNodeIndexSettings)

### Related Enums (1)

*Enumerations referenced in fields, properties, or method signatures:*

<a href="/enums#failreason" class="enum-link" data-tooltip="NotSpecified=0 · HunterOccupied=1 · MissedDestination=2">FailReason</a>

:::
