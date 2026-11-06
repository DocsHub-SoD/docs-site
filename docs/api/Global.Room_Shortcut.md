# Class: Room_Shortcut

- **Category:** <span class="cat-dot" style="--cat-color: #3b82f6" data-cat="Managers & Systems"></span> Managers & Systems
- **Namespace:** `Global`
- **Assembly:** `Dew.Core.dll`
- **Inheritance / Derived:** [DewNetworkBehaviour](/api/Global.DewNetworkBehaviour)

```csharp
public class Room_Shortcut : DewNetworkBehaviour, ILogicUpdate, IInteractable, ICustomInteractable, IPlayerPathablePoint
```

## Fields (6)

::: details Click to expand Fields (6)

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`closedEffect`** | `public GameObject closedEffect` |  |
| **`isOpen`** | `[SyncVar] public bool isOpen` |  |
| **`openEffect`** | `public GameObject openEffect` |  |
| **`targetShortcut`** | `public Room_Shortcut targetShortcut` |  |
| **`walkEndPos`** | `public Transform walkEndPos` |  |
| **`walkStartPos`** | `public Transform walkStartPos` |  |

:::

## Properties (2)

::: details Click to expand Properties (2)

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`altInteractProgress`** | `public float? altInteractProgress { get; }` |  |
| **`cost`** | `public Cost cost { get; }` |  |

:::

## Methods (3)

::: details `Close()`

```csharp
public void Close()
```

:::

::: details `OnStartClient()`

```csharp
public override void OnStartClient()
```

:::

::: details `Open()`

```csharp
public void Open()
```

:::


## Architecture & Relationships

::: details Click to expand Architecture & Relationships

### Used By (1)

*Classes and systems that invoke, reference, or depend on `Room_Shortcut`:*

`Se_UsingShortcut`

### Dependencies (13)

*Types and components that `Room_Shortcut` references or depends upon:*

[Actor](/api/Global.Actor) · [Cost](/api/Global.Cost) · [Dew](/api/Global.Dew) · [DewGizmos](/api/Global.DewGizmos) · [DewLocalization](/api/Global.DewLocalization) · [DewNetworkBehaviour](/api/Global.DewNetworkBehaviour) · [DewPlayer](/api/Global.DewPlayer) · [Entity](/api/Global.Entity) · [EntityStatus](/api/Global.EntityStatus) · [Hero](/api/Global.Hero) · [ICustomInteractable](/api/Global.ICustomInteractable) · [IInteractable](/api/Global.IInteractable) · [IPlayerPathablePoint](/api/Global.IPlayerPathablePoint)

:::
