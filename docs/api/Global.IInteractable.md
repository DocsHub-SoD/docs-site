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


## Architecture & Relationships

::: details Click to expand Architecture & Relationships

### Used By (27)

*Classes and systems that invoke, reference, or depend on `IInteractable`:*

[ActionInteract](/api/Global.ActionInteract) · [Artifact](/api/Global.Artifact) · [CameraManager](/api/Global.CameraManager) · [ControlManager](/api/Global.ControlManager) · [EditSkillManager](/api/Global.EditSkillManager) · [Entity](/api/Global.Entity) · [EntityControl](/api/Global.EntityControl) · [Gem](/api/Global.Gem) · `IInteractableUnityNullCheckExtension` · [Mon_DreamTeller](/api/Global.Mon_DreamTeller) · `Mon_Polaris` · `NetworkReaderWriterExtensions` · [PingInstance](/api/Global.PingInstance) · [PingManager](/api/Global.PingManager) · [PropEnt_Merchant_Base](/api/Global.PropEnt_Merchant_Base) · [ProxyCollider](/api/Global.ProxyCollider) · [Rift](/api/Global.Rift) · [Room_Shortcut](/api/Global.Room_Shortcut) · [Shrine](/api/Global.Shrine) · `Shrine_Stardust` · [SkillTrigger](/api/Global.SkillTrigger) · `SnowMountain_SecretPlaceTriggerInstance` · `SpawnGemStarProp` · `UI_InGame_InteractGroup` · `UI_InGame_Interact_Base` · `UI_InGame_Interact_Rift` · `UI_TooltipManager`

### Dependencies (1)

*Types and components that `IInteractable` references or depends upon:*

[Entity](/api/Global.Entity)

:::
