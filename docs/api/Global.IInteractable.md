# Interface: IInteractable

- **Category:** <span class="cat-dot" style="--cat-color: #f97316" data-cat="Data & Core Math"></span> Data & Core Math
- **Namespace:** `Global`
- **Assembly:** `Dew.Core.dll`

```csharp
public interface IInteractable
```

## Properties (4)

::: details Click to expand Properties (4)

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`canInteractWithMouse`** | `bool canInteractWithMouse { get; }` |  |
| **`focusDistance`** | `float focusDistance { get; }` |  |
| **`interactPivot`** | `Transform interactPivot { get; }` |  |
| **`priority`** | `int priority { get; }` | Lower values are prioritized |

:::

## Methods (2)

::: details `CanInteract(Entity)`

Can this object be interacted by given entity? Checked everywhere, hence this should return consistent results regardless of caller.

```csharp
bool CanInteract(Entity entity)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `entity` | [`Entity`](/api/Global.Entity) |  |

**Returns:** `bool`

:::

::: details `OnInteract(Entity, bool)`

Called everywhere when an entity interacts with an interactable.

```csharp
void OnInteract(Entity entity, bool alt)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `entity` | [`Entity`](/api/Global.Entity) |  |
| `alt` | `bool` |  |

:::
