# Class: DewInputTrigger

- **Namespace:** `Global`
- **Assembly:** `Dew.Core.dll`

```csharp
public class DewInputTrigger
```

## Fields

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`binding`** | `public Func&lt;DewBinding&gt; binding` |  |
| **`canConsume`** | `public bool canConsume` |  |
| **`checkGameAreaForMouse`** | `public bool checkGameAreaForMouse` |  |
| **`ignoreConsumeCheck`** | `public bool ignoreConsumeCheck` |  |
| **`isValidCheck`** | `public Func&lt;bool&gt; isValidCheck` |  |
| **`MockTrigger`** | `public static DewInputTrigger MockTrigger` |  |
| **`owner`** | `public Object owner` |  |
| **`priority`** | `public int priority` | Lower will be checked first. |

## Properties

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`down`** | `public bool down { get; }` |  |
| **`downRepeated`** | `public bool downRepeated { get; }` |  |
| **`up`** | `public bool up { get; }` |  |
