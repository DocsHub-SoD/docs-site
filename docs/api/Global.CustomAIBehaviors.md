# Class: CustomAIBehaviors

- **Category:** <span class="cat-dot" style="--cat-color: #22c55e" data-cat="Actors & Entities"></span> Actors & Entities
- **Namespace:** `Global`
- **Assembly:** `Dew.Core.dll`

```csharp
public class CustomAIBehaviors
```

## Methods (2)

::: details `Add(CustomAIUpdate, int)`

Updates with lower priority value will be executed first. Return true on update if you want to stop execution of further AI updates.

```csharp
public void Add(CustomAIUpdate onUpdate, int priority = 0)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `onUpdate` | [`CustomAIUpdate`](/api/Global.CustomAIUpdate) |  |
| `priority` | `int` |  |

:::

::: details `Remove(CustomAIUpdate)`

```csharp
public void Remove(CustomAIUpdate onUpdate)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `onUpdate` | [`CustomAIUpdate`](/api/Global.CustomAIUpdate) |  |

:::
