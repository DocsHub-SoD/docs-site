# Class: InGameTutorialManager

- **Category:** <span class="cat-dot" style="--cat-color: #3b82f6" data-cat="Managers & Systems"></span> Managers & Systems
- **Namespace:** `Global`
- **Assembly:** `Dew.Core.dll`
- **Inheritance / Derived:** [LogicBehaviour](/api/Global.LogicBehaviour) → `ManagerBase` → [InGameTutorialManager](/api/Global.InGameTutorialManager)

```csharp
public class InGameTutorialManager : ManagerBase<InGameTutorialManager>, ILogicUpdate
```

## Fields (14)

::: details Click to expand Fields (14)

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`arrowPrefab`** | `public TutorialArrow arrowPrefab` |  |
| **`isTutorialDisabled`** | `public bool isTutorialDisabled` |  |
| **`refEditKeyDisplay`** | `public Transform refEditKeyDisplay` |  |
| **`refGeneralSkills`** | `public Transform refGeneralSkills` |  |
| **`refHuntImminentProgress`** | `public Transform refHuntImminentProgress` |  |
| **`refHuntProgress`** | `public Transform refHuntProgress` |  |
| **`refSkillButtonE`** | `public Transform refSkillButtonE` |  |
| **`refSkillButtonMovement`** | `public Transform refSkillButtonMovement` |  |
| **`refSkillButtonQ`** | `public Transform refSkillButtonQ` |  |
| **`refSkillButtonR`** | `public Transform refSkillButtonR` |  |
| **`refSkillButtonTrait`** | `public Transform refSkillButtonTrait` |  |
| **`refSkillButtonW`** | `public Transform refSkillButtonW` |  |
| **`refSkillNotification`** | `public Transform refSkillNotification` |  |
| **`uiParent`** | `public Transform uiParent` |  |

:::

## Properties (1)

::: details Click to expand Properties (1)

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`isTutorialActive`** | `public bool isTutorialActive { get; }` |  |

:::

## Methods (6)

::: details `CreateArrow()`

```csharp
public TutorialArrow CreateArrow()
```

**Returns:** `TutorialArrow`

:::

::: details `FrameUpdate()`

```csharp
public override void FrameUpdate()
```

:::

::: details `GetRefSkill(HeroSkillLocation)`

```csharp
public Transform GetRefSkill(HeroSkillLocation type)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `type` | <a href="/enums#heroskilllocation" class="enum-link" data-tooltip="Q=0 · W=1 · E=2 · R=3 · Identity=4 (+1 more)">HeroSkillLocation</a> |  |

**Returns:** `UnityEngine.Transform`

:::

::: details `LogicUpdate(float)`

```csharp
public override void LogicUpdate(float dt)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `dt` | `float` |  |

:::

::: details `StartTutorials()`

```csharp
public void StartTutorials()
```

:::

::: details `StopTutorials()`

```csharp
public void StopTutorials()
```

:::


## Architecture & Relationships

::: details Click to expand Architecture & Relationships

### Used By (5)

*Classes and systems that invoke, reference, or depend on `InGameTutorialManager`:*

`DewConsoleCommands` · [DewInGameTutorialItem](/api/Global.DewInGameTutorialItem) · [DewSave](/api/Global.DewSave) · `PlayTutorial_Tutorial` · `UI_Settings_View`

### Dependencies (10)

*Types and components that `InGameTutorialManager` references or depends upon:*

[Dew](/api/Global.Dew) · [DewBuildProfile](/api/Global.DewBuildProfile) · [DewInGameTutorialItem](/api/Global.DewInGameTutorialItem) · [DewPlayer](/api/Global.DewPlayer) · [GameManager](/api/Global.GameManager) · [LogicBehaviour](/api/Global.LogicBehaviour) · [ManagerBase`1](/api/Global.ManagerBase`1) · [NetworkedManagerBase`1](/api/Global.NetworkedManagerBase`1) · [SafeAction](/api/Global.SafeAction) · `TutorialArrow`

### Related Enums (1)

*Enumerations referenced in fields, properties, or method signatures:*

<a href="/enums#heroskilllocation" class="enum-link" data-tooltip="Q=0 · W=1 · E=2 · R=3 · Identity=4 (+1 more)">HeroSkillLocation</a>

:::
