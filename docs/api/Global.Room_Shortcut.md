# Class: Room_Shortcut

- **Category:** <span class="cat-dot" style="--cat-color: #3b82f6" data-cat="Managers & Systems"></span> Managers & Systems
- **Namespace:** `Global`
- **Assembly:** `Dew.Core.dll`
- **Inheritance / Derived:** [DewNetworkBehaviour](/api/Global.DewNetworkBehaviour)

```csharp
public class Room_Shortcut : DewNetworkBehaviour, ILogicUpdate, IInteractable, ICustomInteractable, IPlayerPathablePoint
```

## Fields

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`closedEffect`** | `public GameObject closedEffect` |  |
| **`isOpen`** | `public bool isOpen` |  |
| **`openEffect`** | `public GameObject openEffect` |  |
| **`targetShortcut`** | `public Room_Shortcut targetShortcut` |  |
| **`walkEndPos`** | `public Transform walkEndPos` |  |
| **`walkStartPos`** | `public Transform walkStartPos` |  |

## Properties

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`altInteractProgress`** | `public float? altInteractProgress { get; }` |  |
| **`cost`** | `public Cost cost { get; }` |  |

## Methods

### `Close()`

```csharp
public void Close()
```

### `OnStartClient()`

```csharp
public override void OnStartClient()
```

### `Open()`

```csharp
public void Open()
```
