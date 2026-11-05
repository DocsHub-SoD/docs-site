# Class: AchievementManager

- **Namespace:** `Global`
- **Assembly:** `Dew.Core.dll`
- **Inheritance / Derived:** [LogicBehaviour](/api/Global.LogicBehaviour) → `ManagerBase` → [AchievementManager](/api/Global.AchievementManager)

```csharp
public class AchievementManager : ManagerBase<AchievementManager>, ILogicUpdate
```

## Fields

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`disableTrackingAchievements`** | `public bool disableTrackingAchievements` |  |
| **`lastGamePlayReward`** | `public static LastGamePlayReward lastGamePlayReward` |  |
| **`LocalClientEvent_OnAchievementComplete`** | `public SafeAction&lt;Type&gt; LocalClientEvent_OnAchievementComplete` |  |
| **`LocalClientEvent_OnLimboDepthComplete`** | `public SafeAction&lt;int, string&gt; LocalClientEvent_OnLimboDepthComplete` |  |
| **`trackedAchievements`** | `public List&lt;DewAchievementItem&gt; trackedAchievements` |  |

## Properties

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`isTrackingAchievements`** | `public bool isTrackingAchievements { get; }` | Is locally tracking achievement? |

## Methods

### `CheckAndApplyLocalContinueData()`

```csharp
public void CheckAndApplyLocalContinueData()
```

### `CompleteAchievement(DewAchievementItem)`

```csharp
public void CompleteAchievement(DewAchievementItem item)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `item` | [DewAchievementItem](/api/Global.DewAchievementItem) |  |

### `DeleteLocalContinueData()`

```csharp
public void DeleteLocalContinueData()
```

### `SaveLocalContinueData()`

```csharp
public void SaveLocalContinueData()
```

### `SetPlatformStats()`

```csharp
public void SetPlatformStats()
```

### `StartTrackingAchievements()`

```csharp
public void StartTrackingAchievements()
```

### `StopTrackingAchievements()`

```csharp
public void StopTrackingAchievements()
```
