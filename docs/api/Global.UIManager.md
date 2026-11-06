# Class: UIManager

- **Category:** <span class="cat-dot" style="--cat-color: #ec4899" data-cat="User Interface"></span> User Interface
- **Namespace:** `Global`
- **Assembly:** `Dew.Core.dll`
- **Inheritance / Derived:** [LogicBehaviour](/api/Global.LogicBehaviour) → `ManagerBase` → [UIManager](/api/Global.UIManager) → [InGameUIManager](/api/Global.InGameUIManager) → [LobbyUIManager](/api/Global.LobbyUIManager)

```csharp
public class UIManager : ManagerBase<UIManager>, ILogicUpdate
```

## Fields (1)

::: details Click to expand Fields (1)

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`onStateChanged`** | `public SafeAction<string, string> onStateChanged` |  |

:::

## Properties (2)

::: details Click to expand Properties (2)

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`availableStates`** | `public IReadOnlyCollection<string> availableStates { get; }` |  |
| **`state`** | `public string state { get; }` |  |

:::

## Methods (4)

::: details `IsState(string)`

```csharp
public bool IsState(string state)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `state` | `string` |  |

**Returns:** `bool`

:::

::: details `OnStateChanged(string, string)`

```csharp
protected virtual void OnStateChanged(string oldState, string newState)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `oldState` | `string` |  |
| `newState` | `string` |  |

:::

::: details `SetState(string)`

```csharp
public void SetState(string newState)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `newState` | `string` |  |

:::

::: details `ShouldDoAutoFocus()`

```csharp
public virtual bool ShouldDoAutoFocus()
```

**Returns:** `bool`

:::
