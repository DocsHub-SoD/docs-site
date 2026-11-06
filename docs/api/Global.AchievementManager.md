# Class: AchievementManager

- **Category:** <span class="cat-dot" style="--cat-color: #3b82f6" data-cat="Managers & Systems"></span> Managers & Systems
- **Namespace:** `Global`
- **Assembly:** `Dew.Core.dll`
- **Inheritance / Derived:** [LogicBehaviour](/api/Global.LogicBehaviour) → `ManagerBase` → [AchievementManager](/api/Global.AchievementManager)

```csharp
public class AchievementManager : ManagerBase<AchievementManager>, ILogicUpdate
```

## Fields (5)

::: details Click to expand Fields (5)

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`disableTrackingAchievements`** | `public bool disableTrackingAchievements` |  |
| **`lastGamePlayReward`** | `public static LastGamePlayReward lastGamePlayReward` |  |
| **`LocalClientEvent_OnAchievementComplete`** | `public SafeAction<Type> LocalClientEvent_OnAchievementComplete` |  |
| **`LocalClientEvent_OnLimboDepthComplete`** | `public SafeAction<int, string> LocalClientEvent_OnLimboDepthComplete` |  |
| **`trackedAchievements`** | `public List<DewAchievementItem> trackedAchievements` |  |

:::

## Properties (1)

::: details Click to expand Properties (1)

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`isTrackingAchievements`** | `public bool isTrackingAchievements { get; }` | Is locally tracking achievement? |

:::

## Methods (7)

::: details `CheckAndApplyLocalContinueData()`

```csharp
public void CheckAndApplyLocalContinueData()
```

:::

::: details `CompleteAchievement(DewAchievementItem)`

```csharp
public void CompleteAchievement(DewAchievementItem item)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `item` | [`DewAchievementItem`](/api/Global.DewAchievementItem) |  |

:::

::: details `DeleteLocalContinueData()`

```csharp
public void DeleteLocalContinueData()
```

:::

::: details `SaveLocalContinueData()`

```csharp
public void SaveLocalContinueData()
```

:::

::: details `SetPlatformStats()`

```csharp
public void SetPlatformStats()
```

:::

::: details `StartTrackingAchievements()`

```csharp
public void StartTrackingAchievements()
```

:::

::: details `StopTrackingAchievements()`

```csharp
public void StopTrackingAchievements()
```

:::
