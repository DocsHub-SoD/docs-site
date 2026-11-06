# Class: Mon_DreamTeller

- **Category:** <span class="cat-dot" style="--cat-color: #22c55e" data-cat="Actors & Entities"></span> Actors & Entities
- **Namespace:** `Global`
- **Assembly:** `Dew.Core.dll`
- **Inheritance / Derived:** [DewNetworkBehaviour](/api/Global.DewNetworkBehaviour) → [Actor](/api/Global.Actor) → [Entity](/api/Global.Entity) → [Monster](/api/Global.Monster)

```csharp
public class Mon_DreamTeller : Monster, ILogicUpdate, ICleanup, ICustomDestroyRoutine, IInteractable, IForceHeroicHealthbar
```

## Fields

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`fxExplode`** | `public GameObject fxExplode` |  |
| **`showStoryDelay`** | `public float showStoryDelay` |  |

## Properties

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`canInteractWithMouse`** | `public bool canInteractWithMouse { get; }` |  |
| **`defaultOwner`** | `protected override DewPlayer defaultOwner { get; }` |  |
| **`focusDistance`** | `public float focusDistance { get; }` |  |
| **`interactPivot`** | `public Transform interactPivot { get; }` |  |
| **`priority`** | `public int priority { get; }` |  |

## Methods

### `CanInteract(Entity)`

```csharp
public bool CanInteract(Entity entity)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `entity` | [`Entity`](/api/Global.Entity) |  |

**Returns:** `bool`

### `OnCreate()`

```csharp
protected override void OnCreate()
```

### `OnInteract(Entity, bool)`

```csharp
public void OnInteract(Entity entity, bool alt)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `entity` | [`Entity`](/api/Global.Entity) |  |
| `alt` | `bool` |  |

### `ShouldBeSavedWithRoom()`

```csharp
public override bool ShouldBeSavedWithRoom()
```

**Returns:** `bool`
