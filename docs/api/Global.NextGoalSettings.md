# Class: NextGoalSettings

- **Namespace:** `Global`
- **Assembly:** `Dew.Core.dll`

```csharp
public class NextGoalSettings
```

## Fields

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`addedModifiers`** | `public AddedModifierData[] addedModifiers` |  |
| **`dontChangeDescription`** | `public bool dontChangeDescription` |  |
| **`dontChangeTitle`** | `public bool dontChangeTitle` |  |
| **`ignoreSuboptimalSituation`** | `public bool ignoreSuboptimalSituation` |  |
| **`localizedDescriptionKey`** | `public string localizedDescriptionKey` |  |
| **`localizedTitleKey`** | `public string localizedTitleKey` |  |
| **`nodeIndexSettings`** | `public GetNodeIndexSettings nodeIndexSettings` |  |
| **`onFail`** | `[NonSerialized]
public Action&lt;FailReason&gt; onFail` | Called when players fails to reach the goal node. This can be due to skipping the goal node and moving to the next world, the applied modifier being removed by hunters, room override being overriden by other quest, etc. |
| **`onReachDestination`** | `[NonSerialized]
public Action onReachDestination` | Called when players reach the goal node. |
| **`roomOverride`** | `public string roomOverride` |  |
