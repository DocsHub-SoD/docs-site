# Class: FeedbackManager

- **Category:** <span class="cat-dot" style="--cat-color: #3b82f6" data-cat="Managers & Systems"></span> Managers & Systems
- **Namespace:** `Global`
- **Assembly:** `Dew.Core.dll`
- **Inheritance / Derived:** [LogicBehaviour](/api/Global.LogicBehaviour) → `ManagerBase` → [FeedbackManager](/api/Global.FeedbackManager)

```csharp
public class FeedbackManager : ManagerBase<FeedbackManager>, ILogicUpdate
```

## Fields

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`dealDmg`** | `[Title("Damage Feedbacks", null, TitleAlignments.Left, true, true)] public FeedbackManager.EffectPool dealDmg` |  |
| **`dealDmgCrit`** | `public FeedbackManager.EffectPool dealDmgCrit` |  |
| **`dealDmgDot`** | `public FeedbackManager.EffectPool dealDmgDot` |  |
| **`dealDmgDotCrit`** | `public FeedbackManager.EffectPool dealDmgDotCrit` |  |
| **`fxGainStardustOnHero`** | `public GameObject fxGainStardustOnHero` |  |
| **`genericFeedbacksParent`** | `public Transform genericFeedbacksParent` |  |
| **`healCrit`** | `public FeedbackManager.EffectPool healCrit` |  |
| **`healNormal`** | `public FeedbackManager.EffectPool healNormal` |  |
| **`slowTimeBySpecialMenuVolume`** | `public Volume slowTimeBySpecialMenuVolume` |  |
| **`slowTimeBySpecialMenuWeightSpeed`** | `public float slowTimeBySpecialMenuWeightSpeed` |  |
| **`takeDmg`** | `public FeedbackManager.EffectPool takeDmg` |  |
| **`takeDmgDot`** | `public FeedbackManager.EffectPool takeDmgDot` |  |

## Methods

### `Awake()`

```csharp
protected override void Awake()
```

### `FrameUpdate()`

```csharp
public override void FrameUpdate()
```

### `PlayFeedbackEffect(string)`

```csharp
public void PlayFeedbackEffect(string feedbackName)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `feedbackName` | `string` |  |

### `StopFeedbackEffect(string)`

```csharp
public void StopFeedbackEffect(string feedbackName)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `feedbackName` | `string` |  |
