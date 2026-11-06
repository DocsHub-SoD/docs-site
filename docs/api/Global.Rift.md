# Class: Rift

- **Category:** <span class="cat-dot" style="--cat-color: #22c55e" data-cat="Actors & Entities"></span> Actors & Entities
- **Namespace:** `Global`
- **Assembly:** `Dew.Core.dll`
- **Inheritance / Derived:** [DewNetworkBehaviour](/api/Global.DewNetworkBehaviour) → [Actor](/api/Global.Actor) → [Rift_RoomExit](/api/Global.Rift_RoomExit) → [Rift_Sidetrack](/api/Global.Rift_Sidetrack)

```csharp
[DewResourceLink(ResourceLinkBy.None)]
public class Rift : Actor, ILogicUpdate, ICleanup, ICustomDestroyRoutine, IInteractable, IBanRoomNodesNearby
```

## Fields (9)

::: details Click to expand Fields (9)

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`afterOpenInteractableDelay`** | `public float afterOpenInteractableDelay` |  |
| **`chargeDuration`** | `public float chargeDuration` |  |
| **`fxActivate`** | `public GameObject fxActivate` |  |
| **`fxCharge`** | `public GameObject fxCharge` |  |
| **`fxLocked`** | `public GameObject fxLocked` |  |
| **`fxLoop`** | `public GameObject fxLoop` |  |
| **`fxOpen`** | `public GameObject fxOpen` |  |
| **`fxUnlocked`** | `public GameObject fxUnlocked` |  |
| **`softInstance`** | `public static Rift softInstance` |  |

:::

## Properties (7)

::: details Click to expand Properties (7)

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`canInteractWithMouse`** | `public bool canInteractWithMouse { get; }` |  |
| **`focusDistance`** | `public float focusDistance { get; }` |  |
| **`instance`** | `public static Rift instance { get; }` |  |
| **`interactPivot`** | `public Transform interactPivot { get; }` |  |
| **`isDestroyedOnRoomChange`** | `public override bool isDestroyedOnRoomChange { get; }` |  |
| **`isLocked`** | `[SaveVar(SaveVarFlags.Default)] public bool isLocked { get; set; }` |  |
| **`isOpen`** | `[SaveVar(SaveVarFlags.Default)] public bool isOpen { get; set; }` |  |

:::

## Methods (8)

::: details `Awake()`

```csharp
protected override void Awake()
```

:::

::: details `CanInteract(Entity)`

```csharp
public virtual bool CanInteract(Entity entity)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `entity` | [`Entity`](/api/Global.Entity) |  |

**Returns:** `bool`

:::

::: details `Close()`

```csharp
[Button]
public void Close()
```

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

::: details `OnInteractRift(Hero)`

Called on server when a hero interacts with this rift.Return true to indicate success of interaction. (Will play activate effect)

```csharp
protected virtual bool OnInteractRift(Hero hero)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `hero` | [`Hero`](/api/Global.Hero) |  |

**Returns:** `bool`

:::

::: details `Open()`

Open the rift with charging animation. If you wish to skip the animation, set the isOpen property directly.

```csharp
[Button]
public void Open()
```

:::

::: details `ShouldBeSavedWithRoom()`

```csharp
public override bool ShouldBeSavedWithRoom()
```

**Returns:** `bool`

:::
