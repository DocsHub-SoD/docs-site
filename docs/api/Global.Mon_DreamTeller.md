# Class: Mon_DreamTeller

- **Category:** <span class="cat-dot" style="--cat-color: #22c55e" data-cat="Actors & Entities"></span> Actors & Entities
- **Namespace:** `Global`
- **Assembly:** `Dew.Core.dll`
- **Inheritance / Derived:** [DewNetworkBehaviour](/api/Global.DewNetworkBehaviour) → [Actor](/api/Global.Actor) → [Entity](/api/Global.Entity) → [Monster](/api/Global.Monster)

```csharp
public class Mon_DreamTeller : Monster, ILogicUpdate, ICleanup, ICustomDestroyRoutine, IInteractable, IForceHeroicHealthbar
```

## Fields (2)

::: details Click to expand Fields (2)

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`fxExplode`** | `public GameObject fxExplode` |  |
| **`showStoryDelay`** | `public float showStoryDelay` |  |

:::

## Properties (5)

::: details Click to expand Properties (5)

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`canInteractWithMouse`** | `public bool canInteractWithMouse { get; }` |  |
| **`defaultOwner`** | `protected override DewPlayer defaultOwner { get; }` |  |
| **`focusDistance`** | `public float focusDistance { get; }` |  |
| **`interactPivot`** | `public Transform interactPivot { get; }` |  |
| **`priority`** | `public int priority { get; }` |  |

:::

## Methods (4)

::: details `CanInteract(Entity)`

```csharp
public bool CanInteract(Entity entity)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `entity` | [`Entity`](/api/Global.Entity) |  |

**Returns:** `bool`

:::

::: details `OnCreate()`

```csharp
protected override void OnCreate()
```

:::

::: details `OnInteract(Entity, bool)`

```csharp
public void OnInteract(Entity entity, bool alt)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `entity` | [`Entity`](/api/Global.Entity) |  |
| `alt` | `bool` |  |

:::

::: details `ShouldBeSavedWithRoom()`

```csharp
public override bool ShouldBeSavedWithRoom()
```

**Returns:** `bool`

:::


## Architecture & Relationships

::: details Click to expand Architecture & Relationships

### Used By (0)

*No incoming dependencies recorded.*

### Dependencies (16)

*Types and components that `Mon_DreamTeller` references or depends upon:*

[Actor](/api/Global.Actor) · [Artifact](/api/Global.Artifact) · [ControlManager](/api/Global.ControlManager) · [ConversationManager](/api/Global.ConversationManager) · [DewPlayer](/api/Global.DewPlayer) · [DewResources](/api/Global.DewResources) · [Entity](/api/Global.Entity) · [EntityControl](/api/Global.EntityControl) · [EntityStatus](/api/Global.EntityStatus) · [IForceHeroicHealthbar](/api/Global.IForceHeroicHealthbar) · [IInteractable](/api/Global.IInteractable) · [ManagerBase`1](/api/Global.ManagerBase`1) · [Monster](/api/Global.Monster) · `NetworkConnectionToClientExtension` · [NetworkedManagerBase`1](/api/Global.NetworkedManagerBase`1) · [QuestManager](/api/Global.QuestManager)

:::
