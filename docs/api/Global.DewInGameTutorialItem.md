# Class: DewInGameTutorialItem

- **Namespace:** `Global`
- **Assembly:** `Dew.Core.dll`

```csharp
public class DewInGameTutorialItem
```

## Properties

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`isActive`** | `public bool isActive { get; }` |  |
| **`mgr`** | `public InGameTutorialManager mgr { get; set; }` |  |

## Methods

### `OnStart()`

```csharp
public virtual void OnStart()
```

### `OnStop()`

```csharp
public virtual void OnStop()
```

### `TutComplete()`

```csharp
protected void TutComplete()
```

### `TutCreateArrow()`

```csharp
protected TutorialArrow TutCreateArrow()
```

**Returns:** `TutorialArrow`

### `TutDelayedExecution(Action, float)`

```csharp
protected void TutDelayedExecution(Action func, float seconds)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `func` | `System.Action` |  |
| `seconds` | `float` |  |

### `TutGetCoroutiner()`

```csharp
protected Coroutiner TutGetCoroutiner()
```

**Returns:** `Coroutiner`

### `TutOnFrameUpdate(Action)`

```csharp
protected void TutOnFrameUpdate(Action func)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `func` | `System.Action` |  |

### `TutOnLogicUpdate(Action)`

```csharp
protected void TutOnLogicUpdate(Action func)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `func` | `System.Action` |  |

### `TutOnOutOfCombat(Action)`

```csharp
protected void TutOnOutOfCombat(Action func)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `func` | `System.Action` |  |
