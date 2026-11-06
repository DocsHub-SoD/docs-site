# Class: FeedbackManager

- **Category:** <span class="cat-dot" style="--cat-color: #3b82f6" data-cat="Managers & Systems"></span> Managers & Systems
- **Namespace:** `Global`
- **Assembly:** `Dew.Core.dll`
- **Inheritance / Derived:** [LogicBehaviour](/api/Global.LogicBehaviour) → `ManagerBase` → [FeedbackManager](/api/Global.FeedbackManager)

```csharp
public class FeedbackManager : ManagerBase<FeedbackManager>, ILogicUpdate
```

## Fields (12)

::: details Click to expand Fields (12)

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

:::

## Methods (4)

::: details `Awake()`

```csharp
protected override void Awake()
```

:::

::: details `FrameUpdate()`

```csharp
public override void FrameUpdate()
```

:::

::: details `PlayFeedbackEffect(string)`

```csharp
public void PlayFeedbackEffect(string feedbackName)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `feedbackName` | `string` |  |

:::

::: details `StopFeedbackEffect(string)`

```csharp
public void StopFeedbackEffect(string feedbackName)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `feedbackName` | `string` |  |

:::


## Architecture & Relationships

::: details Click to expand Architecture & Relationships

### Used By (16)

*Classes and systems that invoke, reference, or depend on `FeedbackManager`:*

[ControlManager](/api/Global.ControlManager) · [EditSkillManager](/api/Global.EditSkillManager) · [FxFeedbackEffect](/api/Global.FxFeedbackEffect) · [SkillTrigger](/api/Global.SkillTrigger) · `UI_InGame_CurseNotifications` · `UI_InGame_FloatingWindow_Chaos` · `UI_InGame_FloatingWindow_ChoiceShrine` · `UI_InGame_FloatingWindow_CorruptedChaos` · `UI_InGame_FloatingWindow_Hatred` · `UI_InGame_FloatingWindow_SeedOfTorment` · `UI_InGame_FloatingWindow_Shop` · `UI_InGame_ResultView` · `UI_InGame_SkillButton_EditSkill` · `UI_InGame_SkillNotifications` · `UI_InGame_VoteDisplay` · `UI_InGame_WorldView`

### Dependencies (7)

*Types and components that `FeedbackManager` references or depends upon:*

[DewEffect](/api/Global.DewEffect) · [DewPlayer](/api/Global.DewPlayer) · [LogicBehaviour](/api/Global.LogicBehaviour) · [ManagerBase`1](/api/Global.ManagerBase`1) · [NetworkedManagerBase`1](/api/Global.NetworkedManagerBase`1) · [SafeAction`1](/api/Global.SafeAction`1) · [TimescaleManager](/api/Global.TimescaleManager)

:::
