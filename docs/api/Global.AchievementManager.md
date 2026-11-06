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


## Architecture & Relationships

::: details Click to expand Architecture & Relationships

### Used By (2)

*Classes and systems that invoke, reference, or depend on `AchievementManager`:*

[DewAchievementItem](/api/Global.DewAchievementItem) · `UI_Tooltip_CollectableAchievementProgress`

### Dependencies (23)

*Types and components that `AchievementManager` references or depends upon:*

[ChatManager](/api/Global.ChatManager) · `DateTimeExtensions` · [Dew](/api/Global.Dew) · [DewAchievementItem](/api/Global.DewAchievementItem) · [DewBuildProfile](/api/Global.DewBuildProfile) · [DewGameObserverWithProgress](/api/Global.DewGameObserverWithProgress) · [DewNetworkManager](/api/Global.DewNetworkManager) · [DewPersistence](/api/Global.DewPersistence) · [DewPersistentGameObserver](/api/Global.DewPersistentGameObserver) · [DewPlayer](/api/Global.DewPlayer) · [DewProfile](/api/Global.DewProfile) · [DewSave](/api/Global.DewSave) · [DewSteam](/api/Global.DewSteam) · [GameManager](/api/Global.GameManager) · [Gem](/api/Global.Gem) · [Hero](/api/Global.Hero) · [LastGamePlayReward](/api/Global.LastGamePlayReward) · [ManagerBase`1](/api/Global.ManagerBase`1) · [NetworkedManagerBase`1](/api/Global.NetworkedManagerBase`1) · [SafeAction](/api/Global.SafeAction) · [SafeAction`1](/api/Global.SafeAction`1) · [SafeAction`2](/api/Global.SafeAction`2) · [SkillTrigger](/api/Global.SkillTrigger)

:::
