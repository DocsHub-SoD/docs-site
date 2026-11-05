# Class: LobbyUIManager

- **Namespace:** `Global`
- **Assembly:** `Dew.Core.dll`
- **Inheritance / Derived:** [LogicBehaviour](/api/Global.LogicBehaviour) → `ManagerBase` → [UIManager](/api/Global.UIManager) → [UIManager](/api/Global.UIManager)

```csharp
public class LobbyUIManager : UIManager, ILogicUpdate
```

## Fields

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`lobbyEffect`** | `public GameObject lobbyEffect` |  |

## Properties

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`instance`** | `public static LobbyUIManager instance { get; }` | If you expect the instance to be null, you MUST USE softInstance in Update loops.This will call FindObjectOfType if current instance is null, which can be very expensive. |
| **`softInstance`** | `public static LobbyUIManager softInstance { get; }` |  |

## Methods

### `LogicUpdate(float)`

```csharp
public override void LogicUpdate(float dt)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `dt` | `float` |  |

### `OnStateChanged(string, string)`

```csharp
protected override void OnStateChanged(string oldState, string newState)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `oldState` | `string` |  |
| `newState` | `string` |  |

### `OpenCharacterSelection()`

```csharp
public void OpenCharacterSelection()
```
