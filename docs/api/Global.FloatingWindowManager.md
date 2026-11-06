# Class: FloatingWindowManager

- **Category:** <span class="cat-dot" style="--cat-color: #ec4899" data-cat="User Interface"></span> User Interface
- **Namespace:** `Global`
- **Assembly:** `Dew.Core.dll`
- **Inheritance / Derived:** [LogicBehaviour](/api/Global.LogicBehaviour) → `ManagerBase` → [FloatingWindowManager](/api/Global.FloatingWindowManager)

```csharp
public class FloatingWindowManager : ManagerBase<FloatingWindowManager>, ILogicUpdate
```

## Fields (3)

::: details Click to expand Fields (3)

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`backButtonPriority`** | `public int backButtonPriority` |  |
| **`maxDistance`** | `public float maxDistance` |  |
| **`onTargetChanged`** | `public Action<MonoBehaviour> onTargetChanged` |  |

:::

## Properties (2)

::: details Click to expand Properties (2)

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`currentTarget`** | `public MonoBehaviour currentTarget { get; }` |  |
| **`lastSetTargetUnscaledTime`** | `public float lastSetTargetUnscaledTime { get; }` |  |

:::

## Methods (4)

::: details `ClearTarget()`

```csharp
public void ClearTarget()
```

:::

::: details `FrameUpdate()`

```csharp
public override void FrameUpdate()
```

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

::: details `SetTarget(MonoBehaviour)`

```csharp
public void SetTarget(MonoBehaviour newTarget)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `newTarget` | `UnityEngine.MonoBehaviour` |  |

:::


## Architecture & Relationships

::: details Click to expand Architecture & Relationships

### Used By (22)

*Classes and systems that invoke, reference, or depend on `FloatingWindowManager`:*

[ChoiceShrine](/api/Global.ChoiceShrine) · [ControlManager](/api/Global.ControlManager) · [EditSkillManager](/api/Global.EditSkillManager) · [PropEnt_Merchant_Base](/api/Global.PropEnt_Merchant_Base) · `Shrine_Chaos` · `Shrine_CorruptedChaos` · `Shrine_Hatred` · `Shrine_MarshOfDestiny_SeedOfTorment` · `UI_InGame_FloatingWindow_Chaos` · `UI_InGame_FloatingWindow_Chaos_Item` · `UI_InGame_FloatingWindow_ChoiceShrine` · `UI_InGame_FloatingWindow_ChoiceShrine_Item` · `UI_InGame_FloatingWindow_CorruptedChaos` · `UI_InGame_FloatingWindow_CorruptedChaos_Item` · `UI_InGame_FloatingWindow_Hatred` · `UI_InGame_FloatingWindow_Hatred_Item` · `UI_InGame_FloatingWindow_SeedOfTorment` · `UI_InGame_FloatingWindow_Shop` · `UI_InGame_FloatingWindow_Shop_Item` · `UI_InGame_InvertedControlsCursor` · `UI_InGame_MouseInputReceiver` · `UI_InGame_StardustGroup`

### Dependencies (14)

*Types and components that `FloatingWindowManager` references or depends upon:*

[Actor](/api/Global.Actor) · [ActorCheck](/api/Global.ActorCheck) · [ControlManager](/api/Global.ControlManager) · [DewInput](/api/Global.DewInput) · [DewPlayer](/api/Global.DewPlayer) · [EntityCheck](/api/Global.EntityCheck) · [GlobalUIManager](/api/Global.GlobalUIManager) · [InGameUIManager](/api/Global.InGameUIManager) · [LogicBehaviour](/api/Global.LogicBehaviour) · [ManagerBase`1](/api/Global.ManagerBase`1) · [NetworkedManagerBase`1](/api/Global.NetworkedManagerBase`1) · [SafeAction`1](/api/Global.SafeAction`1) · [Shrine](/api/Global.Shrine) · [ZoneManager](/api/Global.ZoneManager)

:::
