# Struct: EditSkillTargetInfo

- **Namespace:** `Global`
- **Assembly:** `Dew.Core.dll`

```csharp
public struct EditSkillTargetInfo
```

## Fields

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`actionTypeRawText`** | `public string actionTypeRawText` | Text to show on action button. |
| **`cost`** | `public Cost? cost` | Providing null denotes the cost is irrelevant here.You don't need to provide rejectReason when the player cannot afford the action, |
| **`nextLevel`** | `public int? nextLevel` | Next level to show by comparison. |
| **`rejectReasonRawText`** | `public string rejectReasonRawText` | If not null, the action will be rejected and center message will be shown. You don't need to set this for the cost affordability. |
| **`tooltipRawText`** | `public string tooltipRawText` | Text to show on tooltip as a description of this action. |
