# Class: UIManager

- **Category:** <span class="cat-dot" style="--cat-color: #ec4899" data-cat="User Interface"></span> User Interface
- **Namespace:** `Global`
- **Assembly:** `Dew.Core.dll`
- **Inheritance / Derived:** [LogicBehaviour](/api/Global.LogicBehaviour) → `ManagerBase` → [UIManager](/api/Global.UIManager) → [InGameUIManager](/api/Global.InGameUIManager) → [LobbyUIManager](/api/Global.LobbyUIManager)

```csharp
public class UIManager : ManagerBase<UIManager>, ILogicUpdate
```

## Fields

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`onStateChanged`** | `public SafeAction<string, string> onStateChanged` |  |

## Properties

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`availableStates`** | `public IReadOnlyCollection<string> availableStates { get; }` |  |
| **`state`** | `public string state { get; }` |  |

## Methods

### `IsState(string)`

```csharp
public bool IsState(string state)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `state` | `string` |  |

**Returns:** `bool`

### `OnStateChanged(string, string)`

```csharp
protected virtual void OnStateChanged(string oldState, string newState)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `oldState` | `string` |  |
| `newState` | `string` |  |

### `SetState(string)`

```csharp
public void SetState(string newState)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `newState` | `string` |  |

### `ShouldDoAutoFocus()`

```csharp
public virtual bool ShouldDoAutoFocus()
```

**Returns:** `bool`
