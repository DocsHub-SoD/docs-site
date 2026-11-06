# Class: TriggerChannelData

- **Category:** <span class="cat-dot" style="--cat-color: #ef4444" data-cat="Combat & Abilities"></span> Combat & Abilities
- **Namespace:** `Global`
- **Assembly:** `Dew.Core.dll`

```csharp
[Serializable]
public class TriggerChannelData
```

## Fields

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`blockedActions`** | `[HorizontalGroup("A", 0, 0, 0, 0)] [HideLabel] [DisableIf("@duration <= 0f")] public Channel.BlockedAction blockedActions` |  |
| **`duration`** | `[HorizontalGroup("A", 0, 0, 0, 0)] [LabelText("Channel Duration")] public float duration` |  |

## Methods

### `CreateChannel(Action, Action, IEntityValidator, Entity, IBinaryEntityValidator)`

Create a channel out of this data.

```csharp
public Channel CreateChannel(Action onComplete, Action onCancel, IEntityValidator selfValidator, Entity target, IBinaryEntityValidator targetValidator)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `onComplete` | `System.Action` |  |
| `onCancel` | `System.Action` |  |
| `selfValidator` | [`IEntityValidator`](/api/Global.IEntityValidator) |  |
| `target` | [`Entity`](/api/Global.Entity) |  |
| `targetValidator` | [`IBinaryEntityValidator`](/api/Global.IBinaryEntityValidator) |  |

**Returns:** `Channel`

### `CreateChannel(Action, Action, IEntityValidator)`

Create a channel out of this data.

```csharp
public Channel CreateChannel(Action onComplete, Action onCancel, IEntityValidator selfValidator)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `onComplete` | `System.Action` |  |
| `onCancel` | `System.Action` |  |
| `selfValidator` | [`IEntityValidator`](/api/Global.IEntityValidator) |  |

**Returns:** `Channel`
