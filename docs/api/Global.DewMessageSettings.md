# Class: DewMessageSettings

- **Namespace:** `Global`
- **Assembly:** `Dew.Core.dll`

```csharp
public class DewMessageSettings
```

## Fields

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`buttons`** | `public DewMessageSettings.ButtonType buttons` |  |
| **`defaultButton`** | `public DewMessageSettings.ButtonType defaultButton` |  |
| **`destructiveConfirm`** | `public bool destructiveConfirm` |  |
| **`onClose`** | `public Action&lt;DewMessageSettings.ButtonType&gt; onClose` |  |
| **`owner`** | `public Object owner` | If set, the message will disappear when owner is destroyed. |
| **`rawContent`** | `public string rawContent` |  |
| **`validator`** | `public Func&lt;bool&gt; validator` | If this returns false, the message will be closed. |
