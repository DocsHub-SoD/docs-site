# Class: DewQuest

- **Category:** <span class="cat-dot" style="--cat-color: #22c55e" data-cat="Actors & Entities"></span> Actors & Entities
- **Namespace:** `Global`
- **Assembly:** `Dew.Core.dll`
- **Inheritance / Derived:** [DewNetworkBehaviour](/api/Global.DewNetworkBehaviour) → [Actor](/api/Global.Actor) → [GameEffect](/api/Global.GameEffect)

```csharp
public abstract class DewQuest : GameEffect, ILogicUpdate, ICleanup, ICustomDestroyRoutine
```

## Fields (3)

::: details Click to expand Fields (3)

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`ClientQuestEvent_OnQuestUpdated`** | `public SafeAction ClientQuestEvent_OnQuestUpdated` |  |
| **`DefaultStep`** | `public const string DefaultStep = "Default"` |  |
| **`type`** | `[BoxGroup("Quest Settings", true, false, 0)] public QuestType type` |  |

:::

## Properties (8)

::: details Click to expand Properties (8)

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`currentProgress`** | `public string currentProgress { get; set; }` |  |
| **`failReason`** | `public FailReason failReason { get; set; }` |  |
| **`progressType`** | `public QuestProgressType progressType { get; set; }` |  |
| **`questDetailedDescriptionRaw`** | `public string questDetailedDescriptionRaw { get; set; }` |  |
| **`questShortDescriptionRaw`** | `public string questShortDescriptionRaw { get; set; }` |  |
| **`questTitleRaw`** | `public string questTitleRaw { get; set; }` |  |
| **`state`** | `public QuestState state { get; set; }` |  |
| **`step`** | `[SaveVar] [SaveVar(SaveVarFlags.ApplyAfterCreation)] public string step { get; set; }` |  |

:::

## Methods (13)

::: details `AddStepGoal_ReachNode(NextGoalSettings)`

```csharp
public void AddStepGoal_ReachNode(NextGoalSettings settings)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `settings` | [`NextGoalSettings`](/api/Global.NextGoalSettings) |  |

:::

::: details `CompleteQuest()`

```csharp
public void CompleteQuest()
```

:::

::: details `EndStep(string)`

```csharp
public void EndStep(string nextStep = null)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `nextStep` | `string` |  |

:::

::: details `FailQuest(FailReason)`

```csharp
public void FailQuest(FailReason reason)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `reason` | [`FailReason`](/api/Global.FailReason) |  |

:::

::: details `GetInitialStep()`

Called on server.

```csharp
public virtual string GetInitialStep()
```

**Returns:** `string`

:::

::: details `IsVisibleLocally()`

Is this quest visible locally? This is checked everywhere when this quest is added.

```csharp
public virtual bool IsVisibleLocally()
```

**Returns:** `bool`

:::

::: details `OnCreate()`

```csharp
protected override void OnCreate()
```

:::

::: details `OnDestroyActor()`

```csharp
protected override void OnDestroyActor()
```

:::

::: details `OnStepEnded(string)`

Called everywhere when a step of this quest has ended.

```csharp
protected virtual void OnStepEnded(string formerStep)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `formerStep` | `string` |  |

:::

::: details `OnStepStarted(bool)`

Called everywhere when a new step starts.

```csharp
protected virtual void OnStepStarted(bool isLoadedFromSave)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `isLoadedFromSave` | `bool` |  |

:::

::: details `RpcInvokeQuestUpdated()`

Invoke UI update across clients. You usually don't need to call this yourself.

```csharp
public void RpcInvokeQuestUpdated()
```

:::

::: details `SetLocalizedDescription(string)`

Provide null for default desc.

```csharp
public void SetLocalizedDescription(string key)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `key` | `string` |  |

:::

::: details `SetLocalizedTitle(string)`

Provide null for default title.

```csharp
public void SetLocalizedTitle(string key)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `key` | `string` |  |

:::


## Architecture & Relationships

::: details Click to expand Architecture & Relationships

### Used By (21)

*Classes and systems that invoke, reference, or depend on `DewQuest`:*

[CurseStatusEffect](/api/Global.CurseStatusEffect) · `Quest_CallOfTheRavenous` · `Quest_FragmentOfRadiance` · `Quest_GuidingCompass` · `Quest_HuntedByObliviax` · `Quest_KillToLiftCurse` · `Quest_Limbo` · `Quest_LostSoul` · `Quest_SecretMeeting` · `Quest_ShapeOfDreams` · `Quest_StarSeekersJournal` · `Quest_StrayMemory` · `Quest_SuspiciousTreasureMap` · `Quest_TheConsortOfNight` · `Quest_TreasureMap` · `UI_InGame_QuestDisplay` · `UI_InGame_QuestDisplay_Item` · `UI_TooltipManager` · `UI_Tooltip_QuestDescription` · `UI_Tooltip_QuestProgress` · `UI_Tooltip_QuestTitle`

### Dependencies (14)

*Types and components that `DewQuest` references or depends upon:*

[Actor](/api/Global.Actor) · [Dew](/api/Global.Dew) · [DewLocalization](/api/Global.DewLocalization) · [EventInfoLoadRoom](/api/Global.EventInfoLoadRoom) · [GameEffect](/api/Global.GameEffect) · [ListReturnHandle`1](/api/Global.ListReturnHandle`1) · [NetworkedManagerBase`1](/api/Global.NetworkedManagerBase`1) · [NextGoalSettings](/api/Global.NextGoalSettings) · [SafeAction](/api/Global.SafeAction) · [SafeAction`1](/api/Global.SafeAction`1) · `ToListNonAllocExtensions` · [WorldNodeData](/api/Global.WorldNodeData) · [ZoneManager](/api/Global.ZoneManager) · `Mirror.GeneratedNetworkCode`

### Related Enums (5)

*Enumerations referenced in fields, properties, or method signatures:*

[`FailReason`](/enums#failreason) · [`QuestProgressType`](/enums#questprogresstype) · [`QuestState`](/enums#queststate) · [`QuestType`](/enums#questtype) · [`SaveVarFlags`](/enums#savevarflags)

:::
