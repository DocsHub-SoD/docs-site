# Class: NetworkedManagerBase&lt;T&gt;

- **Category:** <span class="cat-dot" style="--cat-color: #3b82f6" data-cat="Managers & Systems"></span> Managers & Systems
- **Namespace:** `Global`
- **Assembly:** `Dew.Core.dll`
- **Inheritance / Derived:** [DewNetworkBehaviour](/api/Global.DewNetworkBehaviour) → [ActorManager](/api/Global.ActorManager) → [ChatManager](/api/Global.ChatManager) → [ClientEventManager](/api/Global.ClientEventManager) → [ConsoleManager](/api/Global.ConsoleManager) → [ConversationManager](/api/Global.ConversationManager) → [FlavourManager](/api/Global.FlavourManager) → [GameManager](/api/Global.GameManager) → [GameResultManager](/api/Global.GameResultManager) → [GameSettingsManager](/api/Global.GameSettingsManager) → [LootManager](/api/Global.LootManager) → [PickupManager](/api/Global.PickupManager) → [PingManager](/api/Global.PingManager) → [QuestManager](/api/Global.QuestManager) → [TimescaleManager](/api/Global.TimescaleManager) → [ZoneManager](/api/Global.ZoneManager)

```csharp
[LogicUpdatePriority(-300)]
public class NetworkedManagerBase<T> : DewNetworkBehaviour, ILogicUpdate where T : DewNetworkBehaviour
```

## Properties

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`instance`** | `public static T instance { get; }` | If you expect the instance to be null, you MUST USE softInstance in Update loops.This will call FindObjectOfType if current instance is null, which can be very expensive. |
| **`softInstance`** | `public static T softInstance { get; }` |  |

## Methods

### `Awake()`

```csharp
protected override void Awake()
```

### `OnEnable()`

```csharp
protected virtual void OnEnable()
```

### `OnStartClient()`

```csharp
public override void OnStartClient()
```

### `OnStopClient()`

```csharp
public override void OnStopClient()
```
