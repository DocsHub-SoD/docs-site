# Class: MessageManager

- **Category:** <span class="cat-dot" style="--cat-color: #eab308" data-cat="Items & Economy"></span> Items & Economy
- **Namespace:** `Global`
- **Assembly:** `Dew.Core.dll`
- **Inheritance / Derived:** [LogicBehaviour](/api/Global.LogicBehaviour) → `ManagerBase` → [MessageManager](/api/Global.MessageManager)

```csharp
public class MessageManager : ManagerBase<MessageManager>, ILogicUpdate
```

## Fields

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`buttons`** | `public List<GameObject> buttons` |  |
| **`canvasGroup`** | `public CanvasGroup canvasGroup` |  |
| **`contentText`** | `public TextMeshProUGUI contentText` |  |

## Properties

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`isShowingMessage`** | `public bool isShowingMessage { get; }` |  |

## Methods

### `CloseMessage(ButtonType)`

```csharp
public void CloseMessage(DewMessageSettings.ButtonType button)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `button` | [`DewMessageSettings.ButtonType`](/api/Global.DewMessageSettings) |  |

### `CloseMessageCancel()`

```csharp
public void CloseMessageCancel()
```

### `CloseMessageNo()`

```csharp
public void CloseMessageNo()
```

### `CloseMessageOk()`

```csharp
public void CloseMessageOk()
```

### `CloseMessageYes()`

```csharp
public void CloseMessageYes()
```

### `FrameUpdate()`

```csharp
public override void FrameUpdate()
```

### `LogicUpdate(float)`

```csharp
public override void LogicUpdate(float dt)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `dt` | `float` |  |

### `ShowMessage(DewMessageSettings)`

```csharp
public void ShowMessage(DewMessageSettings msg)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `msg` | [`DewMessageSettings`](/api/Global.DewMessageSettings) |  |

### `ShowMessageLocalized(string)`

```csharp
public void ShowMessageLocalized(string id)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `id` | `string` |  |
