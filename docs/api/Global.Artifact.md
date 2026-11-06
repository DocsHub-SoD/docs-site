# Class: Artifact

- **Category:** <span class="cat-dot" style="--cat-color: #22c55e" data-cat="Actors & Entities"></span> Actors & Entities
- **Namespace:** `Global`
- **Assembly:** `Dew.Core.dll`
- **Inheritance / Derived:** [DewNetworkBehaviour](/api/Global.DewNetworkBehaviour) → [Actor](/api/Global.Actor)

```csharp
[DewResourceLink(ResourceLinkBy.Type)]
public class Artifact : Actor, ILogicUpdate, ICleanup, ICustomDestroyRoutine, IInteractable, ICustomInteractable
```

## Fields (3)

::: details Click to expand Fields (3)

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`icon`** | `public Sprite icon` |  |
| **`mainColor`** | `[ColorUsage(false)] public Color mainColor` |  |
| **`touchSound`** | `public DewAudioClip touchSound` |  |

:::

## Properties (11)

::: details Click to expand Properties (11)

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`altInteractProgress`** | `public float? altInteractProgress { get; }` |  |
| **`canAltInteract`** | `public bool canAltInteract { get; }` |  |
| **`canInteractWithMouse`** | `public bool canInteractWithMouse { get; }` |  |
| **`cost`** | `public Cost cost { get; }` |  |
| **`focusDistance`** | `public float focusDistance { get; }` |  |
| **`grantedStardust`** | `public int grantedStardust { get; }` |  |
| **`interactActionRawText`** | `public string interactActionRawText { get; }` |  |
| **`interactAltActionRawText`** | `public string interactAltActionRawText { get; }` |  |
| **`interactPivot`** | `public Transform interactPivot { get; }` |  |
| **`nameRawText`** | `public string nameRawText { get; }` |  |
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

::: details `OnDestroyActor()`

```csharp
protected override void OnDestroyActor()
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
