# Class: DewQuest

- **Namespace:** `Global`
- **Assembly:** `Dew.Core.dll`
- **Inheritance / Derived:** [DewNetworkBehaviour](/api/Global.DewNetworkBehaviour) → [Actor](/api/Global.Actor) → [GameEffect](/api/Global.GameEffect)

```csharp
public abstract class DewQuest : GameEffect, ILogicUpdate, ICleanup, ICustomDestroyRoutine
```

## Fields

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`ClientQuestEvent_OnQuestUpdated`** | `public SafeAction ClientQuestEvent_OnQuestUpdated` |  |
| **`DefaultStep`** | `public const string DefaultStep = "Default"` |  |
| **`type`** | `[BoxGroup("Quest Settings", true, false, 0)]
public QuestType type` |  |

## Properties

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`currentProgress`** | `public string currentProgress { get; set; }` |  |
| **`failReason`** | `public FailReason failReason { get; set; }` |  |
| **`progressType`** | `public QuestProgressType progressType { get; set; }` |  |
| **`questDetailedDescriptionRaw`** | `public string questDetailedDescriptionRaw { get; set; }` |  |
| **`questShortDescriptionRaw`** | `public string questShortDescriptionRaw { get; set; }` |  |
| **`questTitleRaw`** | `public string questTitleRaw { get; set; }` |  |
| **`state`** | `public QuestState state { get; set; }` |  |
| **`step`** | `[SaveVar(SaveVarFlags.ApplyAfterCreation)]
public string step { get; set; }` |  |

## Methods

### `AddStepGoal_ReachNode(NextGoalSettings)`

```csharp
public void AddStepGoal_ReachNode(NextGoalSettings settings)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `settings` | [NextGoalSettings](/api/Global.NextGoalSettings) |  |

### `CompleteQuest()`

```csharp
public void CompleteQuest()
```

### `EndStep(string)`

```csharp
public void EndStep(string nextStep = null)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `nextStep` | `string` |  |

### `FailQuest(FailReason)`

```csharp
public void FailQuest(FailReason reason)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `reason` | [FailReason](/api/Global.FailReason) |  |

### `GetInitialStep()`

Called on server.

```csharp
public virtual string GetInitialStep()
```

**Returns:** `string`

### `IsVisibleLocally()`

Is this quest visible locally? This is checked everywhere when this quest is added.

```csharp
public virtual bool IsVisibleLocally()
```

**Returns:** `bool`

### `OnCreate()`

```csharp
protected override void OnCreate()
```

### `OnDestroyActor()`

```csharp
protected override void OnDestroyActor()
```

### `OnStepEnded(string)`

Called everywhere when a step of this quest has ended.

```csharp
protected virtual void OnStepEnded(string formerStep)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `formerStep` | `string` |  |

### `OnStepStarted(bool)`

Called everywhere when a new step starts.

```csharp
protected virtual void OnStepStarted(bool isLoadedFromSave)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `isLoadedFromSave` | `bool` |  |

### `RpcInvokeQuestUpdated()`

Invoke UI update across clients. You usually don't need to call this yourself.

```csharp
public void RpcInvokeQuestUpdated()
```

### `SetLocalizedDescription(string)`

Provide null for default desc.

```csharp
public void SetLocalizedDescription(string key)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `key` | `string` |  |

### `SetLocalizedTitle(string)`

Provide null for default title.

```csharp
public void SetLocalizedTitle(string key)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `key` | `string` |  |
