# Class: CustomAIBehaviors

- **Namespace:** `Global`
- **Assembly:** `Dew.Core.dll`

```csharp
public class CustomAIBehaviors
```

## Methods

### `Add(CustomAIUpdate, int)`

Updates with lower priority value will be executed first. Return true on update if you want to stop execution of further AI updates.

```csharp
public void Add(CustomAIUpdate onUpdate, int priority = 0)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `onUpdate` | [CustomAIUpdate](/api/Global.CustomAIUpdate) |  |
| `priority` | `int` |  |

### `Remove(CustomAIUpdate)`

```csharp
public void Remove(CustomAIUpdate onUpdate)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `onUpdate` | [CustomAIUpdate](/api/Global.CustomAIUpdate) |  |
