# Class: DewInputTrigger

- **Category:** <span class="cat-dot" style="--cat-color: #64748b" data-cat="Misc & Utility"></span> Misc & Utility
- **Namespace:** `Global`
- **Assembly:** `Dew.Core.dll`

```csharp
public class DewInputTrigger
```

## Fields (8)

::: details Click to expand Fields (8)

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`binding`** | `public Func<DewBinding> binding` |  |
| **`canConsume`** | `public bool canConsume` |  |
| **`checkGameAreaForMouse`** | `public bool checkGameAreaForMouse` |  |
| **`ignoreConsumeCheck`** | `public bool ignoreConsumeCheck` |  |
| **`isValidCheck`** | `public Func<bool> isValidCheck` |  |
| **`MockTrigger`** | `public static DewInputTrigger MockTrigger` |  |
| **`owner`** | `public Object owner` |  |
| **`priority`** | `public int priority` | Lower will be checked first. |

:::

## Properties (3)

::: details Click to expand Properties (3)

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`down`** | `public bool down { get; }` |  |
| **`downRepeated`** | `public bool downRepeated { get; }` |  |
| **`up`** | `public bool up { get; }` |  |

:::
