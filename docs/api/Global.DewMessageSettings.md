# Class: DewMessageSettings

- **Category:** <span class="cat-dot" style="--cat-color: #f97316" data-cat="Data & Core Math"></span> Data & Core Math
- **Namespace:** `Global`
- **Assembly:** `Dew.Core.dll`

```csharp
public class DewMessageSettings
```

## Fields (7)

::: details Click to expand Fields (7)

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`buttons`** | `public DewMessageSettings.ButtonType buttons` |  |
| **`defaultButton`** | `public DewMessageSettings.ButtonType defaultButton` |  |
| **`destructiveConfirm`** | `public bool destructiveConfirm` |  |
| **`onClose`** | `public Action<DewMessageSettings.ButtonType> onClose` |  |
| **`owner`** | `public Object owner` | If set, the message will disappear when owner is destroyed. |
| **`rawContent`** | `public string rawContent` |  |
| **`validator`** | `public Func<bool> validator` | If this returns false, the message will be closed. |

:::


## Architecture & Relationships

::: details Click to expand Architecture & Relationships

### Used By (2)

*Classes and systems that invoke, reference, or depend on `DewMessageSettings`:*

[MessageManager](/api/Global.MessageManager) · `UI_Title_ProfileSelection_LinkEnterCodeWindow`

### Dependencies (0)

*No outgoing class dependencies recorded.*

:::
