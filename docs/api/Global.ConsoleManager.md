# Class: ConsoleManager

- **Category:** <span class="cat-dot" style="--cat-color: #3b82f6" data-cat="Managers & Systems"></span> Managers & Systems
- **Namespace:** `Global`
- **Assembly:** `Dew.Core.dll`
- **Inheritance / Derived:** [DewNetworkBehaviour](/api/Global.DewNetworkBehaviour) → `NetworkedManagerBase` → [ConsoleManager](/api/Global.ConsoleManager)

```csharp
public class ConsoleManager : NetworkedManagerBase<ConsoleManager>, ILogicUpdate
```

## Fields (5)

::: details Click to expand Fields (5)

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`activeCommandBinds`** | `[NonSerialized] public List<ConsoleBindItem> activeCommandBinds` |  |
| **`ClientEvent_OnCheatEnabledChanged`** | `public SafeAction<bool> ClientEvent_OnCheatEnabledChanged` |  |
| **`executionContext`** | `public ConsoleManager.ExecutionContext executionContext` |  |
| **`glDrawMaterial`** | `public Material glDrawMaterial` |  |
| **`localSelectedEntity`** | `public Entity localSelectedEntity` |  |

:::

## Properties (2)

::: details Click to expand Properties (2)

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`isCheatEnabled`** | `public bool isCheatEnabled { get; }` |  |
| **`isConsoleWindowOpen`** | `public bool isConsoleWindowOpen { get; }` |  |

:::

## Methods (11)

::: details `DisableCheats()`

```csharp
public void DisableCheats()
```

:::

::: details `EnableCheats()`

```csharp
public void EnableCheats()
```

:::

::: details `ExecuteAutoExec(AutoExecKey)`

```csharp
public void ExecuteAutoExec(ConsoleManager.AutoExecKey key)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `key` | [`ConsoleManager.AutoExecKey`](/api/Global.ConsoleManager) |  |

:::

::: details `ExecuteServerCommand(char[], Entity, Vector3, NetworkConnectionToClient)`

```csharp
public void ExecuteServerCommand(char[] charCommand, Entity selected, Vector3 cursorWorldPos, NetworkConnectionToClient sender = null)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `charCommand` | `char[]` |  |
| `selected` | [`Entity`](/api/Global.Entity) |  |
| `cursorWorldPos` | `UnityEngine.Vector3` |  |
| `sender` | `Mirror.NetworkConnectionToClient` |  |

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

::: details `OnDestroy()`

```csharp
protected override void OnDestroy()
```

:::

::: details `OnGameAreaPointerDown(PointerEventData)`

```csharp
public void OnGameAreaPointerDown(PointerEventData eventData)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `eventData` | `UnityEngine.EventSystems.PointerEventData` |  |

:::

::: details `OnLateStart()`

```csharp
public override void OnLateStart()
```

:::

::: details `OnStartClient()`

```csharp
public override void OnStartClient()
```

:::

::: details `ShouldSkipAutoExec()`

```csharp
public bool ShouldSkipAutoExec()
```

**Returns:** `bool`

:::


## Architecture & Relationships

::: details Click to expand Architecture & Relationships

### Used By (5)

*Classes and systems that invoke, reference, or depend on `ConsoleManager`:*

[CameraManager](/api/Global.CameraManager) · [DevGameManager](/api/Global.DevGameManager) · [DewNetworkManager](/api/Global.DewNetworkManager) · `UI_Dev_ConsoleSelectedEntityInfo` · `UI_InGame_MouseInputReceiver`

### Dependencies (12)

*Types and components that `ConsoleManager` references or depends upon:*

[Actor](/api/Global.Actor) · [ControlManager](/api/Global.ControlManager) · [DewNetworkBehaviour](/api/Global.DewNetworkBehaviour) · [DewPlayer](/api/Global.DewPlayer) · [Entity](/api/Global.Entity) · [EntityControl](/api/Global.EntityControl) · `InGameAnalyticsManager` · [ManagerBase`1](/api/Global.ManagerBase`1) · `NetworkConnectionToClientExtension` · [NetworkedManagerBase`1](/api/Global.NetworkedManagerBase`1) · [SafeAction`1](/api/Global.SafeAction`1) · `Mirror.GeneratedNetworkCode`

:::
