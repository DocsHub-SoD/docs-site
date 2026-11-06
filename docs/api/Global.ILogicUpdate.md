# Interface: ILogicUpdate

- **Category:** <span class="cat-dot" style="--cat-color: #64748b" data-cat="Misc & Utility"></span> Misc & Utility
- **Namespace:** `Global`
- **Assembly:** `Dew.Core.dll`

```csharp
public interface ILogicUpdate
```

## Methods (2)

::: details `FrameUpdate()`

```csharp
void FrameUpdate()
```

:::

::: details `LogicUpdate(float)`

```csharp
void LogicUpdate(float dt)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `dt` | `float` |  |

:::


## Architecture & Relationships

::: details Click to expand Architecture & Relationships

### Used By (4)

*Classes and systems that invoke, reference, or depend on `ILogicUpdate`:*

[DewNetworkBehaviour](/api/Global.DewNetworkBehaviour) · `ILogicUpdateNullCheckExtension` · [LogicBehaviour](/api/Global.LogicBehaviour) · [LogicUpdateManager](/api/Global.LogicUpdateManager)

### Dependencies (0)

*No outgoing class dependencies recorded.*

:::
