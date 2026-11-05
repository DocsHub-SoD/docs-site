# Class: UIManager

- **Namespace:** `Global`
- **Assembly:** `Dew.Core.dll`
- **Inheritance / Derived:** [LogicBehaviour](/api/Global.LogicBehaviour) → `ManagerBase` → [UIManager](/api/Global.UIManager) → [InGameUIManager](/api/Global.InGameUIManager) → [LobbyUIManager](/api/Global.LobbyUIManager)

```csharp
public class UIManager : ManagerBase<UIManager>, ILogicUpdate
```

## Fields

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`onStateChanged`** | `public SafeAction&lt;string, string&gt; onStateChanged` |  |

## Properties

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`availableStates`** | `public IReadOnlyCollection&lt;string&gt; availableStates { get; }` |  |
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
