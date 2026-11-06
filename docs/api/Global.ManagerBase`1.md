# Class: ManagerBase&lt;T&gt;

- **Category:** <span class="cat-dot" style="--cat-color: #3b82f6" data-cat="Managers & Systems"></span> Managers & Systems
- **Namespace:** `Global`
- **Assembly:** `Dew.Core.dll`
- **Inheritance / Derived:** [LogicBehaviour](/api/Global.LogicBehaviour) → [AchievementManager](/api/Global.AchievementManager) → [AudioManager](/api/Global.AudioManager) → [CameraManager](/api/Global.CameraManager) → [CastIndicatorManager](/api/Global.CastIndicatorManager) → [CollectablesManager](/api/Global.CollectablesManager) → [ControlManager](/api/Global.ControlManager) → [CursorManager](/api/Global.CursorManager) → [DewCamera](/api/Global.DewCamera) → [DewPhysicsManager](/api/Global.DewPhysicsManager) → [EditSkillManager](/api/Global.EditSkillManager) → [FeedbackManager](/api/Global.FeedbackManager) → [FloatingWindowManager](/api/Global.FloatingWindowManager) → [FPSManager](/api/Global.FPSManager) → [GameCursorManager](/api/Global.GameCursorManager) → [GameLogicPackage](/api/Global.GameLogicPackage) → [GlobalLogicPackage](/api/Global.GlobalLogicPackage) → [GlobalUIManager](/api/Global.GlobalUIManager) → [InGameCrashReportManager](/api/Global.InGameCrashReportManager) → [InGameReverieManager](/api/Global.InGameReverieManager) → [InGameTutorialManager](/api/Global.InGameTutorialManager) → [InputManager](/api/Global.InputManager) → [LobbyManager](/api/Global.LobbyManager) → [LogicUpdateManager](/api/Global.LogicUpdateManager) → [MessageManager](/api/Global.MessageManager) → [MusicManager](/api/Global.MusicManager) → [NetworkLogicPackage](/api/Global.NetworkLogicPackage) → [ObjectHighlightManager](/api/Global.ObjectHighlightManager) → [ObjectiveArrowManager](/api/Global.ObjectiveArrowManager) → [PlayLobbyManager](/api/Global.PlayLobbyManager) → [ShaderManager](/api/Global.ShaderManager) → [SpawnManager](/api/Global.SpawnManager) → [StatisticsManager](/api/Global.StatisticsManager) → [TitleManager](/api/Global.TitleManager) → [TransitionManager](/api/Global.TransitionManager) → [UIManager](/api/Global.UIManager)

```csharp
[LogicUpdatePriority(-380)]
public class ManagerBase<T> : LogicBehaviour, ILogicUpdate where T : LogicBehaviour
```

## Properties

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`instance`** | `public static T instance { get; }` | If you expect the instance to be null, you MUST USE softInstance in Update loops.This will call FindObjectOfType if current instance is null, which can be very expensive. |
| **`softInstance`** | `public static T softInstance { get; }` |  |

## Methods

### `Awake()`

```csharp
protected virtual void Awake()
```

### `OnDisable()`

```csharp
protected override void OnDisable()
```

### `OnEnable()`

```csharp
protected override void OnEnable()
```
