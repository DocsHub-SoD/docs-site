# Class: MessageManager

- **Category:** <span class="cat-dot" style="--cat-color: #eab308" data-cat="Items & Economy"></span> Items & Economy
- **Namespace:** `Global`
- **Assembly:** `Dew.Core.dll`
- **Inheritance / Derived:** [LogicBehaviour](/api/Global.LogicBehaviour) → `ManagerBase` → [MessageManager](/api/Global.MessageManager)

```csharp
public class MessageManager : ManagerBase<MessageManager>, ILogicUpdate
```

## Fields (3)

::: details Click to expand Fields (3)

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`buttons`** | `public List<GameObject> buttons` |  |
| **`canvasGroup`** | `public CanvasGroup canvasGroup` |  |
| **`contentText`** | `public TextMeshProUGUI contentText` |  |

:::

## Properties (1)

::: details Click to expand Properties (1)

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`isShowingMessage`** | `public bool isShowingMessage { get; }` |  |

:::

## Methods (9)

::: details `CloseMessage(ButtonType)`

```csharp
public void CloseMessage(DewMessageSettings.ButtonType button)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `button` | [`DewMessageSettings.ButtonType`](/api/Global.DewMessageSettings) |  |

:::

::: details `CloseMessageCancel()`

```csharp
public void CloseMessageCancel()
```

:::

::: details `CloseMessageNo()`

```csharp
public void CloseMessageNo()
```

:::

::: details `CloseMessageOk()`

```csharp
public void CloseMessageOk()
```

:::

::: details `CloseMessageYes()`

```csharp
public void CloseMessageYes()
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

::: details `ShowMessage(DewMessageSettings)`

```csharp
public void ShowMessage(DewMessageSettings msg)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `msg` | [`DewMessageSettings`](/api/Global.DewMessageSettings) |  |

:::

::: details `ShowMessageLocalized(string)`

```csharp
public void ShowMessageLocalized(string id)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `id` | `string` |  |

:::
